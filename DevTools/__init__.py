
import contextlib
import importlib
import json
import os
import sys
import traceback
import mods_base
from unrealsdk import logging, find_class, unreal
from pathlib import Path
from typing import Collection
import zipfile
from mods_base import ENGINE, build_mod, command
from argparse import Namespace
from typing import Any

EXTRA_FOLDERS_ENV_VAR: str = "OAK_MOD_MANAGER_EXTRA_FOLDERS"

def get_all_mod_folders() -> Collection[Path]:
    """
    Gets all mod folders to try import from, including extra folders defined via env var.

    Returns:
        A collection of mod folder paths.
    """

    extra_folders = []
    with contextlib.suppress(json.JSONDecodeError, TypeError):
        extra_folders = [Path(x) for x in json.loads(os.environ.get(EXTRA_FOLDERS_ENV_VAR, ""))]

    return [Path(__file__).parent, *extra_folders]


def validate_folder_in_mods_folder(folder: Path) -> bool:
    """
    Checks if a folder inside the mods folder is actually a mod we should try import.

    Args:
        folder: The folder to analyse.
    Returns:
        True if the file is a valid module to try import.
    """
    if folder.name == "__pycache__":
        return False

    # A lot of people accidentally extract into double nested folders - they have a
    # `sdk_mods/MyCoolMod/MyCoolMod/__init__.py` instead of a `sdk_mods/MyCoolMod/__init__.py`
    # Usually this silently fails - we import `MyCoolMod` but there's nothing there
    # Detect this and give a proper error message
    if not (folder / "__init__.py").exists() and (folder / folder.name / "__init__.py").exists():
        logging.error(
            f"'{folder.name}' appears to be double nested, which may prevent it from being it from"
            f" being loaded. Move the inner folder up a level.",
        )
        # Since it's a silent error, may as well continue in case it's actually what you wanted

    # In the case we have a `sdk_mods/My Cool Mod v1.2`, python will try import `My Cool Mod v1`
    # first, and fail when it doesn't exist. Try detect this to throw a better error.
    # When this happens we're likely also double nested - `sdk_mods/My Cool Mod v1.2/MyCoolMod`
    # - but we can't detect that as easily, and the problem's the same anyway
    if "." in folder.name:
        logging.error(
            f"'{folder.name}' is not a valid python module - have you extracted the right folder?",
        )
        return False

    return True


def validate_file_in_mods_folder(file: Path) -> bool:
    """
    Checks if a folder inside the mods folder is actually a mod we should try import.

    Sets up sys.path as required.

    Args:
        file: The file to analyse.
    Returns:
        True if the file is a valid .sdkmod to try import.
    """
    match file.suffix.lower():
        # Since hotfix mods can be any text file, this won't be exhaustive, but match and warn
        # about what we can
        # OHL often uses .url files to download the latest version of a mod, so also match that
        case ".bl3hotfix" | ".wlhotfix" | ".url":
            logging.error(
                f"'{file.name}' appears to be a hotfix mod, not an SDK mod. Move it to your hotfix"
                f" mods folder.",
            )
            return False

        case ".sdkmod":
            # Handled below
            pass

        case _:
            return False

    valid_zip: bool
    try:
        zip_iter = zipfile.Path(file).iterdir()
        zip_entry = next(zip_iter)
        valid_zip = zip_entry.name == file.stem and next(zip_iter, None) is None
    except (zipfile.BadZipFile, StopIteration, OSError):
        valid_zip = False

    if not valid_zip:
        logging.error(
            f"'{file.name}' does not appear to be valid, and has been ignored.",
        )
        logging.dev_warning(
            "'.sdkmod' files must be a zip, and may only contain a single root folder, which must"
            " be named the same as the zip (excluding suffix).",
        )
        return False

    sys.path.append(str(file))

    return True


def find_mods_to_import(mod_folders: Collection[Path]) -> Collection[str]:
    """
    Given a collection of mod folders, find the individual mod modules within it to try import.

    Sets up sys.path for `.sdkmod` mods.

    Returns:
        A collection of the module names to import.
    """
    mods_to_import: list[str] = []

    for folder in mod_folders:
        if not folder.exists():
            continue

        for entry in folder.iterdir():
            if entry.name.startswith("."):
                continue

            if entry.is_dir() and validate_folder_in_mods_folder(entry):
                mods_to_import.append(entry.name)

            elif entry.is_file() and validate_file_in_mods_folder(entry):
                mods_to_import.append(entry.stem)

    return mods_to_import

def import_mod(mods_to_import: Collection[str], mod: str) -> None:
    """
    Tries to import a list of mods.

    Args:
        mods_to_import: The list of mods to import.
    """
    if mod not in mods_to_import:
        logging.error(f"Failed to find mod '{mod}' to import")
        return
    try:
        importlib.import_module(mod)
    except Exception as ex:  # noqa: BLE001
        logging.error(f"Failed to import mod '{mod}'")

        tb = traceback.extract_tb(ex.__traceback__)[-1:]

        logging.error("".join(traceback.format_exception_only(ex)))
        logging.error("".join(traceback.format_list(tb)))

@command(splitter=lambda line: [line.strip()])
def load_mod(args: Namespace) -> None:
    import_mod(find_mods_to_import(get_all_mod_folders()), args.mod)
    print(f"Loaded mod '{args.mod}'")

load_mod.add_argument("mod", help="The mod to load")

@command(splitter=lambda line: [line.strip()])
def unload_mod(args: Namespace) -> None:
    mods = mods_base.get_ordered_mod_list()
    for mod in mods:
        if mod.module_name == args.mod:
            mods_base.deregister_mod(mod)
            modules_to_remove = [module for module in sys.modules if module.startswith(args.mod)]
            for module in modules_to_remove:
                del sys.modules[module]
            logging.info(f"Killed mod '{mod.name}'")

unload_mod.add_argument("mod", help="The mod to kill")

@command(splitter=lambda line: [line.strip()])
def reload_mod(args: Namespace) -> None:
    mods = mods_base.get_ordered_mod_list()
    for mod in mods:
        if mod.module_name == args.mod:
            mods_base.deregister_mod(mod)
            modules_to_remove = [module for module in sys.modules if module.startswith(args.mod)]
            for module in modules_to_remove:
                del sys.modules[module]
            import_mod(find_mods_to_import(get_all_mod_folders()), args.mod)
            logging.info(f"Reloaded mod '{mod.name}'")

reload_mod.add_argument("mod", help="The mod to reload")

@command()
def list_mods(_: Namespace) -> None:
    mods = mods_base.get_ordered_mod_list()
    for mod in mods:
        logging.info(f"{mod.name} : {mod.module_name}")

build_mod(
    mod_type=mods_base.ModType.Library
)
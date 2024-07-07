import sys
import zipfile
from pathlib import Path

def main():
    parent_dir = Path(__file__).resolve().parent

    # Check if the script is run with the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python sdkmod.py <mod_name>")
        sys.exit(1)

    # Get the paths to the mod directory and the output file
    mod_name = sys.argv[1]
    mod_dir = parent_dir / mod_name
    output_file = parent_dir / f"{mod_name}.sdkmod"

    # Check if the mod directory exists
    if not mod_dir.exists():
        print(f"Directory '{mod_name}' does not exist")
        sys.exit(1)

    # delete the `__pycache__` directory
    pycache_dir = mod_dir / "__pycache__"
    if pycache_dir.exists():
        for pycache_file in pycache_dir.iterdir():
            pycache_file.unlink()
        pycache_dir.rmdir()

    # Create a zip file with the contents of the mod directory
    with zipfile.ZipFile(output_file, "w") as zf:
        for file in mod_dir.rglob("*"):
            zf.write(file, file.relative_to(mod_dir))

    print(f"Mod '{mod_name}' has been created at '{output_file}'")

if __name__ == "__main__":
    main()
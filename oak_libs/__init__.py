
from typing import TypeVar, cast
from bl3.engine import KismetMathLibrary, KismetStringLibrary, KismetSystemLibrary, KismetTextLibrary
from bl3.gameplay_tags import BlueprintGameplayTagLibrary
from bl3.gbx_abilities import GbxAbilityResourceControllerBlueprintFunctionLibrary
from bl3.gbx_ai import SpawnBlueprintLibrary
from bl3.gbx_blueprint_function_libraries import TagsFunctionLibrary
from bl3.gbx_camera_modes import CameraModesFunctionLibrary
from bl3.gbx_dialog import GbxDialogBlueprintLibrary
from bl3.gbx_game_system_core import DamageInfoFunctionLibrary, DamageStatics, GbxAttributeFunctionLibrary, GbxDataTableFunctionLibrary, GbxGameStatsBlueprintLibrary, GbxGameSystemCoreBlueprintLibrary, GbxGameplayStatics
from bl3.gbx_inventory import InventoryBlueprintLibrary
from bl3.oak_game import MayhemModeFunctionLibrary, OakBlueprintLibrary, OakStatusEffectsStatics
from unrealsdk import find_class

T = TypeVar("T")

def __get_static(cls: type[T]) -> T:
    return cast(T, find_class(cls.__qualname__.split(".")[0]))


OAK = __get_static(OakBlueprintLibrary)
ATTRIBUTE = __get_static(GbxAttributeFunctionLibrary)
GAMEPLAY_STATICS = __get_static(GbxGameplayStatics)
MAYHEM_MODE = __get_static(MayhemModeFunctionLibrary)
DATA_TABLE = __get_static(GbxDataTableFunctionLibrary)
GAME_SYSTEM_CORE = __get_static(GbxGameSystemCoreBlueprintLibrary)
INVENTORY = __get_static(InventoryBlueprintLibrary)
GAME_STATS = __get_static(GbxGameStatsBlueprintLibrary)
GAMEPLAY_TAG = __get_static(BlueprintGameplayTagLibrary)
TAG = __get_static(TagsFunctionLibrary)
ABILITY_RESOURCE_CONTROLLER = __get_static(GbxAbilityResourceControllerBlueprintFunctionLibrary)
SPAWNER = __get_static(SpawnBlueprintLibrary)
CAMERA_MODE = __get_static(CameraModesFunctionLibrary)
DIALOG = __get_static(GbxDialogBlueprintLibrary)
STATUS_EFFECT = __get_static(OakStatusEffectsStatics)
DAMAGE = __get_static(DamageStatics)
DAMAGE_INFO = __get_static(DamageInfoFunctionLibrary)

KISMET_MATH = __get_static(KismetMathLibrary)
KISMET_STRING = __get_static(KismetStringLibrary)
KISMET_SYSTEM = __get_static(KismetSystemLibrary)
KISMET_TEXT = __get_static(KismetTextLibrary)



import mods_base
mods_base.build_mod(
    cls=mods_base.Library,
    mod_type=mods_base.ModType.Library,
    auto_enable=True,
)
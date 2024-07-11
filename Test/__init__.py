from typing import Any, cast
from mods_base import build_mod, ModType, hook, command
from thoth import periodic
from unrealsdk.unreal import UObject, WrappedStruct, BoundFunction
from unrealsdk import find_all

# /Script/OakGame.OakPlayerController:ServerLostLootChanged
# /Script/OakGame.OakPlayerController:ServerSetMaxSpawnCost
# /Script/OakGame.OakPlayerController:ServerSetReadyForSaveGameChannel

@hook("/Game/Common/_Design/BPCont_Player.BPCont_Player_C:UserConstructionScript")
def test_hook(_1, _2, _3, _4):
    print([x.Name for x in find_all("OakSaveGame", True)])

@command()
def test(_):
    print([x.Name for x in find_all("SaveGame", False) if not "Default" in x.Name])


build_mod(
    mod_type=ModType.Library,
    auto_enable=True,
)
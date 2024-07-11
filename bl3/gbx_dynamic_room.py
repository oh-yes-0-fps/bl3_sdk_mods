from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import gbx_runtime
from . import gbx_game_system_core


class DynamicRoomBase(engine.Actor):
    SelectableLevels: unreal.WrappedArray[DynamicRoomBaseData]
    bShowRandomRoomOnStartup: bool
    OnRoomLoaded: Any
    OnRoomUnloaded: Any
    OnRoomVisible: Any
    OnRoomVisibleForAllPlayers: Any
    RoomInfoToLoad: DynamicRoomReplicationInfo
    InstanceInfo: DynamicRoomInstanceInfo
    SpriteComponent: engine.BillboardComponent
    CachedRoomDataReference: DynamicRoomBaseData

    def VisibleForAllPlayers(self) -> bool: ...
    def UnloadRoom(self): ...
    def SelectedRoomVisible(self): ...
    def SelectedRoomLoaded(self): ...
    def SelectedRoomClassLoaded(self): ...
    def OnRep_RoomInfoToLoad(self, OldRoomInfoToLoad: DynamicRoomReplicationInfo): ...
    def InstanceRoom(self, RoomToLoad: DynamicRoomBaseData): ...
    def InstanceRandomRoom(self): ...
    def GetPlayersInLevel(
        self, Players: unreal.WrappedArray[gbx_game_system_core.GbxCharacter]
    ): ...
    def GetCurrentRoomData(self) -> DynamicRoomBaseData: ...
    def GetAvailableRoomData(
        self, AvailableRooms: unreal.WrappedArray[DynamicRoomBaseData]
    ): ...
    def AllPlayerVisibilityTest(self): ...


class DynamicRoomBaseData(gbx_runtime.GbxDataAsset):
    DisplayName: str
    Description: str
    PreviewPicture: Any


class DynamicRoomLevelData(DynamicRoomBaseData):
    DynamicRoomAssetName: core_uobject.SoftObjectPath


class DynamicRoomActor(engine.Actor): ...


class DynamicRoomActorData(DynamicRoomBaseData):
    DynamicRoomAssetName: core_uobject.SoftClassPath

    def HandleDynamicRoomActorSpawned(
        self, SpawnedActor: engine.Actor, InstanceIndex: int
    ): ...


class DynamicRoomModuleSettings(unreal.UObject): ...


class DynamicRoomReplicationInfo:
    RoomToLoad: DynamicRoomBaseData
    RoomUniqueIndex: int
    RoomLoadedOnHost: bool


class DynamicRoomInstanceInfo:
    RoomUniqueName: str
    LoadingData: unreal.UObject
    RoomInstance: unreal.UObject

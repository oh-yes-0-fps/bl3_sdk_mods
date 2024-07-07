from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine
from . import umg
from . import online_subsystem_utils
from . import gbx_runtime
from . import gbx_game_system_core
from . import gbx_ui



class TravelGraph(unreal.UObject):
    InitialStation: TravelStationData
    GraphDisplayName: str
    DLCExpansionData: online_subsystem_utils.DownloadableContentData
    ExternalLinksToOtherLevel: unreal.WrappedArray[ExternalGraphLevelLinks]



class GlobalTravelGraph(TravelGraph):

    def DebugFindClosestLevel(self, WorldContextObject: unreal.UObject, StartingLevel: gbx_game_system_core.LevelData, DestinationLevel: gbx_game_system_core.LevelData): ...


class TravelStationTracker(engine.Actor):
    ResurrectTravelStations: unreal.WrappedArray[TravelStationResurrectComponent]
    LevelTravelStations: unreal.WrappedArray[LevelTravelStationComponent]
    FastTravelStations: unreal.WrappedArray[FastTravelStationComponent]
    AllFastTravelStations: unreal.WrappedArray[FastTravelStationData]
    ActiveFastTravelStations: unreal.WrappedArray[ActiveFastTravelData]
    HostFastTravelStations: unreal.WrappedArray[FastTravelStationData]
    LastActiveTravelToStation_Client: engine.Actor
    LastTravelledThroughStation: engine.Actor
    LastActiveTravelToStation_Server: engine.Actor
    LevelArrivalTravelStation: engine.Actor
    LastDestinationTravelStationName: str
    TravelToStationCountdown: TravelCountdownInfo
    GlobalTravelGraph: GlobalTravelGraph
    def TravelToStationTimer(self): ...
    def PlayerJoinedTimer(self): ...
    def OnRep_TravelToStationCountdown(self): ...
    def OnRep_LastActiveTravelToStation(self): ...
    def OnRep_HostFastTravelStations(self): ...
    def GetTravelStationComponent(self, TravelStationData: TravelStationData, ReturnValue: TravelStationComponentBase) -> TravelStationComponentBase: ...
    def GetLastTravelledThroughStation(self, ReturnValue: engine.Actor) -> engine.Actor: ...
    def GetLastActiveTravelToStation(self, pc: engine.PlayerController, ReturnValue: engine.Actor) -> engine.Actor: ...
    def GetFastTravelStationInfo(self, FastTravelStationName: str, ReturnValue: FastTravelStationData) -> FastTravelStationData: ...
    def GetAllFastTravelStations(self, ReturnValue: unreal.WrappedArray[FastTravelStationData]) -> unreal.WrappedArray[FastTravelStationData]: ...
    def GetActiveFastTravelStationList(self, ReturnValue: unreal.WrappedArray[ActiveFastTravelData]) -> unreal.WrappedArray[ActiveFastTravelData]: ...
    def FindFastTravelStationForMap(self, MapName: str, ReturnValue: FastTravelStationData) -> FastTravelStationData: ...


class TravelStationComponentBase(engine.PrimitiveComponent):
    TravelDataSelection: str
    TravelDataClassName: str
    def TravelToStation(self, WorldContextObject: unreal.UObject, DestinationStationData: TravelStationData, bImmediate: bool, ActivatingPawn: engine.Pawn, bDisallowLocalTravel: bool, ReturnValue: bool) -> bool: ...
    def GetAvailableSpawnLocation(self, ActorForSpawnLocation: engine.Actor, SpawnLocation: core_uobject.Vector, SpawnRotation: core_uobject.Rotator, bTestOnly: bool, bForVehicle: bool, ReturnValue: bool) -> bool: ...
    def EnumerateValidTravelStation(self, TravelStationObject: unreal.UObject, OutItems: unreal.WrappedArray[str]): ...


class FastTravelStationComponent(TravelStationComponentBase):
    FastTravelData: FastTravelStationData
    def OnTravelStationActivated(self, PreviousStation: engine.Actor): ...
    def FastTravelToStation(self, WorldContextObject: unreal.UObject, DestinationStationData: FastTravelStationData, ActivatingPawn: engine.Pawn): ...
    def DeactivateFastTravel(self, FallbackLocation: FastTravelStationComponent, ReturnValue: bool) -> bool: ...
    def ActivateFastTravel(self, ReturnValue: bool) -> bool: ...


class TravelLocationData(gbx_runtime.GbxDataAsset): ...


class TravelStationData(TravelLocationData):
    StationMapName: str
    Dependencies: unreal.WrappedArray[gbx_runtime.GbxCondition]
    DisplayName: str
    DisplayUIName: gbx_game_system_core.GbxUIName
    Description: str
    DescriptionUI: gbx_game_system_core.GbxUIName
    def GetStationMapName(self, ReturnValue: str) -> str: ...


class FastTravelStationData(TravelStationData):
    TravelDirection: EFastTravelDirection
    PlanetTransform: core_uobject.Transform
    bDiscoveredByDefault: bool



class FastTravelStationDebugButton(gbx_ui.GbxUserWidget):
    StationButton: umg.BUTTON
    DescriptionText: umg.TextBlock
    ButtonSelectedColor: core_uobject.LinearColor
    ButtonUnSelectedColor: core_uobject.LinearColor
    def OnStationClicked(self): ...


class FastTravelStationDebugMenu(gbx_ui.GbxDebugMenuSubmenu):
    TravelButton: umg.BUTTON
    ActiveStationsButton: umg.CheckBox
    ShowLevelStationsButton: umg.CheckBox
    TravelStationList: umg.ScrollBox
    ErrorText: umg.TextBlock
    OptionButtonClass: unreal.UClass
    AllFastTravelStations: unreal.WrappedArray[AvailableTravelStation]
    AvailableFastTravelStations: unreal.WrappedArray[AvailableTravelStation]
    AllLevelTravelStations: unreal.WrappedArray[AvailableTravelStation]
    ShowAllFastTravelStations: bool
    def OnTravelStationSelectedChanged(self, TriggeredButton: FastTravelStationDebugButton, bIsChecked: bool): ...
    def OnTravelButtonClicked(self): ...
    def OnShowLevelStationsStateChanged(self, bIsChecked: bool): ...
    def OnActiveStationsStateChanged(self, bIsChecked: bool): ...


class LevelTravelStationComponent(TravelStationComponentBase):
    LevelTravelData: LevelTravelStationData
    LevelTravelDataList: unreal.WrappedArray[TravelDataConditional]
    TextRenderEvalRate: float
    def GetLevelTravelStationData(self, ReturnValue: LevelTravelStationData) -> LevelTravelStationData: ...
    def ActivateLevelTravel(self, ActivatingController: engine.Controller, ReturnValue: bool) -> bool: ...


class LevelTravelStationData(TravelStationData):
    TravelToMapName: str
    DestinationStationString: str
    bVehiclesAllowed: bool
    bVirtualLevel: bool
    bNoOutOfMapWaypoints: bool



class ResurrectTravelStationData(TravelStationData): ...


class TeleportDestinationActor(engine.Actor):
    ResurrectComponent: TravelStationResurrectComponent
    def TeleportPlayersToDestination(self, WorldContextObject: unreal.UObject, Destination: TeleportDestinationActor): ...


class TravelStationBase(engine.Actor): ...


class TravelStationModuleSettings(unreal.UObject):
    PlayerHalfHeight: float
    PlayerRadius: float
    TravelToStationCountdownTime: int
    VehicleExtents: core_uobject.Vector



class TravelStationResurrectComponent(TravelStationComponentBase):
    StationIsActive: bool
    DefaultStationToActive: bool
    bActivateOnEnterArea: bool
    bResurrectionActive: bool
    bNeverResurectThere: bool
    TravelDiscoveredChallenge: unreal.UClass
    ActivationCylinderTestDelay: float
    UseActivationCylinder: bool
    ActivationCylinderRadius: float
    ActivationCylinderHalfHeight: float
    ActivationCylinderZOffset: float
    ResurrectTravelData: ResurrectTravelStationData
    def OnRep_StationIsActive(self): ...
    def ActivateTravelStation(self, bForceActivation: bool, ReturnValue: bool) -> bool: ...


class TravelStationSpawnPointInterface(core_uobject.Interface): ...


class TravelStationSpawnPointComponent(engine.CapsuleComponent): ...


class TravelStationVehicleSpawnPointComponent(engine.BoxComponent): ...


class ActiveFastTravelData:
    FastTravelData: FastTravelStationData
    bHighlightDiscovery: bool



class ActiveFastTravelSaveData:
    FastTravelStationName: str
    bBlacklisted: bool



class FastTravelStationActiveContainer(engine.FastArraySerializer):
    ActiveFastTravelStations: unreal.WrappedArray[FastTravelStationActiveEntry]



class FastTravelStationActiveEntry(engine.FastArraySerializerItem):
    FastTravelData: FastTravelStationData



class AvailableTravelStation:
    StationToTravelTo: str
    OptionButton: FastTravelStationDebugButton



class TravelDataConditional:
    TravelDataSelection: str
    LevelTravelData: LevelTravelStationData
    MovieToPlayDuringTravelMap: int
    ConditionToPlayMovie: gbx_runtime.GbxCondition
    Condition: gbx_runtime.GbxCondition



class ExternalGraphLevelLinks: ...


class SpawnPointTracker:
    LastSpawnedAtCounter: int
    AssignedToActor: engine.Actor



class TravelCountdownInfo:
    TravelStationDestination: TravelStationData
    RemainingTime: int
    Status: ETravelStatus
    bDisallowLocalTravel: bool



class ETravelStatus(enum.Enum):
    Queued = 0
    Cancelled_OpenMenu = 1
    Cancelled_Cinamatic = 2


class EFastTravelDirection(enum.Enum):
    SendOnly = 0
    ReceiveOnly = 1

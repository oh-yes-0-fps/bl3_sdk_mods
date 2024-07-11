from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import online_subsystem_utils
from . import gbx_runtime
from . import gbx_dialog
from . import gbx_game_system_core
from . import gbx_ui
from . import gbx_travel_station


class MissionRewardData(gbx_runtime.GbxDataAsset): ...


class MissionGraph(unreal.UObject):
    GraphPriorityID: int
    GraphDisplayName: str
    bShowReferencedMissionDummy: bool
    ReferencedMissions: unreal.WrappedArray[unreal.UClass]
    DLCExpansionData: online_subsystem_utils.DownloadableContentData


class GlobalMissionGraph(MissionGraph): ...


class Mission(unreal.UObject):
    MissionTrackerBase: MissionTrackerBase
    bAllowAutomaticDebugActivation: bool
    FormattedMissionName: gbx_game_system_core.GbxUIFormattedText
    PreAcceptanceSummary: gbx_game_system_core.GbxUIFormattedText
    PostAcceptanceSummary: gbx_game_system_core.GbxUIFormattedText
    bImmediatelyAdvanceToFirstSet: bool
    bUseImmediatelyAdvanceToFirstSet: bool
    bImmediatelyAdvanceToFirstSetIfNotInMissionLevel: bool
    bAutoPlayKickoff: bool
    bUseAutoPlayKickoff: bool
    bPlotCritical: bool
    bRepeatable: bool
    SecondsToComplete: int
    bFailOnTimerExpiration: bool
    bOnlyDisplayTimer: bool
    RewardData: MissionRewardData
    bDependencyViewDummy: bool
    bIsFirstPlotMission: bool
    MissionDependencies: unreal.WrappedArray[Any]
    ObjectiveDependency: MissionObjectiveDependency
    ObjectiveSets: unreal.WrappedArray[MissionObjectiveSet]
    Objectives: unreal.WrappedArray[MissionObjective]
    ObjectiveChains: unreal.WrappedArray[MissionObjectiveChain]
    MissionPhases: unreal.WrappedArray[MissionPhase]
    MissionChallenge: unreal.UClass
    bFailOnTravel: bool
    StartCriticalSectionSet: MissionObjectiveSet
    StopCriticalSectionSet: MissionObjectiveSet
    bGlobalMissionBlocker: bool
    BlockedMissions: unreal.WrappedArray[Any]
    StartBlockingSet: MissionObjectiveSet
    StopBlockingSet: MissionObjectiveSet
    KickoffConversation: gbx_dialog.DialogConversation
    ActivityPriority: int
    bIsHidden: bool
    Description: gbx_game_system_core.GbxUIFormattedText
    TravelStation: Any
    bActivateMissionDialogScriptInAnyMap: bool
    MissionActivationDialogScript: Any
    KickoffDialog: gbx_dialog.DialogTimeSlotReference
    NextMissionInChain: Any
    AssociatedMissionGraph: Any
    CookedActivityObjectId: str

    def UpdateObjective(
        self, Objective: MissionObjective, Context: unreal.UObject, Amount: int
    ): ...
    def UnpauseObjectiveChain(self, Objective: MissionObjective): ...
    def ThwartObjectiveAndAdvanceObjectiveSet(
        self,
        ObjectiveToThwart: MissionObjective,
        ObjectiveSet: MissionObjectiveSet,
        bJumpToSet: bool,
    ): ...
    def StopMissionTimer(self): ...
    def StartMissionTimer(self): ...
    def MissionTimerExpired(self): ...
    def MissionRemoteEvent(self, EventName: str) -> bool: ...
    def MissionNotStarted(self): ...
    def MissionKickoff(self): ...
    def MissionGameModeEvent(self, EventName: str) -> bool: ...
    def MissionFailed(self): ...
    def MissionCompleteLoad(self): ...
    def MissionComplete(self): ...
    def MissionActiveLoad(self): ...
    def MissionActive(self): ...
    def JumpToObjectiveSet(
        self, ObjectiveSet: MissionObjectiveSet, bIsBranchingMission: bool
    ): ...
    def GetPausableChainedObjectivesList(
        self, ObjectivesList: unreal.WrappedArray[MissionObjective]
    ): ...
    def GetObjectivesList(
        self, ObjectivesList: unreal.WrappedArray[MissionObjective]
    ): ...
    def GetObjectiveSetsList(
        self, ObjectiveSetsList: unreal.WrappedArray[MissionObjectiveSet]
    ): ...
    def GetMissionRemainingSeconds(self) -> int: ...
    def FailMission(self): ...
    def EndKickoff(self): ...
    def CompleteMission(self): ...
    def ClearObjective(self, Objective: MissionObjective): ...
    def AdvanceObjectiveSet(self, ObjectiveSet: MissionObjectiveSet): ...
    def AddTimeToMission(self, SecondsToAdd: int): ...
    def ActivateMission(
        self, InitialObjectiveSet: MissionObjectiveSet, bSetAsTrackedMission: bool
    ): ...


class MissionDirectorComponent(engine.SceneComponent):
    Missions: unreal.WrappedArray[Any]
    MissionEntryPoints: unreal.WrappedArray[MissionObjectiveSetReference]
    MissionDirectorEnableCondition: gbx_runtime.GbxCondition
    MissionDirectorName: gbx_game_system_core.GbxUIFormattedText
    OnMissionDirectorEnabled: Any
    OnMissionDirectorDisabled: Any
    OnMissionsInitialized: Any

    def IsAnyMissionAvailable(self, OutResult: int): ...
    def IsAnyMissionActive(self, OutResult: int): ...
    def GetAllMissions(self, AllMissions: unreal.WrappedArray[unreal.UClass]): ...
    def ClearMissions(self): ...
    def AddMission(self, InMission: unreal.UClass): ...
    def ActivateAvailableMission(self): ...


class MissionIconComponent(engine.PrimitiveComponent):
    IconEnabledCondition: gbx_runtime.GbxCondition
    WaypointRadius: int
    bHideAreaWaypoint: bool
    AreaComponentClassOverride: unreal.UClass
    DrawStyle: EIconRadiusDrawStyle
    AttractParticleTemplate: engine.ParticleSystem
    AttractParticleTransform: core_uobject.Transform
    bSyncAttachedParticles: bool
    bAttachToWaypointSocket: bool
    OnIconEnabled: Any
    OnIconDisabled: Any
    bEnabled: bool

    def SetIconState(self, InState: int): ...
    def SetIconEnabledCondition(
        self, EnabledCondition: gbx_runtime.GbxCondition
    ) -> bool: ...
    def SetDisabledState(self, bDisabled: bool): ...
    def OnRep_Enabled(self, bPreviouslyEnabled: bool): ...
    def IsIconEnabled(self) -> bool: ...
    def GetRequiredInterface(self) -> unreal.UClass: ...
    def EnabledConditionRequiresNativeClass(self) -> bool: ...


class MissionTrackerBase(engine.Actor):
    MissionList: unreal.WrappedArray[MissionProgress]
    TrackedMission: unreal.UClass
    bDataValidated: bool
    GlobalMissionGraph: GlobalMissionGraph


class MissionTracker(MissionTrackerBase):
    DebugActivatedMission: Mission
    JumpedTooObjectiveSet: MissionObjectiveSet
    DefendTarget: DefendMissionTargetData
    bLevelLoadEventsIssued: bool
    AllMissionsObservers: unreal.WrappedArray[Any]
    MissionIconObservers: unreal.WrappedArray[Any]
    ActiveIcons: unreal.WrappedArray[ActiveMissionIconData]

    def OnStatIncrement(
        self,
        StatContext: engine.Actor,
        StatId: gbx_game_system_core.GameStatData,
        Amount: int,
    ): ...
    def OnRep_LevelLoadEventsIssued(self): ...
    def OnRep_ActiveIcons(self): ...


class PlayerMissionComponent(engine.ActorComponent):
    OnMissionDataChanged: Any
    MissionPlaythroughs: unreal.WrappedArray[MissionPlaythroughData]
    CachedMissionTracker: MissionTracker

    def ServerTrackPreviousActiveMissionInList(self): ...
    def ServerTrackNextActiveMissionInList(self): ...
    def ServerSetTrackedMission(self, MissionClass: unreal.UClass): ...
    def ClientUpdateMissionStatus(self, MissionClass: unreal.UClass, Status: int): ...
    def ClientUpdateActiveObjectiveSet(
        self,
        MissionClass: unreal.UClass,
        ActiveObjectiveSet: MissionObjectiveSet,
        DormantObjectives: unreal.WrappedArray[MissionObjective],
    ): ...
    def ClientTrackedMissionChanged(self, MissionClass: unreal.UClass): ...
    def ClientObjectiveUpdated(
        self,
        MissionClass: unreal.UClass,
        UpdatedObjective: MissionObjective,
        ObjectiveBit: int,
        Amount: int,
    ): ...
    def ClientObjectiveSetCompleted(
        self, MissionClass: unreal.UClass, CompletedObjectiveSet: MissionObjectiveSet
    ): ...
    def ClientObjectiveCleared(
        self, MissionClass: unreal.UClass, ClearedObjective: MissionObjective
    ): ...
    def ClientObjectiveChainUnpaused(
        self, MissionClass: unreal.UClass, Objective: MissionObjective
    ): ...
    def ClientMissionTimerStopped(self, MissionClass: unreal.UClass): ...
    def ClientMissionTimerStarted(self, MissionClass: unreal.UClass): ...
    def ClientMissionTimerChanged(
        self, MissionClass: unreal.UClass, SecondsToAdd: float
    ): ...
    def ClientMissionRegistered(self, MissionClass: unreal.UClass): ...
    def ClientDormantObjectiveRemoved(
        self,
        MissionClass: unreal.UClass,
        Objective: MissionObjective,
        bIssueActiveEvent: bool,
    ): ...
    def ClientDormantObjectiveAdded(
        self, MissionClass: unreal.UClass, Objective: MissionObjective
    ): ...


class MissionAttributeValueResolver(gbx_game_system_core.AttributeValueResolver):
    ValueToResolve: EMissionValueType


class MissionCondition_List(gbx_game_system_core.GbxCondition_List): ...


class MissionDebugMenu(gbx_ui.GbxDebugMenuSubmenu):
    MissionGraphToUse: MissionGraph
    bDisplayObjectName: bool
    Missions: unreal.WrappedArray[Mission]

    def SelectMissionGraph(self, MissionGraphId: str): ...
    def NotifyMissionActivationCheatStart(self): ...
    def GetObjectiveSetItemsForMission(
        self,
        MissionId: str,
        OutItems: unreal.WrappedArray[gbx_ui.GbxCascadingListItemData],
    ): ...
    def GetMissionWithId(self, MissionId: str) -> Mission: ...
    def GetMissionStatus(self, MissionId: str) -> int: ...
    def GetItemsForMissionStatus(
        self,
        Status: int,
        OutItems: unreal.WrappedArray[gbx_ui.GbxCascadingListItemData],
    ): ...
    def GetItemsForMissionGraph(
        self, OutItems: unreal.WrappedArray[gbx_ui.GbxCascadingListItemData]
    ): ...
    def CompleteMission(self, MissionId: str): ...
    def AdvanceToObjectiveSet(self, MissionId: str, ObjectiveSetId: str): ...
    def AdvanceMission(self, MissionId: str): ...


class MissionEnableCondition(gbx_runtime.GbxCondition): ...


class MissionEnableConditionBreadcrumbLinkedObjective(MissionEnableCondition):
    ObjectiveRef: MissionObjectiveReferenceWeak


class MissionEnableConditionKickoff(MissionEnableCondition):
    MissionClass: Any


class MissionEnableConditionMission(MissionEnableCondition):
    MissionClass: Any
    MissionStatus: int


class MissionEnableConditionMissionAvailable(MissionEnableCondition):
    MissionClass: Any


class MissionEnableConditionObjective(MissionEnableCondition):
    ObjectiveRef: MissionObjectiveReferenceWeak
    ObjectiveStatus: int
    bIgnoreObjectiveBit: bool


class MissionEnableConditionObjectiveCount(MissionEnableCondition):
    ObjectiveRef: MissionObjectiveReferenceWeak
    ComparisonOperator: EObjectiveCountComparisonOperatorType
    ObjectiveProgress: int
    bRequireActiveObjective: bool


class MissionEnableConditionObjectiveSet(MissionEnableCondition):
    ObjectiveSetRef: MissionObjectiveSetReference
    ObjectiveSetStatus: int
    ObjectivesStatus: int


class MissionFunctionLibrary(engine.BlueprintFunctionLibrary):

    def UpdateMissionObjectiveRef(
        self,
        WorldContextObject: unreal.UObject,
        ObjectiveRef: MissionObjectiveReference,
    ): ...
    def TrackPreviousActiveMissionInList(self, WorldContextObject: unreal.UObject): ...
    def TrackNextActiveMissionInList(self, WorldContextObject: unreal.UObject): ...
    def TrackActiveMission(
        self, WorldContextObject: unreal.UObject, MissionClass: unreal.UClass
    ): ...
    def SendMissionEventWithContext(
        self,
        EventRef: MissionEventReference,
        WorldContextObject: unreal.UObject,
        OptionalContext: unreal.UObject,
    ): ...
    def SendMissionEvent(
        self,
        WorldContextObject: unreal.UObject,
        EventRef: MissionEventReference,
        OptionalContext: unreal.UObject,
    ): ...
    def ResolveMissionSoftClassReference(self, Mission: Any) -> unreal.UClass: ...
    def JumpToMissionObjectiveSetRef(
        self,
        WorldContextObject: unreal.UObject,
        ObjectiveSetRef: MissionObjectiveSetReference,
        bIsBranchingMission: bool,
    ): ...
    def GetSoftObjectiveSetListForMission(
        self, MissionClass: Any, SoftObjectiveSetList: unreal.WrappedArray[Any]
    ): ...
    def GetPlotMissionIndex(self, MissionObj: Mission) -> int: ...
    def GetObjectiveSetNameListForMissionFromAssetSubclass(
        self, MissionClass: Any, NamesList: unreal.WrappedArray[str]
    ): ...
    def GetObjectiveSetNameListForMission(
        self, MissionClass: unreal.UClass, NamesList: unreal.WrappedArray[str]
    ): ...
    def GetObjectiveSetListForMission(
        self,
        MissionClass: unreal.UClass,
        ObjectiveSetList: unreal.WrappedArray[MissionObjectiveSet],
    ): ...
    def GetObjectiveNameListForMissionFromAssetSubclass(
        self, Mission: Any, NamesList: unreal.WrappedArray[str]
    ): ...
    def GetObjectiveNameListForMission(
        self, MissionClass: unreal.UClass, NamesList: unreal.WrappedArray[str]
    ): ...
    def GetMissionStatus(
        self, WorldContextObject: unreal.UObject, MissionClass: unreal.UClass
    ) -> int: ...
    def GetMissionObjectiveStatusRef(
        self,
        WorldContextObject: unreal.UObject,
        ObjectiveRef: MissionObjectiveReference,
        OptionalContext: unreal.UObject,
    ) -> int: ...
    def GetMissionObjectiveSetStatusRef(
        self,
        WorldContextObject: unreal.UObject,
        ObjectiveSetRef: MissionObjectiveSetReference,
    ) -> int: ...
    def GetMissionObjectiveCount(
        self,
        WorldContextObject: unreal.UObject,
        ObjectiveRef: MissionObjectiveReference,
        CurrentObjectiveCount: int,
        TotalObjectiveCount: int,
    ): ...
    def GetMissionLevel(self, MissionObj: Mission) -> int: ...
    def GetMissionClassFromObjectiveReferenceWeak(
        self, ObjectiveReference: MissionObjectiveReferenceWeak
    ) -> unreal.UClass: ...
    def GetMissionClassFromObjectiveReference(
        self, ObjectiveReference: MissionObjectiveReference
    ) -> unreal.UClass: ...
    def GetMission(
        self, WorldContextObject: unreal.UObject, MissionClass: unreal.UClass
    ) -> Mission: ...
    def GetEventNameListForMission(
        self, MissionClass: unreal.UClass, NamesList: unreal.WrappedArray[str]
    ): ...
    def GetCurrentlyTrackedMission(
        self, WorldContextObject: unreal.UObject
    ) -> unreal.UClass: ...
    def GetActivePlotMission(
        self, WorldContextObject: unreal.UObject
    ) -> unreal.UClass: ...
    def GetActiveMissions(
        self, WorldContextObject: unreal.UObject
    ) -> unreal.WrappedArray[Mission]: ...
    def FillMissionObjectiveSetRef(
        self,
        MissionObjectiveSetRef: MissionObjectiveSetReference,
        MissionClass: unreal.UClass,
        ObjectiveSet: str,
    ): ...
    def FillMissionObjectiveRefWeak(
        self,
        MissionObjectiveRef: MissionObjectiveReferenceWeak,
        MissionClass: unreal.UClass,
        Objective: str,
    ): ...
    def FillMissionObjectiveRef(
        self,
        MissionObjectiveRef: MissionObjectiveReference,
        MissionClass: unreal.UClass,
        Objective: str,
    ): ...
    def FillMissionEventRef(
        self,
        MissionEventRef: MissionEventReference,
        MissionClass: unreal.UClass,
        EventName: str,
    ): ...
    def EqualEqual_MissionObjectiveSetReference(
        self, A: MissionObjectiveSetReference, B: MissionObjectiveSetReference
    ) -> bool: ...
    def EqualEqual_MissionObjectiveReference(
        self, A: MissionObjectiveReference, B: MissionObjectiveReference
    ) -> bool: ...
    def DebugJumpToMissionObjectiveSetRef(
        self,
        WorldContextObject: unreal.UObject,
        ObjectiveSetRef: MissionObjectiveSetReference,
        bIsBranchingMission: bool,
    ): ...
    def CreateMission(
        self, WorldContextObject: unreal.UObject, MissionClass: unreal.UClass
    ) -> Mission: ...
    def CompleteMission(
        self, WorldContextObject: unreal.UObject, MissionClass: unreal.UClass
    ): ...
    def AdvanceToBreadcrumbObjective(
        self,
        WorldContextObject: unreal.UObject,
        BreadcrumbObjectiveRef: MissionObjectiveReference,
    ): ...
    def AdvanceMissionObjectiveSetRef(
        self,
        WorldContextObject: unreal.UObject,
        ObjectiveSetRef: MissionObjectiveSetReference,
    ): ...
    def ActivateMissionAtObjectiveSet(
        self,
        WorldContextObject: unreal.UObject,
        ObjectiveSetRef: MissionObjectiveSetReference,
    ): ...
    def ActivateMission(
        self, WorldContextObject: unreal.UObject, MissionClass: unreal.UClass
    ): ...


class MissionIconInterface(core_uobject.Interface): ...


class MissionIconObserverInterface(core_uobject.Interface): ...


class MissionLocationData(gbx_travel_station.TravelLocationData):
    DefaultStation: Any
    MissionLocations: unreal.WrappedArray[MissionLocation]

    def GetRequiredInterface(self) -> unreal.UClass: ...
    def EnabledConditionRequiresNativeClass(self) -> bool: ...


class MissionObjective(unreal.UObject):
    ObjectiveCount: int
    GameStat: gbx_game_system_core.GameStatData
    FormattedProgressMessage: gbx_game_system_core.GbxUIFormattedText
    bRememberIndividualState: bool
    bAllOrNothing: bool
    bClearIfActiveSetNotComplete: bool
    bAutoUpdateIfActivatedInMissionLevel: bool
    bInvisible: bool
    bBreadcrumb: bool
    bBreadcrumbNoClear: bool
    bBreadcrumbLinked: bool
    bOptional: bool
    bPauseObjectiveChain: bool
    bAdvanceChainOnLevelLoad: bool
    bWantsPlanetTravel: bool
    bGrantsStarterGear: bool
    bOnlyActiveIfAnyPlayerInVehicle: bool
    bOnlyActiveIfNoPlayersInVehicle: bool
    bOnlyActiveIfMissionVehicleNotSpawned: bool
    bOnlyActiveIfTravelIdActive: bool
    bOnlyActiveIfTravelIdNotActive: bool
    bOnlyActiveIfMissionWeaponWielded: bool
    bOnlyActiveIfMissionWeaponNotWielded: bool
    bOnlyActiveIfStateStable: bool
    bOnlyActiveIfStateTransitioning: bool
    bAutoClearWhenNoLongerDormant: bool
    bObjectiveChainHead: bool
    bObjectiveChainMember: bool
    bRequiredForObjectiveSetAdvance: bool
    bSuppressEmptyCheckbox: bool
    OptionalRewardData: MissionRewardData
    ObjectiveGuid: core_uobject.Guid


class MissionObjectiveReferenceInterface(core_uobject.Interface):

    def GetMissionObjectiveReferences(
        self, OutMissionObjectives: unreal.WrappedArray[MissionObjectiveReference]
    ): ...


class MissionObjectiveSet(unreal.UObject):
    Objectives: unreal.WrappedArray[MissionObjective]
    StationOverride: Any
    BreadcrumbLinkedObjective: MissionObjective
    DisplayedBreadcrumbLinkedObjective: MissionObjective
    NextSet: MissionObjectiveSet
    bCanCompleteMission: bool
    bAutoAdvanceToNextSet: bool
    bOutOfMapWaypoints: bool
    bContainsRequiredObjectives: bool
    bContainsClearIfNotCompleteObjectives: bool
    DescriptionOverride: gbx_game_system_core.GbxUIFormattedText
    PreAcceptanceSummaryOverride: gbx_game_system_core.GbxUIFormattedText
    ObjectiveSetGuid: core_uobject.Guid
    ObjOrderPos: unreal.WrappedArray[int]


class MissionObjectiveSetReferenceInterface(core_uobject.Interface):

    def GetMissionObjectiveSetReferences(
        self, OutMissionObjectiveSets: unreal.WrappedArray[MissionObjectiveSetReference]
    ): ...


class MissionObserverComponent(engine.ActorComponent):
    Missions: unreal.WrappedArray[unreal.UClass]
    ObjectiveBit: int
    NumberOfObjectiveBits: int
    bEnableObjectiveBit: bool
    OnMissionUpdate: Any
    OnMissionObjectiveUpdate: Any
    OnMissionObjectiveSetUpdate: Any
    OnMissionsInitialized: Any
    ObserverEventList: unreal.WrappedArray[MissionObserverEvent]
    OnLoadEventList: unreal.WrappedArray[MissionEnableConditionEvent]

    def ObserverMission(self, MissionClass: unreal.UClass): ...
    def GetUpdateEventObject(
        self,
        OutMissionInitialized: unreal.WrappedArray[unreal.UObject],
        OutMissionUpdate: unreal.WrappedArray[unreal.UObject],
        OutMissionObjectiveUpdate: unreal.WrappedArray[unreal.UObject],
        OutMissionObjectiveSetUpdate: unreal.WrappedArray[unreal.UObject],
    ) -> bool: ...


class MissionObserverInterface(core_uobject.Interface): ...


class MissionObserverPlayerInterface(MissionObserverInterface):

    def ClientReceiveMissionData(self, MissionData: ReplicatedMissionData): ...


class MissionPhase(unreal.UObject):
    ObjectiveSets: unreal.WrappedArray[MissionObjectiveSet]
    PhaseIndex: int


class MissionReferenceInterface(core_uobject.Interface):

    def GetMissionClassReferences(
        self, OutMissions: unreal.WrappedArray[unreal.UClass]
    ): ...
    def CheckForMissionReferenceErrors(self) -> bool: ...


class MissionObjectiveReferenceBase:
    ObjectiveName: str
    ObjectiveGuid: core_uobject.Guid
    Objective: MissionObjective


class MissionObjectiveReference(MissionObjectiveReferenceBase):
    Mission: unreal.UClass


class MissionObjectiveSetReference:
    Mission: Any
    ObjectiveSetName: str
    ObjectiveSetGuid: core_uobject.Guid
    ObjectiveSet: MissionObjectiveSet


class MissionEventReference:
    Mission: unreal.UClass
    EventName: str


class MissionObjectiveReferenceWeak(MissionObjectiveReferenceBase):
    Mission: Any


class MissionEnableConditionEvent:
    EventName: str
    EnableCondition: MissionEnableCondition
    OnLoad: Any


class MissionLocation:
    TravelStation: Any
    StationCondition: gbx_runtime.GbxCondition


class MissionObjectiveChain:
    ObjectiveChain: unreal.WrappedArray[MissionObjective]


class MissionObjectiveData:
    MissionClass: unreal.UClass
    Objective: MissionObjective


class ActiveMissionIconData:
    Icon: Any
    IconGuid: core_uobject.Guid
    IconLocationComponent: engine.SceneComponent
    IconLocation: core_uobject.Vector
    WaypointRadius: int
    IconData: engine.DataAsset
    MissionClass: unreal.UClass
    MissionObjectives: unreal.WrappedArray[MissionObjective]
    VisibleDistanceOverride: float
    HiddenDistanceOverride: float
    bHideAreaWaypoint: bool
    AreaComponentClassOverride: unreal.UClass


class MissionObserverEvent:
    EventName: str
    bLastConditionValue: bool
    EnabledCondition: gbx_runtime.GbxCondition
    OnConditionTrue: Any
    OnConditionFalse: Any


class DefendMissionTargetData:
    Objective: MissionObjective
    PercentHealth: int


class DefendMissionData: ...


class MissionObjectiveDependency:
    ObjectiveRef: MissionObjectiveReferenceWeak
    ObjectiveStatus: int


class MissionPlaythroughData:
    MissionList: unreal.WrappedArray[MissionStatusPlayerData]
    TrackedMission: unreal.UClass


class MissionStatusPlayerData:
    MissionClass: unreal.UClass
    Status: int
    ObjectivesProgress: unreal.WrappedArray[int]
    ActiveObjectiveSet: MissionObjectiveSet
    bHasBeenViewedInLog: bool
    bKickoffPlayed: bool
    LeagueInstance: int


class ReplicatedMissionData:
    Progress: unreal.WrappedArray[ReplicatedMissionProgress]
    TrackedMission: unreal.UClass
    ActiveTimedMissions: unreal.WrappedArray[TimedMissionData]


class TimedMissionData:
    MissionClass: unreal.UClass
    SecondsLeft: float
    StartingSeconds: float
    bTimerRunning: bool
    bFailOnTimerExpiration: bool
    bTimerExpired: bool


class ReplicatedMissionProgress: ...


class MissionProgress:
    Mission: Mission
    MissionClass: unreal.UClass
    Status: int
    ObjectivesProgress: unreal.WrappedArray[int]
    ActiveObjectiveSet: MissionObjectiveSet
    DormantObjectives: unreal.WrappedArray[MissionObjective]
    PausedObjectiveChains: unreal.WrappedArray[MissionObjective]
    bActivateScriptWhenDependenciesMet: bool
    ActivatedDialogScript: gbx_dialog.DialogScriptPinnedRef
    bKickoffPlayed: bool
    bHasMissionFailed: bool
    bReplicationError: bool


class EMissionEvent(enum.Enum):
    Active_Load = 0
    Complete_Load = 1
    Completed = 2


class EMissionObjectiveEvent(enum.Enum):
    Activated = 0
    Active_Load = 1
    Dormant_Load = 2
    Updated = 3


class EMissionObjectiveSetEvent(enum.Enum):
    Active_Load = 0
    ObjectivesChanged = 1
    Complete_Load = 2


class EMissionValueType(enum.Enum):
    EMissionValueType_MAX = 0


class EMissionDebugStatus(enum.Enum):
    MDS_Eligible = 0
    MDS_DevMission = 1
    MDS_Complete = 2


class EMissionActiveResult(enum.Enum):
    NoMissionsActive = 0
    EMissionActiveResult_MAX = 1


class EMissionAvailableResult(enum.Enum):
    NoMissionsAvailable = 0
    EMissionAvailableResult_MAX = 1


class EObjectiveCountComparisonOperatorType(enum.Enum):
    LessThan = 0
    NotEqualTo = 1
    GreaterThan = 2


class EMissionEnableConditionObjectiveSetObjectiveStatus(enum.Enum):
    MECOSOS_AllCompleteStatusIgnored = 0
    MECOSOS_AllCompleteStatusMatters = 1


class EIconRadiusDrawStyle(enum.Enum):
    EIconRadiusDrawStyle_MAX = 0
    Wire = 1
    Solid = 2


class EMissionIconState(enum.Enum):
    IconState_ForceDisabled = 0
    IconState_ForceEnabled = 1


class EMissionObjectiveDependencyStatus(enum.Enum):
    MODS_Complete = 0
    MODS_MAX = 1


class EMissionTimerEvent(enum.Enum):
    TimerStopped = 0
    TimeAdded = 1
    EMissionTimerEvent_MAX = 2


class EMissionObjectiveSetStatus(enum.Enum):
    MOSS_Unknown = 0
    MOSS_Active = 1


class EMissionObjectiveStatus(enum.Enum):
    MOS_Active = 0
    MOS_Dormant = 1
    MOS_Unknown = 2


class EMissionStatus(enum.Enum):
    MS_Active = 0
    MS_Complete = 1
    MS_Unknown = 2

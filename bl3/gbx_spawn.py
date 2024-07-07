from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine
from . import gbx_runtime
from . import gbx_game_system_core
from . import gameplay_tags



class Spawner(engine.Actor):
    SpawnerComponent: SpawnerComponent
    SpawnerLinkComponent: SpawnerLinkComponent
    SpawnPointComponent: SpawnPointComponent
    SpawnerTeamComponent: SpawnerTeamComponent
    bAutoGroundSpawnPointComponents: bool
    ExcludeAutoGroundPointComponents: unreal.WrappedArray[str]
    def SuspendAllActors(self): ...
    def SetTeamOverride(self, OverrideTeam: gbx_game_system_core.Team): ...
    def SetTeam(self, NewTeam: gbx_game_system_core.Team): ...
    def SetAlwaysActive(self, bInAlwaysActive: bool): ...
    def ResetSpawning(self): ...
    def OverrideSpawnerStyle(self, NewSpawnerStyle: SpawnerStyle): ...
    def OnSpawningComplete(self, Spawner: Spawner): ...
    def IsSpawnerEnabled(self, ReturnValue: bool) -> bool: ...
    def IsFinishedSpawning(self, ReturnValue: bool) -> bool: ...
    def GetSpawnPointComponent(self, ReturnValue: SpawnPointComponent) -> SpawnPointComponent: ...
    def GetSpawnerTeamComponent(self, ReturnValue: SpawnerTeamComponent) -> SpawnerTeamComponent: ...
    def GetSpawnerLinkComponent(self, ReturnValue: SpawnerLinkComponent) -> SpawnerLinkComponent: ...
    def GetSpawnerComponent(self, ReturnValue: SpawnerComponent) -> SpawnerComponent: ...
    def GetNumAliveActors(self, bIncludeExternal: bool, ReturnValue: int) -> int: ...
    def EnableSpawner(self): ...
    def DisableSpawner(self): ...
    def DestroyAllActors(self): ...
    def CompleteScriptedWarmup(self): ...
    def AreAllDead(self, bIncludeExternal: bool, ReturnValue: bool) -> bool: ...


class SpawnerComponent(engine.PrimitiveComponent):
    bEnabled: bool
    ChanceToEnableOnInit: gbx_game_system_core.AttributeInitializationData
    bAlwaysActive: bool
    bResetOnEnabled: bool
    ScriptedWarmup: EScriptedWarmup
    ActivationRadius: float
    bActivationUsesRadius: bool
    ActivationVolumes: unreal.WrappedArray[engine.Volume]
    bActivationUsesVolumes: bool
    SpawnDetails: SpawnDetails
    MinimumActivationTime: float
    SpawnerStyle: SpawnerStyle
    SpawnerStyleOverride: SpawnerStyle
    Limits: unreal.WrappedArray[SpawnLimitData]
    bApplyLimitsToGroup: bool
    WaitingFactories: unreal.WrappedArray[SpawnFactory]
    SpawnPoints: unreal.WrappedArray[SpawnPoint]
    bRandomizeSpawnPoints: bool
    SpawnPointGroups: unreal.WrappedArray[SpawnPointGroup]
    SpawnPointUseType: ESpawnPointUseType
    SpawnPointClusterRadius: float
    SpawnPointComponents: unreal.WrappedArray[SpawnPointComponent]
    Spawner: Spawner
    bIncludeExternalActorsForAllDiedEvent: bool
    DrawStyle: ESpawnerDrawStyle
    bUseScriptedWarmup: bool
    def SuspendAllActors(self): ...
    def SetTeam(self, NewTeam: gbx_game_system_core.Team): ...
    def SetSpawnOptions(self, NewSpawnOptions: SpawnOptionData): ...
    def ResetSpawning(self): ...
    def OverrideSpawnerStyle(self, NewSpawnerStyle: SpawnerStyle): ...
    def IsSpawnerStyleClassAllowed(self, SpawnerStyleClass: unreal.UClass, ReturnValue: bool) -> bool: ...
    def IsFinishedSpawning(self, ReturnValue: bool) -> bool: ...
    def IncludeExternalActorsForAllDiedEvent(self): ...
    def GetSpawnOptions(self, ReturnValue: SpawnOptionData) -> SpawnOptionData: ...
    def GetParentSpawner(self, ReturnValue: SpawnerComponent) -> SpawnerComponent: ...
    def GetNumSuspendedActors(self, ReturnValue: int) -> int: ...
    def GetNumSpawnedActors(self, bIncludeExternal: bool, bInGroup: bool, ReturnValue: int) -> int: ...
    def GetNumDeadActors(self, bIncludeExternal: bool, bInGroup: bool, ReturnValue: int) -> int: ...
    def GetNumAliveActors(self, bIncludeExternal: bool, bInGroup: bool, ReturnValue: int) -> int: ...
    def GetAliveActors(self, ReturnValue: unreal.WrappedArray[engine.Actor]) -> unreal.WrappedArray[engine.Actor]: ...
    def EnableSpawner(self): ...
    def DisableSpawner(self): ...
    def DestroyAllActors(self): ...
    def CompleteScriptedWarmup(self): ...
    def AreAllDead(self, bIncludeExternal: bool, bInGroup: bool, ReturnValue: bool) -> bool: ...


class SpawnPoint(engine.Actor):
    SpawnRootComponent: engine.SceneComponent
    SpawnPointComponent: SpawnPointComponent
    ConnectedSpawners: unreal.WrappedArray[SpawnerComponent]
    TempRootFix: engine.SceneComponent
    def SetSpawnStyleTag(self, NewTag: gameplay_tags.GameplayTag): ...
    def ResetStretchPoint(self): ...
    def GetSpawnStyleTag(self, ReturnValue: gameplay_tags.GameplayTag) -> gameplay_tags.GameplayTag: ...
    def EnableSpawnPoint(self): ...
    def DisableSpawnPoint(self): ...


class AnimNotify_SpawnAnim(engine.AnimNotify):
    Action: ESpawnAnimNotifyAction



class GbxAction_SpawnAnim(gbx_game_system_core.GbxAction_Anim):
    SpawnPointAction: unreal.UClass
    SpawnPointActionStop: unreal.UClass
    OverrideMovementMode: int
    bOverrideMovementMode: bool
    bDisableCollisionOnSpawn: bool
    def K2_GetSpawnPoint(self, ReturnValue: engine.Actor) -> engine.Actor: ...


class GbxCondition_SpawnCostAvailable(gbx_runtime.GbxCondition):
    SpawnOptions: SpawnOptionData



class MultiSpawnPoint(SpawnPoint):
    SpawnPointComponents: unreal.WrappedArray[SpawnPointComponent]



class SpawnDLCScript(unreal.UObject):

    def OnAllSpawned(self, SpawnerComponent: SpawnerComponent): ...
    def OnAllDied(self, SpawnerComponent: SpawnerComponent): ...
    def OnActorSpawned(self, SpawnerComponent: SpawnerComponent, Actor: engine.Actor): ...
    def OnActorDied(self, SpawnerComponent: SpawnerComponent, Actor: engine.Actor): ...


class SpawnDLCData(gbx_runtime.GbxDataAsset):
    bGlobalReplacementAlwaysEnabledDuringEvent: bool
    SpawnerReplacements: unreal.WrappedArray[SpawnDLCGroup]
    Script: unreal.UClass
    bScriptGloballyReplacedSpawners: bool
    bScriptManuallyReplacedSpawners: bool
    MaximumTotalEventEnemies: gbx_game_system_core.GbxParam
    MaximumEventEnemiesPerSpawner: gbx_game_system_core.GbxParam
    MaximumScriptedSpawnersPerGroup: gbx_game_system_core.GbxParam
    ScriptedSpawners: unreal.WrappedArray[SpawnDLCScriptGroup]
    ExpansionScriptedSpawners: unreal.WrappedArray[DLCScriptedSpawerExpansionList]



class GlobalSpawnDLCData(gbx_runtime.GbxDataAsset):
    DLCs: unreal.WrappedArray[SpawnDLCItem]



class DLCScriptedSpawerExpansionList(gbx_runtime.GbxDataAsset):
    ScriptedSpawners: unreal.WrappedArray[SpawnDLCScriptGroup]



class SpawnedActorInterface(core_uobject.Interface): ...


class SpawnerBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def SuspendSpawnedActors(self, WorldContextObject: unreal.UObject): ...
    def SpawnActorWithSpawnOptionsTransform(self, Context: engine.Actor, SpawnOptions: SpawnOptionData, SpawnTransform: core_uobject.Transform, ReturnValue: engine.Actor) -> engine.Actor: ...
    def SpawnActorWithSpawnOptionsAsync(self, WorldContext: unreal.UObject, Request: SpawnManagerAsyncRequest, ReturnValue: int) -> int: ...
    def SpawnActorWithSpawnOptions(self, Context: engine.Actor, SpawnOptions: SpawnOptionData, SpawnPointComponent: SpawnPointComponent, ReturnValue: engine.Actor) -> engine.Actor: ...
    def SpawnActorWithSpawner(self, Context: engine.Actor, Factory: SpawnFactory, SpawnPointComponent: SpawnPointComponent, SpawnerComponent: SpawnerComponent, Owner: engine.Actor, ReturnValue: engine.Actor) -> engine.Actor: ...
    def SetMaxSpawnCost(self, WorldContextObject: unreal.UObject, NewMaxSpawnCost: int): ...
    def RestoreSuspendedActors(self, WorldContextObject: unreal.UObject): ...
    def RemoveActorFromSpawnSystem(self, Actor: engine.Actor): ...
    def CancelSpawnActorWithOptionsAsyncRequest(self, WorldContext: unreal.UObject, RequestID: int): ...


class SpawnerLinkComponent(engine.PrimitiveComponent):
    LinkDataList: unreal.WrappedArray[SpawnerLinkData]
    LinkedSpawners: unreal.WrappedArray[engine.Actor]
    bAutoProximityLink: bool
    MasterLinkData: SpawnerLinkData
    bBeingDestroyed: bool
    SharedStates: unreal.WrappedArray[unreal.UObject]
    AllLinkedSpawners: unreal.WrappedArray[Spawner]



class SpawnerStateInterface(core_uobject.Interface): ...


class SpawnerStyle(gbx_runtime.GbxDataAsset): ...


class SpawnerStyle_Bunch(SpawnerStyle):
    SpawnOptions: SpawnOptionData
    NumActorsParam: gbx_game_system_core.GbxParam
    SpawnDelay: float



class SpawnerStyle_BunchList(SpawnerStyle):
    Bunches: unreal.WrappedArray[SpawnBunchListItem]
    SpawnDelay: float



class SpawnerStyle_Den(SpawnerStyle):
    SpawnOptions: SpawnOptionData
    bInfinite: bool
    NumActorsParam: gbx_game_system_core.GbxParam
    MaxAliveActorsWhenPassive: gbx_game_system_core.GbxParam
    MaxAliveActorsWhenThreatened: gbx_game_system_core.GbxParam
    SpawnDelay: float
    WaveDelay: float
    WavePercent: float
    NumAliveActorsParam: gbx_game_system_core.GbxParam



class SpawnerStyle_Encounter(SpawnerStyle):
    Waves: unreal.WrappedArray[EncounterWave]



class SpawnerStyle_Single(SpawnerStyle):
    SpawnOptions: SpawnOptionData



class SpawnerStyleFactory_Bunch(SpawnerStyle_Bunch):
    SpawnFactory: SpawnFactory
    AliveLimitType: ESpawnLimitType
    InternalSpawnOptions: SpawnOptionData
    def IsFactoryClassAllowed(self, FactoryClass: unreal.UClass, ReturnValue: bool) -> bool: ...


class SpawnerStyleFactory_Den(SpawnerStyle_Den):
    SpawnFactory: SpawnFactory
    AliveLimitType: ESpawnLimitType
    InternalSpawnOptions: SpawnOptionData
    def IsFactoryClassAllowed(self, FactoryClass: unreal.UClass, ReturnValue: bool) -> bool: ...


class SpawnerStyleFactory_Single(SpawnerStyle_Single):
    SpawnFactory: SpawnFactory
    AliveLimitType: ESpawnLimitType
    InternalSpawnOptions: SpawnOptionData
    def IsFactoryClassAllowed(self, FactoryClass: unreal.UClass, ReturnValue: bool) -> bool: ...


class SpawnerTeamComponent(gbx_game_system_core.TeamComponent):
    OverrideTeam: gbx_game_system_core.Team
    bOverrideTeam: bool
    ResolvedTeamType: str
    EvaluatedTeam: gbx_game_system_core.Team



class SpawnFactory(unreal.UObject):
    bUsedInSpawnPointOverlapChecks: bool
    bOverrideActorTags: bool
    Tags: gameplay_tags.GameplayTagContainer
    SpawnDetails: SpawnDetails
    CachedActorClassTagComponent: gbx_game_system_core.GameplayTagContainerComponent
    CachedTeam: gbx_game_system_core.Team



class SpawnFactory_Container(SpawnFactory):
    Options: SpawnOptionData



class SpawnFactory_ContainerSoftRef(SpawnFactory):
    OptionsPath: SpawnOptionDataSoftPath



class SpawnFactory_Generic(SpawnFactory):
    ActorProperties: engine.Actor
    bUseActorProperties: bool
    bIncludeSkeletalMeshForSpawnExtent: bool
    SpawnOrigin: core_uobject.Vector
    SpawnExtent: core_uobject.Vector
    bOverrideSpawnSize: bool
    CollisionHandling: engine.ESpawnActorCollisionHandlingMethod
    bOverrideCollisionHandling: bool
    ActorPropertyAssetRefCache: unreal.WrappedArray[core_uobject.SoftObjectPath]
    def ShouldSkipActorProperty(self, ActorProperty: core_uobject.Property, ReturnValue: bool) -> bool: ...


class SpawnManager(unreal.UObject):
    AdditionalSpawnPointOverlapActors: unreal.WrappedArray[engine.Actor]
    AsyncRequests: unreal.WrappedArray[SpawnManagerAsyncRequestEntry]
    SpawnManagerClassName: core_uobject.SoftClassPath
    MaxSpawnCost: int
    bCanResetSpawners: bool
    SpawnerResetPeriod: float
    MaxActorsSpawnedPerFrame: int
    UpdatePeriod: float
    SuspendTestPeriod: int
    IrrelevantPeriod: int
    AlwaysRelevantDistance: int
    AlwaysIrrelevantDistance: int
    bUseMultiframeSpawning: bool
    PrivateWorld: engine.World
    DLCs: unreal.WrappedArray[SpawnDLCData]
    Spawners: unreal.WrappedArray[SpawnerData]
    CachedPlayerLocations: unreal.WrappedArray[core_uobject.Vector]
    CachedPlayers: unreal.WrappedArray[engine.Controller]
    SpawnedActor: engine.Actor
    def ActorDestroyed(self, Actor: engine.Actor): ...


class SpawnSystemEditorSettings(engine.DeveloperSettings):
    StreamStyle: ESpawnSystemStreamStyle



class SpawnOptionData(gbx_runtime.GbxDataAsset):
    Options: unreal.WrappedArray[SpawnFactoryData]
    SpawnDetails: SpawnDetails



class SpawnPointComponent(engine.PrimitiveComponent):
    bEnabled: bool
    SpawnPoint: SpawnPoint
    SpawnAITreeTag: gameplay_tags.GameplayTag
    SpawnAction: gameplay_tags.GameplayTag
    SpawnStretchType: ESpawnStretchType
    TraceToGroundDistance: float
    bStretchOrient: bool
    Tags: gameplay_tags.GameplayTagContainer
    FilterMatchType: ESpawnPointFilter
    bFilterByTags: bool
    TagMatchType: gameplay_tags.EGameplayContainerMatchType
    StretchyPoint: core_uobject.Transform
    ResetStretch: gbx_runtime.GbxTriggerProperty
    bAttachSpawnedActors: bool
    AttachSlotName: str
    def SetSpawnStyleTag(self, NewTag: gameplay_tags.GameplayTag): ...
    def ResetStretchPoint(self): ...
    def HasSpawnAITreeTag(self, ReturnValue: bool) -> bool: ...
    def GetStretchyPoint(self, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def GetSpawnStyleTag(self, ReturnValue: gameplay_tags.GameplayTag) -> gameplay_tags.GameplayTag: ...
    def GetSpawnAITreeTag(self, ReturnValue: gameplay_tags.GameplayTag) -> gameplay_tags.GameplayTag: ...
    def EnableSpawnPoint(self): ...
    def DisableSpawnPoint(self): ...


class SpawnPointProvider(core_uobject.Interface): ...


class SpawnPreviewComponent(gbx_game_system_core.PreviewComponent):
    PreviewList: unreal.WrappedArray[SpawnPreviewState]
    ActiveSpawnPointIdx: int
    PreviewAction: unreal.UClass
    bAutoCycle: bool
    CycleActor: gbx_runtime.GbxTriggerProperty
    bShowAction: bool
    bRepeatAction: bool
    ReplayAction: gbx_runtime.GbxTriggerProperty
    ActionComponent: gbx_game_system_core.GbxActionComponent
    SpawnerList: unreal.WrappedArray[SpawnerComponent]
    def OnReplayAction(self): ...
    def OnCycleActor(self, Direction: gbx_game_system_core.ECycleDirection): ...


class SpawnerActorData:
    Actor: engine.Actor
    Factory: SpawnFactory
    Owner: engine.Actor



class ActionState_SpawnAnim(gbx_game_system_core.ActionState_Anim): ...


class SpawnDLCItem:
    IsEnabled: gbx_game_system_core.AttributeInitializationData



class SpawnDLCScriptGroup:
    Description: str
    MaximumScriptedSpawnersPerGroupOverride: gbx_game_system_core.GbxParam
    SpawnerSoftPaths: unreal.WrappedArray[SpawnerSoftPath]
    bAlwaysEnabledDuringEvent: bool



class SpawnerSoftPath:
    SpawnerPathName: str
    SpawnerSubPathString: str



class SpawnDLCGroup:
    Description: str
    Replacements: unreal.WrappedArray[SpawnDLCGroupItem]



class SpawnDLCGroupItem:
    SpawnerSoftPaths: unreal.WrappedArray[SpawnerSoftPath]
    SpawnOptions: SpawnOptionData
    bAlwaysEnabledDuringEvent: bool



class SpawnerData:
    Manager: SpawnManager
    Owner: engine.Actor
    Spawner: Spawner
    SpawnerComp: SpawnerComponent
    SpawnerStyle: SpawnerStyle
    Actors: unreal.WrappedArray[SpawnerActorData]
    DeadActors: unreal.WrappedArray[engine.Actor]
    DLCScripts: unreal.WrappedArray[SpawnDLCScript]



class SpawnerLinkData:
    Owner: engine.Actor
    Spawner: Spawner
    TeamComp: gbx_game_system_core.TeamComponent
    SpawnerComp: SpawnerComponent
    LinkComp: SpawnerLinkComponent



class SpawnBunchListItem:
    SpawnOptions: SpawnOptionData
    NumActorsParam: gbx_game_system_core.GbxParam
    SpawnPointGroupName: str



class EncounterWave:
    SpawnerStyle: SpawnerStyle
    Advancement: EncounterAdvanceData
    WarmupTimer: float
    Limits: unreal.WrappedArray[SpawnLimitData]
    SpawnPointGroupName: str



class SpawnLimitData:
    Tags: gameplay_tags.GameplayTagContainer
    DisallowedTypes: gameplay_tags.GameplayTagContainer
    TagFilterType: ESpawnPointFilter
    TotalLimit: gbx_game_system_core.GbxParam
    bLimitTotal: bool
    AliveLimit: gbx_game_system_core.GbxParam
    bLimitAlive: bool
    TagMatchType: gameplay_tags.EGameplayContainerMatchType



class EncounterAdvanceData:
    Type: EEncounterAdvanceType
    bUseTimer: bool
    Timer: float
    bUsePercent: bool
    Percent: float



class SpawnOptionDataSoftPath:
    SpawnOptionDataPathName: str
    SpawnOptionDataSubPathString: str



class SpawnManagerAsyncRequest:
    Context: engine.Actor
    SpawnFactory: SpawnFactory
    SpawnOptions: SpawnOptionData
    SpawnPointComponent: SpawnPointComponent
    SpawnerComponent: SpawnerComponent
    Owner: engine.Actor
    SpawnDetails: SpawnDetails



class SpawnDetails:
    Critical: ESpawnerCritical
    bOverrideCritical: bool
    RespawnStyle: ERespawnStyle
    bOverrideRespawnStyle: bool
    IrrelevantAction: EIrrelevantAction
    bOverrideIrrelevantAction: bool
    bCritical: bool



class SpawnManagerAsyncRequestEntry(SpawnManagerAsyncRequest): ...


class SpawnPreviewState(gbx_game_system_core.PreviewState):
    SpawnPointComponent: SpawnPointComponent
    PreviewFactories: unreal.WrappedArray[SpawnFactory]



class SpawnPointGroup:
    Name: str
    Color: core_uobject.Color
    TerritoryActorForThisGroup: engine.Actor
    SpawnPoints: unreal.WrappedArray[SpawnPoint]
    bRandomize: bool



class SpawnFactoryData:
    Factory: SpawnFactory
    WeightParam: gbx_game_system_core.GbxParam
    Probability: str
    AliveLimitType: ESpawnLimitType
    AliveLimitParam: gbx_game_system_core.GbxParam
    AliveLimit: int



class PointWidget:
    Point: core_uobject.Transform



class ESpawnAnimNotifyAction(enum.Enum):
    Stop = 0
    ESpawnAnimNotifyAction_MAX = 1


class EScriptedWarmup(enum.Enum):
    FirstWave = 0
    AllWaves = 1


class ESpawnerDrawStyle(enum.Enum):
    Wire = 0
    Solid = 1
    ESpawnerDrawStyle_MAX = 2


class EScriptedWarmupState(enum.Enum):
    Activated = 0
    Complete = 1


class EEncounterAdvanceType(enum.Enum):
    Any = 0
    EEncounterAdvanceType_MAX = 1


class ESpawnSystemStreamStyle(enum.Enum):
    MapStartAsynchronous = 0
    ESpawnSystemStreamStyle_MAX = 1


class ESpawnerType(enum.Enum):
    Static = 0
    ESpawnerType_MAX = 1
    Level = 2


class ESpawnerActorState(enum.Enum):
    Alive = 0
    Suspended = 1
    ESpawnerActorState_MAX = 2


class ESpawnPointUseType(enum.Enum):
    List = 0
    ManualGroup = 1
    ESpawnPointUseType_MAX = 2


class ESpawnPointFilter(enum.Enum):
    ESpawnPointFilter_MAX = 0
    NotAny = 1
    All = 2


class ESpawnLimitType(enum.Enum):
    Spawner = 0
    SpawnerGroup = 1


class ESpawnerCritical(enum.Enum):
    AlwaysSpawn = 0
    Critical = 1


class EIrrelevantAction(enum.Enum):
    Remove = 0
    Nothing = 1


class ERespawnStyle(enum.Enum):
    Level = 0
    Never = 1


class ESpawnStretchType(enum.Enum):
    StartPoint = 0
    EndPoint = 1
    ESpawnStretchType_MAX = 2

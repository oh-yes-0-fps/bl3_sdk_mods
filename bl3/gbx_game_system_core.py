from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import online_subsystem_utils
from . import gbx_runtime
from . import wwise_audio
from . import gbx_audio
from . import significance_manager
from . import aimodule
from . import gameplay_tasks
from . import level_sequence
from . import media_assets
from . import input_core
from . import anim_graph_runtime
from . import gameplay_tags
from . import immediate_physics
from . import animation_core
from . import gbx_anim_runtime_base


class StanceDataProvider(gbx_runtime.GbxDataAsset): ...


class StanceData(StanceDataProvider):
    MaxSpeed: StanceFloatValue
    MaxRotation: StanceFloatValue
    MaxAllowedAimOffset: StanceFloatValue
    bUseMaxAllowedAimOffset: bool
    AimRotationRate: StanceFloatValue
    bUseAimRotationRate: bool
    MaxIdleRotation: StanceFloatValue
    bUseMaxIdleRotation: bool
    StanceDataToShowAnimSystem: StanceData
    bOverrideSlowdownSpeed: bool
    SlowdownSpeed: StanceFloatValue
    bOverrideMaxAcceleration: bool
    MaxAcceleration: float
    bLockDodging: bool
    bLockTurns: bool
    bLockFootIK: bool
    bLockHandIK: bool
    bThisStanceAllowsFidgetAnims: bool
    WaitTimeBeforeFirstFidgetAnim: float
    PhysicalAnimation: PhysicalAnimationProfileAsset
    HitReactionLayer: unreal.UClass
    HitReactionData: HitReactionData


class GbxAnimTable(gbx_runtime.GbxDataAsset):
    TriggerAutofill: gbx_runtime.GbxTriggerProperty
    DataTable: engine.DataTable
    bScaleRateByMeshScale: bool

    def Autofill(self): ...


class GbxAction(unreal.UObject):
    bCanUseCDO: bool
    ActionSlotName: str
    ActionPriority: EGbxActionPriority
    InstanceDataType: core_uobject.ScriptStruct

    def OnServerEnd(self, ActionEndState: EGbxActionEndState, Actor: engine.Actor): ...
    def OnServerBegin(self, Actor: engine.Actor): ...
    def OnEnd(self, ActionEndState: EGbxActionEndState, Actor: engine.Actor): ...
    def OnBegin(self, Actor: engine.Actor): ...
    def K2_GetVectorRegisterValue(
        self, InName: str, OutVector: core_uobject.Vector
    ) -> bool: ...
    def K2_GetTimeRemaining(self) -> float: ...
    def K2_GetObjectRegisterValue(
        self, InName: str, OutObject: unreal.UObject
    ) -> bool: ...
    def K2_GetNameRegisterValue(self, InName: str, OutName: str) -> bool: ...
    def K2_GetMaxCurrentTime(self) -> float: ...
    def K2_GetIntRegisterValue(self, InName: str, OutInt: int) -> bool: ...
    def K2_GetFloatRegisterValue(self, InName: str, OutFloat: float) -> bool: ...
    def K2_GetCurrentTime(self) -> float: ...
    def K2_GetCurrentNormalizedTime(self) -> float: ...
    def K2_GetActor(self) -> engine.Actor: ...


class GbxAction_SimpleAnim(GbxAction):
    bStopAI: bool
    bAbortAI: bool
    bStopMovement: bool
    bDisableHitReactions: bool
    bUsePhysNoneWithRootMotion: bool
    bStopLook: bool
    bStopAimRotation: bool
    bStopHeadLook: bool
    bLockHeadLook: bool
    bDisableAvoidance: bool
    bTickAndRefreshBones: bool
    bDisableCollision: bool
    DisableCollisionChannels: unreal.WrappedArray[int]
    bEnableLoopHelper: bool
    bCanInterruptSameSlotAnims: bool
    bResetDynamicsOnBegin: bool
    bUsePhysicalAnimationProfile: bool
    PhysicalAnimationProfile: PhysicalAnimationProfileAsset
    bRestorePreviousPhysicalAnimationProfileOnEnd: bool
    bUseNewBoneSetFilter: bool
    NewBoneSetFilter: engine.GbxBoneSet
    bRestorePreviousBoneSetFilterProfileOnEnd: bool
    bResetBoneSetFilter: bool
    DefaultInterruptBlendOutTime: float
    bReleaseResourceFlagsOnAnimEnd: bool
    bEndActionOnBlendOut: bool

    def OnAnimEnd(self, Actor: engine.Actor): ...
    def K2_SetTickAndRefreshBones(self, bLockResource: bool): ...
    def K2_SetPhysNoneWithRootMotion(self, bEnable: bool): ...
    def K2_SetMovement(self, bDisable: bool): ...
    def K2_SetLook(self, bDisable: bool): ...
    def K2_SetHitReactions(self, bDisable: bool): ...
    def K2_SetHeadLookLocked(self, bLock: bool): ...
    def K2_SetHeadLook(self, bDisable: bool): ...
    def K2_SetCollision(self, bEnable: bool): ...
    def K2_SetAvoidance(self, bDisable: bool): ...
    def K2_SetAIThinking(self, bDisable: bool): ...
    def K2_SetAimRotation(self, bDisable: bool): ...


class GbxAISystemBase(aimodule.AISystem):
    GbxQueryManager: GbxQueryManager


class PreviewComponent(engine.PrimitiveComponent):
    bSpawnInPIE: bool
    bPreviewEnabled: bool
    PreviewActor: unreal.UClass
    PreviewState: PreviewState
    bEnabled: bool
    SkinnedMeshComponent: engine.SkinnedMeshComponent

    def OnBlueprintCompiled(self, BP: engine.Blueprint): ...


class GbxAction_Anim(GbxAction_SimpleAnim):
    DefaultAnims: AnimMeshList
    DefaultEndCondition: EGbxActionEndCondition
    AnimationSlot: str
    BlendInTime: float
    bPushBlendInTime: bool
    DefaultBlendOutTime: float
    bPushBlendOutTime: bool
    PlayRate: float
    bScalePlayrateWithCharacterScale: bool
    SourceCameraAlpha: float
    MontageCameraAlpha: float
    bDisableFootIk: bool
    bBody1stControlsDuration: bool
    bPlay1stPersonAnimationsOnRemotePlayers: bool
    AnimSlot3rd: str
    AnimSlot1st: str
    bHasAnimSlot3rdValue: bool
    bHasAnimSlot1stValue: bool
    bGodMode: bool
    bDemigodMode: bool
    bBlockCrouching: bool
    bBlockMantling: bool
    bEnableScaledRootMotion: bool
    bMaintainRootVelocity: bool
    bOverrideDuration: bool
    OverrideDuration: float
    bOverrideCount: bool
    OverrideCount: int
    bOverridePlayRate: bool
    OverridePlayRate: float
    BlendSpaceXRegisterName: str
    BlendSpaceYRegisterName: str

    def K2_SetMantlingBlocked(self, bBlocked: bool): ...
    def K2_SetGodMode(self, bEnable: bool): ...
    def K2_SetFootIK(self, bDisable: bool): ...
    def K2_SetDemigodMode(self, bEnable: bool): ...
    def K2_SetCrouchBlocked(self, bBlocked: bool): ...
    def K2_Resume(self): ...
    def K2_RepProceedToNextSection(self): ...
    def K2_RepJumpToNextSection(self): ...
    def K2_ProceedToNextSection(self): ...
    def K2_Pause(self): ...
    def K2_JumpToNextSection(self): ...


class TeamComponent(engine.ActorComponent):
    Team: Team
    TeamDefault: Team
    bSetTeamCollision: bool
    bIgnoreCollisionWithTeam: bool
    bInheritSourceTeamFromInstigator: bool
    SourceTeamComponent: TeamComponent

    def SetTeamToDefault(self): ...
    def SetTeamCollision(self, bOn: bool): ...
    def SetTeam(self, NewTeam: Team): ...
    def SetSourceTeamComponent(self, NewSourceTeamComponent: TeamComponent): ...
    def SetCollidesWithTeam(self, bCollidesWithTeam: bool): ...
    def OnRep_Team(self, OldTeam: Team): ...
    def OnRep_bIgnoreCollisionWithTeam(self): ...
    def IsNeutral(self, Actor: engine.Actor) -> bool: ...
    def IsHostile(self, Actor: engine.Actor) -> bool: ...
    def IsFriendly(self, Actor: engine.Actor) -> bool: ...
    def InitializeTeam(self, NewTeam: Team): ...
    def GetTeamCollisionChannel(self) -> ETeamCollisionChannel: ...
    def GetTeamAttitudeTowardsTeam(self, OtherTeam: Team) -> int: ...
    def GetTeamAttitudeTowardsActor(self, Actor: engine.Actor) -> int: ...


class GbxCharacter(engine.Character):
    GbxCharacterMovement: GbxCharacterMovementComponent
    TargetableComponent: TargetableComponent
    DamageComponent: DamageComponent
    DamageCauserComponent: DamageCauserComponent
    GbxAction: GbxActionComponent
    GameplayTagContainerComponent: GameplayTagContainerComponent
    DynamicPhysicalAnimationComponent: DynamicPhysicalAnimationComponent
    TargetingComponent: TargetingComponent
    PerceptionComponent: GbxPerceptionComponent
    FirstPersonComponent: FirstPersonComponent
    LandingData: LandingData
    JumpedImpact: ImpactData
    bPlayJumpAndLandImpactsOnAllFeet: bool
    FootstepImpact: ImpactData
    GenericHandImpact: ImpactData
    LadderHandImpact: ImpactData
    FootstepSockets: unreal.WrappedArray[str]
    HandAccessoryTags: unreal.WrappedArray[str]
    LandingDataTriggeredDelegate: Any
    OwnerPlayerController: GbxPlayerController
    OwnerAIController: aimodule.AIController
    PlayerMaster: GbxCharacter
    Pets: unreal.WrappedArray[GbxCharacter]
    CharacterMass: MassSelection
    SpawnCostSelection: SpawnCostSelection
    GbxMesh: GbxSkeletalMeshComponent
    bOrientEyeHeight: bool
    ViewSocket: str
    ViewSocketComponent: engine.SceneComponent
    ReplicatedPawnAttachState: ReplicatedPawnAttachState
    PawnAttachState: ReplicatedPawnAttachState
    BaseAimHeight: float
    bUseCustomBaseAimHeight: bool
    AimHeightFromGround: float
    CrouchedAimHeight: float
    bUseCustomCrouchedAimHeight: bool
    AimEyeHeightPct: float
    AimSocket: str
    AimSocketComponent: engine.SceneComponent
    FacingController: FacingController
    ClientTurnDelta: int
    InputComponentClass: unreal.UClass
    GestaltFoleyAccessory: gbx_audio.FoleyAccessoryComponent
    CachedFoleyMainComponent: gbx_audio.FoleyMainComponent
    GameplayTasksComponent: gameplay_tasks.GameplayTasksComponent
    LevelSequencePlayerController: level_sequence.LevelSequencePlayer
    LevelSequenceCollisionState: SavedCollision
    AnimGraphBoneSetFilter: engine.GbxBoneSet
    ActiveAnimGraphBoneSetFilterList: unreal.WrappedArray[AnimGraphBoneSet]
    SmartObjectBoneSetFilter: engine.GbxBoneSet
    DefaultBoneSetFilter: engine.GbxBoneSet
    ActionBoneSetFilter: engine.GbxBoneSet
    bPauseAIWhileFalling: bool

    def SetTeam(self, Team: Team): ...
    def SetPlayerMaster(self, NewPlayerMaster: GbxCharacter): ...
    def SetCharacterUIName(self, NewCharacterUIName: GbxUIName): ...
    def SetCharacterNameFromString(self, NewCharacterName: str): ...
    def SetCharacterName(self, NewCharacterName: str): ...
    def RotateCharacterTo(
        self, TargetRotation: core_uobject.Rotator, Duration: float, Easing: int
    ): ...
    def ReceiveOwnerPlayerControllerChanged(
        self, NewPlayerControllerOwner: GbxPlayerController
    ): ...
    def OnRep_ReplicatedPawnAttachState(self): ...
    def OnLandingDataTriggered(self, LandingInfo: LandingInfo, Index: int): ...
    def NetMulticast_TriggerHitReactionSound(
        self, Tag: gbx_audio.CharacterSoundTag
    ): ...
    def NetMulticast_PlayLanded(
        self,
        Hit: engine.HitResult,
        ImpactSpeed: float,
        bLandFromJump: bool,
        LandingDataOverride: LandingData,
    ): ...
    def NetMulticast_PlayJumped(self): ...
    def IsZoomed(self) -> bool: ...
    def GetTeamComponent(self) -> TeamComponent: ...
    def GetTeam(self) -> Team: ...
    def GetTargetingComponent(self) -> TargetingComponent: ...
    def GetTargetableComponent(self) -> TargetableComponent: ...
    def GetPerceptionComponent(self) -> GbxPerceptionComponent: ...
    def GetPawnAttachStatus(self) -> EPawnAttachStatus: ...
    def GetPawnAttachComponent(self) -> PawnAttachSlotComponent: ...
    def GetPawnAttachActor(self) -> engine.Actor: ...
    def GetLookAtLocation(self, OutWeight: float) -> core_uobject.Vector: ...
    def GetLookAt(
        self,
        HeadLocation: core_uobject.Vector,
        EyeLocation: core_uobject.Vector,
        HeadWeight: float,
    ) -> float: ...
    def GetFirstPersonMesh(self) -> engine.SkeletalMeshComponent: ...
    def GetFirstPersonComponent(self) -> FirstPersonComponent: ...
    def GetBlackboardComponent(self) -> aimodule.BlackboardComponent: ...
    def GetBlackboardAsset(self) -> aimodule.BlackboardData: ...
    def GetAvailableSocketNames(self, Array: unreal.WrappedArray[str]): ...
    def GetAimVectorStartLocation(self) -> core_uobject.Vector: ...
    def GetAimOffset(self) -> core_uobject.Rotator: ...
    def FindFirstPersonComponent(self) -> FirstPersonComponent: ...
    def DetachCharacter(self, LocationRule: engine.EDetachmentRule): ...
    def ClientRotateCharacterTo(
        self, TargetRotation: core_uobject.Rotator, Duration: float, Easing: int
    ): ...
    def CauseEveryoneToForgetMe(self): ...
    def AttachCharacterToComponent(
        self,
        Parent: engine.SceneComponent,
        SocketName: str,
        LocationRule: engine.EAttachmentRule,
        RotationRule: engine.EAttachmentRule,
        ScaleRule: engine.EAttachmentRule,
        bWeldSimulatedBodies: bool,
    ): ...
    def AttachCharacterToActor(
        self,
        ParentActor: engine.Actor,
        SocketName: str,
        LocationRule: engine.EAttachmentRule,
        RotationRule: engine.EAttachmentRule,
        ScaleRule: engine.EAttachmentRule,
        bWeldSimulatedBodies: bool,
    ): ...


class BalanceStateComponent(engine.ActorComponent):
    BalanceTableRowHandle: engine.DataTableRowHandle
    InheritedBalanceTableRowHandle: engine.DataTableRowHandle
    GameStage: int
    ExperienceLevel: int
    OnLevelChanged: Any
    bAutoRefreshInheritedBalanceWhenSourceChangesLevel: bool

    def SetGameStage(self, NewGameStage: int): ...
    def SetExperienceLevel(self, NewExperienceLevel: int): ...
    def OnRep_ExperienceLevel(self, OldExperienceLevel: int): ...
    def OnInheritedBalanceSourceLevelChanged(
        self,
        InheritedBalanceStateSource: BalanceStateComponent,
        OldExperienceLevel: int,
        NewExperienceLevel: int,
    ): ...
    def GetGameStage(self) -> int: ...
    def GetExperienceLevel(self) -> int: ...
    def GetBalanceTableRow(self) -> engine.DataTableRowHandle: ...


class GbxChildActorComponent(engine.ChildActorComponent):
    bAutoSpawnActor: bool
    bAutoDestroyActor: bool
    bDestroyExistingChildActorOnSpawn: bool
    bDeferChildActorClassUpdate: bool
    bClearChildActorReferenceToMeWhenChildActorIsDetached: bool
    OnChildActorSpawned: Any

    def SpawnChildActor(self): ...
    def DespawnChildActor(self): ...


class AnimNotify_PawnAttachSlotTransition(engine.AnimNotify):
    bTriggerOnFirstPersonMesh: bool
    bDetach: bool
    bAttach: bool


class AttributeEffectMutatorData(gbx_runtime.GbxDataAsset): ...


class GbxAnimInstance(engine.AnimInstance):
    GbxSkeletalMeshComponent: GbxSkeletalMeshComponent
    AnimStateMachineDefinitions: unreal.WrappedArray[GbxAnimStateMachineDefinition]
    RuntimeStateMachines: unreal.WrappedArray[RuntimeStateMachineData]
    AnimTableMap: Any
    ManagerRuntime: engine.GbxStateManagerRuntime
    bEarlyBindBoneSetDelegates: bool

    def GetAnimTableSequence(self, AnimTable: GbxAnimTable) -> engine.AnimSequence: ...
    def CanUseAnimTable(self, AnimTable: GbxAnimTable) -> bool: ...


class GbxCustomizationData(gbx_runtime.GbxDataAsset):
    CustomizationName: str
    CustomizationDescription: str
    IconFrameName: str
    UIStats: unreal.WrappedArray[UIStatPriorityData]
    ItemCardTypeFrameName: str
    PreviewImage: Any
    PurchasePrice: AttributeInitializationData
    CustomizationType: GbxCustomizationTypeData
    CustomizationTargetAssets: unreal.WrappedArray[CustomizationAssetEntry]
    bUnlockedByDefault: bool
    bEquippedByDefault: bool
    DefaultSkin: GbxCustomizationData
    DependentBody: GbxCustomizationData

    def RemoveCustomizationFromActor(self, TargetActor: engine.Actor) -> bool: ...
    def OnCustomizationAssetLoaded(self): ...
    def K2_PlayAction(
        self, TargetActor: engine.Actor, ActionData: ActionState_Base
    ) -> GbxAction: ...
    def IsLoading(self) -> bool: ...
    def IsLoaded(self, OptionalCustomizationId: int) -> bool: ...
    def AsyncLoadCustomizationAssets(self, LoadedDelegate: Any): ...
    def ApplyCustomizationToActor(
        self, TargetActor: engine.Actor, OptionalCustomizationId: int
    ) -> bool: ...


class ActorPartSelectionData(gbx_runtime.GbxDataAsset):
    BaseSelectionData: ActorPartSelectionData
    PartSetData: ActorPartSetData
    PartSetDataGuid: core_uobject.Guid
    RuntimePartList: RuntimeActorPartListData
    RuntimePartListGuid: core_uobject.Guid
    InheritedRuntimePartListGuid: core_uobject.Guid


class AttributeValueResolver(unreal.UObject):

    def SetValueForAttribute(
        self, Attribute: GbxAttributeData, Context: unreal.UObject, Value: float
    ) -> bool: ...
    def GetValueForAttribute(
        self, Attribute: GbxAttributeData, Context: unreal.UObject
    ) -> float: ...


class GbxAreaComponent(engine.PrimitiveComponent):
    DetectionVolumes: unreal.WrappedArray[engine.Volume]
    bWorldAreaVolume: bool
    DetectionRadius: float
    DetectionHalfHeight: float
    bWorldAreaRadius: bool
    bManualTest: bool
    OnPlayerEnteredArea: Any
    OnPlayerExitedArea: Any
    DrawStyle: EGbxAreaDrawStyle
    PlayersDetected: unreal.WrappedArray[engine.PlayerController]

    def AreaTest(self): ...


class EffectCollectionData(unreal.UObject):

    def StaticGetWwiseEvent(
        self, Collection: unreal.UClass, ContextObject: unreal.UObject
    ) -> wwise_audio.WwiseEvent: ...
    def StaticGetParticleEffectAndWwiseEvent(
        self,
        Collection: unreal.UClass,
        ContextObject: unreal.UObject,
        ParticleEffect: engine.ParticleSystem,
        WwiseEvent: wwise_audio.WwiseEvent,
    ): ...
    def StaticGetParticleEffect(
        self, Collection: unreal.UClass, ContextObject: unreal.UObject
    ) -> engine.ParticleSystem: ...
    def GetWwiseEvent(
        self, ContextObject: unreal.UObject
    ) -> wwise_audio.WwiseEvent: ...
    def GetParticleEffectAndWwiseEvent(
        self,
        ContextObject: unreal.UObject,
        ParticleEffect: engine.ParticleSystem,
        WwiseEvent: wwise_audio.WwiseEvent,
    ): ...
    def GetParticleEffect(
        self, ContextObject: unreal.UObject
    ) -> engine.ParticleSystem: ...


class EnvQueryGenerator_TargetableActors(aimodule.EnvQueryGenerator):
    DistanceMax: aimodule.AIDataProviderFloatValue
    TargetSkipDistanceCheckCondition: gbx_runtime.GbxCondition
    bAllowNonTargetableActors: bool
    bAllowDeadActors: bool
    bAllowQuerier: bool
    bAllowHostiles: bool
    bAllowFriendlies: bool
    bAllowNeutrals: bool
    TargetCondition: gbx_runtime.GbxCondition
    TagQuery: ActorTagCompositeQuery
    AllowedTypes: unreal.WrappedArray[Any]
    bUseAllowedTypes: bool
    DisallowedTypes: unreal.WrappedArray[Any]
    bUseDisallowedTypes: bool
    AllowedTypesCache: unreal.WrappedArray[unreal.UClass]
    DisallowedTypesCache: unreal.WrappedArray[unreal.UClass]


class UsableComponent(engine.ActorComponent):
    HoldToUseSettings: HoldToUseSettings
    UsabilityData: UsabilityDataSelection
    bUseEnabledCondition: bool
    EnabledCondition: gbx_runtime.GbxCondition
    PrimaryUseDefSelection: UseDefSelection
    PrimaryHoldUseDefSelection: UseDefSelection
    SecondaryUseDefSelection: UseDefSelection
    SecondaryHoldUseDefSelection: UseDefSelection
    bCanBeUsedFromVehicle: bool
    bCanBeUsedFromMech: bool
    bCanOnlyBeUsedByOwner: bool
    bDefaultIsBackupPrimaryData: bool
    UsablePriority: int
    bWantsMaxUseCount: bool
    MaxUseCount: int
    CurrentUseCount: int
    RequiredComponentNames: unreal.WrappedArray[str]
    bUseAngleRestriction: bool
    AngleRestriction: UsableAngleRestriction
    bRequiresNetAuthority: bool
    HeaderName: str
    OnUsed: Any
    OnUsedPrimary: Any
    OnUsedPrimaryHold: Any
    OnUsedSecondary: Any
    OnUsedSecondaryHold: Any
    OnLookedAt: Any
    OnLookedAwayFrom: Any

    def SetUsableLocked(self, bLocked: bool, Reason: str): ...
    def SetInteractionHeader(self, NewHeaderName: str): ...
    def ResetUseCount(self): ...
    def K2_GetOptionalErrorText(self) -> str: ...
    def K2_CanBeUsed(self, Query: UsabilityQuery) -> bool: ...
    def GetValidPrimitiveComponentNames(
        self, ComponentNames: unreal.WrappedArray[str]
    ): ...
    def GetInteractionHeader(self) -> str: ...


class GbxGameplayGlobals(gbx_runtime.GbxDataAsset):
    ShieldHealthType: HealthTypeData
    ProjectileReflectionQuery: aimodule.EnvQuery
    ProjectileReflectionSpeedScale: float
    ProjectileHitRegionRicochetSpeedScale: float
    ProjectileReflectionInaccuracy: AttributeInitializationData
    ProjectileReflectionImpact: ImpactData
    ProjectileSelfReflectionImpact: ImpactData
    DefaultUseDefinition: UsableTypeDefinition
    InventoryScoreValueInitializer: AttributeInitializationData
    GlobalAIData: GlobalAIData
    ExplosionWindRadiusModifier: float
    MinExplosionRadiusToTriggerRadialBlur: float
    DefaultExplosionSettings: unreal.WrappedArray[DefaultExplosionSettings]
    ShortDurationTinnitusEvent: wwise_audio.WwiseEvent
    MediumDurationTinnitusEvent: wwise_audio.WwiseEvent
    LongDurationTinnitusEvent: wwise_audio.WwiseEvent
    ExplosionSoundStackingMaxDistanceSquared: float
    ExplosionSoundStackingPreventionDelay: float
    DefaultFeedbackTable: engine.DataTable
    KillStatMap: Any
    GameStatLists: unreal.WrappedArray[GameStatList]
    GameChallengeLists: unreal.WrappedArray[ChallengeList]
    MantleGlobals: MantleGlobalData


class GbxGameMode(engine.GameMode): ...


class GbxGameState(engine.GameState):
    ChallengeManager: ChallengeManager
    StatsManager: GameStatsManager
    CustomizationManager: GbxCustomizationManager
    HostPlayerState: engine.PlayerState
    ImpactDecalManager: ImpactDecalManager
    GameInstanceId: core_uobject.Guid
    GameInstanceTime: float
    GameInstanceTimeUpdateRate: float
    CustomizationManagerClass: unreal.UClass
    bRepPlayersOnly: bool

    def SpawnEmitterAtLocationMulticastImpl(
        self,
        EmitterTemplate: engine.ParticleSystem,
        Location: core_uobject.Vector,
        Rotation: core_uobject.Rotator,
        Scale: core_uobject.Vector,
        bAutoDestroy: bool,
        ParameterEvaluationContext: unreal.UObject,
    ): ...
    def SpawnEmitterAtLocationMulticast(
        self,
        WorldContextObject: unreal.UObject,
        EmitterTemplate: engine.ParticleSystem,
        Location: core_uobject.Vector,
        Rotation: core_uobject.Rotator,
        Scale: core_uobject.Vector,
        bAutoDestroy: bool,
        ParameterEvaluationContext: unreal.UObject,
    ): ...
    def SpawnEmitterAtComponentSocketMulticast(
        self,
        WorldContextObject: unreal.UObject,
        EmitterTemplate: engine.ParticleSystem,
        Component: engine.SceneComponent,
        Socket: str,
        bAutoDestroy: bool,
        ParameterEvaluationContext: unreal.UObject,
    ): ...
    def SpawnEmitterAtActorSocketMulticast(
        self,
        WorldContextObject: unreal.UObject,
        EmitterTemplate: engine.ParticleSystem,
        Actor: engine.Actor,
        Socket: str,
        bAutoDestroy: bool,
        ParameterEvaluationContext: unreal.UObject,
    ): ...
    def PlayImpactMulticast(
        self,
        ImpactData: ImpactData,
        ImpactInstigator: engine.Actor,
        HitResult: ReplicatedImpactHitResult,
        ResponseParams: ImpactResponseParams,
    ): ...
    def PlayHitRegionImpactMulticast(
        self,
        HitRegion: HitRegionData,
        ImpactInstigator: engine.Actor,
        HitResult: ReplicatedImpactHitResult,
    ): ...
    def OnRep_StatsManager(self): ...
    def OnRep_HostPlayerState(self): ...
    def OnRep_GameInstanceTime(self): ...
    def OnRep_GameInstanceId(self): ...
    def OnRep_bPlayersOnly(self): ...


class GbxCharacterAnimInstance(GbxAnimInstance):
    HeadLookAtLocation: core_uobject.Vector
    EyeLookAtLocation: core_uobject.Vector
    HeadLookAtPercentage: float
    LookAtWeight: float
    bLookAtBlinkStarted: bool
    ActiveStanceData: str
    ActiveStanceType: str
    CombatStance: StanceDataProvider
    PassiveStance: StanceDataProvider
    StanceData: StanceData
    StanceType: StanceType
    StanceComponent: StanceComponent
    bInCombatStance: bool
    bInPassiveStance: bool
    IsInAir: bool
    IsCrouching: bool
    bIsFlying: bool
    bIsFalling: bool
    bHasBeenLaunched: bool
    bJumped: bool
    bForceFallingState: bool
    MaxWalkSpeed: float
    MaxSprintSpeed: float
    MaxWalkSpeedCrouched: float
    Speed2D: float
    Speed2DRaw: float
    VelocityZ: float
    ForwardDirection: float
    RightDirection: float
    UpDirection: float
    Acceleration: core_uobject.Vector
    Direction: float
    BodyYaw: float
    ReverseDirection: float
    RotationalVelocity: core_uobject.Rotator
    GroundLocation: core_uobject.Vector
    Radius: float
    WantsToTurn: bool
    TurnAmount: float
    TurnIsActive: bool
    MaxPredictedTurnDegrees: float
    MaxPredictedTurnTime: float
    Pitch: float
    Yaw: float
    AimBlendWeight: float
    AimFacingLocation: core_uobject.Vector
    bCanAimInPassiveStance: bool
    bUpdateFootIK: bool
    bUpdateHandIK: bool
    LeftHandIKWeight: float
    RightHandIKWeight: float
    LeftHandGripWeight: float
    RightHandGripWeight: float
    bUseLegIkBaseClass: bool
    LeftHandWeaponIKOffset: core_uobject.Transform
    RightHandWeaponIKOffset: core_uobject.Transform
    LeftHandWorldIKTarget: core_uobject.Transform
    bHasLeftHandWorldIKTarget: bool
    bBlueprintForceLeftHandWorldIKTarget: bool
    LeftHandIKTargetSocketName: str
    RightHandWorldIKTarget: core_uobject.Transform
    bHasRightHandWorldIKTarget: bool
    bBlueprintForceRightHandWorldIKTarget: bool
    RightHandIKTargetSocketName: str
    LeftFootWorldIKTargetLocation: core_uobject.Vector
    LeftFootWorldIKTargetRotation: core_uobject.Rotator
    RightFootWorldIKTargetLocation: core_uobject.Vector
    RightFootWorldIKTargetRotation: core_uobject.Rotator
    bHasFootWorldIKTargets: bool
    AINavYaw: float
    AINavTurnBlendDegrees: float
    AINavTransitionBlendDegrees: float
    AINavHopDirection: core_uobject.Vector2D
    AINavHopDistance: float
    AINavServerData: NavAnimServerData
    AINavClientData: NavAnimClientData
    AINavState_IdleAlphaTime: float
    AINavState_IdleAlpha: float
    bAINavState_Idle: bool
    bAINavState_Move: bool
    bAINavState_Start: bool
    bAINavState_Stop: bool
    bAINavState_Turn: bool
    BlendPoints: EGbxCharacterBlendPoints
    bAINavWantsForward: bool
    bAINavWantsBackward: bool
    bAINavWantsLeft: bool
    bAINavWantsRight: bool
    bAINavIsMoving2D: bool
    bAINavIsStill2D: bool
    AINavPreviewTableIndex: int
    AINavPreviewDesiredState: ENavAnimState
    bAINav_UseDesired: bool
    bAINav_CanStretch: bool
    MeshScale: float
    AINavPreviewCurrentState: ENavAnimState
    StartTransitionTimeToEvaluate: float
    StopTransitionTimeToEvaluate: float
    TurningRotationTimeToEvaluate: float
    ActiveAnimBoneSetFilter: engine.GbxBoneSet
    PrevAnimBoneSetFilter: engine.GbxBoneSet
    GaitScalingSettings: engine.GaitScalingSettings
    FacialEmoteWeight: float
    DesiredFacialEmoteWeight: float
    FacialEmoteWeightAlphaSpeed: float
    DesiredActionWeight: float
    BoneSetTransitionActionWeight: float
    BoneSetBlendWeight: float
    BoneSetTransitionBlendType: engine.EBoneSetTransitionBlendType
    BoneSetTransitionBlendSpeed: float
    BoneSetBlendSpeed: float
    DefaultBoneSetBlendSpeed: float
    DefaultBoneSetTransitionBlendSpeed: float

    def SetDesiredFacialEmoteWeight(self, Weight: float, BlendTime: float): ...
    def OnStanceChanged(self): ...


class DamageData(unreal.UObject):
    Damage: AttributeInitializationData
    DamageMultiplier: AttributeInitializationData
    DamageAreaType: DamageAreaType
    DamageSource: unreal.UClass
    DamageType: unreal.UClass
    ConditionalDamageModifiers: unreal.WrappedArray[ConditionalDamageModifier]
    bApplyUpwardForce: bool
    UpwardForceScalar: float
    ImpactForceSelection: ForceSelection
    GoreModifier: float
    GibModifier: float
    bImpactForceFallsOff: bool
    HitRotationOffset: core_uobject.Rotator
    bSimulatedOnClients: bool
    bForceNoCrit: bool
    bCanBeExecutedAsync: bool
    MaxAsyncExecutionDeferTime: float
    HitStartSocketOrBone: str
    bBaseTransformComesFromActorTransform: bool
    HitStartOffset: core_uobject.Vector
    HitStartRotationOffset: core_uobject.Rotator
    AttitudeDamageRules: AttitudeDamageRules
    bEnforceAttitudeRulesForHealing: bool
    bCanHurtSelf: bool
    bCanHurtInstigator: bool
    bCausesDamageOverTime: bool
    bAllowMultipleInstances: bool
    bHitEachTargetOnlyOnce: bool
    bCacheSourceLocationAndRotation: bool
    MaxDamageDuration: float
    DamageInterval: float
    bCancelDamageOverTimeWhenOwnerDies: bool
    DamageOverTimeParticleSystem: engine.ParticleSystem
    DamageOverTimeAudioEventStart: wwise_audio.WwiseEvent
    DamageOverTimeAudioEventStop: wwise_audio.WwiseEvent
    InstigatorFeedback: FeedbackData
    TargetFeedbacks: unreal.WrappedArray[FeedbackData]
    ImpactData: ImpactData
    ExplosionData: ExplosionData
    DefaultExplosionParticles: engine.ParticleSystem
    SignificanceEvent: GbxSignificanceEvent
    DefaultAudioEvent: wwise_audio.WwiseEvent
    DefaultExplosionImpactData: ImpactData
    DefaultExplosionDecalOverride: engine.MaterialInterface
    bUseExplosionSizeForDecal: bool
    bOnlyDrawParticleIfFacingDamage: bool
    ScreenParticleParams: ScreenParticleInitParams
    PlayerAudioEvent: wwise_audio.WwiseEvent

    def OnKilledEnemy(
        self,
        DamageInstigator: engine.Actor,
        DamageCauser: engine.Actor,
        DamageTarget: engine.Actor,
        Details: DamageDataEventDetails,
    ): ...
    def OnHitFriendly(
        self,
        DamageInstigator: engine.Actor,
        DamageCauser: engine.Actor,
        DamageTarget: engine.Actor,
        Details: DamageDataEventDetails,
    ): ...
    def OnHitEnemy(
        self,
        DamageInstigator: engine.Actor,
        DamageCauser: engine.Actor,
        DamageTarget: engine.Actor,
        Details: DamageDataEventDetails,
    ): ...
    def OnHitAnyAttitude(
        self,
        DamageInstigator: engine.Actor,
        DamageCauser: engine.Actor,
        DamageTarget: engine.Actor,
        Details: DamageDataEventDetails,
    ): ...


class ProjectileHomingComponent(engine.ActorComponent):
    bMoveDirectlyToTarget: bool
    TurnSpeed: float
    bChangeTurnSpeed: bool
    FinalTurnSpeed: float
    TurnAcceleration: float
    TrueTargetDistance: float
    TrueTargetTime: float
    OverrideHomingSpeed: float
    AccelerationScale: float
    HomingTarget: engine.Actor
    HomingTargetComponent: engine.SceneComponent
    HomingSocketOverride: str
    HomingTargetLocation: core_uobject.Vector
    ReachDistance: float
    ReachDistanceSquared: float
    HomingTargetLocalOffset: core_uobject.Vector
    StopHomingDistance: float
    OnStopHomingDistanceReached: Any
    OnReachedTargetLocation: Any
    bHomeIn: bool
    ProjectileMovement: engine.ProjectileMovementComponent
    Projectile: engine.Actor
    bModifyDefault: bool

    def ToggleHoming(self): ...
    def SetHomeIn(self, bEnabled: bool): ...
    def SetAssociatedProjectileMovement(
        self, ProjectileMovementComponent: engine.ProjectileMovementComponent
    ): ...
    def GetHomingLocation(self) -> core_uobject.Vector: ...


class HitReactionLayer(unreal.UObject):
    bStackable: bool


class AttributeContextResolver(unreal.UObject):
    ComponentTypeToFurtherResolveTo: Any

    def GetContextForAttribute(
        self, Attribute: GbxAttributeData, ContextSource: unreal.UObject
    ) -> unreal.WrappedArray[unreal.UObject]: ...


class SpawnPatternData(gbx_runtime.GbxDataAsset):

    def CalculateSpawnPoint(
        self, Inputs: SpawnPatternInputs, Result: SpawnPatternResult
    ): ...


class PhysicsSpawnPatternData(SpawnPatternData):
    bEnableSpeedRange: bool
    bEnableAngularSpeedRange: bool
    bApplySpeedAsImpulse: bool
    bApplyAngularSpeedAsImpulse: bool
    bPickRandomPointInActorBounds: bool
    bScaleSpeedByIncomingImpulse: bool
    Speed: float
    MaxSpeed: float
    Direction: RelativeDirectionData
    AngularSpeed: float
    MaxAngularSpeed: float
    RotationAxis: RelativeDirectionData
    ActorBoundsScale: core_uobject.Vector


class GbxPlayerCameraManager(engine.PlayerCameraManager):
    GbxPCOwner: GbxPlayerController


class StatusEffectData(engine.DataAsset):
    StackingStrategy: StatusEffectStackingStrategyData
    AttributeEffects: unreal.WrappedArray[AttributeEffect]
    bDoesDamageOverTime: bool
    DamageType: unreal.UClass
    DamageSourceClass: unreal.UClass
    GameplayTags: gameplay_tags.GameplayTagContainer


class CharacterAttributeContextResolver(AttributeContextResolver): ...


class AttributePropertyValueResolver(AttributeValueResolver):
    PropertySupportsModifierRemoval: bool
    Property: engine.ParsedProperty


class UIStatData(gbx_runtime.GbxDataAsset):
    Description: str
    bCanDisplayMultipleTimes: bool
    bBiggerIsBetter: bool
    BasePriority: float
    SectionName: str
    IconFrameName: str

    def K2_ShouldDisplayStat(self, Context: unreal.UObject) -> bool: ...
    def K2_GetValueText(
        self, Context: unreal.UObject, Collector: UIStatCollector
    ) -> str: ...
    def K2_GetComparisonValue(
        self, Context: unreal.UObject, Collector: UIStatCollector
    ) -> float: ...
    def EnumerateSectionNames(self, OutSectionNameList: unreal.WrappedArray[str]): ...
    def ComputeAttributeModification(
        self, Attribute: GbxAttributeData, bScale: bool, Collector: UIStatCollector
    ) -> float: ...


class UIStatData_Numeric(UIStatData):
    ValueStyle: EUIStatValueStyle
    SignStyle: EUIStatValueSignStyle
    RoundingMode: EUIStatValueRoundingMode
    bDisplayAsPercentage: bool
    bDisplayPercentAsFloat: bool
    bDisplayAsInverse: bool
    bDisplayPlusSign: bool
    bDisplayAsOneMinus: bool
    bCalculateWithReductionMath: bool
    bUseFormatText: bool
    bEnableValueRemapping: bool
    bUseSupplementalStatFormatText: bool
    bUseMinValueCondition: bool
    bUseMaxValueCondition: bool
    bMinOrMaxValueCondition: bool
    MinValueCondition: AttributeInitializationData
    MaxValueCondition: AttributeInitializationData
    Condition: gbx_runtime.GbxCondition
    FloatPrecision: int
    FormatText: str
    ValueRemapping: UIStatValueRemappingData
    SupplementalStat: UIStatData_Numeric
    SupplementalStatCombinationMethod: EUIStatCombinationMethod
    SupplementalStatCondition: gbx_runtime.GbxCondition
    SupplementalStatFormatText: str


class AchievementUtility(unreal.UObject): ...


class GbxAction_CoordinatedEffect(GbxAction):
    bInfiniteDuration: bool
    bLoop: bool
    bCensored: bool
    bDestroyActorOnEnd: bool
    bUnhideActorOnBegin: bool
    bHideActorOnEnd: bool
    Duration: float
    NextEffect: unreal.UClass
    PermanentGroupTag: str
    OverrideMaterial: engine.MaterialInterface
    MaskMaterial: engine.MaterialInterface
    GlowMaterial: engine.MaterialInterface
    ConditionalOverrideMaterials: unreal.WrappedArray[
        CoordinatedConditionalMaterialData
    ]
    MaterialScalarParameters: unreal.WrappedArray[CoordinatedScalarParameter]
    MaterialVectorParameters: unreal.WrappedArray[CoordinatedVectorParameter]
    InheritedMaterialParameters: unreal.WrappedArray[str]
    InheritMaterialParametersMethod: engine.EMaterialParameterCopyMethod
    bInheritAllMaterialParameters: bool
    bOverwriteInstancedMaterialParameters: bool
    bApplyToTranslucentMaterials: bool
    bPermanentMaterialOverride: bool
    bAlwaysRestoreMaterialParametersAtEnd: bool
    bApplyMaterialParametersToBothOverrideAndMaskGlow: bool
    ExcludedMaterialStaticParameters: unreal.WrappedArray[str]
    ParticleEffects: unreal.WrappedArray[CoordinatedParticleSystemData]
    ParticleParameters: unreal.WrappedArray[CoordinatedParticleSystemParameterData]
    ParticleSpeedMultiplier: float
    OwnedParticleAction: ECoordinatedOwnedParticleAction
    bAlwaysRestoreParticleParametersAtEnd: bool
    bHideOwnedParticles: bool
    AudioEffects: unreal.WrappedArray[CoordinatedAudioData]
    LightParameters: unreal.WrappedArray[CoordinatedLightParameterData]

    def SetConstantMaterialVectorParamValue(
        self, ParamName: str, Color: core_uobject.LinearColor
    ): ...


class GbxAction_Gib(GbxAction):
    MaxGibCount: int
    Gibs: unreal.WrappedArray[GibData]
    GibMinScale: float
    GibMaxScale: float
    GibSpawnPattern: SpawnPatternData
    GibMassScale: float
    GibActorClass: unreal.UClass
    GibEffect: ImpactResponseEffect
    GibEffectScale: float
    GibParticle: engine.ParticleSystem
    GibSound: wwise_audio.WwiseEvent


class GbxAction_Loop(GbxAction_SimpleAnim):
    AnimStart: AnimMeshList
    AnimLoopList: unreal.WrappedArray[WeightedAnim]
    AnimStop: AnimMeshList
    BlendInTime: float
    BlendOutTime: float
    StartToLoopBlendTime: float
    LoopToLoopBlendTime: float
    LoopToStopBlendTime: float
    AnimSlot: str
    bLetLoopFinish: bool
    LoopCount: GbxParam
    bUseLoopCount: bool
    LoopTime: GbxParam
    bUseLoopTime: bool
    LoopCondition: gbx_runtime.GbxCondition
    bUseLoopCondition: bool
    AnimData3rd: LoopAnimData
    bPlay3rd: bool
    AnimData1st: LoopAnimData
    bPlay1st: bool
    AnimLoop: AnimMeshList

    def OnStop(self, Actor: engine.Actor): ...
    def OnLoop(self, Actor: engine.Actor): ...
    def K2_StopLooping(self): ...


class GbxAction_PhysicalAnim(GbxAction_Anim):
    RootMotionControl: EPhysicalAnimationRootMotionControl
    MovementLockMode: EGbxPhysicalActionMovementLockMode
    DynamicBoneActivationMode: EGbxPhysicalActionDynamicBoneActivationMode
    FatigueParams: BoneFatigueParams
    BeginCondition: EGbxPhysicalActionBeginCondition
    PhysicalBeginConditionFlags: int
    PhysicalEndConditionFlags: int
    PhysicalEndCondition: EGbxPhysicalActionEndCondition
    CustomForceMultiplier: float
    UpwardForceMultiplier: float
    bForceAppliedAtLocation: bool
    bHasValidHitForce: bool

    def K2_GetDynamicBodyState(
        self, AngularThreshold: float
    ) -> EGbxPhysicalActionDynamicBodyState: ...
    def K2_FixupDynamicToKinematicIssues(self, AngularThreshold: float): ...


class GbxAction_PhysicalDeath(GbxAction_PhysicalAnim):
    PhysicalAnimationDelayTime: float
    bCapPhysicalAnimationDelayToAnimationDuration: bool
    PrematurePhysicalAnimationIgnoreBodyNames: unreal.WrappedArray[str]
    bAllowPrematurePhysicalAnimation: bool
    bTearOffOnDeath: bool
    MaxRagdollTime: float


class AimAssistParameters(gbx_runtime.GbxDataAsset): ...


class GbxPlayerController(engine.PlayerController):
    GbxCharacter: GbxCharacter
    PrimaryCharacter: GbxCharacter
    RecentDamageTrackingComponent: RecentDamageTrackingComponent
    CurrentProfile: GbxProfile
    InputComponentClass: unreal.UClass
    PlayerInputClass: unreal.UClass
    AimAssistStrategyClass: unreal.UClass
    CheatClassGbx: core_uobject.SoftClassPath
    OnPrimaryCharacterChanged: Any
    OnPauseChanged: Any
    CachedGlyphMode: EGbxGlyphSetOption
    TargetingComponent: TargetingComponent
    TargetableComponent: TargetableComponent
    TeamComponent: TeamComponent
    PerceptionComponent: GbxPerceptionComponent
    FirstPersonComponent: FirstPersonComponent
    AimAssistStrategy: AimAssistStrategy
    WwiseListener: wwise_audio.WwiseListenerComponent
    ActiveTrackedFeedbacks: unreal.WrappedArray[ActiveTrackedFeedback]
    bUsingGamepad: bool
    CinematicModeStack: unreal.WrappedArray[CinematicModeData]
    CinematicMode: CinematicModeData
    ScreenParticleManagerComponent: ScreenParticleManagerComponent

    def SetTeam(self, Team: Team): ...
    def ServerRequestPawnSlotDetach(self, Occupant: engine.Pawn): ...
    def ServerCanSplitscreenJoin(self, ControllerId: int): ...
    def PushCinematicMode(self, InCinematicMode: CinematicModeData): ...
    def PopCinematicMode(self, InCinematicMode: CinematicModeData): ...
    def OnRep_PrimaryCharacter(self): ...
    def OnRep_CinematicMode(self): ...
    def OnPrimaryCharacterChanged__DelegateSignature(
        self, NewCharacter: GbxCharacter
    ): ...
    def OnPausedChangedDelegate__DelegateSignature(self, bPaused: bool): ...
    def IsUsingGamepad(self) -> bool: ...
    def GetTeamComponent(self) -> TeamComponent: ...
    def GetTeam(self) -> Team: ...
    def GetTargetingComponent(self) -> TargetingComponent: ...
    def GetTargetableComponent(self) -> TargetableComponent: ...
    def GetPrimaryCharacter(self) -> GbxCharacter: ...
    def GetPlayerViewportSize(self, SizeX: int, SizeY: int): ...
    def GetPlayerViewportOffset(self, OffsetX: int, OffsetY: int): ...
    def GetPlayerProfile(self) -> GbxProfile: ...
    def GetGbxPerceptionComponent(self) -> GbxPerceptionComponent: ...
    def DeprojectViewportPositionToWorld(
        self,
        ViewportX: float,
        ViewportY: float,
        WorldLocation: core_uobject.Vector,
        WorldDirection: core_uobject.Vector,
        bUseForegroundProjection: bool,
    ) -> bool: ...
    def DebugCategory(self, CategoryName: str): ...
    def ClientStopFeedback(self, Data: FeedbackData): ...
    def ClientPlayWwiseEvent(self, Event: wwise_audio.WwiseEvent): ...
    def ClientPlayFeedback(
        self,
        Data: FeedbackData,
        Scale: float,
        bLoop: bool,
        SourceContext: unreal.UObject,
    ): ...
    def ClientPerformFeedbackAtLocation(
        self,
        FeedbackData: FeedbackData,
        SourceLocation: core_uobject.Vector,
        bLoop: bool,
        SourceContext: unreal.UObject,
        RangedOverrides: RangedDistanceOverrides,
    ): ...
    def ClientPerformFeedback(
        self, FeedbackData: FeedbackData, SourceContext: unreal.UObject
    ): ...
    def ClientNotifyActivateCheckpoint(self): ...
    def ClientCanSplitscreenJoin(self, ControllerId: int, bCanJoin: bool): ...
    def ClientApplyDamageDataPresentation(
        self, DamageData: DamageData, PlayerPresentation: PlayerDamageDataPresentation
    ): ...
    def Client_StopGbxFeedback(
        self, Data: GbxFeedbackData, SourceContext: unreal.UObject
    ): ...
    def Client_PlayGbxFeedback(
        self,
        Data: GbxFeedbackData,
        bIs3D: bool,
        bLoop: bool,
        Scale: float,
        SourceContext: unreal.UObject,
        SourceLocation: core_uobject.Vector,
        EffectFalloffMinDistance: float,
        EffectFalloffMaxDistance: float,
    ): ...
    def ClearCinematicMode(self): ...
    def ClearAndSetCinematicMode(self, InCinematicMode: CinematicModeData): ...


class AimAssistStrategy(unreal.UObject): ...


class GbxAssetManager(engine.AssetManager):
    StartupAssetTypes: unreal.WrappedArray[StartupAssetTypeData]
    StartupAssetFiles: unreal.WrappedArray[str]


class AssetMappingData(gbx_runtime.GbxDataAsset):
    ChallengesMap: Any
    GameStatDataMap: Any
    CustomizationDataMap: Any
    MissionsMap: Any
    ObjectiveSetsMap: Any
    InventoryCategoryMap: Any
    UINamesMap: Any


class Challenge(unreal.UObject):
    RegisteredOwner: ChallengesComponent
    ParentChallenges: unreal.WrappedArray[unreal.UClass]
    ChallengeName: str
    Description: str
    CompletedDescription: str
    bShared: bool
    bRepeatable: bool
    bHideInUI: bool
    bShowActivationUI: bool
    bShowProgressUI: bool
    bShowCompletionUI: bool
    bShowAsUndiscoveredUntilProgressed: bool
    AssociatedMapName: str
    ChallengeType: EChallengeType
    StatChallengeTests: unreal.WrappedArray[StatChallengeTest]
    bCompleteIfGoalValueReached: bool
    bResetProgressWhenGoalValueReached: bool
    ProgressGoalInfo: unreal.WrappedArray[ChallengeGoalValue]
    ProgressGoalValues: unreal.WrappedArray[int]
    ChallengeCategoryData: ChallengeCategoryData
    bInitiallyActive: bool
    bHideFromCounts: bool
    PrerequisiteChallenge: unreal.UClass
    AssociatedCompletionAchievementId: int
    AssociatedProgressAchievementId: int
    bProfileChallenge: bool
    SubChallenges: unreal.WrappedArray[unreal.UClass]
    CompletedBySubChallenges: bool
    ActivateIfSubChallengesComplete: bool
    bIncrementProgressViaSubChallenges: bool

    def TestForCompleted(
        self,
        PlayerToTest: GbxPlayerController,
        OtherObject: unreal.UObject,
        EnumTag: unreal.WrappedArray[str],
    ) -> bool: ...
    def SetChallengeProgress(self, NewProgress: int): ...
    def PlayerExitChallengeArea(
        self, LevelActorComponent: ChallengeLevelActorComponent
    ): ...
    def PlayerEnterChallengeArea(
        self, LevelActorComponent: ChallengeLevelActorComponent
    ): ...
    def OnLevelActorRegistered(
        self, RegisteredLevelActor: ChallengeLevelActorComponent
    ): ...
    def OnInitChallengeInstance(
        self, OwningChallenges: ChallengesComponent, AssociatedCharacter: GbxCharacter
    ): ...
    def OnChallengeActivated(self): ...
    def IsChallengeComplete(self) -> bool: ...
    def IsChallengeActive(self) -> bool: ...
    def IncrementChallengeProgressByValue(self, Value: int): ...
    def IncrementChallengeProgress(self): ...
    def GetLevelActorComponents(
        self, LevelActorList: unreal.WrappedArray[ChallengeLevelActorComponent]
    ): ...
    def GetChallengeProgressGoalValue(self) -> int: ...
    def GetChallengeProgress(self) -> int: ...
    def GetChallengeCompleteInfo(self, NumCompleted: int, NumChallenges: int): ...
    def CompletedConditional(self) -> bool: ...
    def CompletedChallenge(self, CompletedPlayer: GbxPlayerController): ...
    def CompleteChallenge(self): ...
    def ActivateChallenge(self): ...


class ChallengeCategoryData(gbx_runtime.GbxDataAsset):
    CategoryName: str
    ProgressWeight: float


class ChallengeList(gbx_runtime.GbxDataAsset):
    AssociatedDLC: online_subsystem_utils.DownloadableContentData
    Challenges: unreal.WrappedArray[Any]


class ChallengeManager(engine.Actor):

    def OnStatIncrement(
        self, StatContext: engine.Actor, StatId: GameStatData, Amount: int
    ): ...


class CustomChallengePersistentState(unreal.UObject): ...


class ChallengesComponent(engine.ActorComponent):
    OnChallengeRegistrationComplete: Any
    OnChallengeActivated: Any
    OnChallengeUpdated: Any
    OnChallengeCompleted: Any
    OnChallengeChildCompleted: Any
    LocalChallengeDataCache: unreal.WrappedArray[ChallengeInstanceData]
    ChallengeRewardsEarned: unreal.WrappedArray[int]
    ChallengeRewardsToOfferNext: unreal.WrappedArray[int]
    GameStatsComponent: GameStatsComponent

    def UnregisterInActivePlayerChallenges(self): ...
    def SetChallengeProgress(self, ChalClass: unreal.UClass, NewProgress: int): ...
    def SetChallengeActive(self, ChalClass: unreal.UClass, bInIsActive: bool): ...
    def IsChallengeComplete(self, ChalClass: unreal.UClass) -> bool: ...
    def IsChallengeActive(self, ChalClass: unreal.UClass) -> bool: ...
    def IncrementChallengeProgress(self, ChalClass: unreal.UClass): ...
    def GetMaxChallengeTiers(self, ChalClass: unreal.UClass) -> int: ...
    def GetLocalChallenges(self) -> unreal.WrappedArray[ChallengeInstanceData]: ...
    def GetCompletedChallengeTiers(self, ChalClass: unreal.UClass) -> int: ...
    def GetChallengeStatValue(
        self, ChalClass: unreal.UClass, StatId: GameStatData
    ) -> int: ...
    def GetChallengeStatGoalValue(
        self, ChalClass: unreal.UClass, StatId: GameStatData
    ) -> int: ...
    def GetChallengeProgressGoalValue(self, ChalClass: unreal.UClass) -> int: ...
    def GetChallengeProgress(self, ChalClass: unreal.UClass) -> int: ...
    def GetChallengeCompleteInfoForLevels(
        self,
        LevelsForChallenges: unreal.WrappedArray[str],
        Category: ChallengeCategoryData,
        NumCompleted: int,
        NumActive: int,
        bIgnoreHidden: bool,
    ): ...
    def GetChallengeCompleteInfo(
        self, ChalClass: unreal.UClass, NumCompleted: int, NumChallenges: int
    ): ...
    def CompleteChallengeIfConditionsMet(self, ChalClass: unreal.UClass): ...
    def CompleteChallenge(self, ChalClass: unreal.UClass, bForceActive: bool): ...
    def ClientChallengeUpdateProgress(
        self, ChalClass: unreal.UClass, NewProgress: int
    ): ...
    def ClientChallengeCompleted(
        self, ChalClass: unreal.UClass, NumTiersComplete: int, bForceActive: bool
    ): ...
    def ClientActivateChallenge(self, ChalClass: unreal.UClass): ...
    def AreGlobalChallengesRegistered(self) -> bool: ...
    def ActivateChallenge(self, ChalClass: unreal.UClass): ...


class GbxCharacterMovementComponent(engine.CharacterMovementComponent):
    GbxCharacterOwner: GbxCharacter
    GbxAnimInstance: GbxCharacterAnimInstance
    AnimInstance: engine.AnimInstance
    FallingFloorUpdateInterval: float
    FallingFloorTraceDistance: float
    CurrentMoveToState: CharacterMoveToState
    CurrentRotateToState: CharacterRotateToState
    bCanCrouchInAir: bool
    bCanClimbLadders: bool
    bCenterOnLadder: bool
    bSlideAlongLadderCollision: bool
    bBlockMomentumAdd: bool
    MaxGroundSpeedScale: engine.GbxAttributeFloat
    LadderFriction: float
    MaxLadderAscendSpeed: engine.GbxAttributeFloat
    MaxLadderDescendSpeed: engine.GbxAttributeFloat
    MaxLadderForwardSpeed: float
    MaxLadderReverseSpeed: float
    LadderBrakingDeceleration: float
    LadderInterpSpeed: float
    LadderJumpVelocity: float
    EnterBottomAnimation: unreal.UClass
    ExitBottomAnimation: unreal.UClass
    EnterTopAnimation: unreal.UClass
    ExitTopAnimation: unreal.UClass
    LadderInteractData: LadderInteractData
    OnEnterLadder: Any
    OnExitLadderTop: Any
    OnExitLadderBottom: Any
    OnJumpFromLadder: Any
    OnMantleStarted: Any
    OnMantleFinished: Any
    StanceComponent: StanceComponent
    ActionComponent: GbxActionComponent
    ScriptedMeshOffsetState: CharacterScriptedMeshOffsetState
    bClientWasOnLadder: bool
    OverlappingLadderVolumes: unreal.WrappedArray[Any]
    CurrentLadderVolume: Any
    JumpLadderVolume: Any
    LadderJumpTime: float
    bAlreadyCenteredOnLadder: bool
    bWantsToBeOnLadder: bool
    LadderAnimState: LadderAnimState
    ReplicatedLadderState: ReplicatedLadderState
    RotationRateYaw: engine.GbxAttributeFloat
    IdleRotationRateYaw: engine.GbxAttributeFloat
    bUseIdleRotationRateYaw: bool
    MaxAllowedAimOffset: engine.GbxAttributeFloat
    MinTurnAimOffset: float
    MinBodyFacingThreshold: float
    MaxPredictedTurnDegrees: float
    bUseMaxPredictedTurnDegrees: bool
    MaxPredictedTurnTime: float
    bUseMaxPredictedTurnTime: bool
    bAlwaysFaceActorsCurrentLocation: bool
    AimRotationRate: engine.GbxAttributeFloat
    LookAtAngleClamp: float
    LookRotationRate: float
    FastLookRotationRate: float
    bUseFastLookRotationRate: bool
    FastLookRotationSpeed: gbx_runtime.NumericRange
    HeadLookPercent: float
    HeadLookPercentDistance: gbx_runtime.NumericRange
    bUseHeadLookPercentDistance: bool
    HeadLookPercentInterpSpeed: float
    bUseLookAtParentBoneForAngleClamp: bool
    LookAtBlinkAngle: float
    bUseLookAtBlinkAngle: bool
    LookAtHeadTargetOffset: core_uobject.Vector
    bUseLookAtHeadTargetOffset: bool
    LookAtEyeTargetOffset: core_uobject.Vector
    bUseLookAtEyeTargetOffset: bool
    bUseLookAtTargetClearDelay: bool
    LookAtRate: float
    FootIkEnabledInterpolationSpeed: float
    SlopeAdaptationOverrideInterpSpeed: float
    ControlledMoveState: ControlledMoveState
    ControlledMoveReplicationData: ControlledMoveReplicationData
    MantleData: MantleData
    MantleState: MantleState
    ReplicatedMantleState: ReplicatedMantleState
    GbxNavWalking: GbxCharacterNavWalking
    NavComponent: NavComponent
    NavMeshProjectionDistance: float
    AirFriction: float
    NavMeshProjectionTraceDistance: float
    NavAnimState: NavAnimState
    NavServerData: NavAnimServerData
    NavClientData: NavAnimClientData
    bPretendToBeWalking: bool
    RotationDeltaMatchingInfo: RotationDeltaMatchingInfo
    InterpData: GbxInterpData
    IdleVelocity: IdleVelocityData
    RootMotionState: RootMotionStateData

    def StopRotateTo(self): ...
    def StopMoveTo(self, bForce: bool, bReplicateStop: bool): ...
    def StopControlledMove(
        self, ControlledMove: unreal.UClass, bZeroVelocity: bool, bInterrupted: bool
    ): ...
    def StartRotateTo(self, RotateToCommand: CharacterRotateToCommand): ...
    def StartMoveTo(self, MoveToCommand: CharacterMoveToCommand): ...
    def StartControlledMove(
        self,
        ControlledMove: unreal.UClass,
        Instigator: engine.Actor,
        SpeedOverride: float,
        DurationOverride: float,
        LaunchAngleOverride: float,
        TargetActor: engine.Actor,
        TargetLocation: core_uobject.Vector,
    ) -> bool: ...
    def SetPendingRawInputVector(self, NewInputVector: core_uobject.Vector): ...
    def SetNoneWithRootMotionMode(self, bAnimationWalking: bool, Reason: str): ...
    def SetFacingTarget(self, FacingTarget: FacingInfo, Channel: EFacingChannel): ...
    def SetAnimationBasedTurning(self, bEnable: bool): ...
    def ServerStopMoveTo(self): ...
    def ServerStartMoveTo(self, MoveToCommand: CharacterMoveToCommand): ...
    def ServerAttemptMantle(self, ClientData: MantleAttemptInfo, Timestamp: float): ...
    def OnStanceChanged(self, Args: StanceChangedEventArgs): ...
    def OnRep_ControlledMove(self): ...
    def OnNotifyTurnExit(self): ...
    def OnNotifyTurnEnter(self): ...
    def OnCapsuleEndOverlap(
        self,
        OverlappedComp: engine.PrimitiveComponent,
        OtherActor: engine.Actor,
        OtherComp: engine.PrimitiveComponent,
        OtherBodyIndex: int,
    ): ...
    def OnCapsuleBeginOverlap(
        self,
        OverlappedComp: engine.PrimitiveComponent,
        OtherActor: engine.Actor,
        OtherComp: engine.PrimitiveComponent,
        OtherBodyIndex: int,
        bFromSweep: bool,
        SweepResult: engine.HitResult,
    ): ...
    def MakeFacingInfoRotation(self, Rotation: core_uobject.Rotator) -> FacingInfo: ...
    def MakeFacingInfoNone(self) -> FacingInfo: ...
    def MakeFacingInfoLocation(self, Location: core_uobject.Vector) -> FacingInfo: ...
    def MakeFacingInfoDirection(self, Direction: core_uobject.Vector) -> FacingInfo: ...
    def MakeFacingInfoComponent(
        self, Component: engine.SceneComponent
    ) -> FacingInfo: ...
    def MakeFacingInfoActorEyes(self, Actor: engine.Actor) -> FacingInfo: ...
    def MakeFacingInfoActor(self, Actor: engine.Actor) -> FacingInfo: ...
    def LeaveNoneWithRootMotionMode(self, bApplyDefault: bool): ...
    def IsPerformingSpecificControlledMove(
        self, ControlledMove: unreal.UClass
    ) -> bool: ...
    def IsPerformingControlledMove(self) -> bool: ...
    def IsMovingOnLadder(self) -> bool: ...
    def IsMantlingAllowed(self) -> bool: ...
    def IsMantling(self) -> bool: ...
    def IsInNoneWithRootMotionMode(self) -> bool: ...
    def IsHandIkEnabled(self) -> bool: ...
    def IsFootIkTracingEnabled(self) -> bool: ...
    def IsFootIkEnabled(self) -> bool: ...
    def IsFacingTargetBP(
        self, ThresholdDegrees: float, Channel: EFacingChannel
    ) -> bool: ...
    def GetMaxAllowedAimOffset(self) -> float: ...
    def GetMantleData(self) -> MantleData: ...
    def GetDesiredFacingRotation(
        self, Channel: EFacingChannel
    ) -> core_uobject.Rotator: ...
    def GetDesiredFacingLocation(
        self, Channel: EFacingChannel
    ) -> core_uobject.Vector: ...
    def GetCurrentFacingRotation(
        self, Channel: EFacingChannel
    ) -> core_uobject.Rotator: ...
    def GetCurrentFacingOrigin(
        self, Channel: EFacingChannel
    ) -> core_uobject.Vector: ...
    def GetCurrentFacingLocation(
        self, Channel: EFacingChannel
    ) -> core_uobject.Vector: ...
    def GbxSetAnimInstanceClass(
        self, SkelMeshComponent: engine.SkeletalMeshComponent, NewClass: unreal.UClass
    ): ...
    def GbxCharacterMovementEvent__DelegateSignature(self): ...
    def ClientAdjustControlledMovePosition(
        self,
        Timestamp: float,
        ServerCMData: ControlledMoveNetCorrection,
        NewLoc: core_uobject.Vector,
        NewVel: core_uobject.Vector,
        NewBase: engine.PrimitiveComponent,
        NewBaseBoneName: str,
        bHasBase: bool,
        bBaseRelativePosition: bool,
        ServerMovementMode: int,
    ): ...
    def CanStartPassiveMantle(self) -> bool: ...
    def CanStartMantle(self) -> bool: ...


class GbxCheatManager(engine.CheatManager):
    bHLQNoClipActive: bool

    def TestGameStage(self, GameStageOverride: int): ...
    def StartPlayerInit(self): ...
    def ShowProjectileImpacts(self, Size: float, LifeTime: float): ...
    def SetDebugActorByName(self, ActorName: str): ...
    def SetDebugActor(self, Actor: engine.Actor, ControllerIndex: int): ...
    def Server_TogglePlayersOnly(self): ...
    def Server_DamageTarget(self, DamageAmount: float): ...
    def PlayFeedbackRangedFromThere(self, FeedbackData: str): ...
    def PlayFeedbackDirectional(self, FeedbackData: str, DirectionAngle: float): ...
    def PlayFeedback(self, FeedbackData: str, Scale: float): ...
    def LogQatalystInfo(self): ...
    def DebugNextAI(self): ...
    def DamageAreaDebug(self): ...
    def ClearPlayerInit(self): ...


class CinematicModeData(gbx_runtime.GbxDataAsset):
    bCinematicMode: bool
    bHidePlayer: bool
    bHidePlayerOwnedVehicles: bool
    bHideNPC: bool
    bAffectsHUD: bool
    bAffectsMovement: bool
    bAffectsPawnRotation: bool
    bAffectsTurning: bool
    bCinematicSplitScreen: bool
    bEnableGodMode: bool
    bEnableNoTarget: bool
    AudioMode: ECinematicAudioMode


class ControlledMove(unreal.UObject):
    bIsSpeedScaleNormalized: bool
    bEaseInSpeedConstraints: bool
    bRestoreCharacterMovementMode: bool
    bZeroVelocityAtEnd: bool
    bUpdateCharacterRotationYaw: bool
    bUpdateCharacterRotationPitch: bool
    bApplyLaunchVelocityOnStart: bool
    bSpeedAffectedByMaxGroundSpeedScale: bool
    bBlockMomentumAdd: bool
    bIsMotionNormalized: bool
    bIsInheritVelocityScaleNormalized: bool
    bApplyMoveWhenFalling: bool
    bStopOnLanding: bool
    bOverrideAirControl: bool
    bUseSlopeCurve: bool
    bStopWhenTargetReached: bool
    bEnableMoveControls: bool
    bLimitedLookControl: bool
    bInputVectorRelativeToMoveDirection: bool
    bUseMovingLaunchDirection: bool
    bDirectionRelativeToTarget: bool
    bOffsetLocationByCollisionRadius: bool
    bOffsetLocationByTargetCollisionRadius: bool
    bLeap: bool
    bAlwaysCollideWithTarget: bool
    bStopOnHitWall: bool
    bStopOnHitTargetable: bool
    bTeleport: bool
    bRestrictTeleportToGround: bool
    bDisableLookInput: bool
    bDisableMoveInput: bool
    bEnableTargetControls: bool
    bTargetControlGrounded: bool
    bTrackTarget: bool
    bStopAI: bool
    bAbortAI: bool
    bGodMode: bool
    bDemigodMode: bool
    bEndCrouch: bool
    bForceCrouch: bool
    bUpdateCameraRotationYaw: bool
    bUpdateCameraRotationPitch: bool
    bCancelActionSkillsIfPlayerNotInstigator: bool
    bIsNetworkAutonomous: bool
    bPlayStartStopActionsLocally: bool
    bAllowClientCollisionNotifications: bool
    Duration: AttributeInitializationData
    MovementType: ECMMovementType
    Speed: AttributeInitializationData
    SpeedScaleCurve: engine.RuntimeFloatCurve
    CharacterRotationYawOffset: float
    CharacterRotationPitchOffset: float
    MotionCurves: CMMotionData
    InheritVelocityType: int
    InheritVelocityScaleCurve: engine.RuntimeFloatCurve
    AdjustDurationBySlopeModifier: float
    MaxStepHeight: float
    SpeedSlopeScaleCurve: engine.RuntimeFloatCurve
    LedgeBehavior: ECMLedgeBehavior
    LedgeHeight: float
    AirControl: AttributeInitializationData
    GravityModifier: AttributeInitializationData
    GravityModificationType: ECMGravityModificationType
    GravityModifierEffectOverTime: engine.RuntimeFloatCurve
    TerminalVelocityModifier: AttributeInitializationData
    TerminalVelocityModificationType: ECMTerminalVelocityModificationType
    TargetReached2DThreshold: float
    TargetReachedUpThreshold: float
    TargetReachedDownThreshold: float
    MoveFBControlType: ECMMoveFBControlType
    MoveLRControlType: ECMMoveLRControlType
    MoveForwardRate: AttributeInitializationData
    MoveBackwardRate: AttributeInitializationData
    MoveLRRate: AttributeInitializationData
    LookTurnScale: AttributeInitializationData
    LookUpScale: AttributeInitializationData
    LookDownScale: AttributeInitializationData
    DropRate: AttributeInitializationData
    MaxDiveAngle: AttributeInitializationData
    MaxClimbAngle: AttributeInitializationData
    LaunchDirection: RelativeDirectionData
    MovingLaunchDirection: RelativeDirectionData
    LaunchAngle: AttributeInitializationData
    LocationOffset: float
    LeapApexAngle: float
    LeapStartLandingOffsetTime: float
    StartAction: unreal.UClass
    StopAction: unreal.UClass
    LeapApexAction: unreal.UClass
    LeapLandingAction: unreal.UClass
    HitWallAngle: float
    TeleportOffset: float
    TeleportLocationPreference: ECMTeleportPreferenceType
    LimitedTargetControlDistance: AttributeInitializationData
    TargetControlVelocity: AttributeInitializationData
    TargetControlDelay: AttributeInitializationData
    MaxTrackingCorrectionAngle: float
    TrackingVelocity: float
    ControlledCharacter: GbxCharacter

    def OnTeleported(
        self, MoveDuration: float, PreTeleportLocation: core_uobject.Vector
    ): ...
    def OnTargetLocationChanged(self, NewTargetLocation: core_uobject.Vector): ...
    def OnStop(self, bInterrupted: bool): ...
    def OnStart(self, MoveDuration: float, TargetActor: engine.Actor): ...
    def OnServerStop(self, bInterrupted: bool): ...
    def OnServerStart(
        self, MoveDuration: float, TargetActor: engine.Actor, Instigator: engine.Actor
    ): ...
    def OnHitWorld(self, HitActor: engine.Actor, HitNormal: core_uobject.Vector): ...
    def OnHitTargetable(
        self, HitActor: engine.Actor, HitNormal: core_uobject.Vector
    ): ...


class GbxCustomizationComponent(engine.ActorComponent):
    ColorCustomizationParameters: unreal.WrappedArray[CustomizationColorEntry]
    SharedLinkedParameters: unreal.WrappedArray[CustomizationLinkedParameterEntry]
    LinkedParameters: unreal.WrappedArray[CustomizationLinkedParameterEntry]
    CustomizationSourceInitType: EGbxCustomizationComponentInitSourceType
    TextureInheritanceSettings: CustomizationTextureInheritanceSettings
    CustomizationList: GbxCustomizationContainer
    CustomColorSelections: unreal.WrappedArray[CustomizationColorApplication]
    OnCustomizationApplied: Any
    OnCustomizationRemoved: Any
    LinkedCustomizationSource: GbxCustomizationComponent
    CustomMaterials: Any
    bUseCustomMaterials: bool

    def ServerApplyCustomizationData(
        self, CustomizationToApply: GbxCustomizationData, OptionalCustomizationId: int
    ): ...
    def ServerApplyCustomColor(
        self,
        CustomColorIndex: int,
        InAppliedColor: core_uobject.Vector,
        InSplitColor: core_uobject.Vector,
        InUseDefaultColor: bool,
        InUseDefaultSplitColor: bool,
    ): ...
    def RemoveCustomization(self, Customization: GbxCustomizationData) -> bool: ...
    def OnRep_CustomColorSelections(self): ...
    def LinkToCustomization(self, SourceComponent: GbxCustomizationComponent): ...
    def LinkedCustomizationRemoved(self, Customization: GbxCustomizationData): ...
    def LinkedCustomizationApplied(self, Customization: GbxCustomizationData): ...
    def GetDefaultCustomSplitColor(
        self, SelectionIndex: int, DefaultSplitColor: core_uobject.LinearColor
    ) -> bool: ...
    def GetDefaultCustomColor(
        self, SelectionIndex: int, DefaultColor: core_uobject.LinearColor
    ) -> bool: ...
    def CopyFromCustomization(self, SourceComponent: GbxCustomizationComponent): ...


class GbxCustomizationManager(engine.Actor):
    CustomizationStreamingEntries: unreal.WrappedArray[CustomizationStreamingEntry]

    def OnCustomizationAssetLoaded(self): ...


class DamageBaseComponent(engine.ActorComponent):
    CachedTeamComponent: TeamComponent
    CachedTargetableComponent: TargetableComponent
    ConditionalValueModifiers: unreal.WrappedArray[
        RegisteredConditionalDamageValueModifier
    ]
    ConditionalCritModifiers: unreal.WrappedArray[
        RegisteredConditionalDamageCriticalModifier
    ]
    ConditionalTypeModifiers: unreal.WrappedArray[ConditionalDamageTypeModifier]
    ConditionalHitRegionModifiers: unreal.WrappedArray[
        ConditionalDamageHitRegionModifier
    ]


class DamageCauserComponent(DamageBaseComponent):
    OnCausedAnyDamage: Any
    OnCausedDeath: Any
    OnCausedHealing: Any
    OnHitFriendly: Any
    DefaultModificationContextStrategy: EDamageCausedModificationStrategy
    AttitudeDamageRules: AttitudeDamageRules
    bCanHurtSelf: bool
    StatusEffectChanceModifierScalar: engine.GbxAttributeFloat
    StatusEffectDamageModifierScalar: engine.GbxAttributeFloat
    StatusEffectDurationModifierScalar: engine.GbxAttributeFloat
    StatusEffectModifiers: unreal.WrappedArray[StatusEffectModifiers]
    DamageDealtMultiplier: engine.GbxAttributeFloat
    RadiusDamage_RadiusMultiplier: engine.GbxAttributeFloat
    RadiusDamage_DamageMultiplier: engine.GbxAttributeFloat
    ShouldIgnoreEnemyElementalResistance: engine.GbxAttributeInteger
    bApplyInstigatorSkillDamageModifier: bool
    DefaultCriticalHitMultiplier: engine.GbxAttributeFloat
    DefaultConditionalDamageModifiers: unreal.WrappedArray[ConditionalDamageModifier]
    EnemyReflectionChance: float
    EnemyReflectionParams: ReflectedDamageParams

    def UnregisterConditionalDamageModifier(
        self, Modifier: ConditionalDamageModifier
    ): ...
    def RegisterConditionalDamageModifier(
        self, Modifier: ConditionalDamageModifier
    ): ...


class DamageComponent(DamageBaseComponent):
    OnTakeAnyDamage: Any
    OnPlayerMeleeHit: Any
    OnTakeAnyHealing: Any
    OnHealthDepleted: Any
    OnDeath: Any
    OnHitByFriendly: Any
    OnHitReaction: Any
    HitReactions: HitReactionState
    bShowDamageNumbers: bool
    bShowImmuneFeedbackInGodMode: bool
    bAlwaysBlockWeapons: bool
    bIgnoreDamageAreaVisibilityChecks: bool
    bDieWhenHealthDepleted: bool
    DeathData: DeathData
    HealthMode: EDamageComponentHealthMode
    HealthInformation: unreal.WrappedArray[HealthType]
    SimpleHealthInformation: SimpleHealthInfo
    DamageTakenMultiplier: engine.GbxAttributeFloat
    RadiusDamageTakenMultiplier: engine.GbxAttributeFloat
    StatusEffectChanceModifierScalar: engine.GbxAttributeFloat
    StatusEffectDamageModifierScalar: engine.GbxAttributeFloat
    StatusEffectDurationModifierScalar: engine.GbxAttributeFloat
    StatusEffectModifiers: unreal.WrappedArray[StatusEffectModifiers]
    MinimumDamageLaunchVelocity: float
    bUseBoundForCylinderTest: bool
    LaunchVerticalDampening: float
    MaxSelfInflictedLaunchVelocity: float
    SplatterEffect: ImpactData
    bUseProtectionTimer: bool
    DeathHitReaction: SyncedHitReactionData
    DeathGoreModifiers: DamageGoreModifiers
    LastHitByPlayer: engine.PlayerController
    AvertDeathChance: float
    IntrinsicArmor: float
    SelfReflectionChance: engine.GbxAttributeFloat
    SelfReflectionDamageTakenScale: engine.GbxAttributeFloat
    SelfReflectionDamageScale: engine.GbxAttributeFloat
    SelfReflectionTowardsAttacker: engine.GbxAttributeInteger
    SelfReflectionDamageType: unreal.UClass
    bPassDamageToParent: bool
    bDamageOnlyAppliesToParent: bool
    bCanDamageCorpse: bool
    DefaultConditionalDamageModifiers: unreal.WrappedArray[ConditionalDamageModifier]
    DamageEvents: unreal.WrappedArray[DamageReactionEvent_DamageComponent]
    CachedHitRegionComponent: HitRegionComponent
    ParentDamageComponent: DamageComponent
    LastHitBy: engine.Controller
    bGodMode: bool
    bDemigodMode: bool
    bCurrentlyDead: bool
    ImpactPhysicalMaterialOverride: engine.PhysicalMaterial
    bSuppressOnDeathCall: bool

    def UnregisterConditionalDamageModifier(
        self, Modifier: ConditionalDamageModifier
    ): ...
    def SetSelfReflectedDamageType(self, DamageType: unreal.UClass): ...
    def SetGodMode(self, bInGodMode: bool): ...
    def SetDemiGodMode(self, bInDemiGodMode: bool): ...
    def SetCurrentShield(self, NewCurrentShield: float): ...
    def SetCurrentHealth(self, NewCurrentHealth: float): ...
    def RegisterConditionalDamageModifier(
        self, Modifier: ConditionalDamageModifier
    ): ...
    def ReceiveHealthDepleted(self, DamageCauser: DamageCauserComponent): ...
    def ReceiveAnyHealing(self, Healing: float, HealInstigator: engine.Actor): ...
    def ReceiveAnyDamage(
        self,
        Damage: float,
        DamageType: GbxDamageType,
        DamageSource: DamageSource,
        InstigatedBy: engine.Controller,
        DamageCauser: DamageCauserComponent,
        Details: ReceivedDamageDetails,
    ): ...
    def OnRep_HealthInformation(self): ...
    def OnRep_DeathHitReaction(self): ...
    def OnRep_bCurrentlyDead(self): ...
    def OnOwnerExperienceLevelChanged(
        self, OldExperienceLevel: int, NewExperienceLevel: int
    ): ...
    def OnHealthResourceNowNotDepleted(
        self, ResourcePool: GameResourcePoolReference
    ): ...
    def OnHealthResourceNowDepleted(self, ResourcePool: GameResourcePoolReference): ...
    def IsInGodMode(self) -> bool: ...
    def IsInDemiGodMode(self) -> bool: ...
    def IsDamageOverkill(
        self, DamageAmount: float, OverkillThreshold: float
    ) -> bool: ...
    def GetValidDamageEventFunctionNames(self, Names: unreal.WrappedArray[str]): ...
    def GetTotalMaxHealth(self) -> float: ...
    def GetMaxShield(self) -> float: ...
    def GetMaxHealth(self) -> float: ...
    def GetCurrentShield(self) -> float: ...
    def GetCurrentHealthPercent(self) -> float: ...
    def GetCurrentHealth(self) -> float: ...


class DamageFilter(unreal.UObject):
    bExactDamageSourceClass: bool
    DamageSource: unreal.UClass
    bExactDamageTypeClass: bool
    DamageType: unreal.UClass
    ConditionSelf: gbx_runtime.GbxCondition
    ConditionAttacker: gbx_runtime.GbxCondition
    bOnlyAoEDamage: bool
    bMustNotBeSelfDamage: bool
    bUseRandomChance: bool
    RandomChance: AttributeInitializationData


class DamageGlobalsData(gbx_runtime.GbxDataAsset):
    ProtectionTimerSettings: ProtectionTimerSettings
    DefaultInstigatorSelfDamageScale: AttributeInitializationData
    DefaultHealingDamageType: unreal.UClass
    DefaultHealingImpact: ImpactData
    GlobalAIDamageScale: AttributeInitializationData
    PlayerDamageScaleByLevelDifference: unreal.WrappedArray[LevelBasedDamageScale]
    AIDamageScaleByLevelDifference: unreal.WrappedArray[LevelBasedDamageScale]
    SplatterProbabilityCurve: engine.RuntimeFloatCurve
    SplatterTraceDistanceCurve: engine.RuntimeFloatCurve
    SplatterDirectionSpread: float
    GibLifeSpan: float
    GibCollisionProfileName: str
    GibCollisionProfileNameAttached: str
    GibMaterialParameterResetList: unreal.WrappedArray[str]
    LanguageToTextureMap: Any


class DamageModifierComponent(engine.ActorComponent):
    ConditionalValueModifiers: unreal.WrappedArray[ConditionalDamageValueModifier]
    ConditionalCritModifiers: unreal.WrappedArray[ConditionalDamageCriticalModifier]
    ConditionalTypeModifiers: unreal.WrappedArray[ConditionalDamageTypeModifier]
    ConditionalHitRegionModifiers: unreal.WrappedArray[
        ConditionalDamageHitRegionModifier
    ]

    def UnregisterConditionalDamageModifier(
        self, Modifier: ConditionalDamageModifier
    ): ...
    def RegisterConditionalDamageModifier(
        self, Modifier: ConditionalDamageModifier
    ): ...


class DamageOverTimeManager(unreal.UObject):
    DamageInstances: unreal.WrappedArray[DamageOverTimeInstance]

    def OnParticleSystemStopped(
        self, ParticleSystem: engine.ParticleSystemComponent
    ): ...


class DamageSource(unreal.UObject):
    ModifierAttributes: DamageModifierAttributeCollection
    AIInstigatedDamageScale: AttributeInitializationData
    HealthTypeModifiers: unreal.WrappedArray[DamageSourceHealthTypeModifier]
    bCanCauseCriticals: bool
    bCollectForHitReactions: bool
    bIgnoreCooldown: bool


class GbxDamageType(engine.DamageType):
    DamageTypeDisplayName: str
    DamageEffectVerb: str
    DamageTypeBaseDescription: str
    DamageColor: core_uobject.LinearColor
    DamageIconFrameName: str
    bIsHealingType: bool
    bIsDoT: bool
    InnerDamageRadiusPercent: float
    OuterDamageRadiusPercent: float
    MinRadiusDamageScalar: float
    GameplayTags: gameplay_tags.GameplayTagContainer
    ModifierAttributes: DamageModifierAttributeCollection
    OnlyApplyToThisHealthType: engine.DataTableRowHandle
    StatusEffectData: StatusEffectData
    SurfaceDamageModifiers: unreal.WrappedArray[DamageSurfaceModifier]
    UIStats: unreal.WrappedArray[UIStatData]

    def IsElementalType(self) -> bool: ...


class EnvQueryContext_EnvQueryParam(aimodule.EnvQueryContext):
    DefaultBlackboardKeyName: str
    AllowsUnboundContext: bool


class FirstPersonComponent(engine.ActorComponent):
    ConfigData: unreal.UClass
    Arms: GbxSkeletalMeshComponent
    Legs: GbxSkeletalMeshComponent
    FirstPersonRootBone: str
    CameraSocket: str
    PrimaryHandWeaponSocket: str
    BaseTransformsAnimation: engine.AnimSequence
    CrouchTransitionDuration: float
    CrouchTransitionEasing: float
    TranslationLeadingList: unreal.WrappedArray[ViewLeadingTranslationInfo]
    TranslationLeading: ViewLeadingTranslationInfo
    RotationleadingList: unreal.WrappedArray[ViewLeadingRotationInfo]
    RotationLeading: ViewLeadingRotationInfo
    ZoomRotationLeading: ViewLeadingRotationInfo
    ZoomRotationSocket: str
    ShotOffsetSpeed: float
    ShotOffsetRecoverySpeed: float
    MaxViewModelImpulseTranslationOffset: core_uobject.Vector
    MaxViewModelImpulseRotationOffset: core_uobject.Rotator
    FlinchBlendSpace: engine.BlendSpaceBase
    FlinchAnimSlotName: str
    DefaultFlinchBlendInTime: float
    DefaultFlinchBlendOutTime: float
    InterruptFlinchBlendInTime: float
    FlinchInterruptThreshold: float
    ZoomedFlinchWeight: float
    OnFirstPersonCreated: Any
    ViewModelOffsetList: unreal.WrappedArray[core_uobject.Transform]
    CurrentShotRotationOffset: core_uobject.Rotator
    BaseViewModelLocationOffset: core_uobject.Vector
    CreatedFirstPersonComponents: unreal.WrappedArray[engine.SceneComponent]
    TopLevelComponents: unreal.WrappedArray[TrackedFirstPersonComponent]
    TargetShotRotationOffset: core_uobject.Rotator
    CurrentRelativeLocation: core_uobject.Vector
    DefaultTranslationOffset: core_uobject.Vector

    def SetBaseEyeToWeaponTransform(
        self, NewWeaponTransform: core_uobject.Transform
    ): ...
    def GetFirstPersonComponentByName(self, Name: str) -> engine.SceneComponent: ...


class GbxGameInstance(engine.GameInstance):
    MenuStashes: MenuStash
    CharacterMassPresets: core_uobject.SoftObjectPath
    CachedCharacterMassPresets: engine.DataTable
    ForcePresets: core_uobject.SoftObjectPath
    CachedForcePresets: engine.DataTable
    SpawnCostPresets: core_uobject.SoftObjectPath
    CachedSpawnCostPresets: engine.DataTable
    CinematicModeStack: unreal.WrappedArray[CinematicModeData]
    CinematicMode: CinematicModeData
    ProjectileManager: IGbxProjectileManager
    SharedPickupInventoryActors: unreal.WrappedArray[SharedPickupInventoryActor]

    def DebugLoadStartupAssets(self): ...


class GlobalAIData(gbx_runtime.GbxDataAsset):
    CombatTag: gameplay_tags.GameplayTag
    PassiveTag: gameplay_tags.GameplayTag
    AITimeToRememberDirectAttacks: float
    AITimeToRememberNonAttackingEnemies: float
    AITimeToRememberHiddenEnemies: float
    JumpHitReactionDeathOverride: HitReactionTag
    JumpHitLiveReactionLayer: unreal.UClass
    ChanceOfPlayingFirstNoticerAggroAnimation: float
    ChanceOfPlayingSecondNoticerAggroAnimation: float
    bUseVariableAccuracy: bool
    TimeToBestAccuracy: AttributeInitializationData
    DamagePctToWorstAccuracy: AttributeInitializationData
    DamagePctDecayRate: AttributeInitializationData
    MinAccuracy: float


class GbxGlobalsData(gbx_runtime.GbxDataAsset):
    DamageGlobalsData: Any
    GameplayGlobals: GbxGameplayGlobals
    StatusEffectGlobals: Any
    AssetMapping: AssetMappingData


class HitRegionComponent(engine.ActorComponent):
    DefaultHitRegion: HitRegionData
    HitRegions: unreal.WrappedArray[HitRegionState]
    CachedMesh: engine.SkeletalMeshComponent
    CachedDamageComponent: DamageComponent

    def TriggerClientEvent(self, EventSummary: DamageReactionEventSummary): ...
    def GetValidDamageEventFunctionNames(self, Array: unreal.WrappedArray[str]): ...
    def GetValidAssociatedComponentNames(self, Array: unreal.WrappedArray[str]): ...
    def GetHitRegionPercentHealth(
        self, HitRegion: HitRegionData, AssociatedComponent: engine.PrimitiveComponent
    ) -> float: ...
    def GetHitRegionMaxHealth(
        self, HitRegion: HitRegionData, AssociatedComponent: engine.PrimitiveComponent
    ) -> float: ...
    def GetHitRegionCurrentHealth(
        self, HitRegion: HitRegionData, AssociatedComponent: engine.PrimitiveComponent
    ) -> float: ...


class HitRegionData(gbx_runtime.GbxDataAsset):
    HitRegionName: str
    BoneNames: unreal.WrappedArray[str]
    bCanEverTakeRadiusDamage: bool
    bCriticalHit: bool
    bAllowRadiusDamage: bool
    bShouldBlockAreaDamage: bool
    bAllowRadiusDamageToBeConvertedToImpactDamage: bool
    bTrackDamage: bool
    HealthParams: HitRegionHealthParams
    bUseDamageScale: bool
    DamageScale: AttributeInitializationData
    bShowDamageNumbers: bool
    bCanReflect: bool
    ReflectionChance: float
    bCanRicochet: bool
    RicochetChance: float
    bRicochetIfReflectionFails: bool
    bOnlyReflectToAttacker: bool
    ReflectionAccuracyModifier: float
    IncomingReflectedDamageScale: float
    OutgoingReflectedDamageScale: float
    bDisableBulletMagnetism: bool
    BulletMagnetismOverrideBoneNames: unreal.WrappedArray[str]
    bOverrideImpactEffect: bool
    EffectOverride: ImpactResponseEffect
    bPlayImactEffectWithNoDamage: bool
    bNoSplatterEffect: bool
    SplatterEffect: ImpactData
    CustomDamageNumberParticleSystem: engine.ParticleSystem
    bDisableHitReactions: bool
    PhysicalMaterial: engine.PhysicalMaterial
    DefaultDamageSurface: EDamageSurfaceType


class ActorPartData(gbx_runtime.GbxDataAsset):
    PartTypeEnum: unreal.UEnum
    PartType: int
    GestaltData: engine.GestaltData
    GestaltMeshPartName: str
    AdditionalGestaltMeshPartNames: unreal.WrappedArray[str]
    MultiSelectionGestaltPartNames: unreal.WrappedArray[
        MultiSelectionGestaltPartNameData
    ]
    MinGameStage: AttributeInitializationData
    MaxGameStage: AttributeInitializationData
    Dependencies: unreal.WrappedArray[ActorPartData]
    Excluders: unreal.WrappedArray[ActorPartData]

    def EnumeratePossibleExcluders(
        self, OutPartList: unreal.WrappedArray[ActorPartData]
    ): ...
    def EnumeratePossibleDependencies(
        self, OutPartList: unreal.WrappedArray[ActorPartData]
    ): ...
    def EnumerateOtherParts(self, OutPartList: unreal.WrappedArray[ActorPartData]): ...
    def EnumerateGestaltMeshPartNames(
        self, OutPartNameList: unreal.WrappedArray[str]
    ): ...


class DataTableAttributeValueResolver(AttributePropertyValueResolver):
    DataTableRow: engine.DataTableRowHandle
    DataTableColumn: str

    def GetDataTableColumnNames(self, ValueNames: unreal.WrappedArray[str]): ...


class DataTableFunctionAttributeValueResolver(DataTableAttributeValueResolver):
    DataTableStruct: core_uobject.ScriptStruct

    def GetDataTableRow(self, Context: unreal.UObject) -> engine.DataTableRowHandle: ...


class LadderInteractData(gbx_runtime.GbxDataAsset):
    RequiredViewAlignment: float
    RequiredRearViewAlignment: float
    bCanMountLadderFromTopWhileFacing: bool
    MaxVerticalSpeedToGrabLadder: float
    JumpRegrabDelay: float
    TopEnterAnimSyncTime: float
    TopExitAnimSyncTime: float
    ExitLocationDepthOffset: float
    ExitingTopThresholdHeightOffset: float
    EnteringTopTargetHeightOffset: float
    EnteringTopFeetToLadderThreshold: float
    LadderTopMountCurveHorz: engine.RuntimeFloatCurve
    LadderTopMountCurveVert: engine.RuntimeFloatCurve
    LadderTopDismountCurveHorz: engine.RuntimeFloatCurve
    LadderTopDismountCurveVert: engine.RuntimeFloatCurve


class NavComponent(engine.ActorComponent): ...


class GbxSkeletalMeshComponent(engine.SkeletalMeshComponent):
    ParentAnimationComponent: engine.SkeletalMeshComponent
    GestaltPartList: GestaltPartListData
    GestaltMeshParts: unreal.WrappedArray[GestaltPartData_Mesh]
    ReplicatedGestaltParts: ReplicatedGestaltPartsData
    GestaultSeed: int
    bAllowDynamicallyAddedForwardDynamicsNodes: bool
    BoneModInstances: unreal.WrappedArray[engine.BoneModInstance]
    StretchBonesInstances: unreal.WrappedArray[StretchBonesInstance]
    BoneModifyProfile: GbxBoneModifyProfile
    bReplicateBoneMods: bool
    BoneModifyProfileData: BoneModifyProfileData
    LastUpdateTime: float
    CachedGlobalBMP: unreal.WrappedArray[BMPOverride]
    GlobalBMPRepArray: unreal.WrappedArray[GlobalBoneModifyProfileState]
    NoBodyMass: float
    ImpulseMultiplier: float
    DefaultImpactData: ImpactData
    BodyImpactDataOverrides: Any
    CustomizationTargets: unreal.WrappedArray[GbxCustomizationTargetData]
    StretchAnimData: StretchAnimData
    AnimBPProfile: GbxAnimBlueprintProfile
    bGaitScalingOverride: bool
    GaitScalingSettings: engine.GaitScalingSettings
    bUseAggregateSimulationSleepCheck: bool
    AggregateSimulationSleepCheckSeconds: float
    AggregateSimulationSleepCheckDistance: float
    UpdateRateParametersOverride: engine.AnimUpdateRateParameters
    bOverrideUpdateRateParameters: bool
    PoseMatch: GbxAnimPoseMatch

    def ShowGestaltMeshParts(
        self, Parts: unreal.WrappedArray[GestaltPartData_Mesh], bLocalOnly: bool
    ): ...
    def ShowGestaltMeshPart(
        self, GestaltMeshPart: GestaltPartData_Mesh, bLocalOnly: bool
    ): ...
    def SetUpdateOverrideValues(
        self,
        UpdateRateOverrides: unreal.WrappedArray[float],
        bEnableOverrideProperties: bool,
    ): ...
    def SetParentAnimationComponent(
        self, ParentComponent: engine.SkeletalMeshComponent
    ): ...
    def SetGestaltPartList(self, NewGestaltPartList: GestaltPartListData): ...
    def RunPoseTest(self): ...
    def OnRep_GlobalBoneMod(self): ...
    def OnRep_GestaltMeshParts(self): ...
    def LinkSkelMeshAnimInstances(
        self,
        InLinkedSkelMeshComponents: unreal.WrappedArray[engine.SkeletalMeshComponent],
    ): ...
    def LinkSkelMeshAnimInstance(
        self, InLinkedSkelMeshComponent: engine.SkeletalMeshComponent
    ): ...
    def IsGestaltMeshPartVisible(
        self, GestaltMeshPart: GestaltPartData_Mesh
    ) -> bool: ...
    def IsCustomizationTargetFor(
        self, TargetToTest: GbxCustomizationTargetData
    ) -> bool: ...
    def HideGestaltMeshParts(
        self, Parts: unreal.WrappedArray[GestaltPartData_Mesh], bLocalOnly: bool
    ): ...
    def HideGestaltMeshPart(
        self, GestaltMeshPart: GestaltPartData_Mesh, bLocalOnly: bool
    ): ...
    def GetUpdateOverrideValues(self) -> unreal.WrappedArray[float]: ...
    def GetAvailableBoneNames(self, Array: unreal.WrappedArray[str]): ...
    def CopyGestaltPartList(self, GestaltPartListSource: engine.Actor): ...


class PawnAttachSlotComponent(UsableComponent):
    OnAttachStarted: Any
    OnAttachFinished: Any
    OnDetachStarted: Any
    OnDetachFinished: Any
    OnAttachStateChanged: Any
    AttachState: PawnAttachSlotState
    PersistentAttachInfo: PawnSceneAttachmentInfo
    PersistentPawnAction: unreal.UClass
    AnimSets: unreal.WrappedArray[AttachSlotAnimSet]
    AttachTransition: PawnAttachmentTransition
    DetachTransition: PawnAttachmentTransition
    bManualAttachTransitionDuration: bool
    bEvaluateAttachTransitionBeforeModifyingPawn: bool
    AttachTransitions: unreal.WrappedArray[PawnAttachTransition]
    bOffsetFallbackDetachLocationByActorHeight: bool
    bUseBaseOwnerLocationForSafeLocationTrace: bool
    bUseBaseOwnerLocationForFallbackDetachLocation: bool
    DetachTransitions: unreal.WrappedArray[PawnDetachTransition]
    PossessionRule: EAttachmentPossessionRule
    bPossessWhenAttachmentStarts: bool
    bRestorePossessionWhenDetachStarts: bool
    bIsHijackable: bool
    bCanHijackPlayer: bool
    bCanHijackFriendly: bool
    bCanBeUsedByPlayers: bool
    bForceUntargetable: bool
    bForceGodMode: bool
    bForceHidden: bool
    bForceNoCollision: bool
    bDisableHitReaction: bool
    bCollideDuringTransitions: bool
    bMirrorTeam: bool
    bForceUnCrouch: bool
    bIgnoreCollisionWithBase: bool
    bBaseIgnoreCollisionWithPawn: bool
    bForceSkeletalOptimizations: bool
    bDisableDelayRootMotionOneFrameDuringDetach: bool
    bDisableOverlapOptimization: bool
    bGenerateOverlapEventOnDetach: bool

    def SetPersistentAttachSocketName(self, SocketName: str): ...
    def SetDetachabilityLocked(self, bLock: bool, Reason: str): ...
    def RequestDetachPawn(self): ...
    def OnRep_AttachState(self): ...
    def ManuallyFinishAttach(self): ...
    def IsOccupied(self, bIncludeDetaching: bool) -> bool: ...
    def HandleActorDestroyed(self, Actor: engine.Actor): ...
    def GetPersistentAttachSocketTransform(self) -> core_uobject.Transform: ...
    def GetOccupant(self, bIncludeDetaching: bool) -> engine.Pawn: ...
    def GetAttachStatus(self) -> EPawnAttachStatus: ...
    def DetachPawn(self, bInstant: bool, bSkipPlacement: bool): ...
    def AttachPawn(self, AttachingPawn: engine.Pawn, bInstant: bool): ...


class GbxProfile(engine.SaveGame):
    bDisplayVehicleSpeedAsMPH: bool
    bEnableAimAssist: bool
    bGamepadInvertLook: bool
    bGamepadInvertTurn: bool
    bGamepadInvertMove: bool
    bGamepadInvertStrafe: bool
    bEnableMouseAcceleration: bool
    bEnableGamepadInput: bool
    bUseClassicGamepadInput: bool
    bEnableVibration: bool
    bEnableTriggerFeedback: bool
    GlyphMode: EGbxGlyphSetOption
    bInvertMousePitch: bool
    bEnableMouseSmoothing: bool
    MouseScale: float
    bShowDamageNumbers: bool
    bShowDamageNumberIcons: bool
    bEnableTrainingMessages: bool
    bCenterCrosshair: bool
    bToggleSprint: bool
    bToggleCrouch: bool
    bCensorContent: bool
    MasterVolume: float
    MusicVolume: float
    SoundEffectsVolume: float
    VOVolume: float
    VoiceVolume: float
    bEnableOptionalVO: bool
    bPushToTalk: bool
    bEnableControllerAudio: bool
    SpeakerAngleFront: float
    SpeakerAngleSide: float
    SpeakerAngleBack: float
    SpeakerSetup: ESpeakerSetup
    bMuteAudioOnFocusLoss: bool
    bEnableWindowsSpatialAudio: bool
    GraphicsMode: EGraphicsMode
    BaseFOV: float
    BaseVehicleFOV: float
    bHideStrictNATHelpDialog: bool
    HudScaleMultiplier: float
    PlayerInputBindings: PlayerInputBindings
    bShowTextChat: bool
    NewsHashes: unreal.WrappedArray[int]
    LastUsedSavegameId: int


class RadiusDamageReplicationManager(engine.Actor):

    def Multicast_StopRadiusEffect(
        self,
        ContextActor: engine.Actor,
        DamageData: unreal.UClass,
        bStopAllForContext: bool,
    ): ...
    def Multicast_ProcessRadiusRequest(
        self,
        ContextActor: engine.Actor,
        DamageData: unreal.UClass,
        DamageType: unreal.UClass,
        Radius: float,
        Location: engine.Vector_NetQuantize,
        Damage: float,
        ExplosionData: ExplosionData,
        DefaultParticles: engine.ParticleSystem,
        DefaultAudioEvent: wwise_audio.WwiseEvent,
        DefaultImpactData: ImpactData,
        SignificanceEvent: GbxSignificanceEvent,
        Force: float,
    ): ...


class RecentDamageTrackingComponent(engine.ActorComponent):
    PlayerController: GbxPlayerController
    RecentlyCausedDamageInstances: RecentlyCausedDamageInstance
    InstigatedFeedbacks: unreal.WrappedArray[FeedbackData]


class GbxSaveGame(engine.SaveGame): ...


class SaveGameChannel(engine.Channel):
    SaveGameActor: Any


class GbxSignificanceManager(significance_manager.SignificanceManager):
    WeightInterps: unreal.WrappedArray[CachedInterp]
    BucketInterps: unreal.WrappedArray[CachedInterp]


class GbxSingletons(unreal.UObject):
    ExplosionImpactManager: AsyncExplosionImpactManager
    FeedbackManager: GbxFeedbackManager


class StanceDataSelector(StanceDataProvider):
    StancePriorityList: unreal.WrappedArray[ConditionalStance]
    DefaultStanceProvider: StanceDataProvider


class StatusEffectGlobalsData(gbx_runtime.GbxDataAsset): ...


class StatusEffectManagerComponent(engine.ActorComponent):
    InstanceStacks: unreal.WrappedArray[StatusEffectInstanceStack]

    def RemoveStatusEffectInstance(
        self, Reference: StatusEffectInstanceReference
    ) -> bool: ...
    def RemoveStatusEffect(self, Spec: StatusEffectRemoveSpec) -> bool: ...
    def QueryStatusEffect(
        self, Query: StatusEffectQuery
    ) -> StatusEffectQueryResult: ...
    def AddStatusEffect(
        self, Spec: StatusEffectSpec
    ) -> StatusEffectInstanceReference: ...


class StatusEffectsStatics(engine.BlueprintFunctionLibrary):

    def RemoveStatusEffectInstance(
        self, Target: engine.Actor, Reference: StatusEffectInstanceReference
    ) -> bool: ...
    def RemoveStatusEffect(
        self, Target: engine.Actor, RemoveSpec: StatusEffectRemoveSpec
    ) -> bool: ...
    def QueryStatusEffect(
        self, Target: engine.Actor, Query: StatusEffectQuery
    ) -> StatusEffectQueryResult: ...
    def AddStatusEffect(
        self, Target: engine.Actor, Spec: StatusEffectSpec
    ) -> StatusEffectInstanceReference: ...


class UseComponent(engine.ActorComponent):
    UsableChanged: Any
    ImpactDataChanged: Any
    UsabilityChanged: Any
    OnHoldUseStopped: Any
    ViewDistance: float
    InteractDistance: float
    LeaveInteractionDistance: float
    VehicleInteractDistance: float
    VehicleLeaveInteractionDistance: float
    CachedController: engine.Controller
    PreviousUsableState: UseTraceResult
    ReplicatedUsableState: UseTraceResult
    LocalUsableState: UseTraceResult
    EmptyUsableState: UseTraceResult
    LatentUseStates: LatentUseState
    ReplicatedCostCache: UsableCostCache
    CanUseObjectsLock_Replicated: ResourceLock

    def StopUsingCurrentObject(self, UseType: EUsabilityType): ...
    def StartUsingCurrentObject(self, UseType: EUsabilityType): ...
    def ServerUseObject(
        self, UsableObject: UsableComponent, UseType: EUsabilityType, bHeld: bool
    ): ...
    def ServerStopUsingObject(
        self, UsableObject: UsableComponent, UseType: EUsabilityType
    ): ...
    def ServerStartUsingObject(
        self, UsableObject: UsableComponent, UseType: EUsabilityType
    ): ...
    def OnUsableChanged__DelegateSignature(
        self,
        NewUsableComponent: UsableComponent,
        InUsabilityInfo: UsabilityInfo,
        NewUsableComponentImpactPoint: core_uobject.Vector,
        NewUsableComponentDistanceAway: float,
    ): ...
    def OnUsabilityChanged__DelegateSignature(
        self, NewUsableComponent: UsableComponent, InUsabilityInfo: UsabilityInfo
    ): ...
    def OnUnableToAffordUsableObject__DelegateSignature(
        self, Usable: UsableComponent, UseType: EUsabilityType, bUseHeld: bool
    ): ...
    def OnImpactDataChanged__DelegateSignature(
        self,
        NewUsableComponent: UsableComponent,
        NewUsableComponentImpactPoint: core_uobject.Vector,
        NewUsableComponentDistanceAway: float,
    ): ...
    def OnHoldUseStopped__DelegateSignature(self): ...
    def GetCurrentUsable(self) -> UsableComponent: ...
    def ForceUsingObject(self, UsableObject: UsableComponent): ...
    def ClientNotifyAttemptedUseCouldNotAfford(
        self, Usable: UsableComponent, UseType: EUsabilityType, bUseHeld: bool
    ): ...
    def CanUseCurrentUsable(self, Type: EUsabilityType) -> bool: ...
    def CanInteractWithCurrentUsable(self, Type: EUsabilityType) -> bool: ...


class LevelGroupData(gbx_runtime.GbxDataAsset):
    DisplayName: str
    SubHeader: str
    Description: str
    ContainedLevels: unreal.WrappedArray[Any]


class ActorPartSetData(gbx_runtime.GbxDataAsset):
    PartDataClass: unreal.UClass
    PartTypeEnum: unreal.UEnum
    ActorPartReplacementMode: EActorPartReplacementMode
    ActorPartLists: unreal.WrappedArray[ActorPartListData]
    OldActorPartLists: unreal.WrappedArray[ActorPartListData]
    Guid: core_uobject.Guid

    def EnumeratePartListForPartType(
        self, PartType: int, OutPartList: unreal.WrappedArray[ActorPartData]
    ): ...


class PrototypeActor(engine.Actor): ...


class StatusEffectStackingStrategyData(gbx_runtime.GbxDataAsset): ...


class UIStatData_Attribute(UIStatData_Numeric):
    Attribute: GbxAttributeData
    OtherComparableStats: unreal.WrappedArray[UIStatData]
    StatsToReplace: unreal.WrappedArray[UIStatData]


class UIStatFormulaEvaluator(unreal.UObject): ...


class GbxWeaponSlotData(engine.DataAsset):
    SocketName: str
    InitiallyEnabled: bool


class LevelData(gbx_runtime.GbxDataAsset):
    DisplayName: str
    SubHeader: str
    Description: str
    LevelMapName: str
    LinksToOtherLevel: unreal.WrappedArray[Any]
    OwningLevelGroup: Any
    DLCExpansionData: online_subsystem_utils.DownloadableContentData


class ActorAttributeContextResolver(AttributeContextResolver): ...


class AIChargeData(gbx_runtime.GbxDataAsset):
    StartAction: unreal.UClass
    MissAction: unreal.UClass
    StrikeAction: unreal.UClass
    HitWallAction: unreal.UClass
    ReachCliffAction: unreal.UClass
    StopForFriendlyAction: unreal.UClass
    bUseAnims: bool
    ChargeAction: unreal.UClass
    StrikeAngle: float
    StrikeDistance: float
    MaxTravelDistance: float
    MissDistance: float
    HitWallRadiusPct: float
    SlowStopTime: float
    SlowStopSpeedPercent: float
    HitReactionForceSelection: ForceSelection
    HitReactionFriendly: HitReactionTag
    HitReactionUnfriendly: HitReactionTag
    bCauseHitReaction: bool
    StopForFriendlyOfRelativeSize: ERelativeSizeCharge
    StopForFriendlyDistance: float
    ChargeStance: StanceDataProvider
    SpeedOverrideType: EChargeCurveType
    SpeedOverTime: engine.RuntimeFloatCurve
    RotationOverrideType: EChargeCurveType
    bRotationOverTime: bool
    RotationOverTime: engine.RuntimeFloatCurve
    RotationByDistance: engine.RuntimeFloatCurve
    SpeedCurve: engine.CurveFloat
    RotationCurve: engine.CurveFloat
    HitReactionForce: float


class AIDataProvider_AttributeData(aimodule.AIDataProvider):
    AttributeData: GbxAttributeData
    FloatValue: float
    IntValue: int
    BoolValue: bool


class AIDataProvider_AttributeInitializationData(aimodule.AIDataProvider):
    AttributeInitializationData: AttributeInitializationData
    FloatValue: float
    IntValue: int
    BoolValue: bool


class AIDataProvider_AttributeInitializer(aimodule.AIDataProvider):
    AttributeInitializer: unreal.UClass
    FloatValue: float
    IntValue: int
    BoolValue: bool


class AIDodgeComponent(engine.ActorComponent):
    IsDodging: bool
    DodgeBullet: AIDodgeData
    DodgeGrenade: AIDodgeData
    DodgeRandom: AIDodgeBasicData
    DodgeZone: AIDodgeData
    GlobalCooldown: GbxParam
    OnDodged: Any
    TeamComponent: TeamComponent
    ActionComponent: GbxActionComponent
    BlackboardComponent: aimodule.BlackboardComponent
    BrainComponent: aimodule.BrainComponent
    NavComponent: NavComponent
    MovementComponent: GbxCharacterMovementComponent
    PendingDodge: AIDodgeInstance
    ActiveDodge: AIDodgeInstance

    def TriggerZoneDodge(
        self,
        WorldContextObject: unreal.UObject,
        TargetActor: engine.Actor,
        ZoneLoc: core_uobject.Vector,
        ZoneVel: core_uobject.Vector,
        ActorRef: engine.Actor,
    ): ...
    def TriggerGrenadeDodge(
        self,
        WorldContextObject: unreal.UObject,
        GrenadeLoc: core_uobject.Vector,
        Instigator: engine.Actor,
        ExtraDelay: float,
    ): ...
    def TriggerDodge(
        self,
        Type: EAIDodgeType,
        SourceLoc: core_uobject.Vector,
        SourceActor: engine.Actor,
        ExtraDelay: float,
        bForced: bool,
    ) -> bool: ...
    def TriggerBulletDodge(
        self,
        WorldContextObject: unreal.UObject,
        MuzzleLoc: core_uobject.Vector,
        BulletVel: core_uobject.Vector,
        Instigator: engine.Actor,
    ): ...


class AimControlData(gbx_runtime.GbxDataAsset):
    InputCurveExponent: float
    RotationCap: float
    AccelRate: float
    DecelRate: float
    AccelRateRawBias: float
    HipSensitivityLevels: unreal.WrappedArray[AimSensitivityLevelParameters]
    ZoomSensitivityLevels: unreal.WrappedArray[AimSensitivityLevelParameters]
    VehicleSensitivityLevels: unreal.WrappedArray[AimSensitivityLevelParameters]
    MinFOVScaling: float
    MinAcceptedFOVScale: float
    MinFOVScalingMouse: float
    MinAcceptedFOVScaleMouse: float
    HighDeadZone: float
    AxialDeadZoneBegin: float
    AxialDeadZoneRatio: float


class AISense_Bullet(aimodule.AISense):
    BulletEvents: unreal.WrappedArray[AIBulletEvent]

    def ReportBulletEvent(
        self,
        WorldContext: unreal.UObject,
        StartLoc: core_uobject.Vector,
        EndLoc: core_uobject.Vector,
        bFirstEvent: bool,
        Instigator: engine.Actor,
        Strength: float,
    ): ...


class AISense_GbxPrediction(aimodule.AISense): ...


class AISense_GbxSight(aimodule.AISense_Sight):

    def ForceSightEvent(
        self,
        WorldContext: unreal.UObject,
        SeenActor: engine.Actor,
        LookingActor: engine.Actor,
    ): ...


class AISenseConfig_Bullet(aimodule.AISenseConfig):
    Implementation: unreal.UClass
    ListenRadius: float
    DetectionByAffiliation: aimodule.AISenseAffiliationFilter


class AISenseConfig_GbxPrediction(aimodule.AISenseConfig):
    DetectionByAffiliation: aimodule.AISenseAffiliationFilter


class AnimNotify_CanInterruptAnim(engine.AnimNotify): ...


class AnimNotify_CauseDamage(engine.AnimNotify):
    DamageData: unreal.UClass


class AnimNotify_Feedback(engine.AnimNotify):
    bApplyToAllPlayers: bool
    bIgnoreOwner: bool
    bApplyFeedbackAtRanged: bool
    SocketName: str
    FeedbackData: FeedbackData
    OwnerFeedbackData: FeedbackData
    FeedbackScale: AttributeInitializationData


class AnimNotify_Footstep(engine.AnimNotify):
    FootIndex: int
    Volume: float
    Pitch: float
    bRestrictToMatchingPlayerPerspective: bool


class AnimNotify_GbxAction(engine.AnimNotify):
    CustomEventName: str


class AnimNotify_HandPlant(engine.AnimNotify):
    HandIndex: int
    Volume: float
    Pitch: float
    bRestrictToMatchingPlayerPerspective: bool


class AnimNotify_PlayJumpedImpact(engine.AnimNotify): ...


class AnimNotify_PlayLandedImpact(engine.AnimNotify):
    ImpactSpeed: float
    bAsIfFromJump: bool


class AnimNotify_SetRagdollObjectHoldTransform(engine.AnimNotify):
    bEnable: bool
    Transform: core_uobject.Transform


class AnimNotify_StretchBonesMarker(AnimNotify_GbxAction):
    StartBoneName: str
    EndBoneName: str
    AnimatedTargetDistance: float
    LookAtVector: core_uobject.Vector
    XScale: float


class AnimNotifyState_DeathOverride(engine.AnimNotifyState):
    DeathReactionTag: HitReactionTag
    DefaultReactionTagName: core_uobject.SoftObjectPath


class AnimNotifyState_DisableLegIK(engine.AnimNotifyState): ...


class AnimNotifyState_DisableLegIKTracing(engine.AnimNotifyState): ...


class AnimNotifyState_DisableLookAt(engine.AnimNotifyState): ...


class AnimNotifyState_Feedback(engine.AnimNotifyState):
    bApplyToAllPlayers: bool
    FeedbackData: FeedbackData
    FeedbackScale: AttributeInitializationData


class AnimNotifyState_GbxAction(engine.AnimNotifyState):
    CustomEventName: str


class AnimNotifyState_RootMotionRotation(engine.AnimNotifyState):
    LockFootIkIndex: int
    bLockFootIK: bool


class AnimNotifyState_SoftAlign(engine.AnimNotifyState):
    Type: EAnimNotifyAlignType
    bAffectsLocation: bool
    bAffectsRotation: bool
    PartnerName: str
    ActionSlotName: str
    AlignSocketPartner: str


class AnimNotifyState_StretchAction(engine.AnimNotifyState):
    bRotate: bool
    bTranslate: bool


class AnimNotifyState_StretchBonesMarker(AnimNotifyState_GbxAction):
    StartBoneName: str
    EndBoneName: str
    AnimatedTargetDistance: float
    LookAtVector: core_uobject.Vector
    EndAnimatedTargetDistance: float
    EndLookAtVector: core_uobject.Vector
    XScale: float


class AsyncExplosionImpactManager(unreal.UObject):
    AsyncRequests: unreal.WrappedArray[AsyncExplosionImpactRequest]


class AttributeEffectMultiMutatorData(AttributeEffectMutatorData):
    Mutators: unreal.WrappedArray[AttributeEffectMutatorData]


class AttributeInitializer(unreal.UObject):
    UsageMode: EAttributeInitializerUsageMode

    def EvaluateBalanceFormula(
        self, Multiplier: float, Level: float, Power: float, Offset: float
    ) -> float: ...
    def CalculateAttributeInitialValue(self, Context: unreal.UObject) -> float: ...


class AttributeModifierTestContext(unreal.UObject):
    AttributeProperty: engine.GbxAttributeFloat
    FloatProperty: float


class TestAttributePropertyValueResolver(AttributePropertyValueResolver): ...


class AttributePropertyValueResolverTestContext(unreal.UObject):
    FloatProp: float
    FloatPropStaticArray: float
    FloatPropDynamicArray: unreal.WrappedArray[float]
    ObjectProp: AttributePropertyValueResolverTestContext
    ObjectPropStaticArray: AttributePropertyValueResolverTestContext
    ObjectPropDynamicArray: unreal.WrappedArray[
        AttributePropertyValueResolverTestContext
    ]
    StructProp: AttributePropertyValueResolverTestStruct
    StructPropStaticArray: AttributePropertyValueResolverTestStruct
    StructPropDynamicArray: unreal.WrappedArray[
        AttributePropertyValueResolverTestStruct
    ]


class BalanceFormulaAttributeValueResolver(AttributeValueResolver):
    Value: BalanceFormulaDefinedValueRow
    AdditionalScalars: unreal.WrappedArray[AttributeInitializationData]


class BalanceStateAttributeValueResolver(AttributeValueResolver):
    ValueToResolve: EBalanceValueType


class BalanceTableAttributeValueResolver(DataTableFunctionAttributeValueResolver): ...


class BlackboardKeyAttributeContextResolver(AttributeContextResolver):
    BlackboardKey: GbxBlackboardKeySelector


class BlackboardKeyType_GbxFlag(aimodule.BlackboardKeyType): ...


class BlackboardKeyType_Struct(aimodule.BlackboardKeyType):
    Type: core_uobject.ScriptStruct


class BlackboardKeyType_TargetActorInfo(aimodule.BlackboardKeyType): ...


class BoneModBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def SetBoneTranslation(
        self,
        BoneName: str,
        Translation: core_uobject.Vector,
        Target: unreal.UObject,
        InBlendTime: float,
        InBlendOption: engine.EAlphaBlendOption,
        InCustomBlendCurve: engine.CurveFloat,
    ): ...
    def SetBoneScale3D(
        self,
        BoneName: str,
        Scale3D: core_uobject.Vector,
        Target: unreal.UObject,
        InBlendTime: float,
        InBlendOption: engine.EAlphaBlendOption,
        InCustomBlendCurve: engine.CurveFloat,
    ): ...
    def SetBoneScale(
        self,
        BoneName: str,
        Scale: float,
        Target: unreal.UObject,
        InBlendTime: float,
        InBlendOption: engine.EAlphaBlendOption,
        InCustomBlendCurve: engine.CurveFloat,
    ): ...
    def SetBoneRotation(
        self,
        BoneName: str,
        Rotation: core_uobject.Rotator,
        Target: unreal.UObject,
        InBlendTime: float,
        InBlendOption: engine.EAlphaBlendOption,
        InCustomBlendCurve: engine.CurveFloat,
    ): ...
    def SetBoneModUseTranslation(
        self, BoneModName: str, bUseTranslation: bool, Target: unreal.UObject
    ): ...
    def SetBoneModUseScale(
        self, BoneModName: str, bUseScale: bool, Target: unreal.UObject
    ): ...
    def SetBoneModUseRotation(
        self, BoneModName: str, bUseRotation: bool, Target: unreal.UObject
    ): ...
    def SetBoneModTranslationSpace(
        self, BoneModName: str, TranslationSpace: int, Target: unreal.UObject
    ): ...
    def SetBoneModTranslation(
        self, BoneModName: str, Translation: core_uobject.Vector, Target: unreal.UObject
    ): ...
    def SetBoneModTransform(
        self,
        BoneModName: str,
        Transform: core_uobject.Transform,
        Target: unreal.UObject,
    ): ...
    def SetBoneModScale3D(
        self, BoneModName: str, Scale: core_uobject.Vector, Target: unreal.UObject
    ): ...
    def SetBoneModScale(
        self, BoneModName: str, Scale: float, Target: unreal.UObject
    ): ...
    def SetBoneModRotationSpace(
        self, BoneModName: str, RotationSpace: int, Target: unreal.UObject
    ): ...
    def SetBoneModRotation(
        self, BoneModName: str, Rotation: core_uobject.Rotator, Target: unreal.UObject
    ): ...
    def SetBoneModReplaceTranslation(
        self, BoneModName: str, bReplaceTranslation: bool, Target: unreal.UObject
    ): ...
    def SetBoneModReplaceScale(
        self, BoneModName: str, bReplaceScale: bool, Target: unreal.UObject
    ): ...
    def SetBoneModReplaceRotation(
        self, BoneModName: str, bReplaceRotation: bool, Target: unreal.UObject
    ): ...
    def SetBoneModName(
        self, BoneModName: str, NewBoneModName: str, Target: unreal.UObject
    ): ...
    def SetBoneModifyProfileState(
        self, StateName: str, bActive: bool, Target: unreal.UObject, BlendTime: float
    ): ...
    def SetBoneModifyProfile(
        self, BoneModifyProfile: GbxBoneModifyProfile, Target: unreal.UObject
    ): ...
    def SetBoneModBoneName(
        self, BoneModName: str, BoneModBoneName: str, Target: unreal.UObject
    ): ...
    def SetBoneModBlendTime(
        self, BoneModName: str, BlendTime: float, Target: unreal.UObject
    ): ...
    def SetBoneModAlphaBlend(
        self, BoneModName: str, Blend: engine.AlphaBlend, Target: unreal.UObject
    ): ...
    def SetBoneModActive(
        self, BoneModName: str, bActive: bool, Target: unreal.UObject
    ): ...
    def SetBoneMod(
        self,
        InBoneMod: engine.BoneModInstance,
        BoneModToSet: str,
        Target: unreal.UObject,
        bBlendIn: bool,
    ): ...
    def RemoveBoneMod(
        self, BoneModToRemove: str, Target: unreal.UObject, bBlendOut: bool
    ): ...
    def GetBoneMod(
        self, BoneModName: str, BoneMod: engine.BoneModInstance, Target: unreal.UObject
    ) -> bool: ...
    def CreateBoneMod(
        self,
        InBoneModName: str,
        InBoneName: str,
        InTranslation: core_uobject.Vector,
        InRotation: core_uobject.Rotator,
        InScale: core_uobject.Vector,
        InBlendTime: float,
        Target: unreal.UObject,
        InBlendOption: engine.EAlphaBlendOption,
        InCustomBlendCurve: engine.CurveFloat,
        bInUseTranslation: bool,
        bInUseRotation: bool,
        bInUseScale: bool,
        bInReplaceTranslation: bool,
        bInReplaceRotation: bool,
        bInReplaceScale: bool,
        InTranslationSpace: int,
        InRotationSpace: int,
        bBlendIn: bool,
    ): ...


class BoneModComponent(engine.SceneComponent):
    bUseTranslation: bool
    TranslationSpace: int
    bReplaceTranslation: bool
    bUseRotation: bool
    RotationSpace: int
    bReplaceRotation: bool
    bUseScale: bool
    bReplaceScale: bool
    Blend: engine.AlphaBlend
    bStartActive: bool


class BTDecorator_GbxCondition(aimodule.BTDecorator):
    Condition: gbx_runtime.GbxCondition


class BTTask_PlayGbxAction(aimodule.BTTaskNode):
    ActionClassToPlay: unreal.UClass
    CachedActionComponent: GbxActionComponent
    CachedBTComponent: aimodule.BehaviorTreeComponent


class CauseDamageContextSourceInterface(core_uobject.Interface): ...


class ChallengeConditionData(gbx_runtime.GbxDataAsset):
    Description: str
    StatId: GameStatData
    TargetValue: int


class ChallengeLevelActorComponent(GbxAreaComponent):
    BaseChallengeReference: unreal.UClass
    ChallengeReference: unreal.UClass
    bShowInZoneMap: bool
    bShowInMiniMap: bool
    bShowInWorld: bool
    bInWorldIconEnabled: bool
    UnfogRadiusWhenChallengeActive: float
    UnfogHeightWhenChallengeActive: float
    IconGuid: core_uobject.Guid
    bIsStationary: bool
    OnPlayerChallengeActivated: Any
    OnPlayerChallengeCompleted: Any
    OnPlayerEnteredChallengeArea: Any
    OnPlayerExitedChallengeArea: Any
    OwningLevelActorComponent: ChallengeLevelActorComponent

    def SetIsStationary(self, bInIsStationary: bool): ...
    def SetInWorldIconEnabled(self, bEnable: bool): ...
    def OnRep_IsStationary(self, bOldIsStationary: bool): ...
    def OnRep_InWorldIconEnabled(self, bOldEnabled: bool): ...
    def OnRep_ChallengeReference(self): ...
    def HandleAttachmentChanged(self): ...
    def GetAssociatedActor(self) -> engine.Actor: ...


class ChallengeLevelParentComponent(ChallengeLevelActorComponent):
    bHideIfAssociatedActors: bool
    OnAllAssociatedActorsDestroyed: Any
    AssociatedActors: unreal.WrappedArray[ChallengeLevelActorComponent]

    def RemoveAssociatedActorComponent(
        self, AssociatedComponent: ChallengeLevelActorComponent
    ): ...
    def RemoveAssociatedActor(self, AssociatedActor: engine.Actor): ...
    def ClearAssociatedActors(self): ...
    def AddAssociatedActor(
        self,
        AssociatedActor: engine.Actor,
        ComponentClass: unreal.UClass,
        RelativeOffset: core_uobject.Vector,
    ): ...


class ChallengeObserverInterface(core_uobject.Interface): ...


class ChallengeRewardData(gbx_runtime.GbxDataAsset):
    RewardName: str
    Description: str
    RewardString: str
    AttrInitDef: AttributeInitializationData
    CachedRewardIndex: int


class ChallengeSystemSettings(unreal.UObject):
    MinimumGoalForChallengeNotification: float
    ChallengeCompletionThresholdNotification: unreal.WrappedArray[float]
    ChallengeRanksForToken: AttributeInitializationData
    ChallengePointsPerRank: int
    ChallengeRewards: unreal.WrappedArray[core_uobject.SoftObjectPath]
    DefaultChallengeComponent: unreal.UClass


class CharacterBestTargetAttributeContextResolver(AttributeContextResolver): ...


class CharacterMovementAttributeValueResolver(AttributeValueResolver):
    ValueToResolve: ECharacterMovementAttributeValueType


class CinematicModeBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def PushCinematicMode(
        self, WorldContextObject: unreal.UObject, InCinematicMode: CinematicModeData
    ): ...
    def PopCinematicMode(
        self, WorldContextObject: unreal.UObject, InCinematicMode: CinematicModeData
    ): ...
    def ClearCinematicMode(self, WorldContextObject: unreal.UObject): ...
    def ClearAndSetCinematicMode(
        self, WorldContextObject: unreal.UObject, InCinematicMode: CinematicModeData
    ): ...


class ClothManagerInterface(engine.Actor): ...


class Beacon(engine.Actor):

    def OnBeaconSourceEndPlay(self, Actor: engine.Actor, EndPlayReason: int): ...


class ConditionalAttributeValueResolver(AttributeValueResolver):
    DefaultValue: AttributeInitializationData
    Scaler: AttributeInitializationData
    ConditionalValues: unreal.WrappedArray[AttributeConditionalValue]


class ConditionalDamageModifier(gbx_runtime.GbxDataAsset):
    AttackerCondition: gbx_runtime.GbxCondition
    bAttackerConditionFirstContextIsOverrideContextObject: bool
    bAttackerConditionSecondContextIsDamageCauser: bool
    DefenderCondition: gbx_runtime.GbxCondition
    bDefenderConditionFirstContextIsOverrideContextObject: bool
    bDefenderConditionSecondContextIsDamageCauser: bool
    DamageTypeFilterMode: EDamageFilterExprMode
    DamageTypeFilter: unreal.WrappedArray[unreal.UClass]
    DamageSourceFilterMode: EDamageFilterExprMode
    bIncludeDamageSourceSubclasses: bool
    DamageSourceFilter: unreal.WrappedArray[unreal.UClass]
    bUseHitDirectionAngle: bool
    HitDirectionAngle: AttributeInitializationData
    HitDirectionAngleOffset: AttributeInitializationData
    bUseCriticalFilter: bool
    CriticalFilter: EConditionalDamageCriticalFilter
    bUseAreaDamageFilter: bool
    AreaDamageFilter: EConditionalAreaDamageFilter
    bUseRandomChance: bool
    RandomChance: AttributeInitializationData
    bCanTriggerOnBonusDamage: bool
    bAppliesToInstigatorChildren: bool


class ConditionalDamageCriticalModifier(ConditionalDamageModifier):
    bOnlyApplyIfHitRegionWasCritical: bool
    bUseDefaultCriticalHitMultiplier: bool
    AdditionalCriticalMultiplier: AttributeInitializationData


class ConditionalDamageHitRegionModifier(ConditionalDamageModifier):
    Priority: int
    OverrideHitRegion: HitRegionData


class ConditionalDamageTypeModifier(ConditionalDamageModifier):
    OverrideDamageType: unreal.UClass
    ConditionalDamageTypes: unreal.WrappedArray[ConditionalDamageDamageTypeConditional]
    OptionalOverrideDamageSource: unreal.UClass
    BonusMode: EConditionalDamageTypeBonusMode
    ExtraDamagePercent: AttributeInitializationData
    OverridePrimaryDamageTypeScale: AttributeInitializationData
    Priority: int


class ConditionalDamageValueModifier(ConditionalDamageModifier):
    ModifierType: EConditionalDamageModifierType
    DamageValue: AttributeInitializationData
    ConditionalDamageValues: unreal.WrappedArray[
        ConditionalDamageDamageConditionalValue
    ]
    bModifyValueBasedOnDistance: bool
    ModifyValueBasedOnDistanceCurve: engine.RuntimeFloatCurve
    bDisallowFatalDamage: bool


class ConstantAttributeValueResolver(AttributeValueResolver):
    Value: AttributeInitializationData


class ControlledMoveFunctionLibrary(engine.BlueprintFunctionLibrary):

    def StopControlledMove(
        self,
        Actor: engine.Actor,
        ControlledMove: unreal.UClass,
        bZeroVelocity: bool,
        bInterrupted: bool,
    ): ...
    def StartControlledMove(
        self,
        Actor: engine.Actor,
        ControlledMove: unreal.UClass,
        Instigator: engine.Actor,
        SpeedOverride: float,
        DurationOverride: float,
        LaunchAngleOverride: float,
        TargetActor: engine.Actor,
        TargetLocation: core_uobject.Vector,
    ) -> bool: ...
    def IsPerformingSpecificControlledMove(
        self, Actor: engine.Actor, ControlledMove: unreal.UClass
    ) -> bool: ...
    def IsPerformingControlledMove(self, Actor: engine.Actor) -> bool: ...


class ControllerAttributeContextResolver(AttributeContextResolver): ...


class CoordinatedEffectBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def GetOriginalOverrideMaterialAtIndex(
        self, MeshComponent: engine.MeshComponent, Index: int, OutActualIndex: int
    ) -> engine.MaterialInterface: ...


class DamageableInterface(core_uobject.Interface): ...


class DamageAreaType(unreal.UObject):
    MaxTargets: int
    bUseMaxTargets: bool
    bDoDirectDamageToImpactedActor: bool
    bIgnoreWorldGeometry: bool
    bTryDirectTraceFirst: bool
    bSkipBackupImpactTrace: bool
    bForceZeroPitch: bool
    bZeroPitchBeforeApplyingHitStartOffset: bool
    bForceZeroRoll: bool
    TraceChannel: int
    bTraceToGround: bool
    TraceToGroundDownwardDistance: float
    TraceToGroundStartHeightOffset: float
    TraceToGroundHitOffset: float
    OverlapFilter: EDamageAreaOverlapFilterType
    OverlapProfileName: str
    OverlapObjectTypes: unreal.WrappedArray[int]


class DamageAreaType_BaseRound(DamageAreaType):
    Radius: AttributeInitializationData
    bComputeHitDirectionFromTarget: bool
    bExpandRadiusOverTime: bool
    bExpandingRadiusIsHollow: bool


class DamageAreaType_Sphere(DamageAreaType_BaseRound):
    bTreatAsRadiusDamage: bool
    bDamageFallsOff: bool


class DamageAreaType_Cylinder(DamageAreaType_BaseRound):
    HalfHeight: AttributeInitializationData
    HeightOffset: AttributeInitializationData
    WedgeAngle: AttributeInitializationData


class DamageAreaType_Cone(DamageAreaType):
    Length: AttributeInitializationData
    ConeAngle: AttributeInitializationData


class DamageAreaType_Box(DamageAreaType):
    HalfHeight: AttributeInitializationData
    HalfWidth: AttributeInitializationData
    HalfDepth: AttributeInitializationData
    OriginType: EDamageAreaBoxOriginType
    bDamageFallsOff: bool


class DamageAreaType_Capsule(DamageAreaType):
    HalfHeight: AttributeInitializationData
    Radius: AttributeInitializationData


class DamageAsyncManager(unreal.UObject):
    CauseDamageRequests: unreal.WrappedArray[CauseDamageAsyncRequestEntry]
    PendingCauseDamageRequests: unreal.WrappedArray[CauseDamageAsyncRequestEntry]
    MaxNumCauseDamagePerFrame: int


class DamageCauserInterface(core_uobject.Interface): ...


class DamageStatics(engine.BlueprintFunctionLibrary):

    def StopCausingDamageToTarget(
        self,
        DamageCauser: engine.Actor,
        DamageTarget: engine.Actor,
        DamageData: unreal.UClass,
    ): ...
    def StopCausingDamage(
        self, DamageCauser: engine.Actor, DamageData: unreal.UClass
    ): ...
    def StopCausingAllDamage(self, DamageCauser: engine.Actor): ...
    def MakePipelineDamageInput(
        self,
        DamageCauser: engine.Actor,
        DamageReceiver: engine.Actor,
        DamageType: unreal.UClass,
        DamageSource: unreal.UClass,
        HitInfo: engine.HitResult,
        HitLocation: core_uobject.Vector,
        HitDirection: core_uobject.Vector,
        HitForceDirection: core_uobject.Vector,
        HitForceMagnitude: ForceSelection,
    ) -> PipelineDamageInput: ...
    def GetSummary_ForceSelection(self, ForceSelection: ForceSelection) -> str: ...
    def GetDamageTypeFromClass(
        self, DamageTypeClass: unreal.UClass
    ) -> GbxDamageType: ...
    def GetDamageSourceFromClass(
        self, DamageSourceClass: unreal.UClass
    ) -> DamageSource: ...
    def Conv_ForceSelectionToFloat(self, ForceSelection: ForceSelection) -> float: ...
    def Conv_FloatToForceSelection(self, ForceSelection: float) -> ForceSelection: ...
    def ApplyDamageInRadius(
        self,
        WorldContextObject: unreal.UObject,
        BaseDamage: float,
        Origin: core_uobject.Vector,
        Radius: float,
        DamageType: unreal.UClass,
        DamageSource: unreal.UClass,
        IgnoreActors: unreal.WrappedArray[engine.Actor],
        DamageCauser: engine.Actor,
        EventInstigator: engine.Controller,
        BaseImpactForce: ForceSelection,
        DamagePreventionChannel: int,
        bDamageFalloff: bool,
        DamageModifierComponent: DamageModifierComponent,
        InstigatorFeedback: FeedbackData,
        bUseInstigatorRadiusDamageScale: bool,
    ): ...
    def ApplyDamageEx(self, PipelineInput: PipelineDamageInput, BaseDamage: float): ...
    def ApplyDamage(
        self,
        DamageReceiver: engine.Actor,
        BaseDamage: float,
        DamageType: unreal.UClass,
        DamageSource: unreal.UClass,
        EventInstigator: engine.Controller,
        DamageCauser: engine.Actor,
    ): ...


class DeathData(gbx_runtime.GbxDataAsset):
    DiedStats: unreal.WrappedArray[GameStatData]
    DissolveCorpseDelayBeforeDestroy: float


class Decorator(engine.Actor): ...


class DrunkenBaseMovementComponent(engine.ActorComponent):
    StartApproachDistance: float
    StartDelayTime: float
    EaseInTime: float
    RandomNumberSeed: int


class DrunkenRandomMovementComponent(DrunkenBaseMovementComponent):
    PathCorrectionInterval: float
    TurnSpeed: float
    MaxSpreadAngle: float
    MaxDepartureAngle: float
    bGravityAffectsDrunkenness: bool
    DrunkenGravityScalar: float
    bFixDrunkenMovementAcceleration: bool


class DrunkenWaveMovementComponent(DrunkenBaseMovementComponent):
    Waveforms: unreal.WrappedArray[Vector2DWaveform]
    GlobalWaveformScale: float
    MaxRandomWaveOffsetTime: float
    bGravityAffectsDrunkenness: bool
    DrunkenGravityScalar: float


class DynamicPhysicalAnimationComponent(engine.ActorComponent):
    PhysicalAnimationCollisionProfileName: str
    KinematicAnimationCollisionProfileName: str
    ExclusionBones: unreal.WrappedArray[str]
    SupportBones: unreal.WrappedArray[str]
    SkeletalMeshComponent: engine.SkeletalMeshComponent
    PhysicsAsset: engine.PhysicsAsset
    bHasPhysicallyAnimatingBones: bool

    def SetStrengthMultiplier(self, NewValue: float): ...
    def SetSkeletalMeshComponent(
        self, NewSkeletalMeshComponent: engine.SkeletalMeshComponent
    ): ...
    def SetRootMotionControl(
        self, MotionControl: EPhysicalAnimationRootMotionControl
    ): ...
    def SetHasAnimationPlaying(self, bPlaying: bool): ...
    def SetEnableRagdoll(self, bEnable: bool): ...
    def SetEnablePhysicalAnimation(self, bEnable: bool, BodyName: str): ...
    def SetActiveProfile(self, Profile: PhysicalAnimationProfileAsset): ...
    def OnRigidBodyOverlap(
        self,
        HitComponent: engine.PrimitiveComponent,
        OtherActor: engine.Actor,
        OtherComp: engine.PrimitiveComponent,
        NormalImpulse: core_uobject.Vector,
        Hit: engine.HitResult,
    ): ...
    def GetStrengthMultiplier(self) -> float: ...
    def GetRootMotionControl(self) -> EPhysicalAnimationRootMotionControl: ...
    def DetachBodyFromAllExternalRigidBodies(self, BodyName: str): ...
    def AttachBodyTo(
        self,
        BodyName: str,
        AttachToComponent: engine.PrimitiveComponent,
        AttachToBodyName: str,
        VelocitySpaceBlend: float,
        BreakForce: float,
    ): ...


class EnvQueryContext_AimStart(aimodule.EnvQueryContext): ...


class EnvQueryContext_AimEnd(aimodule.EnvQueryContext): ...


class EnvQueryContext_Owner_AimStart(aimodule.EnvQueryContext): ...


class EnvQueryContext_Owner_AimEnd(aimodule.EnvQueryContext): ...


class EnvQueryContext_LastResult(aimodule.EnvQueryContext): ...


class EnvQueryContext_Origin(EnvQueryContext_EnvQueryParam): ...


class EnvQueryContext_PlayerMaster(aimodule.EnvQueryContext): ...


class EnvQueryContext_Players(aimodule.EnvQueryContext): ...


class EnvQueryContext_QuerierAimDirection(aimodule.EnvQueryContext): ...


class EnvQueryContext_QuerierAimDirection2D(aimodule.EnvQueryContext): ...


class EnvQueryContext_QuerierAimLocation(aimodule.EnvQueryContext): ...


class EnvQueryContext_QuerierMoveDirection(aimodule.EnvQueryContext): ...


class EnvQueryContext_TargetNavLocation(aimodule.EnvQueryContext): ...


class EnvQueryGenerator_TargetActorInfo(aimodule.EnvQueryGenerator):
    MaxAge: float
    bAllowHostiles: bool
    bAllowFriendlies: bool
    bAllowNeutrals: bool
    TagQuery: ActorTagCompositeQuery
    bUseAllowedTypes: bool
    AllowedTypes: unreal.WrappedArray[Any]
    AllowedTypesCache: unreal.WrappedArray[unreal.UClass]


class EnvQueryItemType_Targetable(aimodule.EnvQueryItemType_Actor): ...


class EnvQueryItemType_TargetActorInfo(aimodule.EnvQueryItemType_ActorBase): ...


class EnvQueryContext_InputTarget(EnvQueryContext_EnvQueryParam): ...


class EnvQueryContext_InputTargetMoveDir(EnvQueryContext_EnvQueryParam): ...


class EnvQueryParamsExt(engine.BlueprintFunctionLibrary):

    def RunEnvQueryForBestLocation(
        self,
        QueryOwner: unreal.UObject,
        QueryParams: EnvQueryParams,
        ResultLocation: core_uobject.Vector,
    ) -> bool: ...
    def RunEnvQueryForBestActor(
        self,
        QueryOwner: unreal.UObject,
        QueryParams: EnvQueryParams,
        ResultActor: engine.Actor,
    ) -> bool: ...
    def RunEnvQueryForAllLocations(
        self,
        QueryOwner: unreal.UObject,
        QueryParams: EnvQueryParams,
        ResultLocations: unreal.WrappedArray[core_uobject.Vector],
    ) -> bool: ...
    def RunEnvQueryForAllActors(
        self,
        QueryOwner: unreal.UObject,
        QueryParams: EnvQueryParams,
        ResultActors: unreal.WrappedArray[engine.Actor],
    ) -> bool: ...
    def HasQuery(self, QueryParams: EnvQueryParams) -> bool: ...
    def GetDescription(self, QueryParams: EnvQueryParams) -> str: ...


class EnvQueryParamsProvider(core_uobject.Interface): ...


class EnvQueryTest_ProjectilesHomingTowardsTarget(aimodule.EnvQueryTest):
    bMustBeActivelyHoming: bool


class EnvQueryTestAsset(gbx_runtime.GbxDataAsset):
    EnvQueryTest: aimodule.EnvQueryTest


class EQSProxyInterface(core_uobject.Interface): ...


class ExplosionBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def PlayExplosion(
        self,
        ExplosionData: ExplosionData,
        Size: float,
        ExplosionLocation: core_uobject.Vector,
        Context: unreal.UObject,
        DamageType: unreal.UClass,
    ) -> engine.ParticleSystemComponent: ...


class DamageInfoFunctionLibrary(engine.BlueprintFunctionLibrary):

    def SetImpactForce(self, DamageInfo: DamageInfo, InImpactForce: float): ...
    def SetDamageType(self, DamageInfo: DamageInfo, InDamageType: unreal.UClass): ...
    def SetDamageSource(
        self, DamageInfo: DamageInfo, InDamageSource: unreal.UClass
    ): ...
    def SetDamageRadius(self, DamageInfo: DamageInfo, InDamageRadius: float): ...
    def SetDamageModifierComponent(
        self, DamageInfo: DamageInfo, InModifierComponent: DamageModifierComponent
    ): ...
    def SetDamageCauser(self, DamageInfo: DamageInfo, InDamageCauser: engine.Actor): ...
    def SetDamage(self, DamageInfo: DamageInfo, InDamage: float): ...
    def SetCriticalHitDamageOverrides(
        self, DamageInfo: DamageInfo, Overrides: CriticalHitDamageOverrides
    ): ...
    def SetApplyCriticalHitModsToAoEDamage(
        self, DamageInfo: DamageInfo, bApplyCriticalHitModsToAoEDamage: bool
    ): ...
    def GetImpactForce(self, DamageInfo: DamageInfo) -> float: ...
    def GetDamageType(self, DamageInfo: DamageInfo) -> unreal.UClass: ...
    def GetDamageSource(self, DamageInfo: DamageInfo) -> unreal.UClass: ...
    def GetDamageRadius(self, DamageInfo: DamageInfo) -> float: ...
    def GetDamageModifierComponent(
        self, DamageInfo: DamageInfo
    ) -> DamageModifierComponent: ...
    def GetDamageCauser(self, DamageInfo: DamageInfo) -> engine.Actor: ...
    def GetDamage(self, DamageInfo: DamageInfo) -> float: ...
    def GetCriticalHitDamageOverrides(
        self, DamageInfo: DamageInfo
    ) -> CriticalHitDamageOverrides: ...
    def GetApplyCriticalHitModsToAoEDamage(self, DamageInfo: DamageInfo) -> bool: ...


class ExplosionComponent(engine.ActorComponent):
    ExplosionRadius: engine.GbxAttributeFloat
    ExplosionParticleSystem: engine.ParticleSystem
    ExplosionEffectCollection: unreal.UClass
    ParticleSystemSize: float
    bModifyParticleSystemSize: bool
    ExplosionAudioEvent: wwise_audio.WwiseEvent
    SoundPerception: SoundPerceptionProperties
    Feedback: FeedbackData
    MaxFeedbackRangeScalar: float
    bCauseExplosionDamage: bool
    bOverrideLocation: bool
    LocationOverride: core_uobject.Vector

    def SetExplosionLocation(self, NewLocation: core_uobject.Vector): ...
    def Explode(self, DamageInfo: DamageInfo): ...


class ExplosionData(gbx_runtime.GbxDataAsset):
    DefaultExplosionSizeData: ExplosionSizeSelectionData
    DamageTypeSelections: unreal.WrappedArray[DamageTypeExplosionAssociation]
    bUseRadialBlurOverride: bool
    RadialBlurOverride: engine.RadialBlurSelection
    TinnitusDuration: EExplosionTinnitusDuration
    bUseBasicExplosion: bool
    SignificanceEvent: GbxSignificanceEvent
    bCensorThisExplosion: bool
    FeedbackOverride: FeedbackData
    ParticleSystemOverride: engine.ParticleSystem
    CensoredParticleSystemOverride: engine.ParticleSystem
    AudioEventOverride: wwise_audio.WwiseEvent
    ImpactOverride: ImpactData
    FeedbackFalloffMinDistanceScalar: float
    FeedbackFalloffMaxDistanceScalar: float

    def SelectExplosion(
        self, Size: float, DamageType: unreal.UClass
    ) -> ExplosionSizeProperties: ...


class ExplosionSizeSelectionData(gbx_runtime.GbxDataAsset):
    SizeProperties: unreal.WrappedArray[ExplosionSizeProperties]

    def GetExplosionPropertiesBySize(self, Size: float) -> ExplosionSizeProperties: ...


class EyesOfDeathComponent(engine.PrimitiveComponent): ...


class FeedbackData(gbx_runtime.GbxDataAsset):
    FeedbackType: int
    ControllerRumbleDetails: unreal.WrappedArray[engine.ForceFeedbackChannelDetails]
    ExternalForceFeedbackEffects: unreal.WrappedArray[engine.ForceFeedbackEffect]
    MinControllerRumbleDetails: unreal.WrappedArray[engine.ForceFeedbackChannelDetails]
    MinExternalForceFeedbackEffects: unreal.WrappedArray[engine.ForceFeedbackEffect]
    bAbsoluteControllerRumbleScale: bool
    CameraShakeClass: unreal.UClass
    CameraShakeClassNegativeXAxis: unreal.UClass
    CameraShakeClassYAxis: unreal.UClass
    CameraShakeClassNegativeYAxis: unreal.UClass
    OscillationDuration: float
    OscillationBlendInTime: float
    OscillationBlendOutTime: float
    RotOscillation: engine.ROscillator
    LocOscillation: engine.VOscillator
    FOVOscillation: engine.FOscillator
    RandomShakeInterval: float
    MaxRandomShakeScalar: float
    MinRandomShakeScalar: float
    BaseCameraScale: AttributeInitializationData
    AdditionalCameraShakes: unreal.WrappedArray[ShakeScaleAssociation]
    FirstPersonImpulseType: EFeedbackDataFirstPersonImpulseType
    CustomFirstPersonImpulse: FeedbackDataFirstPersonImpulse
    ParticleSystem: engine.ParticleSystem
    bHideWhenFinished: bool
    ContentDims: core_uobject.Vector2D
    ParticleDepth: float
    ScalingMode: EScreenParticleScalingMode
    bOnlyOwnerSee: bool
    bAlwaysVisible: bool
    bTickParticleEvenWhenPaused: bool
    Tag: str
    bLetSystemFinishAfterStopping: bool
    HUDImpulse: GbxHUDFeedbackImpulse
    bLooping: bool
    EffectFalloffMinDistance: float
    EffectFalloffMaxDistance: float
    AssociatedFeedbacks: unreal.WrappedArray[FeedbackData]
    bUpdateSourceLocation: bool
    bScaleDownOverTime: bool
    bUseScaleOverTimeCurve: bool
    ScaleOverTimeCurve: engine.RuntimeFloatCurve
    bUseContinuousAttributeScale: bool
    ContinuousScale: AttributeInitializationData
    ContinuousScaleCurve: engine.RuntimeFloatCurve
    bPlayRadialBlur: bool
    RadialBlurInfo: engine.RadialBlurSelection
    bOverrideRadialBlurCenter: bool
    RadialBlurWorldSpaceCenter: core_uobject.Vector
    RadialBlurMaxDistance: float
    LoopingShakes: unreal.WrappedArray[LoopingShakeInfo]

    def StopFeedbackForAll(
        self, FeedbackData: FeedbackData, WorldContextObject: unreal.UObject
    ): ...
    def StopFeedback(
        self, FeedbackData: FeedbackData, Controller: engine.PlayerController
    ): ...
    def StopDefaultFeedbackForAll(
        self, Feedback: FeedbackTableRowHandle, WorldContextObject: unreal.UObject
    ): ...
    def StopDefaultFeedback(
        self, Feedback: FeedbackTableRowHandle, Controller: engine.PlayerController
    ): ...
    def PerformFeedbackForAllAtLocation(
        self,
        FeedbackData: FeedbackData,
        SourceLocation: core_uobject.Vector,
        RangedDistanceOverrides: RangedDistanceOverrides,
        bLoop: bool,
        WorldContextObject: unreal.UObject,
        SourceContext: unreal.UObject,
        ControllerToIgnore: engine.PlayerController,
        OverrideControllerFeedback: FeedbackData,
    ): ...
    def PerformFeedbackForAll(
        self,
        FeedbackData: FeedbackData,
        Scale: float,
        bLoop: bool,
        WorldContextObject: unreal.UObject,
        SourceContext: unreal.UObject,
        ControllerToIgnore: engine.PlayerController,
        OverrideControllerFeedback: FeedbackData,
    ): ...
    def PerformFeedbackAtLocation(
        self,
        FeedbackData: FeedbackData,
        Controller: engine.PlayerController,
        SourceLocation: core_uobject.Vector,
        RangedDistanceOverrides: RangedDistanceOverrides,
        bLoop: bool,
        SourceContext: unreal.UObject,
        ControllerToIgnore: engine.PlayerController,
        OverrideControllerFeedback: FeedbackData,
    ): ...
    def PerformFeedback(
        self,
        FeedbackData: FeedbackData,
        Controller: engine.PlayerController,
        Scale: float,
        bLoop: bool,
        SourceContext: unreal.UObject,
    ): ...
    def PerformDefaultFeedbackForAllAtLocation(
        self,
        Feedback: FeedbackTableRowHandle,
        SourceLocation: core_uobject.Vector,
        RangedDistanceOverrides: RangedDistanceOverrides,
        bLoop: bool,
        WorldContextObject: unreal.UObject,
        SourceContext: unreal.UObject,
        ControllerToIgnore: engine.PlayerController,
        OverrideControllerFeedback: FeedbackData,
    ): ...
    def PerformDefaultFeedbackForAll(
        self,
        Feedback: FeedbackTableRowHandle,
        Scale: float,
        bLoop: bool,
        WorldContextObject: unreal.UObject,
        SourceContext: unreal.UObject,
        ControllerToIgnore: engine.PlayerController,
        OverrideControllerFeedback: FeedbackData,
    ): ...
    def PerformDefaultFeedbackAtLocation(
        self,
        Feedback: FeedbackTableRowHandle,
        Controller: engine.PlayerController,
        SourceLocation: core_uobject.Vector,
        RangedDistanceOverrides: RangedDistanceOverrides,
        bLoop: bool,
        SourceContext: unreal.UObject,
        ControllerToIgnore: engine.PlayerController,
        OverrideControllerFeedback: FeedbackData,
    ): ...
    def PerformDefaultFeedback(
        self,
        Feedback: FeedbackTableRowHandle,
        Controller: engine.PlayerController,
        Scale: float,
        bLoop: bool,
        SourceContext: unreal.UObject,
    ): ...
    def GetFeedbackDuration(self, FeedbackData: FeedbackData) -> float: ...
    def GetFeedbackDataRange(
        self, FeedbackData: FeedbackData, MinRange: float, MaxRange: float
    ): ...


class FirstPersonConfigurationData(engine.Actor):
    bAutoFillComponentVariables: bool
    Arms: GbxSkeletalMeshComponent


class FXVolumeManager(unreal.UObject):

    def OnVolumeDestroyed(self, DestroyedActor: engine.Actor): ...
    def OnPlayerDestroyed(self, DestroyedActor: engine.Actor): ...


class FXVolume(engine.Volume):
    ParticleSystem: engine.ParticleSystem
    ParticleDepth: float
    TagName: str
    bDepthPriorityWorld: bool

    def OnActorLeftVolume(
        self,
        OverlappedComponent: engine.PrimitiveComponent,
        Other: engine.Actor,
        OtherComp: engine.PrimitiveComponent,
        OtherBodyIndex: int,
    ): ...
    def OnActorEnteredVolume(
        self,
        OverlappedComp: engine.PrimitiveComponent,
        Other: engine.Actor,
        OtherComp: engine.PrimitiveComponent,
        OtherBodyIndex: int,
        bFromSweep: bool,
        OverlapInfo: engine.HitResult,
    ): ...


class GameplayTagBasedAttributeValueResolver(AttributeValueResolver):
    TagToValueMap: unreal.WrappedArray[GameplayTagToValueMap]
    ValueIfNoTagIsFound: AttributeInitializationData


class GameplayTagContainerComponent(engine.ActorComponent):
    TagContainer: gameplay_tags.GameplayTagContainer

    def GetGameplayTagContainerFromActor(
        self, Actor: engine.Actor, Branches: EContainsTagComponent
    ) -> GameplayTagContainerComponent: ...


class GameplayTask_RunEnvQuery(gameplay_tasks.GameplayTask):
    Success: Any
    Failure: Any

    def RunEnvQueryOnLocation(
        self,
        QueryOwner: engine.Actor,
        QueryParams: EnvQueryParams,
        Location: core_uobject.Vector,
    ) -> GameplayTask_RunEnvQuery: ...
    def RunEnvQueryOnActor(
        self, QueryOwner: engine.Actor, QueryParams: EnvQueryParams, Actor: engine.Actor
    ) -> GameplayTask_RunEnvQuery: ...
    def RunEnvQuery(
        self, QueryOwner: engine.Actor, QueryParams: EnvQueryParams
    ) -> GameplayTask_RunEnvQuery: ...
    def GetResultLocations(
        self,
        QueryResult: aimodule.EnvQueryResult,
        ResultLocations: unreal.WrappedArray[core_uobject.Vector],
    ) -> bool: ...
    def GetResultLocation(
        self, QueryResult: aimodule.EnvQueryResult, ResultLocation: core_uobject.Vector
    ) -> bool: ...
    def GetResultActors(
        self,
        QueryResult: aimodule.EnvQueryResult,
        ResultActors: unreal.WrappedArray[engine.Actor],
    ) -> bool: ...
    def GetResultActor(
        self, QueryResult: aimodule.EnvQueryResult, ResultActor: engine.Actor
    ) -> bool: ...


class GameResourceData(gbx_runtime.GbxDataAsset):
    ResourceName: str
    bIntegerOnlyUpdates: bool
    bSerializeInSavegame: bool
    DefaultResourcePoolData: GameResourcePoolData


class GameResourcePoolAttributePropertyValueResolver(AttributePropertyValueResolver):
    Resource: GameResourceData


class GameResourcePoolClampedMaxValueResolver(
    GameResourcePoolAttributePropertyValueResolver
): ...


class GameResourcePoolClampedValueResolver(
    GameResourcePoolAttributePropertyValueResolver
): ...


class GameResourcePoolCurrentValueResolver(AttributeValueResolver):
    Resource: GameResourceData


class GameResourcePoolCurrentValueNoPauseOnHealResolver(
    GameResourcePoolCurrentValueResolver
): ...


class GameResourcePoolData(gbx_runtime.GbxDataAsset):
    Resource: GameResourceData
    BaseMinValue: float
    BaseMaxValue: AttributeInitializationData
    StartingValue: float
    StartWithMinValue: bool
    StartWithMaxValue: bool
    bUpdateCurrentValueOnExtremaChange: bool
    MinimumReservedValue: float
    bCheckFilledAgainstOldValues: bool
    BaseConsumptionRate: float
    BaseActiveRegenerationRate: float
    BasePassiveRegenerationRate: float
    BasePassivePercentRegenerationRate: float
    BasePassiveMissingPercentRegenerationRate: float
    BaseOnIdleRegenerationRate: float
    BaseOnIdleRegenerationDelay: float
    BaseOnDepletedRegenerationDelay: float
    RecentImpulseTimer: float
    bOnlyReplicateToOwner: bool
    ReplicationType: int


class GameResourcePoolManagerComponent(engine.ActorComponent):
    ResourcePools: unreal.WrappedArray[GameResourcePool]
    PendingResourcePools: unreal.WrappedArray[GameResourcePool]
    ReplicatedPoolData: GameResourcePoolNet
    InitialResourcePools: unreal.WrappedArray[GameResourcePoolData]
    ResourceEvents: unreal.WrappedArray[GameResourceUserEvent]

    def RemoveResourcePoolDelegate(
        self,
        InResourceData: GameResourceData,
        DelegatePropertyName: str,
        ScriptDelegate: Any,
    ): ...
    def RecalculateAttributeInitializedPoolProperties(self): ...
    def OnOwnerExperienceLevelChanged(self, OldExperienceLevel: int): ...
    def GetResourcePoolByResource(
        self, Resource: GameResourceData
    ) -> GameResourcePoolReference: ...
    def CreatePool(
        self, PoolData: GameResourcePoolData, bReinitializeExistingPool: bool
    ) -> GameResourcePoolReference: ...
    def ClearResourcePoolDelegate(
        self, InResourceData: GameResourceData, DelegatePropertyName: str
    ): ...
    def AddResourcePoolDelegate(
        self,
        InResourceData: GameResourceData,
        DelegatePropertyName: str,
        ScriptDelegate: Any,
    ): ...


class GameResourcePoolFunctionLibrary(engine.BlueprintFunctionLibrary):

    def SetResourcePoolValue(
        self, InPool: GameResourcePoolReference, InValue: float
    ): ...
    def ResetResourcePoolRegenDelayByGameResourceData(
        self, Actor: engine.Actor, Resource: GameResourceData
    ): ...
    def ResetResourcePoolRegenDelay(self, InPool: GameResourcePoolReference): ...
    def RefillResourcePoolByPercentage(
        self, InPool: GameResourcePoolReference, Percentage: float, MaxPercentage: float
    ): ...
    def IsResourcePoolInState(
        self, InPool: GameResourcePoolReference, InState: EGameResourcePoolState
    ) -> bool: ...
    def GetDelegatePrefixForResourceEvent(
        self, InResourceUserEvent: GameResourceUserEvent
    ) -> str: ...
    def EqualEqual_ResourcePoolReference(
        self, A: GameResourcePoolReference, B: GameResourcePoolReference
    ) -> bool: ...
    def EqualEqual_ResourcePoolData(
        self,
        ResourcePoolReference: GameResourcePoolReference,
        ResourcePoolData: GameResourcePoolData,
    ) -> bool: ...
    def EqualEqual_ResourceData(
        self,
        ResourcePoolReference: GameResourcePoolReference,
        ResourceData: GameResourceData,
    ) -> bool: ...
    def DrainResourcePoolByPercentage(
        self, InPool: GameResourcePoolReference, Percentage: float, MinPercentage: float
    ): ...
    def DeleteResourcePool(self, InPool: GameResourcePoolReference): ...
    def ClearResourcePoolRegenDelayByGameResourceData(
        self, Actor: engine.Actor, Resource: GameResourceData
    ): ...
    def ClearResourcePoolRegenDelay(self, InPool: GameResourcePoolReference): ...
    def BreakResourcePoolReference(
        self,
        InPool: GameResourcePoolReference,
        bValid: bool,
        CurrentValue: float,
        MinValue: float,
        MaxValue: float,
    ): ...
    def AdjustResourcePoolValue(
        self, InPool: GameResourcePoolReference, InValue: float
    ): ...


class GameStatChannel(engine.Channel):
    GameStatsComponent: GameStatsComponent


class GameStatData(gbx_runtime.GbxDataAsset):
    DefaultValue: int
    MinValue: int
    bHasMinValue: bool
    MaxValue: int
    bHasMaxValue: bool
    StatName: str
    bProfileStat: bool
    bPartyStat: bool


class GameStateAttributeContextResolver(AttributeContextResolver): ...


class GameStatList(gbx_runtime.GbxDataAsset):
    GameStats: unreal.WrappedArray[GameStatData]


class GameStatsComponent(engine.ActorComponent):
    GameStats: unreal.WrappedArray[GameStat]
    GameStatChannel: GameStatChannel

    def UpdateStat(self, GameStat: GameStatData, NewValue: int): ...
    def IncrementStat(self, GameStat: GameStatData, Amount: int): ...
    def GetStatValue(self, GameStat: GameStatData) -> int: ...
    def GetGameStats(self) -> unreal.WrappedArray[GameStat]: ...


class GameStatsManager(engine.Actor):

    def UpdateStat(
        self, StatContext: engine.Actor, GameStat: GameStatData, NewValue: int
    ): ...
    def IncrementStat(
        self, StatContext: engine.Actor, GameStat: GameStatData, IncrementAmount: int
    ): ...
    def GetStatValue(
        self, StatContext: engine.Actor, GameStat: GameStatData
    ) -> int: ...


class GbxAction_AICharge(GbxAction_SimpleAnim):
    bSetLoopSpeedManually: bool
    AnimLoopSpeed: float
    StartBlendInTime: float
    LoopBlendInTime: float
    StopBlendInTime: float
    BlendOutTime: float
    StartAnims: unreal.WrappedArray[AnimMeshList]
    LoopAnims: unreal.WrappedArray[AnimMeshList]
    MissAnims: unreal.WrappedArray[AnimMeshList]
    StrikeAnims: unreal.WrappedArray[AnimMeshList]
    HitWallAnims: unreal.WrappedArray[AnimMeshList]
    ReachCliffAnims: unreal.WrappedArray[AnimMeshList]
    StopForFriendlyAnims: unreal.WrappedArray[AnimMeshList]

    def OnStrike(self, Actor: engine.Actor): ...
    def OnStopForFriendly(self, Actor: engine.Actor): ...
    def OnReachCliff(self, Actor: engine.Actor): ...
    def OnMiss(self, Actor: engine.Actor): ...
    def OnLoop(self, Actor: engine.Actor): ...
    def OnHitWall(self, Actor: engine.Actor): ...


class GbxAction_BlueprintBase(GbxAction):
    bAutoCompleted: bool


class GbxAction_ConditionContainer(GbxAction):
    ActionSelectionMethod: EActionSelectionMethod
    ConditionList: unreal.WrappedArray[ConditionActionPair]


class GbxAction_DirectionContainer(GbxAction):
    DirectionList: unreal.WrappedArray[DirectionActionData]
    DirectionData: RelativeDirectionData
    Plane: EDirectionPlane


class GbxAction_DodgePicker(GbxAction):
    IdleLeft: unreal.UClass
    IdleRight: unreal.UClass
    MovingLeft: unreal.UClass
    MovingLeftBackward: unreal.UClass
    MovingLeftForward: unreal.UClass
    MovingRight: unreal.UClass
    MovingRightBackward: unreal.UClass
    MovingRightForward: unreal.UClass


class GbxAction_DropshipSpawn(GbxAction_SimpleAnim):
    StartAnims: AnimMeshList
    InAirAnims: AnimMeshList
    RecoveryAnims: AnimMeshList
    BlendInTime: float
    BlendOutTime: float
    AnimSlot: str
    RotationLerpTime: float
    MoveWithSpawnPointTime: float
    SwitchToFallingTime: float
    AnimStart: engine.AnimSequenceBase
    AnimInAir: engine.AnimSequenceBase
    AnimRecovery: engine.AnimSequenceBase


class GbxAction_KeyedContainer(GbxAction):
    ActionKey: gameplay_tags.GameplayTag


class GbxAction_Launch(GbxAction_SimpleAnim):
    VelocityMinimum: float
    VelocityScale: float
    VelocityUpBoost: float
    RotationTime: float
    InAirAnims: AnimMeshList
    RecoveryAnims: AnimMeshList
    BlendInTime: float
    BlendOutTime: float
    AnimSlot: str
    AnimInAir: engine.AnimSequenceBase
    AnimRecovery: engine.AnimSequenceBase
    InAirAnim: AnimActionDef
    RecoveryAnim: AnimActionDef


class MotionMatchedAnimationTable(GbxAnimTable):
    RootMotionBone: str
    RootMotionBoneUpAxis: int
    bUpAxisIsNegative: bool
    RootMotionBoneForwardAxis: int
    bForwardAxisIsNegative: bool
    RootBoneForwardAxis: int
    bRootForwardAxisIsNegative: bool
    RootBoneUpAxis: int
    bRootUpAxisIsNegative: bool
    NoMotionSpeed: float
    bUseIdlePoseDriving: bool
    MinIdleTime: float
    DynamicToKinematicTransition: EDynamicToKinematicTransition
    BlendToRecoveryTime: float
    MaxAllowedDeviation: float


class GbxAction_Ragdoll(GbxAction_SimpleAnim):
    RagdollAnim: AnimActionDef
    RagdollDelayTime: float
    UpwardForceMultiplier: float
    TerminalResultantVelocity: float
    bHaltMotionBeforeImpulseApplication: bool
    RagdollAnimBlendInTime: float
    RagdollLoopingAnim: AnimActionDef
    bPlayLoopingAnimWhileNotIdle: bool
    MinRagdollTime: float
    AnimSlot: str
    AttachedObjects: unreal.WrappedArray[AttachedObjectFollow]
    RecoveryAnimations: MotionMatchedAnimationTable
    DeathReactionTag: HitReactionTag
    bCanGetup: bool
    GetupIdleTime: float
    GetupIdleSpeedThreshold: float
    GetupTestBone: str
    TestBoneUpAxis: int
    bUpAxisIsNegative: bool
    TestBoneForwardAxis: int
    bForwardAxisIsNegative: bool
    GetupAnimUp: AnimActionDef
    GetupAnimDown: AnimActionDef
    GetupBlendInTime: float
    GetupBlendOutTime: float


class GbxAction_RandomContainer(GbxAction):
    ActionList: unreal.WrappedArray[RandomActionPair]


class GbxAction_StretchBones(GbxAction_SimpleAnim):
    StretchAnimation: AnimActionDef
    BlendInTime: float
    BlendOutTime: float
    AnimSlot: str
    StretchBonesSettings: StretchBonesSettings
    bUniformStretch: bool
    TargetKey: GbxBlackboardKeySelector
    TargetOffset: core_uobject.Vector
    ActorTrackingStyle: EStretchBonesActorTrackingStyle
    bTraceToGround: bool
    TraceToGroundDistance: float
    MaxPredictionDistance: float


class StretchBonesBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def SetStretchBonesTarget(
        self,
        GbxActionRegisters: unreal.WrappedArray[GbxActionRegister],
        TargetActor: engine.Actor,
        TargetPosition: core_uobject.Vector,
    ) -> unreal.WrappedArray[GbxActionRegister]: ...
    def SetStretchBonesDistance(
        self,
        GbxActionRegisters: unreal.WrappedArray[GbxActionRegister],
        Distance: float,
    ) -> unreal.WrappedArray[GbxActionRegister]: ...


class GbxActionBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def StopLoopingActionClass(
        self, ActionClass: unreal.UClass, Target: engine.Actor
    ): ...
    def StopActionSlot(self, ActionSlotName: str, Target: engine.Actor): ...
    def StopActions(self, Target: engine.Actor): ...
    def StopActionClass(self, ActionClass: unreal.UClass, Target: engine.Actor): ...
    def SetObjectGbxActionRegister(
        self,
        GbxActionRegisters: unreal.WrappedArray[GbxActionRegister],
        RegisterKey: str,
        Value: unreal.UObject,
        bReplicates: bool,
    ) -> unreal.WrappedArray[GbxActionRegister]: ...
    def SetNameGbxActionRegister(
        self,
        GbxActionRegisters: unreal.WrappedArray[GbxActionRegister],
        RegisterKey: str,
        Value: str,
        bReplicates: bool,
    ) -> unreal.WrappedArray[GbxActionRegister]: ...
    def SetIntGbxActionRegister(
        self,
        GbxActionRegisters: unreal.WrappedArray[GbxActionRegister],
        RegisterKey: str,
        Value: int,
        bReplicates: bool,
    ) -> unreal.WrappedArray[GbxActionRegister]: ...
    def SetFloatGbxActionRegister(
        self,
        GbxActionRegisters: unreal.WrappedArray[GbxActionRegister],
        RegisterKey: str,
        Value: float,
        bReplicates: bool,
    ) -> unreal.WrappedArray[GbxActionRegister]: ...
    def K2_UpdateActionPlayRate(self, Action: GbxAction, PlayRate: float): ...
    def K2_UpdateActionDirection(
        self, Action: GbxAction, Direction: core_uobject.Vector
    ): ...
    def K2_StopActionObj(self, Action: GbxAction, Target: engine.Actor): ...
    def K2_ShowGbxActionScreenLogs(self, bShowLogsOnScreen: bool): ...
    def K2_Resume(self, Action: GbxAction): ...
    def K2_ReplicatedProceedToNextSection(self, Action: GbxAction): ...
    def K2_ReplicatedJumpToNextSection(self, Action: GbxAction): ...
    def K2_ProceedToNextSection(self, Action: GbxAction): ...
    def K2_Pause(self, Action: GbxAction): ...
    def K2_JumpToNextSection(self, Action: GbxAction): ...
    def K2_GetTimeRemaining(self, Target: GbxAction) -> float: ...
    def K2_GetMaxCurrentTime(self, Action: GbxAction) -> float: ...
    def K2_GetActionByClass(
        self, ActionClass: unreal.UClass, Target: engine.Actor
    ) -> GbxAction: ...
    def GetSummary_AnimActionDef(self, AnimActionDef: AnimActionDef) -> str: ...
    def GetKeyedActionClass(
        self, ActionKey: gameplay_tags.GameplayTag, Target: engine.Actor
    ) -> unreal.UClass: ...


class GbxActionComponent(engine.ActorComponent):
    ActionSlots: unreal.WrappedArray[GbxActionSlot]
    EditorKeyedActionList: unreal.WrappedArray[DataActionPair]
    SpawnKeyedActionList: unreal.WrappedArray[DataActionPair_Spawn]
    SpawnMeshKeyedActionList: unreal.WrappedArray[DataActionPair_SpawnMesh]
    SmartObjectKeyedActionList: unreal.WrappedArray[DataActionPair_SmartObject]
    OnActionStarted: Any
    OnActionStopped: Any

    def UpdateActionRemoteServer(self, ActionData: ActionState_Base): ...
    def StopOnRemoteServer(self, ManagerRepId: int, EndState: EGbxActionEndState): ...
    def StopLoopingActionClass(self, ActionClass: unreal.UClass): ...
    def StopActionSlot(self, ActionSlotName: str): ...
    def StopActions(self): ...
    def StopActionClass(self, ActionClass: unreal.UClass): ...
    def PlayOnRemoteServer(
        self, ActionClass: unreal.UClass, ActionData: ActionState_Base
    ): ...
    def OnComponentUnregistered(self, ActorComponent: engine.ActorComponent): ...
    def OnComponentDetached(self, SceneComponent: engine.SceneComponent): ...
    def OnComponentAttached(self, SceneComponent: engine.SceneComponent): ...
    def NotifyInterruptRequest(self): ...
    def K2_Play(self, ActionClass: unreal.UClass) -> GbxAction: ...
    def K2_IsPlayingObj(self, Action: GbxAction) -> bool: ...
    def K2_GetActionBySlot(self, ActionSlotName: str) -> GbxAction: ...
    def K2_GetActionByClass(self, ActionClass: unreal.UClass) -> GbxAction: ...
    def IsPlayingSlot(self, ActionSlotName: str) -> bool: ...
    def IsPlayingClass(self, ActionClass: unreal.UClass) -> bool: ...


class GbxActionDataAsset(gbx_runtime.GbxDataAsset): ...


class GbxActionManager(engine.Actor):
    ActionRepWrapper: ActionStateNet


class GbxAnimBlueprintProfile(gbx_runtime.GbxDataAsset):
    bImportedLegIKSettings: bool
    FootIKTraceUpScale: float
    FootIKTraceDownScale: float
    FootIKOffsetInterpSpeed: float
    FootIKTargetOffset: core_uobject.Vector
    FootIKFootLODThreshold: int
    MeshOffsetCharacterSpeedRange: gbx_runtime.NumericRange
    MeshIKOffsetInterpSpeed: float
    bShouldLimitFootDistanceToMeshOffset: bool
    SlopeAdaptation: core_uobject.Vector
    SlopeAdaptationBone: engine.BoneReference
    MaxSlopeAngle: float
    SlopeNormalMinInterpSpeed: float
    SlopeNormalMaxInterpSpeed: float
    SlopeNormalCharacterSpeedRange: gbx_runtime.NumericRange
    FootIKLODThreshold: int
    FootIKLODInterpolationSpeed: float
    FootIkScreenSizeThreshold: anim_graph_runtime.ScreenSizeSelection
    bUseFootIkScreenSizeThreshold: bool
    FootIkTraceScreenSizeThreshold: anim_graph_runtime.ScreenSizeSelection
    bUseFootIkTraceScreenSizeThreshold: bool
    FootIKReachPrecision: float
    FootIKMaxIterations: int
    FootIKLegsDefinition: unreal.WrappedArray[anim_graph_runtime.AnimLegIKDefinition]
    MinVelocity: float
    MaxVelocity: float
    BoneToModify: engine.BoneReference
    ParentBoneToModify: engine.BoneReference
    ParentLookAxis: int
    BonesToModify: unreal.WrappedArray[gbx_anim_runtime_base.BoneBlendParams]
    EyeBonesToModify: unreal.WrappedArray[gbx_anim_runtime_base.BoneBlendParams]
    LookAtBlinkAngleOverride: float
    bUseLookAtBlinkAngleOverride: bool
    bUseEyeMovement: bool
    EyeShiftMin: core_uobject.Rotator
    EyeShiftMax: core_uobject.Rotator
    EyeGlanceMin: core_uobject.Rotator
    EyeGlanceMax: core_uobject.Rotator
    EyeFocusTimeMin: float
    EyeFocusTimeMax: float
    EyeGlanceTimeMin: float
    EyeGlanceTimeMax: float
    EyeShiftTimeMin: float
    EyeShiftTimeMax: float
    LookAtEyeLODThreshold: int
    LookAtLODThreshold: int
    LookAtLODInterpolationSpeed: float
    LookAtEyeScreenSizeThreshold: anim_graph_runtime.ScreenSizeSelection
    bUseLookAtEyeScreenSizeThreshold: bool
    LookAtScreenSizeThreshold: anim_graph_runtime.ScreenSizeSelection
    bUseLookAtScreenSizeThreshold: bool
    ForwardDynamicsNodeList: unreal.WrappedArray[ForwardDynamicsNodeProfile]
    PhysicsAsset: engine.PhysicsAsset
    TeethOffsetOverride: core_uobject.Vector
    bUseTeethOffsetOverride: bool
    UpperTeethBoneRef: engine.BoneReference
    BoneTagToBoneOverrideNameMap: Any
    bUseUpperTeethBoneRefOverride: bool
    DefaultIdleLoopAnimation: engine.AnimSequence
    SlotName: str

    def RebuildBoneLists(self): ...
    def AnimBlueprintImportFunction(self, ImportType: EAnimBPProfileImport): ...


class GbxAnimStateMachineDefinition(gbx_runtime.GbxDataAsset):
    Name: str
    StateMachines: unreal.WrappedArray[str]
    StateGroups: unreal.WrappedArray[AnimStateGroup]


class GbxAnimStateManager_Falling(engine.GbxAnimStateManager):
    GbxCharAnimInst: GbxCharacterAnimInstance
    GbxCharMoveComponent: GbxCharacterMovementComponent


class GbxAnimStateManager_RootMotion(engine.GbxAnimStateManager):
    GbxCharMoveComponent: GbxCharacterMovementComponent


class GbxAttributeData(gbx_runtime.GbxDataAsset):
    ContextResolver: AttributeContextResolver
    ValueResolver: AttributeValueResolver

    def CanSetBaseValue(self) -> bool: ...
    def CanBindToOnChangedEvent(self) -> bool: ...
    def CanAddModifiers(self) -> bool: ...
    def CanAddAndRemoveModifiers(self) -> bool: ...


class GbxAttributeFunctionLibrary(engine.BlueprintFunctionLibrary):

    def UnbindFromOnAttributeChanged(
        self, BindingHandle: GbxAttributeDelegateBindingHandle
    ): ...
    def UnbindEventFromOnIntegerAttributeChanged(
        self, Attribute: engine.GbxAttributeInteger, Delegate: Any
    ): ...
    def UnbindEventFromOnFloatAttributeChanged(
        self, Attribute: engine.GbxAttributeFloat, Delegate: Any
    ): ...
    def UnbindAllEventsFromOnIntegerAttributeChanged(
        self, Attribute: engine.GbxAttributeInteger
    ): ...
    def UnbindAllEventsFromOnFloatAttributeChanged(
        self, Attribute: engine.GbxAttributeFloat
    ): ...
    def RemoveMultipleAttributeModifiers(
        self, ModifierHandles: unreal.WrappedArray[GbxAttributeModifierHandle]
    ): ...
    def RemoveModifierFromGbxAttribute(
        self,
        Attribute: GbxAttributeData,
        ContextSource: unreal.UObject,
        ModifierHandle: GbxAttributeModifierHandle,
        ModifierActionResult: EGbxAttributeModifierActionExecOutput,
    ): ...
    def RemoveAttributeModifier(
        self, ModifierHandle: GbxAttributeModifierHandle
    ) -> bool: ...
    def RefreshBindingToOnAttributeChangedEvent(
        self,
        BindingHandle: GbxAttributeDelegateBindingHandle,
        ContextSource: unreal.UObject,
    ) -> GbxAttributeDelegateBindingHandle: ...
    def MakeGbxAttributeInteger(self, BaseValue: int) -> engine.GbxAttributeInteger: ...
    def MakeGbxAttributeFloat(self, BaseValue: float) -> engine.GbxAttributeFloat: ...
    def GetValueOfAttributeAsInteger(
        self,
        Attribute: GbxAttributeData,
        ContextSource: unreal.UObject,
        DefaultValue: int,
    ) -> int: ...
    def GetValueOfAttributeAsBoolean(
        self,
        Attribute: GbxAttributeData,
        ContextSource: unreal.UObject,
        DefaultValue: bool,
    ) -> bool: ...
    def GetValueOfAttribute(
        self,
        Attribute: GbxAttributeData,
        ContextSource: unreal.UObject,
        DefaultValue: float,
    ) -> float: ...
    def GetValueFromAttributeDefinedRow(
        self, RowHandle: engine.DataTableRowHandle, ContextSource: unreal.UObject
    ) -> float: ...
    def EvaluateAttributeInitializer(
        self, Initializer: unreal.UClass, ContextSource: unreal.UObject
    ) -> float: ...
    def EvaluateAttributeInitializationData(
        self,
        InitializationData: AttributeInitializationData,
        ContextSource: unreal.UObject,
    ) -> float: ...
    def EqualEqual_GbxAttributeIntegerValue(
        self, A: engine.GbxAttributeInteger, B: int
    ) -> bool: ...
    def EqualEqual_GbxAttributeInteger(
        self, A: engine.GbxAttributeInteger, B: engine.GbxAttributeInteger
    ) -> bool: ...
    def EqualEqual_GbxAttributeFloatValue(
        self, A: engine.GbxAttributeFloat, B: float
    ) -> bool: ...
    def EqualEqual_GbxAttributeFloat(
        self, A: engine.GbxAttributeFloat, B: engine.GbxAttributeFloat
    ) -> bool: ...
    def Conv_GbxAttributeModifierHandleToString(
        self, Attribute: GbxAttributeModifierHandle
    ) -> str: ...
    def Conv_GbxAttributeIntegerToString(
        self, Attribute: engine.GbxAttributeInteger
    ) -> str: ...
    def Conv_GbxAttributeIntegerToInteger(
        self, Attribute: engine.GbxAttributeInteger
    ) -> int: ...
    def Conv_GbxAttributeFloatToString(
        self, Attribute: engine.GbxAttributeFloat
    ) -> str: ...
    def Conv_GbxAttributeFloatToFloat(
        self, Attribute: engine.GbxAttributeFloat
    ) -> float: ...
    def Conv_AttributeInitializationDataToString(
        self, InitData: AttributeInitializationData
    ) -> str: ...
    def BreakGbxAttributeInteger(
        self, Attribute: engine.GbxAttributeInteger, Value: int, BaseValue: int
    ): ...
    def BreakGbxAttributeFloat(
        self, Attribute: engine.GbxAttributeFloat, Value: float, BaseValue: float
    ): ...
    def BindEventToOnIntegerAttributeChanged(
        self, Attribute: engine.GbxAttributeInteger, Delegate: Any
    ): ...
    def BindEventToOnFloatAttributeChanged(
        self, Attribute: engine.GbxAttributeFloat, Delegate: Any
    ): ...
    def BindEventToOnAttributeChanged(
        self, Attribute: GbxAttributeData, ContextSource: unreal.UObject, Delegate: Any
    ) -> GbxAttributeDelegateBindingHandle: ...
    def ApplyMultipleAttributeEffects(
        self,
        Effects: unreal.WrappedArray[AttributeEffectData],
        ModifierValueContext: unreal.UObject,
        AttributeToModifyContextSource: unreal.UObject,
    ) -> unreal.WrappedArray[GbxAttributeModifierHandle]: ...
    def ApplyMultipleAttributeBaseValueData(
        self,
        BaseValueData: unreal.WrappedArray[AttributeBaseValueData],
        AttributeToSetContextSource: unreal.UObject,
        ValueContext: unreal.UObject,
    ): ...
    def ApplyAttributeEffect(
        self,
        Effect: AttributeEffectData,
        ModifierValueContext: unreal.UObject,
        AttributeToModifyContextSource: unreal.UObject,
        ModifierActionResult: EGbxAttributeModifierActionExecOutput,
    ) -> GbxAttributeModifierHandle: ...
    def ApplyAttributeBaseValueData(
        self,
        BaseValueData: AttributeBaseValueData,
        AttributeToSetContextSource: unreal.UObject,
        ValueContext: unreal.UObject,
        ModifierActionResult: EGbxAttributeModifierActionExecOutput,
    ): ...
    def AddModifierToGbxAttribute(
        self,
        Attribute: GbxAttributeData,
        ContextSource: unreal.UObject,
        ModifierType: engine.EGbxAttributeModifierType,
        ModifierValue: float,
        ModifierActionResult: EGbxAttributeModifierActionExecOutput,
    ) -> GbxAttributeModifierHandle: ...


class GbxAttributesComponent(engine.ActorComponent):
    AttributeSets: unreal.WrappedArray[GbxAttributeSet]

    def IsAttributeSetClassUnrelatedToExistingSet(
        self, AttributeSetClass: unreal.UClass
    ) -> bool: ...


class GbxAttributeSet(unreal.UObject):
    ContextResolver: AttributeContextResolver


class GbxAttributeSetBlueprint(engine.Blueprint):
    PropertyToAttributeMapping: unreal.WrappedArray[PropertyToAttributeMapping]


class GbxAttributeSetContextResolver(AttributeContextResolver):
    AttributeSetClass: unreal.UClass


class GbxAttributeSetValueResolver(AttributePropertyValueResolver): ...


class GbxBlackboardKeySelectorExt(engine.BlueprintFunctionLibrary):

    def SetValueAsVector(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
        Value: core_uobject.Vector,
    ): ...
    def SetValueAsTargetActorInfo(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
        Value: TargetActorInfo,
    ): ...
    def SetValueAsString(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
        Value: str,
    ): ...
    def SetValueAsRotator(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
        Value: core_uobject.Rotator,
    ): ...
    def SetValueAsObject(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
        Value: unreal.UObject,
    ): ...
    def SetValueAsName(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
        Value: str,
    ): ...
    def SetValueAsInt(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
        Value: int,
    ): ...
    def SetValueAsFloat(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
        Value: float,
    ): ...
    def SetValueAsFlag(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
        Value: bool,
        Duration: float,
    ): ...
    def SetValueAsEnum(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
        Value: int,
    ): ...
    def SetValueAsClass(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
        Value: unreal.UClass,
    ): ...
    def SetValueAsBool(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
        Value: bool,
    ): ...
    def GetValueAsVector(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
    ) -> core_uobject.Vector: ...
    def GetValueAsTargetActorInfo(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
    ) -> TargetActorInfo: ...
    def GetValueAsString(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
    ) -> str: ...
    def GetValueAsRotator(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
    ) -> core_uobject.Rotator: ...
    def GetValueAsObject(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
    ) -> unreal.UObject: ...
    def GetValueAsName(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
    ) -> str: ...
    def GetValueAsInt(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
    ) -> int: ...
    def GetValueAsFloat(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
    ) -> float: ...
    def GetValueAsEnum(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
    ) -> int: ...
    def GetValueAsClass(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
    ) -> unreal.UClass: ...
    def GetValueAsBool(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
    ) -> bool: ...
    def GetValueAsActor(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
    ) -> engine.Actor: ...
    def GetPropertyDescription(
        self, BBKey: GbxBlackboardKeySelector, Property: core_uobject.Property
    ) -> str: ...
    def ClearValue(
        self,
        Key: GbxBlackboardKeySelector,
        BlackboardComponent: aimodule.BlackboardComponent,
    ): ...


class GbxBoneModifyProfile(gbx_runtime.GbxDataAsset):
    ReferenceAnimation: engine.AnimSequence
    bUseTranslation: bool
    bUseRotation: bool
    bUseScale: bool
    PoseMode: EGbxBoneModifyProfile_PoseMode
    AnimationTime: float
    Bones: unreal.WrappedArray[BoneModifyInfo]
    BoneModStates: unreal.WrappedArray[BoneModifyState]


class GbxCameraShake(engine.CameraShake): ...


class GbxCondition_ActorIsOfClass(gbx_runtime.GbxCondition):
    InputClass: unreal.UClass
    bCheckAbsolute: bool


class GbxCondition_AttackedRecently(gbx_runtime.GbxCondition):
    AttackedWithin: GbxParam


class GbxCondition_Blueprint(gbx_runtime.GbxCondition):

    def EvaluateCondition(
        self, Context: unreal.UObject, OptionalContext: unreal.UObject
    ) -> bool: ...


class GbxCondition_CharacterMass(gbx_runtime.GbxCondition):
    ComparisonTest: EMassComparison
    Mass: MassSelection


class GbxCondition_Comparison(gbx_runtime.GbxCondition):
    OperandA: AttributeInitializationData
    Operator: EConditionComparisonOperatorType
    OperandB: AttributeInitializationData


class GbxCondition_Compound(gbx_runtime.GbxCondition):
    Condition1: gbx_runtime.GbxCondition
    Operator: ECompoundConditionOperatorType
    Condition2: gbx_runtime.GbxCondition


class GbxCondition_Flag(gbx_runtime.GbxCondition):
    FlagEval: GbxFlagEval


class GbxCondition_HasActorTags(gbx_runtime.GbxCondition):
    ActorTagQuery: ActorTagCompositeQuery


class GbxCondition_HasGameplayTags(gbx_runtime.GbxCondition):
    GameplayTags: gameplay_tags.GameplayTagContainer


class GbxCondition_HasInstigatedStatusEffect(gbx_runtime.GbxCondition):
    StatusEffectData: StatusEffectData


class GbxCondition_IsBlackboardTarget(gbx_runtime.GbxCondition): ...


class GbxCondition_IsLowOnHealth(gbx_runtime.GbxCondition):
    LowHealth: float
    bEvaluateOnContextOwner: bool


class GbxCondition_IsPlayerController(gbx_runtime.GbxCondition): ...


class GbxCondition_IsTargetAimedAtMe(gbx_runtime.GbxCondition):
    AngleThreshold: GbxParam


class GbxCondition_IsTrue(gbx_runtime.GbxCondition):
    bIsTrue: bool


class GbxCondition_List(gbx_runtime.GbxCondition):
    Operator: ECompoundConditionOperatorType
    Conditions: unreal.WrappedArray[gbx_runtime.GbxCondition]

    def RequiresNativeClass(self) -> bool: ...
    def GetRequiredInterface(self) -> unreal.UClass: ...


class GbxCondition_SensedRecently(gbx_runtime.GbxCondition):
    SensedWithin: GbxParam
    Senses: unreal.WrappedArray[unreal.UClass]
    bAnyTarget: bool


class GbxCondition_TeamAttitude(gbx_runtime.GbxCondition):
    bHostile: bool
    bNeutral: bool
    bFriendly: bool


class GbxCondition_TeamCheck(gbx_runtime.GbxCondition):
    InputTeam: Team


class GbxCustomizationInterface(core_uobject.Interface): ...


class GbxCustomizationTargetData(gbx_runtime.GbxDataAsset):
    DisplayName: str


class GbxCustomizationTypeData(gbx_runtime.GbxDataAsset):
    CustomizationTypeName: str
    CustomizationTypeDescription: str
    bUnique: bool
    DependentCustomizationType: GbxCustomizationTypeData
    DependentCustomizationTarget: GbxCustomizationTargetData
    AssociatedUnlockStat: Any


class GbxDataTableFunctionLibrary(engine.BlueprintFunctionLibrary):

    def GetDataTableValueFromHandle(
        self,
        ValueHandle: DataTableValueHandle,
        ContextSource: unreal.UObject,
        DefaultValue: float,
    ) -> float: ...
    def GetDataTableValue(
        self,
        Table: engine.DataTable,
        RowName: str,
        ValueName: str,
        ValueInStructType: core_uobject.ScriptStruct,
        OutValue: int,
    ) -> bool: ...
    def Conv_DataTableValueHandleToString(
        self, ValueHandle: DataTableValueHandle
    ) -> str: ...


class GbxEnvQueryHotSpotProviderInterface(core_uobject.Interface): ...


class GbxEqsRenderingComponent(aimodule.EQSRenderingComponent):
    bExecuteQuery: bool
    TraceDrawMode: aimodule.EEqsTraceDrawMode
    ExternalQueryParams: str
    EnvQueryParams: EnvQueryParams

    def GetAvailableEnvQueryParamRefNames(self, Names: unreal.WrappedArray[str]): ...


class GbxEventDelegateBinding(engine.DynamicBlueprintBinding):
    DelegateBindings: unreal.WrappedArray[GbxBlueprintlegateBinding]


class GbxFeedbackBase(gbx_runtime.GbxDataAsset):

    def StopGbxFeedback(
        self,
        FeedbackData: GbxFeedbackBase,
        WorldContextObject: unreal.UObject,
        Controller: GbxPlayerController,
    ): ...
    def PlayGbxFeedbackData3D(
        self,
        FeedbackData: GbxFeedbackBase,
        WorldContextObject: unreal.UObject,
        Controller: GbxPlayerController,
        SourceLocation: core_uobject.Vector,
        bLoop: bool,
        bIgnoreController: bool,
        Scale: float,
        SourceContext: unreal.UObject,
        EffectFalloffMinDistance: float,
        EffectFalloffMaxDistance: float,
    ): ...
    def PlayGbxFeedbackData2D(
        self,
        FeedbackData: GbxFeedbackBase,
        WorldContextObject: unreal.UObject,
        Controller: GbxPlayerController,
        bLoop: bool,
        bIgnoreController: bool,
        Scale: float,
        SourceContext: unreal.UObject,
    ): ...


class GbxFeedbackData(GbxFeedbackBase):
    FeedbackType: int
    ControllerRumbleDetails: unreal.WrappedArray[engine.ForceFeedbackChannelDetails]
    ExternalControllerRumbleDetails: unreal.WrappedArray[engine.ForceFeedbackEffect]
    MinControllerRumbleDetails: unreal.WrappedArray[engine.ForceFeedbackChannelDetails]
    MinExternalControllerRumbleDetails: unreal.WrappedArray[engine.ForceFeedbackEffect]
    bAbsoluteControllerRumbleScale: bool
    CameraShakeBase: unreal.UClass
    CameraShakeDirectionalY: unreal.UClass
    RandomShakeInterval: float
    MaxRandomShakeScalar: float
    MinRandomShakeScalar: float
    bUnique: bool
    bUseContinuousAttributeScale: bool
    ContinuousScale: AttributeInitializationData
    ContinuousScaleCurve: engine.RuntimeFloatCurve
    bScaleDownOverTime: bool
    bUseScaleOverTimeCurve: bool
    ScaleOverTimeCurve: engine.RuntimeFloatCurve
    bPlayRadialBlur: bool
    RadialBlurInfo: engine.RadialBlurSelection
    bOverrideRadialBlurCenter: bool
    bUseContextAsWorldSpaceCenter: bool
    RadialBlurWorldSpaceCenter: core_uobject.Vector
    RadialBlurMaxDistance: float
    ScreenParticles: engine.ParticleSystem
    bHideWhenFinished: bool
    ContentDims: core_uobject.Vector2D
    ParticleDepth: float
    ScalingMode: EScreenParticleScalingMode
    bOnlyOwnerSee: bool
    bAlwaysVisible: bool
    bTickParticleEvenWhenPaused: bool
    bLetSystemFinishAfterStopping: bool


class GbxFeedbackList(GbxFeedbackBase):
    FeedbackList: unreal.WrappedArray[GbxFeedbackData]


class GbxFeedbackManager(unreal.UObject): ...


class GbxFlagData(gbx_runtime.GbxDataAsset):
    Condition: gbx_runtime.GbxCondition
    ContextResolver: AttributeContextResolver
    ValueResolver: GbxFlagValueResolver


class GbxFlagFunctionLibrary(engine.BlueprintFunctionLibrary):

    def SetFlagValue(
        self, WorldContextObject: unreal.UObject, Flag: GbxFlag, bNewValue: bool
    ): ...
    def SetFlagTrueTimed(
        self, WorldContextObject: unreal.UObject, Flag: GbxFlag, Duration: float
    ): ...
    def SetFlagDataValue(
        self,
        WorldContextObject: unreal.UObject,
        FlagData: GbxFlagData,
        ContextSource: unreal.UObject,
        bNewValue: bool,
    ): ...
    def SetFlagDataTrueTimed(
        self,
        WorldContextObject: unreal.UObject,
        FlagData: GbxFlagData,
        ContextSource: unreal.UObject,
        Duration: float,
    ): ...
    def GetFlagValue(
        self, WorldContextObject: unreal.UObject, Flag: GbxFlag
    ) -> bool: ...
    def GetFlagDataValue(
        self,
        WorldContextObject: unreal.UObject,
        FlagData: GbxFlagData,
        ContextSource: unreal.UObject,
    ) -> bool: ...
    def FlagTrueWithin(
        self, WorldContextObject: unreal.UObject, Flag: GbxFlag, CheckTime: float
    ) -> bool: ...
    def FlagTrueFor(
        self, WorldContextObject: unreal.UObject, Flag: GbxFlag, CheckTime: float
    ) -> bool: ...
    def FlagFalseWithin(
        self, WorldContextObject: unreal.UObject, Flag: GbxFlag, CheckTime: float
    ) -> bool: ...
    def FlagFalseFor(
        self, WorldContextObject: unreal.UObject, Flag: GbxFlag, CheckTime: float
    ) -> bool: ...
    def FlagDataTrueWithin(
        self,
        WorldContextObject: unreal.UObject,
        FlagData: GbxFlagData,
        ContextSource: unreal.UObject,
        CheckTime: float,
    ) -> bool: ...
    def FlagDataTrueFor(
        self,
        WorldContextObject: unreal.UObject,
        FlagData: GbxFlagData,
        ContextSource: unreal.UObject,
        CheckTime: float,
    ) -> bool: ...
    def FlagDataFalseWithin(
        self,
        WorldContextObject: unreal.UObject,
        FlagData: GbxFlagData,
        ContextSource: unreal.UObject,
        CheckTime: float,
    ) -> bool: ...
    def FlagDataFalseFor(
        self,
        WorldContextObject: unreal.UObject,
        FlagData: GbxFlagData,
        ContextSource: unreal.UObject,
        CheckTime: float,
    ) -> bool: ...


class FlagPropertyTestContext(unreal.UObject):
    TestFlag: GbxFlag
    TestStruct: FlagPropertyTestStruct


class FlagPropertyTestContextResolver(AttributeContextResolver): ...


class GbxFlagValueResolver(unreal.UObject): ...


class GbxFlagValueResolver_Property(GbxFlagValueResolver):
    Property: engine.ParsedProperty


class BaseMenuStackMenuInfo(unreal.UObject): ...


class GbxGameplayStatics(engine.GameplayStatics):

    def SetTeamCollisionResponseWith(
        self, Actor: engine.Actor, TeamActor: engine.Actor, bIgnore: bool
    ): ...
    def SetTeamCollisionResponseToChannel(
        self, Actor: engine.Actor, Channel: ETeamCollisionChannel, bIgnore: bool
    ): ...
    def SetTeamCollisionChannelFrom(
        self, Actor: engine.Actor, TeamActor: engine.Actor, bOn: bool
    ): ...
    def SetTeamCollisionChannel(
        self, Actor: engine.Actor, Channel: ETeamCollisionChannel, bOn: bool
    ): ...
    def SetPlayerMaster(
        self, AIActor: engine.Actor, PlayerMaster: engine.Actor
    ) -> bool: ...
    def SetComponentTeamCollisionResponseWith(
        self,
        Component: engine.SceneComponent,
        TeamActor: engine.Actor,
        bIgnore: bool,
        bPropagateToChildren: bool,
    ): ...
    def SetComponentTeamCollisionResponseToChannel(
        self,
        Component: engine.SceneComponent,
        Channel: ETeamCollisionChannel,
        bIgnore: bool,
        bPropagateToChildren: bool,
    ): ...
    def SetComponentTeamCollisionChannel(
        self,
        Component: engine.SceneComponent,
        Channel: ETeamCollisionChannel,
        bOn: bool,
        bPropagateToChildren: bool,
    ): ...
    def ProjectFromQueryToSimulation(
        self,
        Component: GbxSkeletalMeshComponent,
        BodyName: str,
        InOutHitPoint: core_uobject.Vector,
        InOutHitNormal: core_uobject.Vector,
    ): ...
    def GetPrimaryPlayerController(
        self, WorldContextObject: unreal.UObject
    ) -> engine.PlayerController: ...
    def GetAssociatedPrimaryCharacter(self, Actor: engine.Actor) -> GbxCharacter: ...
    def AlignTransformToSurface(
        self, Transform: core_uobject.Transform, SurfaceNormal: core_uobject.Vector
    ) -> core_uobject.Transform: ...


class GbxGameStatsBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def UpdateStatForParty(
        self, WorldContextObject: unreal.UObject, StatData: GameStatData, NewValue: int
    ): ...
    def UpdateStat(
        self, ContextActor: engine.Actor, StatData: GameStatData, NewValue: int
    ): ...
    def IncrementStatForParty(
        self, WorldContextObject: unreal.UObject, StatData: GameStatData, Amount: int
    ): ...
    def IncrementStat(
        self, ContextActor: engine.Actor, StatData: GameStatData, Amount: int
    ): ...
    def GetStatValue(
        self, ContextActor: engine.Actor, StatData: GameStatData
    ) -> int: ...
    def DecrementStatForParty(
        self, WorldContextObject: unreal.UObject, StatData: GameStatData, Amount: int
    ): ...
    def DecrementStat(
        self, ContextActor: engine.Actor, StatData: GameStatData, Amount: int
    ): ...


class GbxGameSystemCoreBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def SetComponentPhysicalRotation(
        self,
        Target: engine.PrimitiveComponent,
        PitchRotation: float,
        YawRotation: float,
        RollRotation: float,
        BoneName: str,
    ): ...
    def ResourceUnlockTurns(self, Actor: engine.Actor, Reason: str): ...
    def ResourceUnlockTickAndRefreshBones(self, Actor: engine.Actor, Reason: str): ...
    def ResourceUnlockRotation(self, Actor: engine.Actor, Reason: str): ...
    def ResourceUnlockMovement(self, Actor: engine.Actor, Reason: str): ...
    def ResourceUnlockMomentum(self, Actor: engine.Actor, Reason: str): ...
    def ResourceUnlockMantling(self, Actor: engine.Actor, Reason: str): ...
    def ResourceUnlockLookAtTargetLocation(self, Actor: engine.Actor, Reason: str): ...
    def ResourceUnlockLookAt(self, Actor: engine.Actor, Reason: str): ...
    def ResourceUnlockJumping(self, Actor: engine.Actor, Reason: str): ...
    def ResourceUnlockHandIk(self, Actor: engine.Actor, Reason: str): ...
    def ResourceUnlockGod(self, Actor: engine.Actor, Reason: str): ...
    def ResourceUnlockFootIkTracing(self, Actor: engine.Actor, Reason: str): ...
    def ResourceUnlockFootIk(self, Actor: engine.Actor, Reason: str): ...
    def ResourceUnlockDodging(self, Actor: engine.Actor, Reason: str): ...
    def ResourceUnlockDemigod(self, Actor: engine.Actor, Reason: str): ...
    def ResourceUnlockCrouching(self, Actor: engine.Actor, Reason: str): ...
    def ResourceUnlockAIThinking(self, Actor: engine.Actor, Reason: str): ...
    def ResourceUnlockAiming(self, Actor: engine.Actor, Reason: str): ...
    def ResourceLockTurns(self, Actor: engine.Actor, Reason: str): ...
    def ResourceLockTickAndRefreshBones(self, Actor: engine.Actor, Reason: str): ...
    def ResourceLockTargetable(
        self, Actor: engine.Actor, Reason: str, bTargetable: bool
    ): ...
    def ResourceLockRotation(self, Actor: engine.Actor, Reason: str): ...
    def ResourceLockPhysicsRotation(self, Actor: engine.Actor, Reason: str): ...
    def ResourceLockMovement(self, Actor: engine.Actor, Reason: str): ...
    def ResourceLockMomentum(self, Actor: engine.Actor, Reason: str): ...
    def ResourceLockMantling(self, Actor: engine.Actor, Reason: str): ...
    def ResourceLockLookAtTargetLocation(self, Actor: engine.Actor, Reason: str): ...
    def ResourceLockLookAt(self, Actor: engine.Actor, Reason: str): ...
    def ResourceLockJumping(self, Actor: engine.Actor, Reason: str): ...
    def ResourceLockHandIk(self, Actor: engine.Actor, Reason: str): ...
    def ResourceLockGod(self, Actor: engine.Actor, Reason: str): ...
    def ResourceLockFootIkTracing(self, Actor: engine.Actor, Reason: str): ...
    def ResourceLockFootIk(self, Actor: engine.Actor, Reason: str): ...
    def ResourceLockDodging(self, Actor: engine.Actor, Reason: str): ...
    def ResourceLockDemigod(self, Actor: engine.Actor, Reason: str): ...
    def ResourceLockCrouching(self, Actor: engine.Actor, Reason: str): ...
    def ResourceLockAIThinking(
        self, Actor: engine.Actor, Reason: str, bAbort: bool
    ): ...
    def ResourceLockAiming(self, Actor: engine.Actor, Reason: str): ...
    def IsSplitScreen(self, GameInstance: engine.GameInstance) -> bool: ...
    def IsPlayer(self, Actor: engine.Actor) -> bool: ...
    def IsContentCensored(self, WorldContextObject: unreal.UObject) -> bool: ...
    def HoverComponentAtActor(
        self,
        Component: engine.SceneComponent,
        TargetActor: engine.Actor,
        Altitude: float,
        Radius: float,
        AccelerationTime: float,
        Speed: float,
        Duration: float,
        LatentInfo: engine.LatentActionInfo,
    ): ...
    def GetRelativeDirection(
        self,
        RelativeDirectionData: RelativeDirectionData,
        DefaultDirection: core_uobject.Vector,
        SourceActor: engine.Actor,
        SourceSocketName: str,
        TargetActor: engine.Actor,
    ) -> core_uobject.Vector: ...
    def GetCurveFloatValue(
        self, Curve: engine.RuntimeFloatCurve, InTime: float
    ) -> float: ...
    def GetAreAnyPlayersOverlappingActors(
        self,
        WorldContextObject: unreal.UObject,
        Actors: unreal.WrappedArray[engine.Actor],
    ) -> bool: ...
    def GetAreAnyPlayersOverlappingActor(
        self, WorldContextObject: unreal.UObject, Actor: engine.Actor
    ) -> bool: ...
    def GetAreAllPlayersOverlappingActors(
        self,
        WorldContextObject: unreal.UObject,
        Actors: unreal.WrappedArray[engine.Actor],
    ) -> bool: ...
    def GetAreAllPlayersOverlappingActor(
        self, WorldContextObject: unreal.UObject, Actor: engine.Actor
    ) -> bool: ...
    def GetActorListTrimmedToBestCluster(
        self,
        OutputActors: unreal.WrappedArray[engine.Actor],
        ClusterMidpoint: core_uobject.Vector,
        InputActors: unreal.WrappedArray[engine.Actor],
        SourceActor: engine.Actor,
        ClusterRadius: float,
        bPreferClusterContainingCurrentTarget: bool,
    ): ...
    def BranchOnIsPlayer(self, Actor: engine.Actor, Branches: EIsPlayerExecOutput): ...
    def BranchOnIsAutonomous(
        self, Actor: engine.Actor, Branches: EIsAutonomousOuput
    ): ...
    def AreAnyPlayersOverlappingActors(
        self,
        WorldContextObject: unreal.UObject,
        Actors: unreal.WrappedArray[engine.Actor],
        Branches: EPlayersOverlappingActorOutput,
    ): ...
    def AreAnyPlayersOverlappingActor(
        self,
        WorldContextObject: unreal.UObject,
        Actor: engine.Actor,
        Branches: EPlayersOverlappingActorOutput,
    ): ...
    def AreAnyPlayersInVolume(
        self,
        WorldContextObject: unreal.UObject,
        Volumes: unreal.WrappedArray[engine.Volume],
        Branches: EPlayersInVolumeOutput,
    ): ...
    def AreAllPlayersOverlappingActors(
        self,
        WorldContextObject: unreal.UObject,
        Actors: unreal.WrappedArray[engine.Actor],
        Branches: EPlayersOverlappingActorOutput,
    ): ...
    def AreAllPlayersOverlappingActor(
        self,
        WorldContextObject: unreal.UObject,
        Actor: engine.Actor,
        Branches: EPlayersOverlappingActorOutput,
    ): ...
    def AreAllPlayersInVolume(
        self,
        WorldContextObject: unreal.UObject,
        Volumes: unreal.WrappedArray[engine.Volume],
        Branches: EPlayersInVolumeOutput,
    ): ...


class GbxHUDFeedbackData(gbx_runtime.GbxDataAsset):
    MoveWeight: core_uobject.Vector
    MoveAcceleration: core_uobject.Vector
    MoveDeceleration: core_uobject.Vector
    MoveMaxVelocity: core_uobject.Vector
    LookWeight: core_uobject.Vector2D
    LookAcceleration: core_uobject.Vector2D
    LookDeceleration: core_uobject.Vector2D
    LookMaxVelocity: core_uobject.Vector2D
    GamepadLookMultiplier: float


class GbxInventoryCategoryData(gbx_runtime.GbxDataAsset):
    bIsPremiumCurrencyCategory: bool


class GbxLevelSequenceControllableInterface(core_uobject.Interface): ...


class GbxMediaData(gbx_runtime.GbxDataAsset):
    AudioSinkProvider: Any
    MediaTexture: media_assets.MediaTexture
    MediaSource: media_assets.MediaSource


class GbxMediaManager(engine.GbxBaseMediaManager):
    ActiveMediaPlayers: unreal.WrappedArray[media_assets.MediaPlayer]

    def OnMovieMediaOpenFailed(self, DeviceUrl: str): ...
    def OnMovieMediaClosed(self): ...
    def OnMovieEndReached(self): ...
    def GbxPlayMovie(
        self, WorldContextObject: unreal.UObject, InMediaData: GbxMediaData
    ) -> media_assets.MediaPlayer: ...


class GbxNavAvoidanceInterface(core_uobject.Interface):

    def SetObstacleAvoidanceLock(self, bDisable: bool, Reason: str): ...


class GbxPainCausingVolume(engine.PainCausingVolume):
    GbxDamagePerSec: AttributeInitializationData


class GbxParamExt(engine.BlueprintFunctionLibrary):

    def IsValueInRangePure(
        self, Param: GbxParam, Value: float, Context: unreal.UObject
    ) -> bool: ...
    def IsValueInRange(
        self, Param: GbxParam, Value: float, Context: unreal.UObject
    ) -> bool: ...
    def GetParamPropertyDescription(
        self, Param: GbxParam, Property: core_uobject.Property
    ) -> str: ...
    def GetParamDescriptionText(self, Param: GbxParam) -> str: ...
    def GetParamDescription(self, Param: GbxParam) -> str: ...
    def GetNamedParamDescriptionText(self, Param: GbxNamedParam) -> str: ...
    def GetNamedParamDescription(self, Param: GbxNamedParam) -> str: ...
    def EvaluatePure(self, Param: GbxParam, Context: unreal.UObject) -> float: ...
    def EvaluateIntPure(self, Param: GbxParam, Context: unreal.UObject) -> float: ...
    def EvaluateInt(self, Param: GbxParam, Context: unreal.UObject) -> float: ...
    def EvaluateBoolPure(self, Param: GbxParam, Context: unreal.UObject) -> bool: ...
    def EvaluateBool(self, Param: GbxParam, Context: unreal.UObject) -> bool: ...
    def Evaluate(self, Param: GbxParam, Context: unreal.UObject) -> float: ...


class GbxPerceptionComponent(aimodule.AIPerceptionComponent):
    StimulusStrengthOverrideTime: float


class GbxPhysicsCollisionHandler(engine.PhysicsCollisionHandler): ...


class GbxPhysicsSettings(unreal.UObject):
    SurfaceTypeInfoMap: Any
    RigidBodyImpactSettings: RigidBodyImpactSettings
    ForceSmoothing: DestructionForceSmoothing
    LowDamageThreshold: float
    MediumDamageThreshold: float
    HighDamageThreshold: float
    RagdollWeaponForceFeatherPercent: float

    def StaticSetRigidBodySimulationInteractability(
        self, Comp: engine.SkeletalMeshComponent, bAesthetic: bool, BodyName: str
    ): ...


class GbxQueryManager(unreal.UObject):
    MaxActiveQueries: int
    Queries: unreal.WrappedArray[GbxQuery]
    World: engine.World
    EnvQueryManager: aimodule.EnvQueryManager

    def NotifyAIHotSpotListChangedFor(self, OwnerActor: engine.Actor): ...


class GbxSignificanceSettings(engine.DeveloperSettings):
    Events: Any

    def EnumerateSignificanceEvents(self, OutEvents: unreal.WrappedArray[str]): ...


class GbxSimpleMotionLibrary(engine.BlueprintFunctionLibrary):

    def UpdateVectorMotion(
        self,
        DeltaTime: float,
        CurrentValue: core_uobject.Vector,
        ControlValue: float,
        Data: SimpleMotionState,
        SpeedScale: float,
        TargetValue: core_uobject.Vector,
        State: SimpleMotionInstanceState,
    ): ...
    def UpdateRotatorMotion(
        self,
        DeltaTime: float,
        CurrentValue: core_uobject.Rotator,
        ControlValue: float,
        Data: SimpleMotionState,
        SpeedScale: float,
        TargetValue: core_uobject.Rotator,
        bShortestRotation: bool,
        State: SimpleMotionInstanceState,
    ): ...
    def UpdateFloatMotion(
        self,
        DeltaTime: float,
        CurrentValue: float,
        ControlValue: float,
        Data: SimpleMotionState,
        SpeedScale: float,
        TargetValue: float,
        State: SimpleMotionInstanceState,
    ): ...
    def TeleportVectorMotion(
        self,
        CurrentValue: core_uobject.Vector,
        ControlValue: float,
        Data: SimpleMotionState,
        SpeedScale: float,
        TargetValue: core_uobject.Vector,
        State: SimpleMotionInstanceState,
    ): ...
    def TeleportRotatorMotion(
        self,
        CurrentValue: core_uobject.Rotator,
        ControlValue: float,
        Data: SimpleMotionState,
        SpeedScale: float,
        TargetValue: core_uobject.Rotator,
        State: SimpleMotionInstanceState,
    ): ...
    def TeleportFloatMotion(
        self,
        CurrentValue: float,
        ControlValue: float,
        Data: SimpleMotionState,
        SpeedScale: float,
        TargetValue: float,
        State: SimpleMotionInstanceState,
    ): ...
    def ResetMotionState(self, State: SimpleMotionInstanceState): ...


class GbxSkeletalMeshActor(engine.SkeletalMeshActor): ...


class GbxStaticMeshComponent(engine.StaticMeshComponent):
    CustomizationTargets: unreal.WrappedArray[GbxCustomizationTargetData]


class GbxSubtitleManagerInterface(core_uobject.Interface): ...


class GbxThreatSystemInterface(core_uobject.Interface): ...


class GbxUIFormattableParameter(core_uobject.Interface): ...


class GbxUIName(gbx_runtime.GbxDataAsset):
    DisplayName: str

    def GetFormattedText(self) -> str: ...


class GestaltPartData(gbx_runtime.GbxDataAsset): ...


class GestaltPartData_Mesh(GestaltPartData):
    GestaltData: engine.GestaltData
    GestaltMeshPartName: str
    AdditionalGestaltMeshPartNames: unreal.WrappedArray[str]
    ChildParts: unreal.WrappedArray[GestaltChildPartData]
    FoleyAudioAccessory: GestaltPartFoleyAccessory

    def EnumerateGestaltMeshPartNames(
        self, OutPartNameList: unreal.WrappedArray[str]
    ): ...


class GestaltPartData_Random(GestaltPartData):
    RandomParts: unreal.WrappedArray[GestaltRandomPartData]


class GestaltPartListData(gbx_runtime.GbxDataAsset):
    RequiredParts: unreal.WrappedArray[GestaltPartData]
    OptionalParts: unreal.WrappedArray[GesaltOptionalPartData]
    SpecialParts: unreal.WrappedArray[GestaltPartData]


class GlobalBoneModifyProfileState(engine.DataAsset):
    DefaultTransform: BMPOverride
    SkeletonOverrides: Any
    CharacterOverrides: Any
    SkeletonExceptions: Any
    CharacterExceptions: Any


class GlobalBoneModifyProfile(unreal.UObject):
    GlobalProfileSet: Any


class GlobalBoneModBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def K2_SetGBMP(self, State: GlobalBoneModifyProfileState, bEnabled: bool): ...


class GravityOverrideVolume(engine.PhysicsVolume):
    GravityZ: float
    bEnableTeamGravity: bool
    OverrideTeamGravity: int


class HealthResourcePoolModifierAttributeValueResolver(AttributeValueResolver):
    HealthResourcePool: GameResourcePoolData


class HealthTypeData(gbx_runtime.GbxDataAsset):
    DisplayColor: core_uobject.LinearColor
    BarBackgroundFrameName: str
    BalanceData: engine.DataTableRowHandle
    PhysMat: engine.PhysicalMaterial
    NoDamagePhysMat: engine.PhysicalMaterial
    HealthTypeModifierAttribute: GbxAttributeData


class HitReactionBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def SetHitReactionData(
        self, Actor: engine.Actor, HitReactionData: HitReactionData
    ): ...
    def ScriptHitReaction(
        self,
        Actor: engine.Actor,
        Causer: engine.Actor,
        Tag: HitReactionTag,
        LocalHitDirection: core_uobject.Vector,
        BoneName: str,
        Force: ForceSelection,
    ): ...
    def ScriptDeath(
        self,
        Actor: engine.Actor,
        Causer: engine.Actor,
        Tag: HitReactionTag,
        LocalHitDirection: core_uobject.Vector,
        BoneName: str,
        Force: ForceSelection,
    ): ...
    def ResourceUnlockHitReactions(self, Actor: engine.Actor, Reason: str): ...
    def ResourceLockHitReactions(self, Actor: engine.Actor, Reason: str): ...
    def RemoveHitReactionLiveLayer(self, Actor: engine.Actor, Layer: unreal.UClass): ...
    def RemoveHitReactionDeathLayer(
        self, Actor: engine.Actor, Layer: unreal.UClass
    ): ...
    def K2_GetHitLocationFromAction(self, Action: GbxAction) -> core_uobject.Vector: ...
    def K2_GetHitDirectionFromAction(
        self, Action: GbxAction, bLocalSpace: bool
    ) -> core_uobject.Vector: ...
    def K2_GetHitCauserFromAction(self, Action: GbxAction) -> unreal.UObject: ...
    def K2_GetHealthPercentFromAction(self, Action: GbxAction) -> float: ...
    def K2_GetForceFromAction(self, Action: GbxAction) -> float: ...
    def K2_GetBoneIndexFromAction(self, Action: GbxAction) -> int: ...
    def IsHitReactionTagActive(
        self, Actor: engine.Actor, Tag: HitReactionTag
    ) -> bool: ...
    def AddHitReactionLiveLayer(self, Actor: engine.Actor, Layer: unreal.UClass): ...
    def AddHitReactionDeathLayer(self, Actor: engine.Actor, Layer: unreal.UClass): ...


class HitReactionData(gbx_runtime.GbxDataAsset):
    LiveLayers: unreal.WrappedArray[unreal.UClass]
    DeathLayers: unreal.WrappedArray[unreal.UClass]
    HitReactions: unreal.WrappedArray[HitReactionPair]


class HitReactionLayer_Blueprint(HitReactionLayer):

    def EvaluateTag(
        self,
        Receiver: DamageComponent,
        Causer: DamageCauserComponent,
        DamageAmount: float,
        DamageType: GbxDamageType,
        DamageSource: DamageSource,
        HitRegion: HitRegionData,
        Force: float,
        PreviousTag: HitReactionTag,
    ) -> HitReactionTag: ...


class HitReactionLayer_Combine(HitReactionLayer):
    SubLayers: unreal.WrappedArray[unreal.UClass]
    PriorityList: unreal.WrappedArray[HitReactionTag]
    bMissingTagsAreHighestPriority: bool


class HitReactionLayer_Condition(HitReactionLayer):
    Conditions: unreal.WrappedArray[HitReactionCondition]
    Combine: EHitReactionConditionCombine
    SubLayer: unreal.UClass


class HitReactionLayer_Cooldown(HitReactionLayer):
    DefaultCooldown: float
    Cooldowns: unreal.WrappedArray[HitReactionCooldownData]


class HitReactionLayer_Map(HitReactionLayer):
    TagMap: unreal.WrappedArray[HitReactionMapItem]


class HitReactionLayer_Priority(HitReactionLayer):
    PriorityList: unreal.WrappedArray[HitReactionTag]
    CanInterruptSelf: unreal.WrappedArray[HitReactionTag]


class HitReactionTag(gbx_runtime.GbxDataAsset):
    SoundTag: gbx_audio.CharacterSoundTag
    CensoredTag: HitReactionTag


class HitRegionFunctionLibrary(engine.BlueprintFunctionLibrary):

    def ResetHitRegionHealth(
        self,
        Actor: engine.Actor,
        HitRegion: HitRegionData,
        AssociatedComponent: engine.PrimitiveComponent,
    ): ...
    def ResetAllHitRegionHealth(self, Actor: engine.Actor): ...
    def RefillHitRegionHealthByPercent(
        self,
        RefillPercent: float,
        Actor: engine.Actor,
        HitRegion: HitRegionData,
        AssociatedComponent: engine.PrimitiveComponent,
    ): ...
    def RefillHitRegionHealthByAmount(
        self,
        RefillAmount: float,
        Actor: engine.Actor,
        HitRegion: HitRegionData,
        AssociatedComponent: engine.PrimitiveComponent,
    ): ...
    def AssociateComponentWithHitRegion(
        self,
        Actor: engine.Actor,
        ComponentToAssociate: engine.PrimitiveComponent,
        HitRegion: HitRegionData,
    ): ...


class IGbxProjectileManager(unreal.UObject): ...


class GbxReplicatorProxyData(core_uobject.Interface): ...


class InspectionInfoProvider(core_uobject.Interface):

    def GetInspectionInfo(self, InspectionInfo: InspectionInfo): ...


class ImpactData(gbx_runtime.GbxDataAsset):
    ParentImpact: ImpactData
    Usage: EImpactUsage
    bOverrideParentUnconditionalResponse: bool
    UnconditionalResponse: ImpactResponseEffect
    bOverrideParentDefaultResponse: bool
    DefaultResponse: ImpactResponseEffect
    ImpactResponses: unreal.WrappedArray[ImpactResponseInfo]
    DefaultImpactWwiseEvent: wwise_audio.WwiseEvent
    TriggerInfo: ImpactTriggerInfo
    DefaultSignificanceEvent: GbxSignificanceEvent
    LayeredPhysicalResponseQuality: int
    LayeredParentPhysicalResponseQuality: int
    bOverrideParentProximityThrottling: bool
    bEnableProximityThrottling: bool
    FrameLimit: int
    bUseMassWwiseParameter: bool


class ImpactExpansionData(gbx_runtime.GbxDataAsset):
    ImpactDataToExpand: ImpactData
    ImpactResponses: unreal.WrappedArray[ImpactResponseInfo]


class ImpactDataOverride(core_uobject.Interface): ...


class ImpactDecalManager(engine.Actor): ...


class PooledImpactDecalComponent(engine.DecalComponent): ...


class ImpactEffectFunctionLibrary(engine.BlueprintFunctionLibrary):

    def PlayTraceImpactAndGetParticleSystemComponents(
        self,
        ImpactData: ImpactData,
        Instigator: engine.Actor,
        TraceStart: core_uobject.Vector,
        TraceEnd: core_uobject.Vector,
        SpawnedParticleSystemComponents: unreal.WrappedArray[
            engine.ParticleSystemComponent
        ],
        TraceChannel: int,
    ): ...
    def PlayTraceImpact(
        self,
        ImpactData: ImpactData,
        Instigator: engine.Actor,
        TraceStart: core_uobject.Vector,
        TraceEnd: core_uobject.Vector,
        TraceChannel: int,
        bReplicated: bool,
    ): ...
    def PlayHitResultImpactGetParticleSystemComponents(
        self,
        ImpactData: ImpactData,
        Instigator: engine.Actor,
        HitInfo: engine.HitResult,
        SpawnedParticleSystemComponents: unreal.WrappedArray[
            engine.ParticleSystemComponent
        ],
    ): ...
    def PlayHitResultImpact(
        self,
        ImpactData: ImpactData,
        Instigator: engine.Actor,
        HitInfo: engine.HitResult,
        bReplicated: bool,
    ): ...


class ImpactFXManagerComponent(engine.ActorComponent):
    bScaleImpactDecalEffects: bool
    BounceEffect: ImpactData
    BounceEffectThreshold: float
    BounceEffectFrequency: float
    bAlignBounceEffectToVelocity: bool
    SlideEffect: ImpactData
    SlideEffectThreshold: float
    SlideEffectStopThreshold: float
    SlideEffectFrequency: float
    StartSlideEffectDelay: float
    bOverrideSlideEffectOrigin: bool
    SlideEffectOriginSocket: str
    bEffectsEnabled: bool
    bAutoEnableCollisionNotifications: bool
    ActiveSlideEffects: unreal.WrappedArray[ImpactFXManagerTrackingData]

    def SetEffectsEnabled(self, bEnabled: bool): ...
    def OnTrackedParticleSystemFinished(self, PSC: engine.ParticleSystemComponent): ...
    def OnTrackedComponentDeactivated(self, Component: engine.ActorComponent): ...
    def OnHit(
        self,
        SelfActor: engine.Actor,
        OtherActor: engine.Actor,
        NormalImpulse: core_uobject.Vector,
        Hit: engine.HitResult,
    ): ...


class InspectionInfoFunctionLibrary(engine.BlueprintFunctionLibrary):

    def AddScreenOutput(
        self,
        InspectionInfo: InspectionInfo,
        String: str,
        Verbosity: EDebugDisplayVerbosityLevel,
    ): ...
    def AddAboveActorOutput(
        self,
        InspectionInfo: InspectionInfo,
        String: str,
        Verbosity: EDebugDisplayVerbosityLevel,
    ): ...


class InterpComponent(engine.ActorComponent):
    bRemoveOnCompletion: bool
    bUpdateVelocity: bool
    bClearVelocity: bool
    bManualTick: bool
    bInterpYawOnly: bool
    bBallistics: bool
    bMatchRotationToVelocity: bool
    bSetToInitialWhenFinished: bool
    bRelative: bool
    InterpActor: engine.Actor
    InterpController: engine.Controller
    InterpMoveComp: engine.PawnMovementComponent
    InterpLocMode: EInterpMode
    InterpLocTime: float
    InterpLocElapsedTime: float
    InterpLocDiff: core_uobject.Vector
    InterpLocPrev: core_uobject.Vector
    InterpRotMode: EInterpMode
    InterpRotTime: float
    InterpRotElapsedTime: float
    InterpRotDiff: core_uobject.Rotator
    InterpRotPrev: core_uobject.Rotator
    InitialRotation: core_uobject.Rotator
    BallisticsStartLoc: core_uobject.Vector
    BallisticsStartVelocity: core_uobject.Vector
    BallisticsGravity: float
    BallisticsStartTime: float
    BallisticsTotalTime: float

    def Stop(self): ...
    def SetUpdateVelocity(self, bNewUpdateVelocity: bool): ...
    def SetRemoveOnCompletion(self, bRemove: bool): ...
    def SetManualTick(self, bManual: bool): ...
    def SetClearVelocity(self, bNewClearVelocity: bool): ...
    def MatchRotationToVelocity(self, bInSetToInitialWhenFinished: bool): ...
    def ManualTick(self, DeltaTime: float): ...
    def IsFinished(self) -> bool: ...
    def InterpRotation(
        self,
        NewRot: core_uobject.Rotator,
        InterpTime: float,
        bLinear: bool,
        bYawOnly: bool,
        bInRelative: bool,
    ): ...
    def InterpLocation(
        self,
        NewLoc: core_uobject.Vector,
        InterpTime: float,
        bLinear: bool,
        bNoZ: bool,
        bInRelative: bool,
    ): ...
    def InterpDeltaRotation(
        self,
        DeltaRot: core_uobject.Rotator,
        InterpTime: float,
        bLinear: bool,
        bYawOnly: bool,
        bInRelative: bool,
    ): ...
    def InterpDeltaLocation(
        self,
        DeltaLoc: core_uobject.Vector,
        InterpTime: float,
        bLinear: bool,
        bNoZ: bool,
        bInRelative: bool,
    ): ...
    def InterpBallisticsByTime(
        self,
        StartLoc: core_uobject.Vector,
        EndLoc: core_uobject.Vector,
        LeapTime: float,
        LeapGravity: float,
    ) -> core_uobject.Vector: ...
    def InterpBallistics(
        self,
        StartLoc: core_uobject.Vector,
        EndLoc: core_uobject.Vector,
        LeapSpeed: float,
        LeapAngle: float,
    ) -> float: ...


class Ladder(engine.Actor):
    Mobility: int
    SegmentMesh: engine.StaticMesh
    SegmentMeshMaterialOverrides: unreal.WrappedArray[engine.MaterialInterface]
    TopMesh: engine.StaticMesh
    TopMeshMaterialOverrides: unreal.WrappedArray[engine.MaterialInterface]
    BottomAndTopMeshLDMaxDrawDistance: float
    bBottomAndTopMeshNeverDistanceCull: bool
    BottomMesh: engine.StaticMesh
    BottomMeshMaterialOverrides: unreal.WrappedArray[engine.MaterialInterface]
    SegmentSpacing: float
    SegmentOffset: core_uobject.Vector
    SegmentRotation: float
    TopOffset: core_uobject.Vector
    TopRotation: float
    BottomOffset: core_uobject.Vector
    BottomRotation: float
    VolumeDepth: float
    VolumeWidth: float
    VolumeExtraTopHeight: float
    VolumeExtraBottomHeight: float
    TopVolumeDepth: float
    VolumeOffset: core_uobject.Vector
    CharacterOffset: float
    NumSegments: int
    bHideTopMesh: bool
    bHideBottomMesh: bool
    SegmentMeshComponent: engine.InstancedStaticMeshComponent
    TopMeshComponent: engine.StaticMeshComponent
    BottomMeshComponent: engine.StaticMeshComponent
    VolumeBoxComponent: engine.BoxComponent
    TopVolumeBoxComponent: engine.BoxComponent


class LadderInterface(core_uobject.Interface): ...


class LadderVolume(engine.Volume):
    ClimbDirection: core_uobject.Vector
    Normal: core_uobject.Vector


class LandingData(gbx_runtime.GbxDataAsset):
    LandingData: unreal.WrappedArray[LandingInfo]


class MantleData(gbx_runtime.GbxDataAsset):
    Actions: unreal.WrappedArray[MantleActionData]
    ActionSlotToEnd: str
    MaxAlignToEdgeAngle: float
    MaxAdjustedHeightDifference: float
    RequiredLedgeDepth: float
    WallHopHeightMax: float
    WallHopDestinationHeightMax: float
    WallHopDestinationHeightMin: float
    WallHopDepth: float


class ModifierMathAttributeValueResolver(AttributeValueResolver):
    BaseValue: AttributeInitializationData
    ModifierStack: unreal.WrappedArray[ModifierMathAttributeValueResolverStackEntry]


class MotionControlLibrary(engine.BlueprintFunctionLibrary):

    def UpdateSpeed(
        self,
        CurrentSpeed: float,
        TargetSpeed: float,
        Acceleration: float,
        DeltaTime: float,
    ) -> float: ...
    def Spin(
        self,
        CurrentRotation: core_uobject.Rotator,
        RotationRate: float,
        RotationAxis: core_uobject.Vector,
        DeltaTime: float,
    ) -> core_uobject.Rotator: ...


class OrbitingActorComponent(engine.ActorComponent):
    TargetActor: engine.Actor
    BaseOrbitOffset: core_uobject.Vector
    ApproachSpeed: float
    SmoothingDistance: float
    SmoothingDuration: float
    XAxisOscillation: OrbitOscillationInfo
    YAxisOscillation: OrbitOscillationInfo
    ZAxisOscillation: OrbitOscillationInfo
    bIsInOrbit: bool
    SmoothingAlpha: float

    def SetTargetActor(self, NewTarget: engine.Actor): ...
    def OnRep_TargetActor(self, LastTarget: engine.Actor): ...


class ParentChallenge(Challenge): ...


class ParticleAttributeParameterEvaluator(engine.ParticleParameterEvaluator):
    Attribute: GbxAttributeData
    ParameterName: str
    bEvaluateEveryFrame: bool


class ParticleConditionalEmitterEvaluator(engine.ParticleParameterEvaluator):
    Condition: gbx_runtime.GbxCondition
    EmitterName: str
    bEnableIfTrue: bool
    bEvaluateEveryFrame: bool


class ParticlePropertyTrackingData(gbx_runtime.GbxDataAsset):
    MinValue: float
    MaxValue: float
    bStopTrackingWhenMinReached: bool
    bStopTrackingWhenMaxReached: bool
    bStopTrackingWhenPrimaryCharacterIsDeadOrNone: bool
    bDestroyParticleWhenTrackingStopped: bool
    bChangeValueOverTime: bool
    ValueChangePerSecond: float
    bPauseChangeOnUpdate: bool
    PauseDuration: float


class PawnAttachmentFunctionLibrary(engine.BlueprintFunctionLibrary):

    def RequestDetachPawnFromSlot(self, Actor: engine.Actor, SlotName: str): ...
    def RequestDetachPawnFromActor(self, Pawn: engine.Pawn): ...
    def QueryPawnAttachment(self, Pawn: engine.Pawn) -> PawnAttachmentQueryResult: ...
    def FindPawnAttachSlotComponent(
        self, Pawn: engine.Pawn
    ) -> PawnAttachSlotComponent: ...
    def DetachPawnFromSlot(
        self, Actor: engine.Actor, SlotName: str, bInstant: bool
    ): ...
    def DetachPawnFromActor(self, Pawn: engine.Pawn, bInstant: bool): ...
    def AttachPawnToSlot(
        self, Actor: engine.Actor, SlotName: str, Pawn: engine.Pawn, bInstant: bool
    ): ...


class PawnAttributeContextResolver(AttributeContextResolver): ...


class PhysicalAnimationProfileAsset(gbx_runtime.GbxDataAsset):
    BoneData: unreal.WrappedArray[PhysicalAnimationBoneData]
    DynamicToKinematicBlendMode: EPhysicalAnimationBlendToKinematicMode


class ProjectileAimViewPointHomingTargetComponent(engine.ActorComponent):
    LookAheadDistance: float
    HomingComponent: ProjectileHomingComponent
    TargetController: engine.Controller

    def SetTargetController(self, InTargetController: engine.Controller): ...
    def SetTargetActor(self, InTargetActor: engine.Actor): ...
    def GetTargetController(self) -> engine.Controller: ...
    def GetCurrentHomingLoc(self) -> core_uobject.Vector: ...


class PropertyUtilsTestContext(unreal.UObject):
    FloatProp: float
    FloatPropStaticArray: float
    FloatPropDynamicArray: unreal.WrappedArray[float]
    ObjectProp: PropertyUtilsTestContext
    ObjectPropStaticArray: PropertyUtilsTestContext
    ObjectPropDynamicArray: unreal.WrappedArray[PropertyUtilsTestContext]
    StructProp: PropertyUtilsTestStruct
    StructPropStaticArray: PropertyUtilsTestStruct
    StructPropDynamicArray: unreal.WrappedArray[PropertyUtilsTestStruct]
    DoubleProp: float
    Int8Prop: int
    UInt8Prop: int
    Int16Prop: int
    UInt16Prop: int
    Int32Prop: int
    UInt32Prop: int
    Int64Prop: int
    UInt64Prop: int


class RangedFeedbackData(FeedbackData): ...


class ReferenceActor(engine.Actor):
    PreviewClass: str

    def EnumeratePreviewClasses(self, ClasssList: unreal.WrappedArray[str]): ...


class ReplicatedEmitter(engine.Emitter):
    bOwnerNoSeeEmitter: bool
    TemplateOptions: ReplicatedEmitterTemplateOptions
    ReplicatedFloatParams: unreal.WrappedArray[EmitterFloatParam]
    ReplicatedVectorParams: unreal.WrappedArray[EmitterVectorParam]
    ReplicatedColorParams: unreal.WrappedArray[EmitterColorParam]
    ReplicatedWwiseEvent: EmitterWwiseEvent

    def OnRep_TemplateOptions(self): ...
    def OnRep_ReplicatedWwiseEvent(self): ...
    def OnRep_ReplicatedVectorParams(self): ...
    def OnRep_ReplicatedFloatParams(self): ...
    def OnRep_ReplicatedColorParams(self): ...
    def OnRep_OwnerNoSeeEmitter(self): ...


class ResourceWeightAttributeValueResolver(AttributeValueResolver):
    Resource: GameResourceData
    ResourceThreshold: AttributeInitializationData
    AboveThresholdWeight: AttributeInitializationData
    NoPoolWeight: AttributeInitializationData
    MinBelowThresholdWeight: AttributeInitializationData
    MaxBelowThresholdWeight: AttributeInitializationData


class RigidBodyActor(engine.Actor):
    RigidBodyComponent: RigidBodyComponent


class RigidBodyComponent(engine.StaticMeshComponent):
    RigidBodyImpactData: ImpactData
    OnImpulseAdded: Any
    bEnableHardSleeping: bool

    def SetKinematic(
        self, SleepingComponent: engine.PrimitiveComponent, BoneName: str
    ): ...


class SaveGameActorInterface(core_uobject.Interface): ...


class SceneBodySwitchAction(unreal.UObject): ...


class SceneBodySwitchComponent(engine.SceneComponent):
    DefaultState: str
    DetachAction: SceneBodySwitchAction
    ComponentRecords: unreal.WrappedArray[SceneComponentSwitchRecord]
    ReplicatedState: unreal.WrappedArray[int]

    def OnRep_ReplicatedState(self): ...
    def HandleWwiseEventFinished(
        self, WAC: wwise_audio.WwiseAudioComponent, WwiseEvent: wwise_audio.WwiseEvent
    ): ...
    def HandleParticleSystemFinished(self, PSC: engine.ParticleSystemComponent): ...
    def GetValidSwitchStateNames(self, OutNames: unreal.WrappedArray[str]): ...


class SceneBodySwitchFunctionLibrary(engine.BlueprintFunctionLibrary):

    def EnumerateValidSwitchStateNames(
        self, SwitchName: str, Names: unreal.WrappedArray[str]
    ): ...
    def EnumerateValidSwitchNames(self, Names: unreal.WrappedArray[str]): ...
    def ChangeSwitchExternal(
        self, Actor: engine.Actor, SwitchName: str, StateName: str
    ): ...
    def ChangeSwitch(
        self, Context: unreal.UObject, SwitchName: str, StateName: str
    ): ...


class SceneBodySwitchManagerComponent(engine.ActorComponent): ...


class ScreenParticleManagerComponent(engine.ActorComponent):
    ScreenParticleRecords: unreal.WrappedArray[ScreenParticleRecord]
    TrackedParticleProperties: unreal.WrappedArray[ParticlePropertyTracker]

    def ShowScreenParticleForActor(
        self,
        Actor: engine.Actor,
        Template: engine.ParticleSystem,
        bHideWhenFinished: bool,
        ContentDims: core_uobject.Vector2D,
        ParticleDepth: float,
        ScalingMode: EScreenParticleScalingMode,
        bOnlyOwnerSee: bool,
        bAlwaysVisible: bool,
        Tag: str,
        bAllowMultipleInstances: bool,
        bServerAuthority: bool,
        bTickEvenWhenPaused: bool,
        bHideDuringInGameMenu: bool,
    ): ...
    def OnScreenParticleFinished(self, Component: engine.ParticleSystemComponent): ...
    def HideScreenParticleForActor(
        self,
        Actor: engine.Actor,
        Template: engine.ParticleSystem,
        Tag: str,
        bAllowParticleToFinish: bool,
        bServerAuthority: bool,
    ): ...
    def ClientTrackParticleProperty(
        self,
        TrackingData: ParticlePropertyTrackingData,
        Template: engine.ParticleSystem,
        Tag: str,
        PropertyName: str,
        PropertyValue: float,
        bAddToValue: bool,
        UsedMaterialProperty: engine.MaterialInterface,
        MaterialPropertyName: str,
    ): ...
    def ClientShowScreenParticleEx(
        self,
        Template: engine.ParticleSystem,
        InitFlags: int,
        ContentDims: core_uobject.Vector2D,
        ParticleDepth: float,
        ScalingMode: EScreenParticleScalingMode,
        Tag: str,
    ): ...
    def ClientShowScreenParticle(
        self,
        Template: engine.ParticleSystem,
        bHideWhenFinished: bool,
        ContentDims: core_uobject.Vector2D,
        ParticleDepth: float,
        ScalingMode: EScreenParticleScalingMode,
        bOnlyOwnerSee: bool,
        bAlwaysVisible: bool,
        Tag: str,
        bAllowMultipleInstances: bool,
        bTickEvenWhenPaused: bool,
        bHideDuringInGameMenu: bool,
        bDepthPriorityWorld: bool,
    ): ...
    def ClientSetScreenParticleVectorParameter(
        self,
        Template: engine.ParticleSystem,
        Tag: str,
        ParameterName: str,
        Param: core_uobject.Vector,
    ): ...
    def ClientSetScreenParticleMaterialParameter(
        self,
        Template: engine.ParticleSystem,
        Tag: str,
        ParameterName: str,
        Param: engine.MaterialInterface,
    ): ...
    def ClientSetScreenParticleFloatParameter(
        self,
        Template: engine.ParticleSystem,
        Tag: str,
        ParameterName: str,
        Param: float,
    ): ...
    def ClientSetScreenParticleColorParameter(
        self,
        Template: engine.ParticleSystem,
        Tag: str,
        ParameterName: str,
        Param: core_uobject.LinearColor,
    ): ...
    def ClientSetScreenParticleActorParameter(
        self,
        Template: engine.ParticleSystem,
        Tag: str,
        ParameterName: str,
        Param: engine.Actor,
    ): ...
    def ClientHideScreenParticle(
        self, Template: engine.ParticleSystem, Tag: str, bAllowParticleToFinish: bool
    ): ...


class SenseConfigProviderInterface(core_uobject.Interface): ...


class SignificanceInterface(core_uobject.Interface): ...


class SimpleMathValueResolver(AttributeValueResolver):
    ValueA: AttributeInitializationData
    Operator: ESimpleMathValueResolverOperatorType
    ValueB: AttributeInitializationData


class SocketComponent(engine.SceneComponent): ...


class SpawnSimulatedActorSwitchAction(SceneBodySwitchAction):
    ActorClass: unreal.UClass
    bInheritVelocity: bool
    bEnableSpeedRange: bool
    bEnableAngularSpeedRange: bool
    DefaultAxis: int
    Direction: RelativeDirectionData
    Speed: float
    MaxSpeed: float
    RotationAxis: RelativeDirectionData
    AngularSpeed: float
    MaxAngularSpeed: float
    LifeSpan: float


class SprintData(engine.DataAsset):
    SprintFOVCurve: engine.CurveFloat
    bAddModifierToBaseFOV: bool
    SprintFOVModifier: float
    SprintFOVBlendInTime: float
    SprintFOVBlendOutTime: float
    SprintFOVBlendInDelay: float
    Feedback: FeedbackData
    SprintAttributeEffects: unreal.WrappedArray[AttributeEffectData]


class StanceBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def TryGetStanceComponent(
        self, AIController: aimodule.AIController
    ) -> StanceComponent: ...
    def SetStance(self, Target: engine.Actor, Stance: StanceDataProvider): ...
    def IsStanceComponentInStance(
        self, StanceComponent: StanceComponent, Stance: StanceDataProvider
    ) -> bool: ...
    def IsInStance(
        self, AnimInstance: engine.AnimInstance, Stance: StanceDataProvider
    ) -> bool: ...
    def EqualEqual_StanceTypeStanceType(self, A: StanceType, B: StanceType) -> bool: ...
    def EqualEqual_StanceDataStanceData(self, A: StanceData, B: StanceData) -> bool: ...
    def ClearStance(self, Target: engine.Actor): ...


class StanceComponent(engine.ActorComponent):
    OnStanceChanged: Any
    StanceSelector: StanceDataSelector
    StanceStack: StanceStack
    StanceState: StanceChangedEventArgs
    DefaultStanceMap: Any
    TimeEnteredCurrentStance: float

    def StackStanceChangedCallback(
        self,
        PreviousLayer: EStanceStackLayer,
        PreviousStance: StanceData,
        NextLayer: EStanceStackLayer,
        NextStance: StanceData,
    ): ...
    def SetStanceLayer(
        self, Layer: EStanceStackLayer, NewStance: StanceDataProvider
    ): ...
    def SetBlueprintStance(self, NewStance: StanceDataProvider): ...
    def OnRep_StanceState(self): ...
    def IsInStanceType(self, Type: StanceType) -> bool: ...
    def IsInStanceLayer(self, Layer: EStanceStackLayer) -> bool: ...
    def IsInStance(self, Stance: StanceDataProvider) -> bool: ...
    def IsInAnimStance(self, Stance: StanceDataProvider) -> bool: ...
    def GetTimeSpentInCurrentStance(self) -> float: ...
    def GetStanceLayer(self) -> EStanceStackLayer: ...
    def GetStance(self) -> StanceData: ...
    def FindTypeForStance(self, Stance: StanceData) -> StanceType: ...
    def FindStanceForType(self, Type: StanceType) -> StanceData: ...
    def ClearStanceLayer(self, Layer: EStanceStackLayer): ...
    def ClearBlueprintStance(self): ...


class StanceType(StanceDataProvider): ...


class StatusEffect(unreal.UObject):
    StackingStrategy: StatusEffectStackingStrategyData
    AttributeEffects: unreal.WrappedArray[AttributeEffect]
    bDoesDamageOverTime: bool
    DamageType: unreal.UClass
    DamageSourceClass: unreal.UClass
    DataAssetCopy: StatusEffectData

    def OnEndEffect(self, Target: engine.Actor): ...
    def OnBeginEffect(self, Target: engine.Actor): ...


class StatusEffectModifierAttributePropertyValueResolver(
    AttributePropertyValueResolver
):
    StatusEffectData: Any


class StatusEffectStackingStrategyData_Capped(StatusEffectStackingStrategyData):
    MaxCount: int
    bCapPerOwner: bool
    bNoInfiniteDuration: bool
    SelectionCriteria: EStatusEffectStackingInstanceSelectionCriteria
    ReplacementCriteria: EStatusEffectStackingInstanceReplacementCriteria
    DurationRefund: StatusEffectStackingStrategyData_DurationRefundData


class TargetableComponent(TeamComponent):
    SightSenseLock: ResourceLock
    bSearchableByFindProjectileEQSTargetGenerator: bool
    bIsTargetable: bool
    bIsTargetableByHumanPlayers: bool
    bIsTargetableByAIPlayers: bool
    bIsTargetableByNonPlayers: bool
    bOnlyTargetableIfPlayersAreThreatened: bool
    TargetUIName: GbxUIName
    TargetName: str
    TargetSocket: str
    TargetSocketBounds: TargetLocationBoundsSettings
    bUseTargetSocketBounds: bool
    AdditionalTargetSockets: unreal.WrappedArray[TargetLocationSettings]
    TargetingMe: unreal.WrappedArray[TargetingComponent]
    CapsuleSections: float
    UntargetableLock: ResourceLock
    MeleeTargetingSockets: unreal.WrappedArray[str]
    ConditionalMeleeTargetingSockets: unreal.WrappedArray[OverrideMeleeSocket]
    TargetProxyComponents: unreal.WrappedArray[str]
    TargetProxies: unreal.WrappedArray[engine.SceneComponent]
    bAllowCharacterHoming: bool
    AimAssistSnapTargetType: EAimAssistSnapTargetType
    bTargetTracking: bool
    bDisableBulletMagnetism: bool

    def SetTargetUIName(self, NewTargetUIName: GbxUIName): ...
    def SetTargetName(self, NewTargetName: str): ...
    def SetIsTargetableByNonPlayers(self, IsTargetable: bool): ...
    def SetIsTargetableByHumanPlayers(self, IsTargetable: bool): ...
    def SetIsTargetableByAIPlayers(self, IsTargetable: bool): ...
    def SetIsTargetable(self, IsTargetable: bool): ...
    def OnRep_TargetUIName(self): ...
    def IsTargetableByPawn(self, Pawn: engine.Pawn) -> bool: ...
    def IsTargetableByNonPlayers(self) -> bool: ...
    def IsTargetableByHumanPlayers(self) -> bool: ...
    def IsTargetableByController(self, Controller: engine.Controller) -> bool: ...
    def IsTargetableByAIPlayers(self) -> bool: ...
    def IsTargetableByActor(self, Actor: engine.Actor) -> bool: ...
    def IsTargetable(self) -> bool: ...
    def GetTargetSocketName(self) -> str: ...
    def GetTargetProxyComponentNames(self, Array: unreal.WrappedArray[str]): ...
    def GetTargetNameString(self) -> str: ...
    def GetTargetLocations(self) -> unreal.WrappedArray[core_uobject.Vector]: ...
    def GetTargetLocation(self) -> core_uobject.Vector: ...
    def GetClosestTargetLocation(
        self, Origin: core_uobject.Vector, Direction: core_uobject.Vector
    ) -> core_uobject.Vector: ...
    def GetAvailableSocketNames(self, Array: unreal.WrappedArray[str]): ...


class TargetActorInfoLibrary(engine.BlueprintFunctionLibrary):

    def IsSenseActive(self, Info: TargetActorInfo, Sense: unreal.UClass) -> bool: ...
    def IsExistingTarget(self, Info: TargetActorInfo) -> bool: ...
    def IsDirectlySensed(self, Info: TargetActorInfo) -> bool: ...
    def HasStimulusForSense(
        self, Info: TargetActorInfo, Sense: unreal.UClass
    ) -> bool: ...
    def HasAnyKnownStimuli(self, Info: TargetActorInfo) -> bool: ...
    def GetStimulusLocation(
        self, Info: TargetActorInfo, Sense: unreal.UClass
    ) -> core_uobject.Vector: ...
    def GetStimulusForSense(
        self, Info: TargetActorInfo, Sense: unreal.UClass, Stimulus: aimodule.AIStimulus
    ) -> bool: ...
    def GetReceiverLocation(
        self, Info: TargetActorInfo, Sense: unreal.UClass
    ) -> core_uobject.Vector: ...
    def GetBestStimulusLocation(
        self, Info: TargetActorInfo, Age: float
    ) -> core_uobject.Vector: ...
    def GetBestStimulus(
        self, Info: TargetActorInfo, Stimulus: aimodule.AIStimulus
    ) -> bool: ...
    def GetBestAttackLocation(
        self, Info: TargetActorInfo, OutTargetVelocity: core_uobject.Vector
    ) -> core_uobject.Vector: ...
    def FindActorTargetingComponent(
        self, Actor: engine.Actor
    ) -> TargetingComponent: ...


class TargetingComponent(engine.ActorComponent):
    TargetListChangedBpEvent: Any
    QueryFrequency: float
    bQueryImmediately: bool
    QueryParams: EnvQueryParams
    BlackboardKeys: unreal.WrappedArray[GbxBlackboardKeySelector]
    bOnlyTargetThreatsToPlayers: bool
    CurrentTargetable: TargetableComponent

    def ServerSetBestTarget(self, NewBestTarget: engine.Actor): ...
    def IsBestTargetDirectlySensed(self, TargetIndex: int) -> bool: ...
    def HasTargets(self) -> bool: ...
    def HasTarget(self, Actor: engine.Actor) -> bool: ...
    def GetTargetLocationForActor(
        self, Actor: engine.Actor, TargetLocation: core_uobject.Vector
    ) -> bool: ...
    def GetTargetInfoForActor(
        self, Actor: engine.Actor, TargetInfo: TargetActorInfo
    ) -> bool: ...
    def GetTargetInfoCount(self) -> int: ...
    def GetTargetInfoAt(
        self, TargetIndex: int, TargetInfo: TargetActorInfo
    ) -> bool: ...
    def GetTargetActorAt(self, TargetIndex: int) -> engine.Actor: ...
    def GetBestThreatActor(self, bRequireFirsthandKnowledge: bool) -> engine.Actor: ...
    def GetBestTargetLocation(self, TargetIndex: int) -> core_uobject.Vector: ...
    def GetBestTargetInfo(
        self, TargetInfo: TargetActorInfo, TargetIndex: int
    ) -> bool: ...
    def GetBestTargetActor(self, TargetIndex: int) -> engine.Actor: ...
    def GetBestTargetableComponent(self, TargetIndex: int) -> TargetableComponent: ...
    def GetBestAttackTargetLocation(
        self, OutTargetVelocity: core_uobject.Vector, TargetIndex: int
    ) -> core_uobject.Vector: ...
    def DoesBestTargetHaveStimulusForSense(
        self, Sense: unreal.UClass, MaxAge: float, TargetIndex: int
    ) -> bool: ...


class TargetingDebugServerRpcComponent(engine.ActorComponent):

    def SetInspectedActor(self, Actor: engine.Actor): ...


class Team(gbx_runtime.GbxDataAsset):
    DisplayName: str
    SelfAttitude: int
    DefaultAttitude: int
    DefaultAttitudeFromTeams: int
    bUseDefaultAttitudeFromTeams: bool
    AttitudeTowardTeams: unreal.WrappedArray[TeamAttitudeSetEntry]
    AttitudeFromTeams: unreal.WrappedArray[TeamAttitudeSetEntry]
    bEnableTeamCollisionChannel: bool
    TeamCollisionChannel: ETeamCollisionChannel

    def GetAttitudeToward(self, Team: Team) -> int: ...


class TeleportInterface(core_uobject.Interface): ...


class TerritoryComponent(engine.PrimitiveComponent):
    PatrolTerritory: TerritoryData
    ThreatTerritory: TerritoryData
    CombatTerritory: TerritoryData
    CombatProxy: ETerritoryCombatProxyType
    bUseCombatProxy: bool
    bAlwaysAwareInThreatArea: bool
    DrawStyle: ETerritoryDrawStyle
    LinkedTerritories: unreal.WrappedArray[TerritoryComponent]


class TrivialFoleyImplementationComponent(engine.ActorComponent):
    FootstepImpact: ImpactData
    FootstepPhysmat: engine.PhysicalMaterial
    BodySkeletalMesh: engine.SkeletalMeshComponent
    FootSockets: unreal.WrappedArray[str]
    CachedFoleyMainComponent: gbx_audio.FoleyMainComponent


class UIStatData_Numeric_Formula(UIStatData_Numeric):
    Formula: UIStatFormulaEvaluator


class UIStatData_Text(UIStatData):
    Text: str
    TextWithAdditionalInput: str


class UIStatAttributeEffectProvider(core_uobject.Interface): ...


class UsabilityDataSelection(gbx_runtime.GbxDataAsset):
    EnabledCondition: gbx_runtime.GbxCondition
    PrimaryUseDefSelection: UseDefSelection
    PrimaryHoldUseDefSelection: UseDefSelection
    SecondaryUseDefSelection: UseDefSelection
    SecondaryHoldUseDefSelection: UseDefSelection


class UsableTypeDefinition(gbx_runtime.GbxDataAsset):
    ActionText: str
    InputActionOverride: str
    bDisplayLockedIcon: bool
    bHidePrompt: bool
    bCostsToUse: bool
    CurrencyType: GbxInventoryCategoryData
    CostContext: EUsableTypeCostContext
    Cost: AttributeInitializationData


class UserStatesInterface(core_uobject.Interface):

    def HasEnableConditionsSetForAnyUserState(self) -> bool: ...
    def BlueprintStateHandler(self, bFromLoad: bool): ...


class UserStatesFunctionLibrary(engine.BlueprintFunctionLibrary):

    def HasEnableConditionsSetForSpecificUserState(
        self, Context: unreal.UObject, UserStateProperty: str
    ) -> bool: ...


class UseSystemFunctionLibrary(engine.BlueprintFunctionLibrary):

    def SetIsUsable(self, Actor: engine.Actor, bNewIsUsable: bool): ...
    def ResetUseCount(self, Actor: engine.Actor): ...


class WeaponInterface(core_uobject.Interface): ...


class WeaponUserInterface(core_uobject.Interface): ...


class WeatherTemplate(gbx_runtime.GbxDataAsset):
    WorldSpaceParticleTemplate: engine.ParticleSystem
    ScreenSpaceParticleTemplate: engine.ParticleSystem


class StanceChangedEventArgs:
    PreviousLayer: EStanceStackLayer
    PreviousStanceType: StanceType
    PreviousStance: StanceData
    NextLayer: EStanceStackLayer
    NextStanceType: StanceType
    NextStance: StanceData


class ControlledMoveNetCorrection:
    Runtime: float
    ControlledMove: unreal.UClass


class FacingInfo:
    Type: EFacingInfoType
    Actor: engine.Actor
    Component: engine.SceneComponent
    Vector: core_uobject.Vector
    Rotator: core_uobject.Rotator
    Offset: core_uobject.Vector


class MantleAttemptInfo:
    ActionIndex: int
    Location: core_uobject.Vector
    MovementBase: engine.PrimitiveComponent


class CharacterMoveToCommand:
    TargetActor: engine.Actor
    TargetLocation: core_uobject.Vector
    Duration: float
    bContinuouslyUpdate: bool
    bEnforceMaxSpeed: bool
    bEnforceMaxSpeedOnEnding: bool
    bMoveZAxis: bool


class CharacterRotateToCommand:
    TargetActor: engine.Actor
    TargetSocket: str
    TargetLocation: core_uobject.Vector
    Duration: float
    bFreezeRotation: bool
    InterpSpeed: float
    MaxYawRate: float
    MaxPitchRate: float
    bUseEasing: bool
    Easing: GbxEasingFunc


class GbxEasingFunc:
    Func: int
    BlendExp: float
    Steps: int


class RootMotionStateData:
    GbxCharMoveComp: GbxCharacterMovementComponent
    GbxAnimInstance: GbxCharacterAnimInstance


class IdleVelocityData: ...


class GbxInterpData:
    Actor: engine.Actor
    Controller: engine.Controller
    MoveComp: engine.MovementComponent


class RotationDeltaMatchingInfo:
    RotationTimeCurve: engine.FloatCurve


class NavAnimClientData:
    Direction: engine.Vector_NetQuantizeNormal
    GoalLoc: engine.Vector_NetQuantize
    GoalRadius: float


class NavAnimServerData:
    Areas: unreal.UObject
    UserEdges: unreal.UObject


class NavAnimState:
    CachedAnimInst: engine.AnimInstance
    MachineList: unreal.WrappedArray[NavAnimMachineData]
    ServerTransition: NavAnimTransition
    ClientTransitionIdx: int


class NavAnimTransition:
    State: ENavAnimState
    Info: NavAnimDesiredInfo
    RowName: str
    MachineIdx: int
    RunIdx: int


class NavAnimDesiredInfo:
    Yaw: float
    FaceLoc: engine.Vector_NetQuantize


class NavAnimMachineData:
    MachineIdx: int
    ServerBaseState: ENavAnimState
    CurrState: ENavAnimState


class GbxCharacterNavWalking:
    MoveComp: GbxCharacterMovementComponent


class ReplicatedMantleState:
    Counter: int
    ActionIndex: int


class MantleState:
    MovementComponentOwner: GbxCharacterMovementComponent
    MantleData: MantleData
    GameplayGlobals: GbxGameplayGlobals
    ActiveActionData: MantleActiveActionData
    CurrentTrace: MantleTraceCheck


class MantleTraceCheck:
    Inputs: MantleTraceInputs


class MantleTraceInputs:
    World: engine.World
    MantleData: MantleData
    Globals: GbxGameplayGlobals
    SourceActor: engine.Actor


class MantleActiveActionData:
    MantleAttempt: MantleAttemptInfo


class ControlledMoveReplicationData:
    DirtyCounter: int
    ControlledMove: unreal.UClass
    Parameters: ControlledMoveParameters
    PackedDirection: core_uobject.Vector
    bZeroVelocity: bool
    bInterrupted: bool


class ControlledMoveParameters:
    SpeedOverride: float
    DurationOverride: float
    LaunchAngleOverride: float
    TargetActor: engine.Actor
    TargetLocation: core_uobject.Vector


class ControlledMoveState:
    MovementComponentOwner: GbxCharacterMovementComponent
    CurrentMove: ControlledMove
    Instigator: engine.Actor
    BaseSpeed: float
    Speed: float
    Runtime: float
    TargetActor: engine.Actor
    InitialDirection: core_uobject.Vector
    CurrentDirection: core_uobject.Vector
    FrameMoveVelocity: core_uobject.Vector
    LastHitActor: engine.Actor
    aForwardInput: float
    aStrafeInput: float


class ReplicatedLadderState:
    DirtyCounter: int
    LadderType: EScriptedLadderType


class LadderAnimState:
    PendingType: EScriptedLadderType
    CurrentType: EScriptedLadderType


class CharacterScriptedMeshOffsetState:
    Cmd: CharacterScriptedMeshOffsetCommand


class CharacterScriptedMeshOffsetCommand:
    RootMotionSourceAnim: engine.AnimSequence
    HorzCurv: engine.RuntimeFloatCurve
    VertCurv: engine.RuntimeFloatCurve


class CharacterRotateToState:
    CommandData: CharacterRotateToCommand


class CharacterMoveToState:
    CommandData: CharacterMoveToCommand


class UseEvent:
    UserController: engine.Controller
    UsedComponent: engine.PrimitiveComponent
    UseType: EUsabilityType
    bWasHeld: bool


class LandingInfo:
    bNoMinVelIfJumped: bool
    LandedMinVel: float
    LandedImpact: ImpactData
    bPlayLandedImpactAtSpecificFeet: bool
    LandedAction: unreal.UClass
    VocalizationTag: gbx_audio.CharacterSoundTag


class ReceivedDamageDetails:
    bWasCrit: bool
    HitLocation: core_uobject.Vector
    HitDirection: core_uobject.Vector
    HitComponent: engine.PrimitiveComponent
    HitRegion: HitRegionData
    DamagePerHealthType: unreal.WrappedArray[HealthTypeDamageSummary]
    RadiusDamageOrigin: core_uobject.Vector
    DamageRadius: float
    bWasBulletReflected: bool


class HealthTypeDamageSummary:
    HealthType: HealthTypeData
    Damage: float


class CausedDamageDetails:
    bWasCrit: bool
    HitLocation: core_uobject.Vector
    HitDirection: core_uobject.Vector
    DamageCauser: engine.Actor
    HitComponent: engine.PrimitiveComponent
    HitRegion: HitRegionData
    DamagePerHealthType: unreal.WrappedArray[HealthTypeDamageSummary]
    RadiusDamageOrigin: core_uobject.Vector
    DamageRadius: float
    bIsDamageOverTime: bool


class CausedDeathDetails:
    DamageSource: DamageSource
    DamageType: GbxDamageType
    DamageInstigator: engine.Pawn
    DamageCauser: engine.Actor
    Damage: float
    OverkillDamage: float
    bWasCrit: bool
    bWasAwareOfKiller: bool
    bWasFullyHealthy: bool
    HitLocation: core_uobject.Vector
    HitDirection: core_uobject.Vector
    RadiusDamageOrigin: core_uobject.Vector
    DamageRadius: float
    DamagePerHealthType: unreal.WrappedArray[HealthTypeDamageSummary]


class CausedHealingDetails:
    HealTarget: engine.Actor
    HealInstigator: engine.Actor
    Healing: float
    DamageSource: DamageSource
    DamageType: GbxDamageType


class HitFriendlyEventDetails:
    HitTarget: engine.Actor
    HitInstigator: engine.Actor
    DamageSource: DamageSource
    DamageType: GbxDamageType


class HitByFriendlyEventDetails:
    DamageInstigator: engine.Actor
    DamageType: GbxDamageType
    DamageSource: DamageSource


class GameResourcePoolReference:
    PoolIndexInManager: int
    PoolManager: GameResourcePoolManagerComponent


class PlayerDamageDataPresentation:
    ScreenParticle: engine.ParticleSystem
    HitDirection: engine.Vector_NetQuantizeNormal


class RangedDistanceOverrides:
    bOverrideRangedDistances: bool
    MinDistanceOverride: float
    MaxDistanceOverride: float


class ActiveTrackedFeedback:
    FeedbackData: FeedbackData
    LastStartTime: float
    LastRandomShakeTime: float
    RandomCameraShake: float
    BaseScale: float
    CurrentScale: float
    CurrentCameraShakeScale: float
    CameraShakeXScale: float
    CameraShakeYScale: float
    SourceLocation: core_uobject.Vector
    RangedDistanceOverrides: RangedDistanceOverrides
    bRumbleFinished: bool
    bShakeFinished: bool
    AdditionalCameraShakeScales: unreal.WrappedArray[float]
    SourceContext: unreal.UObject


class StatusEffectSpec:
    StatusEffectData: StatusEffectData
    EffectOwner: unreal.UObject
    EffectOwnerContextOverride: unreal.UObject
    DurationType: EStatusEffectDurationType
    Duration: float
    EffectInstigator: engine.Controller
    DamageCauser: engine.Actor
    DamagePerSecond: float


class UsabilityInfo:
    bCanUse: bool
    bCanInteractWith: bool
    bCanPrimaryUse: bool
    bCanPrimaryHoldUse: bool
    bCanSecondaryUse: bool
    bCanSecondaryHoldUse: bool
    bCanShowUseDef: bool
    OptionalErrorText: str
    PrimaryUseDef: UsableTypeDefinition
    PrimaryHoldUseDef: UsableTypeDefinition
    SecondaryUseDef: UsableTypeDefinition
    SecondaryHoldUseDef: UsableTypeDefinition


class ResourceLock:
    bLocked: bool


class UsableCostCache:
    PrimaryCost: int
    SecondaryCost: int
    PrimaryHoldUseCost: int
    SecondaryHoldUseCost: int


class LatentUseState:
    UsableComponent: UsableComponent


class UseTraceResult:
    UsableComponent: UsableComponent
    HitComponent: engine.PrimitiveComponent
    Usability: UsabilityInfo


class UsabilityQuery:
    UserController: engine.Controller
    UsedComponent: engine.PrimitiveComponent
    UseType: EUsabilityType
    bUseHeld: bool


class UsableAngleRestriction:
    AngleOffset: float
    AngleWidth: float


class UseDefSelection:
    bOverrideDefaultUseDefinition: bool
    bOverrideConditionalDefs: bool
    DefaultUseDefinition: UsableTypeDefinition
    ConditionalUseDefs: unreal.WrappedArray[UseDefinitionConditional]


class UseDefinitionConditional:
    UseDefinition: UsableTypeDefinition
    UseCondition: gbx_runtime.GbxCondition


class HoldToUseSettings:
    Mode: EHoldToUseMode
    HoldToUseStartTime: float
    HoldToUseTime: float
    bUseInteractionBreakDistance: bool
    InteractionBreakDistance: float


class StatusEffectInstanceReference:
    StatusEffectManagerComponent: StatusEffectManagerComponent
    StatusEffectData: StatusEffectData
    StatusEffectInstanceID: int


class HealthType:
    HealthTypeData: HealthTypeData
    HealthPoolData: GameResourcePoolData
    HealthSectionPercentages: unreal.WrappedArray[float]
    bResetIdleTimerIfNoDamage: bool
    bUseChanceToExist: bool
    ChanceToExist: AttributeInitializationData
    HealthPool: GameResourcePoolReference


class AttributeInitializationData:
    BaseValueConstant: float
    DataTableValue: DataTableValueHandle
    BaseValueAttribute: GbxAttributeData
    AttributeInitializer: unreal.UClass
    BaseValueScale: float


class DataTableValueHandle:
    DataTable: engine.DataTable
    RowName: str
    ValueName: str


class ReplicatedImpactHitResult:
    bLocalSpace: bool
    ImpactPoint: engine.Vector_NetQuantize
    Normal: engine.Vector_NetQuantizeNormal
    PhysMaterial: engine.PhysicalMaterial
    Actor: engine.Actor
    Component: engine.PrimitiveComponent
    BoneName: str


class ImpactResponseParams:
    ParticleParameters: unreal.WrappedArray[engine.ParticleSysParam]
    AudioParameters: unreal.WrappedArray[ImpactAudioParam]
    AudioSurfaceSwitch: wwise_audio.WwiseSwitch
    DecalOverride: engine.MaterialInterface


class ImpactAudioParam:
    Parameter: wwise_audio.WwiseRtpc
    Switch: wwise_audio.WwiseSwitch
    Value: float


class AnimGraphBoneSet:
    BoneSet: engine.GbxBoneSet
    AnimGraphMachineName: str


class SavedCollision:
    SavedItems: unreal.WrappedArray[SavedCollisionItem]
    SavedTeamItems: unreal.WrappedArray[SavedTeamCollision]


class SavedTeamCollision:
    TeamComponent: TeamComponent
    bUseTeamCollision: bool
    bCollideWithTeam: bool


class SavedCollisionItem:
    Primitive: engine.PrimitiveComponent
    Responses: engine.CollisionResponseContainer


class FacingController:
    RemoteChannels: RemoteFacingChannel


class RemoteFacingChannel:
    Pitch: int
    Yaw: int


class ReplicatedPawnAttachState:
    Slot: PawnAttachSlotComponent
    Status: EPawnAttachStatus
    StatusFlag: int


class SpawnCostSelection:
    Selection: ESpawnCostSelection
    Preset: str
    SpawnCost: int


class MassSelection:
    Selection: EMassSelection
    Preset: str
    Mass: float


class SoundPerceptionProperties:
    bEnabled: bool
    Loudness: float
    MaxRange: float


class BulletPerceptionProperties:
    bEnabled: bool
    Strength: float


class ActorPartList:
    Parts: unreal.WrappedArray[ActorPartData]


class ActorPartSelectionOverrideData:
    PreferredParts: unreal.WrappedArray[ActorPartList]


class StaticRagdollReplicationData:
    Bodies: unreal.WrappedArray[MinimalStaticRigidBodyState]


class MinimalStaticRigidBodyState:
    BoneIndex: int
    Rotation: core_uobject.Rotator


class GbxAttributeModifierHandle: ...


class RegisteredConditionalDamageCriticalModifier:
    Modifier: ConditionalDamageCriticalModifier
    ModifierValueContextOverride: unreal.UObject


class RegisteredConditionalDamageValueModifier:
    Modifier: ConditionalDamageValueModifier
    DamageValueContextOverride: unreal.UObject


class ReflectedDamageParams:
    DamageScale: float
    DamageTakenScale: float
    bReflectTowardAttacker: bool
    DamageType: unreal.UClass


class StatusEffectModifiers:
    StatusEffectData: StatusEffectData
    EffectChanceModifier: engine.GbxAttributeFloat
    EffectDurationModifier: engine.GbxAttributeFloat
    EffectDamageModifier: engine.GbxAttributeFloat


class AttitudeDamageRules:
    bAllowHostileDamage: bool
    bAllowNeutralDamage: bool
    bAllowFriendlyDamage: bool


class DamageGoreModifiers:
    GoreModifier: float
    GibModifier: float


class CriticalHitDamageOverrides:
    Type: ECriticalHitDamageOverride
    bUseDefaultCriticalHitMultiplier: bool
    AdditionalCriticalMultiplier: float


class DamageReactionEventSummary:
    DamageCauser: engine.Pawn
    HitLocation: core_uobject.Vector
    HitDirection: core_uobject.Vector
    DamageSource: unreal.UClass
    DamageType: unreal.UClass
    HitComponent: engine.PrimitiveComponent
    HitRegion: HitRegionInfo
    Origin: core_uobject.Vector
    Radius: float
    EventIndex: int


class HitRegionInfo:
    Data: HitRegionData
    StateIndex: int


class StanceFloatValue:
    ValueType: EStanceValueOverrideType
    Value: float


class SpawnPatternResult:
    Location: core_uobject.Vector
    LinearImpulse: core_uobject.Vector
    bLinearVelocityChange: bool
    AngularImpulse: core_uobject.Vector
    bAngularVelocityChange: bool


class AimControlParameters:
    AimControlData: AimControlData


class CachedUIStatCollectionData:
    Sections: unreal.WrappedArray[CachedUIStatSectionData]


class CachedUIStatSectionData:
    Name: str
    Stats: unreal.WrappedArray[CachedUIStatData]


class CachedUIStatData:
    Stat: UIStatData
    Description: str
    ValueText: str
    ComparisonValue: float
    ComparisonResult: EUIStatComparisonResult


class StatusEffectQueryResult:
    NumberOfInstances: int
    DPS: float


class StatusEffectQuery:
    StatusEffectData: StatusEffectData
    Owner: unreal.UObject


class StatusEffectRemoveSpec:
    StatusEffectData: StatusEffectData
    EffectOwner: unreal.UObject


class StatusEffectInstanceStack:
    Owner: StatusEffectManagerComponent
    StatusEffectData: StatusEffectData
    DoTDamageComponent: DamageComponent
    AttributeEffects: unreal.WrappedArray[AppliedAttributeEffect]
    DPSContributions: unreal.WrappedArray[DamageOverTimeContribution]
    Instances: unreal.WrappedArray[StatusEffectInstance]


class StatusEffectInstance:
    Spec: StatusEffectSpec


class DamageOverTimeContribution:
    PipelineInput: PipelineDamageInput


class PipelineDamageInput:
    DamageReceiverComp: DamageComponent
    Damageable: Any
    InstigatorPawn: engine.Pawn
    AdditionalEventListenerPawn: engine.Pawn
    DamageCauser: engine.Actor
    DamageModifierComp: DamageModifierComponent
    InstigatorController: engine.Controller
    DamageSource: unreal.UClass
    DamageType: unreal.UClass
    ImpactData: ImpactData
    InstigatorFeedback: FeedbackData
    bSimulatedOnClient: bool
    CriticalHitOverrides: CriticalHitDamageOverrides
    GoreModifiers: DamageGoreModifiers


class AppliedAttributeEffect:
    AttributeEffectRef: AttributeEffectReference
    AttributeResolutionContext: unreal.UObject
    Owner: StatusEffectManagerComponent


class AttributeEffectReference:
    StatusEffectData: StatusEffectData


class UserStatesReplicationData:
    bInitialized: bool
    PackedStateBits: int


class UserStatesRuntimeData:
    States: unreal.WrappedArray[UserStateSetRuntimeData]


class UserStateSetRuntimeData:
    Property: core_uobject.ByteProperty
    ActiveState: int
    EnableConditions: unreal.WrappedArray[gbx_runtime.GbxCondition]


class CompiledUserStatesData:
    CompiledSets: unreal.WrappedArray[CompiledUserSet]


class CompiledUserSet:
    StateProperty: engine.MemberReference
    EnableConditionVariableNames: unreal.WrappedArray[str]


class GbxUIFormattedText:
    FormatText: str
    FormatParams: Any


class GbxBlackboardKeySelector:
    KeyName: str
    bRuntimeKey: bool


class GbxParam:
    ValueType: EGbxParamValueType
    DisabledValueModes: int
    ValueFlags: int
    ValueMode: EGbxParamValueMode
    Range: gbx_runtime.NumericRange
    AttributeInitializer: unreal.UClass
    AttributeData: GbxAttributeData
    AttributeInitializationData: AttributeInitializationData
    BlackboardKey: GbxBlackboardKeySelector
    Condition: gbx_runtime.GbxCondition
    Actor: engine.Actor


class GbxQueryOptions:
    OwnerLocationUse: EQueryOwnerLocationUse
    ReplaceLastResultThreshold: float
    bReplaceLastResult: bool
    bKeepValidValues: bool
    MinUpdatePeriod: float
    PauseUpdatesWhenNotPingedForTime: float
    bUpdateAlways: bool
    WhenToDoFullQueryUpdates: ETimedUpdateBehavior
    bCanUpdateWhileActive: bool
    OwnerMoveThreshold: GbxParam
    bUpdateWhenOwnerMoves: bool
    PrimaryContextMoveThreshold: GbxParam
    bUpdateWhenPrimaryContextMoves: bool
    Origin: GbxQueryOriginOptions
    bUpdateOrigin: bool
    bOnlyUpdateWhenCanPath: bool
    bUpdateWhenHotSpotsListChanges: bool


class GbxQueryOriginOptions:
    UpdatePeriod: GbxParam
    UpdateCondition: GbxParam
    bInvertCondition: bool


class EnvQueryParams:
    Query: aimodule.EnvQuery
    AdditionalTests: unreal.WrappedArray[aimodule.EnvQueryTest]
    AdditionalTestAssets: unreal.WrappedArray[EnvQueryTestAsset]
    RunMode: int
    bDisableRunModeEditing: bool
    Contexts: unreal.WrappedArray[GbxNamedParam]
    bDisableContextEditing: bool
    bAllowEmptyContexts: bool
    ContextTypeTable: Any
    Params: unreal.WrappedArray[GbxNamedParam]
    RequiredSignificanceRating: int


class GbxNamedParam(GbxParam):
    Name: str


class GbxAnimTableRow(engine.TableRowBase):
    Animation: AnimActionDef


class AnimActionDef:
    InputType: EAnimActionDefInput
    AnimAsset: engine.AnimationAsset
    AnimAssetName: str


class ActionState_Base: ...


class ActionState_SimpleAnim(ActionState_Base): ...


class AnimMeshList:
    Body3rd: AnimActionDef
    Body1st: AnimActionDef
    Weapon3rd: AnimActionDef
    Weapon1st: AnimActionDef
    Extras: unreal.WrappedArray[AnimMeshExtra]


class AnimMeshExtra:
    Anim: AnimActionDef
    MeshName: str
    AnimSlotOverride: str
    bHasAnimSlotOverride: bool
    BlendInOverride: float
    bHasBlendInOverride: bool
    BlendOutOverride: float
    bHasBlendOutOverride: bool


class PreviewState:
    bEnabled: bool
    PreviewActorManager: PreviewActorManager
    PreviewClass: unreal.UClass
    PreviewBounds: core_uobject.Box
    bAutoCycle: bool
    PreviewIdx: int
    PreviewAction: unreal.UClass
    ElapsedTime: float
    Duration: float
    bPlayingAction: bool
    bQueuedAction: bool
    bShowAction: bool
    bRepeatAction: bool


class PreviewActorManager:
    AttachComponent: engine.SceneComponent
    Actor: engine.Actor
    ActorClass: unreal.UClass
    ActorTemplate: engine.Actor


class ActionState_Anim(ActionState_SimpleAnim): ...


class AttributeBaseValueData:
    AttributeToSetBaseValueOf: GbxAttributeData
    BaseValue: AttributeInitializationData


class ImpactResponseInfo:
    PhysicalMaterial: engine.PhysicalMaterial
    Response: ImpactResponseEffect


class ImpactResponseEffect:
    bHighPriority: bool
    bCensorThisEffect: bool
    CensoredEffectAlternative: ImpactData
    bOverrideImpactWwiseEvent: bool
    ImpactWwiseEvent: wwise_audio.WwiseEvent
    ParticleTemplate: engine.ParticleSystem
    bAttachParticleToHitActor: bool
    bAttachParticleToHitBone: bool
    bHideEffectFromHitActor: bool
    bNoOverlapDecal: bool
    NoOverlapDecalGroupName: str
    DecalMaterials: unreal.WrappedArray[engine.MaterialInterface]
    DecalWidth: float
    DecalHeight: float
    DecalThickness: float
    DecalMinScale: float
    DecalMaxScale: float
    bDecalRandomRotation: bool
    DecalRandomRotationLimit: float
    DecalLifetime: float
    DecalFadeDuration: float
    SignificanceEvent: GbxSignificanceEvent
    bPlayFeedbackOnHitActor: bool
    HitFeedback: FeedbackData
    AreaFeedback: FeedbackData
    EffectParameters: ImpactResponseParams


class GbxSignificanceEvent:
    Event: str


class ForceSelection:
    Selection: EForceSelection
    Preset: str
    Attribute: GbxAttributeData
    Force: float


class GbxAnimInstanceProxy(engine.AnimInstanceProxy): ...


class GbxCharacterAnimInstanceProxy(GbxAnimInstanceProxy): ...


class ActionState_CoordinatedEffect(ActionState_Base): ...


class ActionState_Gib(ActionState_Base): ...


class ActionState_Loop(ActionState_SimpleAnim): ...


class ActionState_PhysicalAnim(ActionState_Anim): ...


class ActionState_PhysicalDeath(ActionState_PhysicalAnim): ...


class AttributeDefinedValueRow(engine.TableRowBase): ...


class CustomizationLinkedParameter:
    LinkedParameterName: str
    LinkedParameterType: ELinkedParameterType


class HealthTypeBalanceData(engine.TableRowBase): ...


class WeightedActorPartData:
    PartData: ActorPartData
    Weight: AttributeInitializationData


class ViewLeadingRotationInfo:
    Effect: core_uobject.Rotator
    EffectFromTranslation: core_uobject.Vector
    TiltFromRotationYaw: float
    AccelRate: float
    DecelRate: float
    Max: core_uobject.Rotator
    Min: core_uobject.Rotator


class ViewLeadingTranslationInfo:
    Effect: core_uobject.Vector
    AccelRate: float
    DecelRate: float
    Max: core_uobject.Vector
    Min: core_uobject.Vector


class AttributeEffectData:
    AttributeToModify: GbxAttributeData
    ModifierType: engine.EGbxAttributeModifierType
    ModifierValue: AttributeInitializationData


class ChallengeInstanceData:
    CCOwner: engine.Actor
    ChallengeState: ChallengePersistentState
    ChallengeInstance: Challenge


class ChallengePersistentState:
    ChallengeClass: unreal.UClass
    ChallengeClassPath: Any
    CompletedCount: int
    CompletedProgressLevel: int
    StatInstanceState: unreal.WrappedArray[ChallengeStatInstanceData]
    bIsActive: bool
    bCurrentlyCompleted: bool
    ProgressCounter: int
    CustomPersistentData: CustomChallengePersistentState


class ChallengeStatInstanceData:
    StatId: GameStatData
    ChallengeStatPath: Any
    CurrentStatValue: int


class DataActionPair_Base:
    ActionValue: unreal.UClass


class DataActionPair_SmartObject(DataActionPair_Base):
    ActionKey: gameplay_tags.GameplayTag
    BoneSetFilter: engine.GbxBoneSet


class DataActionPair_SpawnMesh(DataActionPair_Base):
    ActionKey: gameplay_tags.GameplayTag


class DataActionPair_Spawn(DataActionPair_Base):
    ActionKey: gameplay_tags.GameplayTag


class ActorPartListData:
    PartTypeEnum: unreal.UEnum
    PartType: int
    bCanSelectMultipleParts: bool
    bUseWeightWithMultiplePartSelection: bool
    MultiplePartSelectionRange: core_uobject.Int32Interval
    bEnabled: bool
    Parts: unreal.WrappedArray[WeightedActorPartData]


class MultiSelectionGestaltPartNameData:
    IndexOfType: int
    GestaltMeshPartNames: unreal.WrappedArray[str]
    ConditionalGestaltMeshPartNames: unreal.WrappedArray[
        ConditionalMultiSelectionGestaltPartNameData
    ]


class ConditionalMultiSelectionGestaltPartNameData:
    OtherParts: unreal.WrappedArray[ActorPartData]
    GestaltMeshPartNames: unreal.WrappedArray[str]


class RuntimeActorPartListData:
    bIsInitialized: bool
    PartTypeTOC: unreal.WrappedArray[RuntimeActorPartListPartTypeData]
    AllParts: unreal.WrappedArray[WeightedActorPartData]


class RuntimeActorPartListPartTypeData:
    StartIndex: int
    NumParts: int


class ActorTagCompositeQuery:
    Queries: unreal.WrappedArray[ActorTagQuery]


class ActorTagQuery:
    bIncludeComponents: bool
    Mode: EActorTagQueryMode
    Tags: unreal.WrappedArray[str]


class AIChargeState: ...


class AIDodgeInstance:
    Action: unreal.UClass
    SourceActor: engine.Actor


class AIDodgeBasicData:
    Cooldown: GbxParam
    Action: unreal.UClass
    Condition: gbx_runtime.GbxCondition


class AIDodgeData(AIDodgeBasicData):
    Chance: GbxParam
    Delay: GbxParam
    bRemoveAllDelay: bool
    MaxAngle: float
    bLimitAngle: bool
    MaxDistance: float
    bLimitDistance: bool
    MinShooterDistance: float
    bLimitShooterDistance: bool


class AimAssistSmoothingProperties:
    LastTarget: engine.Actor
    LastTargetTeam: Team


class AimSensitivityLevelParameters:
    Index: int
    YawMaxRotationRate: float
    PitchMaxRotationRate: float
    TurningExtraYaw: float
    TurningExtraPitch: float
    TurningRampUpTime: float
    TurningRampUpDelay: float


class AIBulletEvent:
    Strength: float
    Instigator: engine.Actor


class PredictionSource: ...


class GbxAISightEvent:
    SeenActor: engine.Actor
    Observer: engine.Actor


class WeightedAnim:
    Anims: AnimMeshList
    Weight: AttributeInitializationData


class StretchAnimData:
    Actor: engine.Actor
    AnimSeq: engine.AnimSequence


class AsyncExplosionImpactRequest:
    ExplosionImpact: ImpactData
    ExplodingActor: engine.Actor
    Instigator: engine.Actor
    World: engine.World


class AsyncExplosionImpactRequestEntry: ...


class AttributePropertyValueResolverTestStruct:
    FloatProp: float
    FloatPropStaticArray: float
    FloatPropDynamicArray: unreal.WrappedArray[float]
    ObjectProp: AttributePropertyValueResolverTestContext
    ObjectPropStaticArray: AttributePropertyValueResolverTestContext
    ObjectPropDynamicArray: unreal.WrappedArray[
        AttributePropertyValueResolverTestContext
    ]


class GameStageGradeWeightData:
    MinGameStage: AttributeInitializationData
    MaxGameStage: AttributeInitializationData


class StatChallengeTest:
    StatId: GameStatData
    GoalInfo: unreal.WrappedArray[ChallengeGoalValue]
    GoalValues: unreal.WrappedArray[int]
    bUseLocalStat: bool
    bResetLocalStatWhenGoalReached: bool


class ChallengeGoalValue:
    GoalValue: int
    NotificationThreshold: int


class ChallengeDataType:
    ChallengeDataTypeEnum: unreal.UEnum
    ChallengeDataType: int


class AttributeConditionalValue:
    ValueIfAllConditionsAreTrue: AttributeInitializationData
    Conditions: unreal.WrappedArray[gbx_runtime.GbxCondition]


class ConditionalDamageDamageTypeConditional:
    Condition: gbx_runtime.GbxCondition
    DamageType: unreal.UClass


class ConditionalDamageDamageConditionalValue:
    Condition: gbx_runtime.GbxCondition
    DamageValue: AttributeInitializationData


class CMMotionData:
    X: engine.RuntimeFloatCurve
    Y: engine.RuntimeFloatCurve
    Z: engine.RuntimeFloatCurve


class DamageTargetResult:
    DamageComponent: DamageComponent
    AsyncDamagedActor: DamagedActor


class DamagedActor:
    Actor: engine.Actor
    DamageComponent: DamageComponent


class CauseDamageAsyncRequest:
    DamageData: DamageData
    DamageContext: DamageContextSource
    DamageTarget: engine.Actor


class DamageContextSource:
    SourceActor: engine.Actor
    Instigator: engine.Pawn


class CauseDamageAsyncRequestEntry(CauseDamageAsyncRequest):
    Results: unreal.WrappedArray[DamageTargetResult]


class DamageReactionEvent_DamageComponent:
    EventName: str
    HealthPool: GameResourcePoolData
    EventHealthPercent: float
    EVENTTYPE: EDamageReactionEventType
    Filter: DamageFilter
    DamageTime: float
    RetriggerDelay: float
    MaxTriggerCount: int


class SyncedHitReactionData:
    Tag: HitReactionTag
    Action: unreal.UClass
    CensoredAction: unreal.UClass
    DamageAmount: float
    Direction: engine.Vector_NetQuantizeNormal
    Force: float
    HitBoneIndex: int
    Flags: int


class SimpleHealthInfo:
    MaxHealthFormula: AttributeInitializationData
    HealthType: HealthTypeData
    MaxHealth: engine.GbxAttributeFloat
    CurrentHealth: float


class DamageDataEventDetails:
    DamageDealt: float
    DamagePerHealthType: unreal.WrappedArray[HealthTypeDamageSummary]
    DamageType: GbxDamageType
    DamageSource: DamageSource
    HitDirection: core_uobject.Vector
    HitLocation: core_uobject.Vector
    bWasCrit: bool


class DamageLocalizationSettings:
    CriticalTexture: engine.Texture2D
    ResistTexture: engine.Texture2D
    ImmuneTexture: engine.Texture2D


class ProtectionTimerSettings:
    TimerDuration: float
    Threshold: float
    MaintainedMaxHealthPct: float


class LevelBasedDamageScale:
    LevelDifference: int
    HigherLevelAttackerDmgScale: float
    LowerLevelAttackerDmgScale: float


class DamageModifierAttributeCollection:
    InstigatedModifier: GbxAttributeData
    ReceivedModifier: GbxAttributeData


class DamageOverTimeInstance:
    DamageData: DamageData


class DamageScaleConditionalData:
    bEvaluateUsingAttacker: bool
    Condition: gbx_runtime.GbxCondition
    bAddValueToDamage: bool
    DamageScale: AttributeInitializationData


class DamageSourceHealthTypeModifier:
    HealthTypeData: HealthTypeData
    InstigatedFriendlyFireHealingModifier: GbxAttributeData


class HitRegionDamagePreview:
    HitRegion: HitRegionInfo


class DynamicPhysicalAnimationTickFunction(engine.TickFunction): ...


class ExplosionImpactOverride:
    DecalOverride: engine.MaterialInterface


class DamageInfo:
    Damage: float
    DamageType: unreal.UClass
    DamageSource: unreal.UClass
    DamageRadius: float
    ImpactForce: float
    InstigatorFeedback: FeedbackData
    DamageModifierComponent: DamageModifierComponent
    DamageCauser: engine.Actor
    ActorsToIgnore: unreal.WrappedArray[engine.Actor]
    bApplyCriticalHitModsToAoEDamage: bool
    CriticalHitOverrides: CriticalHitDamageOverrides


class DamageTypeExplosionAssociation:
    DamageType: unreal.UClass
    ExplosionSizeData: ExplosionSizeSelectionData


class ExplosionSizeProperties:
    ExplosionSize: float
    ExplosionFeedback: FeedbackData
    ExplosionParticleSystem: engine.ParticleSystem
    CensoredExplosionParticleSystem: engine.ParticleSystem
    ExplosionAudioEvent: wwise_audio.WwiseEvent
    ExplosionImpact: ImpactData
    bCensorThisExplosion: bool
    bUseExplosionRadialBlur: bool
    bOverrideTinnitusDuration: bool
    ExplosionRadialBlur: engine.RadialBlurSelection
    TinnitusDuration: EExplosionTinnitusDuration
    SignificanceEvent: GbxSignificanceEvent


class FeedbackDataFirstPersonImpulse:
    bUseDurationFromCameraShake: bool
    CameraShakeDurationEaseInWeight: float
    EaseInDuration: float
    EaseOutDuration: float
    EaseInFunc: GbxEasingFunc
    EaseOutFunc: GbxEasingFunc
    RandomRotationOffset: core_uobject.Rotator
    RotationExtent: core_uobject.Rotator
    bOffsetRotationByDirection: bool
    RandomTranslationOffset: core_uobject.Vector
    TranslationExtent: core_uobject.Vector
    ZoomedEffectScale: float


class LoopingShakeInfo:
    AssociatedController: engine.PlayerController
    Scale: float
    ContextObject: unreal.UObject
    TimerHandle: engine.TimerHandle
    FeedbackLocation: core_uobject.Vector


class ShakeScaleAssociation:
    CameraShake: unreal.UClass
    BaseScale: AttributeInitializationData
    bContinuous: bool
    bScaleDownOverTime: bool
    bUseScaleOverTimeCurve: bool
    ScaleOverTimeCurve: engine.RuntimeFloatCurve
    ContinuousScale: AttributeInitializationData
    ContinuousScaleCurve: engine.RuntimeFloatCurve


class HapticFeedbackData:
    HapticFeedbackEffect: engine.HapticFeedbackEffect_Curve
    Hand: input_core.EControllerHand


class FeedbackTableRowHandle(engine.DataTableRowHandle): ...


class FeedbackAssociationRow(engine.TableRowBase):
    Feedback: FeedbackData


class TrackedFirstPersonComponent:
    Component: engine.SceneComponent


class GameplayTagToValueMap:
    Tag: gameplay_tags.GameplayTag
    ValueIfContextHasTag: AttributeInitializationData


class GameResourcePool:
    ResourcePoolData: GameResourcePoolData
    MinValue: engine.GbxAttributeFloat
    MaxValue: engine.GbxAttributeFloat
    PercentOfMaxValueReserved: engine.GbxAttributeFloat
    ConsumptionRate: engine.GbxAttributeFloat
    ActiveRegenerationRate: engine.GbxAttributeFloat
    OnIdleRegenerationRate: engine.GbxAttributeFloat
    OnIdleRegenerationDelay: engine.GbxAttributeFloat
    OnDepletedIdleRegenerationDelay: engine.GbxAttributeFloat
    PassiveRegenerationRate: engine.GbxAttributeFloat
    PassivePercentRegenerationRate: engine.GbxAttributeFloat
    PassiveMissingPercentRegenerationRate: engine.GbxAttributeFloat
    RegenerationDisabled: engine.GbxAttributeInteger
    CurrentValue: float
    LastTotalRegenerationRateValue: float
    LastTotalPercentRegenerationRateValue: float
    LastEffectiveMaxValue: float
    PostAddedRegenerationRate: engine.GbxAttributeFloat
    PostAddedPercentRegenerationRate: engine.GbxAttributeFloat


class GameResourceUserEvent:
    ResourceData: GameResourceData
    OnResourceNowDepleted: Any
    OnResourceNowNotDepleted: Any
    OnResourceNowFilled: Any
    OnResourceNowNotFilled: Any
    OnResourceNowRegenerating: Any
    OnResourceNowNotRegenerating: Any
    OnResourceNowDepleting: Any
    OnResourceNowNotDepleting: Any
    OnResourceNowIdle: Any


class GameResourcePoolNet:
    Manager: GameResourcePoolManagerComponent


class GameStat:
    GameStat: GameStatData
    StatValue: int


class QueuedGameStatEvent:
    StatContext: engine.Actor
    GameStat: GameStatData


class ActionState_AICharge(ActionState_SimpleAnim): ...


class ExtraAnimationSettings:
    SkeletalMeshComponentName: str
    AnimDef: AnimActionDef
    AnimSlotOverride: str
    bHasAnimSlotOverride: bool


class ActionState_BlueprintBase(ActionState_Base): ...


class ConditionActionPair:
    Condition: gbx_runtime.GbxCondition
    ActionClass: unreal.UClass


class CoordinatedAppliedMesh: ...


class CoordinatedLightParameterData:
    LightName: str
    bSetColor: bool
    bSetIntensity: bool
    Color: CoordinatedVectorParameter
    Intensity: CoordinatedScalarParameter


class CoordinatedScalarParameter:
    ParamName: str
    ParamValueOverTime: engine.RuntimeFloatCurve
    ScaleMode: ECoordinatedEffectParamScaleMode
    WorldSpaceAxis: int
    bLoop: bool
    bBlendFromInitialValue: bool
    BlendCurve: engine.RuntimeFloatCurve
    bApplyAttribute: bool
    bScaleAttributeByValueOverTime: bool
    ParamAttributeValue: AttributeInitializationData
    bSpecificMaterial: bool
    SpecificMaterialList: unreal.WrappedArray[int]


class CoordinatedVectorParameter:
    ParamName: str
    ParamValueOverTime: engine.RuntimeCurveLinearColor
    bLoop: bool
    bBlendFromInitialValue: bool
    bBlendUsingHSV: bool
    BlendCurve: engine.RuntimeFloatCurve
    bSpecificMaterial: bool
    SpecificMaterialList: unreal.WrappedArray[int]


class CoordinatedConditionalMaterialData:
    BaseMaterial: engine.Material
    MeshElementIndex: int
    OverrideMaterial: engine.MaterialInterface
    bMatchMaterialStaticParameters: bool
    bUseGlobalInheritedMaterialParameters: bool
    bInheritAllMaterialParameters: bool
    InheritedMaterialParameters: unreal.WrappedArray[str]


class CoordinatedAudioData:
    WwiseEvent: wwise_audio.WwiseEvent
    AttachmentName: str
    StartTime: float
    DeactivateTime: float
    RtpcParam: wwise_audio.WwiseRtpc
    RtpcValueOverTime: engine.RuntimeFloatCurve


class CoordinatedParticleSystemParameterData:
    Name: str
    ParticleSystem: engine.ParticleSystem
    ScalarParameters: unreal.WrappedArray[CoordinatedScalarParameter]
    VectorParameters: unreal.WrappedArray[CoordinatedVectorParameter]


class CoordinatedParticleSystemData:
    ParticleSystem: engine.ParticleSystem
    RelativeTransform: core_uobject.Transform
    AttachmentName: str
    StartTime: float
    DeactivateTime: float
    ScalarParameters: unreal.WrappedArray[CoordinatedScalarParameter]
    VectorParameters: unreal.WrappedArray[CoordinatedVectorParameter]
    ScaleMode: ECoordinatedParticleScaleMode
    bOnlyPlayerOwnerCanSee: bool
    bForegroundLayer: bool
    bInheritViewFlags: bool
    bPermanent: bool


class DirectionActionData:
    AngleRange: gbx_runtime.NumericRange
    ActionClass: unreal.UClass


class ActionState_DropshipSpawn(ActionState_SimpleAnim): ...


class GibData:
    MaxCount: int
    SelectionWeight: float
    bOverrideGlobalScale: bool
    MinScale: float
    MaxScale: float
    Mesh: unreal.UObject
    MaterialOverride: engine.MaterialInstanceConstant


class ActionState_Launch(ActionState_SimpleAnim): ...


class LoopAnimData:
    AnimStart: engine.AnimSequenceBase
    AnimLoop: engine.AnimSequenceBase
    AnimStop: engine.AnimSequenceBase


class ActionState_Ragdoll(ActionState_SimpleAnim): ...


class AttachedObjectCache: ...


class AttachedObjectFollow:
    ObjectBoneName: str
    ObjectHoldBoneName: str
    ObjectHoldBodyName: str


class MotionMatchedAnimationRow(GbxAnimTableRow):
    Forward: core_uobject.Vector
    Up: core_uobject.Vector
    Velocity: core_uobject.Vector
    AngularVelocity: core_uobject.Vector
    OverrideForward: core_uobject.Vector
    bOverrideForward: bool
    OverrideUp: core_uobject.Vector
    bOverrideUp: bool
    RootBoneToRootBodyOffset: float
    OffsetCalculationAxis: int
    bOffsetCalculationAxisIsNegative: bool
    SampleTime: float
    PoseDriverStrength: float


class RandomActionPair:
    ActionClass: unreal.UClass
    Weight: float


class ActionState_StretchBones(ActionState_SimpleAnim): ...


class StretchBonesSettings:
    bUniformStretch: bool
    TargetKey: GbxBlackboardKeySelector
    TargetOffset: core_uobject.Vector
    ActorTrackingStyle: EStretchBonesActorTrackingStyle
    bTraceToGround: bool
    TraceToGroundDistance: float
    MaxPredictionDistance: float


class DataActionPair(DataActionPair_Base):
    ActionKey: gameplay_tags.GameplayTag


class ExampleStruct:
    ActionKey: gameplay_tags.GameplayTag


class ActionStateNet: ...


class GbxActionRegister:
    Name: str
    Type: EActionRegisterType
    Value: float
    IntValue: int
    ObjectValue: unreal.UObject
    NameValue: str
    VecValue: core_uobject.Vector


class GbxActionSlot:
    Name: str


class ForwardDynamicsNodeProfile:
    ForwardDynamicsProfile: PhysicalAnimationProfileAsset
    ForwardDynamicsActivation: EForwardDynamicsActivation
    PhysicsAssetStrengthDefinitionProfileName: str
    TargetSimulationFrequency: int
    MaxSubstepCount: int
    MaxTranslationDistanceUntilReset: float
    LinearJointDivergentTolerence: float
    WorldSpaceVelocityBlend: float
    WorldSpaceAngularVelocityBlend: float
    bBypassSkelMeshSimulatePhysOption: bool
    bStripAnimationFromNonSimulationRelevantBones: bool
    OverridePhysicsAsset: engine.PhysicsAsset
    OverrideWorldGravity: core_uobject.Vector
    ExternalForce: core_uobject.Vector
    OverlapChannel: int
    bEnableWorldGeometry: bool
    SimulationSpace: immediate_physics.ESimulationSpace
    bOverrideWorldGravity: bool
    CachedBoundsScale: float
    bTransferBoneVelocities: bool
    bFreezeIncomingPoseOnStart: bool
    LODThreshold: int
    LODInterpolationSpeed: float


class GbxAnimNode_ApplyBoneModifyProfile(
    anim_graph_runtime.AnimNode_SkeletalControlBase
):
    Config: GbxBoneModifyProfile


class GlobalBMPCachedTransform: ...


class GbxAnimNode_CachedPoseBlend(anim_graph_runtime.AnimNode_SkeletalControlBase): ...


class GbxAnimNode_ForwardDynamics(immediate_physics.AnimNode_RigidBody):
    ForwardDynamicsProfile: PhysicalAnimationProfileAsset
    ForwardDynamicsActivation: EForwardDynamicsActivation
    PhysicsAssetStrengthDefinitionProfileName: str
    TargetSimulationFrequency: int
    MaxSubstepCount: int
    MaxTranslationDistanceUntilReset: float
    WorldSpaceVelocityBlend: float
    WorldSpaceAngularVelocityBlend: float
    JointAnchorPoseAlpha: float
    LinearJointDivergentTolerence: float
    bBypassSkelMeshSimulatePhysOption: bool
    bStripAnimationFromNonSimulationRelevantBones: bool


class GbxAnimNode_RefPoseConstraints(anim_graph_runtime.AnimNode_SkeletalControlBase):
    Constraints: unreal.WrappedArray[GbxRefPoseBoneConstraint]


class GbxRefPoseBoneConstraint:
    Bone: engine.BoneReference
    Weight: float


class GbxAnimNode_SimpleMotionBoneControl(
    anim_graph_runtime.AnimNode_SkeletalControlBase
):
    ControlValue: float
    bIsActive: bool
    bAutoActivate: bool
    bPaused: bool
    bActivateAfterRecovery: bool
    BoneToModify: engine.BoneReference
    IdleSpeedControlValue: float
    ActiveSpeedControlValue: float
    RecoverySpeedControlValue: float
    TranslationMode: int
    TranslationSpace: int
    IdleTranslation: core_uobject.Vector
    ActiveTranslation: core_uobject.Vector
    IdleTranslationState: SimpleMotionState
    ActiveTranslationState: SimpleMotionState
    RecoveryTranslationState: SimpleMotionState
    RotationMode: int
    RotationSpace: int
    IdleRotation: core_uobject.Rotator
    ActiveRotation: core_uobject.Rotator
    IdleRotationState: SimpleMotionState
    ActiveRotationState: SimpleMotionState
    RecoveryRotationState: SimpleMotionState
    ScaleMode: int
    ScaleSpace: int
    IdleScale: core_uobject.Vector
    ActiveScale: core_uobject.Vector
    IdleScaleState: SimpleMotionState
    ActiveScaleState: SimpleMotionState
    RecoveryScaleState: SimpleMotionState
    ControlImpulseSpeed: float
    ControlImpulseMaxValue: float
    ControlImpulseDecayDelay: float
    ControlImpulseDecaySpeed: float


class SimpleMotionState:
    MotionType: ESimpleMotionType
    MinSpeed: float
    MaxSpeed: float
    SpeedControlCurve: engine.CurveFloat
    Acceleration: float
    bScaleTransformByValue: bool
    bScaleSpeedByValue: bool
    bScaleAccelerationByValue: bool


class GbxAnimNode_StretchBones(anim_graph_runtime.AnimNode_SkeletalControlBase):
    StartBone: engine.BoneReference
    EndBone: engine.BoneReference
    bUniformStretch: bool
    AnimatedTargetDistance: float
    EndAnimatedTargetDistance: float
    TargetOffset: core_uobject.Vector
    bUsingStretchDistance: bool
    StretchDistance: float
    bTraceToGround: bool
    TraceToGroundDistance: float
    MarkerMode: EStretchBonesMarkerMode
    BoneToModify: engine.BoneReference
    LookAtBone: engine.BoneReference
    LookAtSocket: str
    LookAtLocation: core_uobject.Vector
    LookAt_Axis: animation_core.AXIS
    EndLookAt_Axis: animation_core.AXIS
    bUseLookUpAxis: bool
    LookUp_Axis: animation_core.AXIS
    LookAtClamp: float
    InterpolationType: int
    InterpolationTime: float
    InterpolationTriggerThreashold: float


class GbxAnimPoseMatch:
    PoseMatchBones: unreal.WrappedArray[str]


class AnimStateGroup:
    GroupName: str
    States: unreal.WrappedArray[str]


class RuntimeStateMachineData: ...


class BakedMachineInfo: ...


class GbxAnimTableMapItem:
    bCanUse: bool
    LastFrame: int


class StartupAssetTypeData:
    Path: str
    ClassType: core_uobject.SoftObjectPath
    ResolvedClassType: unreal.UClass
    bBlueprint: bool
    AssetCategory: str


class GbxAttributeDelegateBindingHandle: ...


class PropertyToAttributeMapping:
    PropertyName: str
    PropertyGuid: core_uobject.Guid
    AttributeDataReference: core_uobject.SoftObjectPath


class BoneModifyProfileData:
    Profile: GbxBoneModifyProfile
    States: unreal.WrappedArray[BoneModifyState_RepData]


class BoneModifyState_RepData:
    bActive: bool
    Alpha: float
    BlendTime: float


class BoneModifyState:
    Name: str
    PoseMode: EGbxBoneModifyProfile_PoseMode
    bStartActive: bool
    Blend: engine.AlphaBlend
    Bones: unreal.WrappedArray[BoneModifyInfo]


class BoneModifyInfo:
    BoneName: str
    Translation: core_uobject.Vector
    Rotation: core_uobject.Rotator
    Scale: core_uobject.Vector


class BoneModifyTransition:
    BoneRef: engine.BoneReference
    Type: EBoneModifyTransition_TransformType
    Blend: engine.AlphaBlend
    Base: core_uobject.Vector
    Desired: core_uobject.Vector


class MantleCheckData: ...


class MantleCheckTypeData: ...


class MantleCheckTypeData_MantleUp(MantleCheckTypeData): ...


class MantleStandData: ...


class DistanceMatchingInfo:
    DistanceCurveMap: Any


class StopDistanceMatchingInfo(DistanceMatchingInfo):
    StoppingInfoMap: Any


class CachedStoppingInfo: ...


class MaterialArray:
    Materials: unreal.WrappedArray[engine.MaterialInterface]


class CustomizationTextureInheritanceSettings:
    OnlyInheritCustomizationTextureParameters: unreal.WrappedArray[str]
    BaseMaterial: engine.MaterialInterface
    CustomizationTargetSpecificBaseMaterials: unreal.WrappedArray[
        CustomizationInheritedTextureBaseMaterial
    ]
    ExtraParams: unreal.WrappedArray[InheritedCustomizationTextureExtraParam]


class InheritedCustomizationTextureExtraParam:
    Target: GbxCustomizationTargetData
    ParamName: str
    Texture: engine.Texture


class CustomizationInheritedTextureBaseMaterial:
    Target: GbxCustomizationTargetData
    MaterialIndex: int
    BaseMaterial: engine.MaterialInterface


class CustomizationColorApplication:
    bUseDefaultColor: bool
    bUseDefaultSplitColor: bool
    bSupportsSplitColor: bool
    AppliedColor: core_uobject.Vector
    SplitColor: core_uobject.Vector
    DefaultColor: core_uobject.Vector
    DefaultSplitColor: core_uobject.Vector


class CustomizationLinkedParameterEntry:
    LinkedParameters: unreal.WrappedArray[CustomizationLinkedParameter]
    LinkedParameterSource: GbxCustomizationTargetData
    LinkedParameterTarget: GbxCustomizationTargetData
    LinkedParameterTargets: unreal.WrappedArray[GbxCustomizationTargetData]


class CustomizationColorEntry:
    ColorCustomizationTargets: unreal.WrappedArray[GbxCustomizationTargetData]
    ColorCustomizationParameter: str
    SplitColorCustomizationParameter: str
    ColorCustomizationDisplayName: str


class GbxCustomizationContainer(engine.FastArraySerializer):
    Customizations: unreal.WrappedArray[GbxCustomizationContainerEntry]
    CustomizationCache: unreal.WrappedArray[GbxCustomizationCacheEntry]
    Owner: GbxCustomizationComponent


class GbxCustomizationCacheEntry:
    AssetRefs: unreal.WrappedArray[unreal.UObject]
    CustomizationData: GbxCustomizationData


class GbxCustomizationContainerEntry(engine.FastArraySerializerItem):
    CustomizationData: GbxCustomizationData
    OptionalCustomizationId: int
    ClientCachedCustomizationData: GbxCustomizationData


class CustomizationAssetEntry:
    CustomizationTarget: GbxCustomizationTargetData
    CustomizationAssetReferences: unreal.WrappedArray[core_uobject.SoftObjectPath]
    CustomizationAssetInfoReferences: unreal.WrappedArray[CustomizationAssetInfo]
    CustomizationClassReferences: unreal.WrappedArray[core_uobject.SoftClassPath]
    LoadForPreview: bool


class CustomizationAssetInfo:
    AssetReferenceTargetName: str
    AssetReference: core_uobject.SoftObjectPath


class CustomizationStreamingEntry:
    CustomizationData: GbxCustomizationData
    WaitingComponents: unreal.WrappedArray[GbxCustomizationComponent]


class DamageSurfaceModifier:
    PhysicalSurface: EDamageSurfaceType
    Modifier: AttributeInitializationData


class GbxBlueprintlegateBinding:
    SubobjectPath: str
    ParsedDelegateOwnerPath: engine.ParsedProperty
    ParsedDelegatePath: engine.ParsedProperty
    FunctionNameToBind: str


class ActiveGbxFeedbackEffect:
    ActiveData: GbxFeedbackData
    Controller: GbxPlayerController
    SourceContext: unreal.UObject


class GbxFlag: ...


class GbxFlagEval:
    FlagData: GbxFlagData
    EvalType: EGbxFlagEval
    TimeSeconds: AttributeInitializationData


class FlagPropertyTestStruct:
    TestFlag: GbxFlag


class SharedPickupInventoryActor:
    Actor: engine.Actor


class MenuStash:
    StashedMenus: unreal.WrappedArray[BaseMenuStackMenuInfo]


class DefaultExplosionSettings:
    ExplosionSize: float
    RadialBlur: engine.RadialBlurSelection


class GbxHUDFeedbackImpulse:
    Velocity: core_uobject.Vector
    RotationalVelocity: float
    Springiness: float
    Damping: float
    bCircularMotion: bool
    bApplyCameraTranslation: bool
    CameraTranslationWeight: float
    bApplyCameraRotation: bool
    CameraRotationWeight: float
    bApplyOriginWorldSpace: bool
    OriginWorldSpace: core_uobject.Vector
    OriginWorldSpaceWeight: float
    Tag: str


class GbxObjectReplicatorProxy:
    Items: unreal.WrappedArray[GbxObjectReplicatorProxyItem]


class GbxObjectReplicatorProxyItem:
    Object: Any
    Component: engine.ActorComponent


class RigidBodyImpactSettings:
    RigidBodyImpactData: Any
    DefaultRigidBodyImpactData: Any
    ImpactSpeedAudioParameter: wwise_audio.WwiseRtpc
    ImpactMassAudioParameter: wwise_audio.WwiseRtpc


class PhysicalMaterialImpactPair:
    MaterialA: engine.PhysicalMaterial
    MaterialB: engine.PhysicalMaterial


class DestructionForceSmoothing:
    MaxResultantVelocity: float
    NormalizationFactor: float
    GlobalScale: float


class SurfaceTypeInfo:
    DamageSurfaceType: EDamageSurfaceType
    AudioMaterialSwitch: wwise_audio.WwiseSwitch


class RecentlyMetPlayer:
    FirstPartyPlayerId: engine.UniqueNetIdRepl
    ShiftPlayerId: engine.UniqueNetIdRepl
    bUseShiftId: bool


class PlayerInputBindings:
    Categories: unreal.WrappedArray[PlayerInputBinding_Category]


class PlayerInputBinding_Category:
    CategoryDataPath: str
    ContextDataPath: str
    ButtonBindings: unreal.WrappedArray[PlayerInputBinding_Button]
    AxisBindings: unreal.WrappedArray[PlayerInputBinding_Axis]


class PlayerInputBinding_Axis:
    RebindDataPath: str
    Keys: unreal.WrappedArray[PlayerInputBinding_Axis_Key]


class PlayerInputBinding_Axis_Key:
    KeyName: str
    Scale3D: core_uobject.Vector


class PlayerInputBinding_Button:
    RebindDataPath: str
    KeyNames: unreal.WrappedArray[str]


class GbxQuery:
    Owner: engine.Actor
    Params: EnvQueryParams
    Options: GbxQueryOptions
    PrimaryContext: engine.Actor
    BlackboardComp: aimodule.BlackboardComponent
    NavComp: NavComponent


class GbxSignificanceEventData:
    bTestVisibility: bool
    AlwaysSignificantDistance: float
    MaxDistance: float
    MinScreenPercent: float
    DistantThreshold: float
    PlayerSourceInfluence: float


class CachedInterp:
    Tag: str
    Interp: str


class SimpleMotionInstanceState:
    Speed: float
    bMotionReversed: bool
    bReachedTarget: bool
    bReachedMaxSpeed: bool
    bInTransition: bool


class GestaltPartFoleyAccessory:
    Priority: int
    WwiseEvent: wwise_audio.WwiseEvent
    AttachmentPoint: str


class GestaltChildPartData:
    GestaltPart: GestaltPartData
    Probability: float


class GestaltRandomPartData:
    GestaltPart: GestaltPartData
    Weight: float


class ReplicatedGestaltPartsData: ...


class GesaltOptionalPartData:
    GestaltPart: GestaltPartData
    Probability: float
    bSuppressChildParts: bool


class BMPOverride:
    Bones: unreal.WrappedArray[BMPOverrideBone]
    PoseMode: EGlobalBoneModifyProfile_PoseMode


class BMPOverrideBone:
    BoneRef: engine.BoneReference
    Scale: float


class HitReactionPair:
    Tag: HitReactionTag
    Action: unreal.UClass


class HitReactionCondition:
    Condition: gbx_runtime.GbxCondition
    Context: EHitReactionConditionContext
    OptionalContext: EHitReactionConditionContext


class HitReactionCooldownData:
    Tag: HitReactionTag
    Cooldown: float
    TagFallback: HitReactionTag
    bCooldownFromStartTime: bool


class HitReactionMapItem:
    FromTag: HitReactionTag
    ToTag: HitReactionTag


class HitReactionParams:
    Receiver: DamageComponent
    Causer: DamageCauserComponent
    DamageAmount: float
    DamageType: GbxDamageType
    DamageSource: DamageSource
    Direction: core_uobject.Vector
    Force: float
    HitRegion: HitRegionData
    HitBoneIndex: int
    HitLocation: core_uobject.Vector
    bIgnoreCooldowns: bool
    bForceInterruptSelf: bool


class HitReactionState:
    HitReactionData: HitReactionData
    NoLockTags: unreal.WrappedArray[HitReactionTag]
    BackupDeathTag: HitReactionTag
    DefaultDeathAction: unreal.UClass
    bCensorDeaths: bool
    CurrHitReactionData: HitReactionData
    DamageComp: DamageComponent
    DodgeComp: AIDodgeComponent
    ActionComp: GbxActionComponent
    BrainComp: aimodule.BrainComponent
    DeathOverrideId: str
    DeathOverride: HitReactionTag
    LiveLayers: unreal.WrappedArray[unreal.UClass]
    DeathLayers: unreal.WrappedArray[unreal.UClass]
    TagTimeStartMap: Any
    TagTimeEndMap: Any
    ActiveTag: HitReactionTag
    Hits: unreal.WrappedArray[HitReactionParams]
    SoundCharacter: GbxCharacter


class HitRegionState:
    HitRegion: HitRegionData
    AssociatedComponentNames: unreal.WrappedArray[str]
    DamageEvents: unreal.WrappedArray[DamageReactionEvent]
    StateIndex: int
    AssociatedPrimitives: unreal.WrappedArray[engine.PrimitiveComponent]
    AssociatedChildActorComponents: unreal.WrappedArray[engine.ChildActorComponent]
    MaxHealth: float
    CurrentHealth: float
    ResourcePool: GameResourcePoolReference


class DamageReactionEvent:
    EventName: str
    EventHealthPercent: float
    EVENTTYPE: EDamageReactionEventType
    Filter: DamageFilter
    DamageTime: float
    RetriggerDelay: float
    MaxTriggerCount: int
    DamageBoneName: str
    bIncludeDamageBoneChildren: bool
    bCensored: bool
    bTriggerOnlyOnDeath: bool


class HitRegionHealthParams:
    OwnerHealthPercent: float
    ResourcePool: GameResourcePoolData
    DamageRule: EHitRegionDamageRule


class HomingTargetedActorInfo:
    Target: engine.Actor
    ProjectileCount: int


class InspectionInfo: ...


class ImpactTriggerInfo:
    RigidBodyRefireDelay: float
    RigidBodyMinimumVelocity: float


class ImpactEffectEventInfo:
    InstigatorActor: engine.Actor
    HitActor: engine.Actor
    HitMaterial: engine.PhysicalMaterial


class ImpactFXManagerTrackingData:
    Component: engine.SceneComponent
    PhysicalMaterial: engine.PhysicalMaterial


class InstigatorAttributeEffectData(AttributeEffectData):
    AttributeToModifyContextSource: (
        EInstigatorAttributeEffectAttributeToModifyContextSource
    )
    ModifierValueContext: EInstigatorAttributeEffectModifierValueContext


class MantleActionData:
    Type: EMantleType
    Animation: unreal.UClass
    HeightMinimum: float
    AlignTime: float
    HorizontalCurve: engine.RuntimeFloatCurve
    VerticalCurve: engine.RuntimeFloatCurve
    PercentThroughAnimationToFinishMantle: float
    bAlignRotation: bool
    bMustLookAt: bool


class MantleGlobalData:
    DistanceToLookAheadForWalls: int
    FootCollisionHeight: float
    HeadCollisionHeight: float
    MinWallSlope: float
    MaxAngleToKeepMantleCache: float
    TimeToHoldValidClimbLocationSeconds: float
    MaxDegreeAngleFromForward: float
    LookAngleRange: float
    bShowPromptWhenAvailable: bool
    DelayBeforeShowingPrompt: float
    ValidActorClasses: unreal.WrappedArray[unreal.UClass]
    InvalidActorClasses: unreal.WrappedArray[unreal.UClass]
    ValidPrimitiveComponentClasses: unreal.WrappedArray[unreal.UClass]
    ValidMovementModes: unreal.WrappedArray[int]
    MaxAscendingSpeedZ: float
    MaxDescendingSpeedZ: float
    MinLedgeHeightToStillAllowMantle: float
    MaxPossibleLedgeHeight: float
    MaxPossibleLedgeDistance: float
    ClientValidationTolerance: float
    MinPassiveMantleHeight_Default: float
    MinPassiveMantleHeight_ForwardInput: float
    bIgnoreTeamCollision: bool


class ModifierMathAttributeValueResolverStackEntry:
    ModifierType: engine.EGbxAttributeModifierType
    ModifierValue: AttributeInitializationData


class MontageLoopHelper: ...


class MontageLoopRecord: ...


class OrbitOscillationInfo:
    Cycle: engine.RuntimeFloatCurve
    OverrideDuration: float
    CurrentTime: float


class PawnAttachmentQueryResult:
    Pawn: engine.Pawn
    SlotName: str
    AttachBase: engine.Actor


class AttachSlotAnimSet:
    AssociatedCharacter: Any
    AnimSet: engine.GbxAnimSet


class PawnAttachmentTransition:
    BaseAction: unreal.UClass
    PawnAction: unreal.UClass
    bForceStopTransitionActions: bool
    AttachTiming: EAttachmentTransitionTiming
    bOverrideAttachInfo: bool
    AttachInfo: PawnSceneAttachmentInfo
    Conditions: gbx_runtime.GbxCondition


class PawnSceneAttachmentInfo:
    bAttachToBaseOwner: bool
    bMaintainWorldLocation: bool
    bApplyMeshOffset: bool
    SocketName: str
    AttachOffset: core_uobject.Vector
    bAddOffsetFromSocket: bool
    SocketNameForAdditionalOffset: str


class PawnDetachTransition(PawnAttachmentTransition):
    bValidateDetachLocation: bool
    ValidationMaxOffset: float
    ValidationToleranceSize: float
    bComputeDetachLocationFromAction: bool
    bAbsoluteDetachLocation: bool
    DetachLocationOffset: core_uobject.Vector


class PawnAttachTransition(PawnAttachmentTransition): ...


class PawnAttachSlotState:
    Owner: PawnAttachSlotComponent
    Pawn: engine.Pawn
    Controller: engine.Controller
    Status: EPawnAttachStatus
    bSkipDetachPlacement: bool
    bSkipStopTransitionAction: bool
    DetachTransitionIndex: int


class PhysicalAnimationBoneData:
    BodyName: str
    bIncludeChildren: bool
    bIsLocalSimulation: bool
    OrientationStrength: float
    AngularVelocityStrength: float
    PositionStrength: float
    VelocityStrength: float


class BoneFatigueParams:
    CurrentFatigue: float
    FatigueDissipationRate: float


class PropertyUtilsTestStruct:
    FloatProp: float
    FloatPropStaticArray: float
    FloatPropDynamicArray: unreal.WrappedArray[float]
    ObjectProp: PropertyUtilsTestContext
    ObjectPropStaticArray: PropertyUtilsTestContext
    ObjectPropDynamicArray: unreal.WrappedArray[PropertyUtilsTestContext]
    DoubleProp: float
    Int8Prop: int
    UInt8Prop: int
    Int16Prop: int
    UInt16Prop: int
    Int32Prop: int
    UInt32Prop: int
    Int64Prop: int
    UInt64Prop: int


class RagdollReplicationData:
    Bodies: unreal.WrappedArray[ArticulatedRigidBodyState]


class ArticulatedRigidBodyState(engine.RigidBodyState):
    BodyName: str


class RecentlyCausedDamageInstance:
    DamageType: unreal.UClass
    DamageSource: unreal.UClass
    DamageLocation: engine.Vector_NetQuantize
    TotalDamage: float
    DirtyCounter: int
    HitRegion: HitRegionData
    DamageFlags: ERecentDamageFlags
    DamagedActor: engine.Actor


class ReferenceActorClasses:
    Name: str
    ActorAsset: core_uobject.SoftObjectPath


class RelativeDirectionData:
    RelativeDirection: ERelativeDirectionType
    ConeAroundDirection: AttributeInitializationData
    AdditionalRotation: core_uobject.Rotator


class EmitterWwiseEvent:
    ParamsProvider: unreal.UObject
    Event: wwise_audio.WwiseEvent
    RTPCs: unreal.WrappedArray[EmitterWwiseEventRTPCParam]
    Switches: unreal.WrappedArray[wwise_audio.WwiseSwitch]
    PlaybackLocation: core_uobject.Vector


class EmitterWwiseEventRTPCParam:
    RTPC: wwise_audio.WwiseRtpc
    Value: float


class EmitterColorParam:
    Name: str
    Value: core_uobject.Color


class EmitterVectorParam:
    Name: str
    Value: core_uobject.Vector


class EmitterFloatParam:
    Name: str
    Value: float


class ReplicatedEmitterTemplateOptions:
    DefaultTemplate: engine.ParticleSystem
    CensoredTemplate: engine.ParticleSystem
    bEligibleForCensoring: bool


class SceneComponentSwitchRecord:
    Component: engine.SceneComponent
    ParentComponent: engine.SceneComponent
    DetachAction: SceneBodySwitchAction


class ScreenParticleInitParams:
    Template: engine.ParticleSystem
    bHideWhenFinished: bool
    bDestroyWhenFinished: bool
    bOnlyOwnerSee: bool
    bAlwaysVisible: bool
    bAllowMultipleInstances: bool
    bTickEvenWhenPaused: bool
    bHideDuringInGameMenu: bool
    bDepthPriorityWorld: bool
    ContentDims: core_uobject.Vector2D
    ParticleDepth: float
    ScalingMode: EScreenParticleScalingMode
    Tag: str
    OwnerOverride: engine.Actor


class ParticlePropertyTracker:
    TrackingData: ParticlePropertyTrackingData
    Template: engine.ParticleSystem
    Tag: str
    PropertyName: str
    FloatParamValue: float
    LastUpdateTime: float
    Material: engine.MaterialInstanceDynamic
    MaterialPropertyName: str


class ScreenParticleRecord:
    Template: engine.ParticleSystem
    Component: engine.ParticleSystemComponent


class SharedAnimInstanceData: ...


class SpawnPatternInputs:
    SourceActor: engine.Actor
    SocketName: str
    BaseLocation: core_uobject.Vector
    BaseRotation: core_uobject.Rotator
    IncomingImpulse: core_uobject.Vector


class StanceVectorValue:
    ValueType: EStanceValueOverrideType
    Value: core_uobject.Vector


class ConditionalStance:
    Condition: gbx_runtime.GbxCondition
    StanceProvider: StanceDataProvider


class StanceStack:
    Owner: engine.Actor
    Top: EStanceStackLayer
    Stack: StanceDataProvider
    LayerCurr: EStanceStackLayer
    StanceCurr: StanceData


class BalanceFormulaDefinedValueRow(AttributeDefinedValueRow):
    Multiplier: AttributeInitializationData
    Level: AttributeInitializationData
    Power: AttributeInitializationData
    Offset: AttributeInitializationData
    Scalar: AttributeInitializationData


class RandomValueRow(AttributeDefinedValueRow):
    RNG_LowerBound: AttributeInitializationData
    RNG_UpperBound: AttributeInitializationData
    bIntegerOnlyValues: bool
    OptionalOutputMinValue: AttributeInitializationData
    bClampToOutputMinValue: bool
    OptionalOutputMaxValue: AttributeInitializationData
    bClampToOutputMaxValue: bool


class GbxParamDefinedSingleValueRow(AttributeDefinedValueRow):
    Value: GbxParam


class AttributeDefinedSingleValueRow(AttributeDefinedValueRow):
    Value: AttributeInitializationData


class AttributeEffect:
    AttributeData: GbxAttributeData
    ModifierType: engine.EGbxAttributeModifierType
    BaseModifierValue: AttributeInitializationData
    Mutator: AttributeEffectMutatorData


class AttributeEffectValueContextHardRef:
    Context: unreal.UObject
    ContextResolverOverride: unreal.UObject


class StatusEffectStackingStrategyData_DurationRefundData:
    bApplyReplacementRefund: bool
    RefundPercent: float


class StretchBonesInstance:
    StartBoneName: str
    EndBoneName: str
    bUniformStretch: bool
    TargetActor: engine.Actor
    TargetPosition: core_uobject.Vector
    Distance: float


class OverrideMeleeSocket:
    OverrideCondition: gbx_runtime.GbxCondition
    OverrideSockets: unreal.WrappedArray[str]


class TargetLocationData:
    TargetLocation: core_uobject.Vector
    TargetBoundsCenter: core_uobject.Vector
    TargetBoundsRadius: float
    TargetBoundsHalfHeight: float


class TargetLocationBoundsSettings:
    BoundsRadius: float
    BoundsHalfHeight: float
    bUseBoundsHalfHeight: bool


class TargetLocationSettings(TargetLocationBoundsSettings):
    Enabled: GbxParam
    Socket: str


class TargetActorInfo:
    Target: engine.Actor
    Proxy: engine.SceneComponent
    TargetableComponent: TargetableComponent
    OwnerTargetingComponent: TargetingComponent
    TargetScore: float
    AttitudeTowardTarget: int
    AttitudeFromTarget: int
    TargetListIndex: int


class TargetQueryTestDebugDesc:
    Value: float
    Score: float


class TargetQueryDebugDesc:
    DebugGroup: str
    Actor: engine.Actor
    Team: Team
    Score: float
    FailReason: str


class TeamAttitudeSetEntry:
    OtherTeam: Team
    Attitude: int


class TerritoryData:
    bEverywhere: bool
    Radius: float
    Height: float
    Volumes: unreal.WrappedArray[engine.Volume]


class TargetPersistentNotes: ...


class UIStatValueRemappingData:
    bUseContextOverride: bool
    InputValueMin: AttributeInitializationData
    InputValueMax: AttributeInitializationData
    OutputValueMin: AttributeInitializationData
    OutputValueMax: AttributeInitializationData


class UIStatCollector: ...


class UIStatPriorityData:
    UIStat: UIStatData
    PriorityIncrease: float


class ReplicatedUIStatCollectionData: ...


class UserStateEnumValue:
    StateProperty: engine.SimpleMemberReference
    PropertyName: str
    Enum: unreal.UEnum
    EnumValue: int


class ViewModelOffsetImpulseInfo:
    EaseInDuration: float
    EaseInFunc: GbxEasingFunc
    EaseOutDuration: float
    EaseOutFunc: GbxEasingFunc
    RotationExtent: core_uobject.Rotator
    TranslationExtent: core_uobject.Vector


class Vector2DWaveform:
    X: FloatWaveform
    Y: FloatWaveform


class FloatWaveform:
    Frequency: float
    Amplitude: float
    Phase: float


class VectorWaveform:
    X: FloatWaveform
    Y: FloatWaveform
    Z: FloatWaveform


class EGbxActionEndState(enum.Enum):
    Success = 0
    Interrupted = 1
    Denied = 2


class EStanceStackLayer(enum.Enum):
    AITree = 0
    Blueprint = 1
    Count = 2


class EFacingChannel(enum.Enum):
    Look = 0
    Aim = 1
    EFacingChannel_MAX = 2


class EFacingInfoType(enum.Enum):
    Actor = 0
    ActorEyes = 1
    Location = 2
    ControllerAim = 3


class ENavAnimState(enum.Enum):
    Idle = 0
    Hop = 1
    Move = 2
    TurnBlend = 3


class EScriptedLadderType(enum.Enum):
    GettingOffAtTop = 0
    GettingOnAtBottom = 1
    GettingOffAtBottom = 2


class EUsabilityType(enum.Enum):
    Secondary = 0
    Count = 1


class EAIDodgeType(enum.Enum):
    Bullet = 0
    Grenade = 1
    Zone = 2


class EGbxGlyphSetOption(enum.Enum):
    Set4 = 0
    Set1 = 1
    Set2 = 2


class EStatusEffectDurationType(enum.Enum):
    Infinite = 0
    EStatusEffectDurationType_MAX = 1


class EHoldToUseMode(enum.Enum):
    Both = 0
    HoldOnly = 1


class EPawnAttachStatus(enum.Enum):
    EPawnAttachStatus_MAX = 0
    Attaching = 1
    Attached = 2


class ESpawnCostSelection(enum.Enum):
    Custom = 0
    ESpawnCostSelection_MAX = 1


class EMassSelection(enum.Enum):
    Preset = 0
    Custom = 1


class EDamageCausedModificationStrategy(enum.Enum):
    UseInstigatorModifier = 0
    EDamageCausedModificationStrategy_MAX = 1


class ECriticalHitDamageOverride(enum.Enum):
    ForceCrit = 0
    ForceNotCrit = 1


class ETeamCollisionChannel(enum.Enum):
    ETeamCollisionChannel_MAX = 0
    Two = 1
    Three = 2


class EStanceValueOverrideType(enum.Enum):
    Relative = 0
    Absolute = 1


class ERecentDamageFlags(enum.Enum):
    DamageOverTime = 0
    Healing = 1
    CriticalHit = 2
    Shield = 3
    Armor = 4
    Resist = 5
    ZeroDamage = 6
    Weapon = 7


class EUIStatComparisonResult(enum.Enum):
    Worse = 0
    Better = 1
    EUIStatComparisonResult_MAX = 2


class EActorPartTypeSelectionOverrideMode(enum.Enum):
    OverrideParts = 0
    EActorPartTypeSelectionOverrideMode_MAX = 1


class EActorPartReplacementMode(enum.Enum):
    Selective = 0
    Complete = 1


class EActorTagQueryMode(enum.Enum):
    HasNone = 0
    HasAll = 1


class EChargeCurveType(enum.Enum):
    Absolute = 0
    EChargeCurveType_MAX = 1


class ERelativeSizeCharge(enum.Enum):
    ERelativeSizeCharge_MAX = 0
    SameAndBigger = 1
    OnlyBigger = 2


class EAnimActionDefInput(enum.Enum):
    AnimAsset = 0
    AnimAssetName = 1


class EAnimNotifyAlignType(enum.Enum):
    Partner = 0
    EAnimNotifyAlignType_MAX = 1


class EAttributeInitializerUsageMode(enum.Enum):
    Add = 0
    Scale = 1
    EAttributeInitializerUsageMode_MAX = 2


class EBalanceValueType(enum.Enum):
    ExperienceLevel = 0
    EBalanceValueType_MAX = 1


class EChallengeType(enum.Enum):
    ECT_LevelObject = 0
    ECT_MAX = 1
    ECT_DesignerTriggered = 2


class ECharacterMovementAttributeValueType(enum.Enum):
    Speed2D = 0
    ECharacterMovementAttributeValueType_MAX = 1


class ECinematicAudioMode(enum.Enum):
    StandardCinematic = 0
    ExclusiveMode = 1


class EConditionalAreaDamageFilter(enum.Enum):
    MustBeRadiusDamage = 0
    EConditionalAreaDamageFilter_MAX = 1


class EConditionalDamageCriticalFilter(enum.Enum):
    EConditionalDamageCriticalFilter_MAX = 0
    HitRegioneMustNotBeCritical = 1
    MustBeAnyCritical = 2


class EDamageFilterExprMode(enum.Enum):
    EDamageFilterExprMode_MAX = 0
    MustNotMatch = 1


class EConditionalDamageTypeBonusMode(enum.Enum):
    ConvertAllDamage = 0
    AddBonusDamage_BackToAttacker = 1
    AddBonusDamage_BackToAttackerInstigator = 2


class EConditionalDamageModifierType(enum.Enum):
    Add = 0
    ScaleSimple = 1


class ECMInheritVelocityType(enum.Enum):
    Backward = 0
    Right = 1
    Up = 2


class ECMTerminalVelocityModificationType(enum.Enum):
    ECMTerminalVelocityModificationType_MAX = 0
    ScaleTerminalVelocity = 1


class ECMGravityModificationType(enum.Enum):
    ScaleDefaultGravity = 0
    OverrideGravity = 1


class ECMLedgeBehavior(enum.Enum):
    CannotWalkOffLedges = 0
    StopOnReachedLedge = 1


class ECMTeleportPreferenceType(enum.Enum):
    Behind_MoveDirection = 0
    Ahead_TargetFacing = 1
    ECMTeleportPreferenceType_MAX = 2


class ECMMoveLRControlType(enum.Enum):
    Speed = 0
    Yaw = 1


class ECMMoveFBControlType(enum.Enum):
    Pitch = 0
    Speed = 1


class ECMMovementType(enum.Enum):
    Flying = 0
    Falling = 1
    ECMMovementType_MAX = 2


class EDamageAreaBoxOriginType(enum.Enum):
    OffsetByDepth = 0
    EDamageAreaBoxOriginType_MAX = 1


class EDamageAreaOverlapFilterType(enum.Enum):
    Custom = 0
    Profile = 1


class EDamageComponentHealthMode(enum.Enum):
    SimpleHealth = 0
    EDamageComponentHealthMode_MAX = 1


class EAdditionalDamageClassifier(enum.Enum):
    ReflectedBonusDamage = 0
    BonusDamage = 1
    EAdditionalDamageClassifier_MAX = 2


class EDebugDisplayVerbosityLevel(enum.Enum):
    Verbose = 0
    EDebugDisplayVerbosityLevel_MAX = 1


class EExplosionTinnitusDuration(enum.Enum):
    Short = 0
    Medium = 1
    EExplosionTinnitusDuration_MAX = 2


class EFeedbackDataFirstPersonImpulseType(enum.Enum):
    Custom = 0
    EFeedbackDataFirstPersonImpulseType_MAX = 1


class EFeedbackType(enum.Enum):
    RandomRumble = 0
    Directional = 1
    RandomShake = 2


class EForceSelection(enum.Enum):
    Preset = 0
    Attribute = 1


class EContainsTagComponent(enum.Enum):
    NoTagComponent = 0
    EContainsTagComponent_MAX = 1


class EGameResourcePoolState(enum.Enum):
    RPS_MAX = 0
    RPS_Filled = 1
    RPS_Depleting = 2


class GameResourcePoolReplicationType(enum.Enum):
    GRPRT_Basic = 0
    GRPRT_Full = 1


class EAIChargeAnim(enum.Enum):
    Loop = 0
    Strike = 1
    Start = 2
    EAIChargeAnim_MAX = 3


class EActionSelectionMethod(enum.Enum):
    RANDOM = 0
    EActionSelectionMethod_MAX = 1


class ECoordinatedOwnedParticleAction(enum.Enum):
    Hide = 0
    Suppress = 1


class ECoordinatedParticleScaleMode(enum.Enum):
    VerticalAxis = 0
    LargestAxis = 1
    SmallestAxis = 2


class ECoordinatedEffectParamScaleMode(enum.Enum):
    XBounds = 0
    YBounds = 1
    ECoordinatedEffectParamScaleMode_MAX = 2


class EDirectionPlane(enum.Enum):
    Vertical = 0
    EDirectionPlane_MAX = 1


class EGbxPhysicalActionMovementLockMode(enum.Enum):
    MLM_AquireOnBegin = 0
    MLM_ReleaseOnEnd = 1
    MLM_MAX = 2


class EGbxPhysicalActionDynamicBodyState(enum.Enum):
    DBS_FaceDown = 0
    DBS_MAX = 1
    DBS_FaceUp = 2


class EGbxPhysicalActionDynamicBoneActivationMode(enum.Enum):
    DBAM_Recursive = 0
    DBAM_FullBody = 1


class EGbxPhysicalActionEndCondition(enum.Enum):
    EndCondition_FullFatigue = 0
    EndCondition_NotAllFlagsMatch = 1
    EndCondition_NoFatigue = 2


class EGbxPhysicalActionBeginCondition(enum.Enum):
    BeginCondition_WaitUntilPoseMatch = 0
    BeginCondition_NotAllFlagsMatch = 1
    BeginCondition_MAX = 2


class ERagdollState(enum.Enum):
    Ragdoll = 0
    Anim = 1
    StartBlend = 2
    ERagdollState_MAX = 3


class EDynamicToKinematicTransition(enum.Enum):
    RagdollLandToStandUp = 0
    PredictiveLanding = 1
    EDynamicToKinematicTransition_MAX = 2


class EGbxActionEndCondition(enum.Enum):
    EndCondition_LastFrame = 0
    EndCondition_Loop = 1


class EGbxActionPriority(enum.Enum):
    Normal = 0
    High = 1
    EGbxActionPriority_MAX = 2


class EGbxActionNetMode(enum.Enum):
    AlwaysRep = 0
    EGbxActionNetMode_MAX = 1
    LocalOnly = 2


class EActionRegisterType(enum.Enum):
    Float = 0
    Name = 1
    Int = 2


class EAnimBPProfileImport(enum.Enum):
    FootIK = 0
    LookAt = 1
    EAnimBPProfileImport_MAX = 2


class EForwardDynamicsActivation(enum.Enum):
    ForwardDynamicsProfileDefinition = 0
    EForwardDynamicsActivation_MAX = 1


class EGbxAreaDrawStyle(enum.Enum):
    Wire = 0
    EGbxAreaDrawStyle_MAX = 1
    Solid = 2


class EGbxAttributeModifierActionExecOutput(enum.Enum):
    Failure = 0
    EGbxAttributeModifierActionExecOutput_MAX = 1


class EGbxBoneModifyProfile_PoseMode(enum.Enum):
    EGbxBoneModifyProfile_MAX = 0
    Additive = 1


class EBoneModifyTransition_TransformType(enum.Enum):
    Rotation = 0
    Scale = 1


class EGbxCharacterBlendPoints(enum.Enum):
    EGbxCharacterBlendPoints_MAX = 0
    EightPoint = 1


class EMantleUpCheckState(enum.Enum):
    StandingSpotCheck_Initial_Rotated_InitiallyPenetrating = 0
    WallCheck_NoWall = 1
    WallCheck_TooFlat = 2
    HeadRoomCheck_BlockedAhead = 3
    StandingSpotCheck_Initial_Ahead_InvalidHitComponent = 4


class EGbxMovementMode(enum.Enum):
    GBXMOVE_NoneWithRootMotion = 0
    GBXMOVE_Mantle = 1
    GBXMOVE_PawnAttached = 2


class EMassComparison(enum.Enum):
    GreaterThan = 0
    LessThan = 1
    EqualTo = 2


class EConditionComparisonOperatorType(enum.Enum):
    LessThan = 0
    NotEqualTo = 1
    GreaterThan = 2


class ECompoundConditionOperatorType(enum.Enum):
    Xor = 0
    Or = 1
    ECompoundConditionOperatorType_MAX = 2


class ELinkedParameterType(enum.Enum):
    Vector = 0
    Texture = 1


class EGbxCustomizationComponentInitSourceType(enum.Enum):
    CopyFromInstigatorOnSpawn = 0
    LinkToInstigatorOnSpawn = 1


class EDamageSurfaceType(enum.Enum):
    Flesh = 0
    Armor = 1
    EDamageSurfaceType_MAX = 2


class EGbxFeedbackType(enum.Enum):
    Continuous = 0
    Ranged = 1
    RandomRumble = 2
    Directional = 3
    RandomShake = 4
    EGbxFeedbackType_MAX = 5


class EGbxFlagEval(enum.Enum):
    TrueForXSeconds = 0
    IsFalse = 1
    TrueWithinXSeconds = 2


class EPlayersOverlappingActorOutput(enum.Enum):
    NotOverlapping = 0
    EPlayersOverlappingActorOutput_MAX = 1


class EPlayersInVolumeOutput(enum.Enum):
    EPlayersInVolumeOutput_MAX = 0
    NotInVolume = 1


class EIsAutonomousOuput(enum.Enum):
    NotAutonomous = 0
    EIsAutonomousOuput_MAX = 1


class EIsPlayerExecOutput(enum.Enum):
    NotPlayer = 0
    EIsPlayerExecOutput_MAX = 1


class EGbxParamValueFlags(enum.Enum):
    AllBBKeyTypes = 0
    EGbxParamValueFlags_MAX = 1


class EGbxParamValueType(enum.Enum):
    Bool = 0
    Int = 1
    Object = 2


class EGbxParamValueMode(enum.Enum):
    ValueVariance = 0
    MinMax = 1
    None_ = 2
    Count = 3


class EDestructibleDamageThresholdMagnitude(enum.Enum):
    EDestructibleDamageThresholdMagnitude_MAX = 0
    Medium = 1
    High = 2


class EGraphicsMode(enum.Enum):
    EGraphicsMode_MAX = 0
    Resolution = 1


class ESpeakerSetup(enum.Enum):
    Hifi = 0
    NightTime = 1
    Headphones = 2


class ETimedUpdateBehavior(enum.Enum):
    UpdateRegularlyEvenWhenNavigating = 0
    UpdateRegularlyExceptWhenNavigating = 1


class EQueryOwnerLocationUse(enum.Enum):
    Always = 0
    Only = 1


class ESimpleMotionType(enum.Enum):
    ScaleByValue = 0
    Interpolate = 1
    Alternate = 2


class EGlobalBoneModifyProfile_PoseMode(enum.Enum):
    EGlobalBoneModifyProfile_MAX = 0
    Multiplicative = 1


class EHitReactionConditionCombine(enum.Enum):
    Or = 0
    EHitReactionConditionCombine_MAX = 1


class EHitReactionConditionContext(enum.Enum):
    DamageType = 0
    Receiver = 1
    CauserOwner = 2


class EDamageReactionEventType(enum.Enum):
    EDamageReactionEventType_MAX = 0
    HealthPersistent = 1
    Damage = 2


class EHitRegionDamageRule(enum.Enum):
    OwnerHealth_DamageCap = 0
    OwnerHealth_NoDamageCap = 1


class EImpactUsage(enum.Enum):
    Footstep = 0
    EImpactUsage_MAX = 1


class EInstigatorAttributeEffectModifierValueContext(enum.Enum):
    EInstigatorAttributeEffectModifierValueContext_MAX = 0
    ThisInventoryActor = 1


class EInstigatorAttributeEffectAttributeToModifyContextSource(enum.Enum):
    EInstigatorAttributeEffectAttributeToModifyContextSource_MAX = 0
    InstigatorOnly = 1


class EInterpMode(enum.Enum):
    EInterpMode_MAX = 0
    Linear = 1
    NonLinear = 2


class EMantleType(enum.Enum):
    WallHop = 0


class ENavAnimType(enum.Enum):
    Direction = 0
    Destination = 1
    ENavAnimType_MAX = 2


class EAttachmentTransitionTiming(enum.Enum):
    AttachBaseDuringTransition = 0
    ChangePawnAfterTransition = 1


class EAttachmentPossessionRule(enum.Enum):
    Unchanged = 0
    EAttachmentPossessionRule_MAX = 1


class EPhysicalAnimationBlendToKinematicMode(enum.Enum):
    DynamicMatchesAnimation = 0
    Immediate = 1


class EPhysicalAnimationRootMotionControl(enum.Enum):
    PARMC_PureDynamic = 0
    PARMC_SimulatedPointDrive = 1
    PARMC_MAX = 2


class EAggregateBoneStatusFlag(enum.Enum):
    ABS_HasMotion = 0
    ABS_HasPoseVariance = 1
    ABS_HasPlayingAnimation = 2


class EAggregateBoneFatigueStatus(enum.Enum):
    ABFS_NoFatigue = 0
    ABFS_FullyDivergedFatigue = 1
    ABFS_MAX = 2


class ECycleDirection(enum.Enum):
    ECycleDirection_MAX = 0
    Forward = 1


class ERelativeDirectionType(enum.Enum):
    ParentOrientation = 0
    ParentOrientation2D = 1
    ParentVelocity = 2
    Random = 3
    ParentAimDirection = 4


class EScreenParticleScalingMode(enum.Enum):
    FitToViewport = 0
    FitToExterior = 1
    FitToVertical = 2


class ESimpleMathValueResolverOperatorType(enum.Enum):
    Subtract = 0
    Multiply = 1
    ESimpleMathValueResolverOperatorType_MAX = 2


class ESplitScreenViewportType(enum.Enum):
    Horizontal = 0
    ESplitScreenViewportType_MAX = 1
    Vertical = 2


class EStatusEffectStackingInstanceReplacementCriteria(enum.Enum):
    ChooseLowerDPS = 0
    ChooseHigherDPS = 1
    ChooseShorterDuration = 2


class EStatusEffectStackingInstanceSelectionCriteria(enum.Enum):
    OldestInstance = 0
    MostTimeRemaining = 1
    EStatusEffectStackingInstanceSelectionCriteria_MAX = 2


class EStretchBonesMarkerMode(enum.Enum):
    AttachedMarker = 0
    AfterMarker = 1


class EStretchBonesActorTrackingStyle(enum.Enum):
    Track = 0
    PredictedFirstFrame = 1
    NavEntry = 2


class EAimAssistSnapTargetType(enum.Enum):
    EAimAssistSnapTargetType_MAX = 0
    Disabled = 1
    Horizontal = 2


class EAITargetScoringBoost(enum.Enum):
    AmplifyLight = 0
    ReduceLight = 1
    ReduceModerate = 2


class ETerritoryCombatProxyType(enum.Enum):
    ETerritoryCombatProxyType_MAX = 0
    Patrol = 1


class ETerritoryType(enum.Enum):
    Combat = 0
    Threat = 1


class ETerritoryDrawStyle(enum.Enum):
    ETerritoryDrawStyle_MAX = 0
    Wire = 1
    Solid = 2


class EThreatReason(enum.Enum):
    ThreatReason_TerritoryEverywhereThreat = 0
    ThreatReason_TerritoryIncursionAuto = 1
    ThreatReason_ShotAt = 2
    ThreatReason_Scripted = 3


class EUIStatCombinationMethod(enum.Enum):
    Divide = 0
    Add = 1
    DontCombine = 2


class EUIStatValueRoundingMode(enum.Enum):
    EUIStatValueRoundingMode_MAX = 0
    RoundToInt = 1
    FloorToInt = 2


class EUIStatValueSignStyle(enum.Enum):
    Negative = 0
    Positive = 1
    EUIStatValueSignStyle_MAX = 2


class EUIStatValueStyle(enum.Enum):
    AbsoluteModification = 0
    ScaleModification = 1


class EUsableTypeCostContext(enum.Enum):
    Player = 0
    EUsableTypeCostContext_MAX = 1

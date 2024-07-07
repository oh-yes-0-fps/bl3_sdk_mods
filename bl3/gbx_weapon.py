from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine
from . import gbx_runtime
from . import wwise_audio
from . import aimodule
from . import gbx_game_system_core
from . import gbx_ui



class Weapon(engine.Actor):
    CurrentFireComponent: WeaponFireComponent
    WeaponDisplayData: WeaponTypeAsset
    WeaponType: WeaponTypeData
    SwitchModeTimeScale: engine.GbxAttributeFloat
    SwitchModeTime: float
    SwitchModeCompletePercent: float
    PostSprintDelayUseTime: float
    ViewModelFOV: float
    DepthOfFieldZoomedForegroundNearRegion: float
    DamageScaleConditionals: unreal.WrappedArray[gbx_game_system_core.DamageScaleConditionalData]
    ReplicationProxy: gbx_game_system_core.GbxObjectReplicatorProxy
    PendingAttachState: WeaponAttachState
    AttachState: WeaponAttachState
    EquipTime: engine.GbxAttributeFloat
    PutDownTime: engine.GbxAttributeFloat
    PendingUseModeIndex: int
    CurrentUseModeIndex: int
    CurrentSlotIndex: int
    NextSlotIndex: int
    UseModeState: unreal.WrappedArray[WeaponUseModeState]
    AimAssetParameters: gbx_game_system_core.AimAssistParameters
    bIsTargetLocked: bool
    bForceUnzoomWhenSwitchingModes: bool
    AttachmentSlots3P: unreal.WrappedArray[WeaponAttachmentSlot]
    AttachmentSlots1P: unreal.WrappedArray[WeaponAttachmentSlot]
    bWeaponAttached: bool
    RegisteredMaterialEffects: unreal.WrappedArray[WeaponRegisterMaterialEffectData]
    RegisteredSkeletalControls: unreal.WrappedArray[WeaponRegisterSkeletalControlData]
    CachedFireTriggerFeedback: WeaponTriggerFeedbackAsset
    CachedZoomTriggerFeedback: WeaponTriggerFeedbackAsset
    bShowCrosshair: bool
    bAlwaysTickAttachedMeshes: bool
    BodyWeaponHoldName: str
    AnimSetGenericNames: unreal.WrappedArray[str]
    DamageModifierCompClass: unreal.UClass
    CurrentState: str
    UnregisteredFirstPersonOnlyAttachmentEffects: unreal.WrappedArray[WeaponRegisterAttachmentEffectData]
    UseModeIcons: unreal.WrappedArray[engine.Texture2D]
    UseModeIconFrameNames: unreal.WrappedArray[str]
    MainHandGripSocketName: str
    OffHandGripSocketName: str
    def Unlock(self, bReplicate: bool): ...
    def TryAutoReload(self): ...
    def ToggleMode(self, InputChannel: int): ...
    def SwitchPendingUseMode(self): ...
    def SwitchMode(self, InputChannel: int, NextUseModeIndex: int, bForced: bool): ...
    def StopZooming(self, bSkipTransitions: bool, bClearInput: bool): ...
    def StopWeaponAction(self, WeaponAction: int): ...
    def StopUsing(self, InputChannel: int, bForced: bool): ...
    def StopReloading(self): ...
    def StopModeSwitch(self): ...
    def StopEffects(self, EffectType: int, UseModeIndex: int): ...
    def StopDynamicMaterialEffect(self, EffectID: int): ...
    def StopAnimation(self, Anim: engine.AnimMontage, bFirstPerson: bool): ...
    def StartZooming(self): ...
    def StartUsing(self, InputChannel: int): ...
    def StartReloading(self, bAuto: bool): ...
    def SetTargetLocked(self, bIsLocked: bool): ...
    def SetPreUseState(self, UseModeIndex: int, bEnabled: bool): ...
    def SetMaterialVectorParameterValue(self, ParamName: str, ParamValue: core_uobject.LinearColor): ...
    def SetMaterialScalarParameterValue(self, ParamName: str, ParamValue: float): ...
    def SetEffectVectorParameter(self, ParamName: str, ParamValue: core_uobject.Vector, QueryData: WeaponEffectQueryData): ...
    def SetEffectMaterialParameter(self, ParamName: str, ParamValue: engine.MaterialInterface, QueryData: WeaponEffectQueryData): ...
    def SetEffectFloatParameter(self, ParamName: str, ParamValue: float, QueryData: WeaponEffectQueryData): ...
    def SetEffectEmitterState(self, EmitterName: str, bEnabled: bool, QueryData: WeaponEffectQueryData): ...
    def SetEffectColorParameter(self, ParamName: str, ParamValue: core_uobject.LinearColor, QueryData: WeaponEffectQueryData): ...
    def SetBoneVisibility(self, BoneName: str, bVisible: bool, AttachmentType: int): ...
    def ServerUnlock(self): ...
    def ServerSwitchMode(self, InputChannel: int, NextUseModeIndex: int, bForced: bool): ...
    def ServerStopUsing(self, InputChannel: int, bForced: bool): ...
    def ServerStopModeSwitch(self, InputChannel: int, ClientUseModeIndex: int): ...
    def ServerStartUsing(self, InputChannel: int, ClientPatternSeed: int): ...
    def ServerStartReloading(self, UseModeIndex: int, bAuto: bool): ...
    def ServerSetZoomState(self, UseModeIndex: int, NewState: WeaponZoomState, ZoomStartOffset: float): ...
    def ServerSetPatternSeed(self, ClientPatternSeed: int): ...
    def ServerRestartAutoUse(self): ...
    def ServerLock(self, Duration: float): ...
    def ServerInterruptReloadToUse(self, ClientLoadedAmmo: int): ...
    def ServerEquipInterruptible(self): ...
    def RegisterTrinketAttachment(self, Data: WeaponRegisterTrinketAttachmentData): ...
    def RegisterSkeletalControl(self, Data: WeaponRegisterSkeletalControlData): ...
    def RegisterSimpleEffect(self, EffectType: int, Effect: engine.ParticleSystem, EffectSocket: str): ...
    def RegisterMaterialEffect(self, Data: WeaponRegisterMaterialEffectData): ...
    def RegisterEffect(self, Data: WeaponRegisterAttachmentEffectData): ...
    def ReevaluateConditionalEffects(self): ...
    def PrevZoomLevel(self): ...
    def PlayEffects(self, EffectType: int, UseModeIndex: int, EffectID: int): ...
    def PlayDynamicMaterialEffect(self, Data: WeaponMaterialEffectData, ReturnValue: int) -> int: ...
    def PlayAnimation(self, Anim: engine.AnimMontage, bFirstPerson: bool, PlayRate: float, Duration: float, ReturnValue: float) -> float: ...
    def OnZoomedOut(self): ...
    def OnUseStarted(self): ...
    def OnUseFinished(self): ...
    def OnUpdateSkeletalControlsWhenUseFinishes(self): ...
    def OnUpdateSkeletalControlsWhenUsed(self): ...
    def OnUpdateSkeletalControlsWhenAmmoChanges(self): ...
    def OnRep_TargetLockedChanged(self): ...
    def OnRep_PendingUseModeIndex(self): ...
    def OnRep_PendingAttachState(self): ...
    def OnRep_CurrentUseModeIndex(self, PreviousUseModeIndex: int): ...
    def OnReloadEnded(self, bCompleted: bool): ...
    def OnAmmoGivenToEmptyWeapon(self): ...
    def NotifySkeletalControl(self, ControlType: int, ControlName: str, Event: EWeaponSkeletalControlEvent, EventValue: float): ...
    def NextZoomLevel(self): ...
    def Lock(self, Duration: float, bReplicate: bool): ...
    def K2_StopWeaponActionObj(self, WeaponAction: gbx_game_system_core.GbxAction): ...
    def K2_PlayWeaponActionEx(self, WeaponAction: int, ActionParams: gbx_game_system_core.ActionState_Base, bCheckForRelevancy: bool, ReturnValue: gbx_game_system_core.GbxAction) -> gbx_game_system_core.GbxAction: ...
    def K2_PlayWeaponAction(self, WeaponAction: int, PlayRate: float, Duration: float, bCheckForRelevancy: bool, ReturnValue: gbx_game_system_core.GbxAction) -> gbx_game_system_core.GbxAction: ...
    def IsZoomedIn(self, bIncludeTransitions: bool, ReturnValue: bool) -> bool: ...
    def IsZoomed(self, ReturnValue: bool) -> bool: ...
    def IsUsing(self, ReturnValue: bool) -> bool: ...
    def IsTargetLocked(self, ReturnValue: bool) -> bool: ...
    def IsSwitchingModes(self, ReturnValue: bool) -> bool: ...
    def IsReloading(self, ReturnValue: bool) -> bool: ...
    def IsPuttingDown(self, ReturnValue: bool) -> bool: ...
    def IsPendingUse(self, InputChannel: int, ReturnValue: bool) -> bool: ...
    def IsLocked(self, ReturnValue: bool) -> bool: ...
    def IsLocalAuthority(self, ReturnValue: bool) -> bool: ...
    def IsInactive(self, ReturnValue: bool) -> bool: ...
    def IsEquipping(self, ReturnValue: bool) -> bool: ...
    def IsAuthorityUsing(self, ReturnValue: bool) -> bool: ...
    def IsAuthoritySwitchingModes(self, ReturnValue: bool) -> bool: ...
    def IsAuthorityReloading(self, ReturnValue: bool) -> bool: ...
    def IsAuthorityPuttingDown(self, ReturnValue: bool) -> bool: ...
    def IsAuthorityEquipping(self, ReturnValue: bool) -> bool: ...
    def IsActive(self, ReturnValue: bool) -> bool: ...
    def GivenTo(self, NewOwner: engine.Pawn): ...
    def GetZoomFOVScale(self, ReturnValue: float) -> float: ...
    def GetZoomEffect(self, ReturnValue: float) -> float: ...
    def GetZoomDuration(self, ReturnValue: float) -> float: ...
    def GetUseModeComponentByClass(self, ComponentClass: unreal.UClass, UseModeIndex: int, ReturnValue: engine.ActorComponent) -> engine.ActorComponent: ...
    def GetMuteADSAlpha(self, ReturnValue: float) -> float: ...
    def GetMaxZoomFOVScale(self, ReturnValue: float) -> float: ...
    def GetLastInputChannel(self, ReturnValue: int) -> int: ...
    def GetCurrentReloadPartType(self, ReturnValue: int) -> int: ...
    def GetAttachmentMesh(self, bFirstPerson: bool, SlotIndex: int, ReturnValue: engine.MeshComponent) -> engine.MeshComponent: ...
    def GetAssociatedUseModeComponentByClass(self, ComponentClass: unreal.UClass, ReferenceComponent: engine.ActorComponent, ReturnValue: engine.ActorComponent) -> engine.ActorComponent: ...
    def GetAimAssistParameters(self, ReturnValue: gbx_game_system_core.AimAssistParameters) -> gbx_game_system_core.AimAssistParameters: ...
    def EquipInterruptible(self): ...
    def Dropped(self): ...
    def CycleZoomLevel(self): ...
    def ClientUnlock(self): ...
    def ClientStopReloading(self): ...
    def ClientLock(self, Duration: float): ...
    def AddUseMode(self, UseComponent: WeaponUseComponent, OtherComponents: unreal.WrappedArray[engine.ActorComponent], InputChannels: int, ReturnValue: int) -> int: ...
    def Activate(self, WeaponOwner: engine.Pawn, InSlot: int, InEquipType: EWeaponEquipType): ...


class WeaponPreUseComponent(engine.ActorComponent):
    bEnabled: bool
    WeaponPrivate: Weapon
    def K2_OnDeactivated(self): ...
    def K2_OnActivated(self): ...


class WeaponUseComponent(engine.ActorComponent):
    UseMode: int
    bAutoSwitchModeWhenOutOfAmmo: bool
    bClearUseInputWhenSwitchingModes: bool
    bActivateModeWhenZoomed: bool
    bUseAnimationSwitchModeTime: bool
    CrosshairData: gbx_ui.GbxCrosshairDataAsset
    ZoomedCrosshairData: gbx_ui.GbxCrosshairDataAsset
    Icon: engine.Texture2D
    ModeName: str
    InstigatorAttributeEffects: unreal.WrappedArray[gbx_game_system_core.AttributeEffectData]
    InstigatorAttributeModifiers: unreal.WrappedArray[gbx_game_system_core.GbxAttributeModifierHandle]
    PreUseComponent: WeaponPreUseComponent
    WeaponPrivate: Weapon
    def ToggleMode(self, ReturnValue: bool) -> bool: ...
    def SwitchToZoomedMode(self, ZoomLevel: int): ...
    def SwitchFromZoomedMode(self, ZoomLevel: int): ...
    def OnPreUseFinished(self, bInterrupted: bool): ...
    def K2_OnDeactivated(self): ...
    def K2_OnActivated(self): ...
    def CanActivateMode(self, ReturnValue: bool) -> bool: ...


class WeaponFireComponent(WeaponUseComponent):
    FireRate: engine.GbxAttributeFloat
    AutomaticBurstCount: engine.GbxAttributeInteger
    BurstFireDelay: engine.GbxAttributeFloat
    bAutoBurst: bool
    FireSocket: str
    FireSockets: unreal.WrappedArray[str]
    FullFireSocketCycle: bool
    TraceChannel: int
    MinFireRateScale: float
    FireRateAccelDuration: engine.GbxAttributeFloat
    FireRateDecelDuration: engine.GbxAttributeFloat
    MinFireRatePercentToFire: float
    FireRateCurve: engine.CurveFloat
    bUseShotStrengthFormula: bool
    ShotStrengthFormula: gbx_game_system_core.AttributeInitializationData
    FireSequenceLength: int
    ResetFireSequenceTime: engine.GbxAttributeFloat
    ResetFireSequenceCompletePercent: float
    bAdvanceFireSequenceAtEndOfBurst: bool
    bTotalShotCostRequiredToFire: bool
    ShotAmmoCost: engine.GbxAttributeInteger
    MinShotAmmoCost: int
    Spread: engine.GbxAttributeFloat
    AccuracyImpulse: engine.GbxAttributeFloat
    BurstAccuracyImpulseScale: engine.GbxAttributeFloat
    ViewModelShotOffsetScale: float
    Damage: engine.GbxAttributeFloat
    DamageFormula: gbx_game_system_core.AttributeInitializationData
    ShotStrengthDamageCurve: engine.CurveFloat
    DamageRadius: engine.GbxAttributeFloat
    DamageRadiusFormula: gbx_game_system_core.AttributeInitializationData
    ShotStrengthDamageRadiusCurve: engine.CurveFloat
    ImpactForce: engine.GbxAttributeFloat
    ImpactForceSelection: gbx_game_system_core.ForceSelection
    ShotStrengthImpactForceCurve: engine.CurveFloat
    DamageType: unreal.UClass
    DamageSource: unreal.UClass
    ImpactData: gbx_game_system_core.ImpactData
    MuzzleFXSequenceLength: int
    FireSoundPerception: gbx_game_system_core.SoundPerceptionProperties
    FireFeedback: gbx_game_system_core.FeedbackData
    bPlayFeedbackAtLocation: bool
    bScaleFeedbackWithFireRate: bool
    ScaledFeedback: gbx_game_system_core.FeedbackData
    FeedbackFireRateScalar: engine.RuntimeFloatCurve
    FeedbackSocket: str
    bSyncAnimationToFireRate: bool
    FireAnimationBlendSpace: float
    SkeletalControlType: int
    SkeletalControlName: str
    SkeletalControlFireInput: float
    bLockOntoBestTarget: bool
    DelayInitializeAttribute: float
    bFireRateAccelActive: bool
    FireRateState: EWeaponFireRateState
    CurrentBurstShotCount: int
    CurrentFireSequenceIndex: int
    ClientFireSequenceState: int
    FireRatePercent: float
    FlashSlot: int
    FlashCount: int
    ImpactLocation: engine.Vector_NetQuantize
    DamageAmount: float
    AIBurstCount: gbx_game_system_core.GbxParam
    AIBurstFireDelay: gbx_game_system_core.GbxParam
    AIFireInterval: gbx_game_system_core.GbxParam
    AIAccuracy: gbx_game_system_core.GbxParam
    AIProjectileSpeedScale: gbx_game_system_core.GbxParam
    AIDesiredRange: gbx_runtime.NumericRange
    AIMinDesiredRange: gbx_game_system_core.GbxParam
    AIMaxDesiredRange: gbx_game_system_core.GbxParam
    ScaledEffect: engine.GbxForceFeedbackEffect
    def ServerResetFireSequence(self): ...
    def OnStopFireRateDeceleration(self): ...
    def OnStopFireRateAcceleration(self): ...
    def OnStartFireRateDeceleration(self): ...
    def OnStartFireRateAcceleration(self): ...
    def OnRep_ImpactLocation(self): ...
    def OnRep_FlashCount(self): ...
    def OnRep_FireRateAccelChanged(self): ...
    def OnRep_ClientFireSequenceState(self): ...
    def OnReloadAmmoGiven(self): ...
    def OnLoopingFireActionEnd(self, EndState: gbx_game_system_core.EGbxActionEndState): ...
    def OnGivenTo(self): ...
    def IsFireRateAccelEnabled(self, ReturnValue: bool) -> bool: ...
    def GetLockedTarget(self, ReturnValue: engine.Actor) -> engine.Actor: ...
    def GetFireRatePercent(self, ReturnValue: float) -> float: ...
    def ClientStopResetFireSequence(self): ...


class WeaponFireProjectileComponent(WeaponFireComponent):
    ProjectilesPerShot: engine.GbxAttributeInteger
    ProjectileSpeedScale: engine.GbxAttributeFloat
    ShotStrengthProjectileSpeedCurve: engine.CurveFloat
    ProjectileTemplate: unreal.UClass
    ProjectileBaseValues: unreal.WrappedArray[gbx_game_system_core.AttributeBaseValueData]
    LightProjectileData: unreal.UClass
    FiringPatternData: FiringPattern
    Range: float
    def GetShotProjectileData(self, ReturnValue: unreal.UClass) -> unreal.UClass: ...
    def GetShotLightProjectileData(self, ReturnValue: unreal.UClass) -> unreal.UClass: ...


class Projectile(engine.Actor):
    bIgnoreCollisionWithInstigator: bool
    bIgnoreCollisionWithInstigatorTeam: bool
    bStopBlockingPawnsAfterCollidingWithOne: bool
    bServerControlsProjectileLifetime: bool
    DamageInfo: gbx_game_system_core.DamageInfo
    DefaultImpact: gbx_game_system_core.ImpactData
    DefaultImpactEffectDelay: float
    SpawnModifierType: EWeaponShotModifierType
    SpawnModifierValue: float
    MovementComponent: GbxProjectileMovementComponent
    ExplosionComponent: gbx_game_system_core.ExplosionComponent
    bClientExplodeAtLeastOnce: bool
    bExplodeOnHit: bool
    bExplodeOnHitWorld: bool
    bExplodeOnHitDamagable: bool
    bExplodeOnHitEnemy: bool
    bExplodeAfterLifetime: bool
    bDestroyAfterExplode: bool
    bDamageOnExplode: bool
    DamageData: unreal.UClass
    ProjectileTeam: gbx_game_system_core.Team
    DamageSourceOverride: unreal.UClass
    DamageTypeOverride: unreal.UClass
    ExplosionData: gbx_game_system_core.ExplosionData
    bUseQuickPopExplosion: bool
    QuickPopExplosion: gbx_game_system_core.ExplosionData
    ImpactData: gbx_game_system_core.ImpactData
    DamageOverride: gbx_game_system_core.AttributeInitializationData
    DamageAreaRadius: float
    DamageAreaBoxExtent: core_uobject.Vector
    ImpactForceOverride: gbx_game_system_core.ForceSelection
    CriticalHitOverrides: gbx_game_system_core.CriticalHitDamageOverrides
    OverrideIgnoreActors: unreal.WrappedArray[engine.Actor]
    WeaponFiredFrom: Weapon
    SpawnSpeedScale: float
    def StopBlockingPawns(self): ...
    def SetProjectileDamageType(self, DamageType: unreal.UClass): ...
    def SetProjectileDamageSource(self, DamageSource: unreal.UClass): ...
    def SetProjectileDamageRadius(self, DamageRadius: float): ...
    def SetProjectileDamage(self, Damage: float): ...
    def ResetCollisionWith(self, ActorToCollide: engine.Actor): ...
    def OnRep_SpawnModifierType(self): ...
    def OnLastBounce(self, ImpactResult: engine.HitResult): ...
    def OnHitWorld(self, Hit: engine.HitResult): ...
    def OnHitNeutral(self, Hit: engine.HitResult): ...
    def OnHitFriendly(self, Hit: engine.HitResult): ...
    def OnHitEnemy(self, Hit: engine.HitResult): ...
    def OnHitDamagableObject(self, Hit: engine.HitResult): ...
    def OnExplode(self): ...
    def OnComponentDetachedFromParent(self, SceneComponent: engine.SceneComponent): ...
    def OnBounce(self, Hit: engine.HitResult, ImpactVelocity: core_uobject.Vector): ...
    def OnBeginExplode(self): ...
    def IgnoreCollisionWith(self, ActorToIgnore: engine.Actor): ...
    def HandleDetachRequest(self): ...
    def GetProjectileMovementComponent(self, ReturnValue: GbxProjectileMovementComponent) -> GbxProjectileMovementComponent: ...
    def GetProjectileDamageType(self, ReturnValue: unreal.UClass) -> unreal.UClass: ...
    def GetProjectileDamageSource(self, ReturnValue: unreal.UClass) -> unreal.UClass: ...
    def GetProjectileDamageRadius(self, ReturnValue: float) -> float: ...
    def GetProjectileDamage(self, ReturnValue: float) -> float: ...
    def GetExplosionComponent(self, ReturnValue: gbx_game_system_core.ExplosionComponent) -> gbx_game_system_core.ExplosionComponent: ...
    def Explode(self): ...
    def CheckProjectileAttachment(self): ...
    def BounceDelegate(self, ImpactResult: engine.HitResult, ImpactVelocity: core_uobject.Vector): ...


class GbxProjectileMovementComponent(engine.ProjectileMovementComponent):
    ProjectileAcceleration: float
    MinSpeedWhenDecelerating: float
    OwningProjectile: Projectile
    bSmoothedRotationFollowsVelocity: bool
    SmoothedRotationSpeed: float
    bDontStopSimulatingAfterHittingAnotherProjectile: bool
    MaxNumBounces: int
    bBounceParallelToHitNormal: bool
    CurrentNumBounces: int
    bFreezeMovementAfterLastBounce: bool
    BulletSensePerception: gbx_game_system_core.BulletPerceptionProperties
    ImpactSoundPerception: gbx_game_system_core.SoundPerceptionProperties
    bCanTriggerGrenadeDodges: bool
    bDisablePhysicsWhenAttached: bool
    InitialProjectileGravity: float
    def ScaleVelocity(self, InScale: float): ...
    def OnRep_InitialProjectileGravity(self): ...
    def OnProjectilePostLastBounceDelegate__DelegateSignature(self, ImpactResult: engine.HitResult): ...
    def OnHit(self, SelfActor: engine.Actor, OtherActor: engine.Actor, NormalImpulse: core_uobject.Vector, Hit: engine.HitResult): ...
    def OnBounce(self, ImpactResult: engine.HitResult, ImpactVelocity: core_uobject.Vector): ...


class LightProjectileManager(engine.Actor):
    ActiveProjectiles: unreal.WrappedArray[LightProjectile]
    ProjectilesWaitingBatch: unreal.WrappedArray[LightProjectile]
    ProjectilePool: unreal.WrappedArray[LightProjectile]
    ActiveParticles: unreal.WrappedArray[engine.ParticleSystemComponent]
    ParticlesPool: unreal.WrappedArray[LightProjectileParticlePoolData]
    MaxAsyncSpawnTime: float
    def OnParticleSystemFinished(self, FinishedComponent: engine.ParticleSystemComponent): ...


class LightProjectile(unreal.UObject):
    SyncID: int
    Data: LightProjectileData
    Damage: float
    DamageRadius: float
    DamageType: unreal.UClass
    DamageSource: unreal.UClass
    ImpactForce: float
    bActive: bool
    InitialClientState: ReplicatedLightProjectileInitializationData
    AttachmentData: LightProjectileAttachment
    ExplodeData: LightProjectileExplodeData
    ImpactInfo: LightProjectileImpactData
    ShutdownID: int
    StartTime: float
    LifeTime: float
    HomingStartTime: float
    ElapsedTime: float
    LastHitActor: engine.Actor
    Location: core_uobject.Vector
    ComponentLocation: core_uobject.Vector
    ComponentRotation: core_uobject.Rotator
    LocalStartLocation: core_uobject.Vector
    LocalStartDirection: core_uobject.Vector
    Velocity: core_uobject.Vector
    GravityScale: float
    BodyComponent: engine.StaticMeshComponent
    TracerComponent: engine.ParticleSystemComponent
    Components: unreal.WrappedArray[engine.PrimitiveComponent]
    NumBounces: int
    DamageModifierComp: gbx_game_system_core.DamageModifierComponent
    def SetLifetime(self, NewLifetime: float): ...
    def SetHomingTargetLocation(self, HomingLocation: core_uobject.Vector): ...
    def SetHomingTarget(self, HomingTarget: engine.Actor, TargetOffset: core_uobject.Vector): ...
    def PlayFeedbackSoundEvent(self, Event: wwise_audio.WwiseEvent): ...
    def OnRep_Shutdown(self): ...
    def OnRep_InitialClientState(self): ...
    def OnRep_Impact(self): ...
    def OnRep_Exploded(self): ...
    def OnRep_Attached(self): ...
    def OnParticleSystemFinished(self, FinishedComponent: engine.ParticleSystemComponent): ...
    def OnAttachedComponentUnregistered(self, UnregisteredComponent: engine.ActorComponent): ...
    def OnAttachedComponentCollisionChanged(self, ChangedComponent: engine.PrimitiveComponent): ...
    def OnAttachedActorFractured(self, HitPoint: core_uobject.Vector, HitDirection: core_uobject.Vector): ...
    def OnAttachedActorDestroyed(self, DestroyedActor: engine.Actor): ...
    def K2_ApplyImpactDamage(self, Hit: engine.HitResult, ImpactDamage: float, bPenetrated: bool, bCanReflect: bool): ...
    def IsHomingMovingDirectlyTowardsTarget(self, ReturnValue: bool) -> bool: ...
    def IsHoming(self, ReturnValue: bool) -> bool: ...
    def InitChildData(self, InitData: LightProjectileInitializationData): ...
    def GetTarget(self, ReturnValue: engine.Actor) -> engine.Actor: ...
    def GetSource(self, ReturnValue: engine.Actor) -> engine.Actor: ...
    def GetModifierValue(self, ReturnValue: float) -> float: ...
    def GetModifierType(self, ReturnValue: EWeaponShotModifierType) -> EWeaponShotModifierType: ...
    def GetInstigator(self, ReturnValue: engine.Pawn) -> engine.Pawn: ...
    def GetImpactDataOverride(self, ReturnValue: gbx_game_system_core.ImpactData) -> gbx_game_system_core.ImpactData: ...
    def GetImpactData(self, ReturnValue: gbx_game_system_core.ImpactData) -> gbx_game_system_core.ImpactData: ...
    def GetHomingStartTime(self, ReturnValue: float) -> float: ...
    def GetFiringPatternID(self, ReturnValue: int) -> int: ...
    def GetDamageType(self, ReturnValue: gbx_game_system_core.GbxDamageType) -> gbx_game_system_core.GbxDamageType: ...
    def GetDamageCauser(self, ReturnValue: engine.Actor) -> engine.Actor: ...
    def GetAttitudeTowards(self, TargetActor: engine.Actor, ReturnValue: int) -> int: ...
    def GetAttachedImpactNormal(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetAttachedDamageReceiverActor(self, ReturnValue: engine.Actor) -> engine.Actor: ...
    def GetAttachedActor(self, ReturnValue: engine.Actor) -> engine.Actor: ...
    def GetAssociatedActor(self, ActorType: ELightProjectileQueryActorType, ReturnValue: engine.Actor) -> engine.Actor: ...
    def Explode(self, Delay: float): ...
    def EnableHoming(self): ...
    def DisableHoming(self): ...
    def Destroy(self): ...
    def ApplyAreaDamage(self, Origin: core_uobject.Vector, HitActor: engine.Actor, Hit: engine.HitResult): ...


class LightProjectileData(unreal.UObject):
    ProjectileClass: unreal.UClass
    BodyMesh: engine.StaticMesh
    BodyTransform: core_uobject.Transform
    TracerSignificanceEvent: gbx_game_system_core.GbxSignificanceEvent
    MaxTracerThrottleLevel: ELightProjectileTracerThrottleLevel
    TracerFX: engine.ParticleSystem
    TracerFXCollection: unreal.UClass
    TracerFXBodySocket: str
    TracerFXTransform: core_uobject.Transform
    ImpactData: gbx_game_system_core.ImpactData
    bPlayImpactEffectOnExplode: bool
    ExplosionData: gbx_game_system_core.ExplosionData
    DamageInstigatorFeedback: gbx_game_system_core.FeedbackData
    AttachedFX: engine.ParticleSystem
    AttachedFXCollection: unreal.UClass
    AttachedFXBodySocket: str
    AttachedFXTransform: core_uobject.Transform
    BounceEffectDelay: float
    Speed: float
    MaxSpeed: float
    InitialRelativeRotation: core_uobject.Rotator
    Acceleration: float
    GravityScale: float
    Friction: float
    RicochetFriction: float
    BounceFriction: float
    Bounciness: float
    MoveModifiers: unreal.WrappedArray[LightProjectileMoveModifier]
    LifeTime: float
    bAttachedLifetimeEnabled: bool
    AttachedLifetime: float
    TraceChannel: int
    TraceInterval: float
    CollisionRadius: float
    MaxRicochet: int
    MaxBounces: int
    MaxReflections: int
    ProxyRadius: float
    ProxyTraceChannel: int
    bIgnoreCollisionWithInstigator: bool
    bSetTeamCollision: bool
    bIgnoreCollisionWithInstigatorTeam: bool
    bPenetratesTargetables: bool
    bPenetratesWorld: bool
    bBounceOffTargetables: bool
    bCollideWithSource: bool
    bEnableProxyCollisionEvents: bool
    CollideWithSourceDelay: float
    TimedEvents: unreal.WrappedArray[LightProjectileTimedEvent]
    BulletSensePerception: gbx_game_system_core.BulletPerceptionProperties
    ImpactSoundPerception: gbx_game_system_core.SoundPerceptionProperties
    bCanTriggerBulletDodges: bool
    bTargetedImpactRadiusDamage: bool
    DamageRadius: gbx_game_system_core.AttributeInitializationData
    DamageSource: unreal.UClass
    DamageAreaData: unreal.UClass
    DamageData: unreal.UClass
    DamageAreaHitOffset: float
    bDamageFalloff: bool
    bRequiresInstigatorToDoDamage: bool
    AttachDamageScale: float
    ImpactedActorDamageScale: gbx_game_system_core.AttributeInitializationData
    ConditionalDamageModifiers: unreal.WrappedArray[gbx_game_system_core.ConditionalDamageModifier]
    AudioProperties: LightProjectileAudioProperties
    AttachedSound: wwise_audio.WwiseEvent
    bCanAttachToTargetables: bool
    bCanAttachToFriendlies: bool
    bCanAttachToWorld: bool
    bHideBodyOnAttach: bool
    bDeactivateTracerFXOnAttach: bool
    DeactivateTracerFXEmitterOnAttach: str
    bEnableHomingOnSpawn: bool
    bOverrideAimAssistSettings: bool
    MagnetismRate: core_uobject.Vector2D
    MaxMagnetismDeflection: float
    RingSettings: LightProjectileRingSettings
    bMakeProjectileRing: bool
    bCallOnDamageEventOncePerHit: bool
    def OnRicochet(self, Projectile: LightProjectile, Hit: engine.HitResult, ImpactVelocity: core_uobject.Vector): ...
    def OnProxyImpact(self, Projectile: LightProjectile, Hit: engine.HitResult): ...
    def OnLifetimeExpired(self, Projectile: LightProjectile): ...
    def OnImpact(self, Projectile: LightProjectile, Hit: engine.HitResult): ...
    def OnExplode(self, Projectile: LightProjectile): ...
    def OnDamage(self, Projectile: LightProjectile, Hit: engine.HitResult, bCritical: bool): ...
    def OnBegin(self, Projectile: LightProjectile): ...
    def OnAttached(self, Projectile: LightProjectile, AttachedActor: engine.Actor): ...
    def GetTimedEventNameList(self, FuncList: unreal.WrappedArray[str]): ...


class LightBeamManager(engine.Actor):
    ActiveBeams: unreal.WrappedArray[LightBeam]
    BeamPool: unreal.WrappedArray[LightBeam]
    ActiveParticles: unreal.WrappedArray[engine.ParticleSystemComponent]
    ParticlesPool: unreal.WrappedArray[LightBeamParticlePoolData]
    def OnParticleSystemFinished(self, FinishedComponent: engine.ParticleSystemComponent): ...


class LightBeam(unreal.UObject):
    Data: LightBeamData
    Component: engine.ParticleSystemComponent
    AltViewComponent: engine.ParticleSystemComponent
    DamageInterval: float
    LockOnContactTime: float
    LockOnBreakRadius: float
    LockOnBreakAngle: float
    ClientState: ClientLightBeamState
    ModifierType: EWeaponShotModifierType
    ModifierValue: float
    StartTime: float
    LastDamagedActor: engine.Actor
    DamagedActors: unreal.WrappedArray[engine.Actor]
    LastDamagedActorContinuousContact: float
    LastImpact: engine.HitResult
    ParentBeam: LightBeam
    RootParentBeam: LightBeam
    ChildBeams: unreal.WrappedArray[LightBeam]
    TrackingImpactEffects: unreal.WrappedArray[LightBeamImpactFXTrackingData]
    def SetTargetSocket(self, Socket: str): ...
    def OnTrackedImpactParticleSystemFinished(self, PSC: engine.ParticleSystemComponent): ...
    def OnRep_ModifierValue(self): ...
    def OnRep_ModifierType(self): ...
    def OnRep_ClientState(self): ...
    def LockOntoTarget(self, Target: LightBeamAttachment): ...
    def InitChildData(self, InitData: LightBeamInitializationData): ...
    def GetTargetActor(self, ReturnValue: engine.Actor) -> engine.Actor: ...
    def GetTarget(self, ReturnValue: LightBeamAttachment) -> LightBeamAttachment: ...
    def GetSourceActor(self, ReturnValue: engine.Actor) -> engine.Actor: ...
    def GetSource(self, ReturnValue: LightBeamAttachment) -> LightBeamAttachment: ...
    def GetInstigator(self, ReturnValue: engine.Pawn) -> engine.Pawn: ...
    def GetImpactForce(self, ReturnValue: float) -> float: ...
    def GetDamageType(self, ReturnValue: gbx_game_system_core.GbxDamageType) -> gbx_game_system_core.GbxDamageType: ...
    def GetDamageCauser(self, ReturnValue: engine.Actor) -> engine.Actor: ...
    def GetDamage(self, ReturnValue: float) -> float: ...
    def GetAssociatedActor(self, ActorType: ELightBeamQueryActorType, ReturnValue: engine.Actor) -> engine.Actor: ...


class LightBeamData(unreal.UObject):
    BeamClass: unreal.UClass
    LifeTime: float
    BeamFX: engine.ParticleSystem
    BeamFXCollection: unreal.UClass
    ViewerBeamFX: engine.ParticleSystem
    ViewerBeamFXCollection: unreal.UClass
    LoopingImpactAudio: wwise_audio.WwiseEvent
    AudioFXCollection: unreal.UClass
    SourceTangentStrengthOverDistance: float
    TargetTangentStrengthOverDistance: float
    BeamEmitterName: str
    ExplosionData: gbx_game_system_core.ExplosionData
    ImpactData: gbx_game_system_core.ImpactData
    ImpactFXFrequency: float
    bShowPenetrationImpacts: bool
    bNoImpactDecals: bool
    TraceChannel: int
    CollisionRadius: float
    TraceInterval: float
    NumTraceSteps: int
    MaxLength: float
    StartLength: float
    GrowSpeed: float
    bGrowOverTime: bool
    bSetTeamCollision: bool
    bIgnoreCollisionWithInstigatorTeam: bool
    bPenetratesTargetables: bool
    bPenetratesWorld: bool
    bCanTriggerBulletDodges: bool
    LockType: ELightBeamLock
    bCanAcquireLock: bool
    bAlignToLockedTarget: bool
    bCanLockOntoFriendlies: bool
    bWorldCollisionBreaksLock: bool
    DamageInterval: float
    bDamageDirectTargetOnce: bool
    DamageData: unreal.UClass
    ConditionalDamageModifiers: unreal.WrappedArray[gbx_game_system_core.ConditionalDamageModifier]
    bEnableDamageProxy: bool
    DamageProxyRadius: float
    DamageProxyTraceChannel: int
    DamageProxyRadiusCurve: engine.RuntimeFloatCurve
    bScaleDamageProxyRadiusByCurve: bool
    bDisableDragWhenLocked: bool
    DragSpeed: float
    MaxDragRadius: float
    SpreadWaveforms: unreal.WrappedArray[gbx_game_system_core.Vector2DWaveform]
    bSpreadWaveformIsAngle: bool
    SpreadWaveformTimeScale: float
    LockOnSpreadScale: float
    bApplyAccuracyToSpread: bool
    MaxChains: int
    MaxChainDepth: int
    ChainBeamData: unreal.UClass
    ChainTargetsQuery: aimodule.EnvQuery
    ChainTargetsQueryMaxRangeParam: str
    ChainDelay: float
    ChainInterval: float
    MaxChainDistance: float
    ChainBreakDistance: float
    NetUpdateTime: float
    def UpdateTarget(self, Beam: LightBeam, ReturnValue: float) -> float: ...
    def CanLockOn(self, Beam: LightBeam, TargetActor: engine.Actor, ReturnValue: bool) -> bool: ...


class WeaponAnimInstance(engine.AnimInstance):
    Weapon: Weapon
    Slot: WeaponAttachmentSlot
    ZoomDuration: float
    ZoomEffect: float
    bIsZoomedIn: bool
    def BlueprintSwitchedMode(self, NewMode: int): ...


class WeaponAudioProviderComponent(engine.ActorComponent): ...


class WalkingProjectileMovementComponent(GbxProjectileMovementComponent):
    bGravityAffectsSlopeWalking: bool
    MaxWalkAngle: float
    bFallOffLedges: bool
    MaxStepUpHeight: float
    MovementFrozenMaxTime: float
    bBounceOffWalls: bool
    MaxWallBounces: int
    WallBounciness: float
    bOverrideWalkingSpeed: bool
    WalkingSpeedOverride: float



class WeaponAmmoComponent(engine.ActorComponent):
    AmmoTypeData: GbxAmmoTypeData
    bDisplayAmmoInHUD: bool
    WeaponPrivate: Weapon
    def ClientRefillAmmo(self, Amount: int): ...


class WeaponHeatComponent(engine.ActorComponent):
    HeatCoolDownRate: engine.GbxAttributeFloat
    HeatCoolDownDelay: engine.GbxAttributeFloat
    UseHeatImpulse: engine.GbxAttributeFloat
    ActiveHeatRate: engine.GbxAttributeFloat
    bSimulateOnClients: bool
    bSimulateOnAI: bool
    bVisibleInHUD: bool
    bStartCoolDownEffectOnEndUse: bool
    bCanOverheat: bool
    bCanUseWhenOverheated: bool
    OverheatTime: engine.GbxAttributeFloat
    OverheatCoolDownDelay: engine.GbxAttributeFloat
    HeatEvents: unreal.WrappedArray[WeaponHeatEventNotify]
    HeatMaterialParamName: str
    HeatMaterialParamCurve: engine.CurveFloat
    CoolDownEffectType: int
    CoolDownEffectOnThreshold: float
    CoolDownEffectOffThreshold: float
    Heat: float
    ReplicatedHeat: int
    bOverheated: bool
    WeaponPrivate: Weapon
    def SetCanUseWhenOverheated(self, bEnabled: bool): ...
    def OnUseFinished(self): ...
    def OnUsed(self): ...
    def OnStopOverheat(self): ...
    def OnStartOverheat(self): ...
    def OnRep_ReplicatedHeat(self): ...
    def OnRep_Overheated(self, bWasOverheated: bool): ...
    def OnPutDown(self): ...
    def OnEquipped(self): ...
    def OnDetached(self): ...
    def OnAttached(self): ...


class WeaponReloadComponent(engine.ActorComponent):
    ReloadPartType: int
    ReloadTime: engine.GbxAttributeFloat
    WeaponPrivate: Weapon



class WeaponZoomComponent(engine.ActorComponent):
    ZoomLevels: unreal.WrappedArray[WeaponZoomLevel]
    InstigatorAccuracyScale: float
    ViewModelShotOffsetScale: float
    ViewModelLeadingScale: float
    MovementAnimationAlpha: float
    FlinchAnimationMagnitudeScale: float
    bForceUnzoomWhenSwitchingModes: bool
    ModeFOVScale: float
    ModeTransitionDuration: float
    EyeSocket: str
    bUseScopeSocket: bool
    FrontScopeSocket: str
    FrontSightSocket: str
    RearSightSocket: str
    FOVScale: float
    DurationScale: float
    bShowCrosshairWhenZoomed: bool
    bApplyAttributesWhenFullyZoomed: bool
    AttributeEffects: unreal.WrappedArray[gbx_game_system_core.AttributeEffectData]
    InstigatorAttributeEffects: unreal.WrappedArray[gbx_game_system_core.AttributeEffectData]
    DepthOfFieldFocusSocket: str
    bEnableBlurVignetteSize: bool
    bOverrideStartBlurVignetteSize: bool
    bOverrideBlurVignetteSharpness: bool
    bEnableColorVignetteSize: bool
    bOverrideStartColorVignetteSize: bool
    bOverrideColorVignetteSharpness: bool
    bOverrideLongitudinalMotionScale: bool
    bOverrideLateralMotionScale: bool
    BlurVignetteSize: float
    StartBlurVignetteSize: float
    BlurVignetteSharpness: float
    ColorVignetteSize: float
    StartColorVignetteSize: float
    ColorVignetteSharpness: float
    LongitudinalMotionScale: float
    LateralMotionScale: float
    UseFeedback: gbx_game_system_core.FeedbackData
    UseFeedbackScale: float
    bApplyWeaponModeZoom: bool
    ZoomState: WeaponZoomState
    ReplicatedZoomState: WeaponZoomState
    DesiredZoomLevel: int
    ZoomStartTime: float
    ZoomTransitionStartTime: float
    AttributeModifiers: unreal.WrappedArray[gbx_game_system_core.GbxAttributeModifierHandle]
    InstigatorAttributeModifiers: unreal.WrappedArray[gbx_game_system_core.GbxAttributeModifierHandle]
    CachedWeaponModeIndex: int
    WeaponPrivate: Weapon
    def OnSwitchedWeaponMode(self): ...
    def OnRep_ReplicatedZoomState(self): ...
    def OnDetached(self): ...
    def OnAttached(self): ...
    def GetMaxZoomFOVScaleWithMode(self, ModeIndex: int, ReturnValue: float) -> float: ...
    def GetMaxZoomFOVScale(self, ReturnValue: float) -> float: ...


class AmmoProviderInterface(core_uobject.Interface): ...


class WeaponAnimNotify(engine.AnimNotify):
    bTriggerOnFirstPerson: bool



class AnimNotify_AmmoReloaded(WeaponAnimNotify): ...


class AnimNotify_EquipInterruptible(WeaponAnimNotify): ...


class AnimNotify_WeaponSkeletalControlEvent(WeaponAnimNotify):
    ControlType: int
    ControlName: str
    ControlEvent: EWeaponSkeletalControlEvent
    ControlInput: float



class BodyWeaponHoldData(gbx_runtime.GbxDataAsset):
    HoldName: str
    HoldNames: unreal.WrappedArray[str]
    WeaponActions: unreal.WrappedArray[BodyWeaponActionInfo]
    DepthOfFieldForegroundFocusDistance: float
    DepthOfFieldForegroundFocusNearRegionPct: float



class BodyWeaponHoldManagerComponent(engine.ActorComponent):
    DefaultWeaponHold: BodyWeaponHoldData
    WeaponHolds: unreal.WrappedArray[BodyWeaponHoldData]
    UnarmedHoldName: str



class EnvQueryContext_ProjectileProxy(aimodule.EnvQueryContext): ...


class EnvQueryGenerator_FindProjectileTargets(aimodule.EnvQueryGenerator):
    Range: aimodule.AIDataProviderFloatValue
    TargetSkipRangeCheckCondition: gbx_runtime.GbxCondition
    bAllowHostiles: bool
    bAllowFriendlies: bool
    bAllowNeutrals: bool
    bAlsoFindTargetableComponents: bool
    bIgnoreNonHostileAttachedParent: bool



class EnvQueryItemType_ProjectileProxy(aimodule.EnvQueryItemType_VectorBase): ...


class FiringPattern(gbx_runtime.GbxDataAsset):
    Samples: unreal.WrappedArray[FiringPatternSample]
    bFireRandomlyFromPattern: bool
    bResetPatternAfterEachShot: bool
    bScalePattern: bool
    bLerpAcrossFiringLineBasedOnProjectileCountWithinEachShot: bool
    bSuppressWeaponSpread: bool
    bSingleWeaponSpread: bool
    bDisableTracerThrottling: bool
    BasePatternScale: float
    MinPatternScale: float
    RequiredProjectilesPerShot: int



class FiringPatternData(unreal.UObject):
    Samples: unreal.WrappedArray[FiringPatternSample]
    bFireRandomlyFromPattern: bool
    bResetPatternAfterEachShot: bool
    bScalePattern: bool
    bLerpAcrossFiringLineBasedOnProjectileCountWithinEachShot: bool
    bSuppressWeaponSpread: bool
    bSingleWeaponSpread: bool
    BasePatternScale: float
    MinPatternScale: float
    RequiredProjectilesPerShot: int



class GbxAmmoTypeData(gbx_runtime.GbxDataAsset):
    DisplayName: str
    DisplayIcon: engine.Texture2D
    ScaleformDisplayFrameID: str
    ResourceData: gbx_game_system_core.GameResourceData
    RegenerationRate: float



class GbxProjectileManager(gbx_game_system_core.IGbxProjectileManager):
    HomingComponents: unreal.WrappedArray[gbx_game_system_core.ProjectileHomingComponent]



class GbxTrajectometerComponent(engine.ActorComponent):
    SimulatorProjectile: GbxTrajectometerProjectile
    TrailParticle: engine.ParticleSystemComponent
    ProjectileUpdatedComp: engine.SceneComponent
    bEnableOnStart: bool
    SimulationStepTime: float
    SimulationMaxTime: float
    SimulatorTemplate: unreal.UClass
    ProjectileSpeed: gbx_game_system_core.AttributeInitializationData
    ProjectileMaxSpeed: gbx_game_system_core.AttributeInitializationData
    ProjectileAcceleration: gbx_game_system_core.AttributeInitializationData
    ProjectileGravityScale: gbx_game_system_core.AttributeInitializationData
    ProjectileInitialDirection: core_uobject.Vector
    TraceSettings: GbxTrajectometerTraceData
    ProjectileToSimulate: unreal.UClass
    TrailEmitterTemplate: engine.ParticleSystem
    OverrideSocket: str
    bStartFromWeapon: bool
    bStartFromViewLocation: bool
    bUseSocketAsStartRotation: bool
    bSimulateWeaponProjectile: bool
    bUseProjectileForCollision: bool
    bConvergeTowardsAimLocation: bool
    def UpdateCollisionShape(self): ...
    def SimulationResultEvent__DelegateSignature(self, HitResult: engine.HitResult): ...
    def SetTrajectometerEnabled(self, bEnabled: bool): ...


class GbxTrajectometerProjectile(Projectile):
    TrailParticle: engine.ParticleSystemComponent



class GbxWeaponUserInterface(gbx_game_system_core.WeaponUserInterface): ...


class LightBeamStatics(engine.BlueprintFunctionLibrary):

    def SetBeamFlag(self, InitData: LightBeamInitializationData, Flag: ELightBeamFlag): ...
    def RemoveLightBeamsBySource(self, Source: engine.Actor, NameId: str): ...
    def RemoveLightBeamsByActor(self, Query: LightBeamQueryData): ...
    def IsBeamFlagSet(self, InitData: LightBeamInitializationData, Flag: ELightBeamFlag, ReturnValue: bool) -> bool: ...
    def DoesLightBeamExist(self, Query: LightBeamQueryData, ReturnValue: bool) -> bool: ...
    def CreateLightBeamFromData(self, InitData: LightBeamInitializationData): ...
    def CreateLightBeam(self, Data: unreal.UClass, Instigator: engine.Pawn, Source: LightBeamAttachment, Target: LightBeamAttachment, bTargetLocked: bool, NameId: str, Damage: float, DamageType: unreal.UClass, DamageSource: unreal.UClass, DamageRadius: float, DamageCauser: engine.Actor, ImpactDataOverride: gbx_game_system_core.ImpactData, ImpactForce: gbx_game_system_core.ForceSelection, LifetimeOverride: float, bViewDependent: bool): ...
    def ClearBeamFlag(self, InitData: LightBeamInitializationData, Flag: ELightBeamFlag): ...


class LightProjectileMoveModifier(unreal.UObject):
    FiringPatternID: int
    bRestrictFiringPattern: bool



class LightProjectileAimViewPointHomingModifier(LightProjectileMoveModifier):
    LookAheadDistance: float



class LightProjectileCurveModifier(LightProjectileMoveModifier):
    StartTangentMultiplier: float



class LightProjectileHomingModifier(LightProjectileMoveModifier):
    MaxTurnRate: core_uobject.Rotator
    StartApproachDistance: float
    FinalApproachDistance: float
    ApproachTurnRateScale: float
    ApproachEaseInFunc: gbx_game_system_core.GbxEasingFunc
    bBreakHomingWhenPassingTargetDuringFinalApproach: bool
    EaseInTime: float
    EaseInFunc: gbx_game_system_core.GbxEasingFunc
    StopHomingDistance: float



class LightProjectileRandomDrunkenModifier(LightProjectileMoveModifier):
    PathCorrectionInterval: float
    TurnSpeed: float
    MaxSpreadAngle: float
    MaxDepartureAngle: float
    bGravityAffectsDrunkenness: bool
    DrunkenGravityScalar: float
    StartApproachDistance: float
    StartDelayTime: float
    EaseInTime: float
    bNormalizedEaseTime: bool
    EaseInFunc: gbx_game_system_core.GbxEasingFunc



class LightProjectileStatics(engine.BlueprintFunctionLibrary):

    def SplitLightProjectile(self, Projectile: LightProjectile, Data: unreal.UClass, Pattern: ELightProjectileSplitPattern, Count: int, SpreadAngle: float, RotateAngle: float, OffsetDistance: float, bDestroySource: bool): ...
    def SetProjectileFlag(self, InitData: LightProjectileInitializationData, Flag: ELightProjectileFlag): ...
    def SetHomingState(self, Query: LightProjectileQueryData, bIsHoming: bool): ...
    def RemoveLightProjectilesByActor(self, Query: LightProjectileQueryData): ...
    def IsProjectileFlagSet(self, InitData: LightProjectileInitializationData, Flag: ELightProjectileFlag, ReturnValue: bool) -> bool: ...
    def DetonateLightProjectiles(self, Query: LightProjectileQueryData, StackingEnemyBonusDamage: float, MinDetonationDelay: float, MaxDetonationDelay: float): ...
    def CreateLightProjectileFromSource(self, SourceProjectile: LightProjectile, Data: unreal.UClass, Location: core_uobject.Vector, Direction: core_uobject.Vector, Damage: float): ...
    def CreateLightProjectileFromDataAsync(self, InitData: LightProjectileInitializationData, ForceSpawnTimer: float): ...
    def CreateLightProjectileFromData(self, InitData: LightProjectileInitializationData): ...
    def CreateLightProjectile(self, Data: unreal.UClass, Location: core_uobject.Vector, Direction: core_uobject.Vector, Instigator: engine.Pawn, Source: engine.Actor, DamageCauser: engine.Actor, Damage: float, DamageType: unreal.UClass, DamageSource: unreal.UClass, ImpactDataOverride: gbx_game_system_core.ImpactData): ...
    def ClearProjectileFlag(self, InitData: LightProjectileInitializationData, Flag: ELightProjectileFlag): ...


class LightProjectileWaveModifier(LightProjectileMoveModifier):
    Waveforms: unreal.WrappedArray[gbx_game_system_core.Vector2DWaveform]
    GlobalWaveformScale: float
    Waveform: gbx_game_system_core.VectorWaveform
    EaseInTime: float
    bNormalizedEaseTime: bool
    EaseInFunc: gbx_game_system_core.GbxEasingFunc
    bRandomize: bool



class ProjectileBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def ThrowProjectileAsync(self, WorldContext: unreal.UObject, Request: ThrowProjectileAsyncRequest, ReturnValue: int) -> int: ...
    def ThrowActorAt(self, Actor: engine.Actor, TargetLocation: core_uobject.Vector, TargetVelocity: core_uobject.Vector, MaxPrediction: float, Speed: float, AnglePercent: float, DirectionOffset: core_uobject.Rotator, LocalTargetOffset: core_uobject.Vector): ...
    def PredictProjectilePathAsync(self, WorldContext: unreal.UObject, Request: PredictProjectilePathAsyncRequest): ...
    def GetSafeProjectileThrowTransform_Component(self, SourceActor: engine.Actor, SourceComponent: engine.SceneComponent, SocketName: str, IgnoreActors: unreal.WrappedArray[engine.Actor], TraceChannel: int, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def GetSafeProjectileThrowTransform(self, SourceActor: engine.Actor, SocketName: str, IgnoreActors: unreal.WrappedArray[engine.Actor], bThrowFromFirstPersonSocket: bool, TraceChannel: int, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def GeneratePointsOnFan(self, Origin: core_uobject.Vector, Direction: core_uobject.Vector, SampleCount: int, SpreadAngle: float, RotateAngle: float, OriginOffset: float, ReturnValue: unreal.WrappedArray[core_uobject.Transform]) -> unreal.WrappedArray[core_uobject.Transform]: ...
    def GeneratePointsOnCone(self, Origin: core_uobject.Vector, Direction: core_uobject.Vector, SampleCount: int, SpreadAngle: float, RotateAngle: float, OriginOffset: float, ReturnValue: unreal.WrappedArray[core_uobject.Transform]) -> unreal.WrappedArray[core_uobject.Transform]: ...
    def DetachProjectilesFromActor(self, BaseActor: engine.Actor): ...
    def CalculateConeVector(self, Fraction: float, Origin: core_uobject.Vector, Direction: core_uobject.Vector, AngleWidth: float, AngleHeight: float, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def CalcThrowVelocityAtActor(self, ResultVelocity: core_uobject.Vector, ResultGravityScale: float, StartLocation: core_uobject.Vector, Target: engine.Actor, MaxPrediction: float, Speed: float, AnglePercent: float, DirectionOffset: core_uobject.Rotator, LocalTargetOffset: core_uobject.Vector): ...
    def CalcThrowVelocity(self, WorldContextObject: unreal.UObject, ResultVelocity: core_uobject.Vector, ResultGravityScale: float, StartLocation: core_uobject.Vector, TargetLocation: core_uobject.Vector, TargetVelocity: core_uobject.Vector, MaxPrediction: float, Speed: float, AnglePercent: float, DirectionOffset: core_uobject.Rotator, LocalTargetOffset: core_uobject.Vector): ...


class ProjectileEQSProxy(unreal.UObject):
    Location: core_uobject.Vector
    Rotation: core_uobject.Rotator
    ReferenceActor: engine.Actor



class ProjectileSourceInterface(core_uobject.Interface): ...


class RecoilControlComponent(engine.ActorComponent):
    bServerSimulatesRecoil: bool
    CurrentRotation: core_uobject.Rotator
    TargetRotation: core_uobject.Rotator
    InputPassthroughThreshold: core_uobject.Rotator



class RecoilPatternData(gbx_runtime.GbxDataAsset):
    Samples: unreal.WrappedArray[core_uobject.Vector2D]
    bRandom: bool
    EndOfPatternAction: ERecoilEndOfPatternAction
    RepeatPatternStartIndex: int
    EndOfPatternRise: float
    ShotSequenceScaleCurve: engine.RuntimeFloatCurve
    bAutoGenerateGoodness: bool
    PatternHeightGoodness: float
    PatternWidthGoodness: float



class WeaponAccuracyPoolAttributePropertyValueResolver(gbx_game_system_core.AttributePropertyValueResolver):
    DefaultResource: gbx_game_system_core.GameResourceData



class WeaponSkeletalControlBase(unreal.UObject):
    ControlName: str
    bAlwaysUpdate: bool
    bUpdateWhenAmmoChanges: bool
    bStartPaused: bool
    bSyncToFireRate: bool
    bAddInputOnUse: bool
    UseInputValue: gbx_game_system_core.AttributeInitializationData
    MinFireRate: float
    MaxFireRate: float
    ReceivedInputSound: wwise_audio.WwiseEvent
    bAttachToBone: bool
    bUseDefaultAudioComponent: bool



class WeaponAmmoChamberBoneControl(WeaponSkeletalControlBase):
    AmmoBoneNames: unreal.WrappedArray[str]



class WeaponConsumedLoadedAmmoValueResolver(gbx_game_system_core.AttributeValueResolver): ...


class WeaponAmmoPoolComponent(WeaponAmmoComponent):
    MaxLoadedAmmo: engine.GbxAttributeInteger
    MaxStoredAmmo: int
    LoadedAmmo: int
    StoredAmmo: int
    SpareAmmo: int
    bInfiniteAmmo: bool
    bInfiniteAmmoForAI: bool
    bCreateAmmoResourceForAI: bool
    bGiveAmmoOnPickup: bool
    ResourceData: gbx_game_system_core.GameResourceData
    PickupAmmoFormula: gbx_game_system_core.AttributeInitializationData
    AmmoRegenType: EAmmoRegenType
    AmmoRegenRate: float
    ConsumeAmmoRegenDelay: float
    ResourcePool: gbx_game_system_core.GameResourcePoolReference
    ServerSyncedLoadedAmmo: int
    def ServerSendAmmoState(self): ...
    def OnRep_SpareAmmo(self): ...
    def OnRep_ServerSyncedLoadedAmmo(self): ...
    def OnMaxLoadedAmmoChanged(self, OldValue: float, NewValue: float): ...
    def OnGivenTo(self): ...
    def ClientSetLoadedAmmo(self, NewLoadedAmmo: int): ...
    def ClientConsumeAmmo(self, Amount: int): ...


class WeaponAmmoRegenAttributeValueResolver(gbx_game_system_core.AttributeValueResolver): ...


class WeaponAttachmentSlot(unreal.UObject):
    AttachSocket: str
    Mesh: engine.MeshComponent
    TextureMipsSetting: EWeaponTextureMipsSetting
    CachedForceMipTextures: unreal.WrappedArray[engine.Texture]
    AttachmentEffects: unreal.WrappedArray[WeaponEffectAttachment]
    ActiveMaterialEffects: unreal.WrappedArray[WeaponMaterialEffectInstance]
    ActiveSkeletalControls: unreal.WrappedArray[WeaponSkeletalControlInstance]
    TrinketAttachments: unreal.WrappedArray[WeaponTrinketAttachment]
    SecondaryMeshes: unreal.WrappedArray[engine.MeshComponent]
    def SetMesh(self, InMesh: engine.MeshComponent): ...


class WeaponAttributeContextResolver(gbx_game_system_core.AttributeContextResolver): ...


class WeaponChargePercentValueResolver(gbx_game_system_core.AttributeValueResolver): ...


class WeaponChargeComponent(WeaponPreUseComponent):
    ChargeTime: engine.GbxAttributeFloat
    DischargeTime: engine.GbxAttributeFloat
    CancelChargeDelay: engine.GbxAttributeFloat
    RequiredUseChargePct: float
    CommitUseChargePct: float
    OverchargeHoldTime: engine.GbxAttributeFloat
    bUseWhenCharged: bool
    bChargeBeforeEachUse: bool
    bStopChargingEffectsOnCharged: bool
    bStopChargedEffectsOnOvercharged: bool
    bUpdateChargeActionBlendSpace: bool
    bZoomModifiesBlendSpaceY: bool
    ChargePercentParamName: str
    ZoomChargeActionBlendSpaceScale: float
    AttributeEffects: unreal.WrappedArray[WeaponChargeAttributeEffect]
    ChargeFeedback: gbx_game_system_core.FeedbackData
    OverchargeFeedback: gbx_game_system_core.FeedbackData
    bPlayFeedbackAtLocation: bool
    FeedbackSocket: str
    ChargeEvents: unreal.WrappedArray[WeaponChargeEventNotify]
    DischargeEvents: unreal.WrappedArray[WeaponChargeEventNotify]
    ChargeState: EWeaponChargeState
    def StopEffects(self): ...
    def Overcharged(self): ...
    def OnRep_ChargeState(self, PrevChargeState: EWeaponChargeState): ...
    def OnChargeActionEnd(self, EndState: gbx_game_system_core.EGbxActionEndState): ...
    def GetDischargeDuration(self, ReturnValue: float) -> float: ...
    def GetChargePercent(self, ReturnValue: float) -> float: ...
    def GetChargeDuration(self, ReturnValue: float) -> float: ...
    def FullyDischarged(self): ...
    def FullyCharged(self): ...
    def DelayChargeFinished(self): ...


class WeaponClipReloadComponent(WeaponReloadComponent):
    ReloadCompletePercent: float
    TapedReloadTime: engine.GbxAttributeFloat
    TapedReloadCompletePercent: float
    TapedClipCount: int
    ClientReloadState: int
    CurrentClip: int
    def OnRep_ClientReloadState(self): ...


class GbxCondition_ZoomState(gbx_runtime.GbxCondition):
    bIsZoomedIn: bool
    bIncludeTransitions: bool



class WeaponDebugInterface(core_uobject.Interface): ...


class WeaponFireBeamComponent(WeaponFireComponent):
    DamageRateScale: float
    LightBeamData: unreal.UClass
    bFollowPlayerCrosshair: bool
    LockOnContactTime: float
    LockOnBreakRadius: float
    LockOnBreakAngle: float
    DamageRampCurve: engine.CurveFloat
    DamageRampScale: engine.GbxAttributeFloat
    def GetShotLightBeamData(self, ReturnValue: unreal.UClass) -> unreal.UClass: ...


class WeaponFireRateAccelPercentValueResolver(gbx_game_system_core.AttributeValueResolver): ...


class WeaponRecoilComponent(engine.ActorComponent):
    CachedControlComponent: RecoilControlComponent
    WeaponPrivate: Weapon
    def OnUsed(self): ...
    def OnDetached(self): ...
    def OnAttached(self): ...


class WeaponRecoilGoodnessValueResolver(gbx_game_system_core.AttributeValueResolver): ...


class WeaponRecoilPatternComponent(WeaponRecoilComponent):
    Pattern: RecoilPatternData
    PatternWidthScale: engine.GbxAttributeFloat
    PatternHeightScale: engine.GbxAttributeFloat
    PatternZoomScale: engine.GbxAttributeFloat
    bScalePatternByFOV: bool
    bResetPatternWhenFiringEnds: bool
    RecoilSpeed: float
    RecoilRecoveryTime: float
    RecoilRecoveryDelayTime: float
    bStartRecoilRecoveryWhenFiringEnds: bool
    def ResetPattern(self): ...
    def OnUseFinished(self): ...
    def GetRecoilPatternWidthGoodness(self, ReturnValue: float) -> float: ...
    def GetRecoilPatternHeightGoodness(self, ReturnValue: float) -> float: ...
    def GetRecoilPatternGoodness(self, ReturnValue: float) -> float: ...


class WeaponSettings(engine.DeveloperSettings):
    WeaponEffectTypes: unreal.WrappedArray[WeaponEffectTypeName]
    WeaponActionTypes: unreal.WrappedArray[WeaponActionTypeName]
    LightProjectileFlags: unreal.WrappedArray[LightProjectileFlagName]
    LightBeamFlags: unreal.WrappedArray[LightBeamFlagName]
    WeaponShotModifierTypes: unreal.WrappedArray[WeaponShotModifierTypeName]



class WeaponShotModifier(gbx_runtime.GbxDataAsset):
    bTriggerEveryXShots: bool
    TriggerEveryXShots: gbx_game_system_core.AttributeInitializationData
    ModifierType: EWeaponShotModifierType
    bModifyDamage: bool
    DamageModifier: gbx_game_system_core.AttributeInitializationData
    DamageModifierType: EWeaponShotDamageModifierType
    bDistributeBetweenProjectiles: bool
    DamageType: unreal.UClass
    ImpactData: gbx_game_system_core.ImpactData
    CriticalHitModifier: gbx_game_system_core.ECriticalHitDamageOverride
    bUseDefaultCriticalHitMultiplier: bool
    AdditionalCriticalMultiplier: gbx_game_system_core.AttributeInitializationData
    GoreModifier: gbx_game_system_core.AttributeInitializationData
    GibModifier: gbx_game_system_core.AttributeInitializationData
    ConditionalDamageModifier: gbx_game_system_core.ConditionalDamageModifier
    bPassConditionalDamageModifierToChildProjectiles: bool
    bRefundShotCostWhenTriggered: bool
    bSuppressRefundThatWouldPreventReload: bool



class WeaponSimpleMotionControlBase(WeaponSkeletalControlBase):
    bStartActive: bool
    bAutoActivate: bool
    InputHandler: ESimpleMotionInputHandler
    ControlValue: gbx_game_system_core.AttributeInitializationData
    bLimitMinControlValue: bool
    bLimitMaxControlValue: bool
    MinControlValue: float
    MaxControlValue: float
    ControlImpulseSpeed: float
    ControlImpulseMaxValue: float
    ControlImpulseDecayDelay: float
    ControlImpulseDecaySpeed: float



class WeaponSimpleMotionBlendControl(WeaponSimpleMotionControlBase):
    bUseExistingNode: bool
    bMeshSpaceBlend: bool
    Animation: engine.AnimationAsset
    BlendLayerSetup: engine.InputBlendPose
    ActiveState: gbx_game_system_core.SimpleMotionState
    ActiveBlendTarget: float
    RecoveryState: gbx_game_system_core.SimpleMotionState



class WeaponSimpleMotionBoneControl(WeaponSimpleMotionControlBase):
    BoneName: str
    TranslationMode: int
    TranslationSpace: int
    IdleTranslation: core_uobject.Vector
    ActiveTranslation: core_uobject.Vector
    IdleTranslationState: gbx_game_system_core.SimpleMotionState
    ActiveTranslationState: gbx_game_system_core.SimpleMotionState
    RecoveryTranslationState: gbx_game_system_core.SimpleMotionState
    RotationMode: int
    RotationSpace: int
    IdleRotation: core_uobject.Rotator
    ActiveRotation: core_uobject.Rotator
    IdleRotationState: gbx_game_system_core.SimpleMotionState
    ActiveRotationState: gbx_game_system_core.SimpleMotionState
    RecoveryRotationState: gbx_game_system_core.SimpleMotionState
    ScaleMode: int
    ScaleSpace: int
    IdleScale: core_uobject.Vector
    ActiveScale: core_uobject.Vector
    IdleScaleState: gbx_game_system_core.SimpleMotionState
    ActiveScaleState: gbx_game_system_core.SimpleMotionState
    RecoveryScaleState: gbx_game_system_core.SimpleMotionState



class WeaponSingleFeedReloadComponent(WeaponReloadComponent):
    bDisableInterruptedToUse: bool
    SingleFeedIncrement: int
    SingleFeedCompletePercent: float
    ClientReloadState: int
    def OnUserInput(self, InputChannel: int): ...
    def OnRep_ClientReloadState(self): ...


class WeaponEffectShotStrengthValueResolver(gbx_game_system_core.AttributeValueResolver): ...


class WeaponStatics(engine.BlueprintFunctionLibrary):

    def UpdateVisibleAmmo(self, Weapon: Weapon): ...
    def UnhideWeapons(self, WeaponUser: engine.Actor, Reason: str): ...
    def UnhideWeapon(self, WeaponUser: engine.Actor, Slot: int, Reason: str): ...
    def SetVisibleAmmoUpdateMethod(self, Weapon: Weapon, NewUpdateMethod: EWeaponVisibleAmmoUpdateMethod): ...
    def SetVisibleAmmoState(self, Weapon: Weapon, NewState: EWeaponVisibleAmmoState): ...
    def ResetVisibleAmmoState(self, Weapon: Weapon): ...
    def RefillAmmo(self, Weapon: Weapon, Amount: int, bAsPercent: bool): ...
    def K2_PlayWeaponHoldActionEx(self, Actor: engine.Actor, WeaponAction: int, Weapon: Weapon, ActionParams: gbx_game_system_core.ActionState_Base, ReturnValue: gbx_game_system_core.GbxAction) -> gbx_game_system_core.GbxAction: ...
    def K2_PlayWeaponHoldAction(self, Actor: engine.Actor, WeaponAction: int, Weapon: Weapon, PlayRate: float, Duration: float, ReturnValue: gbx_game_system_core.GbxAction) -> gbx_game_system_core.GbxAction: ...
    def HideWeapons(self, WeaponUser: engine.Actor, Reason: str): ...
    def HideWeapon(self, WeaponUser: engine.Actor, Slot: int, Reason: str): ...
    def GiveAmmo(self, Weapon: Weapon, Amount: int, bLoaded: bool, bAsPercent: bool): ...
    def GetWeapon(self, Context: unreal.UObject, ReturnValue: Weapon) -> Weapon: ...
    def GetMaxZoomFOVScale(self, Weapon: Weapon, UseMode: int, ReturnValue: float) -> float: ...
    def GetLoadedAmmo(self, Weapon: Weapon, UseMode: int, ReturnValue: int) -> int: ...
    def GetFireRateAccelPercent(self, Weapon: Weapon, UseMode: int, ReturnValue: float) -> float: ...
    def GetFireRate(self, Weapon: Weapon, UseMode: int, ReturnValue: float) -> float: ...
    def GetDamageType(self, Weapon: Weapon, UseMode: int, ReturnValue: gbx_game_system_core.GbxDamageType) -> gbx_game_system_core.GbxDamageType: ...
    def CreateProjectileEQSProxy(self, Location: core_uobject.Vector, Rotation: core_uobject.Rotator, ReferenceActor: engine.Actor, ReturnValue: ProjectileEQSProxy) -> ProjectileEQSProxy: ...


class WeaponTriggerFeedbackAsset(gbx_runtime.GbxDataAsset):
    Mode: EWeaponTriggerFeedbackMode
    Feedback: WeaponTriggerFeedbackData
    Weapon: WeaponTriggerWeaponData
    Vibration: WeaponTriggerVibrationData
    FireThreshold: WeaponTriggerFireThreasholdData



class WeaponTypeAsset(gbx_runtime.GbxDataAsset):
    DisplayName: str
    ScaleformDisplayFrameID: str
    EquipAudioEventName: str



class WeaponTypeData(gbx_runtime.GbxDataAsset):
    BaseWeaponBalanceTableRow: engine.DataTableRowHandle
    ManufacturerDamageScaleRow: engine.DataTableRowHandle



class WeaponTypeDataTableAttributeValueResolver(gbx_game_system_core.DataTableFunctionAttributeValueResolver):
    DataTableFromWeaponType: EWeaponTypeDataTableType



class WeaponVisibleAmmoComponent(engine.ActorComponent):
    AmmoBoneNames: unreal.WrappedArray[str]
    MeshType: int
    InitialState: EWeaponVisibleAmmoState
    UpdateMethod: EWeaponVisibleAmmoUpdateMethod
    HideAmmoEffect: WeaponVisibleAmmoEffectData
    ShowAmmoEffect: WeaponVisibleAmmoEffectData
    VisibleAmmoState: EWeaponVisibleAmmoState
    ServerAmmoCount: int
    CachedAmmoComponent: WeaponAmmoComponent
    WeaponPrivate: Weapon
    def UpdateBoneVisibility(self, bForce: bool): ...
    def SetVisibleAmmoUpdateMethod(self, NewUpdateMethod: EWeaponVisibleAmmoUpdateMethod): ...
    def SetVisibleAmmoState(self, NewState: EWeaponVisibleAmmoState): ...
    def ResetVisibleAmmoState(self): ...
    def OnRep_ServerAmmoCount(self): ...
    def OnDetached(self): ...
    def OnAttached(self): ...
    def OnAmmoChanged(self): ...


class WeaponMaxZoomFOVScaleValueResolver(gbx_game_system_core.AttributeValueResolver):
    bInvertValue: bool
    bApplyWeaponModeZoom: bool



class GbxTrajectometerTraceData:
    Channel: int
    Shape: EGbxTrajectoryTraceShape
    ExtentX: float
    ExtentY: float
    ExtentZ: float



class WeaponShotModifierData:
    ModifierType: EWeaponShotModifierType
    Damage: float
    DamageType: unreal.UClass
    ImpactData: gbx_game_system_core.ImpactData
    ProjectilesPerShot: int
    CriticalHitOverrides: gbx_game_system_core.CriticalHitDamageOverrides
    ModifierValue: float
    GoreModifiers: gbx_game_system_core.DamageGoreModifiers



class LightBeamInitializationData:
    DataBlueprint: unreal.UClass
    Source: LightBeamAttachment
    Target: LightBeamAttachment
    Flags: int
    Instigator: engine.Pawn
    DamageCauser: engine.Actor
    Damage: float
    DamageIntervalOverride: float
    DamageRampCurve: engine.CurveFloat
    DamageRampScale: float
    DamageType: unreal.UClass
    DamageSource: unreal.UClass
    DamageRadius: float
    ImpactForce: gbx_game_system_core.ForceSelection
    ImpactDataOverride: gbx_game_system_core.ImpactData
    NameId: str
    Spread: float
    LifetimeOverride: float
    ModifierType: EWeaponShotModifierType
    ModifierValue: float
    CriticalHitOverrides: gbx_game_system_core.CriticalHitDamageOverrides
    GoreModifiers: gbx_game_system_core.DamageGoreModifiers
    ParentBeam: LightBeam



class LightBeamAttachment:
    Actor: engine.Actor
    Component: engine.SceneComponent
    Socket: str



class LightProjectileInitializationData:
    DataBlueprint: unreal.UClass
    StartLocation: core_uobject.Vector
    EndLocation: core_uobject.Vector
    Flags: int
    StartRotationOverride: core_uobject.Rotator
    Instigator: engine.Pawn
    Source: engine.Actor
    Target: engine.Actor
    TargetOffset: core_uobject.Vector
    Damage: float
    DamageCauser: engine.Actor
    DamageType: unreal.UClass
    DamageSource: unreal.UClass
    DamageRadius: float
    ImpactForce: gbx_game_system_core.ForceSelection
    ImpactDataOverride: gbx_game_system_core.ImpactData
    SpeedScale: float
    GravityScaleOverride: float
    FiringPatternID: int
    FireSocketID: int
    DamageModifierComp: gbx_game_system_core.DamageModifierComponent
    NameId: str
    ModifierType: EWeaponShotModifierType
    ModifierValue: float
    CriticalHitOverrides: gbx_game_system_core.CriticalHitDamageOverrides
    GoreModifiers: gbx_game_system_core.DamageGoreModifiers
    RingData: LightProjectileRingData



class LightProjectileRingData: ...


class FiringPatternSample:
    StartRotation: core_uobject.Rotator
    EndRotation: core_uobject.Rotator
    bUseEndRotation: bool
    bUseID: bool
    ID: int



class LightBeamTickFunction(engine.TickFunction): ...


class LightBeamImpactFXTrackingData:
    Component: engine.SceneComponent
    PhysicalMaterial: engine.PhysicalMaterial



class ClientLightBeamState:
    CreationID: int
    DataBlueprint: unreal.UClass
    Source: LightBeamAttachment
    Target: LightBeamAttachment
    Instigator: engine.Pawn
    DamageCauser: engine.Actor
    ImpactDataOverride: gbx_game_system_core.ImpactData
    Spread: float
    BeamFXOverride: engine.ParticleSystem
    ViewerBeamFXOverride: engine.ParticleSystem
    BeamImpactAudioOverride: wwise_audio.WwiseEvent
    LifetimeOverride: float
    Damage: float
    DamageType: unreal.UClass
    DamageSource: unreal.UClass
    DamageRadius: float
    DamageRampCurve: engine.CurveFloat
    DamageRampScale: float
    ImpactForce: float



class LightBeamQueryData:
    Actor: engine.Actor
    ActorType: ELightBeamQueryActorType
    OtherActor: engine.Actor
    BeamClass: unreal.UClass
    NameId: str



class LightBeamParticlePoolData:
    PSC: engine.ParticleSystemComponent



class PostLightBeamTickFunction(engine.TickFunction): ...


class LightProjectileTickFunction(engine.TickFunction): ...


class LightProjectileExplodeData:
    bHitActor: bool
    Location: engine.Vector_NetQuantize



class LightProjectileImpactData:
    bPlayEffect: bool
    Location: engine.Vector_NetQuantize



class LightProjectileAttachment:
    Actor: engine.Actor
    Component: engine.SceneComponent
    Socket: str
    RelativeRotation: core_uobject.Rotator
    RelativeImpactNormal: engine.Vector_NetQuantizeNormal



class ReplicatedLightProjectileInitializationData:
    CreationID: int
    DataBlueprint: unreal.UClass
    StartRotationOverride: core_uobject.Rotator
    Instigator: engine.Pawn
    Source: engine.Actor
    Target: engine.Actor
    DamageCauser: engine.Actor
    ImpactDataOverride: gbx_game_system_core.ImpactData
    SpeedScale: float
    GravityScaleOverride: float
    ModifierType: EWeaponShotModifierType
    FiringPatternID: int
    FireSocketID: int
    RandomSeed: int
    Damage: float
    DamageType: unreal.UClass
    DamageSource: unreal.UClass
    DamageRadius: float
    ImpactForce: float
    ModifierValue: float
    TracerFXOverride: engine.ParticleSystem
    BulletByAdditiveLayer: wwise_audio.WwiseEvent



class LightProjectileQueryData:
    Actor: engine.Actor
    ActorType: ELightProjectileQueryActorType
    ProjectileClass: unreal.UClass
    NameId: str



class LightProjectileAudioProperties:
    BulletByEntrance: wwise_audio.WwiseEvent
    BulletByBody: wwise_audio.WwiseEvent
    BulletByExit: wwise_audio.WwiseEvent
    BulletByMaxDistance: float
    BulletByChance: float
    TravellingAudioFxCollection: unreal.UClass
    TravellingAudio: wwise_audio.WwiseEvent
    TravellingAudioComponentSize: float
    ListenerApproachSpeedRtpc: wwise_audio.WwiseRtpc



class LightProjectileRingSettings:
    InitialRadius: float
    Angle: float
    InitialProjectileCount: int
    bMakeSolidRing: bool
    bUseBodyMeshBoundsForCollision: bool
    Subdivide: LightProjectileRingSubdivisionSettings
    bSubdivide: bool
    RingAxis: core_uobject.Vector
    bUseRingAxis: bool



class LightProjectileRingSubdivisionSettings:
    MaxSubdivisions: int
    ValueMode: ELightProjectileSubdivisionMode
    Value: float



class LightProjectileTimedEvent:
    Time: float
    CustomEvent: str



class LightProjectileParticlePoolData:
    PSC: engine.ParticleSystemComponent



class LightProjectileBatchTickFunction(engine.TickFunction): ...


class PostLightProjectileTickFunction(engine.TickFunction): ...


class ThrowProjectileAsyncRequest:
    Class: unreal.UClass
    Source: engine.Actor
    SourceSocket: str
    Target: engine.Actor
    TargetSocket: str
    TargetOffset: core_uobject.Vector
    MaxPrediction: float
    Speed: float
    AnglePercent: float
    DirectionOffset: core_uobject.Rotator
    InstanceCount: int
    InstanceDelay: float
    ExposeOnSpawnCache: engine.GbxExposeOnSpawnValueCache



class PredictProjectilePathAsyncRequest(engine.PredictProjectilePathParams):
    TraceMode: engine.EGbxTraceAsyncMode
    ObjectType: int
    TraceName: str



class WeaponAttachState:
    Slot: int
    Instigator: engine.Pawn
    EquipType: EWeaponEquipType
    PutDownType: EWeaponPutDownType



class WeaponUseModeState:
    InputChannels: int
    PrimaryInputChannel: int
    bReloadNeeded: bool
    UseComponent: WeaponUseComponent
    AmmoComponent: WeaponAmmoComponent
    ReloadComponent: WeaponReloadComponent
    ZoomComponent: WeaponZoomComponent
    AudioProviderComponent: WeaponAudioProviderComponent
    DamageModifierComponent: gbx_game_system_core.DamageModifierComponent
    Components: unreal.WrappedArray[engine.ActorComponent]



class BodyWeaponActionInfo:
    WeaponAction: int
    Condition: gbx_runtime.GbxCondition
    ConditionalWeaponActions: unreal.WrappedArray[ConditionalWeaponActionSet]
    ConditionalActions: unreal.WrappedArray[ConditionalActionInfo]



class ConditionalActionInfo:
    Condition: gbx_runtime.GbxCondition
    Action: unreal.UClass
    ActionNetMode: gbx_game_system_core.EGbxActionNetMode



class ConditionalWeaponActionSet:
    Condition: gbx_runtime.GbxCondition
    ConditionalActions: unreal.WrappedArray[ConditionalActionInfo]



class WeaponTrinketAttachment:
    MeshComponent: gbx_game_system_core.GbxSkeletalMeshComponent
    SkeletalMesh: engine.SkeletalMesh
    AnimInstanceClass: unreal.UClass



class WeaponSkeletalControlInstance:
    Data: WeaponSkeletalControlBase



class WeaponMaterialEffectInstance:
    ValueOverTime: engine.CurveFloat



class WeaponEffectAttachment:
    Effect: engine.ParticleSystem
    ConditionalEffect: unreal.UClass
    PSC: engine.ParticleSystemComponent



class WeaponChargeEventNotify:
    Threshold: float
    Comparision: EWeaponChargeComparisonOperatorType
    EVENTTYPE: EWeaponChargeEventType
    EventName: str



class WeaponChargeAttributeEffect:
    StatesBitmask: int
    bApplyToInstigator: bool
    AttributeEffect: gbx_game_system_core.AttributeEffectData
    AttributeModifier: gbx_game_system_core.GbxAttributeModifierHandle



class WeaponRegisterSkeletalControlData:
    Type: int
    Visibility: int
    bPlayerOnly: bool
    Control: WeaponSkeletalControlBase



class WeaponRegisterTrinketAttachmentData:
    SkeletalMesh: engine.SkeletalMesh
    AnimInstanceClass: unreal.UClass
    AttachSocket: str
    RelativeLocation: core_uobject.Vector
    RelativeRotation: core_uobject.Rotator
    Visibility: int



class WeaponEffectQueryData:
    Type: int
    ID: int
    Visibility: int
    UseModeBitmask: int



class WeaponMaterialEffectData:
    MaterialParamName: str
    Visibility: int
    BlendMode: EWeaponMaterialEffectBlendMode
    bPlayOnlyOnActiveSlot: bool
    bLoop: bool
    bApplyAttribute: bool
    bScaleAttributeByValueOverTime: bool
    bScaleAttributeByDeltaTime: bool
    AttributeValue: gbx_game_system_core.AttributeInitializationData
    ValueOverTime: engine.CurveFloat
    Impulse: float
    Duration: float
    DecayRate: float
    MaxValue: float



class WeaponRegisterMaterialEffectData:
    Type: int
    MaterialParamName: str
    ID: int
    Visibility: int
    UseModeBitmask: int
    Slot: int
    BlendMode: EWeaponMaterialEffectBlendMode
    bPlayOnlyOnActiveSlot: bool
    bLoop: bool
    bApplyAttribute: bool
    bScaleAttributeByValueOverTime: bool
    bScaleAttributeByDeltaTime: bool
    AttributeValue: gbx_game_system_core.AttributeInitializationData
    ValueOverTime: engine.CurveFloat
    Impulse: float
    Duration: gbx_game_system_core.AttributeInitializationData
    DecayRate: float
    MaxValue: float



class WeaponRegisterAttachmentEffectData:
    Type: int
    Effect: engine.ParticleSystem
    ConditionalEffect: unreal.UClass
    Socket: str
    ScopedSocket: str
    ID: int
    Visibility: int
    UseModeBitmask: int
    Slot: int
    Flags: int
    RelativeLocation: core_uobject.Vector
    RelativeRotation: core_uobject.Rotator
    RelativeScale: float
    AutoActivateModeBitmask: int
    bPlayOnlyOnActiveSlot: bool
    bAutoActivate: bool
    bIgnoredByFXCoordinator: bool
    bHideWhenScoped: bool



class WeaponHeatEventNotify:
    Threshold: float
    Comparision: EWeaponHeatComparisonOperatorType
    EventName: str



class WeaponShotModifierTypeName:
    Type: EWeaponShotModifierType
    Name: str
    Tooltip: str



class LightBeamFlagName:
    Type: ELightBeamFlag
    Name: str
    Tooltip: str



class LightProjectileFlagName:
    Type: ELightProjectileFlag
    Name: str
    Tooltip: str



class WeaponActionTypeName:
    Type: int
    Name: str
    Tooltip: str



class WeaponEffectTypeName:
    Type: int
    Name: str
    Tooltip: str



class WeaponSkeletalControlState: ...


class WeaponTriggerFireThreasholdData:
    Position: float



class WeaponTriggerVibrationData:
    Position: float
    Frequency: float
    Amplitude: float



class WeaponTriggerWeaponData:
    StartPosition: float
    EndPosition: float
    Force: float



class WeaponTriggerFeedbackData:
    Position: float
    Force: float



class WeaponVisibleAmmoEffectData:
    Effect: engine.ParticleSystem
    RelativeTransform: core_uobject.Transform



class WeaponZoomLevel:
    Duration: float
    FOVScale: float
    FOVLerpPct: float
    ViewModelFOVScale: float



class WeaponZoomState:
    State: EWeaponZoomState
    Level: int



class EGbxTrajectoryTraceShape(enum.Enum):
    Sphere = 0
    Capsule = 1
    EGbxTrajectoryTraceShape_MAX = 2


class EWeaponEquipType(enum.Enum):
    Custom = 0
    Instant = 1


class EWeaponPutDownType(enum.Enum):
    Instant = 0
    EWeaponPutDownType_MAX = 1


class EWeaponShotModifierType(enum.Enum):
    EngineType2 = 0
    EngineType1 = 1
    EngineType4 = 2
    EngineType8 = 3
    GameType8 = 4


class ELightBeamQueryActorType(enum.Enum):
    Instigator = 0
    DamageCauser = 1
    Target = 2


class ELightBeamLock(enum.Enum):
    Always = 0
    LockOn = 1


class ELightBeamFlag(enum.Enum):
    Locked = 0
    LagCompensation = 1
    FollowViewPoint = 2
    EngineFlag6 = 3


class ELightProjectileQueryActorType(enum.Enum):
    Instigator = 0
    DamageCauser = 1
    Target = 2


class ELightProjectileSubdivisionMode(enum.Enum):
    ELightProjectileSubdivisionMode_MAX = 0
    Seconds = 1
    Width = 2


class ELightProjectileTracerThrottleLevel(enum.Enum):
    NPC = 0
    RemotePlayer = 1
    ELightProjectileTracerThrottleLevel_MAX = 2


class ELightProjectileFlag(enum.Enum):
    Homing = 0
    StartFromLocalSource = 1
    Magnetism = 2
    LagCompensation = 3
    ELightProjectileFlag_MAX = 4


class ELightProjectileSplitPattern(enum.Enum):
    Fan = 0
    ELightProjectileSplitPattern_MAX = 1


class EHitTypeEnum(enum.Enum):
    Enemy = 0
    Neutral = 1


class ERecoilEndOfPatternAction(enum.Enum):
    ERecoilEndOfPatternAction_MAX = 0
    Loop = 1
    PingPong = 2


class EWeaponReloadEvent(enum.Enum):
    Ended = 0
    EWeaponReloadEvent_MAX = 1


class EWeaponUseEvent(enum.Enum):
    Used = 0
    UseFinished = 1


class EWeaponActionType(enum.Enum):
    EWAT_PutDown = 0
    EWAT_Reload = 1
    EWAT_Use = 2
    EWAT_Overcharged = 3
    EWAT_GameWeaponActionType3 = 4


class EAmmoRegenType(enum.Enum):
    GenerateAmmo = 0
    RefillLoadedAmmo = 1


class EWeaponChargeEventType(enum.Enum):
    EnableParticleEmitter = 0
    DisableParticleEmitter = 1


class EWeaponChargeComparisonOperatorType(enum.Enum):
    GreaterThan = 0
    LessThanOrEqual = 1
    EWeaponChargeComparisonOperatorType_MAX = 2


class EWeaponChargeState(enum.Enum):
    Discharging = 0
    Charging = 1
    Overcharged = 2


class EWeaponSkeletalControlEvent(enum.Enum):
    RestoreState = 0
    Resume = 1
    Reset = 2
    AddInput = 3


class EWeaponMaterialEffectBlendMode(enum.Enum):
    Add = 0
    EWAVT_MAX = 1
    Replace = 2


class EWeaponEffectFlag(enum.Enum):
    PlayOnlyOnActiveSlot = 0
    IgnoredByFXCoordinator = 1
    SpawnOnlyWhenVisible = 2


class EWeaponTextureMipsSetting(enum.Enum):
    High = 0
    VeryHigh = 1


class EWeaponAttachmentVisibilityType(enum.Enum):
    EWAVT_FirstPerson = 0
    EWAVT_ThirdPerson = 1


class EWeaponEffectType(enum.Enum):
    EWET_Use = 0
    EWET_Charge = 1
    EWET_Charged = 2
    EWET_EngineWeaponEffectType5 = 3
    EWET_GameWeaponEffectType5 = 4


class EWeaponFireRateState(enum.Enum):
    Accelerating = 0
    Decelerating = 1


class EWeaponHeatComparisonOperatorType(enum.Enum):
    EWeaponHeatComparisonOperatorType_MAX = 0
    GreaterThan = 1
    LessThanOrEqual = 2


class EWeaponShotDamageModifierType(enum.Enum):
    Add = 0
    SimpleScale = 1


class ESimpleMotionInputHandler(enum.Enum):
    Set = 0
    ESimpleMotionInputHandler_MAX = 1


class EWeaponTriggerFeedbackMode(enum.Enum):
    Feedback = 0
    EWeaponTriggerFeedbackMode_MAX = 1
    Weapon = 2


class EWeaponTypeDataTableType(enum.Enum):
    ManufacturerDamageScale = 0
    EWeaponTypeDataTableType_MAX = 1


class EWeaponVisibleAmmoUpdateMethod(enum.Enum):
    Manual = 0
    AutoAdd = 1
    EWeaponVisibleAmmoUpdateMethod_MAX = 2


class EWeaponVisibleAmmoState(enum.Enum):
    PendingLoadedAmmo = 0
    Disabled = 1


class EWeaponZoomState(enum.Enum):
    EWeaponZoomState_MAX = 0
    ZoomingIn = 1
    Zoomed = 2

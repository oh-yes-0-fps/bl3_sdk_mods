from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine
from . import gbx_runtime
from . import wwise_audio
from . import gbx_game_system_core
from . import phys_xvehicles
from . import gbx_inventory
from . import anim_graph_runtime



class TurretMovementComponent(engine.PawnMovementComponent):
    TurretRelativeRotation: core_uobject.Rotator
    MovementThresholdTolerance: float
    DurationBeforeStop: float
    MovementStartEvent: wwise_audio.WwiseEvent
    MovementStopEvent: wwise_audio.WwiseEvent
    MovementSpeedRTPC: wwise_audio.WwiseRtpc
    MovementAudioPlaybackInst: wwise_audio.WwisePlaybackInstance
    TimeSinceStop: float
    bReturnToZeroRotation: bool
    bUsePlayersView: bool
    bAimTowardsPlayersViewLocation: bool
    RotationInputs: core_uobject.Vector2D
    RotationMaxSpeed: core_uobject.Vector2D
    RotationDamping: core_uobject.Vector2D
    bEnableReturnToZeroRotationRate: bool
    ReturnToZeroRotationRate: core_uobject.Vector2D
    bControlYawMovement: bool
    bControlPitchMovement: bool
    bEnableMovementCollision: bool
    PivotSocket: str
    bUpdatedComponentRequired: bool
    bUsePitchConstraints: bool
    PitchMinConstraint: float
    PitchMaxConstraint: float
    bUseYawConstraints: bool
    YawMinConstraint: float
    YawMaxConstraint: float
    RemoteTurretRelativeRotation: core_uobject.Rotator
    TurretControlOwner: engine.Pawn
    def UpdateTurretControlDependency(self): ...
    def UpdateParentInitialOffset(self): ...
    def SetRotationInputs(self, XValue: float, YValue: float): ...
    def ServerSetRotationInputs(self, InRotationInputs: core_uobject.Vector2D): ...


class Vehicle(engine.Pawn):
    Mesh: engine.SkeletalMeshComponent
    bUnpushable: bool
    CachedTargetableComponent: gbx_game_system_core.TargetableComponent
    CachedDamageComponent: gbx_game_system_core.DamageComponent
    CachedDamageCauserComponent: gbx_game_system_core.DamageCauserComponent
    CachedTargetingComponent: gbx_game_system_core.TargetingComponent
    VehiclePartSelectionData: VehiclePartSelectionData
    VehicleParts: unreal.WrappedArray[VehiclePartData]
    CharacterCollidingResistance: float
    def SetTeam(self, Team: gbx_game_system_core.Team): ...
    def RemoveVehiclePart(self, CharacterPart: VehiclePartData): ...
    def OnRep_VehicleParts(self): ...
    def IsPowerSliding(self, ReturnValue: bool) -> bool: ...
    def IsInAir(self, ReturnValue: bool) -> bool: ...
    def GetTeamComponent(self, ReturnValue: gbx_game_system_core.TeamComponent) -> gbx_game_system_core.TeamComponent: ...
    def GetTeam(self, ReturnValue: gbx_game_system_core.Team) -> gbx_game_system_core.Team: ...
    def GetTargetingComponent(self, ReturnValue: gbx_game_system_core.TargetingComponent) -> gbx_game_system_core.TargetingComponent: ...
    def GetTargetableComponent(self, ReturnValue: gbx_game_system_core.TargetableComponent) -> gbx_game_system_core.TargetableComponent: ...
    def GetNumWheelsInAir(self, ReturnValue: int) -> int: ...
    def GetEquipedParts(self, ReturnValue: unreal.WrappedArray[VehiclePartData]) -> unreal.WrappedArray[VehiclePartData]: ...
    def AddVehiclePart(self, CharacterPart: VehiclePartData): ...


class VehicleInventoryBalanceStateComponent(gbx_inventory.InventoryBalanceStateComponent): ...


class VehicleBoostData(gbx_runtime.GbxDataAsset):
    bApplyFullThrottleWhenBoosting: bool
    MinBoostDuration: float
    GroundBoostParams: BoostPhysicsParams
    AirBoostParams: BoostPhysicsParams
    BoostPoolData: gbx_game_system_core.GameResourcePoolData
    bContinuousStartCheck: bool
    StartBoostCondition: gbx_runtime.GbxCondition
    StopBoostCondition: gbx_runtime.GbxCondition
    bStopConditionCanOverrideMinBoostDuration: bool
    bPauseWhenInAir: bool
    MinStartBoostSpeed: float
    MinStartBoostAngle: float
    BoostCooldownTime: float
    bInstantBoost: bool
    InstantBoostCharges: int
    InstantBoostDuration: float
    bModifySteering: bool
    SteeringRatioCurve: engine.RuntimeFloatCurve
    SteeringRatioInterpSpeed: float



class VehicleBoostComponent(engine.ActorComponent):
    BoostData: VehicleBoostData
    Vehicle: Vehicle
    bIsBoosting: bool
    BoostPool: gbx_game_system_core.GameResourcePoolReference
    def VehicleBoostEvent__DelegateSignature(self): ...
    def StopBoost(self, bForce: bool): ...
    def StartBoost(self): ...
    def ResumeBoost(self): ...
    def PauseBoost(self): ...
    def OnRep_IsBoosting(self, bWasBoosting: bool): ...
    def K2_BoostStopped(self): ...
    def K2_BoostStarted(self): ...
    def GetRelativeBoostSpeed(self, ReturnValue: float) -> float: ...
    def GetMaxBoostPoolValue(self, ReturnValue: float) -> float: ...
    def GetCurrentBoostPoolValue(self, ReturnValue: float) -> float: ...
    def GetCurrentBoostChargesCount(self, ReturnValue: int) -> int: ...
    def GetBoostEnabled(self, ReturnValue: bool) -> bool: ...
    def GetBoostDirection(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...


class VehiclePartData(gbx_inventory.InventoryPartData):
    VehicleArchetype: str
    bIsAShield: bool



class VehicleAirControlComponent(engine.ActorComponent):
    YawControlForce: float
    PitchControlForce: float
    ForceRatio: engine.RuntimeFloatCurve
    Vehicle: Vehicle



class VehicleContactPtModifierInterface(core_uobject.Interface): ...


class VehicleDigiThrustComponent(engine.ActorComponent):
    TeleportMaxDist: float
    TeleportDuration: float
    bUseTeleportDirection: bool
    bReorientOnTeleport: bool
    ReorientationRatio: float
    TeleportCondition: gbx_runtime.GbxCondition
    BoostPoolData: gbx_game_system_core.GameResourcePoolData
    NumChargesOnFullResource: int
    TraceStepLength: float
    GroundDetectionTraceLength: float
    GroundTraceRadius: float
    PathPtGroundHeight: float
    ValidFloorAngle: float
    FloorMaxAngleDiffBetweenGroundTraces: float
    FloorMaxHeightDiffBetweenGroundTraces: float
    RefUpBlendWeight: float
    bKeepLastValidGroundUpWhenInAir: bool
    Vehicle: Vehicle
    BoostPool: gbx_game_system_core.GameResourcePoolReference
    bTeleportRequested: bool
    DigithrustInAction: unreal.UClass
    DigithrustOutAction: unreal.UClass
    DigithrustOutActionDuration: float
    def SetTeleportDirection(self, WantedDirection: core_uobject.Vector): ...
    def RequestTeleport(self): ...
    def NetMulticast_OnDigiThrustStarted(self): ...
    def NetMulticast_OnDigiThrustEndFinished(self): ...
    def NetMulticast_OnDigiThrustEnd(self): ...
    def NetMulticast_OnDigiThrustCollision(self): ...
    def IsTeleporting(self, ReturnValue: bool) -> bool: ...
    def GetMaxBoostPoolValue(self, ReturnValue: float) -> float: ...
    def GetCurrentBoostPoolValue(self, ReturnValue: float) -> float: ...
    def DigiThrustEvent__DelegateSignature(self): ...


class VehicleFlightComponent(engine.FloatingPawnMovement): ...


class VehicleHitchAttachPtComponent(engine.SphereComponent):
    UpdatedPrimitive: engine.PrimitiveComponent
    AttachTransitionLength: float
    AttachTransitionTolerance: float
    BrakeTorque: float
    CachedAttachedVehicleMovementComp: WheeledVehicleMovementComponentNW
    CachedMovementComponent: WheeledVehicleMovementComponentNW
    def IsAttached(self, ReturnValue: bool) -> bool: ...
    def HitchAttachAction__DelegateSignature(self, FromVehicle: Vehicle): ...


class VehicleHitchComponent(engine.PhysicsConstraintComponent):
    bCheckAutoAttach: bool
    HitchAttachCheckRadius: float
    YawLimit: float
    PitchLimit: float
    HitchConstraintStiffness: float
    HitchConstraintDamping: float
    AttachedPoint: VehicleHitchAttachPtComponent
    OwningVehicle: Vehicle
    OwningVehicleMovementComp: phys_xvehicles.WheeledVehicleMovementComponent
    def TeleportTrailerAndAttachToHitch(self, TrailerToAttach: engine.Actor): ...
    def HitchAttachAction__DelegateSignature(self, FromVehicle: Vehicle): ...
    def DetachFromHitch(self): ...
    def AttachToHitch(self, AttachPtToAttach: VehicleHitchAttachPtComponent): ...


class VehicleHoverComponent(engine.ActorComponent):
    RawStrafeInput: float
    RawForwardInput: float
    ReplicatedState: ReplicatedHoverComponentState
    ForceRefVel: float
    ForceCurve: engine.RuntimeFloatCurve
    DampingForce: float
    BrakingDampingForce: float
    TireConfigWhenStrafing: phys_xvehicles.TireConfig
    CustomGravityModifier: float
    bFaceControlRotation: bool
    TimeToFaceControlRotation: float
    Vehicle: Vehicle
    MovementComponentNW: WheeledVehicleMovementComponentNW
    def VehicleHoverEvent__DelegateSignature(self): ...
    def ServerUpdateState(self, InbIsEnabled: bool, InStrafeInput: float, InForwardInput: float, InTargetRotation: core_uobject.Rotator): ...
    def IsHoverEnabled(self, ReturnValue: bool) -> bool: ...
    def EnableHover(self, bEnable: bool): ...


class VehicleMovementInterface(core_uobject.Interface):

    def GetDirectionBasedThrottleAndSteer(self, StickInput: core_uobject.Vector2D, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...


class VehiclePartActor(engine.Actor):
    bWeldSimulatedBodies: bool
    bWeldedBodiesShouldModifyPhysicalProperties: bool
    bForwardDamageToParent: bool
    OwningVehicle: Vehicle
    ParentSocket: str
    def WeldActorToVehicle(self, SpawnedPart: engine.Actor): ...
    def ReceiveParentVehicleBeginPlay(self): ...
    def OnRep_ParentSocket(self): ...
    def OnRep_OwningVehicle(self): ...


class VehiclePartSelectionData(gbx_game_system_core.ActorPartSelectionData): ...


class VehiclePowerSlideComponent(engine.ActorComponent):
    bApplyHandbrake: bool
    InAirBehavior: EInAirBehavior
    MaxNumWheelsInAir: int
    bIsPowerSliding: bool
    AngleToConsiderDrift: float
    MinDriftVelThreshold: float
    TimeInDriftDecayRate: float
    MinDriftDurationForBoost: float
    MaxDriftDurationForBoost: float
    BoostCurve: engine.RuntimeFloatCurve
    MaxBoostForce: float
    PostDriftBoostDurationMin: float
    PostDriftBoostDurationMax: float
    MinVelForPostDriftBoost: float
    BoostDirection: gbx_game_system_core.RelativeDirectionData
    def SetPowerSlideEnabled(self, bEnable: bool): ...
    def ResumePowerSlide(self, Reason: str): ...
    def PausePowerSlide(self, Reason: str): ...
    def OnRep_IsPowerSliding(self, bWasPowerSliding: bool): ...
    def IsPowerSlidePaused(self, ReturnValue: bool) -> bool: ...
    def IsInPowerSlideBoost(self, ReturnValue: bool) -> bool: ...
    def GetPowerSlideEnabled(self, ReturnValue: bool) -> bool: ...
    def GetCurrentBoostRatio(self, ReturnValue: float) -> float: ...
    def CancelPowerSlide(self): ...


class GbxVehicleWheel(phys_xvehicles.VehicleWheel):
    SuspensionForceXOffset: float
    SuspensionForceYOffset: float
    SuspensionTravelDirection: core_uobject.Vector
    MaxAllowedLongitudinalSlipPerRotation: float



class VehicleCollisionResponseModificationContext(unreal.UObject):
    Collider: Vehicle
    Collidee: Vehicle



class WheeledVehicleMovementComponentNW(phys_xvehicles.WheeledVehicleMovementComponent4W):
    DrivenWheels: unreal.WrappedArray[int]
    VehicleDriveType: EVehicleDriveType
    ForwardMarginOfError: float
    ContiguousMovementDirectionThreshold: float
    ContiguousMovementDirectionSpeedThreshold: float
    bContiguousMovementAppliesToReverse: bool
    bOversteerFixupEnabled: bool
    OversteerFixupCurve: engine.RuntimeFloatCurve
    bAerialRotationalDampingEnabled: bool
    RisingAerialRotationDampingFactor: float
    AerialRotationalDamping: float
    AerialRotationalDeviationAngle: float
    bAerialAutoStabilizationEnabled: bool
    RisingAerialAutoStabilizationFactor: float
    AerialAutoStabilization: float
    bUseAutoUnflip: bool
    AutoUnflipAngleRange: core_uobject.Vector2D
    AutoUnflipEaseInZone: float
    AutoUnflipCurve: engine.RuntimeFloatCurve
    AutoUnflipForce: float
    TankTreadInputDifferenceCurve: engine.RuntimeFloatCurve
    MaxTreadThrustOvershootValue: float
    BrakeWhenTurningRatioCurve: engine.RuntimeFloatCurve
    OppositeThreadSpeedWhenTurningInPlace: float
    CustomGravityModifier: float
    GroundedCustomGravityModifier: float
    bEnableSteeringCurve: bool
    bLateralToLongitudinalVelocityShiftEnabled: bool
    LateralToLongitudinalVelocityShiftCurve: engine.RuntimeFloatCurve
    TireForcesRatioToSlopeAngleCurve: engine.RuntimeFloatCurve
    BalanceAssistMaxSpeed: float
    bUseSagittalBalanceCurve: bool
    SagittalBalanceCurve: engine.RuntimeFloatCurve
    SagittalBalanceSpeedCurve: engine.RuntimeFloatCurve
    SagitalBlendSpeed: float
    EBrakingSagitalBlendSpeed: float
    EBrakingSagittalAngleRefSpeedKmH: float
    EBrakingSagitalLeanAngle: float
    bUseCoronalBalanceCurve: bool
    CoronalBalanceCurve: engine.RuntimeFloatCurve
    bUseBrakeAssist: bool
    bUseHandBrakeAssist: bool
    bApplyBrakeAssistOnLatForces: bool
    BrakeAssistForceScale: float
    BrakeAssistCurve: engine.RuntimeFloatCurve
    bCanHandbrake: bool
    bUseUTurnAssist: bool
    bActivateUTurnAssistOnHandbrake: bool
    ActivateUTurnAssistCondition: gbx_runtime.GbxCondition
    bApplyUTurnAssistInAir: bool
    UTurnAssistForce: float
    UTurnAssistForceInterpSpeed: float
    UTurnAssistForceReturnToZeroInterpSpeed: float
    UTurnAssistRefSpeed: float
    UTurnAssistMaxAngularVelInfluence: float
    UTurnAssistCurve: engine.RuntimeFloatCurve
    LiquidBodyWheelDepthToForceCurve: engine.RuntimeFloatCurve
    LiquidBodyDampingCoefficient: float
    CollisionResponseFormula: gbx_game_system_core.AttributeInitializationData
    AngleToUpsideDown: float
    DefaultPhysicalMaterial: engine.PhysicalMaterial
    UpsideDownPhysicalMaterial: engine.PhysicalMaterial
    bDontMoveWhenCollided: bool
    CryoPenaltyCurve: engine.CurveFloat
    AntiRollBars: unreal.WrappedArray[AntiRollBarData]
    CollisionResponseContext: VehicleCollisionResponseModificationContext
    def SetToRestState(self): ...
    def SetSteerAngle(self, SteerAngle: float, WheelIndex: int): ...
    def SetSagittalBalancingEnabled(self, bEnable: bool): ...
    def SetOversteerFixupEnabled(self, bEnable: bool): ...
    def SetNoDriveSteerAngle(self, SteerAngle: float, WheelIndex: int): ...
    def SetNoDriveDriveTorque(self, DriveTorque: float, WheelIndex: int): ...
    def SetNoDriveBrakeTorque(self, BrakeTorque: float, WheelIndex: int): ...
    def SetLateralToLongitudinalVelocityShiftEnabled(self, bEnable: bool): ...
    def SetCustomGravityModifier(self, NewModifier: float): ...
    def SetCoronalBalancingEnabled(self, bEnable: bool): ...
    def SetAerialRotationalDampingEnabled(self, bEnable: bool): ...
    def ResetCustomGravityModifer(self): ...
    def IsInAir(self, ReturnValue: bool) -> bool: ...
    def GetSagittalBalancingEnabled(self, ReturnValue: bool) -> bool: ...
    def GetOversteerFixupEnabled(self, ReturnValue: bool) -> bool: ...
    def GetNumWheelsInAir(self, ReturnValue: int) -> int: ...
    def GetLateralToLongitudinalVelocityShiftEnabled(self, ReturnValue: bool) -> bool: ...
    def GetDirectionBasedThrottleAndSteer(self, StickInput: core_uobject.Vector2D, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def GetCustomGravityModifier(self, ReturnValue: float) -> float: ...
    def GetCoronalBalancingEnabled(self, ReturnValue: bool) -> bool: ...
    def GetCameraRelativeThrottleAndSteer(self, StickInput: core_uobject.Vector2D, WantedDirAngle: float, Mode: EVehicleCameraRelativeDrivingMode, AngleToSteeringCurve: engine.CurveFloat, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def GetAerialRotationalDampingEnabled(self, ReturnValue: bool) -> bool: ...
    def ApplyAngularVelocityInfluence(self, DeltaTime: float, MaxInfluence: float, Pitch: float, Roll: float, Yaw: float): ...


class ReplicatedHoverComponentState:
    bIsEnabled: bool
    StrafeInput: float
    ForwardInput: float
    TargetRotation: core_uobject.Rotator



class AnimNode_ComplexWheelHandler(anim_graph_runtime.AnimNode_SkeletalControlBase):
    WheelMovementSystems: unreal.WrappedArray[ComplexWheelMovement]



class ComplexWheelMovement:
    WheelReference: engine.BoneReference
    WheelSteeringPivotReference: engine.BoneReference
    ControlArmReference: engine.BoneReference
    PhysicalWheelReference: engine.BoneReference
    SuspensionDropMaxSpeed: float



class BoostRegenerateEvent:
    BoostTarget: float



class BoostPhysicsParams:
    RefVelForPowerCurveKmH: float
    RefAccelForPowerCurve: float
    BoostPower: engine.RuntimeFloatCurve
    PowerOverTimeCurveBaseRatio: float
    RefTimeForPowerOverTimeCurve: float
    BoostPowerOverTime: engine.RuntimeFloatCurve
    BoostDirection: gbx_game_system_core.RelativeDirectionData



class PushbackCharactersTickFunction(engine.TickFunction): ...


class VehiclePartList:
    Parts: unreal.WrappedArray[VehiclePartData]



class AntiRollBarData:
    WheelIndex1: int
    WheelIndex2: int
    Stiffness: float



class EInAirBehavior(enum.Enum):
    Stop = 0
    Pause = 1


class EVehicleCameraRelativeDrivingMode(enum.Enum):
    ForwardOnly = 0
    ReverseOnly = 1
    ForceReverse = 2


class EVehicleDriveType(enum.Enum):
    WheelN = 0
    WheelNNoDrive = 1
    EVehicleDriveType_MAX = 2

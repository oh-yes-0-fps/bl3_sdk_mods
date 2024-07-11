from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import anim_graph_runtime


class WheeledVehicleMovementComponent(engine.PawnMovementComponent):
    bDeprecatedSpringOffsetMode: bool
    WheelSetups: unreal.WrappedArray[WheelSetup]
    Mass: float
    DragCoefficient: float
    ChassisWidth: float
    ChassisHeight: float
    bReverseAsBrake: bool
    ReverseAsBrakeTimeBeforeReverse: float
    bBrakeWhenReleasingReverse: bool
    DragArea: float
    EstimatedMaxEngineSpeed: float
    MaxEngineRPM: float
    DebugDragMagnitude: float
    InertiaTensorScale: core_uobject.Vector
    MinNormalizedTireLoad: float
    MinNormalizedTireLoadFiltered: float
    MaxNormalizedTireLoad: float
    MaxNormalizedTireLoadFiltered: float
    ThresholdLongitudinalSpeed: float
    LowForwardSpeedSubStepCount: int
    HighForwardSpeedSubStepCount: int
    Wheels: unreal.WrappedArray[VehicleWheel]
    bUseRVOAvoidance: bool
    RVOAvoidanceRadius: float
    RVOAvoidanceHeight: float
    AvoidanceConsiderationRadius: float
    RVOSteeringStep: float
    RVOThrottleStep: float
    AvoidanceUID: int
    AvoidanceGroup: engine.NavAvoidanceMask
    GroupsToAvoid: engine.NavAvoidanceMask
    GroupsToIgnore: engine.NavAvoidanceMask
    AvoidanceWeight: float
    PendingLaunchVelocity: core_uobject.Vector
    ReplicatedState: ReplicatedVehicleState
    RawSteeringInput: float
    RawThrottleInput: float
    RawBrakeInput: float
    bRawHandbrakeInput: bool
    bRawGearUpInput: bool
    bRawGearDownInput: bool
    SteeringInput: float
    ThrottleInput: float
    BrakeInput: float
    HandbrakeInput: float
    IdleBrakeInput: float
    StopThreshold: float
    WrongDirectionThreshold: float
    ThrottleInputRate: VehicleInputRate
    BrakeInputRate: VehicleInputRate
    HandbrakeInputRate: VehicleInputRate
    SteeringInputRate: VehicleInputRate
    bWasAvoidanceUpdated: bool
    OverrideController: engine.Controller
    bAutoBrake: bool
    bDisableBrake: bool

    def SetUseAutoGears(self, bUseAuto: bool): ...
    def SetThrottleInput(self, Throttle: float): ...
    def SetTargetGear(self, GearNum: int, bImmediate: bool): ...
    def SetSteeringInput(self, Steering: float): ...
    def SetHandbrakeInput(self, bNewHandbrake: bool): ...
    def SetGroupsToIgnoreMask(self, GroupMask: engine.NavAvoidanceMask): ...
    def SetGroupsToIgnore(self, GroupFlags: int): ...
    def SetGroupsToAvoidMask(self, GroupMask: engine.NavAvoidanceMask): ...
    def SetGroupsToAvoid(self, GroupFlags: int): ...
    def SetGearUp(self, bNewGearUp: bool): ...
    def SetGearDown(self, bNewGearDown: bool): ...
    def SetBrakeInput(self, Brake: float): ...
    def SetAvoidanceGroupMask(self, GroupMask: engine.NavAvoidanceMask): ...
    def SetAvoidanceGroup(self, GroupFlags: int): ...
    def SetAvoidanceEnabled(self, bEnable: bool): ...
    def SetAutoBrake(self, bWantedAutoBrake: bool, Reason: str): ...
    def ServerUpdateState(
        self,
        InSteeringInput: float,
        InThrottleInput: float,
        InBrakeInput: float,
        InHandbrakeInput: float,
        CurrentGear: int,
    ): ...
    def IsAutoBraking(self) -> bool: ...
    def GetUseAutoGears(self) -> bool: ...
    def GetThrottleInput(self) -> float: ...
    def GetTargetGear(self) -> int: ...
    def GetSteeringInput(self) -> float: ...
    def GetPlanarSpeed(self) -> float: ...
    def GetLateralSpeed(self) -> float: ...
    def GetHandbrakeInput(self) -> float: ...
    def GetForwardSpeed(self) -> float: ...
    def GetEngineRotationSpeed(self) -> float: ...
    def GetEngineMaxRotationSpeed(self) -> float: ...
    def GetCurrentGear(self) -> int: ...
    def GetBrakeInput(self) -> float: ...


class SimpleWheeledVehicleMovementComponent(WheeledVehicleMovementComponent):

    def SetSteerAngle(self, SteerAngle: float, WheelIndex: int): ...
    def SetDriveTorque(self, DriveTorque: float, WheelIndex: int): ...
    def SetBrakeTorque(self, BrakeTorque: float, WheelIndex: int): ...


class TireConfig(engine.DataAsset):
    FrictionScale: float
    TireFrictionScales: unreal.WrappedArray[TireConfigMaterialFriction]


class VehicleAnimInstance(engine.AnimInstance):
    WheeledVehicleMovementComponent: WheeledVehicleMovementComponent

    def GetVehicle(self) -> WheeledVehicle: ...


class VehicleWheel(unreal.UObject):
    CollisionMesh: engine.StaticMesh
    WheelCollisionPhysMat: engine.PhysicalMaterial
    bDontCreateShape: bool
    bAutoAdjustCollisionSize: bool
    Offset: core_uobject.Vector
    ShapeRadius: float
    ShapeWidth: float
    Mass: float
    DampingRate: float
    SteerAngle: float
    bAffectedByHandbrake: bool
    TireType: engine.TireType
    TireConfig: TireConfig
    LatStiffMaxLoad: float
    LatStiffValue: float
    LongStiffValue: float
    SuspensionForceOffset: float
    SuspensionMaxRaise: float
    SuspensionMaxDrop: float
    SuspensionNaturalFrequency: float
    SuspensionDampingRatio: float
    SweepType: int
    MaxBrakeTorque: float
    MaxHandBrakeTorque: float
    VehicleSim: WheeledVehicleMovementComponent
    WheelIndex: int

    def IsInAir(self) -> bool: ...
    def GetSuspensionOffset(self) -> float: ...
    def GetSteerAngle(self) -> float: ...
    def GetRotationAngle(self) -> float: ...


class WheeledVehicle(engine.Pawn):
    Mesh: engine.SkeletalMeshComponent
    VehicleMovement: WheeledVehicleMovementComponent


class WheeledVehicleMovementComponent4W(WheeledVehicleMovementComponent):
    EngineSetup: VehicleEngineData
    DifferentialSetup: VehicleDifferential4WData
    TransmissionSetup: VehicleTransmissionData
    SteeringCurve: engine.RuntimeFloatCurve
    AckermannAccuracy: float


class AnimNode_WheelHandler(anim_graph_runtime.AnimNode_SkeletalControlBase): ...


class StartVehicleUpdatesTickFunction(engine.TickFunction): ...


class TireConfigMaterialFriction:
    PhysicalMaterial: engine.PhysicalMaterial
    FrictionScale: float


class VehicleAnimInstanceProxy(engine.AnimInstanceProxy): ...


class VehicleInputRate:
    RiseRate: float
    FallRate: float


class ReplicatedVehicleState:
    SteeringInput: float
    ThrottleInput: float
    BrakeInput: float
    HandbrakeInput: float
    CurrentGear: int


class WheelSetup:
    WheelClass: unreal.UClass
    BoneName: str
    AdditionalOffset: core_uobject.Vector
    bDisableSteering: bool


class VehicleTransmissionData:
    bUseGearAutoBox: bool
    GearSwitchTime: float
    GearAutoBoxLatency: float
    FinalRatio: float
    ForwardGears: unreal.WrappedArray[VehicleGearData]
    ReverseGearRatio: float
    NeutralGearUpRatio: float
    ClutchStrength: float


class VehicleGearData:
    Ratio: float
    DownRatio: float
    UpRatio: float


class VehicleEngineData:
    TorqueCurve: engine.RuntimeFloatCurve
    MaxRPM: float
    MOI: float
    DampingRateFullThrottle: float
    DampingRateZeroThrottleClutchEngaged: float
    DampingRateZeroThrottleClutchDisengaged: float


class VehicleDifferential4WData:
    DifferentialType: int
    FrontRearSplit: float
    FrontLeftRightSplit: float
    RearLeftRightSplit: float
    CentreBias: float
    FrontBias: float
    RearBias: float


class EWheelSweepType(enum.Enum):
    Complex = 0
    Simple = 1


class EVehicleDifferential4W(enum.Enum):
    LimitedSlip_FrontDrive = 0
    LimitedSlip_RearDrive = 1
    Open_FrontDrive = 2

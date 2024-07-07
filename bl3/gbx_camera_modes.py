from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine
from . import gbx_runtime
from . import gbx_game_system_core



class CameraBehavior(unreal.UObject):
    bEnabled: bool
    bUpdatePreViewTarget: bool
    bUpdateForRemoteClient: bool
    def Update(self, DeltaTime: float, State: CameraState): ...
    def Start(self, State: CameraState): ...
    def End(self, State: CameraState): ...


class CameraBehavior_InitialRotation(CameraBehavior):
    bControlPitch: bool
    bControlYaw: bool
    bInterruptedByInput: bool
    bDisableInput: bool
    Pitch: InitialRotationAxisParams
    Yaw: InitialRotationAxisParams
    InitialCondition: gbx_runtime.GbxCondition



class CameraBehavior_BlendToFOV(CameraBehavior):
    FOVCurve: engine.CurveFloat
    bAddModifierToBaseFOV: bool
    FOVModifier: float
    MaxFOV: float
    BlendInTime: float
    BlendOutTime: float
    BlendInDelay: float
    BlendInCondition: gbx_runtime.GbxCondition
    bBlendOutWhenBlendInFails: bool
    BlendOutCondition: gbx_runtime.GbxCondition
    CurrentDelay: float
    MaxFOVModifier: float
    BlendPct: float
    bTransitioningToTargetFoV: bool



class CameraBehavior_Look(CameraBehavior):
    UpAxis: ECameraLookSpaces
    YawSpeedScale: float
    PitchSpeedScale: float
    RollSpeedScale: float
    bSnapOnStart: bool
    AXIS: CameraBehaviorLookAxis
    FeatheringFunction: gbx_game_system_core.GbxEasingFunc



class CameraBehavior_FOV(CameraBehavior):
    FOV: float



class CameraBehavior_OffsetViewModel(CameraBehavior):
    LocationOffset: core_uobject.Vector
    RotationOffset: core_uobject.Rotator
    SplitScreenLocationOffset: core_uobject.Vector
    VerticalSplitScreenLocationOffset: core_uobject.Vector
    QuadSplitScreenLocationOffset: core_uobject.Vector



class PlayerCameraModesManager(gbx_game_system_core.GbxPlayerCameraManager):
    ViewTargetClippingRadius: float
    CameraModesManager: CameraModesManager
    LastViewTarget: engine.Actor
    ViewTargetFlags: int
    def UpdateCameraShakeFromGbxFeedback(self, TrackedFeedback: gbx_game_system_core.ActiveGbxFeedbackEffect): ...
    def UpdateCameraShakeFromFeedback(self, TrackedFeedback: gbx_game_system_core.ActiveTrackedFeedback): ...


class CameraInputs(unreal.UObject):
    CurrentTime: float
    RotationInput: core_uobject.Rotator
    AdditionalInput: core_uobject.Vector
    AdditionalRoll: float
    DefaultFOV: float
    DefaultForegroundFOV: float
    EyeLocation: core_uobject.Vector
    EyeRotation: core_uobject.Rotator
    FacingRotation: core_uobject.Rotator
    CollisionSafeLocation: core_uobject.Vector
    ViewTarget: engine.Actor
    Controller: engine.PlayerController
    AttachComponent: engine.SceneComponent
    AttachSocket: str



class CameraBehavior_AnchorToEyeLocation(CameraBehavior):
    bSetRotation: bool



class CameraBehavior_AnchorToSocket(CameraBehavior):
    bSetLocation: bool
    bSetRotation: bool
    SocketName: str



class CameraBehavior_AutoFollowRotation(CameraBehavior):
    bKeepRelativeRotation: bool
    bRelativeToBase: bool
    bFollowPitch: bool
    bFollowYaw: bool
    bFollowRoll: bool
    RotationRate: float



class CameraBehavior_CollisionOffsetTrace(CameraBehavior):
    CollisionRadius: float
    TraceOffsetZ: float
    bUseAnchorAsStartLocation: bool
    bIgnoreChildToViewTarget: bool
    bIgnoreViewTargetAttachParent: bool



class CameraBehavior_DefaultFOV(CameraBehavior):
    Scale: float
    ScaleSplitScreenHorizontal: float
    ScaleSplitScreenVertical: float
    ScaleSplitScreenQuad: float
    MaxFOV: float



class CameraBehavior_FromAnimation(CameraBehavior):
    bSetLocation: bool
    bSetRotation: bool
    SocketName: str



class CameraBehavior_LimitLook(CameraBehavior):
    Min: core_uobject.Rotator
    Max: core_uobject.Rotator
    bYawRelativeToBase: bool
    bPitchRelativeToBase: bool
    bRollRelativeToBase: bool
    bSnapOnStart: bool



class CameraBehavior_LimitPitch(CameraBehavior):
    MinPitch: float
    MaxPitch: float
    bUseInitialPitch: bool
    InitialPitch: float



class CameraBehavior_OffsetAbsolute(CameraBehavior):
    LocationOffset: core_uobject.Vector



class CameraBehavior_OffsetCameraRelative(CameraBehavior):
    LocationOffset: core_uobject.Vector
    RotationOffset: core_uobject.Rotator



class CameraBehavior_OffsetCameraRelativeFromInputs(CameraBehavior):
    bHackForDayOnePatch: bool
    LimitPitch: float
    CollisionRadius: float
    MoveSpeed: float
    MoveLimit: core_uobject.Box



class CameraBehavior_RestoreControllerRotation(CameraBehavior): ...


class CameraBehavior_RestoreStartRotation(CameraBehavior):
    Rotation: core_uobject.Rotator



class CameraMode(unreal.UObject):
    Data: CameraModeData
    Behaviors: unreal.WrappedArray[CameraBehavior]



class CameraModeData(gbx_runtime.GbxDataAsset):
    ModeName: str
    BlendInTime: float
    bBlendOut: bool
    bIsFirstPerson: bool
    bShowViewModel: bool
    bAllowPitchInversion: bool
    bAutoPerspectiveOverride: bool
    bResetCameraRollOnStart: bool
    bAllowIntentionalClipping: bool
    bInterruptTransitionWhenClipping: bool
    bIncludeInDebugRotation: bool
    ViewTargetRotationUpdateMethod: EViewTargetRotationUpdateMethod
    FirstPersonBlendType: ECameraModeTransitionBlendType
    ThirdPersonBlendType: ECameraModeTransitionBlendType
    Behaviors: unreal.WrappedArray[CameraBehavior]
    bDisableSeparateTranslucency: bool



class CameraModeSet(unreal.UObject):
    Data: CameraModeSetData
    Modes: unreal.WrappedArray[CameraMode]



class CameraModeSetData(gbx_runtime.GbxDataAsset):
    Modes: unreal.WrappedArray[CameraModeData]



class CameraModesFunctionLibrary(engine.BlueprintFunctionLibrary):

    def SetCameraMode(self, Controller: engine.PlayerController, ModeName: str, BlendTimeOverride: float, bTeleport: bool, bForceResetMode: bool): ...
    def ResetCameraRotation(self, Controller: engine.PlayerController, NewRotation: core_uobject.Rotator): ...
    def RemoveCameraModeSet(self, Controller: engine.PlayerController, ModeSet: CameraModeSetData): ...
    def PushCameraMode(self, Controller: engine.PlayerController, ModeName: str, BlendTimeOverride: float, bTeleport: bool): ...
    def PopCameraMode(self, Controller: engine.PlayerController, ModeName: str, BlendTimeOverride: float, bTeleport: bool): ...
    def ApplyCameraRotation(self, Controller: engine.PlayerController, DeltaRotation: core_uobject.Rotator): ...
    def AddCameraModeSet(self, Controller: engine.PlayerController, ModeSet: CameraModeSetData): ...


class CameraModesManager(unreal.UObject):
    bIsClient: bool
    bIsRemote: bool
    ReplicatedModeState: ReplicatedCameraModeState
    bRemoteIsFirstPerson: bool
    ModeNameStack: unreal.WrappedArray[str]
    CurrentMode: CameraMode
    ModeSets: unreal.WrappedArray[CameraModeSet]
    Inputs: CameraInputs
    State: CameraState
    CameraStateClassName: core_uobject.SoftClassPath
    CameraInputsClassName: core_uobject.SoftClassPath



class CameraState(unreal.UObject):
    Inputs: CameraInputs
    POV: engine.POV
    DefaultFOV: float
    AbsoluteLocationOffset: core_uobject.Vector
    BaseLocationOffset: core_uobject.Vector
    BaseRotationOffset: core_uobject.Rotator
    BaseFOVOffset: float
    CameraLocationOffset: core_uobject.Vector
    CameraRotationOffset: core_uobject.Rotator
    ViewModelLocationOffset: core_uobject.Vector
    ViewModelRotationOffset: core_uobject.Rotator
    ViewModelFOV: float
    DefaultViewModelFOV: float
    AspectRatio: float
    bConstrainAspectRatio: bool
    bIsTransitioning: bool
    bIsColliding: bool
    bShowViewModel: bool
    bDisableSeparateTranslucency: bool
    bUpdatingInitialPitchRotation: bool
    bUpdatingInitialYawRotation: bool
    ClampedLookRotationRemainder: core_uobject.Rotator
    PostProcessBlends: unreal.WrappedArray[CameraStatePostProcessBlend]
    FocusDistance: float
    def SetViewModelFOV(self, NewFOV: float, bDefault: bool): ...
    def SetBaseRotation(self, NewRotation: core_uobject.Rotator): ...
    def SetBaseLocation(self, NewLocation: core_uobject.Vector): ...
    def SetBaseFOV(self, NewFOV: float, bDefault: bool): ...
    def GetBaseRotation(self, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def GetBaseLocation(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetBaseFOV(self, ReturnValue: float) -> float: ...
    def CameraTrace(self, Start: core_uobject.Vector, End: core_uobject.Vector, Radius: float, TraceChannel: int, IgnoreMask: int, OutHit: engine.HitResult, ReturnValue: bool) -> bool: ...
    def AddPostProcessBlend(self, Settings: engine.PostProcessSettings, BlendWeight: float): ...


class CameraViewTargetInterface(core_uobject.Interface): ...


class ReplicatedCameraModeState:
    ModeName: str
    BlendTimeOverride: float



class InitialRotationAxisParams:
    MinAngle: float
    MaxAngle: float
    bRelativeToBase: bool
    bLinearInterpolation: bool
    Speed: float
    SpeedScaleCurve: engine.CurveFloat
    Delay: float



class CameraBehaviorLookAxis:
    InputScale: float
    bLimit: bool
    MinAngle: float
    MaxAngle: float
    FeatheringAngle: float
    FeatheringInputScale: float



class CameraStatePostProcessBlend: ...


class ECameraBehaviorLookAxis(enum.Enum):
    Yaw = 0
    Roll = 1


class ECameraLookSpaces(enum.Enum):
    ViewTarget = 0
    ViewTargetBase = 1


class ECameraModeTransitionBlendType(enum.Enum):
    FOV = 0
    Full = 1


class EViewTargetRotationUpdateMethod(enum.Enum):
    Fixed = 0
    FromInputDelta = 1

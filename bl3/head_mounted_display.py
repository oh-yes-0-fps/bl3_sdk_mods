from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine
from . import input_core



class HeadMountedDisplayFunctionLibrary(engine.BlueprintFunctionLibrary):

    def SetWorldToMetersScale(self, WorldContext: unreal.UObject, NewScale: float): ...
    def SetTrackingOrigin(self, Origin: int): ...
    def SetSpectatorScreenTexture(self, InTexture: engine.Texture): ...
    def SetSpectatorScreenModeTexturePlusEyeLayout(self, EyeRectMin: core_uobject.Vector2D, EyeRectMax: core_uobject.Vector2D, TextureRectMin: core_uobject.Vector2D, TextureRectMax: core_uobject.Vector2D, bDrawEyeFirst: bool, bClearBlack: bool): ...
    def SetSpectatorScreenMode(self, Mode: ESpectatorScreenMode): ...
    def SetClippingPlanes(self, Near: float, Far: float): ...
    def ResetOrientationAndPosition(self, Yaw: float, Options: int): ...
    def IsSpectatorScreenModeControllable(self, ReturnValue: bool) -> bool: ...
    def IsInLowPersistenceMode(self, ReturnValue: bool) -> bool: ...
    def IsHeadMountedDisplayEnabled(self, ReturnValue: bool) -> bool: ...
    def IsHeadMountedDisplayConnected(self, ReturnValue: bool) -> bool: ...
    def IsDeviceTracking(self, XRDeviceId: XRDeviceId, ReturnValue: bool) -> bool: ...
    def HasValidTrackingPosition(self, ReturnValue: bool) -> bool: ...
    def GetWorldToMetersScale(self, WorldContext: unreal.UObject, ReturnValue: float) -> float: ...
    def GetVRFocusState(self, bUseFocus: bool, bHasFocus: bool): ...
    def GetTrackingToWorldTransform(self, WorldContext: unreal.UObject, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def GetTrackingSensorParameters(self, Origin: core_uobject.Vector, Rotation: core_uobject.Rotator, LeftFOV: float, RightFOV: float, TopFOV: float, BottomFOV: float, Distance: float, NearPlane: float, FarPlane: float, IsActive: bool, Index: int): ...
    def GetTrackingOrigin(self, ReturnValue: int) -> int: ...
    def GetScreenPercentage(self, ReturnValue: float) -> float: ...
    def GetPositionalTrackingCameraParameters(self, CameraOrigin: core_uobject.Vector, CameraRotation: core_uobject.Rotator, HFOV: float, VFOV: float, CameraDistance: float, NearPlane: float, FarPlane: float): ...
    def GetPixelDensity(self, ReturnValue: float) -> float: ...
    def GetOrientationAndPosition(self, DeviceRotation: core_uobject.Rotator, DevicePosition: core_uobject.Vector): ...
    def GetNumOfTrackingSensors(self, ReturnValue: int) -> int: ...
    def GetHMDWornState(self, ReturnValue: int) -> int: ...
    def GetHMDDeviceName(self, ReturnValue: str) -> str: ...
    def GetDeviceWorldPose(self, WorldContext: unreal.UObject, XRDeviceId: XRDeviceId, bIsTracked: bool, Orientation: core_uobject.Rotator, bHasPositionalTracking: bool, Position: core_uobject.Vector): ...
    def GetDevicePose(self, XRDeviceId: XRDeviceId, bIsTracked: bool, Orientation: core_uobject.Rotator, bHasPositionalTracking: bool, Position: core_uobject.Vector): ...
    def EnumerateTrackedDevices(self, SystemId: str, DeviceType: EXRTrackedDeviceType, ReturnValue: unreal.WrappedArray[XRDeviceId]) -> unreal.WrappedArray[XRDeviceId]: ...
    def EnableLowPersistenceMode(self, bEnable: bool): ...
    def EnableHMD(self, bEnable: bool, ReturnValue: bool) -> bool: ...


class MotionControllerComponent(engine.PrimitiveComponent):
    PlayerIndex: int
    Hand: input_core.EControllerHand
    MotionSource: str
    bDisableLowLatencyUpdate: bool
    CurrentTrackingStatus: ETrackingStatus
    bDisplayDeviceModel: bool
    DisplayModelSource: str
    CustomDisplayMesh: engine.StaticMesh
    DisplayMeshMaterialOverrides: unreal.WrappedArray[engine.MaterialInterface]
    DisplayComponent: engine.PrimitiveComponent
    def SetTrackingSource(self, NewSource: input_core.EControllerHand): ...
    def SetTrackingMotionSource(self, NewSource: str): ...
    def SetShowDeviceModel(self, bShowControllerModel: bool): ...
    def SetDisplayModelSource(self, NewDisplayModelSource: str): ...
    def SetCustomDisplayMesh(self, NewDisplayMesh: engine.StaticMesh): ...
    def SetAssociatedPlayerIndex(self, NewPlayer: int): ...
    def OnMotionControllerUpdated(self): ...
    def IsTracked(self, ReturnValue: bool) -> bool: ...
    def GetTrackingSource(self, ReturnValue: input_core.EControllerHand) -> input_core.EControllerHand: ...
    def GetParameterValue(self, InName: str, bValueFound: bool, ReturnValue: float) -> float: ...


class MotionTrackedDeviceFunctionLibrary(engine.BlueprintFunctionLibrary):

    def SetIsControllerMotionTrackingEnabledByDefault(self, Enable: bool): ...
    def IsMotionTrackingEnabledForSource(self, PlayerIndex: int, SourceName: str, ReturnValue: bool) -> bool: ...
    def IsMotionTrackingEnabledForDevice(self, PlayerIndex: int, Hand: input_core.EControllerHand, ReturnValue: bool) -> bool: ...
    def IsMotionTrackingEnabledForComponent(self, MotionControllerComponent: MotionControllerComponent, ReturnValue: bool) -> bool: ...
    def IsMotionTrackedDeviceCountManagementNecessary(self, ReturnValue: bool) -> bool: ...
    def IsMotionSourceTracking(self, PlayerIndex: int, SourceName: str, ReturnValue: bool) -> bool: ...
    def GetMotionTrackingEnabledControllerCount(self, ReturnValue: int) -> int: ...
    def GetMaximumMotionTrackedControllerCount(self, ReturnValue: int) -> int: ...
    def GetActiveTrackingSystemName(self, ReturnValue: str) -> str: ...
    def EnumerateMotionSources(self, ReturnValue: unreal.WrappedArray[str]) -> unreal.WrappedArray[str]: ...
    def EnableMotionTrackingOfSource(self, PlayerIndex: int, SourceName: str, ReturnValue: bool) -> bool: ...
    def EnableMotionTrackingOfDevice(self, PlayerIndex: int, Hand: input_core.EControllerHand, ReturnValue: bool) -> bool: ...
    def EnableMotionTrackingForComponent(self, MotionControllerComponent: MotionControllerComponent, ReturnValue: bool) -> bool: ...
    def DisableMotionTrackingOfSource(self, PlayerIndex: int, SourceName: str): ...
    def DisableMotionTrackingOfDevice(self, PlayerIndex: int, Hand: input_core.EControllerHand): ...
    def DisableMotionTrackingOfControllersForPlayer(self, PlayerIndex: int): ...
    def DisableMotionTrackingOfAllControllers(self): ...
    def DisableMotionTrackingForComponent(self, MotionControllerComponent: MotionControllerComponent): ...


class VRNotificationsComponent(engine.ActorComponent): ...


class XRAssetFunctionLibrary(engine.BlueprintFunctionLibrary):

    def AddNamedDeviceVisualizationComponentBlocking(self, Target: engine.Actor, SystemName: str, DeviceName: str, bManualAttachment: bool, RelativeTransform: core_uobject.Transform, XRDeviceId: XRDeviceId, ReturnValue: engine.PrimitiveComponent) -> engine.PrimitiveComponent: ...
    def AddDeviceVisualizationComponentBlocking(self, Target: engine.Actor, XRDeviceId: XRDeviceId, bManualAttachment: bool, RelativeTransform: core_uobject.Transform, ReturnValue: engine.PrimitiveComponent) -> engine.PrimitiveComponent: ...


class AsyncTask_LoadXRDeviceVisComponent(engine.BlueprintAsyncActionBase):
    SpawnedComponent: engine.PrimitiveComponent
    def AddNamedDeviceVisualizationComponentAsync(self, Target: engine.Actor, SystemName: str, DeviceName: str, bManualAttachment: bool, RelativeTransform: core_uobject.Transform, XRDeviceId: XRDeviceId, NewComponent: engine.PrimitiveComponent, ReturnValue: AsyncTask_LoadXRDeviceVisComponent) -> AsyncTask_LoadXRDeviceVisComponent: ...
    def AddDeviceVisualizationComponentAsync(self, Target: engine.Actor, XRDeviceId: XRDeviceId, bManualAttachment: bool, RelativeTransform: core_uobject.Transform, NewComponent: engine.PrimitiveComponent, ReturnValue: AsyncTask_LoadXRDeviceVisComponent) -> AsyncTask_LoadXRDeviceVisComponent: ...


class XRDeviceId:
    SystemName: str
    DeviceID: int



class EXRTrackedDeviceType(enum.Enum):
    TrackingReference = 0
    Controller = 1
    EXRTrackedDeviceType_MAX = 2


class ESpectatorScreenMode(enum.Enum):
    SingleEyeLetterboxed = 0
    SingleEye = 1
    Undistorted = 2
    ESpectatorScreenMode_MAX = 3


class EHMDWornState(enum.Enum):
    Worn = 0
    NotWorn = 1


class EHMDTrackingOrigin(enum.Enum):
    Eye = 0
    EHMDTrackingOrigin_MAX = 1


class EOrientPositionSelector(enum.Enum):
    Position = 0
    OrientationAndPosition = 1


class ETrackingStatus(enum.Enum):
    InertialOnly = 0
    Tracked = 1

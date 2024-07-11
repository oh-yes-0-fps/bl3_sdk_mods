from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import input_core


class HeadMountedDisplayFunctionLibrary(engine.BlueprintFunctionLibrary):

    def SetWorldToMetersScale(self, WorldContext: unreal.UObject, NewScale: float): ...
    def SetTrackingOrigin(self, Origin: int): ...
    def SetSpectatorScreenTexture(self, InTexture: engine.Texture): ...
    def SetSpectatorScreenModeTexturePlusEyeLayout(
        self,
        EyeRectMin: core_uobject.Vector2D,
        EyeRectMax: core_uobject.Vector2D,
        TextureRectMin: core_uobject.Vector2D,
        TextureRectMax: core_uobject.Vector2D,
        bDrawEyeFirst: bool,
        bClearBlack: bool,
    ): ...
    def SetSpectatorScreenMode(self, Mode: ESpectatorScreenMode): ...
    def SetClippingPlanes(self, Near: float, Far: float): ...
    def ResetOrientationAndPosition(self, Yaw: float, Options: int): ...
    def IsSpectatorScreenModeControllable(self) -> bool: ...
    def IsInLowPersistenceMode(self) -> bool: ...
    def IsHeadMountedDisplayEnabled(self) -> bool: ...
    def IsHeadMountedDisplayConnected(self) -> bool: ...
    def IsDeviceTracking(self, XRDeviceId: XRDeviceId) -> bool: ...
    def HasValidTrackingPosition(self) -> bool: ...
    def GetWorldToMetersScale(self, WorldContext: unreal.UObject) -> float: ...
    def GetVRFocusState(self, bUseFocus: bool, bHasFocus: bool): ...
    def GetTrackingToWorldTransform(
        self, WorldContext: unreal.UObject
    ) -> core_uobject.Transform: ...
    def GetTrackingSensorParameters(
        self,
        Origin: core_uobject.Vector,
        Rotation: core_uobject.Rotator,
        LeftFOV: float,
        RightFOV: float,
        TopFOV: float,
        BottomFOV: float,
        Distance: float,
        NearPlane: float,
        FarPlane: float,
        IsActive: bool,
        Index: int,
    ): ...
    def GetTrackingOrigin(self) -> int: ...
    def GetScreenPercentage(self) -> float: ...
    def GetPositionalTrackingCameraParameters(
        self,
        CameraOrigin: core_uobject.Vector,
        CameraRotation: core_uobject.Rotator,
        HFOV: float,
        VFOV: float,
        CameraDistance: float,
        NearPlane: float,
        FarPlane: float,
    ): ...
    def GetPixelDensity(self) -> float: ...
    def GetOrientationAndPosition(
        self, DeviceRotation: core_uobject.Rotator, DevicePosition: core_uobject.Vector
    ): ...
    def GetNumOfTrackingSensors(self) -> int: ...
    def GetHMDWornState(self) -> int: ...
    def GetHMDDeviceName(self) -> str: ...
    def GetDeviceWorldPose(
        self,
        WorldContext: unreal.UObject,
        XRDeviceId: XRDeviceId,
        bIsTracked: bool,
        Orientation: core_uobject.Rotator,
        bHasPositionalTracking: bool,
        Position: core_uobject.Vector,
    ): ...
    def GetDevicePose(
        self,
        XRDeviceId: XRDeviceId,
        bIsTracked: bool,
        Orientation: core_uobject.Rotator,
        bHasPositionalTracking: bool,
        Position: core_uobject.Vector,
    ): ...
    def EnumerateTrackedDevices(
        self, SystemId: str, DeviceType: EXRTrackedDeviceType
    ) -> unreal.WrappedArray[XRDeviceId]: ...
    def EnableLowPersistenceMode(self, bEnable: bool): ...
    def EnableHMD(self, bEnable: bool) -> bool: ...


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
    def IsTracked(self) -> bool: ...
    def GetTrackingSource(self) -> input_core.EControllerHand: ...
    def GetParameterValue(self, InName: str, bValueFound: bool) -> float: ...


class MotionTrackedDeviceFunctionLibrary(engine.BlueprintFunctionLibrary):

    def SetIsControllerMotionTrackingEnabledByDefault(self, Enable: bool): ...
    def IsMotionTrackingEnabledForSource(
        self, PlayerIndex: int, SourceName: str
    ) -> bool: ...
    def IsMotionTrackingEnabledForDevice(
        self, PlayerIndex: int, Hand: input_core.EControllerHand
    ) -> bool: ...
    def IsMotionTrackingEnabledForComponent(
        self, MotionControllerComponent: MotionControllerComponent
    ) -> bool: ...
    def IsMotionTrackedDeviceCountManagementNecessary(self) -> bool: ...
    def IsMotionSourceTracking(self, PlayerIndex: int, SourceName: str) -> bool: ...
    def GetMotionTrackingEnabledControllerCount(self) -> int: ...
    def GetMaximumMotionTrackedControllerCount(self) -> int: ...
    def GetActiveTrackingSystemName(self) -> str: ...
    def EnumerateMotionSources(self) -> unreal.WrappedArray[str]: ...
    def EnableMotionTrackingOfSource(
        self, PlayerIndex: int, SourceName: str
    ) -> bool: ...
    def EnableMotionTrackingOfDevice(
        self, PlayerIndex: int, Hand: input_core.EControllerHand
    ) -> bool: ...
    def EnableMotionTrackingForComponent(
        self, MotionControllerComponent: MotionControllerComponent
    ) -> bool: ...
    def DisableMotionTrackingOfSource(self, PlayerIndex: int, SourceName: str): ...
    def DisableMotionTrackingOfDevice(
        self, PlayerIndex: int, Hand: input_core.EControllerHand
    ): ...
    def DisableMotionTrackingOfControllersForPlayer(self, PlayerIndex: int): ...
    def DisableMotionTrackingOfAllControllers(self): ...
    def DisableMotionTrackingForComponent(
        self, MotionControllerComponent: MotionControllerComponent
    ): ...


class VRNotificationsComponent(engine.ActorComponent):
    HMDTrackingInitializingAndNeedsHMDToBeTrackedDelegate: Any
    HMDTrackingInitializedDelegate: Any
    HMDRecenteredDelegate: Any
    HMDLostDelegate: Any
    HMDReconnectedDelegate: Any
    HMDConnectCanceledDelegate: Any
    HMDPutOnHeadDelegate: Any
    HMDRemovedFromHeadDelegate: Any
    VRControllerRecenteredDelegate: Any


class XRAssetFunctionLibrary(engine.BlueprintFunctionLibrary):

    def AddNamedDeviceVisualizationComponentBlocking(
        self,
        Target: engine.Actor,
        SystemName: str,
        DeviceName: str,
        bManualAttachment: bool,
        RelativeTransform: core_uobject.Transform,
        XRDeviceId: XRDeviceId,
    ) -> engine.PrimitiveComponent: ...
    def AddDeviceVisualizationComponentBlocking(
        self,
        Target: engine.Actor,
        XRDeviceId: XRDeviceId,
        bManualAttachment: bool,
        RelativeTransform: core_uobject.Transform,
    ) -> engine.PrimitiveComponent: ...


class AsyncTask_LoadXRDeviceVisComponent(engine.BlueprintAsyncActionBase):
    OnModelLoaded: Any
    OnLoadFailure: Any
    SpawnedComponent: engine.PrimitiveComponent

    def AddNamedDeviceVisualizationComponentAsync(
        self,
        Target: engine.Actor,
        SystemName: str,
        DeviceName: str,
        bManualAttachment: bool,
        RelativeTransform: core_uobject.Transform,
        XRDeviceId: XRDeviceId,
        NewComponent: engine.PrimitiveComponent,
    ) -> AsyncTask_LoadXRDeviceVisComponent: ...
    def AddDeviceVisualizationComponentAsync(
        self,
        Target: engine.Actor,
        XRDeviceId: XRDeviceId,
        bManualAttachment: bool,
        RelativeTransform: core_uobject.Transform,
        NewComponent: engine.PrimitiveComponent,
    ) -> AsyncTask_LoadXRDeviceVisComponent: ...


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

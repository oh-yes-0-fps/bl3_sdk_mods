from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine


class CameraRig_Crane(engine.Actor):
    CranePitch: float
    CraneYaw: float
    CraneArmLength: float
    bLockMountPitch: bool
    bLockMountYaw: bool
    TransformComponent: engine.SceneComponent
    CraneYawControl: engine.SceneComponent
    CranePitchControl: engine.SceneComponent
    CraneCameraMount: engine.SceneComponent


class CameraRig_Rail(engine.Actor):
    CurrentPositionOnRail: float
    bLockOrientationToRail: bool
    TransformComponent: engine.SceneComponent
    RailSplineComponent: engine.SplineComponent
    RailCameraMount: engine.SceneComponent


class CineCameraActor(engine.CameraActor):
    LookatTrackingSettings: CameraLookatTrackingSettings

    def GetCineCameraComponent(self) -> CineCameraComponent: ...


class CineCameraComponent(engine.CameraComponent):
    FilmbackSettings: CameraFilmbackSettings
    LensSettings: CameraLensSettings
    FocusSettings: CameraFocusSettings
    CurrentFocalLength: float
    CurrentAperture: float
    CurrentFocusDistance: float
    FocusPlaneVisualizationMesh: engine.StaticMesh
    FocusPlaneVisualizationMaterial: engine.Material
    DebugFocusPlaneComponent: engine.StaticMeshComponent
    DebugFocusPlaneMID: engine.MaterialInstanceDynamic
    FilmbackPresets: unreal.WrappedArray[NamedFilmbackPreset]
    LensPresets: unreal.WrappedArray[NamedLensPreset]
    DefaultFilmbackPresetName: str
    DefaultLensPresetName: str
    DefaultLensFocalLength: float
    DefaultLensFStop: float

    def SetLensPresetByName(self, InPresetName: str): ...
    def SetFilmbackPresetByName(self, InPresetName: str): ...
    def GetVerticalFieldOfView(self) -> float: ...
    def GetLensPresetName(self) -> str: ...
    def GetHorizontalFieldOfView(self) -> float: ...
    def GetFilmbackPresetName(self) -> str: ...


class CameraLookatTrackingSettings:
    bEnableLookAtTracking: bool
    bDrawDebugLookAtTrackingPosition: bool
    LookAtTrackingInterpSpeed: float
    ActorToTrack: engine.Actor
    RelativeOffset: core_uobject.Vector
    bAllowRoll: bool


class CameraFocusSettings:
    FocusMethod: ECameraFocusMethod
    ManualFocusDistance: float
    TrackingFocusSettings: CameraTrackingFocusSettings
    bDrawDebugFocusPlane: bool
    DebugFocusPlaneColor: core_uobject.Color
    bSmoothFocusChanges: bool
    FocusSmoothingInterpSpeed: float
    FocusOffset: float


class CameraTrackingFocusSettings:
    ActorToTrack: engine.Actor
    RelativeOffset: core_uobject.Vector
    bDrawDebugTrackingFocusPoint: bool


class NamedLensPreset:
    Name: str
    LensSettings: CameraLensSettings


class CameraLensSettings:
    MinFocalLength: float
    MaxFocalLength: float
    MinFStop: float
    MaxFStop: float
    MinimumFocusDistance: float
    DiaphragmBladeCount: int


class NamedFilmbackPreset:
    Name: str
    FilmbackSettings: CameraFilmbackSettings


class CameraFilmbackSettings:
    SensorWidth: float
    SensorHeight: float
    SensorAspectRatio: float


class ECameraFocusMethod(enum.Enum):
    Manual = 0
    Tracking = 1

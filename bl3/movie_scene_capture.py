from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine


class MovieSceneCaptureProtocolSettings(unreal.UObject): ...


class CompositionGraphCaptureSettings(MovieSceneCaptureProtocolSettings):
    IncludeRenderPasses: CompositionGraphCapturePasses
    bCaptureFramesInHDR: bool
    HDRCompressionQuality: int
    CaptureGamut: int
    PostProcessingMaterial: core_uobject.SoftObjectPath
    bDisableScreenPercentage: bool


class FrameGrabberProtocolSettings(MovieSceneCaptureProtocolSettings): ...


class BmpImageCaptureSettings(MovieSceneCaptureProtocolSettings): ...


class ImageCaptureSettings(FrameGrabberProtocolSettings):
    CompressionQuality: int


class MovieSceneCaptureInterface(core_uobject.Interface): ...


class MovieSceneCapture(unreal.UObject):
    CaptureType: CaptureProtocolID
    ProtocolSettings: MovieSceneCaptureProtocolSettings
    Settings: MovieSceneCaptureSettings
    bUseSeparateProcess: bool
    bCloseEditorWhenCaptureStarts: bool
    AdditionalCommandLineArguments: str
    InheritedCommandLineArguments: str


class LevelCapture(MovieSceneCapture):
    bAutoStartCapture: bool
    PrerequisiteActorId: core_uobject.Guid


class MovieSceneCaptureEnvironment(unreal.UObject):

    def GetCaptureFrameNumber(self) -> int: ...
    def GetCaptureElapsedTime(self) -> float: ...


class VideoCaptureSettings(FrameGrabberProtocolSettings):
    bUseCompression: bool
    CompressionQuality: float
    VideoCodec: str


class CompositionGraphCapturePasses:
    Value: unreal.WrappedArray[str]


class CaptureProtocolID:
    Identifier: str


class MovieSceneCaptureSettings:
    OutputDirectory: engine.DirectoryPath
    GameModeOverride: unreal.UClass
    OutputFormat: str
    bOverwriteExisting: bool
    bUseRelativeFrameNumbers: bool
    HandleFrames: int
    ZeroPadFrameNumbers: int
    FrameRate: core_uobject.FrameRate
    Resolution: CaptureResolution
    bEnableTextureStreaming: bool
    bCinematicEngineScalability: bool
    bCinematicMode: bool
    bAllowMovement: bool
    bAllowTurning: bool
    bShowPlayer: bool
    bShowHUD: bool


class CaptureResolution:
    ResX: int
    ResY: int


class EHDRCaptureGamut(enum.Enum):
    HCGM_P3DCI = 0
    HCGM_Rec2020 = 1
    HCGM_ACEScg = 2

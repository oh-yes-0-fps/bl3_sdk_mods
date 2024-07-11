from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine


class AppleImageUtilsBaseAsyncTaskBlueprintProxy(unreal.UObject):
    OnSuccess: Any
    OnFailure: Any
    ConversionResult: AppleImageUtilsImageConversionResult

    def CreateProxyObjectForConvertToTIFF(
        self, SourceImage: engine.Texture, bWantColor: bool, bUseGpu: bool
    ) -> AppleImageUtilsBaseAsyncTaskBlueprintProxy: ...
    def CreateProxyObjectForConvertToPNG(
        self, SourceImage: engine.Texture, bWantColor: bool, bUseGpu: bool
    ) -> AppleImageUtilsBaseAsyncTaskBlueprintProxy: ...
    def CreateProxyObjectForConvertToJPEG(
        self, SourceImage: engine.Texture, Quality: int, bWantColor: bool, bUseGpu: bool
    ) -> AppleImageUtilsBaseAsyncTaskBlueprintProxy: ...
    def CreateProxyObjectForConvertToHEIF(
        self, SourceImage: engine.Texture, Quality: int, bWantColor: bool, bUseGpu: bool
    ) -> AppleImageUtilsBaseAsyncTaskBlueprintProxy: ...


class AppleImageInterface(core_uobject.Interface): ...


class AppleImageUtilsImageConversionResult:
    Error: str
    ImageData: unreal.WrappedArray[int]


class EAppleTextureType(enum.Enum):
    Image = 0
    PixelBuffer = 1
    MetalTexture = 2

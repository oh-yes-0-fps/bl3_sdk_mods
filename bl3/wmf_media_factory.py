from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum





class WmfMediaSettings(unreal.UObject):
    AllowNonStandardCodecs: bool
    LowLatency: bool
    NativeAudioOut: bool


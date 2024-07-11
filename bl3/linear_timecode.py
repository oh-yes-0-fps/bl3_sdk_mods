from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import media_assets


class LinearTimecodeComponent(engine.SceneComponent):
    MediaPlayer: media_assets.MediaPlayer
    DropTimecode: DropTimecode
    OnTimecodeChange: Any

    def SetDropTimecodeFrameNumber(
        self, Timecode: DropTimecode, FrameNumber: int, OutTimecode: DropTimecode
    ): ...
    def GetDropTimeCodeFrameNumber(self, Timecode: DropTimecode, FrameNumber: int): ...
    def GetDropFrameNumber(self) -> int: ...


class DropTimecodeToStringConversion(engine.BlueprintFunctionLibrary):

    def Conv_DropTimecodeToString(self, InTimecode: DropTimecode) -> str: ...


class DropTimecode:
    Timecode: core_uobject.Timecode
    FrameRate: int
    bColorFraming: bool
    bRunningForward: bool
    bNewFrame: bool

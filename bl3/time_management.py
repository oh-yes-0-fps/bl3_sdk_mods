from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine


class FixedFrameRateCustomTimeStep(engine.EngineCustomTimeStep):
    FixedFrameRate: core_uobject.FrameRate


class TimeManagementBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def Multiply_SecondsFrameRate(
        self, TimeInSeconds: float, FrameRate: core_uobject.FrameRate
    ) -> core_uobject.FrameTime: ...
    def GetTimecode(self) -> core_uobject.Timecode: ...
    def Conv_TimecodeToString(
        self, InTimecode: core_uobject.Timecode, bForceSignDisplay: bool
    ) -> str: ...
    def Conv_QualifiedFrameTimeToSeconds(
        self, InFrameTime: core_uobject.QualifiedFrameTime
    ) -> float: ...
    def Conv_FrameRateToSeconds(self, InFrameRate: core_uobject.FrameRate) -> float: ...


class TimeSynchronizationSource(unreal.UObject):
    bUseForSynchronization: bool
    NumberOfExtraBufferedFrame: int
    TimeDelay: float


class EFrameNumberDisplayFormats(enum.Enum):
    Seconds = 0
    DropFrameTimecode = 1
    MAX_Count = 2

from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine


class GbxPerfScopeOptions(unreal.UObject):
    AnalyticsURL: str


class GbxPerfScopePerfSampleData(unreal.UObject):
    Samples: unreal.WrappedArray[PerfSample]

    def GetMapGPUHotspots(
        self,
        WorldContext: unreal.UObject,
        NumSamples: int,
        LatentInfo: engine.LatentActionInfo,
    ): ...


class PerfSample:
    Position: core_uobject.Vector
    Rotation: core_uobject.Rotator
    GpuMS: float

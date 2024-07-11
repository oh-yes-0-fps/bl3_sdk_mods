from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


class PlatformRuntimeAudioCompressionOverrides:
    bOverrideCompressionTimes: bool
    DurationThreshold: float
    MaxNumRandomBranches: int
    SoundCueQualityIndex: int


class ESoundwaveSampleRateSettings(enum.Enum):
    High = 0
    Medium = 1
    Min = 2

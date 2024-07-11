from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import engine


class AudioCurveSourceComponent(engine.AudioComponent):
    CurveSourceBindingName: str
    CurveSyncOffset: float

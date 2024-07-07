from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import engine



class AudioCurveSourceComponent(engine.AudioComponent):
    CurveSourceBindingName: str
    CurveSyncOffset: float


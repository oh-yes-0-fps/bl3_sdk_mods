from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import renderer



class LightPropagationVolumeBlendable(unreal.UObject):
    Settings: renderer.LightPropagationVolumeSettings
    BlendWeight: float


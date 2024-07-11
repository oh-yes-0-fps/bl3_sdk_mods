from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject


class AudioMixerWwiseSettings(unreal.UObject):
    PassthroughEvent: core_uobject.SoftObjectPath

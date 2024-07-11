from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject


class GbxProbeInterface(core_uobject.Interface):

    def GetGbxProbeId(self, OutId: GbxProbeId): ...


class GbxProbeId:
    Class: str
    Type: str
    SubType: str


class EGbxProbeResult(enum.Enum):
    Skipped = 0
    Succeeded = 1
    Disabled = 2

from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import engine


class GbxRumbleRemapping(unreal.UObject):
    WindowsMapping: RemapByConsole
    XBoxOneMapping: RemapByConsole
    PS4Mapping: RemapByConsole
    XBoxSeriesXMapping: RemapByConsole
    PS5Mapping: RemapByConsole


class RemapByConsole:
    ConsoleName: str
    RemapValues: RumbleRemap


class RumbleRemap:
    LeftSmallScalar: RumbleSlotMapping
    LeftLargeScalar: RumbleSlotMapping
    RightSmallScalar: RumbleSlotMapping
    RightLargeScalar: RumbleSlotMapping


class RumbleSlotMapping:
    MapSlotTo: ERumbleSlot
    MappingScalar: engine.RuntimeFloatCurve


class EPlatform(enum.Enum):
    PS4 = 0
    XBoxOne = 1
    XBoxSeriesX = 2


class ERumbleSlot(enum.Enum):
    LeftLarge = 0
    ERumbleSlot_MAX = 1
    RightSmall = 2

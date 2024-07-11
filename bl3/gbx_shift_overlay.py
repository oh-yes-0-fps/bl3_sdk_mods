from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject


class GbxShiftOverlay(unreal.UObject): ...


class GbxShiftSaveGameInterface(core_uobject.Interface): ...


class GbxShiftOverlaySettings(unreal.UObject):
    ZOrder: int
    bAutoBlockOnMapLoad: bool
    bAutoBlockOnMovie: bool
    bAutoBlockOnCinematic: bool
    bAutoBlockOnAppFocus: bool
    NotificationPadding: int
    NotificationSizeX: float
    NotificationSizeY: float
    OverlayVirtualResX: int
    OverlayVirtualResY: int
    InputModeThreshold_Cursor: float
    InputModeThreshold_Analog: float

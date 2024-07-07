from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject



class Overlays(unreal.UObject): ...


class BasicOverlays(Overlays):
    Overlays: unreal.WrappedArray[OverlayItem]



class LocalizedOverlays(Overlays):
    DefaultOverlays: BasicOverlays



class OverlayItem:
    StartTime: core_uobject.Timespan
    EndTime: core_uobject.Timespan
    Text: str
    Position: core_uobject.Vector2D


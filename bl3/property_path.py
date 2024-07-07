from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject



class CachedPropertyPath:
    Segments: unreal.WrappedArray[PropertyPathSegment]
    CachedFunction: core_uobject.Function



class PropertyPathSegment:
    Name: str
    ArrayIndex: int
    Struct: unreal.UStruct
    Field: core_uobject.Field


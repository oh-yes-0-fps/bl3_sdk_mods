from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject



class StructSerializerTestStruct:
    Numerics: StructSerializerNumericTestStruct
    Booleans: StructSerializerBooleanTestStruct
    Objects: StructSerializerObjectTestStruct
    Builtins: StructSerializerBuiltinTestStruct
    Arrays: StructSerializerArrayTestStruct
    Maps: StructSerializerMapTestStruct



class StructSerializerMapTestStruct: ...


class StructSerializerArrayTestStruct:
    Int32Array: unreal.WrappedArray[int]
    StaticSingleElement: int
    StaticInt32Array: int
    StaticFloatArray: float
    VectorArray: unreal.WrappedArray[core_uobject.Vector]



class StructSerializerBuiltinTestStruct:
    Guid: core_uobject.Guid
    Name: str
    String: str
    Rotator: core_uobject.Rotator
    Text: str
    Vector: core_uobject.Vector



class StructSerializerObjectTestStruct:
    Class: unreal.UClass
    ObjectPtr: unreal.UObject



class StructSerializerBooleanTestStruct:
    BoolFalse: bool
    BoolTrue: bool



class StructSerializerNumericTestStruct:
    Int8: int
    Int16: int
    Int32: int
    Int64: int
    Uint8: int
    Float: float
    Double: float


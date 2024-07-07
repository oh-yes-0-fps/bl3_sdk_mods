from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum





class Object:

    def ExecuteUbergraph(self, EntryPoint: int): ...


class Interface(unreal.UObject): ...


class Package(unreal.UObject): ...


class Field(unreal.UObject): ...


class Struct(Field): ...


class Class(unreal.UStruct): ...


class GCObjectReferencer(unreal.UObject): ...


class TextBuffer(unreal.UObject): ...


class ScriptStruct(unreal.UStruct): ...


class Function(unreal.UStruct): ...


class DelegateFunction(Function): ...


class DynamicClass(unreal.UClass): ...


class PackageMap(unreal.UObject): ...


class Enum(Field): ...


class Property(Field): ...


class EnumProperty(Property): ...


class LinkerPlaceholderClass(unreal.UClass): ...


class LinkerPlaceholderExportObject(unreal.UObject): ...


class LinkerPlaceholderFunction(Function): ...


class MetaData(unreal.UObject): ...


class ObjectRedirector(unreal.UObject): ...


class ArrayProperty(Property): ...


class ObjectPropertyBase(Property): ...


class BoolProperty(Property): ...


class NumericProperty(Property): ...


class ByteProperty(NumericProperty): ...


class ObjectProperty(ObjectPropertyBase): ...


class ClassProperty(ObjectProperty): ...


class DelegateProperty(Property): ...


class DoubleProperty(NumericProperty): ...


class FloatProperty(NumericProperty): ...


class IntProperty(NumericProperty): ...


class Int16Property(NumericProperty): ...


class Int64Property(NumericProperty): ...


class Int8Property(NumericProperty): ...


class InterfaceProperty(Property): ...


class LazyObjectProperty(ObjectPropertyBase): ...


class MapProperty(Property): ...


class MulticastDelegateProperty(Property): ...


class NameProperty(Property): ...


class SetProperty(Property): ...


class SoftObjectProperty(ObjectPropertyBase): ...


class SoftClassProperty(SoftObjectProperty): ...


class StrProperty(Property): ...


class StructProperty(Property): ...


class UInt16Property(NumericProperty): ...


class UInt32Property(NumericProperty): ...


class UInt64Property(NumericProperty): ...


class WeakObjectProperty(ObjectPropertyBase): ...


class TextProperty(Property): ...


class Default__Struct: ...


class Default__ScriptStruct: ...


class JoinabilitySettings:
    SessionName: str
    bPublicSearchable: bool
    bAllowInvites: bool
    bJoinViaPresence: bool
    bJoinViaPresenceFriendsOnly: bool
    MaxPlayers: int
    MaxPartySize: int



class UniqueNetIdWrapper: ...


class Guid:
    A: int
    B: int
    C: int
    D: int



class Vector:
    X: float
    Y: float
    Z: float



class Vector4:
    X: float
    Y: float
    Z: float
    W: float



class Vector2D:
    X: float
    Y: float



class TwoVectors:
    v1: Vector
    v2: Vector



class Plane(Vector):
    W: float



class Rotator:
    Pitch: float
    Yaw: float
    Roll: float



class Quat:
    X: float
    Y: float
    Z: float
    W: float



class PackedNormal:
    X: int
    Y: int
    Z: int
    W: int



class PackedRGB1_A2N:
    Packed: int



class PackedRGBA16N:
    XY: int
    ZW: int



class IntPoint:
    X: int
    Y: int



class IntVector:
    X: int
    Y: int
    Z: int



class IntVector4:
    X: int
    Y: int
    Z: int
    W: int



class Color:
    B: int
    G: int
    R: int
    A: int



class LinearColor:
    R: float
    G: float
    B: float
    A: float



class Box:
    Min: Vector
    Max: Vector
    IsValid: int



class Box2D:
    Min: Vector2D
    Max: Vector2D
    bIsValid: int



class BoxSphereBounds:
    Origin: Vector
    BoxExtent: Vector
    SphereRadius: float



class OrientedBox:
    Center: Vector
    AxisX: Vector
    AxisY: Vector
    AxisZ: Vector
    ExtentX: float
    ExtentY: float
    ExtentZ: float



class Matrix:
    XPlane: Plane
    YPlane: Plane
    ZPlane: Plane
    WPlane: Plane



class InterpCurvePointFloat:
    InVal: float
    OutVal: float
    ArriveTangent: float
    LeaveTangent: float
    InterpMode: int



class InterpCurveFloat:
    Points: unreal.WrappedArray[InterpCurvePointFloat]
    bIsLooped: bool
    LoopKeyOffset: float



class InterpCurvePointVector2D:
    InVal: float
    OutVal: Vector2D
    ArriveTangent: Vector2D
    LeaveTangent: Vector2D
    InterpMode: int



class InterpCurveVector2D:
    Points: unreal.WrappedArray[InterpCurvePointVector2D]
    bIsLooped: bool
    LoopKeyOffset: float



class InterpCurvePointVector:
    InVal: float
    OutVal: Vector
    ArriveTangent: Vector
    LeaveTangent: Vector
    InterpMode: int



class InterpCurveVector:
    Points: unreal.WrappedArray[InterpCurvePointVector]
    bIsLooped: bool
    LoopKeyOffset: float



class InterpCurvePointQuat:
    InVal: float
    OutVal: Quat
    ArriveTangent: Quat
    LeaveTangent: Quat
    InterpMode: int



class InterpCurveQuat:
    Points: unreal.WrappedArray[InterpCurvePointQuat]
    bIsLooped: bool
    LoopKeyOffset: float



class InterpCurvePointTwoVectors:
    InVal: float
    OutVal: TwoVectors
    ArriveTangent: TwoVectors
    LeaveTangent: TwoVectors
    InterpMode: int



class InterpCurveTwoVectors:
    Points: unreal.WrappedArray[InterpCurvePointTwoVectors]
    bIsLooped: bool
    LoopKeyOffset: float



class InterpCurvePointLinearColor:
    InVal: float
    OutVal: LinearColor
    ArriveTangent: LinearColor
    LeaveTangent: LinearColor
    InterpMode: int



class InterpCurveLinearColor:
    Points: unreal.WrappedArray[InterpCurvePointLinearColor]
    bIsLooped: bool
    LoopKeyOffset: float



class Transform:
    Rotation: Quat
    Translation: Vector
    Scale3D: Vector



class RandomStream:
    InitialSeed: int
    Seed: int



class DateTime: ...


class FrameNumber:
    Value: int



class FrameRate:
    Numerator: int
    Denominator: int



class FrameTime:
    FrameNumber: FrameNumber
    SubFrame: float



class QualifiedFrameTime:
    Time: FrameTime
    Rate: FrameRate



class Timecode:
    Hours: int
    Minutes: int
    Seconds: int
    Frames: int
    bDropFrameFormat: bool



class Timespan: ...


class SoftObjectPath:
    AssetPathName: str
    SubPathString: str



class SoftClassPath(SoftObjectPath): ...


class PrimaryAssetType:
    Name: str



class PrimaryAssetId:
    PrimaryAssetType: PrimaryAssetType
    PrimaryAssetName: str



class FallbackStruct: ...


class FloatRangeBound:
    Type: int
    Value: float



class FloatRange:
    LowerBound: FloatRangeBound
    UpperBound: FloatRangeBound



class Int32RangeBound:
    Type: int
    Value: int



class Int32Range:
    LowerBound: Int32RangeBound
    UpperBound: Int32RangeBound



class FloatInterval:
    Min: float
    Max: float



class Int32Interval:
    Min: int
    Max: int



class PolyglotTextData:
    Category: ELocalizedTextSourceCategory
    NativeCulture: str
    Namespace: str
    Key: str
    NativeString: str
    CachedText: str



class AutomationEvent:
    Type: EAutomationEventType
    MESSAGE: str
    Context: str
    Artifact: Guid



class AutomationExecutionEntry:
    Event: AutomationEvent
    Filename: str
    LineNumber: int
    Timestamp: DateTime



class Default__Class: ...


class Default__DynamicClass: ...


class Default__LinkerPlaceholderClass: ...


class Default__Enum(enum.Enum): ...


class EInterpCurveMode(enum.Enum):
    CIM_CurveBreak = 0
    CIM_CurveAuto = 1
    CIM_Constant = 2


class ERangeBoundTypes(enum.Enum):
    Open = 0
    Inclusive = 1


class ELocalizedTextSourceCategory(enum.Enum):
    Engine = 0
    Editor = 1


class EAutomationEventType(enum.Enum):
    Warning = 0
    Error = 1


class EMouseCursor(enum.Enum):
    Default = 0
    TextEditBeam = 1
    ResizeUpDown = 2
    Crosshairs = 3


class EAxis(enum.Enum):
    X = 0
    EAxis_MAX = 1
    Y = 2


class ELifetimeCondition(enum.Enum):
    COND_InitialOnly = 0
    COND_OwnerOnly = 1
    COND_SimulatedOnly = 2
    COND_Custom = 3


class EUnit(enum.Enum):
    Miles = 0
    Millimeters = 1
    Centimeters = 2
    Kilometers = 3
    Farenheit = 4
    Gigahertz = 5


class EPixelFormat(enum.Enum):
    PF_A32B32G32R32F = 0
    PF_R16_UINT = 1
    PF_G16 = 2
    PF_B8G8R8A8 = 3
    PF_UYVY = 4
    PF_G16R16F_FILTER = 5


class ELogTimes(enum.Enum):
    UTC = 0
    SinceGStartTime = 1
    ELogTimes_MAX = 2


class ESearchDir(enum.Enum):
    ESearchDir_MAX = 0
    FromEnd = 1


class ESearchCase(enum.Enum):
    IgnoreCase = 0
    ESearchCase_MAX = 1

from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine



class GbxDataAsset(engine.DataAsset): ...


class GbxCondition(unreal.UObject):
    bInvertCondition: bool
    RefreshRate: EConditionRefreshRate
    def K2_EvaluateConditionType(self, Condition: unreal.UClass, Context: unreal.UObject, ReturnValue: bool) -> bool: ...
    def K2_EvaluateCondition(self, Condition: GbxCondition, Context: unreal.UObject, ReturnValue: bool) -> bool: ...


class GbxDataAssetBlueprintable(GbxDataAsset): ...


class NumericRangeExt(engine.BlueprintFunctionLibrary):

    def ToValueVarianceString(self, Range: NumericRange, ReturnValue: str) -> str: ...
    def ToValueString(self, Range: NumericRange, ReturnValue: str) -> str: ...
    def ToString(self, Range: NumericRange, ReturnValue: str) -> str: ...
    def ToMinMaxString(self, Range: NumericRange, ReturnValue: str) -> str: ...
    def SetMinimum(self, Range: NumericRange, Minimum: float): ...
    def SetMaximum(self, Range: NumericRange, Maximum: float): ...
    def IsWithin(self, Range: NumericRange, Value: float, ReturnValue: bool) -> bool: ...
    def GetMinimum(self, Range: NumericRange, ReturnValue: float) -> float: ...
    def GetMaximum(self, Range: NumericRange, ReturnValue: float) -> float: ...
    def GenerateRandomNumber(self, Range: NumericRange, ReturnValue: float) -> float: ...
    def CreateNumericRangeMinMax(self, Minimum: float, Maximum: float, ReturnValue: NumericRange) -> NumericRange: ...
    def CreateNumericRange(self, Value: float, Variance: float, ReturnValue: NumericRange) -> NumericRange: ...


class RenderActor(engine.Actor): ...


class NumericRange:
    Value: float
    Variance: float



class GbxStructPtrParam: ...


class GbxTriggerProperty: ...


class SceneBasedPosition:
    Base: engine.SceneComponent
    Position: core_uobject.Vector
    CachedBaseLocation: core_uobject.Vector
    CachedBaseRotation: core_uobject.Rotator
    CachedTransPosition: core_uobject.Vector



class EConditionRefreshRate(enum.Enum):
    TwicePerSecond = 0
    OncePerSecond = 1
    Immediately = 2


class ENumericRangeEditMode(enum.Enum):
    ValueVariance = 0
    ENumericRangeEditMode_MAX = 1
    Variance = 2
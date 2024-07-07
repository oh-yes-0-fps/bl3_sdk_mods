from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine
from . import gbx_game_system_core
from . import anim_graph_runtime



class AnimNotify_Delegate(engine.AnimNotify): ...


class AnimNotify_GbxCustomEvent(engine.AnimNotify):
    EventName: str
    EventContext: EGbxCustomEventContext
    bRunOnServer: bool
    bRunOnClient: bool
    bRunIfLocalPlayer: bool
    bTriggerOnFirstPersonMesh: bool



class AnimNotify_GbxClosedCaptionEvent(AnimNotify_GbxCustomEvent):
    ClosedCaption: str



class AnimNotify_ToggleClothEnvironmentCollision(engine.AnimNotify):
    bEnable: bool



class GbxAnimNode_AnimTable(engine.AnimNode_AssetPlayerBase):
    AnimTable: gbx_game_system_core.GbxAnimTable
    Sequence: engine.AnimSequenceBase
    GbxAnimInstance: gbx_game_system_core.GbxAnimInstance
    bScaleRateByMeshScale: bool



class GbxAnimNode_BlendListByFloatComparison(anim_graph_runtime.AnimNode_BlendListBase):
    ValueA: float
    ValueB: float
    Comparison: EFloatComparisonType



class GbxAnimNode_BlendListByFloatInRange(anim_graph_runtime.AnimNode_BlendListBase):
    BlendValue: float
    MinMaxRanges: unreal.WrappedArray[FloatMinMaxRange]
    CurrentRangeIndex: int



class FloatMinMaxRange:
    MinValue: float
    MaxValue: float



class GbxAnimNode_BlendListByIntInRange(anim_graph_runtime.AnimNode_BlendListBase):
    BlendValue: int
    MinMaxRanges: unreal.WrappedArray[IntMinMaxRange]
    CurrentRangeIndex: int



class IntMinMaxRange:
    MinValue: int
    MaxValue: int



class GbxAnimNode_BlendTwoPosesPerBone(engine.AnimNode_Base):
    PoseA: engine.PoseLink
    PoseB: engine.PoseLink
    CachedBlendWeights: unreal.WrappedArray[float]
    DynamicCachedBlendWeights: unreal.WrappedArray[float]
    BoneWeightCurveOverrides: unreal.WrappedArray[BoneWeightCurveOverride]
    GbxAnimInstance: gbx_game_system_core.GbxAnimInstance
    SkeletonGuid: core_uobject.Guid
    VirtualBoneGuid: core_uobject.Guid
    BoneSet: engine.GbxBoneSet
    BoneSetGuid: core_uobject.Guid
    ActionSlotName: str



class BoneWeightCurveOverride:
    CurveOverrideType: engine.ECurveOverrideType
    NormalizeCurveOverrideData: engine.NormalizeCurvesOverride
    SingleOverrideCurveName: str
    CacheWeightIndicesToUpdate: unreal.WrappedArray[int]



class GbxAnimNode_CopyParentTransforms(engine.AnimNode_Base): ...


class GbxAnimNode_HandIK(anim_graph_runtime.AnimNode_TwoBoneIK):
    ObjectBone: engine.BoneReference
    ObjectOffset: core_uobject.Transform
    WorldOffset: core_uobject.Transform
    HandOffsetToIkWorld: core_uobject.Transform
    bWorldIkOverride: bool
    EffectorAlignmentBone: engine.BoneReference
    AlignToObjectAlpha: float



class GbxAnimNode_ModifyBoneList(anim_graph_runtime.AnimNode_SkeletalControlBase):
    BonesToModify: unreal.WrappedArray[engine.BoneReference]
    TranslationMode: int
    RotationMode: int
    ScaleMode: int
    TranslationSpace: int
    RotationSpace: int
    ScaleSpace: int
    InputTransforms: InputTransforms



class InputTransforms:
    Transforms: unreal.WrappedArray[core_uobject.Transform]



class GbxAnimNode_Print(engine.AnimNode_Base):
    Source: engine.PoseLink
    inString: str
    bPrintToLog: bool
    bPrintToScreen: bool
    TextColor: core_uobject.LinearColor
    Duration: float



class GbxAnimNode_Spin(anim_graph_runtime.AnimNode_SkeletalControlBase):
    BoneToModify: engine.BoneReference
    RotationAmount: core_uobject.Rotator
    RotationSpace: int



class EGbxCustomEventContext(enum.Enum):
    Instigator = 0
    EGbxCustomEventContext_MAX = 1


class EFloatComparisonType(enum.Enum):
    GreaterThan = 0
    NotEqual = 1
    LessThan = 2


class EWeightTypeToUse(enum.Enum):
    Cached = 0
    One = 1
    EWeightTypeToUse_MAX = 2

from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import engine



class ACLStatsDumpCommandlet(engine.Commandlet): ...


class AnimCompress_ACLBase(engine.AnimCompress): ...


class AnimCompress_ACL(AnimCompress_ACLBase):
    DefaultVirtualVertexDistance: float
    SafeVirtualVertexDistance: float
    SafetyFallbackThreshold: float
    ErrorThreshold: float
    BoneToIgnores: unreal.WrappedArray[str]



class AnimCompress_ACLCustom(AnimCompress_ACLBase):
    DefaultVirtualVertexDistance: float
    SafeVirtualVertexDistance: float
    RotationFormat: int
    TranslationFormat: int
    ScaleFormat: int
    ErrorThreshold: float
    ConstantRotationThresholdAngle: float
    ConstantTranslationThreshold: float
    ConstantScaleThreshold: float
    bClipRangeReduceRotations: bool
    bClipRangeReduceTranslations: bool
    bClipRangeReduceScales: bool
    bEnableSegmenting: bool
    bSegmentRangeReduceRotations: bool
    bSegmentRangeReduceTranslations: bool
    bSegmentRangeReduceScales: bool



class ACLVectorFormat(enum.Enum):
    ACLVF_Vector3_Variable = 0
    ACLVF_Vector3_MAX = 1


class ACLRotationFormat(enum.Enum):
    ACLRF_QuatDropW_96 = 0
    ACLRF_QuatDropW_Variable = 1

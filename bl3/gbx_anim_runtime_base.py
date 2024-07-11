from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import gbx_runtime
from . import anim_graph_runtime


class GbxAnimNode_LegIK(anim_graph_runtime.AnimNode_LegIK):
    FootIKTraceUpScale: float
    FootIKTraceDownScale: float
    FootIKOffsetInterpSpeed: float
    FootIKTargetOffset: core_uobject.Vector
    FootIKLODThreshold: int
    FootIkTraceScreenSizeThreshold: anim_graph_runtime.ScreenSizeSelection
    bUseFootIkTraceScreenSizeThreshold: bool
    MeshOffsetCharacterSpeedRange: gbx_runtime.NumericRange
    MeshIKOffsetInterpSpeed: float
    bShouldLimitFootDistanceToMeshOffset: bool
    SlopeAdaptation: core_uobject.Vector
    SlopeAdaptationBone: engine.BoneReference
    MaxSlopeAngle: float
    SlopeNormalMinInterpSpeed: float
    SlopeNormalMaxInterpSpeed: float
    SlopeNormalCharacterSpeedRange: gbx_runtime.NumericRange
    MinVelocity: float
    MaxVelocity: float


class GbxAnimNode_LookAt(anim_graph_runtime.AnimNode_SkeletalControlBase):
    BoneToModify: engine.BoneReference
    ParentBoneToModify: engine.BoneReference
    ParentLookAxis: int
    BonesToModify: unreal.WrappedArray[BoneBlendParams]
    EyeBonesToModify: unreal.WrappedArray[BoneBlendParams]
    HeadLookAtLocation: core_uobject.Vector
    EyeLookAtLocation: core_uobject.Vector
    HeadLookPercentage: float
    bEnableDebug: bool
    bUseEyeMovement: bool
    EyeShiftMin: core_uobject.Rotator
    EyeShiftMax: core_uobject.Rotator
    EyeGlanceMin: core_uobject.Rotator
    EyeGlanceMax: core_uobject.Rotator
    EyeFocusTimeMin: float
    EyeFocusTimeMax: float
    EyeGlanceTimeMin: float
    EyeGlanceTimeMax: float
    EyeShiftTimeMin: float
    EyeShiftTimeMax: float
    EyeLODThreshold: int
    EyeScreenSizeThreshold: anim_graph_runtime.ScreenSizeSelection
    bUseEyeScreenSizeThreshold: bool
    ReferencePoseLink: engine.PoseLink


class BoneBlendParams:
    Bone: engine.BoneReference
    Weight: float
    YawWeight: float
    PitchWeight: float
    YawClamp: gbx_runtime.NumericRange
    PitchClamp: gbx_runtime.NumericRange
    RotationOffset: core_uobject.Rotator
    bUseRotationOffset: bool
    LookAtClamp: float
    LookAxis: int
    UpAxis: int


class EGbxLookAxisOption(enum.Enum):
    Y = 0
    Y_Neg = 1
    Z = 2

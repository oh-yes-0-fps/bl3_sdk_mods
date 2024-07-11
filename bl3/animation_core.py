from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject


class AXIS:
    AXIS: core_uobject.Vector
    bInLocalSpace: bool


class ConstraintData:
    Constraint: ConstraintDescriptor
    Weight: float
    bMaintainOffset: bool
    Offset: core_uobject.Transform
    CurrentTransform: core_uobject.Transform


class ConstraintDescriptor:
    Type: EConstraintType


class ConstraintDescriptionEx:
    AxesFilterOption: FilterOptionPerAxis


class FilterOptionPerAxis:
    bX: bool
    bY: bool
    bZ: bool


class AimConstraintDescription(ConstraintDescriptionEx):
    LookAt_Axis: AXIS
    LookUp_Axis: AXIS
    bUseLookUp: bool
    LookUpTarget: core_uobject.Vector


class TransformConstraintDescription(ConstraintDescriptionEx):
    TransformType: ETransformConstraintType


class TransformConstraint:
    Operator: ConstraintDescription
    SourceNode: str
    TargetNode: str
    Weight: float
    bMaintainOffset: bool


class ConstraintDescription:
    bTranslation: bool
    bRotation: bool
    bScale: bool
    bParent: bool
    TranslationAxes: FilterOptionPerAxis
    RotationAxes: FilterOptionPerAxis
    ScaleAxes: FilterOptionPerAxis


class ConstraintOffset:
    Translation: core_uobject.Vector
    Rotation: core_uobject.Quat
    Scale: core_uobject.Vector
    Parent: core_uobject.Transform


class TransformFilter:
    TranslationFilter: FilterOptionPerAxis
    RotationFilter: FilterOptionPerAxis
    ScaleFilter: FilterOptionPerAxis


class EulerTransform:
    Location: core_uobject.Vector
    Rotation: core_uobject.Rotator
    Scale: core_uobject.Vector


class NodeChain:
    Nodes: unreal.WrappedArray[str]


class NodeHierarchyWithUserData:
    Hierarchy: NodeHierarchyData


class NodeHierarchyData:
    Nodes: unreal.WrappedArray[NodeObject]
    Transforms: unreal.WrappedArray[core_uobject.Transform]
    NodeNameToIndexMapping: Any


class NodeObject:
    Name: str
    ParentName: str


class ETransformConstraintType(enum.Enum):
    Rotation = 0
    Scale = 1
    ETransformConstraintType_MAX = 2


class EConstraintType(enum.Enum):
    Aim = 0
    MAX = 1

from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import anim_graph_runtime


class AnimNode_RigidBody(anim_graph_runtime.AnimNode_SkeletalControlBase):
    OverridePhysicsAsset: engine.PhysicsAsset
    OverrideWorldGravity: core_uobject.Vector
    ExternalForce: core_uobject.Vector
    ComponentLinearAccScale: core_uobject.Vector
    ComponentLinearVelScale: core_uobject.Vector
    ComponentAppliedLinearAccClamp: core_uobject.Vector
    OverlapChannel: int
    bEnableWorldGeometry: bool
    SimulationSpace: ESimulationSpace
    BaseBoneRef: engine.BoneReference
    bOverrideWorldGravity: bool
    CachedBoundsScale: float
    bTransferBoneVelocities: bool
    bFreezeIncomingPoseOnStart: bool
    bComponentSpaceSimulation: bool


class ESimulationSpace(enum.Enum):
    WorldSpace = 0
    BaseBoneSpace = 1

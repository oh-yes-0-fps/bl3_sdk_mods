from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine


class CableActor(engine.Actor):
    CableComponent: CableComponent


class CableComponent(engine.MeshComponent):
    bAttachStart: bool
    bAttachEnd: bool
    AttachEndTo: engine.ComponentReference
    AttachEndToSocketName: str
    EndLocation: core_uobject.Vector
    CableLength: float
    NumSegments: int
    SubstepTime: float
    SolverIterations: int
    bEnableStiffness: bool
    bEnableCollision: bool
    bAlwaysSimulate: bool
    CollisionFriction: float
    CableForce: core_uobject.Vector
    CableGravityScale: float
    CableWidth: float
    NumSides: int
    TileMaterial: float
    SavedCablePoints: unreal.WrappedArray[core_uobject.Vector]

    def SetAttachEndTo(
        self, Actor: engine.Actor, ComponentProperty: str, SocketName: str
    ): ...
    def GetTransformAtRatio(
        self, Ratio: float, RefUp: core_uobject.Vector
    ) -> core_uobject.Transform: ...
    def GetTransformAtDistance(
        self, Distance: float, RefUp: core_uobject.Vector, bOutIsAtEnd: bool
    ) -> core_uobject.Transform: ...
    def GetSimulatedCableLength(self) -> float: ...
    def GetCableParticleLocations(
        self, Locations: unreal.WrappedArray[core_uobject.Vector]
    ): ...
    def GetAttachedComponent(self) -> engine.SceneComponent: ...
    def GetAttachedActor(self) -> engine.Actor: ...


class FollowCableMovementComponent(engine.MovementComponent):
    MovementMode: EFollowCableMovementMode
    StartingDistance: float
    MovementSpeed: float
    CableComponentHolder: engine.Actor
    CableComponentName: str
    bStartEnabled: bool
    bCollideOnMovement: bool
    bUpdateRotation: bool
    RotationOffset: core_uobject.Rotator
    CableComponentToFollow: CableComponent

    def EnableMovement(self, bEnable: bool, bResetPosition: bool): ...


class EFollowCableMovementMode(enum.Enum):
    PingPong = 0
    Loop = 1

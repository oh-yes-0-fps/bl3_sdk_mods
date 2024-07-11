from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject


class ClothingAssetBase(unreal.UObject):
    ImportedFilePath: str
    AssetGuid: core_uobject.Guid


class ClothingSimulationFactory(unreal.UObject): ...


class ClothingSimulationInteractor(unreal.UObject):

    def PhysicsAssetUpdated(self): ...
    def ClothConfigUpdated(self): ...


class ClothCollisionData:
    Spheres: unreal.WrappedArray[ClothCollisionPrim_Sphere]
    SphereConnections: unreal.WrappedArray[ClothCollisionPrim_SphereConnection]
    Convexes: unreal.WrappedArray[ClothCollisionPrim_Convex]


class ClothCollisionPrim_Convex:
    Planes: unreal.WrappedArray[core_uobject.Plane]
    BoneIndex: int


class ClothCollisionPrim_SphereConnection:
    SphereIndices: int


class ClothCollisionPrim_Sphere:
    BoneIndex: int
    Radius: float
    LocalPosition: core_uobject.Vector

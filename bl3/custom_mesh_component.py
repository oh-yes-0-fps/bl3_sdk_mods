from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine


class CustomMeshComponent(engine.MeshComponent):

    def SetCustomMeshTriangles(
        self, Triangles: unreal.WrappedArray[CustomMeshTriangle]
    ) -> bool: ...
    def ClearCustomMeshTriangles(self): ...
    def AddCustomMeshTriangles(
        self, Triangles: unreal.WrappedArray[CustomMeshTriangle]
    ): ...


class CustomMeshTriangle:
    Vertex1: core_uobject.Vector
    Vertex2: core_uobject.Vector

from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine


class KismetProceduralMeshLibrary(engine.BlueprintFunctionLibrary):

    def SliceProceduralMesh(
        self,
        InProcMesh: ProceduralMeshComponent,
        PlanePosition: core_uobject.Vector,
        PlaneNormal: core_uobject.Vector,
        bCreateOtherHalf: bool,
        OutOtherHalfProcMesh: ProceduralMeshComponent,
        CapOption: EProcMeshSliceCapOption,
        CapMaterial: engine.MaterialInterface,
    ): ...
    def GetSectionFromStaticMesh(
        self,
        InMesh: engine.StaticMesh,
        LODIndex: int,
        SectionIndex: int,
        Vertices: unreal.WrappedArray[core_uobject.Vector],
        Triangles: unreal.WrappedArray[int],
        Normals: unreal.WrappedArray[core_uobject.Vector],
        UVs: unreal.WrappedArray[core_uobject.Vector2D],
        Tangents: unreal.WrappedArray[ProcMeshTangent],
    ): ...
    def GetSectionFromProceduralMesh(
        self,
        InProcMesh: ProceduralMeshComponent,
        SectionIndex: int,
        Vertices: unreal.WrappedArray[core_uobject.Vector],
        Triangles: unreal.WrappedArray[int],
        Normals: unreal.WrappedArray[core_uobject.Vector],
        UVs: unreal.WrappedArray[core_uobject.Vector2D],
        Tangents: unreal.WrappedArray[ProcMeshTangent],
    ): ...
    def GenerateBoxMesh(
        self,
        BoxRadius: core_uobject.Vector,
        Vertices: unreal.WrappedArray[core_uobject.Vector],
        Triangles: unreal.WrappedArray[int],
        Normals: unreal.WrappedArray[core_uobject.Vector],
        UVs: unreal.WrappedArray[core_uobject.Vector2D],
        Tangents: unreal.WrappedArray[ProcMeshTangent],
    ): ...
    def CreateGridMeshTriangles(
        self, NumX: int, NumY: int, bWinding: bool, Triangles: unreal.WrappedArray[int]
    ): ...
    def CopyProceduralMeshFromStaticMeshComponent(
        self,
        StaticMeshComponent: engine.StaticMeshComponent,
        LODIndex: int,
        ProcMeshComponent: ProceduralMeshComponent,
        bCreateCollision: bool,
    ): ...
    def CalculateTangentsForMesh(
        self,
        Vertices: unreal.WrappedArray[core_uobject.Vector],
        Triangles: unreal.WrappedArray[int],
        UVs: unreal.WrappedArray[core_uobject.Vector2D],
        Normals: unreal.WrappedArray[core_uobject.Vector],
        Tangents: unreal.WrappedArray[ProcMeshTangent],
    ): ...


class ProceduralMeshComponent(engine.MeshComponent):
    bUseComplexAsSimpleCollision: bool
    bUseAsyncCooking: bool
    ProcMeshBodySetup: engine.BodySetup
    ProcMeshSections: unreal.WrappedArray[ProcMeshSection]
    CollisionConvexElems: unreal.WrappedArray[engine.KConvexElem]
    LocalBounds: core_uobject.BoxSphereBounds
    AsyncBodySetupQueue: unreal.WrappedArray[engine.BodySetup]

    def SetMeshSectionVisible(self, SectionIndex: int, bNewVisibility: bool): ...
    def IsMeshSectionVisible(self, SectionIndex: int) -> bool: ...
    def GetNumSections(self) -> int: ...
    def ClearMeshSection(self, SectionIndex: int): ...
    def ClearCollisionConvexMeshes(self): ...
    def ClearAllMeshSections(self): ...
    def AddCollisionConvexMesh(
        self, ConvexVerts: unreal.WrappedArray[core_uobject.Vector]
    ): ...


class ProcMeshSection:
    ProcVertexBuffer: unreal.WrappedArray[ProcMeshVertex]
    ProcIndexBuffer: unreal.WrappedArray[int]
    SectionLocalBox: core_uobject.Box
    bEnableCollision: bool
    bSectionVisible: bool


class ProcMeshVertex:
    Position: core_uobject.Vector
    Normal: core_uobject.Vector
    Tangent: ProcMeshTangent
    Color: core_uobject.Color
    UV1: core_uobject.Vector2D
    UV2: core_uobject.Vector2D
    UV3: core_uobject.Vector2D


class ProcMeshTangent:
    TangentX: core_uobject.Vector
    bFlipTangentY: bool


class EProcMeshSliceCapOption(enum.Enum):
    CreateNewSectionForCap = 0
    UseLastSectionForCap = 1

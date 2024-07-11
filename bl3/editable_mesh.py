from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import mesh_description


class EditableMesh(unreal.UObject):
    Adapters: unreal.WrappedArray[EditableMeshAdapter]
    TextureCoordinateCount: int
    PendingCompactCounter: int
    SubdivisionCount: int

    def WeldVertices(
        self,
        VertexIDs: unreal.WrappedArray[mesh_description.VertexID],
        OutNewVertexID: mesh_description.VertexID,
    ): ...
    def TryToRemoveVertex(
        self,
        VertexID: mesh_description.VertexID,
        bOutWasVertexRemoved: bool,
        OutNewEdgeID: mesh_description.EdgeID,
    ): ...
    def TryToRemovePolygonEdge(
        self,
        EdgeID: mesh_description.EdgeID,
        bOutWasEdgeRemoved: bool,
        OutNewPolygonID: mesh_description.PolygonID,
    ): ...
    def TriangulatePolygons(
        self,
        PolygonIDs: unreal.WrappedArray[mesh_description.PolygonID],
        OutNewTrianglePolygons: unreal.WrappedArray[mesh_description.PolygonID],
    ): ...
    def TessellatePolygons(
        self,
        PolygonIDs: unreal.WrappedArray[mesh_description.PolygonID],
        TriangleTessellationMode: ETriangleTessellationMode,
        OutNewPolygonIDs: unreal.WrappedArray[mesh_description.PolygonID],
    ): ...
    def StartModification(
        self,
        MeshModificationType: EMeshModificationType,
        MeshTopologyChange: EMeshTopologyChange,
    ): ...
    def SplitPolygons(
        self,
        PolygonsToSplit: unreal.WrappedArray[PolygonToSplit],
        OutNewEdgeIDs: unreal.WrappedArray[mesh_description.EdgeID],
    ): ...
    def SplitEdge(
        self,
        EdgeID: mesh_description.EdgeID,
        Splits: unreal.WrappedArray[float],
        OutNewVertexIDs: unreal.WrappedArray[mesh_description.VertexID],
    ): ...
    def SetVerticesCornerSharpness(
        self,
        VertexIDs: unreal.WrappedArray[mesh_description.VertexID],
        VerticesNewCornerSharpness: unreal.WrappedArray[float],
    ): ...
    def SetVerticesAttributes(
        self, AttributesForVertices: unreal.WrappedArray[AttributesForVertex]
    ): ...
    def SetVertexInstancesAttributes(
        self,
        AttributesForVertexInstances: unreal.WrappedArray[AttributesForVertexInstance],
    ): ...
    def SetTextureCoordinateCount(self, NumTexCoords: int): ...
    def SetSubdivisionCount(self, NewSubdivisionCount: int): ...
    def SetPolygonsVertexAttributes(
        self,
        VertexAttributesForPolygons: unreal.WrappedArray[VertexAttributesForPolygon],
    ): ...
    def SetEdgesVertices(
        self, VerticesForEdges: unreal.WrappedArray[VerticesForEdge]
    ): ...
    def SetEdgesHardnessAutomatically(
        self,
        EdgeIDs: unreal.WrappedArray[mesh_description.EdgeID],
        MaxDotProductForSoftEdge: float,
    ): ...
    def SetEdgesHardness(
        self,
        EdgeIDs: unreal.WrappedArray[mesh_description.EdgeID],
        EdgesNewIsHard: unreal.WrappedArray[bool],
    ): ...
    def SetEdgesCreaseSharpness(
        self,
        EdgeIDs: unreal.WrappedArray[mesh_description.EdgeID],
        EdgesNewCreaseSharpness: unreal.WrappedArray[float],
    ): ...
    def SetEdgesAttributes(
        self, AttributesForEdges: unreal.WrappedArray[AttributesForEdge]
    ): ...
    def SetAllowUndo(self, bInAllowUndo: bool): ...
    def SetAllowSpatialDatabase(self, bInAllowSpatialDatabase: bool): ...
    def SetAllowCompact(self, bInAllowCompact: bool): ...
    def SearchSpatialDatabaseForPolygonsPotentiallyIntersectingLineSegment(
        self,
        LineSegmentStart: core_uobject.Vector,
        LineSegmentEnd: core_uobject.Vector,
        OutPolygons: unreal.WrappedArray[mesh_description.PolygonID],
    ): ...
    def RevertInstance(self) -> EditableMesh: ...
    def Revert(self): ...
    def RemovePolygonPerimeterVertices(
        self,
        PolygonID: mesh_description.PolygonID,
        FirstVertexNumberToRemove: int,
        NumVerticesToRemove: int,
        bDeleteOrphanedVertexInstances: bool,
    ): ...
    def RebuildRenderMesh(self): ...
    def QuadrangulateMesh(
        self, OutNewPolygonIDs: unreal.WrappedArray[mesh_description.PolygonID]
    ): ...
    def PropagateInstanceChanges(self): ...
    def MoveVertices(self, VerticesToMove: unreal.WrappedArray[VertexToMove]): ...
    def MakeVertexID(self, VertexIndex: int) -> mesh_description.VertexID: ...
    def MakePolygonID(self, PolygonIndex: int) -> mesh_description.PolygonID: ...
    def MakePolygonGroupID(
        self, PolygonGroupIndex: int
    ) -> mesh_description.PolygonGroupID: ...
    def MakeEdgeID(self, EdgeIndex: int) -> mesh_description.EdgeID: ...
    def IsValidVertex(self, VertexID: mesh_description.VertexID) -> bool: ...
    def IsValidPolygonGroup(
        self, PolygonGroupID: mesh_description.PolygonGroupID
    ) -> bool: ...
    def IsValidPolygon(self, PolygonID: mesh_description.PolygonID) -> bool: ...
    def IsValidEdge(self, EdgeID: mesh_description.EdgeID) -> bool: ...
    def IsUndoAllowed(self) -> bool: ...
    def IsSpatialDatabaseAllowed(self) -> bool: ...
    def IsPreviewingSubdivisions(self) -> bool: ...
    def IsOrphanedVertex(self, VertexID: mesh_description.VertexID) -> bool: ...
    def IsCompactAllowed(self) -> bool: ...
    def IsCommittedAsInstance(self) -> bool: ...
    def IsCommitted(self) -> bool: ...
    def IsBeingModified(self) -> bool: ...
    def InvalidVertexID(self) -> mesh_description.VertexID: ...
    def InvalidPolygonID(self) -> mesh_description.PolygonID: ...
    def InvalidPolygonGroupID(self) -> mesh_description.PolygonGroupID: ...
    def InvalidEdgeID(self) -> mesh_description.EdgeID: ...
    def InsetPolygons(
        self,
        PolygonIDs: unreal.WrappedArray[mesh_description.PolygonID],
        InsetFixedDistance: float,
        InsetProgressTowardCenter: float,
        Mode: EInsetPolygonsMode,
        OutNewCenterPolygonIDs: unreal.WrappedArray[mesh_description.PolygonID],
        OutNewSidePolygonIDs: unreal.WrappedArray[mesh_description.PolygonID],
    ): ...
    def InsertPolygonPerimeterVertices(
        self,
        PolygonID: mesh_description.PolygonID,
        InsertBeforeVertexNumber: int,
        VerticesToInsert: unreal.WrappedArray[VertexAndAttributes],
    ): ...
    def InsertEdgeLoop(
        self,
        EdgeID: mesh_description.EdgeID,
        Splits: unreal.WrappedArray[float],
        OutNewEdgeIDs: unreal.WrappedArray[mesh_description.EdgeID],
    ): ...
    def InitializeAdapters(self): ...
    def GetVertexPairEdge(
        self,
        VertexID: mesh_description.VertexID,
        NextVertexID: mesh_description.VertexID,
        bOutEdgeWindingIsReversed: bool,
    ) -> mesh_description.EdgeID: ...
    def GetVertexInstanceVertex(
        self, VertexInstanceID: mesh_description.VertexInstanceID
    ) -> mesh_description.VertexID: ...
    def GetVertexInstanceCount(self) -> int: ...
    def GetVertexInstanceConnectedPolygons(
        self,
        VertexInstanceID: mesh_description.VertexInstanceID,
        OutConnectedPolygonIDs: unreal.WrappedArray[mesh_description.PolygonID],
    ): ...
    def GetVertexInstanceConnectedPolygonCount(
        self, VertexInstanceID: mesh_description.VertexInstanceID
    ) -> int: ...
    def GetVertexInstanceConnectedPolygon(
        self,
        VertexInstanceID: mesh_description.VertexInstanceID,
        ConnectedPolygonNumber: int,
    ) -> mesh_description.PolygonID: ...
    def GetVertexCount(self) -> int: ...
    def GetVertexConnectedPolygons(
        self,
        VertexID: mesh_description.VertexID,
        OutConnectedPolygonIDs: unreal.WrappedArray[mesh_description.PolygonID],
    ): ...
    def GetVertexConnectedEdges(
        self,
        VertexID: mesh_description.VertexID,
        OutConnectedEdgeIDs: unreal.WrappedArray[mesh_description.EdgeID],
    ): ...
    def GetVertexConnectedEdgeCount(
        self, VertexID: mesh_description.VertexID
    ) -> int: ...
    def GetVertexConnectedEdge(
        self, VertexID: mesh_description.VertexID, ConnectedEdgeNumber: int
    ) -> mesh_description.EdgeID: ...
    def GetVertexAdjacentVertices(
        self,
        VertexID: mesh_description.VertexID,
        OutAdjacentVertexIDs: unreal.WrappedArray[mesh_description.VertexID],
    ): ...
    def GetTextureCoordinateCount(self) -> int: ...
    def GetSubdivisionLimitData(self) -> SubdivisionLimitData: ...
    def GetSubdivisionCount(self) -> int: ...
    def GetPolygonTriangulatedTriangleCount(
        self, PolygonID: mesh_description.PolygonID
    ) -> int: ...
    def GetPolygonTriangulatedTriangle(
        self, PolygonID: mesh_description.PolygonID, PolygonTriangleNumber: int
    ) -> mesh_description.MeshTriangle: ...
    def GetPolygonPerimeterVertices(
        self,
        PolygonID: mesh_description.PolygonID,
        OutPolygonPerimeterVertexIDs: unreal.WrappedArray[mesh_description.VertexID],
    ): ...
    def GetPolygonPerimeterVertexInstances(
        self,
        PolygonID: mesh_description.PolygonID,
        OutPolygonPerimeterVertexInstanceIDs: unreal.WrappedArray[
            mesh_description.VertexInstanceID
        ],
    ): ...
    def GetPolygonPerimeterVertexInstance(
        self, PolygonID: mesh_description.PolygonID, PolygonVertexNumber: int
    ) -> mesh_description.VertexInstanceID: ...
    def GetPolygonPerimeterVertexCount(
        self, PolygonID: mesh_description.PolygonID
    ) -> int: ...
    def GetPolygonPerimeterVertex(
        self, PolygonID: mesh_description.PolygonID, PolygonVertexNumber: int
    ) -> mesh_description.VertexID: ...
    def GetPolygonPerimeterEdges(
        self,
        PolygonID: mesh_description.PolygonID,
        OutPolygonPerimeterEdgeIDs: unreal.WrappedArray[mesh_description.EdgeID],
    ): ...
    def GetPolygonPerimeterEdgeCount(
        self, PolygonID: mesh_description.PolygonID
    ) -> int: ...
    def GetPolygonPerimeterEdge(
        self,
        PolygonID: mesh_description.PolygonID,
        PerimeterEdgeNumber: int,
        bOutEdgeWindingIsReversedForPolygon: bool,
    ) -> mesh_description.EdgeID: ...
    def GetPolygonInGroup(
        self, PolygonGroupID: mesh_description.PolygonGroupID, PolygonNumber: int
    ) -> mesh_description.PolygonID: ...
    def GetPolygonHoleVertices(
        self,
        PolygonID: mesh_description.PolygonID,
        HoleNumber: int,
        OutHoleVertexIDs: unreal.WrappedArray[mesh_description.VertexID],
    ): ...
    def GetPolygonHoleVertexInstances(
        self,
        PolygonID: mesh_description.PolygonID,
        HoleNumber: int,
        OutHoleVertexInstanceIDs: unreal.WrappedArray[
            mesh_description.VertexInstanceID
        ],
    ): ...
    def GetPolygonHoleVertexInstance(
        self,
        PolygonID: mesh_description.PolygonID,
        HoleNumber: int,
        PolygonVertexNumber: int,
    ) -> mesh_description.VertexInstanceID: ...
    def GetPolygonHoleVertexCount(
        self, PolygonID: mesh_description.PolygonID, HoleNumber: int
    ) -> int: ...
    def GetPolygonHoleVertex(
        self,
        PolygonID: mesh_description.PolygonID,
        HoleNumber: int,
        PolygonVertexNumber: int,
    ) -> mesh_description.VertexID: ...
    def GetPolygonHoleEdges(
        self,
        PolygonID: mesh_description.PolygonID,
        HoleNumber: int,
        OutHoleEdgeIDs: unreal.WrappedArray[mesh_description.EdgeID],
    ): ...
    def GetPolygonHoleEdgeCount(
        self, PolygonID: mesh_description.PolygonID, HoleNumber: int
    ) -> int: ...
    def GetPolygonHoleEdge(
        self,
        PolygonID: mesh_description.PolygonID,
        HoleNumber: int,
        HoleEdgeNumber: int,
    ) -> mesh_description.EdgeID: ...
    def GetPolygonHoleCount(self, PolygonID: mesh_description.PolygonID) -> int: ...
    def GetPolygonGroupCount(self) -> int: ...
    def GetPolygonCountInGroup(
        self, PolygonGroupID: mesh_description.PolygonGroupID
    ) -> int: ...
    def GetPolygonCount(self) -> int: ...
    def GetPolygonAdjacentPolygons(
        self,
        PolygonID: mesh_description.PolygonID,
        OutAdjacentPolygons: unreal.WrappedArray[mesh_description.PolygonID],
    ): ...
    def GetGroupForPolygon(
        self, PolygonID: mesh_description.PolygonID
    ) -> mesh_description.PolygonGroupID: ...
    def GetFirstValidPolygonGroup(self) -> mesh_description.PolygonGroupID: ...
    def GetEdgeVertex(
        self, EdgeID: mesh_description.EdgeID, EdgeVertexNumber: int
    ) -> mesh_description.VertexID: ...
    def GetEdgeLoopElements(
        self,
        EdgeID: mesh_description.EdgeID,
        EdgeLoopIDs: unreal.WrappedArray[mesh_description.EdgeID],
    ): ...
    def GetEdgeCount(self) -> int: ...
    def GetEdgeConnectedPolygons(
        self,
        EdgeID: mesh_description.EdgeID,
        OutConnectedPolygonIDs: unreal.WrappedArray[mesh_description.PolygonID],
    ): ...
    def GetEdgeConnectedPolygonCount(self, EdgeID: mesh_description.EdgeID) -> int: ...
    def GetEdgeConnectedPolygon(
        self, EdgeID: mesh_description.EdgeID, ConnectedPolygonNumber: int
    ) -> mesh_description.PolygonID: ...
    def GeneratePolygonTangentsAndNormals(
        self, PolygonIDs: unreal.WrappedArray[mesh_description.PolygonID]
    ): ...
    def FlipPolygons(
        self, PolygonIDs: unreal.WrappedArray[mesh_description.PolygonID]
    ): ...
    def FindPolygonPerimeterVertexNumberForVertex(
        self, PolygonID: mesh_description.PolygonID, VertexID: mesh_description.VertexID
    ) -> int: ...
    def FindPolygonLoop(
        self,
        EdgeID: mesh_description.EdgeID,
        OutEdgeLoopEdgeIDs: unreal.WrappedArray[mesh_description.EdgeID],
        OutFlippedEdgeIDs: unreal.WrappedArray[mesh_description.EdgeID],
        OutReversedEdgeIDPathToTake: unreal.WrappedArray[mesh_description.EdgeID],
        OutPolygonIDsToSplit: unreal.WrappedArray[mesh_description.PolygonID],
    ): ...
    def FindPolygonHoleVertexNumberForVertex(
        self,
        PolygonID: mesh_description.PolygonID,
        HoleNumber: int,
        VertexID: mesh_description.VertexID,
    ) -> int: ...
    def ExtrudePolygons(
        self,
        Polygons: unreal.WrappedArray[mesh_description.PolygonID],
        ExtrudeDistance: float,
        bKeepNeighborsTogether: bool,
        OutNewExtrudedFrontPolygons: unreal.WrappedArray[mesh_description.PolygonID],
    ): ...
    def ExtendVertices(
        self,
        VertexIDs: unreal.WrappedArray[mesh_description.VertexID],
        bOnlyExtendClosestEdge: bool,
        ReferencePosition: core_uobject.Vector,
        OutNewExtendedVertexIDs: unreal.WrappedArray[mesh_description.VertexID],
    ): ...
    def ExtendEdges(
        self,
        EdgeIDs: unreal.WrappedArray[mesh_description.EdgeID],
        bWeldNeighbors: bool,
        OutNewExtendedEdgeIDs: unreal.WrappedArray[mesh_description.EdgeID],
    ): ...
    def EndModification(self, bFromUndo: bool): ...
    def DeleteVertexInstances(
        self,
        VertexInstanceIDsToDelete: unreal.WrappedArray[
            mesh_description.VertexInstanceID
        ],
        bDeleteOrphanedVertices: bool,
    ): ...
    def DeleteVertexAndConnectedEdgesAndPolygons(
        self,
        VertexID: mesh_description.VertexID,
        bDeleteOrphanedEdges: bool,
        bDeleteOrphanedVertices: bool,
        bDeleteOrphanedVertexInstances: bool,
        bDeleteEmptyPolygonGroups: bool,
    ): ...
    def DeletePolygons(
        self,
        PolygonIDsToDelete: unreal.WrappedArray[mesh_description.PolygonID],
        bDeleteOrphanedEdges: bool,
        bDeleteOrphanedVertices: bool,
        bDeleteOrphanedVertexInstances: bool,
        bDeleteEmptyPolygonGroups: bool,
    ): ...
    def DeletePolygonGroups(
        self, PolygonGroupIDs: unreal.WrappedArray[mesh_description.PolygonGroupID]
    ): ...
    def DeleteOrphanVertices(
        self, VertexIDsToDelete: unreal.WrappedArray[mesh_description.VertexID]
    ): ...
    def DeleteEdges(
        self,
        EdgeIDsToDelete: unreal.WrappedArray[mesh_description.EdgeID],
        bDeleteOrphanedVertices: bool,
    ): ...
    def DeleteEdgeAndConnectedPolygons(
        self,
        EdgeID: mesh_description.EdgeID,
        bDeleteOrphanedEdges: bool,
        bDeleteOrphanedVertices: bool,
        bDeleteOrphanedVertexInstances: bool,
        bDeleteEmptyPolygonGroups: bool,
    ): ...
    def CreateVertices(
        self,
        VerticesToCreate: unreal.WrappedArray[VertexToCreate],
        OutNewVertexIDs: unreal.WrappedArray[mesh_description.VertexID],
    ): ...
    def CreateVertexInstances(
        self,
        VertexInstancesToCreate: unreal.WrappedArray[VertexInstanceToCreate],
        OutNewVertexInstanceIDs: unreal.WrappedArray[mesh_description.VertexInstanceID],
    ): ...
    def CreatePolygons(
        self,
        PolygonsToCreate: unreal.WrappedArray[PolygonToCreate],
        OutNewPolygonIDs: unreal.WrappedArray[mesh_description.PolygonID],
        OutNewEdgeIDs: unreal.WrappedArray[mesh_description.EdgeID],
    ): ...
    def CreatePolygonGroups(
        self,
        PolygonGroupsToCreate: unreal.WrappedArray[PolygonGroupToCreate],
        OutNewPolygonGroupIDs: unreal.WrappedArray[mesh_description.PolygonGroupID],
    ): ...
    def CreateMissingPolygonPerimeterEdges(
        self,
        PolygonID: mesh_description.PolygonID,
        OutNewEdgeIDs: unreal.WrappedArray[mesh_description.EdgeID],
    ): ...
    def CreateMissingPolygonHoleEdges(
        self,
        PolygonID: mesh_description.PolygonID,
        HoleNumber: int,
        OutNewEdgeIDs: unreal.WrappedArray[mesh_description.EdgeID],
    ): ...
    def CreateEmptyVertexRange(
        self,
        NumVerticesToCreate: int,
        OutNewVertexIDs: unreal.WrappedArray[mesh_description.VertexID],
    ): ...
    def CreateEdges(
        self,
        EdgesToCreate: unreal.WrappedArray[EdgeToCreate],
        OutNewEdgeIDs: unreal.WrappedArray[mesh_description.EdgeID],
    ): ...
    def ComputePolygonTriangulation(
        self,
        PolygonID: mesh_description.PolygonID,
        OutTriangles: unreal.WrappedArray[mesh_description.MeshTriangle],
    ): ...
    def ComputePolygonsSharedEdges(
        self,
        PolygonIDs: unreal.WrappedArray[mesh_description.PolygonID],
        OutSharedEdgeIDs: unreal.WrappedArray[mesh_description.EdgeID],
    ): ...
    def ComputePolygonPlane(
        self, PolygonID: mesh_description.PolygonID
    ) -> core_uobject.Plane: ...
    def ComputePolygonNormal(
        self, PolygonID: mesh_description.PolygonID
    ) -> core_uobject.Vector: ...
    def ComputePolygonCenter(
        self, PolygonID: mesh_description.PolygonID
    ) -> core_uobject.Vector: ...
    def ComputeBoundingBoxAndSphere(self) -> core_uobject.BoxSphereBounds: ...
    def ComputeBoundingBox(self) -> core_uobject.Box: ...
    def ComputeBarycentricWeightForPointOnPolygon(
        self,
        PolygonID: mesh_description.PolygonID,
        PointOnPolygon: core_uobject.Vector,
        OutTriangle: mesh_description.MeshTriangle,
        OutTriangleVertexWeights: core_uobject.Vector,
    ) -> bool: ...
    def CommitInstance(
        self, ComponentToInstanceTo: engine.PrimitiveComponent
    ) -> EditableMesh: ...
    def COMMIT(self): ...
    def ChangePolygonsVertexInstances(
        self,
        VertexInstancesForPolygons: unreal.WrappedArray[
            ChangeVertexInstancesForPolygon
        ],
    ): ...
    def BevelPolygons(
        self,
        PolygonIDs: unreal.WrappedArray[mesh_description.PolygonID],
        BevelFixedDistance: float,
        BevelProgressTowardCenter: float,
        OutNewCenterPolygonIDs: unreal.WrappedArray[mesh_description.PolygonID],
        OutNewSidePolygonIDs: unreal.WrappedArray[mesh_description.PolygonID],
    ): ...
    def AssignPolygonsToPolygonGroups(
        self,
        PolygonGroupForPolygons: unreal.WrappedArray[PolygonGroupForPolygon],
        bDeleteOrphanedPolygonGroups: bool,
    ): ...
    def AnyChangesToUndo(self) -> bool: ...


class EditableMeshAdapter(unreal.UObject): ...


class EditableMeshFactory(unreal.UObject):

    def MakeEditableMesh(
        self, PrimitiveComponent: engine.PrimitiveComponent, LODIndex: int
    ) -> EditableMesh: ...


class EditableStaticMeshAdapter(EditableMeshAdapter):
    StaticMesh: engine.StaticMesh
    OriginalStaticMesh: engine.StaticMesh
    StaticMeshLODIndex: int


class PolygonGroupForPolygon:
    PolygonID: mesh_description.PolygonID
    PolygonGroupID: mesh_description.PolygonGroupID


class PolygonGroupToCreate:
    PolygonGroupAttributes: MeshElementAttributeList
    OriginalPolygonGroupID: mesh_description.PolygonGroupID


class MeshElementAttributeList:
    Attributes: unreal.WrappedArray[MeshElementAttributeData]


class MeshElementAttributeData:
    AttributeName: str
    AttributeIndex: int
    AttributeValue: MeshElementAttributeValue


class MeshElementAttributeValue: ...


class VertexToMove:
    VertexID: mesh_description.VertexID
    NewVertexPosition: core_uobject.Vector


class VerticesForEdge:
    EdgeID: mesh_description.EdgeID
    NewVertexID1: mesh_description.VertexID


class ChangeVertexInstancesForPolygon:
    PolygonID: mesh_description.PolygonID
    PerimeterVertexIndicesAndInstanceIDs: unreal.WrappedArray[VertexIndexAndInstanceID]
    VertexIndicesAndInstanceIDsForEachHole: unreal.WrappedArray[
        VertexInstancesForPolygonHole
    ]


class VertexInstancesForPolygonHole:
    VertexIndicesAndInstanceIDs: unreal.WrappedArray[VertexIndexAndInstanceID]


class VertexIndexAndInstanceID:
    ContourIndex: int
    VertexInstanceID: mesh_description.VertexInstanceID


class VertexAttributesForPolygon:
    PolygonID: mesh_description.PolygonID
    PerimeterVertexAttributeLists: unreal.WrappedArray[MeshElementAttributeList]
    VertexAttributeListsForEachHole: unreal.WrappedArray[VertexAttributesForPolygonHole]


class VertexAttributesForPolygonHole:
    VertexAttributeList: unreal.WrappedArray[MeshElementAttributeList]


class AttributesForEdge:
    EdgeID: mesh_description.EdgeID
    EdgeAttributes: MeshElementAttributeList


class AttributesForVertexInstance:
    VertexInstanceID: mesh_description.VertexInstanceID
    VertexInstanceAttributes: MeshElementAttributeList


class AttributesForVertex:
    VertexID: mesh_description.VertexID
    VertexAttributes: MeshElementAttributeList


class PolygonToSplit:
    PolygonID: mesh_description.PolygonID
    VertexPairsToSplitAt: unreal.WrappedArray[VertexPair]


class VertexPair:
    VertexID1: mesh_description.VertexID


class PolygonToCreate:
    PolygonGroupID: mesh_description.PolygonGroupID
    PerimeterVertices: unreal.WrappedArray[VertexAndAttributes]
    PolygonHoles: unreal.WrappedArray[PolygonHoleVertices]
    OriginalPolygonID: mesh_description.PolygonID
    PolygonEdgeHardness: EPolygonEdgeHardness


class PolygonHoleVertices:
    HoleVertices: unreal.WrappedArray[VertexAndAttributes]


class VertexAndAttributes:
    VertexInstanceID: mesh_description.VertexInstanceID
    VertexID: mesh_description.VertexID
    PolygonVertexAttributes: MeshElementAttributeList


class EdgeToCreate:
    VertexID1: mesh_description.VertexID
    ConnectedPolygons: unreal.WrappedArray[mesh_description.PolygonID]
    EdgeAttributes: MeshElementAttributeList
    OriginalEdgeID: mesh_description.EdgeID


class VertexInstanceToCreate:
    VertexID: mesh_description.VertexID
    VertexInstanceAttributes: MeshElementAttributeList
    OriginalVertexInstanceID: mesh_description.VertexInstanceID


class VertexToCreate:
    VertexAttributes: MeshElementAttributeList
    OriginalVertexID: mesh_description.VertexID


class SubdivisionLimitData:
    VertexPositions: unreal.WrappedArray[core_uobject.Vector]
    Sections: unreal.WrappedArray[SubdivisionLimitSection]
    SubdividedWireEdges: unreal.WrappedArray[SubdividedWireEdge]


class SubdividedWireEdge:
    EdgeVertex1PositionIndex: int


class SubdivisionLimitSection:
    SubdividedQuads: unreal.WrappedArray[SubdividedQuad]


class SubdividedQuad:
    QuadVertex1: SubdividedQuadVertex
    QuadVertex2: SubdividedQuadVertex
    QuadVertex3: SubdividedQuadVertex


class SubdividedQuadVertex:
    VertexPositionIndex: int
    TextureCoordinate1: core_uobject.Vector2D
    VertexColor: core_uobject.Color
    GbxVertexColor: core_uobject.Color
    VertexNormal: core_uobject.Vector
    VertexTangent: core_uobject.Vector
    VertexBinormalSign: float


class RenderingPolygonGroup:
    RenderingSectionIndex: int
    MaterialIndex: int
    MaxTriangles: int


class RenderingPolygon:
    PolygonGroupID: mesh_description.PolygonGroupID
    TriangulatedPolygonTriangleIndices: unreal.WrappedArray[TriangleID]


class TriangleID(mesh_description.ElementID): ...


class ETriangleTessellationMode(enum.Enum):
    FourTriangles = 0
    ETriangleTessellationMode_MAX = 1


class EInsetPolygonsMode(enum.Enum):
    CenterPolygonOnly = 0
    SidePolygonsOnly = 1


class EPolygonEdgeHardness(enum.Enum):
    NewEdgesHard = 0
    AllEdgesSoft = 1
    EPolygonEdgeHardness_MAX = 2


class EMeshElementAttributeType(enum.Enum):
    FVector = 0
    FVector4 = 1
    Float = 2
    EMeshElementAttributeType_MAX = 3


class EMeshTopologyChange(enum.Enum):
    TopologyChange = 0
    EMeshTopologyChange_MAX = 1


class EMeshModificationType(enum.Enum):
    Final = 0
    Interim = 1

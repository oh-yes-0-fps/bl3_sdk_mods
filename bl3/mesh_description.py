from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum





class MeshDescription(unreal.UObject): ...


class ElementID:
    IDValue: int



class PolygonGroupID(ElementID): ...


class PolygonID(ElementID): ...


class VertexID(ElementID): ...


class EdgeID(ElementID): ...


class VertexInstanceID(ElementID): ...


class MeshTriangle:
    VertexInstanceID1: VertexInstanceID
    VertexInstanceID2: VertexInstanceID



class EComputeNTBsOptions(enum.Enum):
    Tangents = 0
    Normals = 1
    WeightedNTBs = 2

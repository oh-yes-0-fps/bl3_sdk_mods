from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine


class ReplicationGraph(engine.ReplicationDriver):
    ReplicationConnectionManagerClass: unreal.UClass
    NetDriver: engine.NetDriver
    Connections: unreal.WrappedArray[NetReplicationGraphConnection]
    PendingConnections: unreal.WrappedArray[NetReplicationGraphConnection]
    GlobalGraphNodes: unreal.WrappedArray[ReplicationGraphNode]
    PrepareForReplicationNodes: unreal.WrappedArray[ReplicationGraphNode]


class ReplicationGraphNode(unreal.UObject):
    AllChildNodes: unreal.WrappedArray[ReplicationGraphNode]


class ReplicationGraphNode_ActorList(ReplicationGraphNode): ...


class NetReplicationGraphConnection(engine.ReplicationConnectionDriver):
    NetConnection: engine.NetConnection
    DebugActor: ReplicationGraphDebugActor
    ConnectionGraphNodes: unreal.WrappedArray[ReplicationGraphNode]
    TearOffNode: ReplicationGraphNode_TearOff_ForConnection
    NonReplicatedDormantActors: unreal.WrappedArray[engine.Actor]


class BasicReplicationGraph(ReplicationGraph):
    GridNode: ReplicationGraphNode_GridSpatialization2D
    AlwaysRelevantNode: ReplicationGraphNode_ActorList
    AlwaysRelevantForConnectionList: unreal.WrappedArray[
        ConnectionAlwaysRelevantNodePair
    ]
    ActorsWithoutNetConnection: unreal.WrappedArray[engine.Actor]


class ReplicationGraphNode_ActorListFrequencyBuckets(ReplicationGraphNode): ...


class ReplicationGraphNode_ConnectionDormanyNode(ReplicationGraphNode_ActorList): ...


class ReplicationGraphNode_DormancyNode(ReplicationGraphNode_ActorList): ...


class ReplicationGraphNode_GridCell(ReplicationGraphNode_ActorList):
    DynamicNode: ReplicationGraphNode_ActorListFrequencyBuckets
    DormancyNode: ReplicationGraphNode_DormancyNode


class ReplicationGraphNode_GridSpatialization2D(ReplicationGraphNode): ...


class ReplicationGraphNode_AlwaysRelevant(ReplicationGraphNode):
    ChildNode: ReplicationGraphNode


class ReplicationGraphNode_AlwaysRelevant_ForConnection(ReplicationGraphNode_ActorList):
    LastViewer: engine.Actor
    LastViewTarget: engine.Actor


class ReplicationGraphNode_TearOff_ForConnection(ReplicationGraphNode):
    TearOffActors: unreal.WrappedArray[TearOffActorInfo]


class ReplicationGraphDebugActor(engine.Actor):
    ReplicationGraph: ReplicationGraph
    ConnectionManager: NetReplicationGraphConnection

    def ServerStopDebugging(self): ...
    def ServerStartDebugging(self): ...
    def ServerSetCullDistanceForClass(
        self, Class: unreal.UClass, CullDistance: float
    ): ...
    def ServerPrintAllActorInfo(self, str: str): ...
    def ServerCellInfo(self): ...
    def ClientCellInfo(
        self,
        CellLocation: core_uobject.Vector,
        CellExtent: core_uobject.Vector,
        Actors: unreal.WrappedArray[engine.Actor],
    ): ...


class ConnectionAlwaysRelevantNodePair:
    NetConnection: engine.NetConnection
    Node: ReplicationGraphNode_AlwaysRelevant_ForConnection


class TearOffActorInfo:
    Actor: engine.Actor

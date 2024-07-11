from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import engine


class GeometryCache(unreal.UObject):
    Materials: unreal.WrappedArray[engine.MaterialInterface]
    Tracks: unreal.WrappedArray[GeometryCacheTrack]
    StartFrame: int
    EndFrame: int


class GeometryCacheActor(engine.Actor):
    GeometryCacheComponent: GeometryCacheComponent

    def GetGeometryCacheComponent(self) -> GeometryCacheComponent: ...


class GeometryCacheCodecBase(unreal.UObject):
    TopologyRanges: unreal.WrappedArray[int]


class GeometryCacheCodecRaw(GeometryCacheCodecBase):
    DummyProperty: int


class GeometryCacheCodecV1(GeometryCacheCodecBase): ...


class GeometryCacheComponent(engine.MeshComponent):
    GeometryCache: GeometryCache
    bRunning: bool
    bLooping: bool
    StartTimeOffset: float
    PlaybackSpeed: float
    NumTracks: int
    ElapsedTime: float
    Duration: float
    bManualTick: bool

    def TickAtThisTime(
        self, Time: float, bInIsRunning: bool, bInBackwards: bool, bInIsLooping: bool
    ): ...
    def Stop(self): ...
    def SetStartTimeOffset(self, NewStartTimeOffset: float): ...
    def SetPlaybackSpeed(self, NewPlaybackSpeed: float): ...
    def SetLooping(self, bNewLooping: bool): ...
    def SetGeometryCache(self, NewGeomCache: GeometryCache) -> bool: ...
    def PlayReversedFromEnd(self): ...
    def PlayReversed(self): ...
    def PlayFromStart(self): ...
    def Play(self): ...
    def Pause(self): ...
    def IsPlayingReversed(self) -> bool: ...
    def IsPlaying(self) -> bool: ...
    def IsLooping(self) -> bool: ...
    def GetStartTimeOffset(self) -> float: ...
    def GetPlaybackSpeed(self) -> float: ...
    def GetPlaybackDirection(self) -> float: ...
    def GetNumberOfFrames(self) -> int: ...
    def GetDuration(self) -> float: ...
    def GetAnimationTime(self) -> float: ...


class GeometryCacheTrack(unreal.UObject):
    Duration: float


class GeometryCacheTrack_FlipbookAnimation(GeometryCacheTrack):
    NumMeshSamples: int

    def AddMeshSample(self, MeshData: GeometryCacheMeshData, SampleTime: float): ...


class GeometryCacheTrackStreamable(GeometryCacheTrack):
    Codec: GeometryCacheCodecBase
    StartSampleTime: float


class GeometryCacheTrack_TransformAnimation(GeometryCacheTrack):

    def SetMesh(self, NewMeshData: GeometryCacheMeshData): ...


class GeometryCacheTrack_TransformGroupAnimation(GeometryCacheTrack):

    def SetMesh(self, NewMeshData: GeometryCacheMeshData): ...


class TrackRenderData: ...


class GeometryCacheMeshData: ...


class GeometryCacheVertexInfo: ...


class GeometryCacheMeshBatchInfo: ...

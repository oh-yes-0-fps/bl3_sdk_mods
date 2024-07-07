from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import engine



class GeometryCache(unreal.UObject):
    Materials: unreal.WrappedArray[engine.MaterialInterface]
    Tracks: unreal.WrappedArray[GeometryCacheTrack]
    StartFrame: int
    EndFrame: int



class GeometryCacheActor(engine.Actor):
    GeometryCacheComponent: GeometryCacheComponent
    def GetGeometryCacheComponent(self, ReturnValue: GeometryCacheComponent) -> GeometryCacheComponent: ...


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
    def TickAtThisTime(self, Time: float, bInIsRunning: bool, bInBackwards: bool, bInIsLooping: bool): ...
    def Stop(self): ...
    def SetStartTimeOffset(self, NewStartTimeOffset: float): ...
    def SetPlaybackSpeed(self, NewPlaybackSpeed: float): ...
    def SetLooping(self, bNewLooping: bool): ...
    def SetGeometryCache(self, NewGeomCache: GeometryCache, ReturnValue: bool) -> bool: ...
    def PlayReversedFromEnd(self): ...
    def PlayReversed(self): ...
    def PlayFromStart(self): ...
    def Play(self): ...
    def Pause(self): ...
    def IsPlayingReversed(self, ReturnValue: bool) -> bool: ...
    def IsPlaying(self, ReturnValue: bool) -> bool: ...
    def IsLooping(self, ReturnValue: bool) -> bool: ...
    def GetStartTimeOffset(self, ReturnValue: float) -> float: ...
    def GetPlaybackSpeed(self, ReturnValue: float) -> float: ...
    def GetPlaybackDirection(self, ReturnValue: float) -> float: ...
    def GetNumberOfFrames(self, ReturnValue: int) -> int: ...
    def GetDuration(self, ReturnValue: float) -> float: ...
    def GetAnimationTime(self, ReturnValue: float) -> float: ...


class GeometryCacheTrack(unreal.UObject):
    Duration: float



class GeometryCacheTrack_FlipbookAnimation(GeometryCacheTrack):

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

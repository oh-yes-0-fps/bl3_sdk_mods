from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import movie_scene
from . import gameplay_tasks
from . import level_sequence


class GbxLevelSequence(level_sequence.LevelSequence): ...


class GbxLevelSequenceActor(level_sequence.LevelSequenceActor):
    OnPlay: Any
    OnPause: Any
    OnFinished: Any
    OnStop: Any
    GameplayTasksComponent: gameplay_tasks.GameplayTasksComponent
    GbxLevelSequencePlayer: GbxLevelSequencePlayer
    BindingSlots: unreal.WrappedArray[GbxLevelSequenceBindingSlot]
    ReplicatedLevelSequence: core_uobject.SoftObjectPath
    ReplicatedPlaybackStatus: int
    bReplicatedReversePlayback: bool
    ReplicatedPlaybackPosition: float
    ReplicatedPlaybackRate: float
    ReplicatedLoopCount: int
    BoundActors: unreal.WrappedArray[GbxLevelSequenceBoundActorSlot]
    bIgnoreReplicatedPlaybackState: bool
    bPendingReplicatedCutsceneSkip: bool
    bWasCutsceneSkipped: bool

    def Stop(self): ...
    def SetPlayRate(self, PlayRate: float): ...
    def PlayLooping(self, NumLoops: int): ...
    def PlayFromStart(self): ...
    def Play(self): ...
    def Pause(self): ...
    def OnRep_ReplicatedCutsceneSkip(self): ...
    def OnLevelSequenceStop(self): ...
    def OnLevelSequencePlay(self): ...
    def OnLevelSequencePause(self): ...
    def OnLevelSequenceFinished(self): ...
    def IsPlaying(self) -> bool: ...
    def IsPaused(self) -> bool: ...
    def IsFinished(self) -> bool: ...
    def GoToEndAndStop(self): ...
    def GetPlayRate(self) -> float: ...


class GbxLevelSequencePlayer(level_sequence.LevelSequencePlayer):
    GbxLevelSequenceActor: GbxLevelSequenceActor

    def OnStarted(self): ...
    def IsFinished(self) -> bool: ...
    def CreateGbxLevelSequencePlayer(
        self,
        WorldContextObject: unreal.UObject,
        LevelSequence: level_sequence.LevelSequence,
        bPlay: bool,
        Settings: movie_scene.MovieSceneSequencePlaybackSettings,
        OutActor: GbxLevelSequenceActor,
    ) -> GbxLevelSequencePlayer: ...


class GbxLevelSequenceThrottleLibrary(engine.BlueprintFunctionLibrary):

    def UnlimitSequenceActor(self, Player: GbxLevelSequenceActor): ...
    def ShouldLimitSequenceGroup(self, InGroup: str) -> bool: ...
    def LimitSequenceActor(self, Player: GbxLevelSequenceActor, Group: str): ...
    def ClearLimitGroup(self, Group: str): ...


class GbxMovieSceneBindingOverrides(movie_scene.MovieSceneBindingOverrides): ...


class GbxLevelSequenceBoundActorSlot:
    BindingID: core_uobject.Guid
    BoundActor: engine.Actor


class GbxLevelSequenceBindingSlot:
    BindingID: core_uobject.Guid
    BindingName: str
    BindingClass: unreal.UClass
    BoundActor: engine.Actor
    Location: core_uobject.Vector
    Rotation: core_uobject.Rotator
    SpawnOwnership: movie_scene.ESpawnOwnership

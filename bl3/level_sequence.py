from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine
from . import umg
from . import movie_scene



class LevelSequence(movie_scene.MovieSceneSequence):
    MovieScene: movie_scene.MovieScene
    ObjectReferences: LevelSequenceObjectReferenceMap
    BindingReferences: LevelSequenceBindingReferences



class LevelSequenceActor(engine.Actor):
    bAutoPlay: bool
    PlaybackSettings: movie_scene.MovieSceneSequencePlaybackSettings
    SequencePlayer: LevelSequencePlayer
    LevelSequence: core_uobject.SoftObjectPath
    AdditionalEventReceivers: unreal.WrappedArray[engine.Actor]
    BurnInOptions: LevelSequenceBurnInOptions
    BindingOverrides: movie_scene.MovieSceneBindingOverrides
    bOverrideInstanceData: bool
    DefaultInstanceData: unreal.UObject
    BurnInInstance: LevelSequenceBurnIn
    def SetSequence(self, InSequence: LevelSequence): ...
    def SetEventReceivers(self, AdditionalReceivers: unreal.WrappedArray[engine.Actor]): ...
    def SetBinding(self, Binding: movie_scene.MovieSceneObjectBindingID, Actors: unreal.WrappedArray[engine.Actor], bAllowBindingsFromAsset: bool): ...
    def ResetBindings(self): ...
    def ResetBinding(self, Binding: movie_scene.MovieSceneObjectBindingID): ...
    def RemoveBinding(self, Binding: movie_scene.MovieSceneObjectBindingID, Actor: engine.Actor): ...
    def OnRequestStopTicking(self): ...
    def OnCancelStopTicking(self): ...
    def GetSequence(self, bLoad: bool, bInitializePlayer: bool, ReturnValue: LevelSequence) -> LevelSequence: ...
    def AddBinding(self, Binding: movie_scene.MovieSceneObjectBindingID, Actor: engine.Actor, bAllowBindingsFromAsset: bool): ...


class LevelSequencePlayer(movie_scene.MovieSceneSequencePlayer):
    AdditionalEventReceivers: unreal.WrappedArray[unreal.UObject]
    def CreateLevelSequencePlayer(self, WorldContextObject: unreal.UObject, LevelSequence: LevelSequence, Settings: movie_scene.MovieSceneSequencePlaybackSettings, OutActor: LevelSequenceActor, ReturnValue: LevelSequencePlayer) -> LevelSequencePlayer: ...


class DefaultLevelSequenceInstanceData(unreal.UObject):
    TransformOriginActor: engine.Actor
    TransformOrigin: core_uobject.Transform



class LevelSequenceBurnInInitSettings(unreal.UObject): ...


class LevelSequenceBurnInOptions(unreal.UObject):
    bUseBurnIn: bool
    BurnInClass: core_uobject.SoftClassPath
    Settings: LevelSequenceBurnInInitSettings
    def SetBurnIn(self, InBurnInClass: core_uobject.SoftClassPath): ...


class LevelSequenceBurnIn(umg.UserWidget):
    FrameInformation: LevelSequencePlayerSnapshot
    LevelSequenceActor: LevelSequenceActor
    def SetSettings(self, InSettings: unreal.UObject): ...
    def GetSettingsClass(self, ReturnValue: unreal.UClass) -> unreal.UClass: ...


class BoundActorProxy: ...


class LevelSequenceBindingReferences: ...


class LevelSequenceBindingReferenceArray:
    References: unreal.WrappedArray[LevelSequenceBindingReference]



class LevelSequenceBindingReference:
    PackageName: str
    ExternalObjectPath: core_uobject.SoftObjectPath
    ObjectPath: str



class LevelSequenceObjectReferenceMap: ...


class LevelSequenceLegacyObjectReference: ...


class LevelSequenceObject:
    ComponentName: str
    CachedComponent: unreal.UObject



class LevelSequencePlayerSnapshot:
    MasterName: str
    MasterTime: core_uobject.QualifiedFrameTime
    CurrentShotName: str
    CurrentShotLocalTime: core_uobject.QualifiedFrameTime
    CameraComponent: engine.CameraComponent
    Settings: LevelSequenceSnapshotSettings
    ShotID: movie_scene.MovieSceneSequenceID



class LevelSequenceSnapshotSettings:
    ZeroPadAmount: int
    FrameRate: core_uobject.FrameRate


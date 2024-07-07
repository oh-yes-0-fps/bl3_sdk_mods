from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine
from . import movie_scene



class ActorSequence(movie_scene.MovieSceneSequence):
    MovieScene: movie_scene.MovieScene
    ObjectReferences: ActorSequenceObjectReferenceMap



class ActorSequenceComponent(engine.ActorComponent):
    bAutoPlay: bool
    PlaybackSettings: movie_scene.MovieSceneSequencePlaybackSettings
    Sequence: ActorSequence
    SequencePlayer: ActorSequencePlayer



class ActorSequencePlayer(movie_scene.MovieSceneSequencePlayer): ...


class ActorSequenceObjectReferenceMap:
    BindingIds: unreal.WrappedArray[core_uobject.Guid]
    References: unreal.WrappedArray[ActorSequenceObjectReferences]



class ActorSequenceObjectReferences:
    Array: unreal.WrappedArray[ActorSequenceObjectReference]



class ActorSequenceObjectReference:
    Type: EActorSequenceObjectReferenceType
    ActorId: core_uobject.Guid
    PathToComponent: str



class EActorSequenceObjectReferenceType(enum.Enum):
    ExternalActor = 0
    Component = 1

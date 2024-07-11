from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import wwise_audio
from . import movie_scene


class FaceFXAsset(unreal.UObject): ...


class FaceFXActor(FaceFXAsset):
    PlatformData: unreal.WrappedArray[FaceFXActorData]
    Animations: unreal.WrappedArray[FaceFXAnim]
    bHasBonesFromMultipleSkeletons: bool


class FaceFXAnim(FaceFXAsset):
    PlatformData: unreal.WrappedArray[FaceFXAnimData]
    ID: FaceFXAnimId
    Audio: FaceFXAudioAsset


class FaceFXAnimationSection(movie_scene.MovieSceneSection):
    SkelMeshComponentId: FaceFXSkelMeshComponentId
    AnimationId: FaceFXAnimId
    Animation: Any
    StartOffset: float
    EndOffset: float
    bIsAnimationDurationLoaded: bool
    AnimationDuration: float


class FaceFXAnimationTrack(movie_scene.MovieSceneNameableTrack):
    AnimationSections: unreal.WrappedArray[movie_scene.MovieSceneSection]


class FaceFXAnimSet(engine.DataAsset):
    FaceFXAnimSetData: GbxFaceFXAnimSetData


class FaceFXAudioComponent(engine.ActorComponent):
    WwiseAudioComponent: wwise_audio.WwiseAudioComponent


class FaceFXCharacter(unreal.UObject):
    FaceFXActor: FaceFXActor
    AudioComponent: FaceFXAudioComponent
    CurrentAnim: FaceFXAnim
    CurrentAnimSet: FaceFXAnimSet


class FaceFXComponent(engine.ActorComponent):
    OnPlaybackAudioStart: Any
    OnPlaybackStopped: Any
    Entries: unreal.WrappedArray[FaceFXEntry]

    def StopAll(self): ...
    def Stop(
        self, SkelMeshComp: engine.SkeletalMeshComponent, Caller: unreal.UObject
    ) -> bool: ...
    def Setup(
        self,
        SkelMeshComp: engine.SkeletalMeshComponent,
        AudioComponent: FaceFXAudioComponent,
        Asset: FaceFXActor,
        IsAutoPlaySound: bool,
        IsDisableMorphTargets: bool,
        Caller: unreal.UObject,
    ) -> bool: ...
    def Resume(
        self, SkelMeshComp: engine.SkeletalMeshComponent, Caller: unreal.UObject
    ) -> bool: ...
    def PlayById(
        self,
        Group: str,
        AnimName: str,
        SkelMeshComp: engine.SkeletalMeshComponent,
        Loop: bool,
        Caller: unreal.UObject,
    ) -> bool: ...
    def Play(
        self,
        Animation: FaceFXAnim,
        SkelMeshComp: engine.SkeletalMeshComponent,
        Loop: bool,
        Caller: unreal.UObject,
    ) -> bool: ...
    def Pause(
        self, SkelMeshComp: engine.SkeletalMeshComponent, Caller: unreal.UObject
    ) -> bool: ...
    def OnCharacterPlaybackStopped(
        self, Character: FaceFXCharacter, AnimId: FaceFXAnimId
    ): ...
    def OnCharacterAudioStart(
        self,
        Character: FaceFXCharacter,
        AnimId: FaceFXAnimId,
        IsAudioStarted: bool,
        AudioComponentStartedOn: FaceFXAudioComponent,
    ): ...
    def JumpToById(
        self,
        Position: float,
        Pause: bool,
        Group: str,
        AnimName: str,
        LoopAnimation: bool,
        SkelMeshComp: engine.SkeletalMeshComponent,
        Caller: unreal.UObject,
    ) -> bool: ...
    def JumpTo(
        self,
        Position: float,
        Pause: bool,
        Animation: FaceFXAnim,
        LoopAnimation: bool,
        SkelMeshComp: engine.SkeletalMeshComponent,
        Caller: unreal.UObject,
    ) -> bool: ...
    def IsPlayingAnimation(
        self,
        AnimId: FaceFXAnimId,
        SkelMeshComp: engine.SkeletalMeshComponent,
        Caller: unreal.UObject,
    ) -> bool: ...
    def IsPlaying(
        self, SkelMeshComp: engine.SkeletalMeshComponent, Caller: unreal.UObject
    ) -> bool: ...
    def IsPaused(
        self, SkelMeshComp: engine.SkeletalMeshComponent, Caller: unreal.UObject
    ) -> bool: ...
    def GetFaceFXBlendWeight(
        self,
        SkeletalMeshComponent: engine.SkeletalMeshComponent,
        DeltaTime: float,
        BlendTime: float,
    ) -> float: ...


class FaceFXMatineeControl(engine.InterpTrack):
    Keys: unreal.WrappedArray[FaceFXTrackKey]


class FaceFXMatineeControlInst(engine.InterpTrackInst):
    LastUpdatePosition: float


class FaceFXSettings(unreal.UObject):
    FaceFXLocalizationEquivalents: Any


class FaceFXEditorSettings(unreal.UObject):
    FaceFXDLCSettings: Any


class AnimNode_BlendFaceFXAnimation(engine.AnimNode_Base):
    ComponentPose: engine.ComponentSpacePoseLink
    Alpha: float
    TranslationMode: int
    RotationMode: int
    ScaleMode: int
    BoneNamesToExclude: unreal.WrappedArray[str]


class FaceFXAnimComponentSet:
    SkelMeshComponentId: FaceFXSkelMeshComponentId
    AnimationId: FaceFXAnimId
    Animation: Any


class FaceFXAnimId:
    Group: str
    Name: str


class FaceFXSkelMeshComponentId:
    Index: int
    Name: str


class FaceFXAnimationSectionTemplate(movie_scene.MovieSceneEvalTemplate):
    SectionData: FaceFXAnimationSectionData


class FaceFXAnimationSectionData:
    TrackId: core_uobject.Guid
    RowIndex: int
    AnimationId: FaceFXAnimId
    Animation: Any
    ComponentId: FaceFXSkelMeshComponentId
    AnimDuration: float
    StartOffset: float
    EndOffset: float
    StartTime: core_uobject.FrameNumber
    EndTime: core_uobject.FrameNumber
    bCachedAnimDuration: bool


class FaceFXAudioAsset:
    WwiseEvent: wwise_audio.WwiseEvent
    WwiseID: int


class FaceFXEntry:
    SkelMeshComp: engine.SkeletalMeshComponent
    AudioComp: FaceFXAudioComponent
    Asset: Any
    Character: FaceFXCharacter
    bIsAutoPlaySound: bool
    bIsDisableMorphTargets: bool
    bHasBonesFromMultipleSkeletons: bool


class GbxFaceFXAnimSetData:
    FaceFXAnimDataList: unreal.WrappedArray[GbxFaceFXAnimData]


class GbxFaceFXAnimData:
    FaceFXAnimId: FaceFXAnimId
    Audio: FaceFXAudioAsset
    AnimationRawData: unreal.WrappedArray[FaceFXAnimData]


class FaceFXAnimData:
    RawData: unreal.WrappedArray[int]


class FaceFXActorData:
    ActorRawData: unreal.WrappedArray[int]
    BonesRawData: unreal.WrappedArray[int]
    Ids: unreal.WrappedArray[FaceFXIdData]


class FaceFXIdData:
    ID: int
    Name: str


class FaceFXAnimSetData:
    Animations: unreal.WrappedArray[FaceFXAnimData]


class FaceFXTrackKey:
    SkelMeshComponentId: FaceFXSkelMeshComponentId
    AnimationId: FaceFXAnimId
    Animation: Any
    Time: float
    bLoop: bool
    bIsAnimationDurationLoaded: bool
    AnimationDuration: float


class FaceFXDLCPathSettings:
    PatchContentPath: str
    PluginContentPath: str
    ProductionFolderExtension: str
    WwiseFolderExtension: str
    AdditionalWwiseFolderExtensions: unreal.WrappedArray[str]


class FaceFXLocalizationData:
    GroupName: str
    ExportLanguage: str


class EFaceFXTargetPlatform(enum.Enum):
    XBoxOne = 0
    PS4 = 1
    MAX = 2

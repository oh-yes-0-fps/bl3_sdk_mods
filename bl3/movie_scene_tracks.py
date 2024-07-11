from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import movie_scene


class MovieSceneTransformOrigin(core_uobject.Interface):

    def BP_GetTransformOrigin(self) -> core_uobject.Transform: ...


class MovieScene3DConstraintSection(movie_scene.MovieSceneSection):
    ConstraintId: core_uobject.Guid
    ConstraintBindingID: movie_scene.MovieSceneObjectBindingID


class MovieScene3DAttachSection(MovieScene3DConstraintSection):
    AttachSocketName: str
    AttachComponentName: str
    AttachmentLocationRule: engine.EAttachmentRule
    AttachmentRotationRule: engine.EAttachmentRule
    AttachmentScaleRule: engine.EAttachmentRule
    DetachmentLocationRule: engine.EDetachmentRule
    DetachmentRotationRule: engine.EDetachmentRule
    DetachmentScaleRule: engine.EDetachmentRule


class MovieScene3DConstraintTrack(movie_scene.MovieSceneTrack):
    ConstraintSections: unreal.WrappedArray[movie_scene.MovieSceneSection]


class MovieScene3DAttachTrack(MovieScene3DConstraintTrack): ...


class MovieScene3DPathSection(MovieScene3DConstraintSection):
    TimingCurve: movie_scene.MovieSceneFloatChannel
    FrontAxisEnum: MovieScene3DPathSection_Axis
    UpAxisEnum: MovieScene3DPathSection_Axis
    bFollow: bool
    bReverse: bool
    bForceUpright: bool


class MovieScene3DPathTrack(MovieScene3DConstraintTrack): ...


class MovieScene3DTransformSection(movie_scene.MovieSceneSection):
    TransformMask: MovieSceneTransformMask
    Translation: movie_scene.MovieSceneFloatChannel
    Rotation: movie_scene.MovieSceneFloatChannel
    Scale: movie_scene.MovieSceneFloatChannel
    ManualWeight: movie_scene.MovieSceneFloatChannel
    bUseQuaternionInterpolation: bool


class MovieScenePropertyTrack(movie_scene.MovieSceneNameableTrack):
    PropertyName: str
    PropertyPath: str
    Sections: unreal.WrappedArray[movie_scene.MovieSceneSection]


class MovieScene3DTransformTrack(MovieScenePropertyTrack): ...


class MovieSceneActorReferenceSection(movie_scene.MovieSceneSection):
    ActorReferenceData: MovieSceneActorReferenceData
    ActorGuidIndexCurve: engine.IntegralCurve
    ActorGuidStrings: unreal.WrappedArray[str]


class MovieSceneActorReferenceTrack(MovieScenePropertyTrack): ...


class MovieSceneAudioSection(movie_scene.MovieSceneSection):
    Sound: engine.SoundBase
    StartOffset: float
    AudioStartTime: float
    AudioDilationFactor: float
    AudioVolume: float
    SoundVolume: movie_scene.MovieSceneFloatChannel
    PitchMultiplier: movie_scene.MovieSceneFloatChannel
    bSuppressSubtitles: bool
    bOverrideAttenuation: bool
    AttenuationSettings: engine.SoundAttenuation
    OnQueueSubtitles: Any
    OnAudioFinished: Any
    OnAudioPlaybackPercent: Any


class MovieSceneAudioTrack(movie_scene.MovieSceneNameableTrack):
    AudioSections: unreal.WrappedArray[movie_scene.MovieSceneSection]


class MovieSceneBoolSection(movie_scene.MovieSceneSection):
    DefaultValue: bool
    BoolCurve: movie_scene.MovieSceneBoolChannel


class MovieSceneBoolTrack(MovieScenePropertyTrack): ...


class MovieSceneByteSection(movie_scene.MovieSceneSection):
    ByteCurve: movie_scene.MovieSceneByteChannel


class MovieSceneByteTrack(MovieScenePropertyTrack):
    Enum: unreal.UEnum


class MovieSceneCameraAnimSection(movie_scene.MovieSceneSection):
    AnimData: MovieSceneCameraAnimSectionData
    CameraAnim: engine.CameraAnim
    PlayRate: float
    PlayScale: float
    BlendInTime: float
    BlendOutTime: float
    bLooping: bool


class MovieSceneCameraAnimTrack(movie_scene.MovieSceneNameableTrack):
    CameraAnimSections: unreal.WrappedArray[movie_scene.MovieSceneSection]


class MovieSceneCameraCutSection(movie_scene.MovieSceneSection):
    CameraGuid: core_uobject.Guid
    CameraBindingID: movie_scene.MovieSceneObjectBindingID


class MovieSceneCameraCutTrack(movie_scene.MovieSceneNameableTrack):
    Sections: unreal.WrappedArray[movie_scene.MovieSceneSection]


class MovieSceneCameraShakeSection(movie_scene.MovieSceneSection):
    ShakeData: MovieSceneCameraShakeSectionData
    ShakeClass: unreal.UClass
    PlayScale: float
    PlaySpace: int
    UserDefinedPlaySpace: core_uobject.Rotator


class MovieSceneCameraShakeTrack(movie_scene.MovieSceneNameableTrack):
    CameraShakeSections: unreal.WrappedArray[movie_scene.MovieSceneSection]


class MovieSceneCinematicShotSection(movie_scene.MovieSceneSubSection):
    ShotDisplayName: str
    DisplayName: str


class MovieSceneCinematicShotTrack(movie_scene.MovieSceneSubTrack): ...


class MovieSceneColorSection(movie_scene.MovieSceneSection):
    RedCurve: movie_scene.MovieSceneFloatChannel
    GreenCurve: movie_scene.MovieSceneFloatChannel
    BlueCurve: movie_scene.MovieSceneFloatChannel
    AlphaCurve: movie_scene.MovieSceneFloatChannel


class MovieSceneColorTrack(MovieScenePropertyTrack):
    bIsSlateColor: bool


class MovieSceneEnumSection(movie_scene.MovieSceneSection):
    EnumCurve: movie_scene.MovieSceneByteChannel


class MovieSceneEnumTrack(MovieScenePropertyTrack):
    Enum: unreal.UEnum


class MovieSceneEulerTransformTrack(MovieScenePropertyTrack): ...


class MovieSceneEventSection(movie_scene.MovieSceneSection):
    Events: engine.NameCurve
    EventData: MovieSceneEventSectionData


class MovieSceneEventTrack(movie_scene.MovieSceneNameableTrack):
    bFireEventsWhenForwards: bool
    bFireEventsWhenBackwards: bool
    EventPosition: EFireEventsAtPosition
    EventReceivers: unreal.WrappedArray[movie_scene.MovieSceneObjectBindingID]
    Sections: unreal.WrappedArray[movie_scene.MovieSceneSection]


class MovieSceneFloatSection(movie_scene.MovieSceneSection):
    FloatCurve: movie_scene.MovieSceneFloatChannel


class MovieSceneFadeSection(MovieSceneFloatSection):
    FadeColor: core_uobject.LinearColor
    bFadeAudio: bool


class MovieSceneFloatTrack(MovieScenePropertyTrack): ...


class MovieSceneFadeTrack(MovieSceneFloatTrack): ...


class MovieSceneFeedbackSection(MovieSceneFloatSection):
    bAffectsCoarseMotor: bool
    bAffectsFineMotor: bool
    bAffectsRightTrigger: bool
    bAffectsLeftTrigger: bool


class MovieSceneFeedbackTrack(movie_scene.MovieSceneNameableTrack):
    Sections: unreal.WrappedArray[movie_scene.MovieSceneSection]


class MovieSceneGbxPlayRateSection(movie_scene.MovieSceneSection):
    PlayRateChannel: movie_scene.MovieSceneFloatChannel
    FrameSnappingChannel: movie_scene.MovieSceneBoolChannel


class MovieSceneGbxPlayRateTrack(MovieScenePropertyTrack): ...


class MovieSceneIntegerSection(movie_scene.MovieSceneSection):
    IntegerCurve: movie_scene.MovieSceneIntegerChannel


class MovieSceneIntegerTrack(MovieScenePropertyTrack): ...


class MovieSceneLevelVisibilitySection(movie_scene.MovieSceneSection):
    Visibility: ELevelVisibility
    LevelNames: unreal.WrappedArray[str]


class MovieSceneLevelVisibilityTrack(movie_scene.MovieSceneNameableTrack):
    Sections: unreal.WrappedArray[movie_scene.MovieSceneSection]


class MovieSceneMaterialTrack(movie_scene.MovieSceneNameableTrack):
    Sections: unreal.WrappedArray[movie_scene.MovieSceneSection]


class MovieSceneMaterialParameterCollectionTrack(MovieSceneMaterialTrack):
    MPC: engine.MaterialParameterCollection


class MovieSceneComponentMaterialTrack(MovieSceneMaterialTrack):
    MaterialIndex: int


class MovieSceneParameterSection(movie_scene.MovieSceneSection):
    ScalarParameterNamesAndCurves: unreal.WrappedArray[ScalarParameterNameAndCurve]
    VectorParameterNamesAndCurves: unreal.WrappedArray[VectorParameterNameAndCurves]
    ColorParameterNamesAndCurves: unreal.WrappedArray[ColorParameterNameAndCurves]
    ActorParameterNamesAndChannels: unreal.WrappedArray[ActorParameterNameAndChannel]


class MovieSceneParticleParameterTrack(movie_scene.MovieSceneNameableTrack):
    Sections: unreal.WrappedArray[movie_scene.MovieSceneSection]


class MovieSceneParticleSection(movie_scene.MovieSceneSection):
    ParticleKeys: MovieSceneParticleChannel


class MovieSceneParticleTrack(movie_scene.MovieSceneNameableTrack):
    ParticleSections: unreal.WrappedArray[movie_scene.MovieSceneSection]


class MovieSceneSkeletalAnimationSection(movie_scene.MovieSceneSection):
    Params: MovieSceneSkeletalAnimationParams
    AnimSequence: engine.AnimSequence
    Animation: engine.AnimSequenceBase
    StartOffset: float
    EndOffset: float
    PlayRate: float
    bReverse: bool
    SlotName: str

    def GetAvailableSlotNames(self, OutSlotNames: unreal.WrappedArray[str]): ...


class MovieSceneSkeletalAnimationTrack(movie_scene.MovieSceneNameableTrack):
    AnimationSections: unreal.WrappedArray[movie_scene.MovieSceneSection]
    bUseLegacySectionIndexBlend: bool


class MovieSceneSlomoSection(MovieSceneFloatSection): ...


class MovieSceneSlomoTrack(MovieSceneFloatTrack): ...


class MovieSceneSpawnSection(MovieSceneBoolSection): ...


class MovieSceneSpawnTrack(movie_scene.MovieSceneTrack):
    Sections: unreal.WrappedArray[movie_scene.MovieSceneSection]
    ObjectGuid: core_uobject.Guid


class MovieSceneStringSection(movie_scene.MovieSceneSection):
    StringCurve: MovieSceneStringChannel


class MovieSceneStringTrack(MovieScenePropertyTrack): ...


class MovieSceneTransformTrack(MovieScenePropertyTrack): ...


class MovieSceneVectorSection(movie_scene.MovieSceneSection):
    Curves: movie_scene.MovieSceneFloatChannel
    ChannelsUsed: int


class MovieSceneVectorTrack(MovieScenePropertyTrack):
    NumChannelsUsed: int


class MovieSceneVisibilityTrack(MovieSceneBoolTrack): ...


class MovieScene3DAttachSectionTemplate(movie_scene.MovieSceneEvalTemplate):
    AttachBindingID: movie_scene.MovieSceneObjectBindingID
    AttachSocketName: str
    AttachComponentName: str
    AttachmentLocationRule: engine.EAttachmentRule
    AttachmentRotationRule: engine.EAttachmentRule
    AttachmentScaleRule: engine.EAttachmentRule
    DetachmentLocationRule: engine.EDetachmentRule
    DetachmentRotationRule: engine.EDetachmentRule
    DetachmentScaleRule: engine.EDetachmentRule


class MovieScene3DPathSectionTemplate(movie_scene.MovieSceneEvalTemplate):
    PathBindingID: movie_scene.MovieSceneObjectBindingID
    TimingCurve: movie_scene.MovieSceneFloatChannel
    FrontAxisEnum: MovieScene3DPathSection_Axis
    UpAxisEnum: MovieScene3DPathSection_Axis
    bFollow: bool
    bReverse: bool
    bForceUpright: bool


class MovieSceneTransformMask:
    Mask: int


class MovieScene3DTransformKeyStruct(movie_scene.MovieSceneKeyStruct):
    Location: core_uobject.Vector
    Rotation: core_uobject.Rotator
    Scale: core_uobject.Vector
    Time: core_uobject.FrameNumber


class MovieScene3DScaleKeyStruct(movie_scene.MovieSceneKeyStruct):
    Scale: core_uobject.Vector
    Time: core_uobject.FrameNumber


class MovieScene3DRotationKeyStruct(movie_scene.MovieSceneKeyStruct):
    Rotation: core_uobject.Rotator
    Time: core_uobject.FrameNumber


class MovieScene3DLocationKeyStruct(movie_scene.MovieSceneKeyStruct):
    Location: core_uobject.Vector
    Time: core_uobject.FrameNumber


class MovieSceneComponentTransformSectionTemplate(movie_scene.MovieSceneEvalTemplate):
    TemplateData: MovieScene3DTransformTemplateData


class MovieScene3DTransformTemplateData:
    TranslationCurve: movie_scene.MovieSceneFloatChannel
    RotationCurve: movie_scene.MovieSceneFloatChannel
    ScaleCurve: movie_scene.MovieSceneFloatChannel
    ManualWeight: movie_scene.MovieSceneFloatChannel
    BlendType: movie_scene.EMovieSceneBlendType
    Mask: MovieSceneTransformMask
    bUseQuaternionInterpolation: bool


class MovieSceneActorReferenceData(movie_scene.MovieSceneChannel):
    KeyTimes: unreal.WrappedArray[core_uobject.FrameNumber]
    KeyValues: unreal.WrappedArray[MovieSceneActorReferenceKey]


class MovieSceneActorReferenceKey:
    Object: movie_scene.MovieSceneObjectBindingID


class MovieSceneActorReferenceSectionTemplate(movie_scene.MovieSceneEvalTemplate):
    PropertyData: movie_scene.MovieScenePropertySectionData
    ActorReferenceData: MovieSceneActorReferenceData


class MovieSceneAudioSectionTemplate(movie_scene.MovieSceneEvalTemplate):
    AudioData: MovieSceneAudioSectionTemplateData


class MovieSceneAudioSectionTemplateData:
    Sound: engine.SoundBase
    AudioStartOffset: float
    SectionStartTimeSeconds: float
    AudioPitchMultiplierCurve: movie_scene.MovieSceneFloatChannel
    AudioVolumeCurve: movie_scene.MovieSceneFloatChannel
    RowIndex: int
    bOverrideAttenuation: bool
    AttenuationSettings: engine.SoundAttenuation
    OnQueueSubtitles: Any
    OnAudioFinished: Any
    OnAudioPlaybackPercent: Any


class MovieSceneCameraAnimSectionData:
    CameraAnim: engine.CameraAnim
    PlayRate: float
    PlayScale: float
    BlendInTime: float
    BlendOutTime: float
    bLooping: bool


class MovieSceneAdditiveCameraAnimationTemplate(movie_scene.MovieSceneEvalTemplate): ...


class MovieSceneCameraShakeSectionTemplate(MovieSceneAdditiveCameraAnimationTemplate):
    SourceData: MovieSceneCameraShakeSectionData
    SectionStartTime: core_uobject.FrameNumber
    CompletionMode: movie_scene.EMovieSceneCompletionMode
    SourceSection: movie_scene.MovieSceneSection


class MovieSceneCameraShakeSectionData:
    ShakeClass: unreal.UClass
    PlayScale: float
    PlaySpace: int
    UserDefinedPlaySpace: core_uobject.Rotator


class MovieSceneCameraAnimSectionTemplate(MovieSceneAdditiveCameraAnimationTemplate):
    SourceData: MovieSceneCameraAnimSectionData
    SectionStartTime: core_uobject.FrameNumber
    CompletionMode: movie_scene.EMovieSceneCompletionMode
    SourceSection: movie_scene.MovieSceneSection


class MovieSceneCameraCutSectionTemplate(movie_scene.MovieSceneEvalTemplate):
    CameraBindingID: movie_scene.MovieSceneObjectBindingID
    CutTransform: core_uobject.Transform
    bHasCutTransform: bool


class MovieSceneColorKeyStruct(movie_scene.MovieSceneKeyStruct):
    Color: core_uobject.LinearColor
    Time: core_uobject.FrameNumber


class MovieSceneColorSectionTemplate(movie_scene.MovieScenePropertySectionTemplate):
    Curves: movie_scene.MovieSceneFloatChannel
    BlendType: movie_scene.EMovieSceneBlendType


class MovieSceneEventSectionData(movie_scene.MovieSceneChannel):
    Times: unreal.WrappedArray[core_uobject.FrameNumber]
    KeyValues: unreal.WrappedArray[EventPayload]


class EventPayload:
    EventName: str
    Parameters: MovieSceneEventParameters


class MovieSceneEventParameters: ...


class MovieSceneEventSectionTemplate(movie_scene.MovieSceneEvalTemplate):
    EventData: MovieSceneEventSectionData
    EventReceivers: unreal.WrappedArray[movie_scene.MovieSceneObjectBindingID]
    bFireEventsWhenForwards: bool
    bFireEventsWhenBackwards: bool


class MovieSceneFadeSectionTemplate(movie_scene.MovieSceneEvalTemplate):
    FadeCurve: movie_scene.MovieSceneFloatChannel
    FadeColor: core_uobject.LinearColor
    bFadeAudio: bool


class MovieSceneFeedbackSectionTemplate(movie_scene.MovieSceneEvalTemplate):
    FloatCurve: movie_scene.MovieSceneFloatChannel
    bAffectsCoarseMotor: bool
    bAffectsFineMotor: bool
    bAffectsRightTrigger: bool
    bAffectsLeftTrigger: bool


class MovieSceneGbxPlayRateSectionTemplate(movie_scene.MovieSceneEvalTemplate):
    PlayRateCurve: movie_scene.MovieSceneFloatChannel
    FrameSnappingCurve: movie_scene.MovieSceneBoolChannel


class MovieSceneLevelVisibilitySectionTemplate(movie_scene.MovieSceneEvalTemplate):
    Visibility: ELevelVisibility
    LevelNames: unreal.WrappedArray[str]


class MovieSceneParameterSectionTemplate(movie_scene.MovieSceneEvalTemplate):
    Scalars: unreal.WrappedArray[ScalarParameterNameAndCurve]
    Vectors: unreal.WrappedArray[VectorParameterNameAndCurves]
    Colors: unreal.WrappedArray[ColorParameterNameAndCurves]
    Actors: unreal.WrappedArray[ActorParameterNameAndChannel]


class ActorParameterNameAndChannel:
    ParameterName: str
    Channel: MovieSceneActorReferenceData


class ColorParameterNameAndCurves:
    ParameterName: str
    RedCurve: movie_scene.MovieSceneFloatChannel
    GreenCurve: movie_scene.MovieSceneFloatChannel
    BlueCurve: movie_scene.MovieSceneFloatChannel
    AlphaCurve: movie_scene.MovieSceneFloatChannel


class VectorParameterNameAndCurves:
    ParameterName: str
    XCurve: movie_scene.MovieSceneFloatChannel
    YCurve: movie_scene.MovieSceneFloatChannel
    ZCurve: movie_scene.MovieSceneFloatChannel


class ScalarParameterNameAndCurve:
    ParameterName: str
    ParameterCurve: movie_scene.MovieSceneFloatChannel


class MovieSceneMaterialParameterCollectionTemplate(MovieSceneParameterSectionTemplate):
    MPC: engine.MaterialParameterCollection


class MovieSceneComponentMaterialSectionTemplate(MovieSceneParameterSectionTemplate):
    MaterialIndex: int


class MovieSceneParticleParameterSectionTemplate(
    MovieSceneParameterSectionTemplate
): ...


class MovieSceneParticleChannel(movie_scene.MovieSceneByteChannel): ...


class MovieSceneParticleSectionTemplate(movie_scene.MovieSceneEvalTemplate):
    ParticleKeys: MovieSceneParticleChannel


class MovieSceneEulerTransformPropertySectionTemplate(
    movie_scene.MovieScenePropertySectionTemplate
):
    TemplateData: MovieScene3DTransformTemplateData


class MovieSceneTransformPropertySectionTemplate(
    movie_scene.MovieScenePropertySectionTemplate
):
    TemplateData: MovieScene3DTransformTemplateData


class MovieSceneVectorPropertySectionTemplate(
    movie_scene.MovieScenePropertySectionTemplate
):
    ComponentCurves: movie_scene.MovieSceneFloatChannel
    NumChannelsUsed: int
    BlendType: movie_scene.EMovieSceneBlendType


class MovieSceneStringPropertySectionTemplate(
    movie_scene.MovieScenePropertySectionTemplate
):
    StringCurve: MovieSceneStringChannel


class MovieSceneStringChannel(movie_scene.MovieSceneChannel):
    Times: unreal.WrappedArray[core_uobject.FrameNumber]
    Values: unreal.WrappedArray[str]
    DefaultValue: str
    bHasDefaultValue: bool


class MovieSceneIntegerPropertySectionTemplate(
    movie_scene.MovieScenePropertySectionTemplate
):
    IntegerCurve: movie_scene.MovieSceneIntegerChannel
    BlendType: movie_scene.EMovieSceneBlendType


class MovieSceneEnumPropertySectionTemplate(
    movie_scene.MovieScenePropertySectionTemplate
):
    EnumCurve: movie_scene.MovieSceneByteChannel


class MovieSceneBytePropertySectionTemplate(
    movie_scene.MovieScenePropertySectionTemplate
):
    ByteCurve: movie_scene.MovieSceneByteChannel


class MovieSceneFloatPropertySectionTemplate(
    movie_scene.MovieScenePropertySectionTemplate
):
    FloatFunction: movie_scene.MovieSceneFloatChannel
    BlendType: movie_scene.EMovieSceneBlendType


class MovieSceneBoolPropertySectionTemplate(
    movie_scene.MovieScenePropertySectionTemplate
):
    BoolCurve: movie_scene.MovieSceneBoolChannel


class MovieSceneSkeletalAnimationParams:
    Animation: engine.AnimSequenceBase
    StartOffset: float
    EndOffset: float
    PlayRate: float
    bReverse: bool
    SlotName: str
    bOverrideSlotName: bool
    Weight: movie_scene.MovieSceneFloatChannel
    bSkipAnimNotifiers: bool


class MovieSceneSkeletalAnimationSectionTemplate(movie_scene.MovieSceneEvalTemplate):
    Params: MovieSceneSkeletalAnimationSectionTemplateParameters


class MovieSceneSkeletalAnimationSectionTemplateParameters(
    MovieSceneSkeletalAnimationParams
):
    SectionStartTime: core_uobject.FrameNumber
    SectionEndTime: core_uobject.FrameNumber


class MovieSceneSlomoSectionTemplate(movie_scene.MovieSceneEvalTemplate):
    SlomoCurve: movie_scene.MovieSceneFloatChannel


class MovieSceneSpawnSectionTemplate(movie_scene.MovieSceneEvalTemplate):
    Curve: movie_scene.MovieSceneBoolChannel


class MovieSceneVectorKeyStructBase(movie_scene.MovieSceneKeyStruct):
    Time: core_uobject.FrameNumber


class MovieSceneVector4KeyStruct(MovieSceneVectorKeyStructBase):
    Vector: core_uobject.Vector4


class MovieSceneVectorKeyStruct(MovieSceneVectorKeyStructBase):
    Vector: core_uobject.Vector


class MovieSceneVector2DKeyStruct(MovieSceneVectorKeyStructBase):
    Vector: core_uobject.Vector2D


class MovieSceneVisibilitySectionTemplate(MovieSceneBoolPropertySectionTemplate): ...


class MovieScene3DPathSection_Axis(enum.Enum):
    Y = 0
    Z = 1
    NEG_Y = 2


class EFireEventsAtPosition(enum.Enum):
    AtEndOfEvaluation = 0
    AfterSpawn = 1


class ELevelVisibility(enum.Enum):
    Hidden = 0
    ELevelVisibility_MAX = 1


class EParticleKey(enum.Enum):
    Trigger = 0
    Deactivate = 1

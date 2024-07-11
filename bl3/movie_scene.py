from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine


class MovieSceneSignedObject(unreal.UObject):
    Signature: core_uobject.Guid


class MovieSceneTrack(MovieSceneSignedObject):
    EvalOptions: MovieSceneTrackEvalOptions


class MovieSceneNameableTrack(MovieSceneTrack): ...


class MovieSceneSection(MovieSceneSignedObject):
    EvalOptions: MovieSceneSectionEvalOptions
    Easing: MovieSceneEasingSettings
    SectionRange: MovieSceneFrameRange
    PreRollFrames: core_uobject.FrameNumber
    PostRollFrames: core_uobject.FrameNumber
    RowIndex: int
    OverlapPriority: int
    bIsActive: bool
    bIsLocked: bool
    StartTime: float
    EndTime: float
    PrerollTime: float
    PostrollTime: float
    bIsInfinite: bool
    bSupportsInfiniteRange: bool
    BlendType: OptionalMovieSceneBlendType


class MovieSceneSequence(MovieSceneSignedObject):
    PrecompiledEvaluationTemplate: MovieSceneEvaluationTemplate
    DefaultCompletionMode: EMovieSceneCompletionMode
    bParentContextsAreSignificant: bool
    bDisableURO: bool


class MovieSceneSequencePlayer(unreal.UObject):
    OnPlay: Any
    OnPlayReverse: Any
    OnStop: Any
    OnPause: Any
    OnFinished: Any
    Status: int
    bReversePlayback: bool
    Sequence: MovieSceneSequence
    StartTime: core_uobject.FrameNumber
    DurationFrames: int
    CurrentNumLoops: int
    PlaybackSettings: MovieSceneSequencePlaybackSettings

    def Stop(self): ...
    def SetTimeRange(self, StartTime: float, Duration: float): ...
    def SetPlayRate(self, PlayRate: float): ...
    def SetPlaybackRange(self, NewStartTime: float, NewEndTime: float): ...
    def SetPlaybackPosition(self, NewPlaybackPosition: float): ...
    def SetFrameRate(self, FrameRate: core_uobject.FrameRate): ...
    def SetFrameRange(self, StartFrame: int, Duration: int): ...
    def SetEnableUpdateRateOptimizations(self, Enable: bool): ...
    def SetDisableCameraCuts(self, bInDisableCameraCuts: bool): ...
    def ScrubToSeconds(self, TimeInSeconds: float): ...
    def ScrubToFrame(self, NewPosition: core_uobject.FrameTime): ...
    def Scrub(self): ...
    def PlayToSeconds(self, TimeInSeconds: float): ...
    def PlayToFrame(self, NewPosition: core_uobject.FrameTime): ...
    def PlayReverse(self): ...
    def PlayLooping(self, NumLoops: int): ...
    def Play(self): ...
    def Pause(self): ...
    def JumpToSeconds(self, TimeInSeconds: float): ...
    def JumpToPosition(self, NewPlaybackPosition: float): ...
    def JumpToFrame(self, NewPosition: core_uobject.FrameTime): ...
    def IsReversed(self) -> bool: ...
    def IsPlaying(self) -> bool: ...
    def IsPaused(self) -> bool: ...
    def GoToEndAndStop(self): ...
    def GetStartTime(self) -> core_uobject.QualifiedFrameTime: ...
    def GetPlayRate(self) -> float: ...
    def GetPlaybackStart(self) -> float: ...
    def GetPlaybackPosition(self) -> float: ...
    def GetPlaybackEnd(self) -> float: ...
    def GetLength(self) -> float: ...
    def GetFrameRate(self) -> core_uobject.FrameRate: ...
    def GetFrameDuration(self) -> int: ...
    def GetEndTime(self) -> core_uobject.QualifiedFrameTime: ...
    def GetEnableUpdateRateOptimizations(self) -> bool: ...
    def GetDuration(self) -> core_uobject.QualifiedFrameTime: ...
    def GetDisableCameraCuts(self) -> bool: ...
    def GetCurrentTime(self) -> core_uobject.QualifiedFrameTime: ...
    def GetBoundObjects(
        self, ObjectBinding: MovieSceneObjectBindingID
    ) -> unreal.WrappedArray[unreal.UObject]: ...
    def ChangePlaybackDirection(self): ...


class MovieSceneBindingOverrides(unreal.UObject):
    BindingData: unreal.WrappedArray[MovieSceneBindingOverrideData]


class MovieScene(MovieSceneSignedObject):
    Spawnables: unreal.WrappedArray[MovieSceneSpawnable]
    Possessables: unreal.WrappedArray[MovieScenePossessable]
    ObjectBindings: unreal.WrappedArray[MovieSceneBinding]
    MasterTracks: unreal.WrappedArray[MovieSceneTrack]
    CameraCutTrack: MovieSceneTrack
    SelectionRange: MovieSceneFrameRange
    PlaybackRange: MovieSceneFrameRange
    TickResolution: core_uobject.FrameRate
    DisplayRate: core_uobject.FrameRate
    EvaluationType: EMovieSceneEvaluationType
    ClockSource: EUpdateClockSource
    DisableFrameSnapping: bool


class MovieSceneBindingOverridesInterface(core_uobject.Interface): ...


class MovieSceneBindingOwnerInterface(core_uobject.Interface): ...


class MovieSceneBuiltInEasingFunction(unreal.UObject):
    Type: EMovieSceneBuiltInEasing


class MovieSceneEasingExternalCurve(unreal.UObject):
    Curve: engine.CurveFloat


class MovieSceneEasingFunction(core_uobject.Interface):

    def OnEvaluate(self, Interp: float) -> float: ...


class MovieSceneFolder(unreal.UObject):
    FolderName: str
    ChildFolders: unreal.WrappedArray[MovieSceneFolder]
    ChildMasterTracks: unreal.WrappedArray[MovieSceneTrack]
    ChildObjectBindingStrings: unreal.WrappedArray[str]


class MovieSceneKeyProxy(core_uobject.Interface): ...


class MovieSceneSegmentCompilerTestTrack(MovieSceneTrack):
    bHighPassFilter: bool
    SectionArray: unreal.WrappedArray[MovieSceneSection]


class MovieSceneSegmentCompilerTestSection(MovieSceneSection): ...


class MovieSceneSubSection(MovieSceneSection):
    Parameters: MovieSceneSectionParameters
    StartOffset: float
    TimeScale: float


class MovieSceneSubTrack(MovieSceneNameableTrack):
    Sections: unreal.WrappedArray[MovieSceneSection]


class MovieSceneEvalTemplateBase: ...


class MovieSceneEvalTemplate(MovieSceneEvalTemplateBase):
    CompletionMode: EMovieSceneCompletionMode
    SourceSection: MovieSceneSection


class MovieSceneTrackLabels:
    Strings: unreal.WrappedArray[str]


class MovieSceneEditorData:
    ExpansionStates: Any
    ViewStart: float
    ViewEnd: float
    WorkStart: float
    WorkEnd: float
    WorkingRange: core_uobject.FloatRange
    ViewRange: core_uobject.FloatRange


class MovieSceneExpansionState:
    bExpanded: bool


class MovieSceneTimecodeSource:
    Timecode: core_uobject.Timecode
    DeltaFrame: core_uobject.FrameNumber


class MovieSceneBinding:
    ObjectGuid: core_uobject.Guid
    BindingName: str
    Tracks: unreal.WrappedArray[MovieSceneTrack]


class MovieSceneBindingOverrideData:
    ObjectBindingId: MovieSceneObjectBindingID
    Object: unreal.UObject
    bOverridesDefault: bool


class MovieSceneObjectBindingID:
    SequenceID: int
    Space: EMovieSceneObjectBindingSpace
    Guid: core_uobject.Guid


class OptionalMovieSceneBlendType:
    BlendType: EMovieSceneBlendType
    bIsValid: bool


class MovieSceneChannel: ...


class MovieSceneBoolChannel(MovieSceneChannel):
    Times: unreal.WrappedArray[core_uobject.FrameNumber]
    DefaultValue: bool
    bHasDefaultValue: bool
    Values: unreal.WrappedArray[bool]


class MovieSceneByteChannel(MovieSceneChannel):
    Times: unreal.WrappedArray[core_uobject.FrameNumber]
    DefaultValue: int
    bHasDefaultValue: bool
    Values: unreal.WrappedArray[int]
    Enum: unreal.UEnum


class MovieSceneKeyHandleMap(engine.KeyHandleLookupTable): ...


class MovieSceneEvalTemplatePtr: ...


class MovieSceneEmptyStruct: ...


class MovieSceneEvaluationField:
    Ranges: unreal.WrappedArray[MovieSceneFrameRange]
    Groups: unreal.WrappedArray[MovieSceneEvaluationGroup]
    MetaData: unreal.WrappedArray[MovieSceneEvaluationMetaData]


class MovieSceneEvaluationMetaData:
    ActiveSequences: unreal.WrappedArray[MovieSceneSequenceID]
    ActiveEntities: unreal.WrappedArray[MovieSceneOrderedEvaluationKey]
    SubTemplateSerialNumbers: Any


class MovieSceneSequenceID:
    Value: int


class MovieSceneOrderedEvaluationKey:
    Key: MovieSceneEvaluationKey
    EvaluationIndex: int


class MovieSceneEvaluationKey:
    SequenceID: MovieSceneSequenceID
    TrackIdentifier: MovieSceneTrackIdentifier
    SectionIndex: int


class MovieSceneTrackIdentifier:
    Value: int


class MovieSceneEvaluationGroup:
    LUTIndices: unreal.WrappedArray[MovieSceneEvaluationGroupLUTIndex]
    SegmentPtrLUT: unreal.WrappedArray[MovieSceneEvaluationFieldSegmentPtr]


class MovieSceneEvaluationFieldTrackPtr:
    SequenceID: MovieSceneSequenceID
    TrackIdentifier: MovieSceneTrackIdentifier


class MovieSceneEvaluationFieldSegmentPtr(MovieSceneEvaluationFieldTrackPtr):
    SegmentID: MovieSceneSegmentIdentifier


class MovieSceneSegmentIdentifier:
    IdentifierIndex: int


class MovieSceneEvaluationGroupLUTIndex:
    LUTOffset: int
    NumInitPtrs: int
    NumEvalPtrs: int


class MovieSceneFrameRange: ...


class MovieSceneEvaluationOperand:
    ObjectBindingId: core_uobject.Guid
    SequenceID: MovieSceneSequenceID


class MovieSceneEvaluationTemplate:
    Tracks: Any
    EvaluationField: MovieSceneEvaluationField
    Hierarchy: MovieSceneSequenceHierarchy
    SequenceSignature: core_uobject.Guid
    TemplateSerialNumber: MovieSceneEvaluationTemplateSerialNumber
    TemplateLedger: MovieSceneTemplateGenerationLedger
    TrackFieldData: MovieSceneTrackFieldData
    SubSectionFieldData: MovieSceneSubSectionFieldData


class MovieSceneSubSectionFieldData: ...


class MovieSceneTrackFieldData: ...


class MovieSceneTemplateGenerationLedger:
    LastTrackIdentifier: MovieSceneTrackIdentifier
    TrackSignatureToTrackIdentifier: Any
    SubSectionRanges: Any


class MovieSceneEvaluationTemplateSerialNumber:
    Value: int


class MovieSceneSequenceHierarchy:
    SubSequences: Any
    Hierarchy: Any


class MovieSceneSequenceHierarchyNode:
    ParentId: MovieSceneSequenceID
    Children: unreal.WrappedArray[MovieSceneSequenceID]


class MovieSceneSubSequenceData:
    Sequence: core_uobject.SoftObjectPath
    RootToSequenceTransform: MovieSceneSequenceTransform
    TickResolution: core_uobject.FrameRate
    DeterministicSequenceID: MovieSceneSequenceID
    PlayRange: MovieSceneFrameRange
    PreRollRange: MovieSceneFrameRange
    PostRollRange: MovieSceneFrameRange
    HierarchicalBias: int
    InstanceData: MovieSceneSequenceInstanceDataPtr
    SubSectionSignature: core_uobject.Guid
    OuterToInnerTransform: MovieSceneSequenceTransform


class MovieSceneSequenceTransform:
    TimeScale: float
    Offset: core_uobject.FrameTime


class MovieSceneSequenceInstanceDataPtr: ...


class MovieSceneEvaluationTrack:
    ObjectBindingId: core_uobject.Guid
    EvaluationPriority: int
    EvaluationMethod: EEvaluationMethod
    Segments: MovieSceneEvaluationTrackSegments
    SourceTrack: MovieSceneTrack
    EvaluationTree: SectionEvaluationDataTree
    ChildTemplates: unreal.WrappedArray[MovieSceneEvalTemplatePtr]
    TrackTemplate: MovieSceneTrackImplementationPtr
    EvaluationGroup: str
    bEvaluateInPreroll: bool
    bEvaluateInPostroll: bool


class MovieSceneTrackImplementationPtr: ...


class SectionEvaluationDataTree: ...


class MovieSceneEvaluationTrackSegments:
    SegmentIdentifierToIndex: unreal.WrappedArray[int]
    SortedSegments: unreal.WrappedArray[MovieSceneSegment]


class MovieSceneSegment: ...


class MovieSceneSubSectionData:
    Section: MovieSceneSubSection
    ObjectBindingId: core_uobject.Guid
    Flags: ESectionEvaluationFlags


class MovieSceneFloatChannel(MovieSceneChannel):
    PreInfinityExtrap: int
    PostInfinityExtrap: int
    Times: unreal.WrappedArray[core_uobject.FrameNumber]
    Values: unreal.WrappedArray[MovieSceneFloatValue]
    DefaultValue: float
    bHasDefaultValue: bool
    KeyHandles: MovieSceneKeyHandleMap
    TickResolution: core_uobject.FrameRate


class MovieSceneFloatValue:
    Value: float
    InterpMode: int
    TangentMode: int
    Tangent: MovieSceneTangentData


class MovieSceneTangentData:
    ArriveTangent: float
    LeaveTangent: float
    TangentWeightMode: int
    ArriveTangentWeight: float
    LeaveTangentWeight: float


class MovieSceneIntegerChannel(MovieSceneChannel):
    Times: unreal.WrappedArray[core_uobject.FrameNumber]
    DefaultValue: int
    bHasDefaultValue: bool
    Values: unreal.WrappedArray[int]


class MovieSceneKeyStruct: ...


class MovieSceneKeyTimeStruct(MovieSceneKeyStruct):
    Time: core_uobject.FrameNumber


class MovieScenePossessable:
    Tags: unreal.WrappedArray[str]
    Guid: core_uobject.Guid
    Name: str
    PossessedObjectClass: unreal.UClass
    ParentGuid: core_uobject.Guid


class MovieScenePropertySectionTemplate(MovieSceneEvalTemplate):
    PropertyData: MovieScenePropertySectionData


class MovieScenePropertySectionData:
    PropertyName: str
    PropertyPath: str
    FunctionName: str
    NotifyFunctionName: str


class MovieSceneEasingSettings:
    AutoEaseInDuration: int
    AutoEaseOutDuration: int
    EaseIn: Any
    bManualEaseIn: bool
    ManualEaseInDuration: int
    EaseOut: Any
    bManualEaseOut: bool
    ManualEaseOutDuration: int


class MovieSceneSectionEvalOptions:
    bCanEditCompletionMode: bool
    CompletionMode: EMovieSceneCompletionMode


class MovieSceneSectionParameters:
    StartFrameOffset: core_uobject.FrameNumber
    TimeScale: float
    HierarchicalBias: int
    StartOffset: float
    PrerollTime: float
    PostrollTime: float


class SectionEvaluationData:
    ImplIndex: int
    ForcedTime: core_uobject.FrameNumber
    Flags: ESectionEvaluationFlags


class TestMovieSceneEvalTemplate(MovieSceneEvalTemplate): ...


class MovieSceneSequenceInstanceData: ...


class MovieSceneSequencePlaybackSettings:
    LoopCount: int
    PlayRate: float
    bRandomStartTime: bool
    StartTime: float
    bRestoreState: bool
    bDisableMovementInput: bool
    bDisableLookAtInput: bool
    bHidePlayer: bool
    bHideHud: bool
    bDisableCameraCuts: bool
    bPauseAtEnd: bool
    InstanceData: unreal.UObject
    BindingOverrides: Any
    bAllowUpdateRateOptimizations: bool


class MovieSceneSpawnable:
    SpawnTransform: core_uobject.Transform
    Tags: unreal.WrappedArray[str]
    Guid: core_uobject.Guid
    Name: str
    ObjectTemplate: unreal.UObject
    ChildPossessables: unreal.WrappedArray[core_uobject.Guid]
    Ownership: ESpawnOwnership
    LevelName: str


class MovieSceneTrackEvalOptions:
    bCanEvaluateNearestSection: bool
    bEvalNearestSection: bool
    bEvaluateInPreroll: bool
    bEvaluateInPostroll: bool
    bEvaluateNearestSection: bool


class MovieSceneTrackImplementation(MovieSceneEvalTemplateBase): ...


class EMovieSceneKeyInterpolation(enum.Enum):
    User = 0
    Break = 1
    Constant = 2


class EMovieSceneBlendType(enum.Enum):
    Absolute = 0
    Relative = 1
    Additive = 2


class EMovieSceneBuiltInEasing(enum.Enum):
    SinIn = 0
    SinOut = 1
    QuadIn = 2
    CubicOut = 3
    ExpoIn = 4


class EEvaluationMethod(enum.Enum):
    Swept = 0
    EEvaluationMethod_MAX = 1


class EUpdateClockSource(enum.Enum):
    Platform = 0
    Audio = 1


class EMovieSceneEvaluationType(enum.Enum):
    EMovieSceneEvaluationType_MAX = 0
    WithSubFrames = 1


class EMovieScenePlayerStatus(enum.Enum):
    Playing = 0
    Recording = 1
    Jumping = 2


class EMovieSceneObjectBindingSpace(enum.Enum):
    Root = 0
    EMovieSceneObjectBindingSpace_MAX = 1


class EMovieSceneCompletionMode(enum.Enum):
    RestoreState = 0
    ProjectDefault = 1


class ESectionEvaluationFlags(enum.Enum):
    PreRoll = 0
    PostRoll = 1


class ESpawnOwnership(enum.Enum):
    External = 0
    MasterSequence = 1

from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import gbx_runtime
from . import wwise_audio
from . import movie_scene
from . import gbx_game_system_core


class AnimNotify_DialogEvent(engine.AnimNotify):
    DialogEvent: DialogEvent
    ParameterValues: Any


class CharacterEchoDataBase(gbx_runtime.GbxDataAsset):
    AvailableVoGMoodKeyframes: unreal.WrappedArray[str]


class DialogActionBlueprintImplementation(gbx_runtime.GbxDataAsset):

    def Execute(self, Context: DialogContext): ...


class GbxDialogDataAsset(gbx_runtime.GbxDataAsset):
    Guid: core_uobject.Guid


class DialogActionFunction(GbxDialogDataAsset):
    Parameters: unreal.WrappedArray[DialogParameter]
    BlueprintImplementation: unreal.UClass


class DialogAudioComponentProvider(unreal.UObject): ...


class DialogAudioComponentProvider_OcclusionResistant(DialogAudioComponentProvider):
    OcclusionWeight: float
    ComponentTag: str


class DialogBehaviorPreset(gbx_runtime.GbxDataAsset): ...


class DialogBlackboard(unreal.UObject):
    DistributedSpeakers: Any
    PlayingSequenceDelegates: Any
    LookupSystem: DialogLookupSystem
    ControlSystem: DialogControlSystem
    RegisteredSpeakers: unreal.WrappedArray[GbxDialogComponent]
    ActiveScripts: unreal.WrappedArray[DialogScriptData]
    ActivePureEchoNameTags: Any
    PinnedScriptRefCounts: Any
    CounterValues: Any
    PureEchoSpeakerHost: engine.Actor
    ConversationForDialogLookup: DialogConversation
    SuggestedPlayerForNextConversation: engine.PlayerController
    SuggestedKeyActorForNextConversation: engine.Actor
    SuggestedKeyLocationForNextConversation: core_uobject.Vector
    RecentConversationInfo: Any
    RecentPerformances: Any


class QuietTimePredicate(unreal.UObject): ...


class QuietTimePredicate_BlockStuff(QuietTimePredicate):
    BlockDialogScopeObjects: unreal.WrappedArray[unreal.UObject]
    BlockKinds: unreal.WrappedArray[str]
    BlockStyles: unreal.WrappedArray[DialogStyle]
    OnlyForCharacter: DialogNameTag


class DialogControlSystem(unreal.UObject):
    DialogThreads: unreal.WrappedArray[DialogThread]
    ActiveQuietTimes: unreal.WrappedArray[QuietTimeTracker]
    LookupSystem: DialogLookupSystem
    Blackboard: DialogBlackboard
    Settings: GbxDialogSettings
    World: engine.World
    bFakePauseMode: bool
    bInCinematicMode: bool
    PauseModeLastFrameTime: float


class DialogEnumType(GbxDialogDataAsset): ...


class DialogEnumValue(GbxDialogDataAsset):
    EnumType: DialogEnumType
    UIName: gbx_game_system_core.GbxUIName
    bRestrictedQualifier: bool


class DialogEnumValueInterface(core_uobject.Interface):

    def GetEnumValue(self, EnumType: DialogEnumType) -> DialogEnumValue: ...


class DialogEvent(GbxDialogDataAsset):
    Parameters: unreal.WrappedArray[DialogParameter]
    PerformanceNotifyNames: unreal.WrappedArray[str]


class DialogEventList(GbxDialogDataAsset): ...


class DialogLineData(GbxDialogDataAsset):
    ScorePriorityMode: ELineScorePriorityMode
    Weight: float
    SelectionConditions: unreal.WrappedArray[DialogSelectionCondition]
    SpeakingCharacter: DialogEnumValue
    CharacterQualifier: DialogEnumValue
    Performances: unreal.WrappedArray[DialogPerformanceData]
    VoGMoodKey: str
    FollowupTimeSlot: DialogTimeSlotReference
    FollowupEvent: DialogEvent
    FollowupParameterMappings: unreal.WrappedArray[DialogParameterMapping]
    bSequential: bool


class DialogLookupSystem(unreal.UObject):
    ControlSystem: DialogControlSystem
    Blackboard: DialogBlackboard
    EventTriggeringDecisionTrees: Any
    ConditionTriggeringDecisionTree: DialogDecisionTree
    ActiveScriptRegistrationIDs: Any


class DialogNameTagMoodData(gbx_runtime.GbxDataAsset):
    MoodData: Any


class DialogNameTag(gbx_runtime.GbxDataAsset):
    NameTagEnumValue: DialogEnumValue
    SupportedQualifiers: unreal.WrappedArray[DialogEnumValue]
    ParentNameTag: DialogNameTag
    VoGSpeaker: EVoiceOfGodSpeaker
    EchoData: CharacterEchoDataBase
    ConditionalAlternateEchoData: unreal.WrappedArray[ConditionalEchoData]
    bUsableForPureEchoes: bool
    bDistributedSpeaker: bool
    VoicePitchOffset: int
    CustomizationRTPC: wwise_audio.WwiseRtpc
    CustomizationRTPCValue: float
    MoodDataAsset: DialogNameTagMoodData
    MoodData: Any


class DialogParameter(GbxDialogDataAsset):
    DefaultInputParameter: DialogParameter
    Type: DialogParameterType
    bForceDecisionsToAlwaysRetest: bool


class DialogPerformanceData(GbxDialogDataAsset):
    Text: str
    TriggerPlayWwiseEventPreview: gbx_runtime.GbxTriggerProperty
    WwiseEvent: wwise_audio.WwiseEvent
    WwiseExternalMediaTemplate: wwise_audio.WwiseEvent
    EstimatedDuration: float
    WwiseEventShortID: int
    Action: unreal.UClass
    ActionWeight: float
    MoodName: str
    MoodWeight: float
    bEnableEarlyFinish: bool
    EarlyFinishTimeFraction: float
    Notifies: unreal.WrappedArray[DialogPerformanceNotify]
    Style: DialogStyle
    OutputDelay: float
    ChanceToPlay: float
    QuietTime: core_uobject.FloatInterval
    QuietTimeScope: EGbxDialogQuietTimeScope
    DialogKindCooldownTime: core_uobject.FloatInterval
    EchoData: PerformanceEchoDataBase

    def PlayWwiseEventPreview(self): ...


class DialogScriptData(GbxDialogDataAsset):
    TimeSlots: unreal.WrappedArray[DialogTimeSlotData]
    PureEchoNameTags: unreal.WrappedArray[DialogNameTag]
    EventTriggeredDecisionTrees: Any
    OtherConditionTriggeredDecisionTree: DialogDecisionTree
    FaceFXAnimSet: unreal.UObject


class DialogSelectorFunction(GbxDialogDataAsset):
    Parameters: unreal.WrappedArray[DialogParameter]
    bTriggeringCondition: bool
    CachedResultLifetime: ECachedResultLifetime
    Implementation: DialogSelectorImplementation


class DialogSelectorImplementation(unreal.UObject):

    def PerformTest(
        self, Context: DialogContext, Result: EDialogDecisionTestResult
    ): ...


class DialogSelectorImplementation_CheckDistance(DialogSelectorImplementation):
    FromActorParam: DialogParameter
    ToActorParam: DialogParameter
    bUseCustomDistance: bool
    CustomDistance: float
    bTrueIfCloser: bool


class DialogSelectorImplementation_CheckNameTag(DialogSelectorImplementation):
    WhoParam: DialogParameter
    NameTagParam: DialogParameter


class DialogSelectorImplementation_Equality(DialogSelectorImplementation):
    ParamA: DialogParameter
    ParamB: DialogParameter


class DialogSelectorImplementation_IsPreferredPlayer(DialogSelectorImplementation):
    WhoParam: DialogParameter


class DialogSpeakerInterface(core_uobject.Interface):

    def CanPerformThisDialog(self, Performance: DialogPerformanceData) -> bool: ...


class DialogStyle(gbx_runtime.GbxDataAsset):
    SocialStrategy: EGbxDialogSocialStrategy
    bInterruptSamePriority: bool
    InterruptStrategy: EGbxDialogInterruptStrategy
    Priority: int
    SubtitlePriority: int
    PatientWaitTime: float
    MaxWaitTime: float
    bSpeakableWhenDead: bool
    bInterruptableByHighPriorityVox: bool
    bPlayableWhenPaused: bool
    bPlayableDuringCinematic: bool
    Kind: str
    bCallout: bool
    AudioComponentProvider: DialogAudioComponentProvider
    bLocalOnly: bool


class DialogSystemEchoManagerInterface(core_uobject.Interface): ...


class DialogTimeSlotData(GbxDialogDataAsset):
    TriggerPreviewAudio: gbx_runtime.GbxTriggerProperty
    CompositeAudioAdditionalTimeSlots: unreal.WrappedArray[DialogTimeSlotReference]
    EchoPreference: ETimeSlotEchoPreference
    Parameters: unreal.WrappedArray[DialogParameter]
    Lines: unreal.WrappedArray[DialogLineData]
    DecisionTree: DialogDecisionTree

    def PreviewAudio(self): ...


class GameDialogSystemCustomizationInterface(core_uobject.Interface): ...


class GbxDialogBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def WaitForDialog(
        self, Conversation: DialogConversation, LatentInfo: engine.LatentActionInfo
    ): ...
    def TestDialogSelector(
        self,
        WorldContextObject: unreal.UObject,
        Selector: DialogSelectorFunction,
        InputParameters: DialogContext,
    ) -> bool: ...
    def StopActiveDialog(self, Target: unreal.UObject, bIncludeDeathDialog: bool): ...
    def SetNextDialogPlayerHints(
        self,
        WorldContextObject: unreal.UObject,
        Actor: engine.Actor,
        NameTag: DialogNameTag,
        Location: core_uobject.Vector,
    ): ...
    def SetDialogGameCustomizationMetadata(
        self,
        WorldContextObject: unreal.UObject,
        SequenceID: int,
        Object: unreal.UObject,
        Cookie: int,
    ): ...
    def SetDialogFlag(
        self,
        WorldContextObject: unreal.UObject,
        DialogEnumValue: DialogEnumValue,
        Value: bool,
        Duration: float,
    ): ...
    def SetDialogContextParameter(
        self,
        Context: DialogContext,
        Parameter: DialogParameter,
        ObjectValue: unreal.UObject,
        FloatValue: float,
        bBoolValue: bool,
    ): ...
    def SetConversationPlayerHints(
        self,
        Conversation: DialogConversation,
        Actor: engine.Actor,
        NameTag: DialogNameTag,
        Location: core_uobject.Vector,
    ): ...
    def ResolveDialogTimeSlotReference(
        self,
        Reference: DialogTimeSlotReference,
        TimeSlot: DialogTimeSlotData,
        Script: DialogScriptData,
    ): ...
    def PlaceRegionalDialogHold(
        self,
        WorldContextObject: unreal.UObject,
        HoldName: str,
        Location: core_uobject.Vector,
        Radius: float,
        Rules: QuietTimePredicate,
        Duration: float,
    ): ...
    def PlaceGlobalDialogHold(
        self,
        WorldContextObject: unreal.UObject,
        HoldName: str,
        Rules: QuietTimePredicate,
        Duration: float,
    ): ...
    def NewDialogConversation(
        self,
        WorldContextObject: unreal.UObject,
        KeyActor: engine.Actor,
        KeySpeakerName: DialogNameTag,
        KeyLocation: core_uobject.Vector,
    ) -> DialogConversation: ...
    def NewDialogContext(self) -> DialogContext: ...
    def InterruptDialogInRadius(
        self,
        WorldContextObject: unreal.UObject,
        Origin: core_uobject.Vector,
        Radius: float,
    ): ...
    def InterruptConversation(self, Conversation: DialogConversation): ...
    def GetDialogFlag(
        self, WorldContextObject: unreal.UObject, DialogEnumValue: DialogEnumValue
    ) -> bool: ...
    def GetDialogContextParameterSummary(
        self, Context: DialogContext
    ) -> unreal.WrappedArray[str]: ...
    def GetDialogContextParameter(
        self,
        Context: DialogContext,
        Parameter: DialogParameter,
        ObjectValue: unreal.UObject,
        FloatValue: float,
        bBoolValue: bool,
    ): ...
    def GetConversationStatus(
        self, Conversation: DialogConversation
    ) -> EGbxDialogConversationStatus: ...
    def FinishTriggerDialog(
        self,
        WorldContextObject: unreal.UObject,
        Event: DialogEvent,
        Context: DialogContext,
        ContinueConversation: DialogConversation,
        Conversation: DialogConversation,
        StartDelay: float,
        SequenceID: int,
    ) -> bool: ...
    def FinishSpeak(
        self,
        WorldContextObject: unreal.UObject,
        TimeSlotRef: DialogTimeSlotReference,
        OptionalSpeaker: GbxDialogComponent,
        Context: DialogContext,
        ContinueConversation: DialogConversation,
        Conversation: DialogConversation,
        StartDelay: float,
        SequenceID: int,
        OverrideMaxWait: float,
    ) -> bool: ...
    def FindOrCreateNamedSpeaker(
        self,
        NameTag: DialogNameTag,
        bIncludePureEchoSpeakers: bool,
        bCreateIfNotFound: bool,
        Speaker: GbxDialogComponent,
    ) -> bool: ...
    def EnqueueDialogPerformance(
        self,
        WorldContextObject: unreal.UObject,
        Speaker: GbxDialogComponent,
        Performance: DialogPerformanceData,
        StartDelay: float,
        ContinueConversation: DialogConversation,
        Conversation: DialogConversation,
        DialogPlaybackSequence: int,
    ) -> bool: ...
    def DeactivateDialogScript(
        self,
        WorldContextObject: unreal.UObject,
        SoftScript: Any,
        Script: DialogScriptData,
    ): ...
    def ConvertBoolToDialogTestResult(
        self, bValue: bool
    ) -> EDialogDecisionTestResult: ...
    def CancelDialogBlockingHold(
        self, WorldContextObject: unreal.UObject, HoldName: str
    ): ...
    def BindToDialogSequenceFinished(
        self, WorldContextObject: unreal.UObject, PlayingSequenceID: int, Delegate: Any
    ): ...
    def BindToDialogNotify(
        self,
        WorldContextObject: unreal.UObject,
        PlayingSequenceID: int,
        NotifyName: str,
        Delegate: Any,
    ): ...
    def ActivateDialogScript(
        self,
        WorldContextObject: unreal.UObject,
        SoftScript: Any,
        Script: DialogScriptData,
    ): ...


class GbxDialogComponent(engine.ActorComponent):
    RandomNameTags: unreal.WrappedArray[DialogNameTag]
    DialogScripts: unreal.WrappedArray[DialogScriptData]
    OnStartedPerformance: Any
    NameTag: DialogNameTag
    CurrentPerformance: CurrentDialogPerformanceInfo
    PendingPerformance: CurrentDialogPerformanceInfo
    PinnedScripts: unreal.WrappedArray[DialogScriptPinnedRef]
    bPureEchoSpeaker: bool
    DistributedAudioComponent: wwise_audio.WwiseAudioComponent
    bTransientEchoSpeaker: bool
    TransientEchoSpeakerIdleTime: float
    bSpeakDirectlyToPlayer: bool
    DirectSpeakerTarget: engine.PlayerController
    bPositional: bool
    bDistributedSpeaker: bool
    InitialDialogInProgress: InitialDialogInProgress

    def StopPerformance(self, DialogThreadID: int, bIncludeDeathDialog: bool): ...
    def StartPerformance(
        self,
        DialogThreadID: int,
        DialogSequenceID: int,
        Performance: DialogPerformanceData,
    ): ...
    def OnRep_InitialDialogInProgress(self): ...
    def IsSpeakerClearToPlayDialog(
        self,
        ProposedStyle: DialogStyle,
        bProposingEcho: bool,
        ProposedConversation: DialogConversation,
    ) -> bool: ...
    def IsSpeakerActive(self, bIncludePendingVO: bool) -> bool: ...


class GbxDialogSettings(gbx_runtime.GbxDataAsset):
    PureEchoSpeakerActorClass: unreal.UClass
    GameGlobalParametersProviderClass: unreal.UClass
    BlackboardClass: unreal.UClass
    ConfigurePureEchoTalkerEvent: wwise_audio.WwiseEvent
    EchoControlWwiseParameter: wwise_audio.WwiseRtpc
    PureEchoSpeakerWwiseParameter: wwise_audio.WwiseRtpc
    VoicePitchParameter: wwise_audio.WwiseRtpc
    EnforcedRestrictionQualifiers: unreal.WrappedArray[DialogEnumValue]
    ConversationExpirationDuration: float
    RecentPerformancesExpirationDuration: float
    EmoteWeightBlendDuration: float
    SmallCooldownRadius: float
    NearRadius: float
    QuietTimeMergeRadius: float
    RegionRadius: float
    EnableEchoBelowVolume: float
    DisableEchoAboveVolume: float
    EchoTransitionReqiredVolumeChange: float
    InterConversationDelay: float
    ConfigurationErrorSound: core_uobject.SoftObjectPath
    EventParameter: DialogParameter
    SelfParameter: DialogParameter
    GlobalContextParameter: DialogParameter
    ScriptContextParameter: DialogParameter
    ConversationContextParameter: DialogParameter
    LineContextParameter: DialogParameter
    CountersEnum: DialogEnumType
    FlagsEnum: DialogEnumType


class GlobalDialogParametersProviderInterface(core_uobject.Interface):

    def InitDialogContext(self, Parameters: DialogContext): ...


class MovieSceneDialogTrack(movie_scene.MovieSceneNameableTrack):
    bAllowRename: bool
    Sections: unreal.WrappedArray[movie_scene.MovieSceneSection]


class MovieSceneDialogSection(movie_scene.MovieSceneSection):
    Dialog: DialogTimeSlotReference
    bPlayThroughDialogSystem: bool
    bSubtitleOnly: bool
    ManualSubtitleText: str
    ManualSubtitleDuration: float
    SubtitleNameTag: DialogNameTag


class PerformanceEchoDataBase(gbx_runtime.GbxDataAsset): ...


class PureEchoSpeakerHost(engine.Actor): ...


class DialogParameterValue: ...


class RecentDialogPerformanceInfo:
    ExpirationTime: float
    SequenceID: int
    Speaker: GbxDialogComponent
    Performance: DialogPerformanceData


class RecentConversationInfo:
    ExpirationTime: float
    PreferredPlayer: engine.PlayerController
    LastKeyActor: engine.Actor
    LastKeyLocation: core_uobject.Vector


class DistributedSpeakerInfo:
    DistributedSpeaker: GbxDialogComponent
    RepresentedSpeakers: unreal.WrappedArray[GbxDialogComponent]


class DialogSequenceDelegates:
    OnFinished: Any
    Notifies: Any


class DialogSequenceNotifyDelegate:
    OnNotify: Any


class DialogScriptPinnedRef:
    Blackboard: DialogBlackboard
    Script: DialogScriptData


class DialogBlackboardCounterValueMap:
    Map: Any


class DialogBlackboardFlagValueMap:
    Map: Any


class DialogBlackboardFlagValue: ...


class QuietTimeTracker:
    KeyObject: unreal.UObject
    ScopeObject: unreal.UObject
    ScopePredicate: QuietTimePredicate


class DialogThread:
    Context: DialogContext
    Speaker: GbxDialogComponent
    Performance: DialogPerformanceData
    QuietTimeKey: unreal.UObject
    GameCustomizationObject: unreal.UObject


class DialogContext: ...


class DialogEventSubscription:
    ReferencerTimeSlot: core_uobject.SoftObjectPath


class ConditionalEchoData:
    Condition: gbx_runtime.GbxCondition
    EchoData: CharacterEchoDataBase


class DialogMoodInfo:
    Action: unreal.UClass


class DialogPerformanceNotify:
    TimeFraction: float
    Name: str


class DialogTimeSlotReference:
    Script: Any
    Guid: core_uobject.Guid
    CachedTimeSlot: DialogTimeSlotData


class InitialDialogInProgress:
    DialogThreadID: int
    DialogSequenceID: int
    Performance: DialogPerformanceData
    PlayTime: float


class DialogDecisionTree:
    Decisions: unreal.WrappedArray[DialogLookupDecision]
    Nodes: unreal.WrappedArray[DialogDecisionNode]
    ResultBuckets: unreal.WrappedArray[DialogLookupResultBucket]


class DialogLookupResultBucket:
    Results: unreal.WrappedArray[DialogLookupResult]


class DialogLookupResult:
    Line: DialogLineData
    Quality: int


class DialogDecisionNode:
    Parent: int
    Decision: int
    TrueResultChild: int
    FalseResultChild: int
    UnrelatedResultChild: int
    ResultBucket: int
    MaxChildQuality: int


class DialogLookupDecision:
    Call: DialogSelectorFunctionCallInstance
    CachedLifetime: ECachedResultLifetime
    DecisionNumber: int


class DialogSelectorFunctionCallInstance:
    Function: DialogSelectorFunction
    ParameterMappings: unreal.WrappedArray[DialogParameterMapping]


class DialogParameterMapping:
    TargetParameter: DialogParameter
    SourceType: EDialogParameterMappingSourceType
    SourceObject: unreal.UObject
    SourceObjectSubContext: unreal.UObject
    SourceNumber: float


class DialogSelectionCondition:
    Requirements: unreal.WrappedArray[DialogConditionRequirement]


class DialogConditionRequirement:
    SelectorCall: DialogSelectorFunctionCallInstance
    bRequiredResult: bool


class DialogScopeParameterInfo:
    Target: unreal.UObject
    ParameterMappings: unreal.WrappedArray[DialogParameterMapping]


class DialogParameterType:
    PrimaryType: EDialogParameterPrimaryType
    SecondaryType: DialogEnumType


class CurrentDialogPerformanceInfo:
    DialogThreadID: int
    DialogSequenceID: int
    Performance: DialogPerformanceData
    PlayingAudioInstance: wwise_audio.WwisePlaybackInstance
    bForcingOwnerRelevantForEcho: bool


class DialogConversation:
    ConversationID: int
    ConversationWorld: engine.World


class MovieSceneDialogSectionTemplate(movie_scene.MovieSceneEvalTemplate):
    TemplateData: MovieSceneDialogSectionTemplateData


class MovieSceneDialogSectionTemplateData:
    Dialog: DialogTimeSlotReference
    bPlayThroughDialogSystem: bool
    bSubtitleOnly: bool
    ManualSubtitleText: str
    ManualSubtitleDuration: float
    SubtitleNameTag: DialogNameTag
    RowIdx: int
    SectionStartFrame: core_uobject.FrameNumber
    SectionEndFrame: core_uobject.FrameNumber


class EVoiceOfGodSpeaker(enum.Enum):
    Lilith_Normal = 0
    Tannis_Normal = 1


class ETimeSlotEchoPreference(enum.Enum):
    LiveOnly = 0
    EchoOnly = 1


class ECachedResultLifetime(enum.Enum):
    OneSearch = 0
    ManualReset = 1


class EDialogParameterMappingSourceType(enum.Enum):
    Constant = 0
    EDialogParameterMappingSourceType_MAX = 1
    Counter = 2


class EDialogImplementationStatus(enum.Enum):
    Implemented = 0
    EDialogImplementationStatus_MAX = 1


class EDialogParameterPrimaryType(enum.Enum):
    Boolean = 0
    Object = 1
    Enum = 2


class EGbxDialogQuietTimeScope(enum.Enum):
    SmallArea = 0
    Area = 1


class ELineScorePriorityMode(enum.Enum):
    DiscardLowerScores = 0
    ELineScorePriorityMode_MAX = 1


class EDialogDecisionTestResult(enum.Enum):
    ConditionIsFalse = 0
    TestIsInvalid = 1


class EGbxDialogConversationStatus(enum.Enum):
    Pending = 0
    Canceled = 1
    HoldingConversation = 2


class EGbxDialogInterruptStrategy(enum.Enum):
    SpeakOverOthers = 0
    EGbxDialogInterruptStrategy_MAX = 1


class EGbxDialogSocialStrategy(enum.Enum):
    Selfish = 0
    NonSocial = 1


class EGbxDialogCompileStatus(enum.Enum):
    Dirty = 0
    Error = 1

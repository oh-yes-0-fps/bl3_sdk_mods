from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine
from . import movie_scene



class AudioParametersProviderInterface(core_uobject.Interface): ...


class AudioPositioningProviderInterface(core_uobject.Interface): ...


class InterpTrackInstWwiseAudioEvent(engine.InterpTrackInst):
    LastUpdatePosition: float



class InterpTrackInstWwiseAudioRTPC(engine.InterpTrackInst):
    LastUpdatePosition: float



class InterpTrackWwiseAudioEvent(engine.InterpTrackVectorBase):
    Events: unreal.WrappedArray[WwiseAudioEventTrackKey]
    bContinueEventOnMatineeEnd: bool



class InterpTrackWwiseAudioRTPC(engine.InterpTrackFloatBase):
    RTPC: WwiseRtpc
    bPlayOnReverse: bool
    bContinueRTPCOnMatineeEnd: bool



class MovieSceneWwiseTrack(movie_scene.MovieSceneNameableTrack):
    bAllowRename: bool
    WwiseSections: unreal.WrappedArray[movie_scene.MovieSceneSection]



class MovieSceneWwiseEventSection(movie_scene.MovieSceneSection):
    PlaybackDirection: EWwiseTrackDirectionality
    WwiseEventStart: WwiseEvent
    WwiseEventStop: WwiseEvent
    EmitterRadius: float
    bAllowPlaythrough: bool
    bIsLoopingEvent: bool



class WwiseAmbientSound(engine.Actor):
    AkComponent: WwiseAudioComponent
    WwiseEvent: WwiseEvent
    bStartAutomatically: bool
    ChildEmitters: unreal.WrappedArray[WwiseAmbientSound]
    SuppressEmitters: unreal.WrappedArray[WwiseAmbientSound]
    bOnlyEmitWhenContainingListener: bool
    bOrientToPlayer: bool
    VolumetricEmitterRadius: float
    VolumetricEmitterGain: float
    VolumetricAttenuationRTPC: WwiseRtpc
    VolumetricAttenuationMaxDistance: float
    ExternalActiveRTPCAttenuationPortals: unreal.WrappedArray[WwiseAmbientSound]
    ActiveSuppressors: unreal.WrappedArray[WwiseAmbientSound]
    def ToggleAmbientSound(self): ...
    def StopAmbientSound(self): ...
    def StartAmbientSound(self): ...
    def GetAudioEmitterLocation(self, ListenerLocation: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...


class WwiseAssetSyncDestination(unreal.UObject):
    WwiseObjectID: core_uobject.Guid
    SyncPath: str



class WwiseGameObjectComponent(engine.SceneComponent): ...


class WwiseAudioComponent(WwiseGameObjectComponent):
    OnAttachEvent: WwiseEvent
    OptionalBodySwitchStopEvent: WwiseEvent
    WwiseComponentType: EWwiseAudioComponentType
    EmitterGain: float
    OverrideLocations: unreal.WrappedArray[WwiseLocationOverride]
    bOverrideLocationsAreRelative: bool
    WwiseMixBehavior: EWwiseAudioComponentMixBehavior
    AcousticsMode: EAcousticsMode
    ReverbBoost: float
    PreviousRotationVector: core_uobject.Vector
    MultiPositionType: EWwiseMultiPositionType
    def StopManagedLoop(self, OptionalStopEvent: WwiseEvent): ...
    def StopAll(self): ...
    def StartManagedLoop(self, NewLoopEvent: WwiseEvent): ...
    def SetSwitch(self, WwiseSwitch: WwiseSwitch): ...
    def SetRTPCValue(self, GameParameter: WwiseRtpc, Value: float, ValueChangeDuration: float, FadeCurve: EWwiseCurveInterpolation): ...
    def SetEmitterLocations(self, NewLocations: unreal.WrappedArray[WwiseLocationOverride], MultiPositionType: EWwiseMultiPositionType, bLocationsAreRelative: bool): ...
    def ScaleToRadius(self, Radius: float): ...
    def ScaleAttenuation(self, ScalingFactor: float): ...
    def RegisterRtpcValueCallback(self, CallbackRtpcs: unreal.WrappedArray[WwiseRtpc]): ...
    def PostWwiseEvent(self, WwiseEvent: WwiseEvent, Flags: int, ReturnValue: WwisePlaybackInstance) -> WwisePlaybackInstance: ...
    def PostTrigger(self, Trigger: WwiseTrigger): ...
    def MakeMidiNote(self, NoteNum: int, Velocity: int, Channel: int, Duration: float, StartTime: float, AssociatedEvent: WwiseEvent): ...
    def Jettison(self): ...
    def IsPossiblyAudible(self, WwiseEvent: WwiseEvent, EventAttenuationScale: float, ReturnValue: bool) -> bool: ...
    def IsPlaying(self, ReturnValue: bool) -> bool: ...
    def GetRtpcValue(self, RTPC: WwiseRtpc, ReturnValue: float) -> float: ...
    def GetRadius(self, ReturnValue: float) -> float: ...
    def GetPlayingInstances(self, ReturnValue: unreal.WrappedArray[WwisePlaybackInstance]) -> unreal.WrappedArray[WwisePlaybackInstance]: ...
    def GetMaxAttenuationRadius(self, ReturnValue: float) -> float: ...


class WwiseWorldComponentPool(engine.ActorComponent):
    DesiredPoolSize: int
    CurrentPoolSize: int
    PooledComponents: unreal.WrappedArray[WwiseAudioComponent]



class WwiseAudioComponentPool(engine.ActorComponent):
    MaxPoolSize: int
    PoolMode: EWwiseAudioComponentPoolMode
    bRecycleComponents: bool
    ReservedComponents: unreal.WrappedArray[WwiseAudioComponent]
    ActiveComponents: unreal.WrappedArray[WwiseAudioComponent]
    def GetPooledComponent(self, ReturnValue: WwiseAudioComponent) -> WwiseAudioComponent: ...


class WwiseObject(unreal.UObject): ...


class WwiseEvent(WwiseObject):
    RequiredBank: WwiseBank
    MaxAttenuationRadius: float
    bEcho: bool
    ClosedCaptionName: str
    DurationRange: core_uobject.FloatInterval
    ActionSetSwitches: unreal.WrappedArray[WwiseSwitch]
    bOneShot: bool
    bSimple: bool
    bHighImportance: bool
    bLocalizedVoice: bool
    bUsesSpeedParameter: bool
    bUsesApproachSpeedParameter: bool
    bUsesRotationalSpeedParameter: bool
    bUsesComponentRelativeSpeedParameter: bool
    bUsesPhysicalMaterialSwitch: bool
    bSupportsLiveVoice: bool
    bSupportsEchoVoice: bool
    bEchoWasForcedOff: bool
    bUsesPerspectiveParameter: bool
    PrepareEventRefCount: int
    bPrepareEventDidLoadAllGameSyncs: bool
    def GetMaxDuration(self, ReturnValue: float) -> float: ...


class WwiseAudioInputEvent(WwiseEvent):
    BaseWwiseEvent: WwiseEvent
    OverflowProtectionLimitInFrames: int
    PlayingInstances: unreal.WrappedArray[WwisePlaybackInstance]



class WwiseAuxBus(WwiseObject):
    RequiredBank: WwiseBank



class WwiseBank(WwiseObject):
    bAutoLoad: bool
    MediaSourceBanks: unreal.WrappedArray[WwiseBank]
    bUsesPrepareEvent: bool
    bAutoPrepareEvents: bool



class WwiseAudioEffect(unreal.UObject):
    AuxBus: WwiseAuxBus
    EffectStrengh: float
    def DeactivateEffect(self): ...
    def ActivateEffect(self): ...


class WwiseListenerEnvironmentalEffect(WwiseAudioEffect): ...


class WwiseZoneAudioEffect(WwiseAudioEffect):
    EffectLocation: core_uobject.Vector
    EffectSize: float
    EffectFadeDistance: float



class WwiseEffectProviderInterface(core_uobject.Interface): ...


class WwiseEnvironmentalEffectProvider(core_uobject.Interface): ...


class WwiseExternalSourcesEditorData(engine.DataAsset): ...


class WwiseExternalSourceDebugData(engine.DataAsset): ...


class WwiseGameplayStatics(engine.BlueprintFunctionLibrary):

    def WaitForAudioPlayback(self, PlaybackInstance: WwisePlaybackInstance, LatentInfo: engine.LatentActionInfo): ...
    def WaitForAudioInputConnection(self, WorldContextObject: unreal.UObject, AudioInputEvent: WwiseAudioInputEvent, LatentInfo: engine.LatentActionInfo, MaxWaitTime: float): ...
    def UnloadBank(self, Bank: WwiseBank): ...
    def StopProfilerCapture(self): ...
    def StopOutputCapture(self): ...
    def StopAudio(self, PlaybackInstance: WwisePlaybackInstance, TransitionDuration: float, FadeCurve: EWwiseCurveInterpolation): ...
    def StartProfilerCapture(self, Filename: str): ...
    def StartOutputCapture(self, Filename: str): ...
    def SpawnWwiseComponentAtLocation(self, WorldContextObject: unreal.UObject, Location: core_uobject.Vector, EmitterRadius: float, Orientation: core_uobject.Rotator, IsTemporaryComponent: bool, ReturnValue: WwiseAudioComponent) -> WwiseAudioComponent: ...
    def SpawnAttachedWwiseComponent(self, Actor: engine.Actor, SocketName: str, IsTemporaryComponent: bool, AttachmentComponent: engine.SceneComponent, ReturnValue: WwiseAudioComponent) -> WwiseAudioComponent: ...
    def SetGlobalState(self, State: WwiseState): ...
    def SetGlobalRTPCValue(self, GameParameter: WwiseRtpc, Value: float, TransitionDuration: float, FadeCurve: EWwiseCurveInterpolation): ...
    def SetAudioPlaybackPosition(self, PlaybackInstance: WwisePlaybackInstance, PlaybackPosition: float): ...
    def ResumeAudio(self, PlaybackInstance: WwisePlaybackInstance, TransitionDuration: float, FadeCurve: EWwiseCurveInterpolation): ...
    def PostEventAtMultipleLocations(self, WorldContextObject: unreal.UObject, WwiseEvent: WwiseEvent, NewLocations: unreal.WrappedArray[WwiseLocationOverride], MultiPositionType: EWwiseMultiPositionType, ReturnValue: WwisePlaybackInstance) -> WwisePlaybackInstance: ...
    def PostEventAtLocation(self, WorldContextObject: unreal.UObject, WwiseEvent: WwiseEvent, Location: core_uobject.Vector, EmitterRadius: float, Orientation: core_uobject.Rotator, ReturnValue: WwisePlaybackInstance) -> WwisePlaybackInstance: ...
    def PostAttachedEvent(self, WwiseEvent: WwiseEvent, AttachToActor: engine.Actor, AttachToComponent: engine.SceneComponent, SocketName: str, EmitterRadius: float, ReturnValue: WwisePlaybackInstance) -> WwisePlaybackInstance: ...
    def PauseAudio(self, PlaybackInstance: WwisePlaybackInstance, TransitionDuration: float, FadeCurve: EWwiseCurveInterpolation): ...
    def LoadBank(self, Bank: WwiseBank): ...
    def IsPossiblyAudible(self, WorldContextObject: unreal.UObject, inWwiseEvent: WwiseEvent, Location: core_uobject.Vector, AttenuationScale: float, EmitterRadius: float, ReturnValue: bool) -> bool: ...
    def IsAudioPlaying(self, PlaybackInstance: WwisePlaybackInstance, ReturnValue: bool) -> bool: ...
    def IsAudioPaused(self, PlaybackInstance: WwisePlaybackInstance, ReturnValue: bool) -> bool: ...
    def GetWwiseBankEfficiencyReport(self, ReportData: unreal.WrappedArray[WwiseBankEfficiencyReportDatum]): ...
    def GetPlayingEvent(self, PlaybackInstance: WwisePlaybackInstance, ReturnValue: WwiseEvent) -> WwiseEvent: ...
    def GetEstimatedAudioDuration(self, PlaybackInstance: WwisePlaybackInstance, ReturnValue: float) -> float: ...
    def GetDefaultWwiseComponent(self, Actor: engine.Actor, bCreateIfNotFound: bool, ReturnValue: WwiseAudioComponent) -> WwiseAudioComponent: ...
    def GetClosestListenerLocation(self, WorldContextObject: unreal.UObject, TestPosition: core_uobject.Vector, ClosestLocation: core_uobject.Vector, bSuccess: bool): ...
    def GetAudioPlaybackPosition(self, PlaybackInstance: WwisePlaybackInstance, bExtrapolateSubFrameTime: bool, ReturnValue: float) -> float: ...
    def GetAudioComponentFromPlaybackInstance(self, PlaybackInstance: WwisePlaybackInstance, bCreateIfNotFound: bool, ReturnValue: WwiseAudioComponent) -> WwiseAudioComponent: ...
    def ExecuteActionOnAudioInstance(self, PlaybackInstance: WwisePlaybackInstance, Action: EWwiseEventAction, TransitionDuration: float, FadeCurve: EWwiseCurveInterpolation): ...
    def CreateZoneAudioEffect(self, WorldContextObject: unreal.UObject, AuxBus: WwiseAuxBus, EffectLocation: core_uobject.Vector, EffectSize: float, EffectAttenuationDistance: float, ReturnValue: WwiseZoneAudioEffect) -> WwiseZoneAudioEffect: ...
    def CreateListenerAudioEffect(self, AuxBus: WwiseAuxBus, TargetActor: engine.Actor, WetAmount: float, ReturnValue: WwiseListenerEnvironmentalEffect) -> WwiseListenerEnvironmentalEffect: ...
    def CreateAudioEffect(self, AuxBus: WwiseAuxBus, EffectType: EWwiseEffectType, WetAmount: float, TargetActor: engine.Actor, ReturnValue: WwiseAudioEffect) -> WwiseAudioEffect: ...
    def ConvertLocationsToWwiseLocationOverrides(self, Locations: unreal.WrappedArray[core_uobject.Vector], Orientation: core_uobject.Rotator, Gain: float, Radius: float, ReturnValue: unreal.WrappedArray[WwiseLocationOverride]) -> unreal.WrappedArray[WwiseLocationOverride]: ...
    def AddOutputCaptureMarker(self, MarkerText: str): ...


class WwiseImplementerInterface(core_uobject.Interface): ...


class WwiseListenerComponent(WwiseGameObjectComponent):

    def SetBusRTPCValue(self, GameParameter: WwiseRtpc, Value: float, ValueChangeDuration: float, FadeCurve: EWwiseCurveInterpolation): ...
    def FindAssociatedListener(self, TargetActor: engine.Actor, ReturnValue: WwiseListenerComponent) -> WwiseListenerComponent: ...
    def ConfigureListener(self, WwiseEvent: WwiseEvent): ...


class WwiseMediaAudioSinkProvider(engine.DataAsset):
    AudioInputPlayEvent: WwiseAudioInputEvent
    bAutoPlayOnLocalPlayer: bool



class WwiseRtpc(WwiseObject):
    ValueRange: core_uobject.FloatInterval
    DefaultValue: float



class WwiseSettings(unreal.UObject):
    WwiseWindowsInstallationPath: engine.DirectoryPath
    WwiseMacInstallationPath: engine.FilePath
    WwiseProjectPath: engine.FilePath
    ExternalSourcesDebugData: core_uobject.SoftObjectPath
    pExternalSourcesDebugData: WwiseExternalSourceDebugData
    WorldPoolSize: int
    DefaultPlaybackConfiguration: EWwisePlaybackConfiguration
    DefaultSpeakerAngles: unreal.WrappedArray[float]
    PlaybackConfigurationRtpcName: str
    MinVolumeForCaptionDB: float
    StreamManagerPoolSizeMB: float
    IOMemoryPoolSizeMB: float
    bEnableStreamCache: bool
    DefaultPoolSizeEditorMB: float
    DefaultPoolSizeCookedMB: float
    LowerEngineDefaultPoolSizeMB: float
    MonitorPoolSizeMB: float
    MonitorQueuePoolSizeMB: float
    PrepareEventPoolSizeMB: float
    PrepareEventPoolSizeEditorMB: float
    DefaultPoolLowMemoryModeThreshold: float
    LowerEnginePoolLowMemoryModeThreshold: float
    bEnableHardwareXMADecoding: bool
    APUCachedHeapSizeMB: float
    APUNoncachedHeapSizeMB: float



class WwiseUserSettings(unreal.UObject):
    SpriteSize: EWwiseAudioComponentSpriteSize
    bShowWwiseAudioComponents: bool
    ActiveComponentColor: core_uobject.Color
    HibernatingComponentColor: core_uobject.Color
    ComponentHighlightColor: core_uobject.Color
    SelectionHighlightColor: core_uobject.Color
    SelectionLineThickness: float
    bDrawAudioThresholdManagerDebug: bool



class WwiseState(WwiseObject):
    StateGroup: WwiseStateGroup



class WwiseStateGroup(WwiseObject):
    ChildStates: unreal.WrappedArray[WwiseState]
    NoneState: WwiseState



class WwiseSwitch(WwiseObject):
    SwitchGroup: WwiseSwitchGroup



class WwiseSwitchGroup(WwiseObject):
    ChildSwitches: unreal.WrappedArray[WwiseSwitch]



class WwiseTrigger(WwiseObject): ...


class WwisePlaybackInstance: ...


class WwiseMusicTiming:
    CurrentPositionInBeats: float
    BeatDurationInSeconds: float
    BarLengthInBeats: float
    SegementLengthInBeats: float
    GridLengthInBeats: float



class WwiseAudioEventTrackKey:
    Time: float
    AkAudioEvent: WwiseEvent
    EventName: str



class MovieSceneWwiseSectionTemplate(movie_scene.MovieSceneEvalTemplate):
    TemplateData: MovieSceneWwiseSectionTemplateData



class MovieSceneWwiseSectionTemplateData:
    PlaybackDirection: EWwiseTrackDirectionality
    WwiseEventStart: WwiseEvent
    WwiseEventStop: WwiseEvent
    EmitterRadius: float
    bAllowPlaythrough: bool
    bIsLoopingEvent: bool
    RowIdx: int
    SectionStartFrame: core_uobject.FrameNumber
    SectionEndFrame: core_uobject.FrameNumber
    CachedFrameRate: core_uobject.FrameRate



class WwiseAmbSoundCheckpointRecord:
    bCurrentlyPlaying: bool



class WwiseLocationOverride:
    Location: core_uobject.Vector
    Rotation: core_uobject.Rotator
    Radius: float
    Gain: float



class WwiseEventConfiguration:
    Event: WwiseEvent
    ExternalSourceMedia: unreal.WrappedArray[WwiseExternalSourceMediaInfo]



class WwiseExternalSourceMediaInfo:
    bLocalize: bool



class WwiseEmitterAcousticData:
    DryVolume: float
    ERVolume: float
    LRVolume: float
    LRDuration: float
    DirectionAmbiX: float
    DirectionAmbiY: float



class WwiseEffectInfo:
    EffectID: int
    WetVolume: float
    DryVolume: float



class WwiseEmitter:
    OwnerComponent: WwiseAudioComponent



class WwiseEmitterSource:
    Transform: core_uobject.Transform
    Gain: float



class WwiseExternalAssetData:
    EstimatedDuration: float



class WwiseBankEfficiencyReportDatum:
    BankName: str
    TotalEvents: int



class WwiseAcousticEmulationParameters:
    EarlyReflectionsOffsetTimeMs: int
    GlobalWetnessScaleDB: float
    DecayDistance: float
    EarlyReflectionDecay: float
    LateReflectionDecay: float
    DryVolumeCorrectionDistance: float



class EWwiseTrackDirectionality(enum.Enum):
    OnlyForwards = 0
    OnlyBackwards = 1


class EWwiseAudioComponentPoolMode(enum.Enum):
    Steal = 0
    EWwiseAudioComponentPoolMode_MAX = 1


class EWwisePlaybackConfiguration(enum.Enum):
    Small = 0
    Headphones = 1
    Mono = 2


class EBankLoadState(enum.Enum):
    AsyncLoading = 0
    Loaded = 1


class EAcousticsMode(enum.Enum):
    EnabledUnconditionalSampleMode = 0
    Enabled = 1
    UsePlayerLocationForAcoustics = 2


class EWwiseMultiPositionType(enum.Enum):
    MultiDirections = 0
    MultiSources = 1


class EWwiseCurveInterpolation(enum.Enum):
    Linear = 0
    Log1 = 1
    Sine = 2
    Exp3 = 3


class EWwiseEventAction(enum.Enum):
    Pause = 0
    Resume = 1
    ReleaseEnvelope = 2


class EWwisePostEventFlags(enum.Enum):
    SupportDuration = 0
    SupportPlaybackPosition = 1
    EWwisePostEventFlags_MAX = 2


class EWwiseAudioComponentMixBehavior(enum.Enum):
    MixGroup = 0
    DirectToMasterMix = 1


class EWwiseAudioComponentType(enum.Enum):
    ActorDefault = 0
    Temporary = 1
    EWwiseAudioComponentType_MAX = 2


class EWwiseEffectType(enum.Enum):
    EWwiseEffectType_MAX = 0


class EWwiseDebugFlags(enum.Enum):
    HideActiveComponents = 0
    ShowComponentType = 1
    ShowEventNames = 2


class EWwiseAudioComponentSpriteSize(enum.Enum):
    Small = 0
    None_ = 1

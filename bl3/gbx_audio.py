from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import gbx_runtime
from . import wwise_audio
from . import gbx_fluid_simulation


class ActiveAmbientLocationChooser(unreal.UObject): ...


class ActiveAmbientLocationChooser_Blueprint(ActiveAmbientLocationChooser):

    def NominateSoundLocation(
        self,
        ActiveAmbientComponent: ActiveAmbientSoundComponent,
        Out_Location: core_uobject.Vector,
        Out_Radius: float,
    ) -> bool: ...
    def InitLocationChooser(
        self, ActiveAmbientComponent: ActiveAmbientSoundComponent
    ): ...


class ActiveAmbientLocationChooser_RandomWithinActor(ActiveAmbientLocationChooser):
    WithinActor: Any


class ActiveAmbientLocationChooser_RandomWithTrace(
    ActiveAmbientLocationChooser_RandomWithinActor
):
    TraceVector: core_uobject.Vector


class ActiveAmbientLocationChooser_RandomOnCeiling(
    ActiveAmbientLocationChooser_RandomWithTrace
): ...


class ActiveAmbientLocationChooser_RandomOnFloor(
    ActiveAmbientLocationChooser_RandomWithTrace
): ...


class ActiveAmbientLocationChooser_PreselectedLocation(ActiveAmbientLocationChooser):
    Locations: unreal.WrappedArray[core_uobject.Vector]
    Radii: unreal.WrappedArray[float]

    def UpdateLocations(self): ...
    def DrawLocations(self): ...
    def AddLocation(self, InLocation: core_uobject.Vector, InRadius: float) -> bool: ...


class ActiveAmbientLocationChooser_Party(
    ActiveAmbientLocationChooser_PreselectedLocation
):
    PartierWeight: float
    PartierRadius: float
    IntensityRange: core_uobject.FloatInterval
    PartyDecayPerNomination: float
    bVisualizeParty: bool
    PartyVisualizationLineLength: float
    PartyWeights: unreal.WrappedArray[float]
    TotalPartyWeight: float


class ActiveAmbientLocationValidator(unreal.UObject): ...


class ActiveAmbientLocationValidator_Blueprint(ActiveAmbientLocationValidator):

    def IsProposedLocationValid(
        self,
        ActiveAmbientComponent: ActiveAmbientSoundComponent,
        Location: core_uobject.Vector,
    ) -> bool: ...


class ActiveAmbientLocationValidator_DistanceFromListener(
    ActiveAmbientLocationValidator
):
    Range: core_uobject.FloatInterval


class ActiveAmbientSound(engine.Actor):
    TargetInstances: int
    ActiveAmbientSound: ActiveAmbientSoundComponent

    def EnableSounds(self): ...
    def DisableSounds(self): ...


class ActiveAmbientSoundComponent(engine.ActorComponent):
    StartEvent: wwise_audio.WwiseEvent
    LoopDuration: core_uobject.FloatInterval
    ExpiredStopEvent: wwise_audio.WwiseEvent
    ExpiredStopFadeTime: float
    TargetSimultaneousInstances: int
    RepopulateDelay: core_uobject.FloatInterval
    LocationChooser: ActiveAmbientLocationChooser
    LocationValidator: ActiveAmbientLocationValidator
    Updaters: unreal.WrappedArray[ActiveAmbientUpdater]
    bWaryOfPlayers: bool
    WaryDistance: float
    WaryStopEvent: wwise_audio.WwiseEvent
    WaryStopFadeTime: float
    StartleRecoveryTime: float
    StartedStopEvent: wwise_audio.WwiseEvent
    StartledStopFadeTime: float
    ActiveAmbientInstances: unreal.WrappedArray[ActiveAmbientInstance]
    NextSpawnTime: float
    TimeSinceLastSpawn: float
    RemainingStartleRecovery: float

    def Startle(self, Location: core_uobject.Vector, Radius: float): ...


class ActiveAmbientUpdater(unreal.UObject): ...


class ActiveAmbientUpdater_Blueprint(ActiveAmbientUpdater):

    def UpdateActiveAmbientInstance(
        self,
        ActiveAmbientComponent: ActiveAmbientSoundComponent,
        ActiveAmbientInstance: ActiveAmbientInstance,
        DeltaTime: float,
    ): ...
    def InitializeActiveAmbientInstance(
        self,
        ActiveAmbientComponent: ActiveAmbientSoundComponent,
        ActiveAmbientInstance: ActiveAmbientInstance,
    ): ...


class ActiveAmbientUpdater_MoveInRandomDirection(ActiveAmbientUpdater):
    SpeedRange: core_uobject.FloatInterval


class ActiveAmbientUpdater_MoveWithWobble(ActiveAmbientUpdater_MoveInRandomDirection):
    DirectionUpdateFrequency: float
    DirectionUpdateCone: float


class AmbientSoundBox(wwise_audio.WwiseAmbientSound):
    BoxComponent: engine.BoxComponent


class AmbientSoundSphere(wwise_audio.WwiseAmbientSound):
    SphereComponent: engine.SphereComponent


class AmbientSoundSpline(wwise_audio.WwiseAmbientSound):
    SplineComponent: engine.SplineComponent
    bForceEmitterUniformScale: bool
    CachedBounds: core_uobject.BoxSphereBounds


class AnimNotify_CharacterSound(engine.AnimNotify):
    Tag: CharacterSoundTag


class AnimNotify_Foley(engine.AnimNotify):
    FoleyParams: FoleyEventParams
    bRestrictToMatchingPlayerPerspective: bool


class AnimNotify_FootFoley(AnimNotify_Foley):
    FootIndex: int


class AnimNotify_WwiseEvent(engine.AnimNotify):
    WwiseEvent: wwise_audio.WwiseEvent
    PlaybackMethod: EWwiseNotifyComponentMethod
    WwiseComponentTag: str
    SocketName: str
    bAttachToOwner: bool
    EmitterRadius: float
    bIgnorePerspective: bool
    AcousticsMode: wwise_audio.EAcousticsMode


class AnimNotifyState_LoopingSound(engine.AnimNotifyState):
    StartEvent: wwise_audio.WwiseEvent
    StopEvent: wwise_audio.WwiseEvent
    PlaybackMethod: EWwiseNotifyComponentMethod
    WwiseComponentTag: str
    SocketName: str
    bAttachToOwner: bool
    EmitterRadius: float
    ActivePlaybackInstances: Any


class AudioDistanceThresholdSubscriberInterface(core_uobject.Interface): ...


class AudioDistanceThresholdManager(unreal.UObject):
    World: engine.World
    SubscriberData: unreal.WrappedArray[ADMSubscriberData]


class AudioOcclusionVoxelDataProvider(gbx_fluid_simulation.VoxelDataProvider):
    DataResolution: core_uobject.IntVector
    bUseMaterialLibrary: bool
    TritonMaterialLibraryFile: str
    ExtraTritonMaterialEquivalences: Any
    CheckCollisionChannel: int
    CheckCollisionResponse: int
    bVoxelizeFoliage: bool
    ExtraTerrainThickness: int
    bFlagMatchingVoxels: bool
    FlagVoxelsForComponentsFilter: AudioPrepComponentFilter


class AudioOcclusionVoxelizerZone(engine.Actor):

    def Voxelize(self): ...
    def ExportAsRLE(self): ...
    def ExportAsRaw(self): ...


class AudioPrepLocationConsumer(core_uobject.Interface): ...


class AudioPrepLocationFinder(unreal.UObject): ...


class AudioPrepLocationFinder_Blueprint(AudioPrepLocationFinder):
    CurrentConsumer: Any

    def AddLocation(
        self,
        Location: core_uobject.Vector,
        Rotation: core_uobject.Rotator,
        Radius: float,
    ): ...
    def AddFoundLocations(self): ...


class ActiveAmbientLocationFinder_Blueprint(AudioPrepLocationFinder):

    def AddFoundLocations(
        self,
        ActiveAmbientComponent: ActiveAmbientSoundComponent,
        PreselectedLocationChooser: ActiveAmbientLocationChooser_PreselectedLocation,
    ): ...


class AudioPrepLocationFinder_ActorList(AudioPrepLocationFinder): ...


class AudioPrepLocationFinder_FilteredComponents(AudioPrepLocationFinder): ...


class AudioPrepLocationFinder_SplineTracer(AudioPrepLocationFinder): ...


class AudioPrepLocationFinder_PincushionTracer(AudioPrepLocationFinder): ...


class AudioPrepLocationFinder_TraceDownToActor(AudioPrepLocationFinder): ...


class AudioPrepLocationFinder_FoliageLocations(AudioPrepLocationFinder): ...


class AudioPrepLocationFinder_LandscapeGrassLocations(AudioPrepLocationFinder): ...


class AudioPrepLocationFinder_InstanceLocations(AudioPrepLocationFinder): ...


class AudioPrepLocationFinder_Grid(AudioPrepLocationFinder): ...


class AudioPrepLocationFinder_TraceGrid(AudioPrepLocationFinder): ...


class AudioPrepLocationFinder_VoxelMaterialBoundary(AudioPrepLocationFinder): ...


class CharacterSoundData(gbx_runtime.GbxDataAsset):
    TriggerRefreshAll: gbx_runtime.GbxTriggerProperty
    InheritData: CharacterSoundData
    Sounds: InheritableSoundMap
    VocalLoops: InheritableVocalLoopList

    def RefreshAll(self): ...


class CharacterSoundInterface(core_uobject.Interface): ...


class CharacterSoundLogicComponent(engine.ActorComponent):
    CurrentVocalization: CurrentVocalization
    CurrentVocalLoop: CurrentVocalLoopInfo


class CharacterSoundTag(gbx_runtime.GbxDataAsset):
    Type: ECharacterSoundType
    ChanceToPlay: float
    bHighPriorityInterruptingVox: bool
    bPainVox: bool
    bDeathVox: bool


class DistributedAmbientSound(engine.Actor):
    SoundVariants: unreal.WrappedArray[wwise_audio.WwiseEvent]
    SoundMode: EDistributedSoundMode
    LocationFinder: AudioPrepLocationFinder
    bTreatLocationsAsOneSource: bool
    MultiPositionType: wwise_audio.EWwiseMultiPositionType
    DOffset: float
    DScale: float
    MaxEmitterSize: float
    CombinedSourceVolumeRatio: float
    bUseUnconditionalSampleModeForAcoustics: bool
    AudioComponents: unreal.WrappedArray[wwise_audio.WwiseAudioComponent]
    PackedTreeData: unreal.WrappedArray[int]
    Bounds: core_uobject.Box

    def DoUpdateTree(self): ...
    def DoFindNewLocationsAndRebuild(self): ...


class FluidSimExampleZone(engine.Actor):

    def UpdateVisualization(self): ...
    def ExportVectorField(self): ...
    def ApplyToOtherSim(self): ...


class FoleyAccessoryComponent(engine.SceneComponent):
    FoleyAccessoryWwiseEvent: wwise_audio.WwiseEvent
    LoopStartWwiseEvent: wwise_audio.WwiseEvent
    AccessoryVolume: float
    AccesoryPitch: float
    AccessoryRadius: float
    MyFoleyMain: FoleyMainComponent


class FoleyImplementerInterface(core_uobject.Interface): ...


class FoleyMainComponent(engine.ActorComponent):
    FoleyMainWwiseEvent: wwise_audio.WwiseEvent
    LoopStartWwiseEvent: wwise_audio.WwiseEvent
    FootstepWwiseEvent: wwise_audio.WwiseEvent
    PerFootFootstepWwiseEvents: unreal.WrappedArray[wwise_audio.WwiseEvent]
    CharacterSizeSwitch: wwise_audio.WwiseSwitch
    FoleyVolume: float
    FoleyPitch: float
    FootstepVolume: float
    FootstepPitch: float
    FootstepFoleyComponentTags: unreal.WrappedArray[str]
    FoleyAccessoryVolume: float
    FoleyAccessoryPitch: float
    ExtraParameters: unreal.WrappedArray[ExtraFoleyParameter]
    AttenuationScalingFactor: float
    CachedFootstepParams: FoleyEventParams
    LastMaterialSwitch: wwise_audio.WwiseSwitch
    SurfaceModifierEvent: wwise_audio.WwiseEvent
    SurfaceModifierVolume: float
    SurfaceModifierFootstepVolumeMultiplier: float
    AssociatedFoleyAccessories: unreal.WrappedArray[FoleyAccessoryComponent]

    def SetSurfaceModifier(
        self,
        PlayEvent: wwise_audio.WwiseEvent,
        Volume: float,
        FootstepVolumeMultiplier: float,
    ): ...
    def PlayFootstepEvent(self, EventParams: FoleyEventParams): ...
    def PlayFootstep(
        self,
        FootstepLocation: core_uobject.Vector,
        FootstepRotation: core_uobject.Rotator,
        MaterialSwitch: wwise_audio.WwiseSwitch,
        VolumeAdjustment: float,
        PitchAdjustment: float,
        ConfigureEvent: wwise_audio.WwiseEvent,
        bPreview: bool,
    ): ...


class GbxAudioBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def TriggerCharacterSound(
        self, Character: engine.Actor, SoundTag: CharacterSoundTag
    ): ...
    def RemoveListenerAudioEffect(
        self, Character: engine.Actor, Efx: wwise_audio.WwiseAuxBus
    ): ...
    def PassesAudioPreparationHitFilter(
        self, Hit: engine.HitResult, Filter: AudioPrepHitResultFilter
    ) -> bool: ...
    def PassesAudioPreparationComponentFilter(
        self, Component: engine.PrimitiveComponent, Filter: AudioPrepComponentFilter
    ) -> bool: ...
    def ApplyListenerAudioEffect(
        self,
        Character: engine.Actor,
        Efx: wwise_audio.WwiseAuxBus,
        WetVolume: float,
        DryVolume: float,
    ): ...


class GbxAudioGlobalsData(gbx_runtime.GbxDataAsset):
    PauseGameAudioEvent: wwise_audio.WwiseEvent
    UnpauseGameAudioEvent: wwise_audio.WwiseEvent
    PreLevelTransitionEvent: wwise_audio.WwiseEvent
    PostLevelTransitionEvent: wwise_audio.WwiseEvent
    MasterVolumeParameter: wwise_audio.WwiseRtpc
    UserVolumeMusicParameter: wwise_audio.WwiseRtpc
    UserVolumeSfxParameter: wwise_audio.WwiseRtpc
    UserVolumeVOParameter: wwise_audio.WwiseRtpc
    UserVolumeHdrSfxParameter: wwise_audio.WwiseRtpc
    UserVolumeHdrVOParameter: wwise_audio.WwiseRtpc
    UserVolumeHdrMixRtpc: wwise_audio.WwiseRtpc
    UserPS4ControllerRtpc: wwise_audio.WwiseRtpc
    AlwaysLoadedBanks: unreal.WrappedArray[wwise_audio.WwiseBank]
    bEnableAcoustics: bool
    OcclusionStrength: float
    RedirectionVolumeInterval: core_uobject.FloatInterval
    EarlyReflectionsVolumeCurve: engine.CurveFloat
    LateReverbVolumeCurve: engine.CurveFloat
    ReverbBoostOutdoornessModifierCurve: engine.CurveFloat
    ReverbBoostDryGainFraction: float
    EarlyReflectionsReverbBoostStrength: float
    LateReverbReverbBoostStrength: float
    WeaponFireReverbBoost: float
    ExplosionReverbBoost: float
    MusicVolumeSliderPreviewSound: wwise_audio.WwiseEvent
    MusicVolumeSliderPreviewSoundStop: wwise_audio.WwiseEvent
    SFXVolumeSliderPreviewSound: wwise_audio.WwiseEvent
    VOVolumeSliderPreviewSound: wwise_audio.WwiseEvent
    VoiceCommVolumeSliderPreviewSound: wwise_audio.WwiseEvent
    StartStandardCinematicModeEvent: wwise_audio.WwiseEvent
    EndStandardCinematicModeEvent: wwise_audio.WwiseEvent
    StartExclusiveCinematicModeEvent: wwise_audio.WwiseEvent
    EndExclusiveCinematicModeEvent: wwise_audio.WwiseEvent
    JumpedVocalizationTag: CharacterSoundTag
    FootstepVolumeRtpc: wwise_audio.WwiseRtpc
    FoleyMainVolumeRtpc: wwise_audio.WwiseRtpc
    FoleyAccessoryVolumeRtpc: wwise_audio.WwiseRtpc
    FootstepPitchRtpc: wwise_audio.WwiseRtpc
    FoleyMainPitchRtpc: wwise_audio.WwiseRtpc
    FoleyAccessoryPitchRtpc: wwise_audio.WwiseRtpc
    FoleyPerspectiveRtpc: wwise_audio.WwiseRtpc
    SurfaceModifierVolumeRtpc: wwise_audio.WwiseRtpc
    HighDetailFoleySwitch: wwise_audio.WwiseSwitch
    LowDetailFoleySwitch: wwise_audio.WwiseSwitch
    FootstepAction: wwise_audio.WwiseEvent
    HandPlantAction: wwise_audio.WwiseEvent
    FirstPersonFootstepsForwardOffset: float
    CharacterRelativeSpeedRtpc: wwise_audio.WwiseRtpc
    CharacterRelativeVerticalAirSpeedRtpc: wwise_audio.WwiseRtpc
    WalkingSlopeRtpc: wwise_audio.WwiseRtpc
    WaterDepthRtpc: wwise_audio.WwiseRtpc
    RelativeWaterDepthRtpc: wwise_audio.WwiseRtpc
    RandomVariationRtpc: wwise_audio.WwiseRtpc
    PerspectiveRtpc: wwise_audio.WwiseRtpc
    ExplosionSizeRtpc: wwise_audio.WwiseRtpc
    PlayerLocationOutdoornessRTPC: wwise_audio.WwiseRtpc
    OutdoornessRTPC: wwise_audio.WwiseRtpc


class GbxAudioSettings(unreal.UObject):
    AudioGlobalsData: GbxAudioGlobalsData
    DefaultAudioGlobalsData: core_uobject.SoftObjectPath
    FoleyCullingDistanceFraction: float
    FoleyCullingDistanceMinVolumeForReduction: float
    FoleyCullingDistanceReductionFractionPerDBOverMin: float
    SkipCinematicEvents: unreal.WrappedArray[core_uobject.SoftObjectPath]


class LightAudioComponent(engine.SceneComponent):
    PersistentRTPCValues: Any
    Loops: unreal.WrappedArray[wwise_audio.WwiseEvent]
    RelativeDetailedLocations: unreal.WrappedArray[wwise_audio.WwiseLocationOverride]
    bDynamicPosition: bool
    SubscribedToManager: AudioDistanceThresholdManager

    def SetRTPCValue(
        self,
        GameParameter: wwise_audio.WwiseRtpc,
        Value: float,
        bPersistent: bool,
        ValueChangeDuration: float,
        FadeCurve: wwise_audio.EWwiseCurveInterpolation,
    ): ...
    def PostWwiseEvent(
        self, WwiseEvent: wwise_audio.WwiseEvent
    ) -> wwise_audio.WwisePlaybackInstance: ...


class MusicSequencerComponent(engine.ActorComponent):
    BPM: float
    SequencerLatencyInSeconds: float
    bKillLateEvents: bool
    bRegisteredWithAudioDevice: bool

    def StopSequence(self): ...
    def PostSequenceEvent(
        self,
        WwiseComponent: wwise_audio.WwiseAudioComponent,
        WwiseEvent: wwise_audio.WwiseEvent,
        Note: int,
        Velocity: int,
        Channel: int,
        StartBeat: float,
        Duration: float,
    ): ...
    def PlaySequence(self): ...
    def PauseSequence(self): ...
    def IsPlaying(self) -> bool: ...
    def GetRealTimeUntilBeat(self, Beat: float) -> float: ...
    def GetCurrentBeat(self) -> float: ...


class ParticleModuleGbxAudioBase(engine.ParticleModule): ...


class ParticleModuleGbxAudioLoop(ParticleModuleGbxAudioBase):
    LoopStartEvent: wwise_audio.WwiseEvent
    LoopStopEvent: wwise_audio.WwiseEvent
    MultiPositionType: wwise_audio.EWwiseMultiPositionType
    AudioComponentRadius: float
    GainOverLifetime: engine.RawDistributionFloat


class ParticleModuleGbxAudioPool(ParticleModuleGbxAudioBase):
    AudioEvent: wwise_audio.WwiseEvent
    MaxNumberOfAudioComponents: int
    bStealComponents: bool
    AudioComponentRadius: float
    GainOverLifetime: engine.RawDistributionFloat


class WindAudioLoopComponent(LightAudioComponent):
    WindSpeedAudioParameter: wwise_audio.WwiseRtpc
    WindAccelerationAudioParameter: wwise_audio.WwiseRtpc
    WindSensitivity: WindDirectionalSensitivity


class WwiseListenerEffectComponent(engine.ActorComponent):
    bRegisteredWithAudioDevice: bool
    WwiseEffects: unreal.WrappedArray[wwise_audio.WwiseEffectInfo]

    def RemoveAudioEffect(self, Efx: wwise_audio.WwiseAuxBus): ...
    def RemoveAllAudioEffects(self): ...
    def ApplyAudioEffect(
        self, Efx: wwise_audio.WwiseAuxBus, WetPercent: float, DryPercent: float
    ): ...


class ActiveAmbientInstance: ...


class ActiveLoopingSoundNotifyData:
    Instances: unreal.WrappedArray[wwise_audio.WwisePlaybackInstance]


class ADMSubscriberData:
    Subscriber: Any


class AudioPrepHitResultFilter:
    HitAssetNameFilter: unreal.WrappedArray[str]
    SurfaceTypeFilter: unreal.WrappedArray[int]
    PhysMatFilter: unreal.WrappedArray[Any]
    MaterialFilter: unreal.WrappedArray[Any]
    WithinActorBoundsBlueprint: unreal.WrappedArray[engine.Actor]
    WithinActorBounds: unreal.WrappedArray[Any]
    NormalDirectionLimits: unreal.WrappedArray[AudioPropHitFilter_DirectionLimit]
    bAllowHitsWithinGeometry: bool


class AudioPropHitFilter_DirectionLimit:
    Direction: core_uobject.Vector
    DotProductLimits: core_uobject.FloatInterval


class AudioPrepComponentFilter:
    AssetNameFilter: unreal.WrappedArray[str]
    SurfaceTypeFilter: unreal.WrappedArray[int]
    PhysMatFilter: unreal.WrappedArray[Any]
    MaterialFilter: unreal.WrappedArray[Any]
    MaterialName: unreal.WrappedArray[str]
    WithinActorBoundsBlueprint: unreal.WrappedArray[engine.Actor]
    WithinActorBounds: unreal.WrappedArray[Any]
    AttachedToActors: unreal.WrappedArray[Any]
    ActorClassName: unreal.WrappedArray[str]
    ComponentClassName: unreal.WrappedArray[str]
    bOnlyWorldGeometry: bool


class ResultGridFilter:
    Iterations: int
    ResultOperation: EFilterResultOperation
    StructuringElements: unreal.WrappedArray[str]


class InheritableVocalLoopList:
    VocalLoops: unreal.WrappedArray[CharacterVocalLoopImplementation]


class CharacterVocalLoopImplementation:
    bOriginator: bool
    LoopName: str
    bPainLoop: bool
    LoopID: core_uobject.Guid
    bOverrideConditions: bool
    ConditionID: core_uobject.Guid
    Condition: gbx_runtime.GbxCondition
    bPlayOnce: bool
    StopTryingToRunAfterXSeconds: float
    WhileConditionID: core_uobject.Guid
    WhileCondition: gbx_runtime.GbxCondition
    bOverrideAudio: bool
    StartEvent: wwise_audio.WwiseEvent
    StopEvent: wwise_audio.WwiseEvent


class InheritableSoundMap:
    CharacterSounds: Any


class CharacterSoundImplementation:
    bOriginator: bool
    DefaultWwiseEvent: wwise_audio.WwiseEvent
    bOverrideWwiseEvent: bool
    WwiseEvent: wwise_audio.WwiseEvent


class CharacterSoundLoopDetails: ...


class CurrentVocalization:
    Tag: CharacterSoundTag
    PlayingInstance: wwise_audio.WwisePlaybackInstance


class CurrentVocalLoopInfo:
    LoopID: core_uobject.Guid
    PlayingInstance: wwise_audio.WwisePlaybackInstance
    Details: CharacterSoundLoopDetails


class CharacterVocalLoop:
    StartEvent: wwise_audio.WwiseEvent
    StopEvent: wwise_audio.WwiseEvent
    Condition: gbx_runtime.GbxCondition
    WhileCondition: gbx_runtime.GbxCondition
    bPainLoop: bool


class FoleyEventParams:
    WwiseEvent: wwise_audio.WwiseEvent
    OptionalMaterialSwitch: wwise_audio.WwiseSwitch
    Volume: float
    Pitch: float
    ComponentTags: unreal.WrappedArray[str]


class ExtraFoleyParameter:
    RtpcParam: wwise_audio.WwiseRtpc
    Value: float


class WindDirectionalSensitivity:
    LocalX: WindLocalAxisSensitivity
    LocalY: WindLocalAxisSensitivity
    LocalZ: WindLocalAxisSensitivity


class WindLocalAxisSensitivity:
    PositiveDirectionSensitivity: float
    NegativeDirectionSensitivity: float


class EDistributedSoundDebugVisualizationMode(enum.Enum):
    ActiveLocations = 0
    Tree = 1
    EDistributedSoundDebugVisualizationMode_MAX = 2


class EWwiseNotifyComponentMethod(enum.Enum):
    FindComponentsByTag = 0
    SpawnComponentAtSocket = 1


class EOcclusionVoxelThinningAlgorithm(enum.Enum):
    EOcclusionVoxelThinningAlgorithm_MAX = 0
    MedialPlane = 1


class EFilterResultOperation(enum.Enum):
    Add = 0
    Subtract = 1


class ECharacterSoundType(enum.Enum):
    Vocalization = 0
    ECharacterSoundType_MAX = 1


class EDistributedSoundMode(enum.Enum):
    VolumetricSphere = 0
    EDistributedSoundMode_MAX = 1

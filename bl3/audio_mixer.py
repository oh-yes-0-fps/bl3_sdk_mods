from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import engine


class SynthComponent(engine.SceneComponent):
    bAutoDestroy: bool
    bStopWhenOwnerDestroyed: bool
    bAllowSpatialization: bool
    bOverrideAttenuation: bool
    bOutputToBusOnly: bool
    AttenuationSettings: engine.SoundAttenuation
    AttenuationOverrides: engine.SoundAttenuationSettings
    ConcurrencySettings: engine.SoundConcurrency
    SoundClass: engine.SoundClass
    SourceEffectChain: engine.SoundEffectSourcePresetChain
    SoundSubmix: engine.SoundSubmix
    SoundSubmixSends: unreal.WrappedArray[engine.SoundSubmixSendInfo]
    BusSends: unreal.WrappedArray[engine.SoundSourceBusSendInfo]
    PreEffectBusSends: unreal.WrappedArray[engine.SoundSourceBusSendInfo]
    bIsUISound: bool
    bIsPreviewSound: bool
    EnvelopeFollowerAttackTime: int
    EnvelopeFollowerReleaseTime: int
    OnAudioEnvelopeValue: Any
    Synth: SynthSound
    AudioComponent: engine.AudioComponent
    LastSampleRate: int

    def Stop(self): ...
    def Start(self): ...
    def SetVolumeMultiplier(self, VolumeMultiplier: float): ...
    def SetSubmixSend(self, Submix: engine.SoundSubmix, SendLevel: float): ...
    def IsPlaying(self) -> bool: ...


class AudioMixerBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def StopRecordingOutput(
        self,
        WorldContextObject: unreal.UObject,
        ExportType: engine.EAudioRecordingExportType,
        Name: str,
        Path: str,
        SubmixToRecord: engine.SoundSubmix,
        ExistingSoundWaveToOverwrite: engine.SoundWave,
    ) -> engine.SoundWave: ...
    def StartRecordingOutput(
        self,
        WorldContextObject: unreal.UObject,
        ExpectedDuration: float,
        SubmixToRecord: engine.SoundSubmix,
    ): ...
    def SetBypassSourceEffectChainEntry(
        self,
        WorldContextObject: unreal.UObject,
        PresetChain: engine.SoundEffectSourcePresetChain,
        EntryIndex: int,
        bBypassed: bool,
    ): ...
    def RemoveSourceEffectFromPresetChain(
        self,
        WorldContextObject: unreal.UObject,
        PresetChain: engine.SoundEffectSourcePresetChain,
        EntryIndex: int,
    ): ...
    def RemoveMasterSubmixEffect(
        self,
        WorldContextObject: unreal.UObject,
        SubmixEffectPreset: engine.SoundEffectSubmixPreset,
    ): ...
    def GetNumberOfEntriesInSourceEffectChain(
        self,
        WorldContextObject: unreal.UObject,
        PresetChain: engine.SoundEffectSourcePresetChain,
    ) -> int: ...
    def ClearMasterSubmixEffects(self, WorldContextObject: unreal.UObject): ...
    def AddSourceEffectToPresetChain(
        self,
        WorldContextObject: unreal.UObject,
        PresetChain: engine.SoundEffectSourcePresetChain,
        Entry: engine.SourceEffectChainEntry,
    ): ...
    def AddMasterSubmixEffect(
        self,
        WorldContextObject: unreal.UObject,
        SubmixEffectPreset: engine.SoundEffectSubmixPreset,
    ): ...


class SubmixEffectDynamicsProcessorPreset(engine.SoundEffectSubmixPreset):
    Settings: SubmixEffectDynamicsProcessorSettings

    def SetSettings(self, InSettings: SubmixEffectDynamicsProcessorSettings): ...


class SubmixEffectSubmixEQPreset(engine.SoundEffectSubmixPreset):
    Settings: SubmixEffectSubmixEQSettings

    def SetSettings(self, InSettings: SubmixEffectSubmixEQSettings): ...


class SubmixEffectReverbPreset(engine.SoundEffectSubmixPreset):
    Settings: SubmixEffectReverbSettings

    def SetSettingsWithReverbEffect(
        self, InReverbEffect: engine.ReverbEffect, WetLevel: float
    ): ...
    def SetSettings(self, InSettings: SubmixEffectReverbSettings): ...


class SynthSound(engine.SoundWaveProcedural): ...


class SubmixEffectDynamicsProcessorSettings:
    DynamicsProcessorType: ESubmixEffectDynamicsProcessorType
    PeakMode: ESubmixEffectDynamicsPeakMode
    LookAheadMsec: float
    AttackTimeMsec: float
    ReleaseTimeMsec: float
    ThresholdDb: float
    Ratio: float
    KneeBandwidthDb: float
    InputGainDb: float
    OutputGainDb: float
    bChannelLinked: bool
    bAnalogMode: bool


class SubmixEffectSubmixEQSettings:
    EQBands: unreal.WrappedArray[SubmixEffectEQBand]


class SubmixEffectEQBand:
    Frequency: float
    Bandwidth: float
    GainDb: float
    bEnabled: bool


class SubmixEffectReverbSettings:
    Density: float
    Diffusion: float
    Gain: float
    GainHF: float
    DecayTime: float
    DecayHFRatio: float
    ReflectionsGain: float
    ReflectionsDelay: float
    LateGain: float
    LateDelay: float
    AirAbsorptionGainHF: float
    WetLevel: float


class ESubmixEffectDynamicsPeakMode(enum.Enum):
    RootMeanSquared = 0
    ESubmixEffectDynamicsPeakMode_MAX = 1
    Peak = 2


class ESubmixEffectDynamicsProcessorType(enum.Enum):
    Count = 0
    Limiter = 1
    Expander = 2

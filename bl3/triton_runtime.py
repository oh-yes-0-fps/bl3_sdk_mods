from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine
from . import gbx_runtime
from . import wwise_audio
from . import gbx_audio



class TritonAcousticDataComponent(engine.SceneComponent):
    ProbeLayers: unreal.WrappedArray[TritonProbeLayer]
    SpeedOfSound: float
    ExcludeComponentsFilters: unreal.WrappedArray[gbx_audio.AudioPrepComponentFilter]
    IncludeComponentsFilters: unreal.WrappedArray[gbx_audio.AudioPrepComponentFilter]
    ThinningSteps: unreal.WrappedArray[gbx_audio.EOcclusionVoxelThinningAlgorithm]
    ExtraTerrainThickness: int
    bOnlyGenerateSelected: bool
    UpdateSteps: TritonUpdateDesc
    TriggerRefreshCachedVoxelData: gbx_runtime.GbxTriggerProperty
    TriggerVisualizeMaterials: gbx_runtime.GbxTriggerProperty
    TriggerAuditProbeLocations: gbx_runtime.GbxTriggerProperty
    TriggerUpdateProbeLocations: gbx_runtime.GbxTriggerProperty
    CachedVoxelData: gbx_audio.AudioOcclusionVoxelDataProvider
    CachedVoxelDataNoThinning: gbx_audio.AudioOcclusionVoxelDataProvider
    CachedNavMeshVoxelData: gbx_audio.AudioOcclusionVoxelDataProvider
    TriggerBuildFallbackAcousticData: gbx_runtime.GbxTriggerProperty
    def VisualizeMaterials(self): ...
    def UpdateProbeLocations(self): ...
    def RefreshCachedVoxelData(self): ...
    def BuildFallbackAcousticData(self): ...
    def AuditProbeLocations(self): ...


class TritonZone(engine.Actor):
    TritonDataComponent: TritonAcousticDataComponent



class TritonVoxelOverrideVolume(engine.Volume): ...


class TritonProbeHelper(engine.Actor):
    DistanceLimit: float
    bRecording: bool
    RecordedLocations: unreal.WrappedArray[core_uobject.Vector]



class TritonProbeLocationProvider(engine.Volume):
    TargetDistanceAboveGround: float
    MinimumHorizontalSpacing: float
    MinWallDistanceForLowDensityProbes: float
    SpacingFactorForLowDensityProbes: float
    DecimationThreshold: float
    MaxNumberDecimations: int
    SuppressingZones: unreal.WrappedArray[TritonProbeLocationProvider]
    def FindProbeLocations(self, WorldBoxSphere: core_uobject.BoxSphereBounds, GeoVoxels: gbx_audio.AudioOcclusionVoxelDataProvider, NavVoxels: gbx_audio.AudioOcclusionVoxelDataProvider, out_ResultProbeLocations: unreal.WrappedArray[core_uobject.Vector]): ...


class TritonSettings(unreal.UObject):
    TritonDataPath: engine.DirectoryPath



class CachedPerProbeAcousticData:
    ERVolume: float
    LRVolume: float
    LRDuration: float



class TritonUpdateDesc:
    bCleanTempDirectory: bool
    bExportVoxelizedRegion: bool
    bCreateJobConfig: bool
    bCreateTaskImages: bool
    bRunTasks: bool
    bCreateCompressedVoxMap: bool
    bCollateResults: bool
    bGenerateLongDistanceProbes: bool
    bFixupDirectionalReciprocity: bool
    bIncorporateNewACE: bool



class TritonProbeLayer:
    ProbeLocationSets: unreal.WrappedArray[TritonProbeSet]
    SimulationParams: TritonSimulationParams
    FadeParams: TritonLayerFadeParams
    AdvancedParams: TritonAdvancedParams
    DatasetPathOverride: engine.DirectoryPath
    DatasetFile: str
    FallbackAcousticData: unreal.WrappedArray[FallbackAcousticData]
    FallbackAcousticDataAggregate: FallbackAcousticData
    FallbackAcousticEmulationParameters: wwise_audio.WwiseAcousticEmulationParameters
    bHasGeneratedEarlyReflections: bool



class FallbackAcousticData:
    Location: core_uobject.Vector
    AcousticData: wwise_audio.WwiseEmitterAcousticData
    Outdoorness: float
    EarlyReflections: unreal.WrappedArray[float]



class TritonAdvancedParams:
    bUseProbeStreaming: bool
    PreloadDistance: float
    MaxLoadedProbes: int
    MinDistanceFractionForPreload: float
    SpatialInterpCacheSize: int
    VoxelDecompressionCacheSize: int
    SimCellCacheSize: int
    bAllowProbeAutoLoad: bool
    ProbeSearchDistance: float



class TritonLayerFadeParams:
    RangeMin: float
    VolMin: float
    Pivot: float
    RangeMax: float
    VolMax: float



class TritonSimulationParams:
    SimulationFrequency: float
    SimulationRadius: float
    SimulationDepth: float
    SimulationHeight: float
    IdealVoxelmapResolutionInMeters: float
    bUseRMSForAveragingLongDistanceVolumes: bool
    bUseWallinessFactorForLongDistanceVolumes: bool



class TritonProbeSet:
    Label: str
    ProbeLocationProvider: TritonProbeLocationProvider
    ProbeLocations: unreal.WrappedArray[core_uobject.Vector]
    bLowDetail: bool


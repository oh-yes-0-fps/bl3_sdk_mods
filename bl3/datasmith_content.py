from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine


class DatasmithAreaLightActor(engine.Actor):
    LightShape: EDatasmithAreaLightActorShape
    Dimensions: core_uobject.Vector2D
    Color: core_uobject.LinearColor
    Intensity: float


class DatasmithObjectTemplate(unreal.UObject): ...


class DatasmithAreaLightActorTemplate(DatasmithObjectTemplate):
    LightShape: EDatasmithAreaLightActorShape
    Dimensions: core_uobject.Vector2D
    Color: core_uobject.LinearColor
    Intensity: float
    bHidden: bool


class DatasmithAssetImportData(engine.AssetImportData): ...


class DatasmithStaticMeshImportData(DatasmithAssetImportData): ...


class DatasmithStaticMeshCADImportData(DatasmithStaticMeshImportData): ...


class DatasmithSceneImportData(engine.AssetImportData): ...


class DatasmithCADImportSceneData(DatasmithSceneImportData): ...


class DatasmithAssetUserData(engine.AssetUserData):
    MetaData: Any


class DatasmithCineCameraComponentTemplate(DatasmithObjectTemplate):
    FilmbackSettings: DatasmithCameraFilmbackSettingsTemplate
    LensSettings: DatasmithCameraLensSettingsTemplate
    FocusSettings: DatasmithCameraFocusSettingsTemplate
    CurrentFocalLength: float
    CurrentAperture: float
    PostProcessSettings: DatasmithPostProcessSettingsTemplate


class DatasmithContentBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def GetDatasmithUserDataValueForKey(
        self, Object: unreal.UObject, Key: str
    ) -> str: ...
    def GetDatasmithUserDataKeysAndValuesForValue(
        self,
        Object: unreal.UObject,
        StringToMatch: str,
        OutKeys: unreal.WrappedArray[str],
        OutValues: unreal.WrappedArray[str],
    ): ...
    def GetDatasmithUserData(
        self, Object: unreal.UObject
    ) -> DatasmithAssetUserData: ...


class DatasmithImportOptions(unreal.UObject):
    SearchPackagePolicy: EDatasmithImportSearchPackagePolicy
    MaterialConflictPolicy: EDatasmithImportAssetConflictPolicy
    TextureConflictPolicy: EDatasmithImportAssetConflictPolicy
    StaticMeshActorImportPolicy: EDatasmithImportActorPolicy
    LightImportPolicy: EDatasmithImportActorPolicy
    CameraImportPolicy: EDatasmithImportActorPolicy
    OtherActorImportPolicy: EDatasmithImportActorPolicy
    MaterialQuality: EDatasmithImportMaterialQuality
    BaseOptions: DatasmithImportBaseOptions
    TessellationOptions: DatasmithTessellationOptions
    ReimportOptions: DatasmithReimportOptions


class DatasmithLightComponentTemplate(DatasmithObjectTemplate):
    bVisible: bool
    CastShadows: bool
    bUseTemperature: bool
    bUseIESBrightness: bool
    Intensity: float
    Temperature: float
    IESBrightnessScale: float
    LightColor: core_uobject.LinearColor
    LightFunctionMaterial: engine.MaterialInterface
    IESTexture: engine.TextureLightProfile


class DatasmithPointLightComponentTemplate(DatasmithObjectTemplate):
    IntensityUnits: engine.ELightUnits
    SourceRadius: float
    SourceLength: float
    AttenuationRadius: float


class DatasmithScene(unreal.UObject): ...


class DatasmithSceneActor(engine.Actor):
    Scene: DatasmithScene
    RelatedActors: Any


class DatasmithSceneComponentTemplate(DatasmithObjectTemplate):
    RelativeTransform: core_uobject.Transform
    Mobility: int
    AttachParent: engine.SceneComponent


class DatasmithSkyLightComponentTemplate(DatasmithObjectTemplate):
    SourceType: int
    CubemapResolution: int
    Cubemap: engine.TextureCube


class DatasmithSpotLightComponentTemplate(DatasmithObjectTemplate):
    InnerConeAngle: float
    OuterConeAngle: float


class DatasmithStaticMeshComponentTemplate(DatasmithSceneComponentTemplate):
    StaticMesh: engine.StaticMesh
    OverrideMaterials: unreal.WrappedArray[engine.MaterialInterface]


class DatasmithStaticMeshTemplate(DatasmithObjectTemplate):
    SectionInfoMap: DatasmithMeshSectionInfoMapTemplate
    LightMapCoordinateIndex: int
    LightMapResolution: int
    BuildSettings: unreal.WrappedArray[DatasmithMeshBuildSettingsTemplate]
    StaticMaterials: unreal.WrappedArray[DatasmithStaticMaterialTemplate]


class DatasmithPostProcessSettingsTemplate:
    bOverride_WhiteTemp: bool
    bOverride_ColorSaturation: bool
    bOverride_VignetteIntensity: bool
    bOverride_FilmWhitePoint: bool
    bOverride_AutoExposureMethod: bool
    bOverride_CameraISO: bool
    WhiteTemp: float
    VignetteIntensity: float
    FilmWhitePoint: core_uobject.LinearColor
    ColorSaturation: core_uobject.Vector4
    AutoExposureMethod: int
    CameraISO: float


class DatasmithCameraFocusSettingsTemplate:
    ManualFocusDistance: float


class DatasmithCameraLensSettingsTemplate:
    MaxFStop: float


class DatasmithCameraFilmbackSettingsTemplate:
    SensorWidth: float
    SensorHeight: float


class DatasmithTessellationOptions:
    ChordTolerance: float
    MaxEdgeLength: float
    NormalTolerance: float


class DatasmithImportBaseOptions:
    SceneHandling: EDatasmithImportScene
    bIncludeGeometry: bool
    bIncludeMaterial: bool
    bIncludeLight: bool
    bIncludeCamera: bool
    AssetOptions: DatasmithAssetImportOptions
    StaticMeshOptions: DatasmithStaticMeshImportOptions


class DatasmithStaticMeshImportOptions:
    MinLightmapResolution: EDatasmithImportLightmapMin
    MaxLightmapResolution: EDatasmithImportLightmapMax
    bGenerateLightmapUVs: bool
    bRemoveDegenerates: bool


class DatasmithAssetImportOptions:
    PackagePath: str


class DatasmithReimportOptions:
    bUpdateActors: bool
    bRespawnDeletedActors: bool


class DatasmithMeshSectionInfoMapTemplate:
    Map: Any


class DatasmithMeshSectionInfoTemplate:
    MaterialIndex: int


class DatasmithStaticMaterialTemplate:
    MaterialSlotName: str
    MaterialInterface: engine.MaterialInterface


class DatasmithMeshBuildSettingsTemplate:
    bUseMikkTSpace: bool
    bRecomputeNormals: bool
    bRecomputeTangents: bool
    bRemoveDegenerates: bool
    bBuildAdjacencyBuffer: bool
    bUseHighPrecisionTangentBasis: bool
    bUseFullPrecisionUVs: bool
    bGenerateLightmapUVs: bool
    MinLightmapResolution: int
    SrcLightmapIndex: int
    DstLightmapIndex: int


class EDatasmithAreaLightActorShape(enum.Enum):
    Disc = 0
    Sphere = 1
    EDatasmithAreaLightActorShape_MAX = 2


class EDatasmithImportHierarchy(enum.Enum):
    UseSingleActor = 0
    UseOneBlueprint = 1


class EDatasmithImportScene(enum.Enum):
    CurrentLevel = 0
    AssetsOnly = 1


class EDatasmithImportLightmapMax(enum.Enum):
    LIGHTMAP_128 = 0
    LIGHTMAP_256 = 1
    LIGHTMAP_1024 = 2


class EDatasmithImportLightmapMin(enum.Enum):
    LIGHTMAP_32 = 0
    LIGHTMAP_64 = 1
    LIGHTMAP_256 = 2


class EDatasmithImportMaterialQuality(enum.Enum):
    UseSimplifierFresnelCurves = 0
    UseRealFresnelCurves = 1


class EDatasmithImportActorPolicy(enum.Enum):
    Full = 0
    Ignore = 1


class EDatasmithImportAssetConflictPolicy(enum.Enum):
    EDatasmithImportAssetConflictPolicy_MAX = 0
    Use = 1
    Update = 2


class EDatasmithImportSearchPackagePolicy(enum.Enum):
    All = 0
    EDatasmithImportSearchPackagePolicy_MAX = 1

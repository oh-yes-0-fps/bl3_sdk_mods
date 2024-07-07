from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine



class ControlPointMeshComponent(engine.StaticMeshComponent): ...


class LandscapeProxy(engine.Actor):
    SplineComponent: LandscapeSplinesComponent
    LandscapeGuid: core_uobject.Guid
    LandscapeSectionOffset: core_uobject.IntPoint
    MaxLODLevel: int
    LODDistanceFactor: float
    LODFalloff: int
    ComponentScreenSizeToUseSubSections: float
    LODDistributionSetting: float
    TessellationComponentScreenSize: float
    UseTessellationComponentScreenSizeFalloff: bool
    TessellationComponentScreenSizeFalloff: float
    OccluderGeometryLOD: int
    StaticLightingLOD: int
    DefaultPhysMaterial: engine.PhysicalMaterial
    StreamingDistanceMultiplier: float
    LandscapeMaterial: engine.MaterialInterface
    LandscapeHoleMaterial: engine.MaterialInterface
    BakedAutoPaintMaterial: engine.MaterialInterface
    AutoPaintStatus: int
    NegativeZBoundsExtension: float
    PositiveZBoundsExtension: float
    LandscapeComponents: unreal.WrappedArray[LandscapeComponent]
    CollisionComponents: unreal.WrappedArray[LandscapeHeightfieldCollisionComponent]
    FoliageComponents: unreal.WrappedArray[engine.HierarchicalInstancedStaticMeshComponent]
    bHasLandscapeGrass: bool
    StaticLightingResolution: float
    bCastStaticShadow: bool
    bCastShadowAsTwoSided: bool
    bCastFarShadow: bool
    bAffectDistanceFieldLighting: bool
    LightingChannels: engine.LightingChannels
    bUseMaterialPositionOffsetInStaticLighting: bool
    bRenderCustomDepth: bool
    CustomDepthStencilValue: int
    LDMaxDrawDistance: float
    LightmassSettings: engine.LightmassPrimitiveSettings
    CollisionMipLevel: int
    SimpleCollisionMipLevel: int
    CollisionThickness: float
    BodyInstance: engine.BodyInstance
    bGenerateOverlapEvents: bool
    bBakeMaterialPositionOffsetIntoCollision: bool
    ComponentSizeQuads: int
    SubsectionSizeQuads: int
    NumSubsections: int
    bUsedForNavigation: bool
    bUseDynamicMaterialInstance: bool
    NavigationGeometryGatheringMode: engine.ENavDataGatheringMode
    bUseLandscapeForCullingInvisibleHLODVertices: bool
    def SetLandscapeMaterialVectorParameterValue(self, ParameterName: str, Value: core_uobject.LinearColor): ...
    def SetLandscapeMaterialTextureParameterValue(self, ParameterName: str, Value: engine.Texture): ...
    def SetLandscapeMaterialScalarParameterValue(self, ParameterName: str, Value: float): ...
    def EditorSetLandscapeMaterial(self, NewLandscapeMaterial: engine.MaterialInterface): ...
    def EditorApplySpline(self, InSplineComponent: engine.SplineComponent, StartWidth: float, EndWidth: float, StartSideFalloff: float, EndSideFalloff: float, StartRoll: float, EndRoll: float, NumSubdivisions: int, bRaiseHeights: bool, bLowerHeights: bool, PaintLayer: LandscapeLayerInfoObject): ...
    def ChangeUseTessellationComponentScreenSizeFalloff(self, InComponentScreenSizeToUseSubSections: bool): ...
    def ChangeTessellationComponentScreenSizeFalloff(self, InUseTessellationComponentScreenSizeFalloff: float): ...
    def ChangeTessellationComponentScreenSize(self, InTessellationComponentScreenSize: float): ...
    def ChangeLODDistanceFactor(self, InLODDistanceFactor: float): ...
    def ChangeComponentScreenSizeToUseSubSections(self, InComponentScreenSizeToUseSubSections: float): ...


class Landscape(LandscapeProxy): ...


class LandscapeComponent(engine.PrimitiveComponent):
    SectionBaseX: int
    SectionBaseY: int
    ComponentSizeQuads: int
    SubsectionSizeQuads: int
    NumSubsections: int
    OverrideMaterial: engine.MaterialInterface
    OverrideHoleMaterial: engine.MaterialInterface
    MaterialInstances: unreal.WrappedArray[engine.MaterialInstanceConstant]
    MaterialInstancesDynamic: unreal.WrappedArray[engine.MaterialInstanceDynamic]
    WeightmapLayerAllocations: unreal.WrappedArray[WeightmapLayerAllocationInfo]
    WeightmapTextures: unreal.WrappedArray[engine.Texture2D]
    XYOffsetmapTexture: engine.Texture2D
    WeightmapScaleBias: core_uobject.Vector4
    WeightmapSubsectionOffset: float
    HeightmapScaleBias: core_uobject.Vector4
    HeightmapTexture: engine.Texture2D
    CachedLocalBox: core_uobject.Box
    MapBuildDataId: core_uobject.Guid
    IrrelevantLights: unreal.WrappedArray[core_uobject.Guid]
    CollisionMipLevel: int
    SimpleCollisionMipLevel: int
    NegativeZBoundsExtension: float
    PositiveZBoundsExtension: float
    StaticLightingResolution: float
    ForcedLOD: int
    LODBias: int
    StateId: core_uobject.Guid
    BakedTextureMaterialGuid: core_uobject.Guid
    GIBakedBaseColorTexture: engine.Texture2D
    MobileBlendableLayerMask: int
    MobileMaterialInterface: engine.MaterialInterface
    MobileWeightmapTextures: unreal.WrappedArray[engine.Texture2D]
    bHasBakedAutoPaint: bool
    def GetMaterialInstanceDynamic(self, InIndex: int, ReturnValue: engine.MaterialInstanceDynamic) -> engine.MaterialInstanceDynamic: ...


class LandscapeGizmoActor(engine.Actor): ...


class LandscapeGizmoActiveActor(LandscapeGizmoActor): ...


class LandscapeGizmoRenderComponent(engine.PrimitiveComponent): ...


class LandscapeGrassType(unreal.UObject):
    GrassVarieties: unreal.WrappedArray[GrassVariety]
    bEnableDensityScaling: bool
    GrassMesh: engine.StaticMesh
    GrassDensity: float
    PlacementJitter: float
    StartCullDistance: int
    EndCullDistance: int
    RandomRotation: bool
    AlignToSurface: bool



class LandscapeHeightfieldCollisionComponent(engine.PrimitiveComponent):
    ComponentLayerInfos: unreal.WrappedArray[LandscapeLayerInfoObject]
    SectionBaseX: int
    SectionBaseY: int
    CollisionSizeQuads: int
    CollisionScale: float
    SimpleCollisionSizeQuads: int
    CollisionQuadFlags: unreal.WrappedArray[int]
    HeightfieldGuid: core_uobject.Guid
    CachedLocalBox: core_uobject.Box
    CookedPhysicalMaterials: unreal.WrappedArray[engine.PhysicalMaterial]



class LandscapeInfo(unreal.UObject):
    LandscapeGuid: core_uobject.Guid
    ComponentSizeQuads: int
    SubsectionSizeQuads: int
    ComponentNumSubsections: int
    DrawScale: core_uobject.Vector



class LandscapeInfoMap(unreal.UObject): ...


class LandscapeLayerInfoObject(unreal.UObject):
    LayerName: str
    PhysMaterial: engine.PhysicalMaterial
    Hardness: float
    AutoPaintType: int
    LayerPriority: int
    LayerIndex: int
    LayerUsageDebugColor: core_uobject.LinearColor



class LandscapeMaterialInstanceConstant(engine.MaterialInstanceConstant):
    bIsLayerThumbnail: bool
    bDisableTessellation: bool
    bMobile: bool
    bEditorToolUsage: bool



class LandscapeMeshCollisionComponent(LandscapeHeightfieldCollisionComponent):
    MeshGuid: core_uobject.Guid



class LandscapeMeshProxyActor(engine.Actor):
    LandscapeMeshProxyComponent: LandscapeMeshProxyComponent



class LandscapeMeshProxyComponent(engine.StaticMeshComponent):
    LandscapeGuid: core_uobject.Guid
    ProxyComponentBases: unreal.WrappedArray[core_uobject.IntPoint]
    ProxyLOD: int



class LandscapeSplinesComponent(engine.PrimitiveComponent):
    ControlPoints: unreal.WrappedArray[LandscapeSplineControlPoint]
    Segments: unreal.WrappedArray[LandscapeSplineSegment]
    CookedForeignMeshComponents: unreal.WrappedArray[engine.MeshComponent]



class LandscapeSplineControlPoint(unreal.UObject):
    Location: core_uobject.Vector
    Rotation: core_uobject.Rotator
    Width: float
    SideFalloff: float
    EndFalloff: float
    ConnectedSegments: unreal.WrappedArray[LandscapeSplineConnection]
    Points: unreal.WrappedArray[LandscapeSplineInterpPoint]
    Bounds: core_uobject.Box
    LocalMeshComponent: ControlPointMeshComponent



class LandscapeSplineSegment(unreal.UObject):
    Connections: LandscapeSplineSegmentConnection
    SplineInfo: core_uobject.InterpCurveVector
    Points: unreal.WrappedArray[LandscapeSplineInterpPoint]
    Bounds: core_uobject.Box
    LocalMeshComponents: unreal.WrappedArray[engine.SplineMeshComponent]



class LandscapeStreamingProxy(LandscapeProxy): ...


class MaterialExpressionLandscapeAutoPaintLayers(engine.MaterialExpressionCustomOutput):
    AutoPaintSourceLayerName: str
    AutoPaintLayers: unreal.WrappedArray[AutoPaintLayerInput]



class MaterialExpressionLandscapeGrassOutput(engine.MaterialExpressionCustomOutput):
    GrassTypes: unreal.WrappedArray[GrassInput]



class MaterialExpressionLandscapeLayerBlend(engine.MaterialExpression):
    Layers: unreal.WrappedArray[LayerBlendInput]
    ExpressionGUID: core_uobject.Guid



class MaterialExpressionLandscapeLayerCoords(engine.MaterialExpression):
    MappingType: int
    CustomUVType: int
    MappingScale: float
    MappingRotation: float
    MappingPanU: float
    MappingPanV: float



class MaterialExpressionLandscapeLayerSample(engine.MaterialExpression):
    ParameterName: str
    PreviewWeight: float
    ExpressionGUID: core_uobject.Guid



class MaterialExpressionLandscapeLayerSwitch(engine.MaterialExpression):
    LayerUsed: engine.ExpressionInput
    LayerNotUsed: engine.ExpressionInput
    ParameterName: str
    PreviewUsed: bool
    ExpressionGUID: core_uobject.Guid



class MaterialExpressionLandscapeLayerWeight(engine.MaterialExpression):
    Base: engine.ExpressionInput
    Layer: engine.ExpressionInput
    ParameterName: str
    PreviewWeight: float
    ConstBase: core_uobject.Vector
    ExpressionGUID: core_uobject.Guid



class MaterialExpressionLandscapeVisibilityMask(engine.MaterialExpression):
    ExpressionGUID: core_uobject.Guid



class WeightmapLayerAllocationInfo:
    LayerInfo: LandscapeLayerInfoObject
    WeightmapTextureIndex: int
    WeightmapTextureChannel: int



class LandscapeEditToolRenderData:
    ToolMaterial: engine.MaterialInterface
    GizmoMaterial: engine.MaterialInterface
    SelectedType: int
    DebugChannelR: int
    DebugChannelG: int
    DebugChannelB: int
    DataTexture: engine.Texture2D



class GizmoSelectData: ...


class GrassVariety:
    GrassMesh: engine.StaticMesh
    GrassDensity: engine.PerPlatformFloat
    bUseGrid: bool
    PlacementJitter: float
    StartCullDistance: engine.PerPlatformInt
    EndCullDistance: engine.PerPlatformInt
    MinLOD: int
    Scaling: EGrassScaling
    ScaleX: core_uobject.FloatInterval
    ScaleY: core_uobject.FloatInterval
    ScaleZ: core_uobject.FloatInterval
    RandomRotation: bool
    AlignToSurface: bool
    bUseLandscapeLightmap: bool
    LightingChannels: engine.LightingChannels
    bReceivesDecals: bool
    bUseAsOccluder: bool
    bCastDynamicShadow: bool
    bKeepInstanceBufferCPUCopy: bool



class LandscapeInfoLayerSettings:
    LayerInfoObj: LandscapeLayerInfoObject
    LayerName: str



class LandscapeImportLayerInfo: ...


class LandscapeLayerStruct:
    LayerInfoObj: LandscapeLayerInfoObject



class LandscapeEditorLayerSettings: ...


class LandscapeWeightmapUsage:
    ChannelUsage: LandscapeComponent



class LandscapeSplineConnection:
    Segment: LandscapeSplineSegment
    End: bool



class ForeignWorldSplineData: ...


class ForeignSplineSegmentData: ...


class ForeignControlPointData: ...


class LandscapeSplineMeshEntry:
    Mesh: engine.StaticMesh
    MaterialOverrides: unreal.WrappedArray[engine.MaterialInterface]
    bCenterH: bool
    CenterAdjust: core_uobject.Vector2D
    bScaleToWidth: bool
    Scale: core_uobject.Vector
    Orientation: int
    ForwardAxis: int
    UpAxis: int



class LandscapeSplineSegmentConnection:
    ControlPoint: LandscapeSplineControlPoint
    TangentLen: float
    SocketName: str



class LandscapeSplineInterpPoint:
    Center: core_uobject.Vector
    Left: core_uobject.Vector
    Right: core_uobject.Vector
    FalloffLeft: core_uobject.Vector
    FalloffRight: core_uobject.Vector
    StartEndFalloff: float



class AutoPaintLayerInput:
    LayerName: str
    Input: engine.ExpressionInput



class GrassInput:
    Name: str
    GrassType: LandscapeGrassType
    Input: engine.ExpressionInput



class LayerBlendInput:
    LayerName: str
    BlendType: int
    LayerInput: engine.ExpressionInput
    HeightInput: engine.ExpressionInput
    PreviewWeight: float
    ConstLayerInput: core_uobject.Vector
    ConstHeightInput: float



class ELandscapeSetupErrors(enum.Enum):
    LSE_NoLandscapeInfo = 0
    LSE_CollsionXY = 1
    LSE_MAX = 2


class ELandscapeGizmoType(enum.Enum):
    LGT_Height = 0
    LGT_Weight = 1


class EGrassScaling(enum.Enum):
    Free = 0
    LockXY = 1


class ELandscapeLayerAutoPaintType(enum.Enum):
    LSLAPT_AutoPaintMaster = 0
    LSLAPT_AutoPaintChild = 1


class ELandscapeLODFalloff(enum.Enum):
    SquareRoot = 0
    ELandscapeLODFalloff_MAX = 1


class ELandscapeLayerDisplayMode(enum.Enum):
    Alphabetical = 0
    UserSpecific = 1


class ELandscapeLayerPaintingRestriction(enum.Enum):
    UseMaxLayers = 0
    ExistingOnly = 1
    ELandscapeLayerPaintingRestriction_MAX = 2


class ELandscapeAutoPaintActorState(enum.Enum):
    LAPS_AllComponentsBaked = 0
    LAPS_NoAutoPaint = 1
    LAPS_SomeComponentsBaked = 2


class ELandscapeAutoPaintOperation(enum.Enum):
    LAPO_DebugClear = 0
    LAPO_AutoPaintBake = 1
    LAPO_AutoPaintRevert = 2


class ELandscapeImportAlphamapType(enum.Enum):
    Layered = 0
    ELandscapeImportAlphamapType_MAX = 1


class LandscapeSplineMeshOrientation(enum.Enum):
    LSMO_MAX = 0
    LSMO_YUp = 1


class ELandscapeLayerBlendType(enum.Enum):
    LB_AlphaBlend = 0
    LB_HeightBlend = 1


class ELandscapeCustomizedCoordType(enum.Enum):
    LCCT_CustomUV0 = 0
    LCCT_CustomUV1 = 1
    LCCT_WeightMapUV = 2


class ETerrainCoordMappingType(enum.Enum):
    TCMT_XY = 0
    TCMT_MAX = 1
    TCMT_XZ = 2

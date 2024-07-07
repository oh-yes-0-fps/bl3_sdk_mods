from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine



class NavigationSystemV1(engine.NavigationSystemBase):
    MainNavData: NavigationData
    AbstractNavData: NavigationData
    CrowdManagerClass: unreal.UClass
    bAutoCreateNavigationData: bool
    bSpawnNavDataInNavBoundsLevel: bool
    bAllowClientSideNavigation: bool
    bShouldDiscardSubLevelNavData: bool
    bTickWhilePaused: bool
    bSupportRebuilding: bool
    bInitialBuildingLocked: bool
    bSkipAgentHeightCheckWhenPickingNavData: bool
    DataGatheringMode: engine.ENavDataGatheringModeConfig
    bGenerateNavigationOnlyAroundNavigationInvokers: bool
    ActiveTilesUpdateInterval: float
    SupportedAgents: unreal.WrappedArray[engine.NavDataConfig]
    DirtyAreasUpdateFreq: float
    NavDataSet: unreal.WrappedArray[NavigationData]
    NavDataRegistrationQueue: unreal.WrappedArray[NavigationData]
    OperationMode: engine.FNavigationSystemRunMode
    NavigationDataClassName: core_uobject.SoftClassPath
    def SimpleMoveToLocation(self, Controller: engine.Controller, Goal: core_uobject.Vector): ...
    def SimpleMoveToActor(self, Controller: engine.Controller, Goal: engine.Actor): ...
    def ProjectPointToNavigation(self, WorldContextObject: unreal.UObject, Point: core_uobject.Vector, NavData: NavigationData, FilterClass: unreal.UClass, QueryExtent: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def OnNavigationBoundsUpdated(self, NavVolume: NavMeshBoundsVolume): ...
    def K2_ProjectPointToNavigation(self, WorldContextObject: unreal.UObject, Point: core_uobject.Vector, ProjectedLocation: core_uobject.Vector, NavData: NavigationData, FilterClass: unreal.UClass, QueryExtent: core_uobject.Vector, ReturnValue: bool) -> bool: ...
    def K2_GetRandomReachablePointInRadius(self, WorldContextObject: unreal.UObject, Origin: core_uobject.Vector, RandomLocation: core_uobject.Vector, Radius: float, NavData: NavigationData, FilterClass: unreal.UClass, ReturnValue: bool) -> bool: ...
    def K2_GetRandomPointInNavigableRadius(self, WorldContextObject: unreal.UObject, Origin: core_uobject.Vector, RandomLocation: core_uobject.Vector, Radius: float, NavData: NavigationData, FilterClass: unreal.UClass, ReturnValue: bool) -> bool: ...
    def GetRandomReachablePointInRadius(self, WorldContextObject: unreal.UObject, Origin: core_uobject.Vector, Radius: float, NavData: NavigationData, FilterClass: unreal.UClass, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetRandomPointInNavigableRadius(self, WorldContextObject: unreal.UObject, Origin: core_uobject.Vector, Radius: float, NavData: NavigationData, FilterClass: unreal.UClass, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetNavigationSystem(self, WorldContextObject: unreal.UObject, ReturnValue: NavigationSystemV1) -> NavigationSystemV1: ...


class NavigationData(engine.Actor):
    RenderingComp: engine.PrimitiveComponent
    NavDataConfig: engine.NavDataConfig
    bEnableDrawing: bool
    bForceRebuildOnLoad: bool
    bCanBeMainNavData: bool
    bCanSpawnOnRebuild: bool
    bRebuildAtRuntime: bool
    RuntimeGeneration: ERuntimeGenerationType
    ObservedPathsTickInterval: float
    SupportedAreas: unreal.WrappedArray[SupportedAreaData]



class AbstractNavData(NavigationData): ...


class CrowdManagerBase(unreal.UObject): ...


class HavokNavData(unreal.UObject): ...


class NavigationQueryFilter(unreal.UObject):
    Areas: unreal.WrappedArray[NavigationFilterArea]
    IncludeFlags: NavigationFilterFlags
    ExcludeFlags: NavigationFilterFlags



class HavokNavigationQueryFilter(NavigationQueryFilter): ...


class GbxNavLayerBase(engine.DataAsset): ...


class HavokNavLayer(engine.HavokNavLayerBase):
    GbxNavLayer: GbxNavLayerBase
    DrawColor: core_uobject.Color



class HavokNavLayerRegistry(unreal.UObject): ...


class HavokNavMesh(HavokNavData): ...


class NavTraversalData(engine.DataAsset):
    Settings: HavokTraversalAnalysisSettings



class HavokNavMeshGenerationSettings(unreal.UObject):
    QuantizationGridSize: float
    MaxWalkableSlope: float
    DegenerateAreaThreshold: float
    DegeneratedWidthThreshold: float
    ConvexThreshold: float
    MaxNumEdgesPerFace: int
    EdgeMatchingSettings: HavokNavMeshEdgeMatchingSettings
    StreamEdgeMatchingSettings: HavokNavMeshEdgeMatchingSettings
    EdgeMatchingMetric: int
    EdgeConnectionIterations: int
    RegionPruningSettings: HavokNavMeshRegionPruningSettings
    bFixupOverlappingTriangles: bool
    OverlappingTrianglesSettings: HavokNavMeshOverlappingTrianglesSettings
    bWeldInputVertices: bool
    WeldThreshold: float
    bEnableSimplification: bool
    SimplificationSettings: HavokNavMeshSimplificationSettings
    TraversalAnalysisSettings: HavokTraversalAnalysisSettings
    TraversalSettingsName: core_uobject.SoftObjectPath
    bSaveInputSnapshot: bool



class HavokNavMeshLayer(HavokNavLayer):
    CharacterRadius: float
    CharacterHalfHeight: float
    UserEdgeEntryDistance: float
    bErodeWidth: bool



class HavokNavMeshLayer_Default(HavokNavMeshLayer): ...


class HavokNavVolume(HavokNavData): ...


class HavokNavVolumeGenerationSettings(unreal.UObject):
    ChunkSettings: HavokNavVolumeChunkSettings
    BorderSettings: HavokNavVolumeBorderSettings
    MergingSettings: HavokNavVolumeMergingSettings
    PruningSettings: HavokNavVolumePruningSettings
    bSaveInputSnapshot: bool



class HavokNavVolumeLayer(HavokNavLayer):
    CharacterRadius: float
    CellWidth: float
    ResolutionRoundingMode: int



class HavokNavVolumeLayer_Default(HavokNavVolumeLayer): ...


class HavokTraversalType(unreal.UObject):
    MaxPlanarAngle: float
    MaxRelativeSlopeAngle: float
    BaseCost: float
    AssociatedLayers: unreal.WrappedArray[GbxNavLayerBase]
    GbxUserEdge: GbxUserEdgeBase
    UserEdge: unreal.UClass



class HavokTraversalType_ClimbUp(HavokTraversalType):
    MaxUnderhang: float
    MinUpHeight: float
    MaxUpHeight: float
    GrabAngle: float
    GrabScanDepth: float
    GrabMaxProfileAngle: float
    VerticalLipHeight: float
    ResolveHangExtraDist: float



class HavokTraversalType_DropDown(HavokTraversalType):
    MinDropDistance: float
    MaxDropDistance: float
    MaxUnderhang: float
    MinUnderhang: float
    VerticalLipHeight: float



class HavokTraversalType_Jump(HavokTraversalType):
    MaxHorizontalDistance: float
    MinHorizontalDistance: float
    MaxUpHeight: float
    MaxDownHeight: float
    VerticalApex: float



class HavokTraversalType_Vault(HavokTraversalType):
    MinWallWidth: float
    MaxWallWidth: float
    MinWallHeight: float
    MaxWallHeight: float
    MaxUpHeight: float
    MaxDownHeight: float
    VerticalApex: float
    HandPlantAngle: float
    HandPlantLeftExtent: float
    HandPlantRightExtent: float
    HandPlantMaxProfileAngle: float



class GbxUserEdgeBase(engine.DataAsset): ...


class HavokUserEdge(unreal.UObject):
    GbxUserEdge: GbxUserEdgeBase
    ReverseEdge: unreal.UClass
    DrawColor: core_uobject.Color
    bAlignEdges: bool
    bLimitDistanceMin: bool
    DistanceMin: float
    bLimitDistanceMax: bool
    DistanceMax: float
    bLimitHeightMin: bool
    HeightMin: float
    bLimitHeightMax: bool
    HeightMax: float
    bZeroWidthEntry: bool
    bZeroWidthExit: bool
    bTeleportEntry: bool
    bTeleportExit: bool
    TeleportEdges: unreal.WrappedArray[unreal.UClass]



class NavArea(engine.NavAreaBase):
    DefaultCost: float
    FixedAreaEnteringCost: float
    DrawColor: core_uobject.Color
    SupportedAgents: engine.NavAgentSelector
    bSupportsAgent1: bool
    bSupportsAgent2: bool
    bSupportsAgent3: bool
    bSupportsAgent4: bool
    bSupportsAgent5: bool
    bSupportsAgent6: bool
    bSupportsAgent7: bool
    bSupportsAgent8: bool
    bSupportsAgent9: bool
    bSupportsAgent11: bool
    bSupportsAgent12: bool
    bSupportsAgent13: bool
    bSupportsAgent14: bool
    bSupportsAgent15: bool
    GbxNavArea: unreal.UObject
    HavokNavMaterial: EHavokNavMaterial
    IgnoreLayers: unreal.WrappedArray[GbxNavLayerBase]
    EffectiveArea: unreal.UClass



class NavArea_Default(NavArea): ...


class NavArea_LowHeight(NavArea): ...


class NavArea_Null(NavArea): ...


class NavArea_Obstacle(NavArea): ...


class NavAreaMeta(NavArea): ...


class NavAreaMeta_SwitchByAgent(NavAreaMeta):
    Agent1Area: unreal.UClass
    Agent2Area: unreal.UClass
    Agent3Area: unreal.UClass
    Agent4Area: unreal.UClass
    Agent5Area: unreal.UClass
    Agent6Area: unreal.UClass
    Agent7Area: unreal.UClass
    Agent8Area: unreal.UClass
    Agent9Area: unreal.UClass
    Agent11Area: unreal.UClass
    Agent12Area: unreal.UClass
    Agent13Area: unreal.UClass
    Agent14Area: unreal.UClass
    Agent15Area: unreal.UClass



class NavCollision(engine.NavCollisionBase):
    CylinderCollision: unreal.WrappedArray[NavCollisionCylinder]
    BoxCollision: unreal.WrappedArray[NavCollisionBox]
    AreaClass: unreal.UClass
    bGatherConvexGeometry: bool



class NavigationGraph(NavigationData): ...


class NavigationGraphNode(engine.Actor): ...


class NavigationGraphNodeComponent(engine.SceneComponent):
    Node: NavGraphNode
    NextNodeComponent: NavigationGraphNodeComponent
    PrevNodeComponent: NavigationGraphNodeComponent



class NavigationInvokerComponent(engine.ActorComponent):
    TileGenerationRadius: float
    TileRemovalRadius: float



class NavigationPath(unreal.UObject):
    PathPoints: unreal.WrappedArray[core_uobject.Vector]
    RecalculateOnInvalidation: int
    def IsValid(self, ReturnValue: bool) -> bool: ...
    def IsStringPulled(self, ReturnValue: bool) -> bool: ...
    def IsPartial(self, ReturnValue: bool) -> bool: ...
    def GetPathLength(self, ReturnValue: float) -> float: ...
    def GetPathCost(self, ReturnValue: float) -> float: ...
    def GetDebugString(self, ReturnValue: str) -> str: ...
    def EnableRecalculationOnInvalidation(self, DoRecalculation: int): ...
    def EnableDebugDrawing(self, bShouldDrawDebugData: bool, PathColor: core_uobject.LinearColor): ...


class NavigationPathGenerator(core_uobject.Interface): ...


class NavigationSystemModuleConfig(engine.NavigationSystemConfig):
    bStrictlyStatic: bool
    bCreateOnClient: bool
    bAutoSpawnMissingNavData: bool
    bSpawnNavDataInNavBoundsLevel: bool



class NavigationTestingActor(engine.Actor):
    CapsuleComponent: engine.CapsuleComponent
    InvokerComponent: NavigationInvokerComponent
    bActAsNavigationInvoker: bool
    NavAgentProps: engine.NavAgentProperties
    QueryingExtent: core_uobject.Vector
    MyNavData: NavigationData
    ProjectedLocation: core_uobject.Vector
    bProjectedLocationValid: bool
    bSearchStart: bool
    bUseHierarchicalPathfinding: bool
    bGatherDetailedInfo: bool
    bDrawDistanceToWall: bool
    bShowNodePool: bool
    bShowBestPath: bool
    bShowDiffWithPreviousStep: bool
    bShouldBeVisibleInGame: bool
    CostDisplayMode: int
    TextCanvasOffset: core_uobject.Vector2D
    bPathExist: bool
    bPathIsPartial: bool
    bPathSearchOutOfNodes: bool
    PathfindingTime: float
    PathCost: float
    PathfindingSteps: int
    OtherActor: NavigationTestingActor
    FilterClass: unreal.UClass
    ShowStepIndex: int
    OffsetFromCornersDistance: float



class NavLinkComponent(engine.PrimitiveComponent):
    Links: unreal.WrappedArray[engine.NavigationLink]



class NavRelevantComponent(engine.ActorComponent):
    bAttachToOwnersRoot: bool
    CachedNavParent: unreal.UObject
    def SetNavigationRelevancy(self, bRelevant: bool): ...


class NavLinkCustomComponent(NavRelevantComponent):
    EnabledAreaClass: unreal.UClass
    DisabledAreaClass: unreal.UClass
    LinkRelativeStart: core_uobject.Vector
    LinkRelativeEnd: core_uobject.Vector
    LinkDirection: int
    bLinkEnabled: bool
    bNotifyWhenEnabled: bool
    bNotifyWhenDisabled: bool
    bCreateBoxObstacle: bool
    ObstacleOffset: core_uobject.Vector
    ObstacleExtent: core_uobject.Vector
    ObstacleAreaClass: unreal.UClass
    BroadcastRadius: float
    BroadcastInterval: float
    BroadcastChannel: int



class NavLinkCustomInterface(core_uobject.Interface): ...


class NavLinkHostInterface(core_uobject.Interface): ...


class NavLinkRenderingComponent(engine.PrimitiveComponent): ...


class NavLinkTrivial(engine.NavLinkDefinition): ...


class NavMeshBoundsVolume(engine.Volume):
    SupportedAgents: engine.NavAgentSelector



class NavMeshRenderingComponent(engine.PrimitiveComponent): ...


class NavModifierComponent(NavRelevantComponent):
    AreaClass: unreal.UClass
    FailsafeExtent: core_uobject.Vector
    bIncludeAgentHeight: bool
    def SetAreaClass(self, NewAreaClass: unreal.UClass): ...


class NavModifierVolume(engine.Volume):
    AreaClass: unreal.UClass
    def SetAreaClass(self, NewAreaClass: unreal.UClass): ...


class NavNodeInterface(core_uobject.Interface): ...


class NavTestRenderingComponent(engine.PrimitiveComponent): ...


class RecastFilter_UseDefaultArea(NavigationQueryFilter): ...


class RecastNavMesh(NavigationData):
    bDrawTriangleEdges: bool
    bDrawPolyEdges: bool
    bDrawFilledPolys: bool
    bDrawNavMeshEdges: bool
    bDrawTileBounds: bool
    bDrawPathCollidingGeometry: bool
    bDrawTileLabels: bool
    bDrawPolygonLabels: bool
    bDrawDefaultPolygonCost: bool
    bDrawLabelsOnPathNodes: bool
    bDrawNavLinks: bool
    bDrawFailedNavLinks: bool
    bDrawClusters: bool
    bDrawOctree: bool
    bDrawOctreeDetails: bool
    bDistinctlyDrawTilesBeingBuilt: bool
    bDrawNavMesh: bool
    DrawOffset: float
    bFixedTilePoolSize: bool
    TilePoolSize: int
    TileSizeUU: float
    CellSize: float
    CellHeight: float
    AgentRadius: float
    AgentHeight: float
    AgentMaxHeight: float
    AgentMaxSlope: float
    AgentMaxStepHeight: float
    MinRegionArea: float
    MergeRegionSize: float
    MaxSimplificationError: float
    MaxSimultaneousTileGenerationJobsCount: int
    TileNumberHardLimit: int
    PolyRefTileBits: int
    PolyRefNavPolyBits: int
    PolyRefSaltBits: int
    DefaultDrawDistance: float
    DefaultMaxSearchNodes: float
    DefaultMaxHierarchicalSearchNodes: float
    RegionPartitioning: int
    LayerPartitioning: int
    RegionChunkSplits: int
    LayerChunkSplits: int
    bSortNavigationAreasByCost: bool
    bPerformVoxelFiltering: bool
    bMarkLowHeightAreas: bool
    bFilterLowSpanSequences: bool
    bFilterLowSpanFromTileCache: bool
    bDoFullyAsyncNavDataGathering: bool
    bUseBetterOffsetsFromCorners: bool
    bStoreEmptyTileLayers: bool
    bUseVirtualFilters: bool
    bAllowNavLinkAsPathEnd: bool
    bUseVoxelCache: bool
    TileSetUpdateInterval: float
    HeuristicScale: float
    VerticalDeviationFromGroundCompensation: float



class RecastNavMeshDataChunk(engine.NavigationDataChunk): ...


class HavokTraversalAnalysisSettings:
    TraversalTypes: unreal.WrappedArray[HavokTraversalType]
    MinEdgeLength: float
    MaxSectionDistance: float
    RaiseEdgeHeightLimit: float



class HavokNavMeshSimplificationSettings:
    MaxBorderSimplifyArea: float
    MaxConcaveBorderSimlifyArea: float
    MinCorridorWidth: float
    MaxCorridorWidth: float
    HoleReplacementArea: float
    AabbReplacementAreaFraction: float
    MaxLoopShrinkFraction: float
    MaxBorderHeightError: float
    MaxBorderDistanceError: float
    MaxPartitionSize: int
    bUseHeightPartitioning: bool
    MaxPartitionHeightError: float
    bUseConservativeHeightPartitioning: bool
    HertelMehlhornHeightError: float
    CosPlanarityThreshold: float
    NonConvexityThreshold: float
    BoundaryEdgeFilterThreshold: float
    MaxSharedVertexHorizontalError: float
    MaxSharedVertexVerticalError: float
    MaxBoundaryVertexHorizontalError: float
    MaxBoundaryVertexVerticalError: float
    bMergeLongestEdgesFirst: bool
    ExtraVertexSettings: HavokNavMeshExtraVertexSettings



class HavokNavMeshExtraVertexSettings:
    VertexSelectionMethod: int
    VertexFraction: float
    AreaFraction: float
    MinPartitionArea: float
    NumSmoothingIterations: int
    IterationDamping: float
    bAddVerticesOnBoundaryEdges: bool
    bAddVerticesOnPartitionBorders: bool
    BoundaryEdgeSplitLength: float
    PartitionBordersSplitLength: float



class HavokNavMeshOverlappingTrianglesSettings:
    CoplanarityTolerance: float
    RayCastLengthMultiplier: float
    WalkableTriangleSetting: int



class HavokNavMeshRegionPruningSettings:
    MinRegionArea: float
    MinDistanceToSeedPoints: float
    BorderPreservationTolerance: float
    bPreserveVerticalBorderRegions: bool
    bPruneBeforeTriangulation: bool
    bUseRegionSeeds: bool



class HavokNavMeshEdgeMatchingSettings:
    MaxStepHeight: float
    MaxSeparation: float
    MaxOverhang: float
    BehindFaceTolerance: float
    CosPlanarAlignmentAngle: float
    CosVerticalAlignmentAngle: float
    MinEdgeOverlap: float
    EdgeParallelTolerance: float
    EdgeTraversibilityHorizontalEpsilon: float
    bUseSafeEdgeTraversibilityHorizontalEpsilon: bool



class HavokNavSectionFixedBound:
    Layer: unreal.UClass
    WorldBoxBound: core_uobject.Box
    WorldConvexHullPoints: unreal.WrappedArray[core_uobject.Vector]
    DominationGuid: core_uobject.Guid



class HavokNavVolumePruningSettings:
    MinRegionVolume: float
    MinDistanceToSeedPoints: float



class HavokNavVolumeMergingSettings:
    NodeWeight: float
    EdgeWeight: float
    bEstimateNewEdges: bool
    IterationsStabilizationThreshold: float
    MaxMergingIterations: float
    RandomSeed: int
    Multiplier: float
    bUseSimpleFirstMergePass: bool



class HavokNavVolumeBorderSettings:
    Border: float
    bUseBorderCells: bool



class HavokNavVolumeChunkSettings:
    bDoGreedyMergeAfterCombine: bool



class NavCollisionBox:
    Offset: core_uobject.Vector
    Extent: core_uobject.Vector



class NavCollisionCylinder:
    Offset: core_uobject.Vector
    Radius: float
    Height: float



class SupportedAreaData:
    AreaClassName: str
    AreaID: int
    AreaClass: unreal.UClass



class NavGraphNode:
    Owner: unreal.UObject



class NavGraphEdge: ...


class NavigationFilterFlags:
    bNavFlag1: bool
    bNavFlag2: bool
    bNavFlag3: bool
    bNavFlag4: bool
    bNavFlag5: bool
    bNavFlag6: bool
    bNavFlag7: bool
    bNavFlag8: bool
    bNavFlag9: bool
    bNavFlag11: bool
    bNavFlag12: bool
    bNavFlag13: bool
    bNavFlag14: bool
    bNavFlag15: bool



class NavigationFilterArea:
    AreaClass: unreal.UClass
    TravelCostOverride: float
    EnteringCostOverride: float
    bIsExcluded: bool
    bOverrideTravelCost: bool
    bOverrideEnteringCost: bool



class EHavokNavMeshVertexSelectionMethod(enum.Enum):
    PROPORTIONAL_TO_VERTICES = 0
    PROPORTIONAL_TO_MAX = 1


class EHavokNavMeshWalkableTriangleSeetings(enum.Enum):
    PREFER_WALKABLE = 0
    PREFER_UNWALKABLE = 1


class EHavokNavMeshCharacterWidthUsage(enum.Enum):
    BLOCK_EDGES = 0
    SHRINK_NAV_MESH = 1


class EHavokNavMeshEdgeMatchingMetric(enum.Enum):
    ORDER_BY_DISTANCE = 0
    ORDER_BY_MAX = 1


class EHavokNavVolumeCellWidthToResolutionRounding(enum.Enum):
    RoundToNearest = 0
    EHavokNavVolumeCellWidthToResolutionRounding_MAX = 1


class EHavokUserEdgeDirection(enum.Enum):
    AToB = 0
    BToA = 1
    EHavokUserEdgeDirection_MAX = 2


class EHavokNavMaterial(enum.Enum):
    Walkable = 0
    Cutting = 1
    EHavokNavMaterial_MAX = 2


class ERuntimeGenerationType(enum.Enum):
    DynamicModifiersOnly = 0
    Dynamic = 1
    ERuntimeGenerationType_MAX = 2


class ENavCostDisplay(enum.Enum):
    HeuristicOnly = 0
    RealCostOnly = 1


class ERecastPartitioning(enum.Enum):
    Watershed = 0
    ChunkyMonotone = 1

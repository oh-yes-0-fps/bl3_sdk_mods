from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import gbx_runtime
from . import aimodule
from . import gbx_game_system_core
from . import navigation_system


class GbxNavSystem(navigation_system.NavigationSystemV1):
    GbxNavWorld: GbxNavWorld


class GbxNavCharacterMovementComponent(
    gbx_game_system_core.GbxCharacterMovementComponent
):
    NavMovementOptions: GbxNavMovementOptions
    NavClientPopDistance: float
    NavAvoidanceOptions: GbxNavAvoidanceOptions
    NavSlowdownOptions: GbxNavSlowdownData
    bOverrideSlowdownNearGoal: bool
    SlowdownSpeedOverride: gbx_game_system_core.StanceFloatValue
    GbxNavWorld: GbxNavWorld
    GbxNavComponent: GbxNavComponent
    Agent: GbxNavAgent
    PathingData: GbxNavPathingData
    ForcedNavMeshLayer: GbxNavMeshLayer
    bOverrideMaxAcceleration: bool
    StanceMaxAcceleration: float


class GbxNavComponent(gbx_game_system_core.NavComponent):
    ForwardState: GbxNavForwardState
    StuckState: GbxNavStuckState
    GbxNavWorld: GbxNavWorld
    OverrideMovementData: HavokMovementData
    OverridePathFindingData: HavokPathFindingData
    MyCapsule: engine.CapsuleComponent
    MyAIController: aimodule.AIController
    MyMovement: GbxNavCharacterMovementComponent
    Agent: GbxNavAgent
    UserEdgeState: GbxUserEdgeState
    NavCorrecter: GbxNavCorrecter
    Reachability: GbxReachabilityState
    MovementOptions: GbxNavMovementOptions
    AvoidanceOptions: GbxNavAvoidanceOptions

    def TryMoving(self, fDuration: float): ...
    def SetPathFindingData(self, NewPathFindingData: HavokPathFindingData): ...
    def ResetPathFindingData(self): ...
    def GetPathFindingData(self) -> HavokPathFindingData: ...


class GbxNavWorld(navigation_system.NavigationData):
    UserEdgeManager: GbxUserEdgeManager
    PainterManager: GbxPainterManager
    FlyStreamingData: GbxNavStreamingData
    MeshStreamingData: GbxNavStreamingData
    MeshLayers: GbxNavLayerState
    FlyLayers: GbxNavLayerState
    ReachabilityBuilding: GbxNavComponent
    ReachabilityQueue: unreal.WrappedArray[GbxNavComponent]
    NavComps: unreal.WrappedArray[GbxNavComponent]
    ReachabilityTracker: GbxReachabilityTracker
    MaxClearanceFillsPerStep: int
    MaxClearanceChecksPerStep: int
    bAsyncProcessingEnabled: bool
    bAsyncAgentUpdatesEnabled: bool
    DefaultMeshLayer: core_uobject.SoftObjectPath
    DefaultFlyLayer: core_uobject.SoftObjectPath
    DefaultNavArea: core_uobject.SoftObjectPath
    NullNavArea: core_uobject.SoftObjectPath
    AllNavAreas: unreal.WrappedArray[core_uobject.SoftObjectPath]
    LoadedAllNavAreas: unreal.WrappedArray[GbxNavArea]
    SectionsWithDirtyTransforms: unreal.WrappedArray[GbxNavSectionComponent]
    MeshGenSettings: navigation_system.HavokNavMeshGenerationSettings
    VolumeGenSettings: navigation_system.HavokNavVolumeGenerationSettings


class AIVehicleFlightComponent(engine.FloatingPawnMovement):
    RotationRate: core_uobject.Rotator
    GbxNavComponent: GbxNavComponent
    VelocityScaleDuringDescent: float
    RotationScaleDuringDescent: float
    LateralDistanceToStartDescent: float
    VelocityScaleDuringAscent: float
    RotationScaleDuringAscent: float
    MaxPitchInDegrees: float
    MaxRollInDegrees: float
    FlightState: FlightState

    def OnRep_FlightState(self): ...


class GbxNavAnimTable(gbx_game_system_core.GbxAnimTable):
    Type: EGbxNavAnimTableType
    MinStopDistance: float
    MaxInterpDistance: float
    AutoFillAngle: float


class GbxAnimStateManager_AINav(engine.GbxAnimStateManager):
    Type: gbx_game_system_core.ENavAnimState
    AnimTable: GbxNavAnimTable
    BlendSpaceRef: gbx_game_system_core.AnimActionDef
    GbxCharAnimInstance: gbx_game_system_core.GbxCharacterAnimInstance
    GbxCharMoveComponent: gbx_game_system_core.GbxCharacterMovementComponent
    ResolvedBlendSpace: engine.BlendSpaceBase
    ResolvedBlendSpaceYawMin: float
    ResolvedBlendSpaceYawMax: float
    BlendSpace: engine.BlendSpaceBase

    def Owner_PostBeginPlay(self): ...


class GbxAnimStateManager_NavIdle(engine.GbxAnimStateManager): ...


class GbxNavIdleTurnTable(gbx_game_system_core.GbxAnimTable): ...


class GbxAnimStateManager_NavIdleTurn(
    gbx_game_system_core.GbxAnimStateManager_RootMotion
): ...


class GbxAnimStateManager_NavTable(GbxAnimStateManager_NavIdleTurn): ...


class GbxAnimStateManager_NavHop(
    gbx_game_system_core.GbxAnimStateManager_RootMotion
): ...


class GbxNavArea(engine.GbxNavAreaBase):
    DrawColor: core_uobject.Color
    IgnoreLayers: unreal.WrappedArray[GbxNavMeshLayer]
    EffectiveArea: GbxNavArea
    HavokNavMaterial: navigation_system.EHavokNavMaterial


class GbxNavAreaData(engine.DataAsset):
    NavAreas: unreal.WrappedArray[GbxNavAreaItem]


class GbxNavBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def SetAINavPathType(self, Actor: engine.Actor, PathType: EGbxPathType): ...
    def ResourceUnlockAvoidance(self, Actor: engine.Actor, Reason: str): ...
    def ResourceLockAvoidance(self, Actor: engine.Actor, Reason: str): ...
    def ForceNavMeshLayer(
        self, Actor: engine.Actor, ForcedNavMeshLayer: GbxNavMeshLayer
    ): ...
    def FindNavMeshPointForActor(
        self,
        Actor: engine.Actor,
        Point: core_uobject.Vector,
        Radius: float,
        Result: core_uobject.Vector,
    ) -> bool: ...
    def FindNavMeshPoint(
        self,
        WorldContextObject: unreal.UObject,
        Point: core_uobject.Vector,
        Radius: float,
        Result: core_uobject.Vector,
        Layer: GbxNavMeshLayer,
    ) -> bool: ...


class GbxNavBoxComponent(engine.BoxComponent):
    AutoResize: gbx_runtime.GbxTriggerProperty

    def DoAutoResize(self): ...


class GbxNavLayer(navigation_system.GbxNavLayerBase):
    DrawColor: core_uobject.Color


class GbxNavFlyLayer(GbxNavLayer):
    MaxAgentRadius: float
    CellWidth: float
    RoundingMode: EGbxNavFlyRoundingMode


class GbxNavSection(navigation_system.NavMeshBoundsVolume):
    SectionComponent: GbxNavSectionComponent


class GbxNavFlySection(GbxNavSection):
    FlySectionComponent: GbxNavFlySectionComponent


class GbxNavSectionComponent(engine.PrimitiveComponent):
    SectionID: int
    StreamingGuid: core_uobject.Guid
    GbxNavWorld: GbxNavWorld
    bAddAllConnectedComponentsToBounds: bool
    BuildTransform: core_uobject.Transform


class GbxNavFlySectionComponent(GbxNavSectionComponent):
    FlyLayer: GbxNavFlyLayer
    BuildFlyLayer: GbxNavFlyLayer
    bDrawBoundingFaces: bool
    bDrawCells: bool
    bDrawFaces: bool
    DrawBoxSize: float
    DrawCullDistance: float
    NavVolume: navigation_system.HavokNavVolume
    CellGroups: unreal.WrappedArray[int]
    Layer: unreal.UClass
    BuildLayer: unreal.UClass


class GbxNavGlobalData(gbx_runtime.GbxDataAsset):
    DefaultMeshLayer: GbxNavMeshLayer
    DefaultFlyLayer: GbxNavFlyLayer
    DefaultMeshArea: GbxNavArea
    NullMeshArea: GbxNavArea
    AllMeshAreas: unreal.WrappedArray[GbxNavArea]
    DefaultUserEdge: GbxUserEdge
    GlobalUserEdges: unreal.WrappedArray[GbxUserEdge]


class GbxNavMeshLayer(GbxNavLayer):
    MaxAgentHalfHeight: float
    MaxAgentRadius: float
    bSetRadiusManually: bool
    UserEdgeDistance: float
    bSetUserEdgeDistanceManually: bool


class GbxNavMeshPainter(engine.Volume):
    PainterComponent: GbxNavMeshPainterComponent

    def SetPainterEnabled(self, bNewEnabled: bool): ...
    def IsPainterEnabled(self) -> bool: ...


class GbxNavMeshPainterComponent(engine.ActorComponent):
    bAlwaysEnabled: bool
    bEnabled: bool
    IdleTime: float
    PainterType: EGbxPainterType
    GbxNavArea: GbxNavArea
    AssociatedComponentNames: unreal.WrappedArray[str]
    PainterId: int
    PainterMovedThreshold: float
    bBlocksAutoGeneratedUserEdges: bool
    Painters: unreal.WrappedArray[GbxPainterItem]
    NavArea: unreal.UClass

    def SetPainterEnabled(self, bNewEnabled: bool): ...
    def SetPainterAlwaysEnabled(self, bNewAlwaysEnabled: bool): ...
    def ResetToStatic(self): ...
    def IsPainterEnabled(self) -> bool: ...


class GbxNavMeshSection(GbxNavSection):
    MeshSectionComponent: GbxNavMeshSectionComponent


class GbxNavMeshSectionComponent(GbxNavSectionComponent):
    MeshLayer: GbxNavMeshLayer
    BuildMeshLayer: GbxNavMeshLayer
    bAutoAddUserEdges: bool
    NavMesh: navigation_system.HavokNavMesh
    Layer: unreal.UClass
    BuildLayer: unreal.UClass


class GbxNavUserEdgeTrailComponent(engine.ActorComponent):
    GbxUserEdge: GbxUserEdge
    EdgeWidth: float
    AgentRadius: float
    AgentHalfHeight: float
    NavCheckDistance: float
    ValidEdgeLength: gbx_runtime.NumericRange
    MaxActiveEdges: int
    TraceRadius: float
    GbxNavWorld: GbxNavWorld
    AgentProps: GbxNavAgentProperties
    UserEdge: unreal.UClass


class HavokPathFollowingComponent(aimodule.PathFollowingComponent): ...


class GbxPathFollowingComponent(HavokPathFollowingComponent): ...


class GbxUserEdge(navigation_system.GbxUserEdgeBase):
    ReverseEdge: GbxUserEdge
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
    TeleportEdges: unreal.WrappedArray[GbxUserEdge]


class GbxUserEdgeBlocker(engine.Volume): ...


class HavokMovementData(engine.DataAsset): ...


class HavokNavObstacle(unreal.UObject):
    SphereRadius: float
    bUseSphere: bool
    BoxSize: core_uobject.Vector
    bUseBox: bool
    Scale: core_uobject.Vector
    NavArea: GbxNavArea
    PrimitiveBase: engine.PrimitiveComponent


class HavokNavObstacleComponent(engine.PrimitiveComponent):
    Obstacle: HavokNavObstacle

    def UnlockObstacle(self, Reason: str): ...
    def LockObstacle(self, Reason: str): ...


class HavokPathFindingData(engine.DataAsset):
    UserEdges: unreal.WrappedArray[HavokUserEdgeItem]
    UserEdgeTeleports: unreal.WrappedArray[HavokUserEdgeTeleportItem]
    DefaultTeleportAction: unreal.UClass


class HavokStreamingSet(unreal.UObject):
    SectionIdA: int
    SectionIdB: int


class HavokUserEdge_Jump(navigation_system.HavokUserEdge): ...


class HavokUserEdgeActor(engine.Actor):
    EdgeEnd: core_uobject.Transform
    UserEdgeComponent: HavokUserEdgeComponent

    def SetEdgeEnabled(self, bNewEnabled: bool): ...
    def IsEdgeEnabled(self) -> bool: ...


class HavokUserEdgeComponent(engine.PrimitiveComponent):
    bEnabled: bool
    EdgeEnd: core_uobject.Transform
    EdgeBeginWidth: float
    EdgeEndWidth: float
    Direction: EGbxUserEdgeDirection
    GbxUserEdge: GbxUserEdge
    TeleportRadius: float
    TeleportEdges: unreal.WrappedArray[HavokUserEdgeComponent]
    bAnchorEnd: bool
    EndAnchorBase: engine.Actor
    EndAnchorTransform: core_uobject.Transform
    RegisteredEndAnchorRoot: engine.SceneComponent
    EdgeID: int
    UserEdge: unreal.UClass

    def SetEdgeEnabled(self, bNewEnabled: bool): ...
    def IsEdgeEnabled(self) -> bool: ...
    def AnchorDestroyed(self, Actor: engine.Actor): ...


class HavokUserEdgePreviewComponent(engine.PrimitiveComponent):

    def OnBlueprintCompiled(self, BP: engine.Blueprint): ...


class VehicleSplineConsumerInterface(core_uobject.Interface): ...


class VehicleSplineInterface(core_uobject.Interface): ...


class GbxAvoidanceProperties:
    WallFollowingAngle: float
    DodgingPenalty: float
    VelocityHysteresis: float
    SidednessChangingPenalty: float
    CollisionPenalty: float
    PenetrationPenalty: float
    Weight: float
    Priority: int
    MaxSpeedScale: float
    SensorSizeScale: float
    RadiusScale: float
    GoalDistanceOffsetPct: float
    DirectionHysteresis: float
    bUseSimplifiedAvoiance: bool


class GbxNavPathingData:
    Areas: GbxNavAreaData
    UserEdges: HavokPathFindingData


class GbxNavAgent:
    Props: GbxNavAgentProperties
    GbxNavWorld: GbxNavWorld
    Context: engine.Actor


class GbxNavAgentProperties:
    PathingData: GbxNavPathingData


class GbxNavSlowdownData:
    bSlowdownNearGoal: bool
    SlowdownSpeed: gbx_game_system_core.StanceFloatValue
    SlowdownDistanceMin: float
    SlowdownDistanceMax: float


class GbxNavAvoidanceOptions:
    bAvoidanceSteering: bool
    bAvoidanceObstacle: bool
    bAvoidPawnsBehindMe: bool
    bAvoidWithNoGoal: bool
    AvoidanceProperties: GbxAvoidanceProperties


class GbxNavMovementOptions:
    PathFindingData: HavokPathFindingData
    PathingData: GbxNavPathingData
    MoveStyleDefault: EGbxNavMoveStyleDefault
    bCanReverse: bool
    ReverseGoalDistance: float
    bCanChangePitchWhenStrafeFlying: bool
    IdleDirectionTime: float
    NearUserEdgeTimeThreshold: float
    UserEdgeEnterDistancePercent: float
    bMustBeFacingUserEdgeBeforeEntering: bool


class GbxNavGoalModifiers:
    OffsetType: EGbxOffsetType
    Offset: core_uobject.Vector
    bAddAgentRadius: bool
    bAddAgentHeight: bool
    bAddGoalRadius: bool
    bAddGoalHeight: bool
    bAdjustHeightForMelee: bool
    bCenterOnFloor: bool
    VerticalFlyOffset: float


class FlightState:
    CurrentMovementState: int
    VehicleSplineActor: engine.Actor
    DropOffSpawner: engine.Actor
    AscentTargetLocationZ: float
    AscentTargetRotation: core_uobject.Rotator


class GbxNavIdleTurnTableRow(gbx_game_system_core.GbxAnimTableRow): ...


class GbxNavAnimTableRow(gbx_game_system_core.GbxAnimTableRow):
    Angle: gbx_runtime.NumericRange
    bCorner: bool
    CornerMaxAngle: float
    bCanStretchRotation: bool
    bAutoFill: bool


class GbxNavAreaItem:
    GbxNavArea: GbxNavArea
    CostScale: float
    NavArea: unreal.UClass


class GbxNavBoundsTracker:
    Bounds: core_uobject.Box
    PrimitiveComponent: engine.PrimitiveComponent
    HullPoints: unreal.WrappedArray[core_uobject.Vector]


class GbxNavCorrecter:
    World: engine.World
    GbxNavWorld: GbxNavWorld
    NavComp: GbxNavComponent
    PathingActor: engine.Actor
    MoveComp: gbx_game_system_core.GbxCharacterMovementComponent
    NavAgentProps: engine.NavAgentProperties
    SavedCollision: gbx_game_system_core.SavedCollision


class GbxNavForwardState:
    MinSpeedScale: float
    bScaleSpeed: bool
    MaxTurnScale: float
    bScaleRotation: bool
    ScaleInterpTime: float
    DistanceRange: gbx_runtime.NumericRange
    WallCheckDegreesPerSegment: float
    MinTurnRadius: float
    World: engine.World
    GbxNavWorld: GbxNavWorld
    NavComponent: GbxNavComponent
    MovementComponent: gbx_game_system_core.GbxCharacterMovementComponent
    VehicleFlightComponent: AIVehicleFlightComponent


class GbxNavLayerState:
    Layers: unreal.WrappedArray[GbxNavLayerItem]
    GbxNavWorld: GbxNavWorld


class GbxNavLayerItem:
    NavLayer: GbxNavLayer
    Radius: float
    HalfHeight: float
    LayerIdx: int
    Color: core_uobject.Color
    Layer: unreal.UClass


class GbxPainterItem:
    Component: engine.PrimitiveComponent


class GbxNavSectionBounds:
    WorldBoxBound: core_uobject.Box
    WorldConvexHullPoints: unreal.WrappedArray[core_uobject.Vector]
    DominationGuid: core_uobject.Guid


class GbxNavStreamingData:
    Guid: core_uobject.Guid
    Sets: unreal.WrappedArray[HavokStreamingSet]


class GbxNavStuckState:
    World: engine.World
    NavComp: GbxNavComponent
    PathingActor: engine.Actor
    GbxMoveComp: gbx_game_system_core.GbxCharacterMovementComponent
    StuckDistance: float
    StuckVelocity: float
    StuckWaitTime: float
    bStuckFixEnabled: bool
    StuckFixStartTime: float
    StuckFixStopTime: float


class GbxPainterManager:
    NavAreas: unreal.WrappedArray[GbxNavArea]
    Painters: unreal.WrappedArray[GbxPainterData]


class GbxPainterData:
    Painter: GbxNavMeshPainterComponent


class GbxReachabilityState:
    GbxNavWorld: GbxNavWorld
    NavComp: GbxNavComponent


class GbxReachabilityTracker:
    GbxNavWorld: GbxNavWorld
    CachedSourceRoot: engine.SceneComponent
    CachedGoalRoot: engine.SceneComponent


class GbxUserEdgeManager:
    NormalEdgeTypes: unreal.WrappedArray[GbxUserEdge]
    TeleportTypes: unreal.WrappedArray[GbxUserEdgeTeleportType]
    Edges: unreal.WrappedArray[GbxUserEdgeData]
    UserEdgesToAdd: unreal.WrappedArray[GbxDynamicUserEdgeInfo]
    UserEdgesToRemove: unreal.WrappedArray[int]
    NormalTypes: unreal.WrappedArray[unreal.UClass]


class GbxDynamicUserEdgeInfo:
    Component: GbxNavUserEdgeTrailComponent


class GbxUserEdgeData:
    Edge: HavokUserEdgeComponent


class GbxUserEdgeTeleportType:
    EntryEdge: GbxUserEdge
    ExitEdge: GbxUserEdge
    Entry: unreal.UClass
    Exit: unreal.UClass


class GbxUserEdgeState:
    EntryPosition: engine.BasedPosition
    ExitPosition: engine.BasedPosition
    TeleportData: TeleportUserEdgeData
    GbxNavWorld: GbxNavWorld
    NavComp: GbxNavComponent
    GbxActionComp: gbx_game_system_core.GbxActionComponent
    AIController: aimodule.AIController


class TeleportUserEdgeData:
    EntryAction: unreal.UClass
    TeleportAction: unreal.UClass
    ExitAction: unreal.UClass


class HavokUserEdgeTeleportItem:
    EntryUserEdge: GbxUserEdge
    ExitUserEdge: GbxUserEdge
    CostScale: float
    TeleportAction: unreal.UClass
    EntryEdge: unreal.UClass
    ExitEdge: unreal.UClass


class HavokUserEdgeItem:
    GbxUserEdge: GbxUserEdge
    CostScale: float
    MaxDistance: float
    Action: unreal.UClass
    UserEdge: unreal.UClass


class HavokUserEdgePreviewItem:
    ActorClass: unreal.UClass
    ForwardAction: unreal.UClass
    ReverseAction: unreal.UClass


class EGbxNavMoveStyleDefault(enum.Enum):
    EGbxNavMoveStyleDefault_MAX = 0
    Forward = 1


class EFlightMovementState(enum.Enum):
    Descent = 0
    DigistructingOut = 1
    Ascent = 2


class EGbxNavAnimTableType(enum.Enum):
    Stop = 0
    TurnIdle = 1
    EGbxNavAnimTableType_MAX = 2


class EAvoidWhileIdle(enum.Enum):
    AvoidWhileIdle = 0
    OnlyAvoidWhileMoving = 1


class EGbxNavState(enum.Enum):
    WaitingGoal = 0
    WaitingPath = 1
    EGbxNavState_MAX = 2


class EGbxGoalResult(enum.Enum):
    Reached = 0
    Success = 1


class EGbxNavFlyRoundingMode(enum.Enum):
    RoundToNearest = 0
    EGbxNavFlyRoundingMode_MAX = 1


class EGbxNavGoalCheats(enum.Enum):
    MoveEvenIfUnreachable = 0
    ValidEvenIfNoNav = 1


class EGbxOffsetType(enum.Enum):
    World = 0
    EGbxOffsetType_MAX = 1


class EGbxStrafeType(enum.Enum):
    Strafe = 0
    Forward = 1


class EGbxNavGoalReach(enum.Enum):
    Pass = 0
    EGbxNavGoalReach_MAX = 1


class EGbxPainterType(enum.Enum):
    Dynamic = 0
    StaticAndDynamic = 1


class EGbxPathType(enum.Enum):
    Walk = 0
    Fly = 1


class EGbxUserEdgeDirection(enum.Enum):
    EGbxUserEdgeDirection_MAX = 0
    AToB = 1
    BToA = 2

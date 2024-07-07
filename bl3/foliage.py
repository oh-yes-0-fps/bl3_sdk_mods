from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine



class FoliageInstancedStaticMeshComponent(engine.HierarchicalInstancedStaticMeshComponent): ...


class FoliageStatistics(engine.BlueprintFunctionLibrary):

    def FoliageOverlappingSphereCount(self, WorldContextObject: unreal.UObject, StaticMesh: engine.StaticMesh, CenterPosition: core_uobject.Vector, Radius: float, ReturnValue: int) -> int: ...
    def FoliageOverlappingBoxCount(self, WorldContextObject: unreal.UObject, StaticMesh: engine.StaticMesh, Box: core_uobject.Box, ReturnValue: int) -> int: ...


class FoliageType(unreal.UObject):
    UpdateGuid: core_uobject.Guid
    Density: float
    DensityAdjustmentFactor: float
    Radius: float
    Scaling: EFoliageScaling
    ScaleX: core_uobject.FloatInterval
    ScaleY: core_uobject.FloatInterval
    ScaleZ: core_uobject.FloatInterval
    VertexColorMaskByChannel: FoliageVertexColorChannelMask
    VertexColorMask: int
    VertexColorMaskThreshold: float
    VertexColorMaskInvert: bool
    ZOffset: core_uobject.FloatInterval
    AlignToNormal: bool
    AlignMaxAngle: float
    RandomYaw: bool
    SnapToGround: bool
    RandomPitchAngle: float
    GroundSlopeAngle: core_uobject.FloatInterval
    Height: core_uobject.FloatInterval
    LandscapeLayers: unreal.WrappedArray[str]
    LandscapeLayer: str
    CollisionWithWorld: bool
    CollisionScale: core_uobject.Vector
    MinimumLayerWeight: float
    MeshBounds: core_uobject.BoxSphereBounds
    LowBoundOriginRadius: core_uobject.Vector
    Mobility: int
    CullDistance: core_uobject.Int32Interval
    bEnableStaticLighting: bool
    CastShadow: bool
    bAffectDynamicIndirectLighting: bool
    bAffectDistanceFieldLighting: bool
    bCastDynamicShadow: bool
    bCastStaticShadow: bool
    bCastShadowAsTwoSided: bool
    bReceivesDecals: bool
    bOverrideLightMapRes: bool
    OverriddenLightMapRes: int
    LightmapType: engine.ELightmapType
    bUseAsOccluder: bool
    BodyInstance: engine.BodyInstance
    CustomNavigableGeometry: int
    LightingChannels: engine.LightingChannels
    bRenderCustomDepth: bool
    CustomDepthStencilValue: int
    CollisionRadius: float
    ShadeRadius: float
    NumSteps: int
    InitialSeedDensity: float
    AverageSpreadDistance: float
    SpreadVariance: float
    SeedsPerStep: int
    DistributionSeed: int
    MaxInitialSeedOffset: float
    bCanGrowInShade: bool
    bSpawnsInShade: bool
    MaxInitialAge: float
    MaxAge: float
    OverlapPriority: float
    ProceduralScale: core_uobject.FloatInterval
    ScaleCurve: engine.RuntimeFloatCurve
    ChangeCount: int
    ReapplyDensity: bool
    ReapplyRadius: bool
    ReapplyAlignToNormal: bool
    ReapplyRandomYaw: bool
    ReapplySnapToGround: bool
    ReapplyScaling: bool
    ReapplyScaleX: bool
    ReapplyScaleY: bool
    ReapplyScaleZ: bool
    ReapplyRandomPitchAngle: bool
    ReapplyGroundSlope: bool
    ReapplyHeight: bool
    ReapplyLandscapeLayers: bool
    ReapplyZOffset: bool
    ReapplyCollisionWithWorld: bool
    ReapplyVertexColorMask: bool
    bEnableDensityScaling: bool



class FoliageType_InstancedStaticMesh(FoliageType):
    Mesh: engine.StaticMesh
    OverrideMaterials: unreal.WrappedArray[engine.MaterialInterface]
    ComponentClass: unreal.UClass



class InstancedFoliageActor(engine.Actor): ...


class InteractiveFoliageActor(engine.StaticMeshActor):
    CapsuleComponent: engine.CapsuleComponent
    TouchingActorEntryPosition: core_uobject.Vector
    FoliageVelocity: core_uobject.Vector
    FoliageForce: core_uobject.Vector
    FoliagePosition: core_uobject.Vector
    FoliageDamageImpulseScale: float
    FoliageTouchImpulseScale: float
    FoliageStiffness: float
    FoliageStiffnessQuadratic: float
    FoliageDamping: float
    MaxDamageImpulse: float
    MaxTouchImpulse: float
    MaxForce: float
    Mass: float
    def CapsuleTouched(self, OverlappedComp: engine.PrimitiveComponent, Other: engine.Actor, OtherComp: engine.PrimitiveComponent, OtherBodyIndex: int, bFromSweep: bool, OverlapInfo: engine.HitResult): ...


class InteractiveFoliageComponent(engine.StaticMeshComponent): ...


class ProceduralFoliageBlockingVolume(engine.Volume):
    ProceduralFoliageVolume: ProceduralFoliageVolume



class ProceduralFoliageComponent(engine.ActorComponent):
    FoliageSpawner: ProceduralFoliageSpawner
    TileOverlap: float
    SpawningVolume: engine.Volume
    ProceduralGuid: core_uobject.Guid



class ProceduralFoliageSpawner(unreal.UObject):
    RandomSeed: int
    TileSize: float
    NumUniqueTiles: int
    MinimumQuadTreeSize: float
    FoliageTypes: unreal.WrappedArray[FoliageTypeObject]
    bNeedsSimulation: bool
    def Simulate(self, NumSteps: int): ...


class ProceduralFoliageTile(unreal.UObject):
    FoliageSpawner: ProceduralFoliageSpawner
    InstancesArray: unreal.WrappedArray[ProceduralFoliageInstance]



class ProceduralFoliageVolume(engine.Volume):
    ProceduralComponent: ProceduralFoliageComponent



class FoliageVertexColorChannelMask:
    UseMask: bool
    MaskThreshold: float
    InvertMask: bool



class FoliageTypeObject:
    FoliageTypeObject: unreal.UObject
    TypeInstance: FoliageType_InstancedStaticMesh
    bIsAsset: bool
    Type: unreal.UClass



class ProceduralFoliageInstance:
    Location: core_uobject.Vector
    Rotation: core_uobject.Quat
    Normal: core_uobject.Vector
    Age: float
    Scale: float
    Type: FoliageType_InstancedStaticMesh



class EFoliageScaling(enum.Enum):
    Free = 0
    LockXY = 1
    LockYZ = 2


class EVertexColorMaskChannel(enum.Enum):
    Green = 0
    Blue = 1
    MAX_None = 2


class FoliageVertexColorMask(enum.Enum):
    FOLIAGEVERTEXCOLORMASK_Alpha = 0
    FOLIAGEVERTEXCOLORMASK_Red = 1
    FOLIAGEVERTEXCOLORMASK_Green = 2


class ESimulationQuery(enum.Enum):
    CollisionOverlap = 0
    ShadeOverlap = 1
    ESimulationQuery_MAX = 2


class ESimulationOverlap(enum.Enum):
    ShadeOverlap = 0
    None_ = 1

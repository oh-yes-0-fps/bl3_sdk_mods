from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine



class DestructibleActor(engine.Actor):
    DestructibleComponent: DestructibleComponent
    bAffectNavigation: bool



class DestructibleComponent(engine.SkinnedMeshComponent):
    bFractureEffectOverride: bool
    FractureEffects: unreal.WrappedArray[engine.FractureEffect]
    bEnableHardSleeping: bool
    LargeChunkThreshold: float
    bUseParentComponentPose: bool
    DestructiblePoseComponent: engine.SkinnedMeshComponent
    bIsPosable: bool
    def SetDestructiblePoseComponent(self, NewDestructiblePoseComponent: engine.SkinnedMeshComponent): ...
    def SetDestructibleMesh(self, NewMesh: DestructibleMesh): ...
    def GetDestructibleMesh(self, ReturnValue: DestructibleMesh) -> DestructibleMesh: ...
    def ApplyRadiusDamage(self, BaseDamage: float, HurtOrigin: core_uobject.Vector, DamageRadius: float, ImpulseStrength: float, bFullDamage: bool): ...
    def ApplyDamage(self, DamageAmount: float, HitLocation: core_uobject.Vector, ImpulseDir: core_uobject.Vector, ImpulseStrength: float): ...


class DestructibleFractureSettings(unreal.UObject):
    CellSiteCount: int
    FractureMaterialDesc: FractureMaterial
    RandomSeed: int
    VoronoiSites: unreal.WrappedArray[core_uobject.Vector]
    OriginalSubmeshCount: int
    Materials: unreal.WrappedArray[engine.MaterialInterface]
    ChunkParameters: unreal.WrappedArray[DestructibleChunkParameters]
    CustomBuilder: engine.DestructibleMeshCustomBuilder



class DestructibleMesh(engine.SkeletalMesh):
    DefaultDestructibleParameters: DestructibleParameters
    FractureEffects: unreal.WrappedArray[engine.FractureEffect]
    PosableChunkInfo: unreal.WrappedArray[PosableDestructibleChunkInfo]
    InitialPosableFractureChunkIndex: int



class DestructibleChunkParameters:
    bIsSupportChunk: bool
    bDoNotFracture: bool
    bDoNotDamage: bool
    bDoNotCrumble: bool
    bDoNotSplit: bool



class FractureMaterial:
    UVScale: core_uobject.Vector2D
    UVOffset: core_uobject.Vector2D
    Tangent: core_uobject.Vector
    UAngle: float
    InteriorElementIndex: int



class PosableDestructibleChunkInfo:
    BoneName: str
    GestaltPartName: str
    bIsSupportChunk: bool



class DestructibleParameters:
    DamageParameters: DestructibleDamageParameters
    DebrisParameters: DestructibleDebrisParameters
    AdvancedParameters: DestructibleAdvancedParameters
    SpecialHierarchyDepths: DestructibleSpecialHierarchyDepths
    DepthParameters: unreal.WrappedArray[DestructibleDepthParameters]
    Flags: DestructibleParametersFlag
    ApexCollisionVolumeParameters: DestructibleApexCollisionVolumeParameters



class DestructibleApexCollisionVolumeParameters:
    DepthCollisionVolume: unreal.WrappedArray[DestructibleApexDepthCollisionVolumeParameters]
    bHigherDepthsUseDefaultCollisionVolume: bool
    MaximumTrimming: float
    ConvexHullMethod: EApexConvexHullMethod
    ConcavityPercent: float
    MergeThreshold: float



class DestructibleApexDepthCollisionVolumeParameters:
    ConvexHullMethod: EApexConvexHullMethod
    ConcavityPercent: float
    MergeThreshold: float



class DestructibleParametersFlag:
    bAccumulateDamage: bool
    bAssetDefinedSupport: bool
    bWorldSupport: bool
    bDebrisTimeout: bool
    bDebrisMaxSeparation: bool
    bCrumbleSmallestChunks: bool
    bAccurateRaycasts: bool
    bUseValidBounds: bool
    bFormExtendedStructures: bool



class DestructibleDepthParameters:
    ImpactDamageOverride: int



class DestructibleSpecialHierarchyDepths:
    SupportDepth: int
    MinimumFractureDepth: int
    bEnableDebris: bool
    DebrisDepth: int
    EssentialDepth: int



class DestructibleAdvancedParameters:
    DamageCap: float
    ImpactVelocityThreshold: float
    MaxChunkSpeed: float
    FractureImpulseScale: float



class DestructibleDebrisParameters:
    DebrisLifetimeMin: float
    DebrisLifetimeMax: float
    DebrisMaxSeparationMin: float
    DebrisMaxSeparationMax: float
    ValidBounds: core_uobject.Box



class DestructibleDamageParameters:
    DamageThreshold: float
    DamageSpread: float
    DamageSpreadFalloffExponent: float
    DamageSpreadMinimumRadius: float
    DamageSpreadRadiusMultiplier: float
    bEnableImpactDamage: bool
    ImpactDamage: float
    DefaultImpactDamageDepth: int
    bCustomImpactResistance: bool
    ImpactResistance: float



class MeshParentIndex:
    Mesh: engine.StaticMesh
    ParentIndex: int



class EApexConvexHullMethod(enum.Enum):
    Use_10_DOP_X = 0
    Use_10_DOP_Y = 1
    Use_14_DOP_XY = 2
    Use_26_DOP = 3


class EImpactDamageOverride(enum.Enum):
    IDO_On = 0
    IDO_Off = 1

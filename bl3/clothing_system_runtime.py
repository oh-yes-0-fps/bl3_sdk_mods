from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import clothing_system_runtime_interface


class ClothingAssetCustomData(unreal.UObject): ...


class ClothingAsset(clothing_system_runtime_interface.ClothingAssetBase):
    PhysicsAsset: engine.PhysicsAsset
    ClothConfig: ClothConfig
    LODData: unreal.WrappedArray[ClothLODData]
    LodMap: unreal.WrappedArray[int]
    UsedBoneNames: unreal.WrappedArray[str]
    UsedBoneIndices: unreal.WrappedArray[int]
    ReferenceBoneIndex: int
    CustomData: ClothingAssetCustomData


class ClothingSimulationFactoryNv(
    clothing_system_runtime_interface.ClothingSimulationFactory
): ...


class ClothingSimulationInteractorNv(
    clothing_system_runtime_interface.ClothingSimulationInteractor
):

    def SetAnimDriveSpringStiffness(self, InStiffness: float): ...
    def SetAnimDriveDamperStiffness(self, InStiffness: float): ...
    def EnableGravityOverride(self, InVector: core_uobject.Vector): ...
    def DisableGravityOverride(self): ...


class ClothConfig:
    WindMethod: EClothingWindMethod
    VerticalConstraintConfig: ClothConstraintSetup
    HorizontalConstraintConfig: ClothConstraintSetup
    BendConstraintConfig: ClothConstraintSetup
    ShearConstraintConfig: ClothConstraintSetup
    SelfCollisionRadius: float
    SelfCollisionStiffness: float
    SelfCollisionCullScale: float
    Damping: core_uobject.Vector
    Friction: float
    WindDragCoefficient: float
    WindLiftCoefficient: float
    LinearDrag: core_uobject.Vector
    AngularDrag: core_uobject.Vector
    LinearInertiaScale: core_uobject.Vector
    AngularInertiaScale: core_uobject.Vector
    CentrifugalInertiaScale: core_uobject.Vector
    SolverFrequency: float
    StiffnessFrequency: float
    GravityScale: float
    TetherStiffness: float
    TetherLimit: float
    CollisionThickness: float
    AnimDriveSpringStiffness: float
    AnimDriveDamperStiffness: float


class ClothConstraintSetup:
    Stiffness: float
    StiffnessMultiplier: float
    StretchLimit: float
    CompressionLimit: float


class ClothLODData:
    PhysicalMeshData: ClothPhysicalMeshData
    CollisionData: clothing_system_runtime_interface.ClothCollisionData


class ClothPhysicalMeshData:
    Vertices: unreal.WrappedArray[core_uobject.Vector]
    Normals: unreal.WrappedArray[core_uobject.Vector]
    Indices: unreal.WrappedArray[int]
    MaxDistances: unreal.WrappedArray[float]
    BackstopDistances: unreal.WrappedArray[float]
    BackstopRadiuses: unreal.WrappedArray[float]
    AnimDriveMultipliers: unreal.WrappedArray[float]
    InverseMasses: unreal.WrappedArray[float]
    BoneData: unreal.WrappedArray[ClothVertBoneData]
    MaxBoneWeights: int
    NumFixedVerts: int
    SelfCollisionIndices: unreal.WrappedArray[int]


class ClothVertBoneData:
    NumInfluences: int
    BoneIndices: int
    BoneWeights: float


class ClothParameterMask_PhysMesh:
    MaskName: str
    CurrentTarget: MaskTarget_PhysMesh
    MaxValue: float
    MinValue: float
    Values: unreal.WrappedArray[float]
    bEnabled: bool


class EClothingWindMethod(enum.Enum):
    EClothingWindMethod_MAX = 0
    Accurate = 1


class MaskTarget_PhysMesh(enum.Enum):
    MaxDistance = 0
    BackstopDistance = 1
    AnimDriveMultiplier = 2

from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import engine
from . import gbx_audio
from . import apex_destruction
from . import gbx_game_system_core


class ClothActor(engine.Actor):
    WindSensitivity: gbx_audio.WindDirectionalSensitivity


class ClothSkeletalMeshActor(ClothActor):
    SkeletalMeshComponent: engine.SkeletalMeshComponent


class ClothStaticMeshActor(ClothActor):
    StaticMeshComponent: engine.StaticMeshComponent


class ClothManager(gbx_game_system_core.ClothManagerInterface):
    MaxAllowedSimCost: float
    TimeOffScreenBeforeSimulationPause: float


class GbxDestructibleActor(apex_destruction.DestructibleActor):
    FractureBuffer: GbxDestructibleNetBuffer
    TransformBuffer: GbxDestructibleNetBuffer
    SyncID: int

    def SetFracturable(self, bFracturable: bool): ...
    def OnRep_TransformBuffer(self): ...
    def OnRep_SyncID(self): ...
    def OnRep_FractureBuffer(self): ...


class GbxDestructibleComponent(apex_destruction.DestructibleComponent):
    SecondsToWaitAfterNotRenderedToCleanUp: float
    ProbabilityOfTransientChunk: float
    FractureEventRefireDelay: float
    OnGbxComponentFracture: Any
    DestructibleRelevance: EDestructibleRelevance
    ChunkCollisionChannel: int
    ChunkImpactData: gbx_game_system_core.ImpactData
    bPlayFractureEventOnDebris: bool
    bSupportChunksBlockPawnMovement: bool
    bOverrideAssetDamageThreshold: bool
    MetersDroppedToBreak: float
    DamageThresholdMagnitude: gbx_game_system_core.EDestructibleDamageThresholdMagnitude
    ImpactDamageDefaultDepth: int
    bAutoComputeMaterialStrength: bool
    bAccumulateImpactDamage: bool
    ImpactVelocityThresholdOverride: float
    bUseTotalMass: bool
    TotalMass: float
    bOverrideDebrisLifetime: bool
    DebrisLifetimeMin: float
    DebrisLifetimeMax: float
    FractureEffectOverlapPercent: float

    def SetFracturable(self, bFracturable: bool): ...
    def GetTotalPercentFractured(self) -> float: ...
    def GetDamageRequiredToFracture(self, Depth: int) -> float: ...
    def FractureRandomChunk(self): ...


class GbxUserDestructibleSyncManager(engine.Actor): ...


class GbxDestructibleNetBuffer: ...


class EDestructibleRelevance(enum.Enum):
    DR_Gameplay = 0
    DR_None = 1

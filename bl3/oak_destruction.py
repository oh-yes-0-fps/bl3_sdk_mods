from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import apex_destruction
from . import gbx_destruction


class CryoDestructibleComponent(gbx_destruction.GbxDestructibleComponent):
    BaseMaterial: engine.MaterialInterface
    FracturedLifeSpan: float
    FracturedMaterial: engine.MaterialInterface
    FracturedInteriorMaterial: engine.MaterialInterface
    FractureEffect: engine.FractureEffect
    FracturedActorClass: unreal.UClass
    FreezeRateVariation: float
    ThawJitterSpeed: float
    ThawJitterScale: float
    ThawMaterialParamName: str
    DissolveTime: float
    DissolveDelayTime: float
    DissolvePositionOffsetScale: float
    LinkedDestructible: apex_destruction.DestructibleComponent


class OakDestructibleFXManager(engine.Actor):

    def OnDestructibleDestroyed(self, DestroyedActor: engine.Actor): ...
    def DestroyAllDestructibles(self): ...
    def ClientApplyRadiusDamage(
        self,
        SyncID: int,
        DamageAmount: float,
        HurtOrigin: core_uobject.Vector,
        DamageRadius: float,
        ImpulseStrength: float,
        bFullDamage: bool,
    ): ...
    def ClientApplyDamage(
        self,
        SyncID: int,
        DamageAmount: float,
        HitLocation: core_uobject.Vector,
        ImpulseDir: core_uobject.Vector,
        ImpulseStrength: float,
    ): ...

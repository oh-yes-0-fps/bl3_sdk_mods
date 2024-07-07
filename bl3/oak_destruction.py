from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


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

from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine


class SignificanceManager(unreal.UObject):
    SignificanceManagerClassName: core_uobject.SoftClassPath

    def UnregisterForTickOptim(self, TickOptimActor: engine.Actor): ...
    def OnTickActorEndPlay(self, TickOptimActor: engine.Actor, EndPlayReason: int): ...

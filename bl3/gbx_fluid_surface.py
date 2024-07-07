from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine
from . import procedural_mesh_component



class FluidSurface(engine.Actor):
    NumberOfFluidParticlesX: int
    NumberOfFluidParticlesY: int
    TargetHeight: float
    FluidStiffness: float
    FluidPropagation: float
    IterationCount: int
    RenderComponent: procedural_mesh_component.ProceduralMeshComponent
    def PerturbSurface(self, Position: core_uobject.Vector, Radius: float, Force: float): ...

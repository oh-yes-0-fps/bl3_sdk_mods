from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine



class GbxBlueprintFunctionLibrariesBPLibrary(engine.BlueprintFunctionLibrary):

    def SortActorListByDistance(self, TargetActor: engine.Actor, ActorList: unreal.WrappedArray[engine.Actor]): ...
    def SimplexNoise4D(self, Location: core_uobject.Vector4, ReturnValue: float) -> float: ...
    def SimplexNoise3D(self, Location: core_uobject.Vector, ReturnValue: float) -> float: ...
    def SimplexNoise2D(self, Location: core_uobject.Vector2D, ReturnValue: float) -> float: ...
    def SimplexNoise1D(self, Location: float, ReturnValue: float) -> float: ...
    def SetForceMipLevelsToBeResidentForMaterialArray(self, MaterialArray: unreal.WrappedArray[engine.MaterialInterface], OverrideForceMiplevelsToBeResident: bool, bForceMiplevelsToBeResidentValue: bool, ForceDuration: float, CinematicTextureGroups: int): ...
    def PerlinNoise2D(self, Location: core_uobject.Vector2D, Octaves: int, Persistence: float, Amplitude: float, ReturnValue: float) -> float: ...
    def PerlinNoise1D(self, X: float, Octaves: int, Persistence: float, Amplitude: float, ReturnValue: float) -> float: ...
    def IsWithinRangeAndAngle(self, Source: core_uobject.Transform, Target: engine.Actor, Range: float, Angle: float, ReturnValue: bool) -> bool: ...
    def IsInEditorMode(self, ReturnValue: bool) -> bool: ...
    def GbxBlueprintFunctionLibrariesSampleFunction(self, Param: float, ReturnValue: float) -> float: ...
    def FloatDamp(self, Current: float, Target: float, CurrentVelocity: float, SmoothDuration: float, MaxSpeed: float, DeltaTime: float, ReturnValue: float) -> float: ...
    def FindClosestPlayerCharacter(self, WorldContextObject: unreal.UObject, RefLocation: core_uobject.Vector, ReturnValue: engine.Character) -> engine.Character: ...
    def FindClosestActor(self, ActorArray: unreal.WrappedArray[int], RefLocation: core_uobject.Vector, ClosestActor: int): ...
    def BroadcastRemoteEvent(self, WorldContextObject: unreal.UObject, EventName: str): ...


class HitResultFunctionLibrary(engine.BlueprintFunctionLibrary):

    def IsBlockingHit(self, HitResult: engine.HitResult, ReturnValue: bool) -> bool: ...
    def GetPhysMaterial(self, HitResult: engine.HitResult, ReturnValue: engine.PhysicalMaterial) -> engine.PhysicalMaterial: ...
    def GetHitNormal(self, HitResult: engine.HitResult, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetHitLocation(self, HitResult: engine.HitResult, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetHitDistance(self, HitResult: engine.HitResult, ReturnValue: float) -> float: ...
    def GetHitComponent(self, HitResult: engine.HitResult, ReturnValue: engine.PrimitiveComponent) -> engine.PrimitiveComponent: ...
    def GetHitActor(self, HitResult: engine.HitResult, ReturnValue: engine.Actor) -> engine.Actor: ...
    def GetBoneName(self, HitResult: engine.HitResult, ReturnValue: str) -> str: ...


class TagsFunctionLibrary(engine.BlueprintFunctionLibrary):

    def RemoveTagFromComponent(self, Target: engine.ActorComponent, Tag: str): ...
    def RemoveTagFromActor(self, Target: engine.Actor, Tag: str): ...
    def ComponentContainsTag(self, Target: engine.ActorComponent, Tag: str, ReturnValue: bool) -> bool: ...
    def CompareComponentTags(self, FirstComponent: engine.ActorComponent, SecondComponent: engine.ActorComponent, Branches: ECompareTag, ReturnValue: unreal.WrappedArray[str]) -> unreal.WrappedArray[str]: ...
    def CompareActorTagsWithComponent(self, Actor: engine.Actor, Component: engine.ActorComponent, Branches: ECompareTag, ReturnValue: unreal.WrappedArray[str]) -> unreal.WrappedArray[str]: ...
    def CompareActorTags(self, FirstActor: engine.Actor, SecondActor: engine.Actor, Branches: ECompareTag, ReturnValue: unreal.WrappedArray[str]) -> unreal.WrappedArray[str]: ...
    def AddTagToComponent(self, Target: engine.ActorComponent, Tag: str): ...
    def AddTagToActor(self, Target: engine.Actor, Tag: str): ...
    def ActorContainsTag(self, Target: engine.Actor, Tag: str, ReturnValue: bool) -> bool: ...


class ECompareTag(enum.Enum):
    UniqueTags = 0
    ECompareTag_MAX = 1
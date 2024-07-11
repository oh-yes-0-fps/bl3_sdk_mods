from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine


class GameplayTask(unreal.UObject):
    InstanceName: str
    ResourceOverlapPolicy: ETaskResourceOverlapPolicy
    ChildTask: GameplayTask

    def ReadyForActivation(self): ...
    def GenericGameplayTaskDelegate__DelegateSignature(self): ...
    def EndTask(self): ...


class GameplayTaskResource(unreal.UObject):
    ManualResourceID: int
    AutoResourceID: int
    bManuallySetID: bool


class GameplayTask_ClaimResource(GameplayTask):

    def ClaimResources(
        self,
        InTaskOwner: Any,
        ResourceClasses: unreal.WrappedArray[unreal.UClass],
        Priority: int,
        TaskInstanceName: str,
    ) -> GameplayTask_ClaimResource: ...
    def ClaimResource(
        self,
        InTaskOwner: Any,
        ResourceClass: unreal.UClass,
        Priority: int,
        TaskInstanceName: str,
    ) -> GameplayTask_ClaimResource: ...


class GameplayTask_SpawnActor(GameplayTask):
    Success: Any
    DidNotSpawn: Any
    ClassToSpawn: unreal.UClass

    def SpawnActor(
        self,
        TaskOwner: Any,
        SpawnLocation: core_uobject.Vector,
        SpawnRotation: core_uobject.Rotator,
        Class: unreal.UClass,
        bSpawnOnlyOnAuthority: bool,
    ) -> GameplayTask_SpawnActor: ...
    def FinishSpawningActor(
        self, WorldContextObject: unreal.UObject, SpawnedActor: engine.Actor
    ): ...
    def BeginSpawningActor(
        self, WorldContextObject: unreal.UObject, SpawnedActor: engine.Actor
    ) -> bool: ...


class GameplayTask_TimeLimitedExecution(GameplayTask):
    OnFinished: Any
    OnTimeExpired: Any


class GameplayTask_WaitDelay(GameplayTask):
    OnFinish: Any

    def TaskWaitDelay(
        self, TaskOwner: Any, Time: float, Priority: int
    ) -> GameplayTask_WaitDelay: ...
    def TaskDelayDelegate__DelegateSignature(self): ...


class GameplayTaskOwnerInterface(core_uobject.Interface): ...


class GameplayTasksComponent(engine.ActorComponent):
    bIsNetDirty: bool
    SimulatedTasks: unreal.WrappedArray[GameplayTask]
    TaskPriorityQueue: unreal.WrappedArray[GameplayTask]
    TickingTasks: unreal.WrappedArray[GameplayTask]
    KnownTasks: unreal.WrappedArray[GameplayTask]
    OnClaimedResourcesChange: Any

    def OnRep_SimulatedTasks(self): ...
    def K2_RunGameplayTask(
        self,
        TaskOwner: Any,
        Task: GameplayTask,
        Priority: int,
        AdditionalRequiredResources: unreal.WrappedArray[unreal.UClass],
        AdditionalClaimedResources: unreal.WrappedArray[unreal.UClass],
    ) -> EGameplayTaskRunResult: ...


class GameplayResourceSet: ...


class ETaskResourceOverlapPolicy(enum.Enum):
    ETaskResourceOverlapPolicy_MAX = 0
    StartAtEnd = 1


class EGameplayTaskState(enum.Enum):
    Finished = 0
    Paused = 1
    AwaitingActivation = 2


class EGameplayTaskRunResult(enum.Enum):
    Failed = 0
    Success_Finished = 1
    Success_Paused = 2

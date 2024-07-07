from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
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



class GameplayTask_ClaimResource(GameplayTask): ...


class GameplayTask_SpawnActor(GameplayTask):
    ClassToSpawn: unreal.UClass
    def FinishSpawningActor(self, WorldContextObject: unreal.UObject, SpawnedActor: engine.Actor): ...
    def BeginSpawningActor(self, WorldContextObject: unreal.UObject, SpawnedActor: engine.Actor, ReturnValue: bool) -> bool: ...


class GameplayTask_TimeLimitedExecution(GameplayTask): ...


class GameplayTask_WaitDelay(GameplayTask):

    def TaskDelayDelegate__DelegateSignature(self): ...


class GameplayTaskOwnerInterface(core_uobject.Interface): ...


class GameplayTasksComponent(engine.ActorComponent):
    bIsNetDirty: bool
    SimulatedTasks: unreal.WrappedArray[GameplayTask]
    TaskPriorityQueue: unreal.WrappedArray[GameplayTask]
    TickingTasks: unreal.WrappedArray[GameplayTask]
    KnownTasks: unreal.WrappedArray[GameplayTask]
    def OnRep_SimulatedTasks(self): ...


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

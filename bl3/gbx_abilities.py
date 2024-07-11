from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import gbx_runtime
from . import gbx_game_system_core


class GbxAbility(unreal.UObject):
    AbilityName: str
    AbilityDescription: str
    AbilityEffects: unreal.WrappedArray[GbxAbilityEffect]
    Manager: GbxAbilityManagerComponent
    DurationType: EGbxAbilityDurationType
    Duration: float
    DesiredAbilityState: EGbxAbilityState
    AbilityState: EGbxAbilityState
    AbilityEffectInstances: unreal.WrappedArray[GbxAbilityEffectInstance]
    PendingManager: GbxAbilityManagerComponent

    def OnUnregistered(self): ...
    def OnResumed(self): ...
    def OnRep_Manager(self): ...
    def OnRep_AbilityState(self): ...
    def OnRegistered(self): ...
    def OnPaused(self): ...
    def OnForcedRefresh(self): ...
    def OnDeactivated(self): ...
    def OnActivated(self): ...
    def IsReplicated(self) -> bool: ...
    def GetAbilityOwner(self) -> engine.Actor: ...
    def Client_Deactivate(self): ...
    def CalculateAbilityState(self) -> EGbxAbilityState: ...


class GbxAbilityEffectTargetResolutionData(gbx_runtime.GbxDataAsset): ...


class GbxAbilityManagerComponent(engine.ActorComponent):
    Abilities: unreal.WrappedArray[GbxAbility]
    ReplicatedAbilities: unreal.WrappedArray[GbxAbility]
    PendingReplicatedAbilities: unreal.WrappedArray[GbxAbility]
    RegisteredAbilities: Any
    ListLock: GbxAbilityManagerComponentListLock

    def RemoveAbility(self, AbilityClass: unreal.UClass) -> bool: ...
    def HasAbility(self, AbilityClass: unreal.UClass) -> bool: ...
    def FindAbility(self, AbilityClass: unreal.UClass) -> GbxAbility: ...
    def AddAbility(self, Spec: GbxAbilitySpec) -> GbxAbility: ...


class GbxAbilityAttributePropertyValueResolver(
    gbx_game_system_core.AttributePropertyValueResolver
):
    GbxAbilityClass: Any


class GbxAbilityEffectTargetResolutionData_Owner(
    GbxAbilityEffectTargetResolutionData
): ...


class GbxAbilityEffectTargetResolutionData_Self(
    GbxAbilityEffectTargetResolutionData
): ...


class GbxAbilityResourceControllerBlueprintFunctionLibrary(
    engine.BlueprintFunctionLibrary
):

    def UnregisterResourcePoolDelegate(
        self,
        Controller: GbxAbilityResourceController_ResourcePoolDelegate,
        Spec: GbxAbilityResourceSpec_ResourcePoolDelegate,
    ): ...
    def UnregisterConditionalDamageModifier(
        self,
        Controller: GbxAbilityResourceController_ConditionalDamageModifier,
        Spec: GbxAbilityResourceSpec_ConditionalDamageModifier,
    ): ...
    def UnregisterAbilityDelegate(
        self,
        Controller: GbxAbilityResourceController_ScriptDelegate,
        Spec: GbxAbilityResourceSpec_ScriptDelegate,
    ): ...
    def RegisterResourcePoolDelegate(
        self,
        Controller: GbxAbilityResourceController_ResourcePoolDelegate,
        Spec: GbxAbilityResourceSpec_ResourcePoolDelegate,
    ): ...
    def RegisterConditionalDamageModifier(
        self,
        Controller: GbxAbilityResourceController_ConditionalDamageModifier,
        Spec: GbxAbilityResourceSpec_ConditionalDamageModifier,
    ): ...
    def RegisterAbilityDelegate(
        self,
        Controller: GbxAbilityResourceController_ScriptDelegate,
        Spec: GbxAbilityResourceSpec_ScriptDelegate,
    ): ...


class GbxCondition_HasAbility(gbx_runtime.GbxCondition):
    AbilityClass: unreal.UClass


class GbxAbilityResourceController:
    Owner: GbxAbility


class GbxAbilityResourceSpec:
    AbilityContext: GbxAbility
    bWhenActive: bool
    bWhenPaused: bool


class GbxAbilityEffectInstance:
    Owner: GbxAbility
    StatusEffectSpec: gbx_game_system_core.StatusEffectSpec
    Targets: unreal.WrappedArray[GbxAbilityEffectInstanceTarget]
    Condition: gbx_runtime.GbxCondition
    TargetResolutionStrategies: unreal.WrappedArray[
        GbxAbilityEffectTargetResolutionData
    ]


class GbxAbilityEffectInstanceTarget:
    TargetActor: engine.Actor
    TargetStatusEffectManagerComponent: (
        gbx_game_system_core.StatusEffectManagerComponent
    )
    StatusEffectInstanceReference: gbx_game_system_core.StatusEffectInstanceReference


class GbxAbilityEffect:
    StatusEffectData: gbx_game_system_core.StatusEffectData
    TargetResolutionStrategies: unreal.WrappedArray[
        GbxAbilityEffectTargetResolutionData
    ]
    Condition: gbx_runtime.GbxCondition


class GbxAbilityManagerComponentListLock:
    Owner: GbxAbilityManagerComponent
    DeferredOps: unreal.WrappedArray[GbxAbilityManagerComponentDeferredOperation]


class GbxAbilityManagerComponentDeferredOperation:
    AddSpec: GbxAbilitySpec
    RemoveSpec: unreal.UClass


class GbxAbilitySpec:
    AbilityClass: unreal.UClass
    DurationType: EGbxAbilityDurationType
    DurationInitializerData: float


class GbxAbilityResourceController_ConditionalDamageModifier(
    GbxAbilityResourceController
): ...


class GbxAbilityResourceSpec_ConditionalDamageModifier(GbxAbilityResourceSpec):
    DamageComponent: gbx_game_system_core.DamageBaseComponent
    DamageModifier: gbx_game_system_core.ConditionalDamageModifier
    ContextOverride: unreal.UObject


class GbxAbilityResourceController_ResourcePoolDelegate(
    GbxAbilityResourceController
): ...


class GbxAbilityResourceSpec_ResourcePoolDelegate(GbxAbilityResourceSpec):
    ResourcePoolComponent: gbx_game_system_core.GameResourcePoolManagerComponent
    ResourcePoolData: gbx_game_system_core.GameResourcePoolData
    DelegateType: EAbilityResourceDelegateType
    DelegateEventProperty: core_uobject.DelegateProperty


class GbxAbilityResourceController_ScriptDelegate(GbxAbilityResourceController): ...


class GbxAbilityResourceSpec_ScriptDelegate(GbxAbilityResourceSpec):
    TargetContext: unreal.UObject
    TargetProperty: core_uobject.MulticastDelegateProperty
    DelegateEventProperty: core_uobject.DelegateProperty


class EAbilityResourceDelegateType(enum.Enum):
    OnResourceNowDepleted = 0
    OnResourceNowNotDepleted = 1
    OnResourceNowNotDepleting = 2
    OnResourceNowNotFilled = 3


class EGbxAbilityState(enum.Enum):
    EGbxAbilityState_MAX = 0
    Deactivated = 1
    Paused = 2


class EGbxAbilityDurationType(enum.Enum):
    Indefinite = 0
    Infinite = 1

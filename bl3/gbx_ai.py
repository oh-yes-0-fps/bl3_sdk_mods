from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine
from . import gbx_runtime
from . import aimodule
from . import gameplay_tasks
from . import gbx_game_system_core
from . import gbx_nav
from . import gbx_spawn
from . import level_sequence
from . import gbx_level_sequence
from . import gameplay_tags



class AIActionBase(unreal.UObject):
    ExecutionSettings: AIActionExecutionSettings
    BaseVersion: int
    CreationMethod: EAIActionCreationMethod
    def StopBP(self, Action: AIActionBase, Context: AIActionBlueprintContext, bSucceeded: bool): ...
    def CreateSubobjectNoName(self, Class: unreal.UClass, ReturnValue: unreal.UObject) -> unreal.UObject: ...


class AIAction(AIActionBase):
    Blackboard: aimodule.BlackboardData
    bWaitForAllAspects: bool
    Aspects: unreal.WrappedArray[AIAspect]
    BuiltInAspects: unreal.WrappedArray[AIAspect]
    bIsChildAction: bool
    SubActions: unreal.WrappedArray[AIAction]
    ActionVersion: int
    def CreateSubAction(self, ActionClass: unreal.UClass, Name: str, ReturnValue: AIAction) -> AIAction: ...


class AIAction_Composite(AIAction):
    Children: unreal.WrappedArray[AIAction_CompositeChild]
    CompositeVersion: int
    def CreateChild(self, ChildName: str, ReturnValue: AIAction_CompositeChild) -> AIAction_CompositeChild: ...


class AIAction_Selector(AIAction_Composite): ...


class AIAction_Sequence(AIAction_Selector):
    CanStartChecks: EAIActionSequenceCanStartCheck
    CanBeInterrupted: gbx_game_system_core.GbxParam



class AIAction_GoToPoint(AIAction_Sequence):
    LocationSettings: AIAspectSettings_Location
    GoalKey: gbx_game_system_core.GbxBlackboardKeySelector
    NavSettings: AIAspectSettings_Navigation
    bUseNavSettings: bool
    MoveTicket: AITicketDataAsset
    MoveTicketHoldDuration: gbx_game_system_core.GbxParam
    MoveFailTimeLimit: gbx_game_system_core.GbxParam
    bUseMoveFailTimeLimit: bool
    QueryKey: gbx_game_system_core.GbxBlackboardKeySelector
    QuerySettings: AIAspectSettings_EnvQuery
    bUseQuery: bool
    MinOffsetInFrontOfTarget: float
    MaxOffsetInFrontOfTarget: float
    OffsetAngle: float
    bUseOffsetInFrontOfTarget: bool
    CirclingDistance: float
    Direction: ECircleDirection
    bRotateAroundTarget: bool
    CustomRotationTarget: gbx_game_system_core.GbxBlackboardKeySelector
    bUseCustomRotationTarget: bool
    RotationSettings: AIAspectSettings_Rotation
    bUseRotation: bool
    bTestDirectPath: bool
    bDebugTestDirectPath: bool
    GoToPointVersion: int



class AIAction_ActionAtPoint(AIAction_GoToPoint):
    ActionSettings: AIAspectSettings_GbxAction
    bCheckLocationDuringAction: bool
    bUseRotationDuringAction: bool
    bUseRotationTargetDuringAction: bool
    ActionRotationSettings: AIAspectSettings_Rotation
    bUseActionRotation: bool
    ActionAtPointVersion: int



class BTTask_AIAction(aimodule.BTTaskNode):
    ActionDecorator: BTDecorator_AIAction



class BTTask_AIAction_ActionAtPoint(BTTask_AIAction):
    Action: AIAction_ActionAtPoint



class AIAction_Priority(AIAction_Selector):
    TryInterruptPeriod: float
    TryInterruptInsignificantPeriod: float
    bInterruptWhileInsignificant: bool



class AIAction_AITree(AIAction_Priority): ...


class AIAction_Charge(AIAction_GoToPoint):
    ChargeSettings: AIAspectSettings_Charge



class BTTask_AIAction_Charge(BTTask_AIAction):
    Action: AIAction_Charge



class AIAction_CompositeChild(AIAction):
    Action: AIAction
    bCanCauseParentToStop: bool
    def CreateAction(self, ActionClass: unreal.UClass, ReturnValue: AIAction) -> AIAction: ...


class AIAction_Decorator(AIAction): ...


class AIAction_MoveNode(AIAction_Priority):
    NodeKey: gbx_game_system_core.GbxBlackboardKeySelector
    NavSettings: AIAspectSettings_Navigation
    MoveNodeVersion: int



class AIAction_Dropship(AIAction_MoveNode): ...


class AIAction_Follow(AIAction_Priority):
    Settings: AIAspectSettings_Follow
    NavSettings: AIAspectSettings_Navigation
    FindClosestPlayerSettings: AIAspectSettings_FindClosestPlayer
    bFindClosestPlayer: bool
    TeleportTarget: gbx_game_system_core.GbxBlackboardKeySelector
    MoveTarget: gbx_game_system_core.GbxBlackboardKeySelector
    Distance: gbx_game_system_core.GbxBlackboardKeySelector
    BodyDirection: gbx_game_system_core.GbxBlackboardKeySelector
    FollowVersion: int



class BTTask_AIAction_GoToPoint(BTTask_AIAction):
    Action: AIAction_GoToPoint



class AIAction_Land(AIAction_Sequence):
    FlyToNavMeshSettings: AIAspectSettings_FlyToNavMesh
    AnimSettings: AIAspectSettings_GbxAction
    NavSettings: AIAspectSettings_Navigation



class AIAction_LeadRoute(AIAction_Priority):
    LeadSettings: AIAspectSettings_LeadRoute
    NavSettings: AIAspectSettings_Navigation
    FindClosestPlayerSettings: AIAspectSettings_FindClosestPlayer
    MoveTarget: gbx_game_system_core.GbxBlackboardKeySelector
    Distance: gbx_game_system_core.GbxBlackboardKeySelector
    TeleportTarget: gbx_game_system_core.GbxBlackboardKeySelector
    UnusedKey: gbx_game_system_core.GbxBlackboardKeySelector
    LeadRouteVersion: int



class BTTask_AIAction_LeadRoute(BTTask_AIAction):
    Action: AIAction_LeadRoute



class AIAction_Leap(AIAction_GoToPoint):
    LeapSettings: AIAspectSettings_Leap



class BTTask_AIAction_Leap(BTTask_AIAction):
    Action: AIAction_Leap



class AIAction_LeapDirect(AIAction):
    LeapSettings: AIAspectSettings_Leap
    QuerySettings: AIAspectSettings_EnvQuery
    bUseQuery: bool



class BTTask_AIAction_LeapDirect(BTTask_AIAction):
    Action: AIAction_LeapDirect



class AIAction_LookAroundRandomly(AIAction):
    Settings: LookAroundRandomlySettings



class BTTask_AIAction_MoveNode(BTTask_AIAction):
    Action: AIAction_MoveNode



class AIAction_MoveSpline(AIAction):
    MoveSplineSettings: AIAspectSettings_MoveSpline
    NavSettings: AIAspectSettings_Navigation
    def SetupMoveSpline(self, TargetActor: engine.Actor, TargetSpline: unreal.UObject, Offset: float, bIsReverse: bool, ReturnValue: bool) -> bool: ...
    def ChangeSplineOffset(self, TargetActor: engine.Actor, Offset: float, ReturnValue: bool) -> bool: ...


class AIAction_OnAggro(AIAction_Sequence):
    bRotateBeforeAction: bool
    bRotateDuringAction: bool
    ActionWhenFirstNoticer: AIAspectSettings_GbxAction
    ActionWhenSecondNoticer: AIAspectSettings_GbxAction



class AIAction_Orbit(AIAction):
    OrbitSettings: AIAspectSettings_Orbit
    NavSettings: AIAspectSettings_Navigation
    RotationSettings: AIAspectSettings_Rotation



class AIAction_Parallel(AIAction_Composite):
    bWaitForAllChildren: bool



class AIAction_ParallelChild(AIAction_CompositeChild):
    bCanPreventActionFromStarting: bool
    bCanCauseActionToSucceed: bool
    bCanCauseActionToFail: bool
    bMustFinish: bool



class AIAction_Plan(AIAction_Sequence):
    Settings: AIActionSettings_Plan



class AIAction_PlayGbxAction(AIAction):
    ActionSettings: AIAspectSettings_GbxAction



class BTTask_AIAction_PlayGbxAction(BTTask_AIAction):
    Action: AIAction_PlayGbxAction



class AIAction_Random(AIAction_Selector):
    bUseCumulativeInverseWeight: bool
    ResetRunCountTime: float



class AIAction_RandomChild(AIAction_CompositeChild):
    Weight: float
    MaxRunCount: int
    bUseMaxRunCount: bool



class AIAction_Route(AIAction_Sequence):
    RouteSettings: AIAspectSettings_Route
    NavSettings: AIAspectSettings_Navigation
    SmartAction: gbx_game_system_core.GbxBlackboardKeySelector
    MoveTarget: gbx_game_system_core.GbxBlackboardKeySelector
    Distance: gbx_game_system_core.GbxBlackboardKeySelector
    BodyEnable: gbx_game_system_core.GbxBlackboardKeySelector
    BodyTarget: gbx_game_system_core.GbxBlackboardKeySelector
    LookEnable: gbx_game_system_core.GbxBlackboardKeySelector
    LookTarget: gbx_game_system_core.GbxBlackboardKeySelector
    RouteVersion: int



class BTTask_AIAction_Route(BTTask_AIAction):
    Action: AIAction_Route



class AIAction_UseCover(AIAction_Priority):
    bCanShootWhileMoving: bool
    UseCoverVersion: int
    CoverSettings: AIAspectSettings_UseCover
    CoverQuery: gbx_game_system_core.EnvQueryParams
    CoverQueryOptions: gbx_game_system_core.GbxQueryOptions
    WeaponSettings: AIAspectSettings_Weapon
    NavSettings: AIAspectSettings_Navigation
    MovingRotationSettings: AIAspectSettings_Rotation
    bRotateDuringMovement: bool



class AIAction_SimpleCover(AIAction_UseCover):
    bTakeRangesFromWeapon: bool
    MinRange: gbx_game_system_core.GbxParam
    IdealRange: gbx_game_system_core.GbxParam
    MaxRange: gbx_game_system_core.GbxParam
    AdditionalTests: unreal.WrappedArray[gbx_game_system_core.EnvQueryTestAsset]
    DefaultEnvQuery: core_uobject.SoftObjectPath
    SimpleCoverVersion: int



class AIAction_WeaponAtPoint(AIAction_GoToPoint):
    bCanShootWhileMoving: bool
    WeaponSettings: AIAspectSettings_Weapon
    HoldDuration: gbx_game_system_core.GbxParam
    bUseHoldDuration: bool
    WeaponAtPointVersion: int



class AIAction_SimpleHide(AIAction_WeaponAtPoint):
    MinRange: gbx_game_system_core.GbxParam
    IdealRange: gbx_game_system_core.GbxParam
    MaxRange: gbx_game_system_core.GbxParam
    FaceTarget: gbx_game_system_core.GbxParam
    CanUseWeaponWhileMoving: gbx_game_system_core.GbxParam
    WeaponSlots: unreal.WrappedArray[gbx_game_system_core.GbxWeaponSlotData]
    WeaponUseModeIndex: gbx_game_system_core.GbxParam
    HideDuration: gbx_game_system_core.GbxParam
    HideActionSettings: AIAspectSettings_GbxAction
    bUseHideAction: bool
    DefaultEnvQuery: core_uobject.SoftObjectPath
    DefaultEnvQueryAsset: aimodule.EnvQuery
    SimpleHideVersion: int



class AIAction_SimpleMelee(AIAction_ActionAtPoint):
    MeleeAction: unreal.UClass
    MeleeActionSettings: AIAspectSettings_GbxAction
    bCanMove: bool
    ReachedHeight: gbx_game_system_core.GbxParam
    ReachedDistance: gbx_game_system_core.GbxParam
    FacingPolicyDuringAction: EMeleeRotationOption
    OverrideAngle: gbx_game_system_core.GbxParam
    bUseOverrideAngle: bool
    bAlignBodyWithTarget: bool
    bKeepFacingTargetOnStop: bool
    bStopWhenReached: bool
    bCanStartWhenGoalIsUncertain: bool
    Count: gbx_game_system_core.GbxParam
    PlayRate: gbx_game_system_core.GbxParam
    bCanBeInterrupted: bool
    MeleeActionVersion: int



class AIAction_SimpleRangedAttack(AIAction_ActionAtPoint):
    MinRange: gbx_game_system_core.GbxParam
    IdealRange: gbx_game_system_core.GbxParam
    MaxRange: gbx_game_system_core.GbxParam
    MinRepositionDistance: gbx_game_system_core.GbxParam
    AdditionalTests: unreal.WrappedArray[gbx_game_system_core.EnvQueryTestAsset]
    SphereTraceExtent: float
    bDoArcTrace: bool
    ArcSpeed: gbx_game_system_core.GbxParam
    ArcAnglePercent: gbx_game_system_core.GbxParam
    OverrideAngle: gbx_game_system_core.GbxParam
    bUseOverrideAngle: bool
    FacingPolicyDuringAction: EMeleeRotationOption
    bAlignBodyWithTarget: bool
    bKeepFacingTargetOnStop: bool
    bDistanceToTargetTestShouldFilterOnly: bool
    DefaultEnvQuery: core_uobject.SoftObjectPath
    DefaultTraceTests: core_uobject.SoftObjectPath
    DefaultEnvQueryAsset: aimodule.EnvQuery
    DefaultTraceTestsAsset: aimodule.EnvQuery
    TraceTestInstance: aimodule.EnvQueryTest_Trace
    SimpleRangedAttackVersion: int



class AIAction_SimpleWeapon(AIAction_WeaponAtPoint):
    CanUseWeaponWhileMoving: gbx_game_system_core.GbxParam
    bTakeRangesFromWeapon: bool
    MinRange: gbx_game_system_core.GbxParam
    IdealRange: gbx_game_system_core.GbxParam
    MaxRange: gbx_game_system_core.GbxParam
    AdditionalTests: unreal.WrappedArray[gbx_game_system_core.EnvQueryTestAsset]
    WeaponSlots: unreal.WrappedArray[gbx_game_system_core.GbxWeaponSlotData]
    WeaponUseModeIndex: gbx_game_system_core.GbxParam
    BurstCountOverride: gbx_game_system_core.GbxParam
    bOverrideBurstCount: bool
    BurstDelayOverride: gbx_game_system_core.GbxParam
    bOverrideBurstDelay: bool
    AccuracyOverride: gbx_game_system_core.GbxParam
    bOverrideAccuracy: bool
    SuppressingFireTime: gbx_game_system_core.GbxParam
    bUseSuppressingFireTime: bool
    bUseRepositionTicket: bool
    MinRepositionDistance: gbx_game_system_core.GbxParam
    RepositionTicket: AITicketDataAsset
    TimeToStayAtSpotWhileShooting: gbx_game_system_core.GbxParam
    bDistanceToTargetTestShouldFilterOnly: bool
    DefaultEnvQuery: core_uobject.SoftObjectPath
    DefaultRepositionTicket: core_uobject.SoftObjectPath
    DefaultEnvQueryAsset: aimodule.EnvQuery
    DefaultRepositionTicketAsset: AITicketDataAsset
    SimpleWeaponVersion: int



class AIAction_StateMachine(AIAction_Selector): ...


class AIAction_StateMachineChild(AIAction_CompositeChild):
    OnSuccess: AIAction_StateMachineChild
    OnFailure: AIAction_StateMachineChild
    def GetAvailableStates(self, Array: unreal.WrappedArray[AIAction_StateMachineChild]): ...


class AIAction_Sweep(AIAction_Orbit):
    SweepSettings: AIAspectSettings_Sweep



class AIAction_Swoop(AIAction_Sequence):
    SwoopSettings: AIAspectSettings_Swoop
    NavSettings: AIAspectSettings_Navigation
    MoveFarRotationSettings: AIAspectSettings_Rotation
    bUseFarRotation: bool
    MoveNearRotationSettings: AIAspectSettings_Rotation
    bUseNearRotation: bool
    MovePassRotationSettings: AIAspectSettings_Rotation
    bUsePassRotation: bool



class AIAction_TargetSequence(AIAction_Sequence):
    TargetCountMin: gbx_game_system_core.GbxParam
    bUseTargetCountMin: bool
    TargetCountMax: gbx_game_system_core.GbxParam
    bUseTargetCountMax: bool
    TargetDistance: gbx_game_system_core.GbxParam
    bUseTargetDistance: bool
    bPlayersOnly: bool



class AIAction_Teleport(AIAction):
    GoalKey: gbx_game_system_core.GbxBlackboardKeySelector
    TeleportSettings: AIAspectSettings_Teleport
    QuerySettings: AIAspectSettings_EnvQuery
    bUseQuery: bool



class BTTask_AIAction_Teleport(BTTask_AIAction):
    Action: AIAction_Teleport



class BTTask_AIAction_UseCover(BTTask_AIAction):
    Action: AIAction_UseCover



class AIAction_UseSmartObject(AIAction_Sequence):
    SmartObjectSettings: AIAspectSettings_UseSmartObject
    NavSettings: AIAspectSettings_Navigation
    MoveToRotationSettings: AIAspectSettings_Rotation
    QuerySettings: AIAspectSettings_EnvQuery
    bUseQuery: bool
    SmartAction: gbx_game_system_core.GbxBlackboardKeySelector
    MoveTarget: gbx_game_system_core.GbxBlackboardKeySelector
    Distance: gbx_game_system_core.GbxBlackboardKeySelector
    BodyTarget: gbx_game_system_core.GbxBlackboardKeySelector
    LookTarget: gbx_game_system_core.GbxBlackboardKeySelector
    LookEnabled: gbx_game_system_core.GbxBlackboardKeySelector
    MoveSettings: AIAspectSettings_Move
    SmartObjectQuery: gbx_game_system_core.EnvQueryParams
    UseSmartObjectVersion: int



class BTTask_AIAction_UseSmartObject(BTTask_AIAction):
    Action: AIAction_UseSmartObject



class BTTask_AIAction_WeaponAtPoint(BTTask_AIAction):
    Action: AIAction_WeaponAtPoint



class AIAction_WeaponIdle(AIAction):
    WeaponSettings: AIAspectSettings_Weapon
    RotationSettings: AIAspectSettings_Rotation



class BTTask_AIAction_WeaponIdle(BTTask_AIAction):
    Action: AIAction_WeaponIdle



class AIActionBlueprint(engine.Blueprint):
    ParentBlueprint: AIActionBlueprint
    Blackboard: aimodule.BlackboardData
    def ShouldSkipBlackboardProperty(self, Property: core_uobject.Property, ReturnValue: bool) -> bool: ...


class AIActionBlueprintGeneratedClass(engine.BlueprintGeneratedClass): ...


class GameplayTask_RunScriptedAIAction(gameplay_tasks.GameplayTask):
    ActionComponent: AIActionComponent
    ActionToRun: unreal.UClass
    def RunScriptedAIAction_Object(self, Object: unreal.UObject, Action: unreal.UClass, ReturnValue: GameplayTask_RunScriptedAIAction) -> GameplayTask_RunScriptedAIAction: ...
    def RunScriptedAIAction_Controller(self, Controller: GbxAIController, Action: unreal.UClass, ReturnValue: GameplayTask_RunScriptedAIAction) -> GameplayTask_RunScriptedAIAction: ...
    def RunScriptedAIAction_AIActionComponent(self, AIActionComponent: AIActionComponent, Action: unreal.UClass, ReturnValue: GameplayTask_RunScriptedAIAction) -> GameplayTask_RunScriptedAIAction: ...
    def RunScriptedAIAction_Actor(self, Actor: engine.Actor, Action: unreal.UClass, ReturnValue: GameplayTask_RunScriptedAIAction) -> GameplayTask_RunScriptedAIAction: ...


class AIActionComponent(aimodule.BrainComponent):
    MainAction: unreal.UClass
    ScriptedMoveAction: unreal.UClass
    ScriptedMoveSplineAction: unreal.UClass
    ScriptedMoveToLevelSequenceAction: unreal.UClass
    ScriptedLookAction: unreal.UClass
    ScriptedWaitAction: unreal.UClass
    ScriptedUseAction: unreal.UClass
    ScriptedCoverAction: unreal.UClass
    ScriptedFollowAction: unreal.UClass
    ScriptedRouteAction: unreal.UClass
    ScriptedLeadAction: unreal.UClass
    ScriptedLandAction: unreal.UClass
    ActionStack: AIActionInstance
    def ReplaceMainAIAction(self, Action: unreal.UClass): ...
    def GetBlackboardData(self, ReturnValue: aimodule.BlackboardData) -> aimodule.BlackboardData: ...
    def AbortScriptedAIAction(self, bStopImmediately: bool): ...


class AIActionManager(unreal.UObject):
    MaxTickTimeMs: float



class AIAspect(AIActionBase):
    AspectExecutionSettings: AIAspectExecutionSettings



class AIAspect_ActorCollision(AIAspect):
    Settings: AIAspectSettings_ActorCollision
    def OnPawnHit(self, SelfActor: engine.Actor, OtherActor: engine.Actor, NormalImpulse: core_uobject.Vector, Hit: engine.HitResult): ...
    def GetOnCollisionOptions(self, Options: unreal.WrappedArray[str]): ...


class AIAspect_Condition(AIAspect):
    Settings: AIAspectSettings_Condition
    def GetConditionDataDescription(self, ConditionData: AIAspectSettings_ConditionData, ReturnValue: str) -> str: ...


class AIAspect_AIGroupCondition(AIAspect_Condition):
    GroupSettings: AIAspectSettings_AIGroupCondition



class AIAspect_AvoidWhileIdle(AIAspect):
    bAvoidWhileIdle: bool



class AIAspect_BlackboardKey(AIAspect):
    Settings: AIAspectSettings_BlackboardKey
    def GetSettingsDescription(self, BBKeySettings: AIAspectSettings_BlackboardKey, ReturnValue: str) -> str: ...


class AIAspect_Charge(AIAspect):
    Settings: AIAspectSettings_Charge



class AIAspect_Navigation(AIAspect):
    Settings: AIAspectSettings_Navigation
    def GetNavSettingsDescription(self, NavSettings: AIAspectSettings_Navigation, Property: core_uobject.Property, ReturnValue: str) -> str: ...


class AIAspect_Circle(AIAspect_Navigation):
    GoalKey: gbx_game_system_core.GbxBlackboardKeySelector
    Distance: float
    Direction: ECircleDirection
    MinOffsetInFrontOfTarget: float
    MaxOffsetInFrontOfTarget: float
    OffsetAngle: float
    GoalUpdateDistance: float
    bTestDirectPath: bool
    bDebugTestDirectPath: bool
    Reach: gbx_nav.EGbxNavGoalReach



class AIAspect_ClaimSmartObject(AIAspect):
    SmartObjectSettings: AIAspectSettings_UseSmartObject
    SmartAction: gbx_game_system_core.GbxBlackboardKeySelector
    MoveTarget: gbx_game_system_core.GbxBlackboardKeySelector
    Distance: gbx_game_system_core.GbxBlackboardKeySelector
    BodyTarget: gbx_game_system_core.GbxBlackboardKeySelector
    LookTarget: gbx_game_system_core.GbxBlackboardKeySelector
    LookEnabled: gbx_game_system_core.GbxBlackboardKeySelector



class AIAspect_Cooldown(AIAspect):
    Settings: AIAspectSettings_Cooldown



class AIAspect_Crouch(AIAspect):
    Settings: AIAspectSettings_Crouch



class AIAspect_DisableAvoidance(AIAspect): ...


class AIAspect_MoveNode(AIAspect_Navigation):
    NodeKey: gbx_game_system_core.GbxBlackboardKeySelector



class AIAspect_UseNode(AIAspect_MoveNode): ...


class AIAspect_DropshipSpawn(AIAspect_UseNode):
    DropshipSettings: AIAspectSettings_DropshipSpawn



class AIAspect_EnvQuery(AIAspect):
    Settings: AIAspectSettings_EnvQuery
    def GetQuerySettingsDescription(self, QuerySettings: AIAspectSettings_EnvQuery, Property: core_uobject.Property, ReturnValue: str) -> str: ...


class AIAspect_FaceNearbyCover(AIAspect):
    CoverKey: gbx_game_system_core.GbxBlackboardKeySelector



class AIAspect_GbxAction(AIAspect):
    Settings: AIAspectSettings_GbxAction



class AIAspect_FallToGround(AIAspect_GbxAction): ...


class AIAspect_FindClosestPlayer(AIAspect):
    Settings: AIAspectSettings_FindClosestPlayer



class AIAspect_FindCover(AIAspect_EnvQuery):
    bCheckFlanking: bool



class AIAspect_FlyToNavMesh(AIAspect_Navigation):
    FlyToNavMeshSettings: AIAspectSettings_FlyToNavMesh



class AIAspect_FollowUpdate(AIAspect):
    Settings: AIAspectSettings_Follow
    NavSettings: AIAspectSettings_Navigation
    TeleportTarget: gbx_game_system_core.GbxBlackboardKeySelector
    MoveTarget: gbx_game_system_core.GbxBlackboardKeySelector
    Distance: gbx_game_system_core.GbxBlackboardKeySelector



class AIAspect_GroupLocation(AIAspect):
    Settings: AIAspectSettings_GroupLocation



class AIAspect_IntCompare(AIAspect):
    Settings: AIAspectSettings_IntCompare



class AIAspect_IsInRange(AIAspect):
    Settings: AIAspectSettings_IsInRange



class AIAspect_IsInTerritory(AIAspect):
    Settings: AIAspectSettings_IsInTerritory



class AIAspect_Land(AIAspect_Navigation):
    LandSettings: AIAspectSettings_Land



class AIAspect_LeadUpdate(AIAspect):
    LeadSettings: AIAspectSettings_LeadRoute
    MoveTarget: gbx_game_system_core.GbxBlackboardKeySelector
    Distance: gbx_game_system_core.GbxBlackboardKeySelector
    TeleportTarget: gbx_game_system_core.GbxBlackboardKeySelector



class AIAspect_Leap(AIAspect):
    Settings: AIAspectSettings_Leap
    def GetQuerySettingsDescription(self, LeapSettings: AIAspectSettings_Leap, Property: core_uobject.Property, ReturnValue: str) -> str: ...


class AIAspect_Location(AIAspect):
    Settings: AIAspectSettings_Location



class AIAspect_LockTarget(AIAspect):
    bFailOnTargetChange: bool



class AIAspect_LookAroundRandomly(AIAspect): ...


class AIAspect_Loop(AIAspect):
    Settings: AIAspectSettings_Loop
    def GetSettingsDescription(self, LoopSettings: AIAspectSettings_Loop, ReturnValue: str) -> str: ...


class AIAspect_MoveSpline(AIAspect_Navigation):
    MoveSplineSettings: AIAspectSettings_MoveSpline



class AIAspect_NavBlackboard(AIAspect_Navigation):
    GoalKey: gbx_game_system_core.GbxBlackboardKeySelector
    MinOffsetInFrontOfTarget: float
    MaxOffsetInFrontOfTarget: float
    OffsetAngle: float
    Reach: gbx_nav.EGbxNavGoalReach



class AIAspect_NavCover(AIAspect_Navigation):
    GoalKey: gbx_game_system_core.GbxBlackboardKeySelector



class AIAspect_NavFlyOffset(AIAspect_Navigation):
    OffsetSettings: AIAspectSettings_NavFlyOffset



class AIAspect_Orbit(AIAspect_Navigation):
    OrbitSettings: AIAspectSettings_Orbit



class AIAspect_Plan(AIAspect):
    Settings: AIAspectSettings_Plan



class AIAspect_Rotation(AIAspect):
    Settings: AIAspectSettings_Rotation
    def GetRotationSettingsDescription(self, RotationSettings: AIAspectSettings_Rotation, Property: core_uobject.Property, ReturnValue: str) -> str: ...
    def GetRotationChannelSettingsDescription(self, RotationChannelSettings: AIAspectSettings_RotationChannel, Property: core_uobject.Property, ReturnValue: str) -> str: ...


class AIAspect_Route(AIAspect):
    RouteSettings: AIAspectSettings_Route
    MoveTarget: gbx_game_system_core.GbxBlackboardKeySelector
    Distance: gbx_game_system_core.GbxBlackboardKeySelector
    SmartAction: gbx_game_system_core.GbxBlackboardKeySelector
    BodyEnable: gbx_game_system_core.GbxBlackboardKeySelector
    BodyTarget: gbx_game_system_core.GbxBlackboardKeySelector
    LookEnable: gbx_game_system_core.GbxBlackboardKeySelector
    LookTarget: gbx_game_system_core.GbxBlackboardKeySelector



class AIAspect_Stance(AIAspect):
    Settings: AIAspectSettings_Stance



class AIAspect_Sweep(AIAspect_Orbit):
    SweepSettings: AIAspectSettings_Sweep



class AIAspect_Swoop(AIAspect_Navigation):
    SwoopSettings: AIAspectSettings_Swoop



class AIAspect_TakeOff(AIAspect_GbxAction):
    NearFlightDistance: float



class AIAspect_Teleport(AIAspect):
    Settings: AIAspectSettings_Teleport
    def GetTeleportSettingsDescription(self, TeleportSettings: AIAspectSettings_Teleport, Property: core_uobject.Property, ReturnValue: str) -> str: ...


class AIAspect_Territory(AIAspect):
    TerritoryKeys: unreal.WrappedArray[gbx_game_system_core.GbxBlackboardKeySelector]



class AIAspect_Ticket(AIAspect):
    Settings: AIAspectSettings_Ticket



class AIAspect_TimedCondition(AIAspect):
    Settings: AIAspectSettings_TimedCondition



class AIAspect_TimeLimit(AIAspect):
    Settings: AIAspectSettings_TimeLimit



class AIAspect_Timer(AIAspect):
    Settings: AIAspectSettings_Timer



class AIAspect_UseCover(AIAspect):
    Settings: AIAspectSettings_UseCover



class AIAspect_UseSmartObject(AIAspect_GbxAction): ...


class AIAspect_Weapon(AIAspect):
    Settings: AIAspectSettings_Weapon
    def GetWeaponSettingsDescription(self, WeaponSettings: AIAspectSettings_Weapon, Property: core_uobject.Property, ReturnValue: str) -> str: ...


class AIAspect_ZeroRotation(AIAspect):
    Settings: AIAspectSettings_ZeroRotation



class AIAspectBlueprint(engine.Blueprint):
    ParentBlueprint: AIAspectBlueprint



class AICloakData(engine.DataAsset):
    CloakPriorities: unreal.WrappedArray[CloakCondition]
    bDefaultCloaked: bool



class AICloakComponent(engine.ActorComponent):
    DefaultCloakData: AICloakData
    bRender: bool
    bCollide: bool
    bVisible: bool
    bTargetable: bool
    bGodMode: bool
    bDemigodMode: bool
    bAllowHitReactions: bool
    bOnlyMoveWhileCloaked: bool
    bCanCloakWithMovementHold: bool
    bCloakedOnSpawn: bool
    RenderExceptions: unreal.WrappedArray[str]
    MinimumTransitionTime: float
    CloakedStance: gbx_game_system_core.StanceDataProvider
    ActionCloak: unreal.UClass
    ActionUncloak: unreal.UClass
    bCloakAfterAction: bool
    bUncloakAfterAction: bool
    bCanInterruptActions: bool
    bLockActions: bool
    OverrideData: AICloakData
    ActionComp: gbx_game_system_core.GbxActionComponent
    TargetableComp: gbx_game_system_core.TargetableComponent
    NavComp: gbx_nav.GbxNavComponent
    MoveComp: gbx_game_system_core.GbxCharacterMovementComponent
    StanceComp: gbx_game_system_core.StanceComponent
    DamageComp: gbx_game_system_core.DamageComponent
    SavedCollision: gbx_game_system_core.SavedCollision
    RepData: CloakRepData
    PrimCompData: unreal.WrappedArray[CloakPrimData]
    def SetCloakData(self, NewCloakData: AICloakData): ...
    def OnRep_Cloaked(self): ...
    def IsPlayingAction(self, ReturnValue: bool) -> bool: ...
    def IsCloakStateForced(self, ReturnValue: bool) -> bool: ...
    def IsCloaked(self, ReturnValue: bool) -> bool: ...
    def InterruptCloakAction(self): ...
    def GetCloakData(self, ReturnValue: AICloakData) -> AICloakData: ...
    def ForceUncloak(self, bInCanPlayActions: bool): ...
    def ForceCloak(self, bInCanPlayActions: bool): ...
    def ClearForcedState(self): ...
    def ClearCloakData(self): ...


class AIConstraint(AIAspect): ...


class AIGroupBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def IsUsingAITicket(self, AIUser: aimodule.AIController, Ticket: AITicketDataAsset, bInterruptible: bool, ReturnValue: bool) -> bool: ...
    def IsTicketValid(self, TicketHandle: AITicketHandle, ReturnValue: bool) -> bool: ...
    def ClearTicket(self, TicketHandle: AITicketHandle, HoldDuration: float): ...
    def ClearAITicket(self, AIUser: aimodule.AIController, Ticket: AITicketDataAsset, HoldDuration: float): ...
    def CanUseAITicket(self, AIUser: aimodule.AIController, Ticket: AITicketDataAsset, Value: float, bInterruptible: bool, ReturnValue: bool) -> bool: ...
    def AddAITicket(self, OutTicketHandle: AITicketHandle, AIUser: aimodule.AIController, Ticket: AITicketDataAsset, Value: float, MaxDuration: float, bPriority: bool, bInterruptible: bool, ReturnValue: bool) -> bool: ...


class AIGroupState(unreal.UObject):
    LinkComponent: gbx_spawn.SpawnerLinkComponent
    TicketManager: AITicketManager
    CommunicationManager: AICommunicationManager
    PlanManager: AIPlanManager
    TargetPersistentNotes: unreal.WrappedArray[gbx_game_system_core.TargetPersistentNotes]
    def OnThreatActorDied(self, DamageReceiver: engine.Actor, DamageCauser: engine.Actor): ...


class AINode(engine.Actor):
    AINodeComponent: AINodeComponent
    def OnPawnDepartedNodeCB(self, NodeActor: engine.Actor, DepartedPawn: engine.Pawn): ...
    def OnPawnArrivedNodeCB(self, NodeActor: engine.Actor, ArrivedPawn: engine.Pawn): ...


class AINodeBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def FindNearestNode(self, WorldContextObject: unreal.UObject, Location: core_uobject.Vector, bIncludeDisabled: bool, ReturnValue: engine.Actor) -> engine.Actor: ...
    def FindAllNodes(self, OutputNodes: unreal.WrappedArray[engine.Actor], WorldContextObject: unreal.UObject, bIncludeDisabled: bool): ...
    def ChooseRandomNode(self, WorldContextObject: unreal.UObject, bIncludeDisabled: bool, ReturnValue: engine.Actor) -> engine.Actor: ...


class AINodeComponent(engine.PrimitiveComponent):
    bEnabled: bool
    bUseRouteSystem: bool
    RouteFindNavHeight: float
    bDrawRouteFindNavHeight: bool
    ArrivalThreshold: float
    ArrivalHeightThreshold: float
    bSnapToGround: bool
    MaxSnapDistance: float
    LinksTo: unreal.WrappedArray[AINodeLink]
    EditCache: unreal.WrappedArray[engine.Actor]
    LinksFrom: unreal.WrappedArray[AINodeComponent]
    bLinkOnAltDrag: bool
    bVisualizeWhileUnlinked: bool
    bRouteSelected: bool
    bSelected: bool
    def SelectNextNode(self, ReturnValue: engine.Actor) -> engine.Actor: ...
    def HasLinkTo(self, Node: engine.Actor, ReturnValue: bool) -> bool: ...
    def HasLinkFrom(self, Node: engine.Actor, ReturnValue: bool) -> bool: ...
    def HasArrived(self, Point: core_uobject.Vector, Error: float, ReturnValue: bool) -> bool: ...
    def GetLinkedNodeNum(self, ReturnValue: int) -> int: ...
    def GetLinkedNode(self, I: int, ReturnValue: engine.Actor) -> engine.Actor: ...
    def CreateLinkTo(self, Node: engine.Actor, Weight: float): ...
    def BreakLinkTo(self, Node: engine.Actor, ReturnValue: bool) -> bool: ...


class AIPlanData(gbx_runtime.GbxDataAsset):
    MaxNumberOfInstances: gbx_game_system_core.GbxParam
    RoleRequirements: unreal.WrappedArray[PlanRoleRequirements]



class AISense_Proximity(aimodule.AISense): ...


class AISense_Threat(aimodule.AISense):
    TargetingComponents: unreal.WrappedArray[gbx_game_system_core.TargetingComponent]
    UpdatePeriod: float



class AISenseConfig_Proximity(aimodule.AISenseConfig):
    SenseEnemyDistance: float
    DetectionByAffiliation: aimodule.AISenseAffiliationFilter



class AISenseConfig_Threat(aimodule.AISenseConfig):
    DetectionByAffiliation: aimodule.AISenseAffiliationFilter
    Implementation: unreal.UClass



class AIStanceData(gbx_game_system_core.StanceData):
    AIPathFindData: gbx_nav.HavokPathFindingData
    AIStrafeType: gbx_nav.EGbxStrafeType



class AITargetingBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def IsThreatenedByInfo(self, AIActor: engine.Actor, TargetInfo: gbx_game_system_core.TargetActorInfo, ReturnValue: bool) -> bool: ...
    def IsThreatenedBy(self, AIActor: engine.Actor, Target: engine.Actor, ReturnValue: bool) -> bool: ...
    def GetTargetSenseAge(self, TargetInfo: gbx_game_system_core.TargetActorInfo, Sense: unreal.UClass, ReturnValue: float) -> float: ...
    def GetNumTargetsInRange(self, AIActor: engine.Actor, Radius: float, ReturnValue: int) -> int: ...
    def GetBestKnownLocation(self, AIActor: engine.Actor, TargetActor: engine.Actor, Socket: str, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def CalcTargetGroupLocation(self, AIActor: engine.Actor, GroupDistance: float, Result: core_uobject.Vector, ReturnValue: bool) -> bool: ...
    def ApplyTargetScoringBoost(self, TargetActor: engine.Actor, BoostName: str, ScoringBoost: gbx_game_system_core.EAITargetScoringBoost, DurationInSeconds: float): ...
    def AISetTargetInBlackboard(self, AIActor: engine.Actor, Key: gbx_game_system_core.GbxBlackboardKeySelector, TargetIndex: int): ...
    def AISetScriptedTarget(self, AIActor: engine.Actor, TargetActor: engine.Actor): ...
    def AISendCommunication(self, AIActor: engine.Actor, Radius: float): ...
    def AIProvokeSpecificSense(self, AITarget: engine.Actor, Source: engine.Actor, SenseType: unreal.UClass, StimulusLocation: core_uobject.Vector): ...
    def AIProvoke(self, AITarget: engine.Actor, Source: engine.Actor): ...
    def AIPlayerProvoke(self, AITarget: engine.Actor): ...
    def AIGetScriptedTarget(self, AIActor: engine.Actor, ReturnValue: engine.Actor) -> engine.Actor: ...
    def AICanCommunicate(self, AIActor: engine.Actor, Radius: float, MinSenseAgeDelta: float, ReturnValue: bool) -> bool: ...


class AITask_UseLookAtPoint(aimodule.AITask):
    LookAtPointComponent: LookAtPointComponent
    Tag: LookAtPointTag
    MoveToTask: aimodule.AITask_MoveTo
    State: ESmartObjectTaskState



class AITask_UsePerch(aimodule.AITask):
    PerchComponent: PerchComponent
    Tag: PerchTag
    MoveToTask: aimodule.AITask_MoveTo
    State: ESmartObjectTaskState



class AITask_UseSmartObject(aimodule.AITask): ...


class AITicketDataAsset(gbx_runtime.GbxDataAsset):
    MaxValue: gbx_game_system_core.GbxParam
    DefaultMaxHoldTime: gbx_game_system_core.GbxParam
    bPerActor: bool
    ActorBlackboardKeyName: str



class AIUsableComponent(engine.ActorComponent):
    bEnabled: bool
    SmartObjectComponent: SmartObjectComponent
    UseSlots: unreal.WrappedArray[AIUseSlotComponent]



class AIUseComponent(engine.ActorComponent):
    CachedPawn: engine.Pawn
    CachedController: GbxAIController
    CachedActionComponent: gbx_game_system_core.GbxActionComponent
    UseState: ActionUseState
    bInitializingAction: bool
    GlobalCooldowns: unreal.WrappedArray[ActionCooldownInfo]
    def StopUse(self, bSucceeded: bool): ...
    def RequestUse(self, SmartObject: engine.Actor, ActionName: gameplay_tags.GameplayTag, bAbortExisting: bool, bUntilInterrupted: bool, ReturnValue: bool) -> bool: ...
    def OnUseCompleted(self, Task: aimodule.AITask, Result: ESmartObjectTaskResult): ...
    def GetCurrentObject(self, ReturnValue: engine.Actor) -> engine.Actor: ...


class AIUseSlotComponent(engine.PrimitiveComponent):
    bEnabled: bool
    bSnapToGround: bool
    AlignRule: ESlotAlignRule
    bInterpOnArrival: bool
    bInterpRotationOnArrival: bool
    InterpOnArrivalTime: float
    LookAtRule: ESmartObjectLookAtRule
    bOverrideLookAtRule: bool
    LookAtSocket: str
    ActionTypes: gameplay_tags.GameplayTagContainer
    Radius: float
    bMaxUsers: bool
    MaxUsers: int
    bForceUsePhysNoneWithRootMotion: bool
    Users: unreal.WrappedArray[engine.Controller]
    def GetAvailableSocketNames(self, Array: unreal.WrappedArray[str]): ...


class AIWeaponUserComponent(engine.ActorComponent):
    AIController: GbxAIController
    GbxCharacter: gbx_game_system_core.GbxCharacter
    FireConeAngle: float
    DamageComponent: gbx_game_system_core.DamageComponent
    CoverUserComponent: CoverUserComponent
    BlackboardComponent: aimodule.BlackboardComponent
    PerceptionComponent: aimodule.AIPerceptionComponent
    TargetingComponent: gbx_game_system_core.TargetingComponent
    CanFireIf: gbx_runtime.GbxCondition
    Settings: AIWeaponUseSettings
    SettingsOverride: AIWeaponUseSettings
    bSuppressingFireTimeExpired: bool
    BurstCountOverride: gbx_game_system_core.GbxParam
    bOverrideBurstCount: bool
    BurstDelayOverride: gbx_game_system_core.GbxParam
    bOverrideBurstDelay: bool
    AccuracyOverride: gbx_game_system_core.GbxParam
    bOverrideAccuracy: bool
    DesiredRangeOverride: gbx_runtime.NumericRange
    bOverrideDesiredRange: bool
    def WantsToFire(self, ReturnValue: bool) -> bool: ...
    def OnWeaponUsed(self): ...


class AnimNotify_SmartObject(engine.AnimNotifyState):
    Action: ESmartObjectNotify



class AnimNotify_UseSmartAction(engine.AnimNotify): ...


class BlackboardKeyType_SmartAction(aimodule.BlackboardKeyType): ...


class BTComposite_Random(aimodule.BTComposite_Selector):
    Entries: unreal.WrappedArray[BTRandomEntrySettings]



class BTDecorator_AIAction(aimodule.BTDecorator): ...


class UBTDecorator_AITicket(aimodule.BTDecorator): ...


class BTDecorator_GbxLoop(aimodule.BTDecorator):
    LoopCount: gbx_game_system_core.GbxParam
    bUseLoopCount: bool
    LoopTime: gbx_game_system_core.GbxParam
    bUseLoopTime: bool
    LoopCondition: BTGbxLoopConditionData
    bUseLoopCondition: bool



class BTDecorator_IsInRange(aimodule.BTDecorator_BlackboardBase):
    Range: gbx_game_system_core.GbxParam



class BTService_GameFocus(aimodule.BTService_DefaultFocus): ...


class BTService_GbxRunEQS(aimodule.BTService_RunEQS): ...


class BTTask_AIAction_Custom(BTTask_AIAction):
    Action: AIAction



class BTTask_LookAt(aimodule.BTTaskNode):
    AngleThresholdDegrees: float
    TargetActorKey: aimodule.BlackboardKeySelector
    TurnSpeedKey: aimodule.BlackboardKeySelector



class BTTask_MoveToComponent(aimodule.BTTask_BlackboardBase):
    AcceptableRadius: float
    bAllowStrafe: bool
    bStopOnOverlap: bool
    bAllowPartialPath: bool
    bProjectGoalLocation: bool



class BTTask_MoveToNode(aimodule.BTTask_MoveTo): ...


class BTTask_UseCover(aimodule.BTTaskNode): ...


class BTTask_UseSmartObject(aimodule.BTTaskNode): ...


class Cover(engine.Actor):
    DefaultCoverSlotName: core_uobject.SoftObjectPath
    SlotType: CoverSlotData
    SlotInterval: float
    TotalWidth: float
    bSlotsAlwaysVisible: bool
    bDrawLineOfSight: bool
    bDrawAreas: bool
    bDrawInvalidViews: bool
    bDrawLocationTests: bool
    Slots: unreal.WrappedArray[CoverSlotComponent]
    bOverrideAutoAdjust: bool
    AutoAdjustParamsOverride: CoverAdjustParams
    TargetTestActor: engine.Actor
    HostileTestActor: engine.Actor
    bAutoAdjust: bool
    def SetEnabled(self, bEnabled: bool): ...
    def IsEnabled(self, ReturnValue: bool) -> bool: ...


class CoverSlotComponent(engine.PrimitiveComponent):
    SlotType: CoverSlotData
    bEnabled: bool
    bAutoDetect: bool
    bValid: bool
    Views: unreal.WrappedArray[CoverSlotViewData]
    FailedViews: unreal.WrappedArray[CoverSlotViewFailData]
    SlotHeight: ECoverSlotHeight
    OverlappingSlots: unreal.WrappedArray[CoverSlotComponent]
    ExposedLosData: CoverLineOfSightData
    SlotOwnerUsing: engine.Pawn
    SlotOwnerClaimed: engine.Pawn
    def SetEnabled(self, bNewEnabled: bool): ...
    def IsEnabled(self, ReturnValue: bool) -> bool: ...


class CoverSlotData(gbx_runtime.GbxDataAsset):
    SlotWidth: float
    SlotHeightLow: float
    SlotHeightHigh: float
    bOffGroundCover: bool
    ExposedParams: CoverLineOfSightParams
    bCheckExposure: bool
    AutoAdjustParams: CoverAdjustParams
    Views: unreal.WrappedArray[CoverViewData]
    ValidColor: core_uobject.Color
    NavSearchRadius: float



class CoverStyleData(gbx_runtime.GbxDataAsset):
    AnimType: ECoverStyleAnimType
    View: CoverViewData
    bAllowLookAts: bool
    bAllowAimOffsets: bool
    bForceFiring: bool



class GbxCoverTransitionTable(gbx_game_system_core.GbxAnimTable):
    AnimSet: engine.GbxAnimSet
    Filters: CoverTransitionFilters
    DefaultHeight: float



class CoverUserComponent(engine.ActorComponent):
    DesiredAction: CoverAction
    CurrentAction: CoverAction
    PreviousAction: CoverAction
    State: ECoverUserState
    DesiredState: ECoverUserState
    TransitionName: str
    SkelMeshComponent: engine.SkeletalMeshComponent
    GbxCharacter: gbx_game_system_core.GbxCharacter
    GbxAIController: GbxAIController
    DamageComponent: gbx_game_system_core.DamageComponent
    GbxNavComponent: gbx_nav.GbxNavComponent
    StanceComponent: gbx_game_system_core.StanceComponent
    TargetingComponent: gbx_game_system_core.TargetingComponent
    WeaponUserComponent: AIWeaponUserComponent
    MovementComponent: gbx_nav.GbxNavCharacterMovementComponent
    SavedCollision: gbx_game_system_core.SavedCollision
    ClientData: CoverClientData
    bFlanked: bool
    MaxVerticalNavDistance: float
    MaxHorizontalNavDistance: float
    MaxDeltaLocationThreshold: float
    MaxDeltaRotationThreshold: float
    ExitInterpSearchDistance: float
    TransitionBetweenTraceHeight: float
    WidthAdjustment: float
    HeightAdjustment: float
    bDisableFootIk: bool
    Styles: unreal.WrappedArray[CoverStyleUserData]
    FireToIdleStates: unreal.WrappedArray[str]
    DefaultIdleTime: gbx_game_system_core.GbxParam
    DefaultFireTime: gbx_game_system_core.GbxParam
    DefaultWaitTimeBeforeSeekingBetterCover: gbx_game_system_core.GbxParam
    TicketForAdvancingToBetterCover: AITicketUseData
    FaceDirections: CoverFaceDirections
    HitReactionLayer: unreal.UClass
    TransitionBlendTime: float
    NearCoverDistance: float
    EnterTransitionTable: GbxCoverTransitionTable
    BetweenTransitionTable: GbxCoverTransitionTable
    def SetEnterTransitionTable(self, NewTable: GbxCoverTransitionTable): ...
    def OnRep_ClientData(self): ...
    def OnMovementModeChanged(self, Character: engine.Character, PrevMovementMode: int, PreviousCustomMode: int): ...
    def GetStyle(self, ReturnValue: CoverStyleData) -> CoverStyleData: ...


class CoverViewData(gbx_runtime.GbxDataAsset):
    SlotHeight: ECoverSlotHeight
    ViewOffset: core_uobject.Vector
    TargetParams: CoverLineOfSightParams
    ForwardCheckDistance: float
    ForwardCheckExtent: core_uobject.Vector



class EnvQueryContext_AllTargets(aimodule.EnvQueryContext): ...


class EnvQueryContext_Friendlies(aimodule.EnvQueryContext): ...


class EnvQueryContext_Target(aimodule.EnvQueryContext): ...


class EnvQueryContext_TargetActualLocation(aimodule.EnvQueryContext): ...


class EnvQueryGenerator_AINodes(aimodule.EnvQueryGenerator):
    SearchCenter: unreal.UClass
    SearchRadius: aimodule.AIDataProviderFloatValue
    TagQuery: gbx_game_system_core.ActorTagCompositeQuery
    bUseAllowedTypes: bool
    bUseDisallowedTypes: bool
    AllowedTypesCache: unreal.WrappedArray[unreal.UClass]
    DisallowedTypesCache: unreal.WrappedArray[unreal.UClass]



class EnvQueryGenerator_Cover(aimodule.EnvQueryGenerator):
    SlotTypes: unreal.WrappedArray[CoverSlotData]
    SearchRadius: aimodule.AIDataProviderFloatValue
    SearchCenter: unreal.UClass
    SlotType: CoverSlotData



class EnvQueryGenerator_DynamicPoints(aimodule.EnvQueryGenerator_ProjectedPoints):
    InnerRadius: aimodule.AIDataProviderFloatValue
    OuterRadius: aimodule.AIDataProviderFloatValue
    PointsPerRing: EQSDynamicPointRange
    NumberOfRings: EQSDynamicPointRange
    NumberOfLayers: EQSDynamicPointRange
    TopLayerHeight: aimodule.AIDataProviderFloatValue
    BottomLayerHeight: aimodule.AIDataProviderFloatValue
    bUseLayers: bool
    NumberOfPointsMin: int
    NumberOfPointsMax: int
    ArcDirection: aimodule.EnvDirection
    ArcAngle: aimodule.AIDataProviderFloatValue
    bDefineArc: bool
    Center: unreal.UClass



class EnvQueryGenerator_FindLookAtPoint(aimodule.EnvQueryGenerator):
    LookAtPointType: ELookAtPointType
    SearchRadius: aimodule.AIDataProviderFloatValue
    SearchCenter: unreal.UClass



class EnvQueryGenerator_FindPerch(aimodule.EnvQueryGenerator):
    PerchType: PerchType
    SearchRadius: aimodule.AIDataProviderFloatValue
    SearchCenter: unreal.UClass



class EnvQueryGenerator_SmartAction(aimodule.EnvQueryGenerator):
    CombatActions: aimodule.AIDataProviderBoolValue
    PassiveActions: aimodule.AIDataProviderBoolValue
    ActorTypesCache: unreal.WrappedArray[unreal.UClass]
    ActionNames: gameplay_tags.GameplayTagContainer
    SearchRadius: aimodule.AIDataProviderFloatValue
    SearchCenter: unreal.UClass
    TerritoryArea: gbx_game_system_core.ETerritoryType
    bUseTerritoryArea: bool



class EnvQueryGenerator_SmartGrid(aimodule.EnvQueryGenerator_ProjectedPoints):
    SearchSets: unreal.WrappedArray[SmartGridSearchSet]



class EnvQueryGenerator_Territory(aimodule.EnvQueryGenerator_ProjectedPoints):
    TerritoryArea: gbx_game_system_core.ETerritoryType
    SpaceBetween: aimodule.AIDataProviderFloatValue
    EverywhereRadius: aimodule.AIDataProviderFloatValue
    MovementType: ETerritoryMovementType



class EnvQueryItemType_SmartAction(aimodule.EnvQueryItemType_VectorBase): ...


class EnvQueryTest_ActorHealth(aimodule.EnvQueryTest):
    bHealthPercentage: bool
    bHealthConsumed: bool



class EnvQueryTest_AITicket(aimodule.EnvQueryTest):
    AITicket: AITicketDataAsset
    Value: aimodule.AIDataProviderFloatValue



class EnvQueryTest_Angle(aimodule.EnvQueryTest):
    LineA: aimodule.EnvDirection
    LineAHeadingOffset: aimodule.AIDataProviderFloatValue
    LineAPitchOffset: aimodule.AIDataProviderFloatValue
    LineB: aimodule.EnvDirection
    LineBHeadingOffset: aimodule.AIDataProviderFloatValue
    LineBPitchOffset: aimodule.AIDataProviderFloatValue
    bTestHeading: bool
    bTestPitch: bool



class EnvQueryTest_ArcTrace(aimodule.EnvQueryTest_Trace):
    ArcSpeed: aimodule.AIDataProviderFloatValue
    ArcAnglePercent: aimodule.AIDataProviderFloatValue
    NumSegments: int



class EnvQueryTest_AttackerCountAgainstTarget(aimodule.EnvQueryTest): ...


class EnvQueryTest_BlackboardKey(aimodule.EnvQueryTest):
    BlackboardKey: gbx_game_system_core.GbxBlackboardKeySelector



class EnvQueryTest_Boundary(aimodule.EnvQueryTest):
    Distance: aimodule.AIDataProviderFloatValue



class EnvQueryTest_CoverCurrent(aimodule.EnvQueryTest): ...


class EnvQueryTest_CoverExposure(aimodule.EnvQueryTest):
    Context: unreal.UClass
    DoExposureTest: aimodule.AIDataProviderBoolValue



class EnvQueryTest_CoverView(aimodule.EnvQueryTest):
    Context: unreal.UClass
    DoViewTest: aimodule.AIDataProviderBoolValue



class EnvQueryTest_CurrentTarget(aimodule.EnvQueryTest): ...


class EnvQueryTest_CustomScoringBoost(aimodule.EnvQueryTest):
    ReductionExtreme: float
    ReductionModerate: float
    ReductionLight: float
    NoBoostWeighting: float
    AmplificationLight: float
    AmplificationModerate: float
    AmplificationExtreme: float



class EnvQueryTest_DirectPath(aimodule.EnvQueryTest):
    Context: unreal.UClass
    CloseEnoughDistance: float



class EnvQueryTest_GbxPath(aimodule.EnvQueryTest):
    Context: unreal.UClass



class EnvQueryTest_IsInGodMode(aimodule.EnvQueryTest): ...


class EnvQueryTest_MyMasterIsAttackingTarget(aimodule.EnvQueryTest):
    DecayRate: float



class EnvQueryTest_PetModifier(aimodule.EnvQueryTest):
    PetTag: gameplay_tags.GameplayTag
    BossTag: gameplay_tags.GameplayTag



class EnvQueryTest_PetOwnerDistance(aimodule.EnvQueryTest):
    MaxDistanceToOwner: aimodule.AIDataProviderFloatValue
    AnyDistanceTag: gameplay_tags.GameplayTag



class EnvQueryTest_StandardCover(aimodule.EnvQueryTest):
    FriendliesContext: unreal.UClass
    TargetContext: unreal.UClass
    ExposureContext: unreal.UClass
    TargetDistanceMinPriorToTakingCover: aimodule.AIDataProviderFloatValue
    TargetDistanceMaxPriorToTakingCover: aimodule.AIDataProviderFloatValue
    TargetDistanceMinMultiplierAfterTakingCover: float
    TargetDistanceMaxMultiplierAfterTakingCover: float
    QuerierMaxDistance: aimodule.AIDataProviderFloatValue
    DoViewTest: aimodule.AIDataProviderBoolValue
    DoExposureTest: aimodule.AIDataProviderBoolValue
    FriendlyDistance: aimodule.AIDataProviderFloatValue
    ScoringWeight_AlreadyAtCover: float
    ScoringWeight_DistanceToQuerier: float
    ScoringWeight_DistanceToTarget: float
    ScoringWeight_DistanceToFriendlies: float
    ScoringWeight_CoverView: float
    ScoringWeight_CoverExposure: float



class EnvQueryTest_TacticalCover(aimodule.EnvQueryTest):
    Context: unreal.UClass



class EnvQueryTest_TargetIsAttackingMyMaster(aimodule.EnvQueryTest):
    DecayRate: float



class EnvQueryTest_TargetIsCloseToMyMaster(aimodule.EnvQueryTest):
    DistanceThreshold: gbx_game_system_core.GbxParam



class EnvQueryTest_TargetIsExposed(aimodule.EnvQueryTest): ...


class EnvQueryTest_TargetIsHurtingMe(aimodule.EnvQueryTest):
    DecayRate: float



class EnvQueryTest_TargetIsThreat(aimodule.EnvQueryTest): ...


class EnvQueryTest_TargetSensed(aimodule.EnvQueryTest):
    DevLabel: str
    SensesToTestFor: unreal.WrappedArray[unreal.UClass]
    TimeToCareAboutStimuli: float



class EnvQueryTest_UberTrace(aimodule.EnvQueryTest_Trace):
    TracesToPerform: unreal.WrappedArray[ExtendedTraceInfo]
    bWantsTracesToHit: bool



class EnvQueryTest_WithinTerritory(aimodule.EnvQueryTest):
    TerritoryArea: gbx_game_system_core.ETerritoryType



class AIResource_ScriptedAction(gameplay_tasks.GameplayTaskResource): ...


class GameplayTask_ScriptedAction(gameplay_tasks.GameplayTask):
    Controllers: unreal.WrappedArray[GbxAIController]
    AbortingControllers: unreal.WrappedArray[GbxAIController]
    ScriptedAIAction: AIAction
    def OnActorSpawned(self, Spawner: gbx_spawn.Spawner, Actor: engine.Actor): ...


class GameplayTask_ScriptedCover(GameplayTask_ScriptedAction):
    CoverSlot: CoverSlotComponent
    CoverUser: CoverUserComponent
    def TaskScriptedCoverDelegate__DelegateSignature(self): ...
    def EndScriptedCover(self, User: engine.Actor): ...
    def BeginScriptedCover(self, User: engine.Actor, Cover: Cover, ReturnValue: GameplayTask_ScriptedCover) -> GameplayTask_ScriptedCover: ...


class GameplayTask_ScriptedFollow(GameplayTask_ScriptedAction):
    ActorToFollow: engine.Actor
    StanceProvider: gbx_game_system_core.StanceDataProvider
    def TaskScriptedMoveDelegate__DelegateSignature(self): ...
    def BeginScriptedFollow(self, Follower: engine.Actor, ActorToFollow: engine.Actor, OptionalStance: gbx_game_system_core.StanceDataProvider, ReturnValue: GameplayTask_ScriptedFollow) -> GameplayTask_ScriptedFollow: ...


class GameplayTask_ScriptedLand(GameplayTask_ScriptedAction):

    def TaskScriptedLandDelegate__DelegateSignature(self): ...
    def BeginScriptedLand(self, Lander: engine.Actor, ReturnValue: GameplayTask_ScriptedLand) -> GameplayTask_ScriptedLand: ...


class GameplayTask_ScriptedLead(GameplayTask_ScriptedAction):
    DestNode: engine.Actor
    ActorToLead: engine.Actor
    StanceProvider: gbx_game_system_core.StanceDataProvider
    def TaskScriptedLeadDelegate__DelegateSignature(self): ...
    def BeginScriptedLead(self, Leader: engine.Actor, DestAINode: engine.Actor, ActorToLead: engine.Actor, OptionalStance: gbx_game_system_core.StanceDataProvider, ReturnValue: GameplayTask_ScriptedLead) -> GameplayTask_ScriptedLead: ...


class GameplayTask_ScriptedMove(GameplayTask_ScriptedAction):
    AINode: engine.Actor
    StanceProvider: gbx_game_system_core.StanceDataProvider
    LookAtActor: engine.Actor
    bTeleportOnFail: bool
    def TaskScriptedMoveDelegate__DelegateSignature(self): ...
    def BeginScriptedMoveActor(self, Target: aimodule.AIController, StartNode: engine.Actor, OptionalStance: gbx_game_system_core.StanceDataProvider, OptionalLookAtActor: engine.Actor, ReturnValue: GameplayTask_ScriptedMove) -> GameplayTask_ScriptedMove: ...
    def BeginScriptedMove2(self, User: engine.Actor, StartAINode: engine.Actor, OptionalStance: gbx_game_system_core.StanceDataProvider, OptionalLookAtActor: engine.Actor, ReturnValue: GameplayTask_ScriptedMove) -> GameplayTask_ScriptedMove: ...
    def BeginScriptedMove(self, Target: engine.Actor, StartNode: engine.Actor, SuccessRule: EScriptedActionRule, FailRule: EScriptedActionRule, bAddSpawned: bool, OptionalStance: gbx_game_system_core.StanceDataProvider, OptionalLookAtActor: engine.Actor, bTeleportOnFail: bool, ReturnValue: GameplayTask_ScriptedMove) -> GameplayTask_ScriptedMove: ...


class GameplayTask_ScriptedMoveSpline(GameplayTask_ScriptedAction):
    Target: engine.Actor
    SplineComponent: engine.SplineComponent
    StanceProvider: gbx_game_system_core.StanceDataProvider
    LookAtActor: engine.Actor
    OptionalAIAction: unreal.UClass
    DropOffSpawner: GbxSpawner
    NextSpline: engine.Actor
    def TaskScriptedMoveDelegate__DelegateSignature(self, Targeted: engine.Actor): ...
    def BeginScriptedMoveOnSpline(self, Target: engine.Actor, StartSpline: engine.Actor, SuccessRule: EScriptedActionRule, FailRule: EScriptedActionRule, Offset: float, bReverse: bool, bAddSpawned: bool, OptionalStance: gbx_game_system_core.StanceDataProvider, OptionalLookAtActor: engine.Actor, OptionalAIAction: unreal.UClass, ReturnValue: GameplayTask_ScriptedMoveSpline) -> GameplayTask_ScriptedMoveSpline: ...


class AIAction_MoveToLevelSequence(AIAction_GoToPoint): ...


class GameplayTask_ScriptedMoveToLevelSequence(GameplayTask_ScriptedAction):
    LevelSequenceActor: gbx_level_sequence.GbxLevelSequenceActor
    StanceProvider: gbx_game_system_core.StanceDataProvider
    def TaskScriptedMoveDelegate__DelegateSignature(self): ...
    def TaskScriptedMoveActorsDelegate__DelegateSignature(self): ...
    def TaskScriptedMoveActorDelegate__DelegateSignature(self, Actor: engine.Actor): ...
    def OnLevelSequenceStopped(self): ...
    def OnLevelSequenceFinished(self): ...
    def BeginScriptedMoveToLevelSequenceMulti(self, Targets: unreal.WrappedArray[engine.Actor], LevelSequenceActor: gbx_level_sequence.GbxLevelSequenceActor, bStartSequence: bool, OptionalStance: gbx_game_system_core.StanceDataProvider, ReturnValue: GameplayTask_ScriptedMoveToLevelSequence) -> GameplayTask_ScriptedMoveToLevelSequence: ...
    def BeginScriptedMoveToLevelSequence(self, Target: engine.Actor, LevelSequenceActor: gbx_level_sequence.GbxLevelSequenceActor, bStartSequence: bool, OptionalStance: gbx_game_system_core.StanceDataProvider, ReturnValue: GameplayTask_ScriptedMoveToLevelSequence) -> GameplayTask_ScriptedMoveToLevelSequence: ...


class GameplayTask_ScriptedRoute(GameplayTask_ScriptedAction):
    AINode: engine.Actor
    StanceProvider: gbx_game_system_core.StanceDataProvider
    def TaskScriptedMoveDelegate__DelegateSignature(self): ...
    def BeginScriptedRoute2(self, Target: engine.Actor, FirstAINode: engine.Actor, SuccessRule: EScriptedActionRule, FailRule: EScriptedActionRule, bAddSpawned: bool, OptionalStance: gbx_game_system_core.StanceDataProvider, ReturnValue: GameplayTask_ScriptedRoute) -> GameplayTask_ScriptedRoute: ...
    def BeginScriptedRoute(self, User: engine.Actor, FirstAINode: engine.Actor, OptionalStance: gbx_game_system_core.StanceDataProvider, ReturnValue: GameplayTask_ScriptedRoute) -> GameplayTask_ScriptedRoute: ...


class GameplayTask_SmartAction(GameplayTask_ScriptedAction):
    Action: SmartActionInfoContext
    def UnreserveCallback(self, User: engine.Actor, SmartObject: engine.Actor, ActionTag: gameplay_tags.GameplayTag): ...
    def SuccessCallback(self, User: engine.Actor, SmartObject: engine.Actor, ActionTag: gameplay_tags.GameplayTag): ...
    def ReserveCallback(self, User: engine.Actor, SmartObject: engine.Actor, ActionTag: gameplay_tags.GameplayTag): ...
    def InterruptCallback(self, User: engine.Actor, SmartObject: engine.Actor, ActionTag: gameplay_tags.GameplayTag): ...
    def EndSmartAction(self, User: engine.Actor): ...
    def BeginSmartAction(self, User: engine.Actor, SmartObject: engine.Actor, ActionTag: gameplay_tags.GameplayTag, ReturnValue: GameplayTask_SmartAction) -> GameplayTask_SmartAction: ...
    def BeginCallback(self, User: engine.Actor, SmartObject: engine.Actor, ActionTag: gameplay_tags.GameplayTag): ...
    def AITaskEvent__DelegateSignature(self): ...


class GbxAction_CoverHitReaction(gbx_game_system_core.GbxAction_SimpleAnim):
    Styles: unreal.WrappedArray[CoverHitReactionItem]
    BlendInTime: float
    BlendOutTime: float



class GbxAction_CoverTransition(gbx_game_system_core.GbxAction): ...


class GbxAction_Navigation(gbx_game_system_core.GbxAction_SimpleAnim):
    bMaintainRootVelocity: bool
    def K2_GetExitLocation(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def K2_GetEntryLocation(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...


class GbxAction_NavAnim(GbxAction_Navigation):
    EntryTime: float
    BlendInTime: float
    BlendOutTime: float
    AnimSlot: str
    NavAnimations: gbx_game_system_core.AnimMeshList
    bLerpLocation: bool
    bLerpRotation: bool
    bUseStretchy: bool
    StretchBonesSettings: gbx_game_system_core.StretchBonesSettings
    NavAnim: engine.AnimSequenceBase
    NavAnimation: gbx_game_system_core.AnimActionDef



class GbxAction_NavJump(GbxAction_Navigation):
    StretchBonesSettings: gbx_game_system_core.StretchBonesSettings
    RotationTime: float
    bCancelRotationOnActionStop: bool
    bApplyRotationOnStart: bool
    BlendInTime: float
    BlendOutTime: float
    AnimSlot: str
    JumpEnterAnims: gbx_game_system_core.AnimMeshList
    JumpExitAnims: gbx_game_system_core.AnimMeshList
    JumpIdleAnims: gbx_game_system_core.AnimMeshList
    RotationDirective: ENavJumpRotation
    bLockRotation: bool
    DisablePhysicsStage: ENavJumpStage
    EnablePhysicsStage: ENavJumpStage
    ArcSpeed: float
    ArcAnglePercent: float
    MaxPrediction: float
    ArcTimeScale: float
    bLimitHitReactions: bool
    JumpEnter: engine.AnimSequenceBase
    JumpExit: engine.AnimSequenceBase
    JumpIdle: engine.AnimSequenceBase
    JumpEnterAnim: gbx_game_system_core.AnimActionDef
    JumpExitAnim: gbx_game_system_core.AnimActionDef
    JumpIdleAnim: gbx_game_system_core.AnimActionDef
    def OnIdle(self, Actor: engine.Actor): ...
    def OnExit(self, Actor: engine.Actor): ...


class GbxAction_NavHomingJump(GbxAction_NavJump):
    MaxHomingDistance: float



class GbxAction_NavLerp(GbxAction_Navigation):
    bWaitForDistance: bool
    MaxHorizontalDistance: float
    MaxVerticalDistance: float
    bWaitForVelocity: bool
    MaxVelocity: float
    bCallAlmostDone: bool
    AlmostedDoneTime: float
    bSpecifyLerpTime: bool
    LerpTime: float
    bVisible: bool
    def OnAlmostDone(self, Actor: engine.Actor): ...


class GbxAIBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def SetPerceivableToAllAI(self, Actor: engine.Actor, bPerceivable: bool): ...
    def SetAIPathFindingData(self, InActor: engine.Actor, PathFindingData: gbx_nav.HavokPathFindingData): ...
    def SetAINavAreaData(self, InActor: engine.Actor, NavAreaData: gbx_nav.GbxNavAreaData): ...
    def ResetTeamForAllAIChildren(self, Actor: engine.Actor): ...
    def IsActorThreatened(self, InActor: engine.Actor, ReturnValue: bool) -> bool: ...
    def GetValueAsActorAndLocation(self, Blackboard: aimodule.BlackboardComponent, Key: aimodule.BlackboardKeySelector, Actor: engine.Actor, Location: core_uobject.Vector, ReturnValue: bool) -> bool: ...
    def GetBlackboardValueAsActorAndLocation(self, BTNode: aimodule.BTNode, Key: aimodule.BlackboardKeySelector, Actor: engine.Actor, Location: core_uobject.Vector, ReturnValue: bool) -> bool: ...
    def AIScriptedUseWeapon(self, Actor: engine.Actor, bUseWeapon: bool): ...
    def AIScriptedAction(self, Actor: engine.Actor, Action: unreal.UClass): ...
    def AIIsWithinTerritory(self, AIActor: engine.Actor, Zone: gbx_game_system_core.ETerritoryType, ReturnValue: bool) -> bool: ...


class GbxAIController(aimodule.AIController):
    GbxCharacter: gbx_game_system_core.GbxCharacter
    SpawnLocation: core_uobject.Vector
    MovementComponent: gbx_game_system_core.GbxCharacterMovementComponent
    TargetingComponent: gbx_game_system_core.TargetingComponent
    TargetableComponent: gbx_game_system_core.TargetableComponent
    TeamComponent: gbx_game_system_core.TeamComponent
    AIActionComponent: AIActionComponent
    DefaultTerritory: gbx_game_system_core.TerritoryComponent
    CurrentTerritory: gbx_game_system_core.TerritoryComponent
    SpawnerComponent: GbxSpawnerComponent
    GbxNavComponent: gbx_nav.GbxNavComponent
    AIUseComponent: AIUseComponent
    WeaponUserComponents: unreal.WrappedArray[AIWeaponUserComponent]
    GbxActionComponent: gbx_game_system_core.GbxActionComponent
    ChildActors: unreal.WrappedArray[engine.Actor]
    LevelSequencePlayerController: gbx_level_sequence.GbxLevelSequencePlayer
    def SetTerritory(self, Territory: gbx_game_system_core.TerritoryComponent): ...
    def SetTeam(self, Team: gbx_game_system_core.Team): ...
    def SetObstacleAvoidanceLock(self, bDisable: bool, Reason: str): ...
    def ResetTerritoryToDefault(self): ...
    def OnMyWeaponHitSomething(self, HitActor: engine.Actor, HitLocation: core_uobject.Vector): ...
    def GetWeaponUserComponent(self, ReturnValue: AIWeaponUserComponent) -> AIWeaponUserComponent: ...
    def GetUseComponent(self, ReturnValue: AIUseComponent) -> AIUseComponent: ...
    def GetTerritory(self, ReturnValue: gbx_game_system_core.TerritoryComponent) -> gbx_game_system_core.TerritoryComponent: ...
    def GetTeamComponent(self, ReturnValue: gbx_game_system_core.TeamComponent) -> gbx_game_system_core.TeamComponent: ...
    def GetTeam(self, ReturnValue: gbx_game_system_core.Team) -> gbx_game_system_core.Team: ...
    def GetTargetingComponent(self, ReturnValue: gbx_game_system_core.TargetingComponent) -> gbx_game_system_core.TargetingComponent: ...
    def GetTargetableComponent(self, ReturnValue: gbx_game_system_core.TargetableComponent) -> gbx_game_system_core.TargetableComponent: ...
    def GetSpawnerComponent(self, ReturnValue: gbx_spawn.SpawnerComponent) -> gbx_spawn.SpawnerComponent: ...
    def GetSpawner(self, ReturnValue: gbx_spawn.Spawner) -> gbx_spawn.Spawner: ...
    def GetPerceptionComponent(self, ReturnValue: aimodule.AIPerceptionComponent) -> aimodule.AIPerceptionComponent: ...
    def GetNumChildActors(self, ReturnValue: int) -> int: ...
    def GetNavComponent(self, ReturnValue: gbx_nav.GbxNavComponent) -> gbx_nav.GbxNavComponent: ...
    def GetMovementComponent(self, ReturnValue: gbx_game_system_core.GbxCharacterMovementComponent) -> gbx_game_system_core.GbxCharacterMovementComponent: ...
    def GetGroupState(self, ReturnValue: AIGroupState) -> AIGroupState: ...
    def GetGbxCharacter(self, ReturnValue: gbx_game_system_core.GbxCharacter) -> gbx_game_system_core.GbxCharacter: ...
    def GetGbxActionComponent(self, ReturnValue: gbx_game_system_core.GbxActionComponent) -> gbx_game_system_core.GbxActionComponent: ...
    def GetChildActors(self, ReturnValue: unreal.WrappedArray[engine.Actor]) -> unreal.WrappedArray[engine.Actor]: ...
    def GetBlackboardComponent(self, ReturnValue: aimodule.BlackboardComponent) -> aimodule.BlackboardComponent: ...
    def GetBlackboardAsset(self, ReturnValue: aimodule.BlackboardData) -> aimodule.BlackboardData: ...
    def GetAIGroupSize(self, ReturnValue: int) -> int: ...
    def GetAIGroupList(self, AIGroupList: unreal.WrappedArray[engine.Actor], bIncludeSelf: bool, InRadius: float): ...
    def GetAIActionComponent(self, ReturnValue: AIActionComponent) -> AIActionComponent: ...
    def ChildDestroyed(self, DestroyedActor: engine.Actor): ...
    def CheckPauseWhileFalling(self, TheCharacter: engine.Character, PrevMovementMode: int, PreviousCustomMode: int): ...
    def AddChildActors(self, NewChildren: unreal.WrappedArray[engine.Actor]): ...
    def AddChildActor(self, NewChild: engine.Actor): ...


class GbxAINavSystem(gbx_nav.GbxNavSystem): ...


class GbxAISystem(gbx_game_system_core.GbxAISystemBase):
    AIActionManager: AIActionManager
    PlayerAIGroupState: AIGroupState



class GbxAnimStateManager_Cover(engine.GbxAnimStateManager):
    Type: ECoverUserAnimState
    Style: CoverStyleData
    Views: unreal.WrappedArray[CoverViewData]
    TransitionTable: GbxCoverTransitionTable
    CoverUser: CoverUserComponent
    GbxCharAnimInstance: gbx_game_system_core.GbxCharacterAnimInstance
    GbxCharMoveComponent: gbx_game_system_core.GbxCharacterMovementComponent
    AnimSequence: engine.AnimSequence
    def Owner_PostBeginPlay(self): ...


class GbxBehaviorTreeComponent(aimodule.BehaviorTreeComponent): ...


class GbxCondition_AI_IsInRange(gbx_runtime.GbxCondition):
    Target: gbx_game_system_core.GbxBlackboardKeySelector
    Range: gbx_game_system_core.GbxParam
    bInvertRange: bool



class GbxCondition_AI_IsMoving(gbx_runtime.GbxCondition):
    SpeedThreshold: float



class GbxCondition_AIHasNearbyAllies(gbx_runtime.GbxCondition):
    AllyCount: gbx_game_system_core.GbxParam
    Distance: gbx_game_system_core.GbxParam
    bUseDistance: bool



class GbxCondition_BlackboardKey(gbx_runtime.GbxCondition):
    Key: gbx_game_system_core.GbxBlackboardKeySelector
    bInvertResult: bool



class GbxCondition_CanFidgetNow(gbx_runtime.GbxCondition): ...


class GbxCondition_HasEnemyTarget(gbx_runtime.GbxCondition): ...


class GbxCondition_HasFriendlyTarget(gbx_runtime.GbxCondition): ...


class GbxCondition_HasPlayerTarget(gbx_runtime.GbxCondition): ...


class GbxCondition_HasTargetsInRange(gbx_runtime.GbxCondition):
    Range: gbx_game_system_core.GbxParam
    NumTargets: gbx_game_system_core.GbxParam



class GbxCondition_IsActorThreatened(gbx_runtime.GbxCondition): ...


class GbxCondition_IsAttachedToOtherActor(gbx_runtime.GbxCondition): ...


class GbxCondition_IsCloaked(gbx_runtime.GbxCondition): ...


class GbxCondition_IsInCover(gbx_runtime.GbxCondition): ...


class GbxCondition_IsInStance(gbx_runtime.GbxCondition):
    StanceToMatch: gbx_game_system_core.StanceType
    OptionalSpeedThreshold: float



class GbxEqsTestingPawn(aimodule.EQSTestingPawn):
    GbxCharacterMovement: gbx_game_system_core.GbxCharacterMovementComponent
    TargetableComponent: gbx_game_system_core.TargetableComponent
    DamageComponent: gbx_game_system_core.DamageComponent
    DamageCauserComponent: gbx_game_system_core.DamageCauserComponent
    GameplayTagContainerComponent: gbx_game_system_core.GameplayTagContainerComponent
    BaseAimHeight: float
    AimHeightFromGround: float



class SmartObject(engine.Actor):
    SmartObjectComponent: SmartObjectComponent
    GbxActionComponent: gbx_game_system_core.GbxActionComponent
    def GetSmartObjectComponent(self, ReturnValue: SmartObjectComponent) -> SmartObjectComponent: ...
    def GetGbxActionComponent(self, ReturnValue: gbx_game_system_core.GbxActionComponent) -> gbx_game_system_core.GbxActionComponent: ...


class GbxSmartObject(SmartObject): ...


class GbxSpawner(gbx_spawn.Spawner):
    GbxSpawnerComponent: GbxSpawnerComponent
    SpawnNodeComponent: SpawnNodeComponent
    BalanceStateComponent: gbx_game_system_core.BalanceStateComponent
    GameplayTasksComponent: gameplay_tasks.GameplayTasksComponent
    def GetGameplayTasksComponent(self, ReturnValue: gameplay_tasks.GameplayTasksComponent) -> gameplay_tasks.GameplayTasksComponent: ...
    def GetAINodeComponent(self, ReturnValue: AINodeComponent) -> AINodeComponent: ...
    def GetAIGroupState(self, ReturnValue: AIGroupState) -> AIGroupState: ...
    def DEPRECATED_IsThreatened(self, ReturnValue: bool) -> bool: ...


class GbxSpawnerComponent(gbx_spawn.SpawnerComponent):
    GbxSpawner: GbxSpawner
    GroupGbxSpawner: GbxSpawner
    AdditionalGameplayTags: gameplay_tags.GameplayTagContainer



class GbxSpawnPoint(gbx_spawn.SpawnPoint):
    SpawnNodeComponent: SpawnNodeComponent
    def HasNavNearSpawnPointFor(self, SpawnPointComp: gbx_spawn.SpawnPointComponent, SpawnOptions: gbx_spawn.SpawnOptionData, ReturnValue: bool) -> bool: ...


class LookAtPoint(engine.Actor):
    LookAtPointComponent: LookAtPointComponent



class LookAtPointComponent(engine.PrimitiveComponent):
    LookAtPointTag: LookAtPointTag
    bEnabled: bool
    bSearchDataOverride: bool
    SearchHeightOverride: float
    SearchRadiusOverride: float
    bUsageTimeOverride: bool
    UsageTimeOverride: gbx_game_system_core.GbxParam
    bUserCooldownTimeOverride: bool
    UserCooldownTimeOverride: gbx_game_system_core.GbxParam
    UserList: unreal.WrappedArray[SmartObjectUseRequest]



class LookAtPointTag(gbx_runtime.GbxDataAsset):
    LookAtPointType: ELookAtPointType
    FacingStyle: gbx_game_system_core.EFacingChannel
    ActionType: gameplay_tags.GameplayTag
    SearchHeight: float
    SearchRadius: float
    UseChance: gbx_game_system_core.GbxParam
    UseCondition: gbx_runtime.GbxCondition
    bGetInCloser: bool
    UseRadius: float
    UsageTime: gbx_game_system_core.GbxParam
    UserCooldownTime: gbx_game_system_core.GbxParam
    bMaxUsers: bool
    MaxUsers: int



class Perch(engine.Actor):
    PerchComponent: PerchComponent



class PerchComponent(engine.PrimitiveComponent):
    PerchTag: PerchTag
    bEnabled: bool
    SearchRadius: float
    SearchHeight: float
    UseRadius: float
    bUsageTimeOverride: bool
    UsageTimeOverride: gbx_game_system_core.GbxParam
    bCooldownTimeOverride: bool
    CooldownTimeOverride: gbx_game_system_core.GbxParam
    bUserCooldownTimeOverride: bool
    UserCooldownTimeOverride: gbx_game_system_core.GbxParam
    Claimant: SmartObjectUseRequest
    CooldownTime: float



class PerchTag(gbx_runtime.GbxDataAsset):
    PerchType: PerchType
    ActionType: gameplay_tags.GameplayTag
    UsageTime: gbx_game_system_core.GbxParam
    CooldownTime: gbx_game_system_core.GbxParam
    UserCooldownTime: gbx_game_system_core.GbxParam



class PerchType(gbx_runtime.GbxDataAsset): ...


class ScriptedBehaviorTreeLibrary(engine.BlueprintFunctionLibrary):

    def PerformScriptedAbort(self, Target: engine.Actor, bStopImmediately: bool): ...
    def BeginScriptedWait(self, Target: engine.Actor, OptionalStance: gbx_game_system_core.StanceDataProvider): ...
    def BeginScriptedLook(self, Target: engine.Actor, LookAtActor: engine.Actor, bAimAtActor: bool, bFireWeaponAtActor: bool, OptionalStance: gbx_game_system_core.StanceDataProvider): ...


class SmartObjectAction(gbx_runtime.GbxDataAsset):
    bPassiveAction: bool
    bCombatAction: bool
    UseChance: gbx_game_system_core.GbxParam
    UseCondition: gbx_runtime.GbxCondition
    bUsageTime: bool
    UsageTime: gbx_game_system_core.GbxParam
    bMaxUsers: bool
    MaxUsers: int
    ActionCooldownTime: gbx_game_system_core.GbxParam
    LocalUserCooldownTime: gbx_game_system_core.GbxParam
    GlobalUserCooldownTime: gbx_game_system_core.GbxParam



class AIResource_SmartObject(gameplay_tasks.GameplayTaskResource): ...


class SmartObjectInterface(core_uobject.Interface): ...


class SmartObjectBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def UseSmartObject(self, User: engine.Actor, SmartObject: engine.Actor, ActionTag: gameplay_tags.GameplayTag, bAbortExisting: bool, bUntilInterrupted: bool, ReturnValue: bool) -> bool: ...
    def AbortSmartObjectUse(self, User: engine.Actor): ...


class SmartObjectComponent(engine.ActorComponent):
    bUseInRoutes: bool
    LookAtRule: ESmartObjectLookAtRule
    LookAtSocket: str
    UseLookAtQuery: gbx_game_system_core.GbxParam
    LookAtQueryDuration: gbx_game_system_core.GbxParam
    LookAtQueryForgetDuration: gbx_game_system_core.GbxParam
    LookAtQueryPeriod: gbx_game_system_core.GbxParam
    LookAtQuery: gbx_game_system_core.EnvQueryParams
    Actions: unreal.WrappedArray[SmartObjectActionState]
    UseSlots: unreal.WrappedArray[AIUseSlotComponent]
    def UnreserveEventSignature(self, User: engine.Pawn): ...
    def ToggleActionSet(self, ActionSet: SmartObjectActionSet): ...
    def SuccessEventSignature(self, User: engine.Pawn): ...
    def ReserveEventSignature(self, User: engine.Pawn): ...
    def OnActionEnded(self, EndState: gbx_game_system_core.EGbxActionEndState, ActionName: gameplay_tags.GameplayTag, User: engine.Controller): ...
    def InterruptEventSignature(self, User: engine.Pawn): ...
    def GetAvailableSocketNames(self, Array: unreal.WrappedArray[str]): ...
    def GetActionUsers(self, ActionTag: gameplay_tags.GameplayTag, OutUsers: unreal.WrappedArray[engine.Pawn]): ...
    def EnableAllActions(self): ...
    def EnableAction(self, ActionTag: gameplay_tags.GameplayTag): ...
    def DisableAllActions(self): ...
    def DisableAction(self, ActionTag: gameplay_tags.GameplayTag): ...
    def BeginEventSignature(self, User: engine.Pawn): ...


class SmartObjectPreviewComponent(gbx_game_system_core.PreviewComponent):
    PreviewList: unreal.WrappedArray[SmartObjectPreviewState]
    ActiveAISlotIdx: int
    PreviewAction: unreal.UClass
    bAutoCycle: bool
    CycleActor: gbx_runtime.GbxTriggerProperty
    bShowAction: bool
    bRepeatAction: bool
    ReplayAction: gbx_runtime.GbxTriggerProperty
    ActionComponent: gbx_game_system_core.GbxActionComponent
    def OnReplayAction(self): ...
    def OnCycleActor(self, Direction: gbx_game_system_core.ECycleDirection): ...


class SmartObjectUser(core_uobject.Interface): ...


class SpawnBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def SetSpawnOptions(self, SpawnerActor: engine.Actor, SpawnOptions: gbx_spawn.SpawnOptionData): ...
    def GenerateSpawnerByRadius(self, Instigator: engine.Actor, Style: gbx_spawn.SpawnerStyle, Radius: float, MinRequiredAttitude: int, ReturnValue: gbx_spawn.Spawner) -> gbx_spawn.Spawner: ...
    def GenerateSpawnerByOwningSpawner(self, Instigator: engine.Actor, Style: gbx_spawn.SpawnerStyle, ReturnValue: gbx_spawn.Spawner) -> gbx_spawn.Spawner: ...


class SpawnNodeComponent(AINodeComponent):
    InitialPathAction: EInitialPathAction



class Territory(engine.Info):
    TerritoryComponent: gbx_game_system_core.TerritoryComponent
    def GetTerritoryComponent(self, ReturnValue: gbx_game_system_core.TerritoryComponent) -> gbx_game_system_core.TerritoryComponent: ...


class AIActionBlueprintContext:
    Controller: GbxAIController



class SmartActionInfoContext:
    SmartObject: engine.Actor
    UseInfo: SmartActionUseInfo
    ContextLoc: core_uobject.Vector



class SmartActionUseInfo:
    ActionTag: gameplay_tags.GameplayTag
    bInterrupting: bool
    UseDuration: float
    CooldownTime: float
    bPassiveAction: bool
    bCombatAction: bool



class AIActionSettings_Plan:
    PlansAlwaysAvailableToMe: unreal.WrappedArray[AIPlanData]
    RoleTags: unreal.WrappedArray[gameplay_tags.GameplayTag]



class AIActionExecutionSettings:
    bEnabled: bool
    SuccessTransition: EAIActionResultTransition
    FailureTransition: EAIActionResultTransition
    bAlwaysReportSuccess: bool
    CheckCanStartPeriod: float



class AIActionInstance:
    ScriptedGameplayTask: gameplay_tasks.GameplayTask
    Action: AIAction



class AIAspectExecutionSettings:
    bCanPreventActionFromStarting: bool
    bCanCauseActionToSucceed: bool
    bCanForceActionToSucceed: bool
    bCanCauseActionToFail: bool
    bMustFinish: bool



class AIAspectSettings_ActorCollision:
    Target: gbx_game_system_core.GbxBlackboardKeySelector
    OnCollision: EAIActionResultDirective



class AIAspectSettings_AIGroupCondition:
    FullfillmentQuantity: int
    bPartialFullfillment: bool



class AIAspectSettings_BlackboardKey:
    Key: gbx_game_system_core.GbxBlackboardKeySelector
    bInvertResult: bool
    WhenConditionFails: EAIActionResultDirective
    OnBecomeFalse: EAIActionResult
    bAbortOnChange: bool
    bRefreshImmediatelyOnChange: bool



class AIAspectSettings_Charge:
    ChargeData: gbx_game_system_core.AIChargeData
    Target: gbx_game_system_core.GbxBlackboardKeySelector



class AIAspectSettings_UseSmartObject:
    SmartAction: gbx_game_system_core.GbxBlackboardKeySelector
    bAbortExisting: bool
    bUntilInterrupted: bool
    bCanBeInterrupted: bool
    SmartObjectQuery: gbx_game_system_core.EnvQueryParams
    bUseQuery: bool
    QuerySettings: AIAspectSettings_EnvQuery



class AIAspectSettings_EnvQuery:
    Query: gbx_game_system_core.EnvQueryParams
    QueryBlackboardKey: gbx_game_system_core.GbxBlackboardKeySelector
    bRefreshAITreeOnQuerySuccess: bool
    bForceRequeryOnSuccess: bool
    bClearQueryOnSuccess: bool
    Options: gbx_game_system_core.GbxQueryOptions
    Preset: int
    bUsePreset: bool
    QueryPeriod: gbx_game_system_core.GbxParam
    bQueryContinuously: bool
    bUpdateValueWhileRunning: bool
    bKeepValidValues: bool
    bCanUseSelf: bool
    UseSelfDistance: float
    bSucceedIfHasValue: bool
    bMigrated: bool



class AIAspectSettings_Condition:
    CanStartCondition: AIAspectSettings_ConditionData
    SucceedCondition: AIAspectSettings_ConditionData
    FailCondition: AIAspectSettings_ConditionData
    CanAbortCondition: AIAspectSettings_ConditionData
    bUseCanStartCondition: bool
    bUseSucceedCondition: bool
    bUseFailCondition: bool
    bUseCanAbortCondition: bool



class AIAspectSettings_ConditionData:
    Condition: gbx_game_system_core.GbxParam
    ContextResolver: gbx_game_system_core.AttributeContextResolver
    bInvertCondition: bool



class AIAspectSettings_Cooldown:
    SucceedTimer: gbx_game_system_core.GbxParam
    bUseSucceedTimer: bool
    FailTimer: gbx_game_system_core.GbxParam
    bUseFailTimer: bool
    AbortTimer: gbx_game_system_core.GbxParam
    bUseAbortTimer: bool
    InitialTimer: gbx_game_system_core.GbxParam
    bUseInitialTimer: bool



class AIAspectSettings_Crouch:
    CanCrouchWhileIdle: gbx_game_system_core.GbxParam
    bUseCanCrouchWhileMoving: bool
    CanCrouchWhileMoving: gbx_game_system_core.GbxParam



class AIAspectSettings_DropshipSpawn:
    StartAction: unreal.UClass
    StopAction: unreal.UClass



class AIAspectSettings_FindClosestPlayer:
    BlackboardKey: gbx_game_system_core.GbxBlackboardKeySelector
    bOnlyRunIfKeyIsValid: bool
    bClearKeyOnStop: bool
    UpdatePeriod: float
    bIsInternal: bool



class AIAspectSettings_FlyToNavMesh:
    GroundSearchDistance: float
    LookAheadDistance: float
    FlySearchDistance: float
    UpdatePeriod: float



class AIAspectSettings_Follow:
    FollowActorKey: gbx_game_system_core.GbxBlackboardKeySelector
    TargetDistance: gbx_runtime.NumericRange
    MaxSpeedScale: float
    MinSpeedScale: float
    GoalUpdatePeriod: float
    InvalidWaitPeriod: float
    TeleportWaitPeriod: float
    bAllowTeleport: bool
    TeleportDistance: float
    bTeleportWhenFar: bool
    bContinueWhileClose: bool



class AIAspectSettings_GbxAction:
    ActionType: unreal.UClass
    bUseActionType: bool
    ActionKey: gameplay_tags.GameplayTag
    bUseActionKey: bool
    ActionBlackboardKey: gbx_game_system_core.GbxBlackboardKeySelector
    bUseActionBlackboardKey: bool
    Count: gbx_game_system_core.GbxParam
    CanBeInterrupted: gbx_game_system_core.GbxParam
    CanBeInterruptedOnFailure: gbx_game_system_core.GbxParam
    PlayRate: gbx_game_system_core.GbxParam



class AIAspectSettings_GroupLocation:
    GroupLocationKey: gbx_game_system_core.GbxBlackboardKeySelector
    GroupDistance: gbx_game_system_core.GbxParam
    UpdatePeriod: float
    bUpdateWhileActive: bool



class AIAspectSettings_IntCompare:
    Key: gbx_game_system_core.GbxBlackboardKeySelector
    WhenConditionFails: EAIActionResultDirective
    CompareMethod: ECompareMethod
    CompareAgainst: gbx_game_system_core.GbxParam
    bAbortOnChange: bool
    bRefreshImmediatelyOnChange: bool



class AIAspectSettings_IsInRange:
    Target: gbx_game_system_core.GbxBlackboardKeySelector
    DistanceTest: EIsInRangeAspectDistanceTest
    CanRunRange: AIAspectSettings_IsInRangeData
    AdvancedRanges: AIAspectIsInRangeAdvancedData
    bUseAdvancedRanges: bool



class AIAspectIsInRangeAdvancedData:
    CanStartRange: AIAspectSettings_IsInRangeData
    SucceedRange: AIAspectSettings_IsInRangeData
    FailRange: AIAspectSettings_IsInRangeData
    bUseCanStartRange: bool
    bUseSucceedRange: bool
    bUseFailRange: bool



class AIAspectSettings_IsInRangeData:
    Range: gbx_game_system_core.GbxParam
    bInvertRange: bool



class AIAspectSettings_IsInTerritory:
    GoalKey: gbx_game_system_core.GbxBlackboardKeySelector
    TerritoryArea: gbx_game_system_core.ETerritoryType
    TimeThreshold: float



class AIAspectSettings_Land:
    GroundSearchDistance: float
    FlySearchDistance: float
    UpdatePeriod: float



class AIAspectSettings_LeadRoute:
    LeadActorKey: gbx_game_system_core.GbxBlackboardKeySelector
    DestinationNodeKey: gbx_game_system_core.GbxBlackboardKeySelector
    SegmentDistance: float
    MaxWanderingOffset: float
    ArrivalDistance: float
    TargetRouteDistance: gbx_runtime.NumericRange
    SpeedScaleRange: gbx_runtime.NumericRange
    RouteOffsetFromTarget: float
    TeleportDist: float
    bAllowBackwards: bool
    bAllowTeleport: bool
    FindNavRadius: float



class AIAspectSettings_Leap:
    Action: unreal.UClass
    Target: gbx_game_system_core.GbxBlackboardKeySelector
    LocalOffset: core_uobject.Vector
    TargetOffset: core_uobject.Vector
    TargetSocket: str
    Speed: float
    AnglePercent: float
    MaxPrediction: float
    bDoNavigationTest: bool
    bDoCollisionTest: bool
    bAddTargetRadius: bool
    UseExactLocationDistance: float
    TestPeriod: float
    bCanStartWhileFalling: bool



class AIAspectSettings_Location:
    Target: gbx_game_system_core.GbxBlackboardKeySelector
    TargetChangeTransition: EAIActionResultTransition
    Distance: gbx_game_system_core.GbxParam
    TargetQuery: gbx_game_system_core.EnvQueryParams
    TargetQueryPeriod: gbx_game_system_core.GbxParam
    bUseTargetQuery: bool
    MoveSettings: AIAspectSettings_Move
    bCanMove: bool



class AIAspectSettings_Move:
    PathUpdateThreshold: float
    bStopWhenInPosition: bool
    bAllowStrafe: bool
    bAllowPartialPath: bool
    bRequireDirectPath: bool



class LookAroundRandomlySettings:
    MinAngleChangeEachIterationDeg: float
    MaxAngleChangeEachIterationDeg: float
    MaxTimeSpentEachScan: float



class AIAspectSettings_Loop:
    LoopCondition: gbx_game_system_core.GbxParam
    bUseLoopCondition: bool
    LoopCount: gbx_game_system_core.GbxParam
    bUseLoopCount: bool
    LoopDuration: gbx_game_system_core.GbxParam
    bUseLoopDuration: bool
    bStopImmediately: bool
    bIgnoreFailure: bool



class AIAspectSettings_MoveSpline:
    SplineKey: gbx_game_system_core.GbxBlackboardKeySelector
    OffsetKey: gbx_game_system_core.GbxBlackboardKeySelector
    ReverseKey: gbx_game_system_core.GbxBlackboardKeySelector
    LookDistance: float
    MissNavigationStep: float
    MissNavigationStepDistance: float
    AdditionnalLookDistanceSpeedFactor: float
    SnapToNavigation: float
    bSnapToNavigation: bool
    GoalUpdateDistance: float
    Reach: gbx_nav.EGbxNavGoalReach



class AIAspectSettings_NavFlyOffset:
    CenterKey: gbx_game_system_core.GbxBlackboardKeySelector
    Distance: gbx_game_system_core.GbxParam
    Height: gbx_game_system_core.GbxParam
    SearchRadius: float
    bLimitSearchRadius: bool
    UpdatePeriod: float
    bForward: float



class AIAspectSettings_Navigation:
    ReachedHeight: gbx_game_system_core.GbxParam
    ReachedDistance: gbx_game_system_core.GbxParam
    Advanced: AIAspectSettings_NavigationAdvanced
    bCanMove: bool
    bReachedRequiresDirect: bool
    StrafeType: gbx_nav.EGbxStrafeType
    PathType: gbx_nav.EGbxPathType
    bStopWhenReached: bool
    bCanRunWhenAtGoal: bool
    bUpdateGoalWhileRunning: bool



class AIAspectSettings_NavigationAdvanced:
    bCanMove: bool
    bReachedRequiresDirect: bool
    StrafeType: gbx_nav.EGbxStrafeType
    PathType: gbx_nav.EGbxPathType
    bStopWhenReached: bool
    bCanRunWhenAtGoal: bool
    bUpdateGoalWhileRunning: bool
    Cheats: gbx_nav.EGbxNavGoalCheats
    GoalModifiers: gbx_nav.GbxNavGoalModifiers
    bCanStartWhenGoalIsUncertain: bool
    bMoveEvenIfUnreachable: bool



class AIAspectSettings_Orbit:
    CenterKey: gbx_game_system_core.GbxBlackboardKeySelector
    HeightOffset: gbx_game_system_core.GbxParam
    OrbitRadius: gbx_game_system_core.GbxParam
    OrbitAngle: gbx_game_system_core.GbxParam
    OrbitAngleInterval: gbx_game_system_core.GbxParam
    Direction: EOrbitDirection
    SearchRadius: float
    bRespectCombatTerritory: bool



class AIAspectSettings_Plan:
    PlansAlwaysAvailableToMe: unreal.WrappedArray[AIPlanData]
    RoleTags: unreal.WrappedArray[gameplay_tags.GameplayTag]



class AIAspectSettings_Rotation:
    bCanRotate: bool
    bTrackTargetOverTime: bool
    BodyHeadingOffsetPresets: EAIAspectSettingsDefaults_Rotation_BodyHeadingOffset
    BodyHeadingOffset: float
    PremadeSettings: EAIAspectSettingsDefaults_Rotation
    Body: AIAspectSettings_RotationChannel
    bUseBody: bool
    Aim: AIAspectSettings_RotationChannel
    bUseAim: bool
    Look: AIAspectSettings_RotationChannel
    bUseLook: bool
    bKeepFacingTargetOnStop: bool



class AIAspectSettings_RotationChannel:
    Target: gbx_game_system_core.GbxBlackboardKeySelector
    TargetOffset: core_uobject.Vector
    Angle: gbx_game_system_core.GbxParam
    bUseAngle: bool
    MaxRotateAngle: gbx_game_system_core.GbxParam
    bUseMaxRotateAngle: bool
    ConditionalEnable: gbx_game_system_core.GbxParam
    bUseConditionalEnable: bool



class AIAspectSettings_Route:
    NodeKey: gbx_game_system_core.GbxBlackboardKeySelector
    SegmentDistance: float
    MaxWanderingOffset: float
    ArrivalDistance: float
    PerchCooldown: float
    bPassiveAction: bool
    bCombatAction: bool



class AIAspectSettings_Stance:
    Stance: gbx_game_system_core.StanceDataProvider
    bOverrideBlueprint: bool



class AIAspectSettings_Sweep:
    CenterKey: gbx_game_system_core.GbxBlackboardKeySelector
    HeightOffset: gbx_game_system_core.GbxParam
    SweepRadius: float
    SweepAngle: float
    SweepAngleInterval: float
    Direction: ESweepDirection
    SearchRadius: float



class AIAspectSettings_Swoop:
    CenterKey: gbx_game_system_core.GbxBlackboardKeySelector
    FarDistance: gbx_game_system_core.GbxParam
    FarHeight: gbx_game_system_core.GbxParam
    NearDistance: gbx_game_system_core.GbxParam
    NearHeight: gbx_game_system_core.GbxParam
    PassDistance: gbx_game_system_core.GbxParam
    PassHeight: gbx_game_system_core.GbxParam
    SearchRadius: float
    bLimitSearchRadius: bool
    UpdatePeriod: float



class AIAspectSettings_Teleport:
    GoalKey: gbx_game_system_core.GbxBlackboardKeySelector
    bCloak: bool
    bTraceToGround: bool
    bClearVelocity: bool
    bChangeRotation: bool
    bClearGoalOnStop: bool
    RotationKey: gbx_game_system_core.GbxBlackboardKeySelector
    TravelTime: gbx_game_system_core.GbxParam
    bUseSpeedInsteadOfTime: bool
    TravelSpeed: gbx_game_system_core.GbxParam
    bUpdateGoal: bool



class AIAspectSettings_Ticket:
    bPriority: bool
    bInterruptible: bool
    Value: gbx_game_system_core.GbxParam
    HoldDuration: gbx_game_system_core.GbxParam
    AITicket: AITicketDataAsset
    ActorBlackboardKey: gbx_game_system_core.GbxBlackboardKeySelector
    bOverrideActorBlackboardKey: bool
    bApplyHoldOnSuccess: bool
    bApplyHoldOnFailure: bool
    bApplyHoldOnAbort: bool
    bAcquireTicket: bool



class AIAspectSettings_TimedCondition:
    Condition: AIAspectSettings_ConditionData
    Timer: gbx_game_system_core.GbxParam
    WhenConditionFails: EAIActionResultDirective
    FalseResult: EAIActionResult



class AIAspectSettings_TimeLimit:
    SucceedTime: gbx_game_system_core.GbxParam
    FailTime: gbx_game_system_core.GbxParam
    bUseSucceedTime: bool
    bUseFailTime: bool



class AIAspectSettings_Timer:
    CanStartWarmup: gbx_game_system_core.GbxParam
    bUseCanStartWarmup: bool
    SpawnedWarmup: gbx_game_system_core.GbxParam
    bUseSpawnedWarmup: bool
    CombatStartedWarmup: gbx_game_system_core.GbxParam
    bUseCombatStartedWarmup: bool
    TargetChangedWarmup: gbx_game_system_core.GbxParam
    bUseTargetChangedWarmup: bool
    SucceededCooldown: gbx_game_system_core.GbxParam
    bUseSucceededCooldown: bool
    FailedCooldown: gbx_game_system_core.GbxParam
    bUseFailedCooldown: bool
    AbortedCooldown: gbx_game_system_core.GbxParam
    bUseAbortedCooldown: bool
    SucceedTimeLimit: gbx_game_system_core.GbxParam
    bUseSucceedTimeLimit: bool
    FailTimeLimit: gbx_game_system_core.GbxParam
    bUseFailTimeLimit: bool



class AIAspectSettings_UseCover:
    Target: gbx_game_system_core.GbxBlackboardKeySelector
    Cover: gbx_game_system_core.GbxBlackboardKeySelector
    UseParams: CoverUseParams



class CoverUseParams:
    bMustHaveViewToTarget: bool
    bMustBeHiddenFromThreats: bool
    InCoverExposurePercent: float
    bOverrideIdleTime: bool
    IdleTimeOverride: gbx_game_system_core.GbxParam
    bOverrideFireTime: bool
    FireTimeOverride: gbx_game_system_core.GbxParam



class AIWeaponUseSettings:
    FireConeAngle: float
    bOverrideFireConeAngle: bool
    BurstCountOverride: gbx_game_system_core.GbxParam
    bOverrideBurstCount: bool
    BurstDelayOverride: gbx_game_system_core.GbxParam
    bOverrideBurstDelay: bool
    AccuracyOverride: gbx_game_system_core.GbxParam
    bOverrideAccuracy: bool
    SuppressingFireTime: gbx_game_system_core.GbxParam
    bUseSuppressingFireTime: bool
    DesiredRangeOverride: gbx_runtime.NumericRange
    bOverrideDesiredRange: bool
    MaxWeaponLeadingDistance: float



class AIAspectSettings_Weapon(AIWeaponUseSettings):
    WeaponSlots: unreal.WrappedArray[gbx_game_system_core.GbxWeaponSlotData]
    WeaponUseModeIndex: gbx_game_system_core.GbxParam
    CanUseWeapon: gbx_game_system_core.GbxParam
    CanUseWeaponWhileMoving: gbx_game_system_core.GbxParam
    bUseCanUseWeaponWhileMoving: bool
    bOnlyShootWhenTargetIsKnown: bool



class AIAspectSettings_ZeroRotation:
    Body: AIAspectSettings_ZeroRotationChannel
    bUseBody: bool
    Aim: AIAspectSettings_ZeroRotationChannel
    bUseAim: bool
    Look: AIAspectSettings_ZeroRotationChannel
    bUseLook: bool



class AIAspectSettings_ZeroRotationChannel:
    bZeroPitch: bool
    bZeroYaw: bool
    bZeroRoll: bool



class CloakRepData:
    bCloaked: bool
    bCanPlayActions: bool



class CloakPrimData:
    bWasHidden: bool
    PrimComp: engine.PrimitiveComponent



class CloakCondition:
    Condition: gbx_runtime.GbxCondition
    bCloaked: bool



class AICommunicationManager: ...


class AITicketHandle:
    Ticket: AITicketDataAsset
    AIController: GbxAIController



class AINodeLink:
    Weight: float
    PrevWeight: float
    Actor: engine.Actor
    SmartObjects: unreal.WrappedArray[AINodeSmartObjectData]



class AINodeSmartObjectData:
    Object: engine.Actor
    Distance: float
    Offset: float



class PlanRoleRequirements:
    RoleTag: gameplay_tags.GameplayTag
    MinInstancesOfRole: int
    MaxInstancesOfRole: int
    DistanceToLeaderForParticipation: gbx_game_system_core.GbxParam
    DistanceToLeaderToRemove: gbx_game_system_core.GbxParam
    AdditionalStartCondition: gbx_runtime.GbxCondition
    bAlsoUseStartConditionAsStopCondition: bool
    AdditionalStopCondition: gbx_runtime.GbxCondition
    MemberReplacementStrategy: EPlanMemberReplacement



class AIPlanManager:
    AvailablePlans: unreal.WrappedArray[AIPlanData]
    ActivePlans: unreal.WrappedArray[PlanState]



class RoleCandidates: ...


class PlanState: ...


class PlanRoleMapping: ...


class RoleController: ...


class ProximitySource: ...


class ThreatSource: ...


class ThreatTerritory: ...


class AITicketUseData:
    Value: gbx_game_system_core.GbxParam
    HoldDuration: gbx_game_system_core.GbxParam
    Ticket: AITicketDataAsset



class AITicketManager: ...


class ActionUseState:
    Controller: GbxAIController
    SmartObjectComponent: SmartObjectComponent
    AIUseSlotComponent: AIUseSlotComponent
    UseInfo: SmartActionUseInfo
    State: ESmartObjectTaskState



class ActionCooldownInfo:
    ActorClass: unreal.UClass
    ActionTag: gameplay_tags.GameplayTag
    CooldownTime: float



class BTRandomEntrySettings:
    Name: str
    Weight: gbx_game_system_core.GbxParam
    LoopCountMax: gbx_game_system_core.GbxParam
    bUseLoopCountMax: bool



class BTGbxLoopConditionData:
    Condition: gbx_runtime.GbxCondition
    bInvert: bool



class CoverFaceDirections:
    Low: ECoverFaceDirection
    HighLeft: ECoverFaceDirection
    HighRight: ECoverFaceDirection



class CoverLineOfSightData:
    LocalToWorld: core_uobject.Transform
    WorldToLocal: core_uobject.Matrix
    Sections: unreal.WrappedArray[CoverLineOfSightSectionData]
    Params: CoverLineOfSightParams



class CoverLineOfSightParams:
    NumVerticalSections: int
    NumHorizontalSections: int
    VerticalAngleUp: float
    VerticalAngleDown: float
    HorizontalAngle: float
    MaxDistance: float
    NumBlockSubdivisions: int
    RotationOffset: core_uobject.Rotator



class CoverLineOfSightSectionData:
    Blocks: unreal.WrappedArray[CoverLineOfSightBlockData]



class CoverLineOfSightBlockData:
    Distance: float



class CoverAdjustParams:
    AdjustDistanceDown: float
    bDoDownAdjustment: bool
    AdjustDistanceUp: float
    bDoUpAdjustment: bool
    AdjustDistanceForward: float
    bDoForwardAdjustment: bool
    bEdgeTestLeft: bool
    bEdgeTestRight: bool
    EdgeTestSections: int
    EdgeTestHeightPct: float
    EdgeTestDistancePct: float
    EdgeTestWalkBackDistance: float
    EdgeTestAngleThreshold: int
    BlockTestHitPct: float
    BlockTestDistancePct: float
    BlockTestHorizontalSections: int
    BlockTestVerticalSections: int
    BlockTestAngleThreshold: int



class CoverSlotViewFailData:
    View: CoverViewData
    FailReason: ECoverAdjustFailReason
    FailDescription: str



class CoverSlotViewData:
    View: CoverViewData
    LosData: CoverLineOfSightData



class CoverTransitionData:
    DataTable: engine.DataTable
    AnimSet: engine.GbxAnimSet
    Filters: CoverTransitionFilters



class CoverTransitionFilters:
    Use: unreal.WrappedArray[str]
    Corner: unreal.WrappedArray[str]
    High: unreal.WrappedArray[str]
    Away: unreal.WrappedArray[str]
    Stances: unreal.WrappedArray[CoverTransitionStanceFilter]



class CoverTransitionStanceFilter:
    Filter: str
    Stance: gbx_game_system_core.StanceDataProvider



class CoverTransitionTableRow(gbx_game_system_core.GbxAnimTableRow):
    Angle: gbx_runtime.NumericRange
    Distance: gbx_runtime.NumericRange
    Height: float
    FaceDirection: ECoverFaceDirection
    SlotHeight: ECoverSlotHeight
    CoverStyles: unreal.WrappedArray[CoverStyleData]
    ViewsFrom: unreal.WrappedArray[CoverViewData]
    ViewsTo: unreal.WrappedArray[CoverViewData]
    bCornerTransition: bool
    Stance: gbx_game_system_core.StanceDataProvider
    bAutoFill: bool
    AutoFillAngle: gbx_runtime.NumericRange
    AutoFillDistance: gbx_runtime.NumericRange



class CoverTransitionInput: ...


class CoverClientData:
    Style: CoverStyleData
    Slot: CoverSlotComponent
    DesiredState: ECoverUserState
    TransitionName: str
    bFlanked: bool



class CoverAction:
    Slot: CoverSlotComponent
    Style: CoverStyleData
    Target: engine.Actor
    Params: CoverUseParams



class CoverStyleUserData:
    Style: CoverStyleData
    Weight: gbx_game_system_core.GbxParam
    bOverrideIdleTime: bool
    IdleTimeOverride: gbx_game_system_core.GbxParam
    bOverrideFireTime: bool
    FireTimeOverride: gbx_game_system_core.GbxParam
    TicketData: AITicketUseData
    ForceUseCondition: gbx_runtime.GbxCondition



class CoverWalk: ...


class EQSDynamicPointRange:
    MinPoints: int
    MaxPoints: int
    IdealSpacing: float
    MinSpacing: float



class SmartGridSearchSet:
    SetName: str
    MaxPoints: int
    Center: unreal.UClass
    bOnlyGenerateDensePoints: bool
    InnerRadius: aimodule.AIDataProviderFloatValue
    OuterRadius: aimodule.AIDataProviderFloatValue
    bDefineArc: bool
    ArcDirection: aimodule.EnvDirection
    ArcAngle: aimodule.AIDataProviderFloatValue
    PointSeparationDistanceNormal: float
    PointSeparationDistanceDenseSpots: float
    RadiusApplyDenserSeparation: float
    DenseSpotProvider: unreal.UClass



class ExtendedTraceInfo:
    ReadableName: str
    TestComment: str
    bDoArcTrace: bool
    ArcSpeed: aimodule.AIDataProviderFloatValue
    ArcAnglePercent: aimodule.AIDataProviderFloatValue
    NumSegments: int
    TraceData: aimodule.EnvTraceData
    Context: unreal.UClass
    MultipleContextRequirement: EUberTraceMultiTraceRequirement
    MaxScoreIfFails: float
    MinScoreIfSucceeds: float
    bStopIfSucceeds: bool
    bStopIfFails: bool
    PassTestIfTrue: gbx_game_system_core.GbxParam
    FailTestIfTrue: gbx_game_system_core.GbxParam



class ActionState_CoverHitReaction(gbx_game_system_core.ActionState_SimpleAnim): ...


class CoverHitReactionItem:
    Anims: gbx_game_system_core.AnimMeshList
    Styles: unreal.WrappedArray[CoverStyleData]



class ActionState_CoverTransition(gbx_game_system_core.ActionState_Base): ...


class ActionState_Navigation(gbx_game_system_core.ActionState_SimpleAnim): ...


class ActionState_NavAnim(ActionState_Navigation): ...


class ActionState_NavJump(ActionState_Navigation): ...


class ActionState_NavHomingJump(ActionState_NavJump): ...


class ReplicatedJumpParams:
    bStarted: bool
    EndLoc: core_uobject.Vector
    TargetVel: core_uobject.Vector



class ActionState_NavLerp(ActionState_Navigation): ...


class SmartObjectActionState:
    bEnabled: bool
    ActionTag: gameplay_tags.GameplayTag
    ActionDefinition: SmartObjectAction
    DebugColor: core_uobject.Color
    CooldownTime: float
    Users: unreal.WrappedArray[SmartActionUser]



class SmartActionUser:
    Controller: engine.Controller
    UseDuration: float
    State: ESmartObjectTaskState



class RouteSection:
    Start: engine.Actor
    End: engine.Actor



class SmartObjectPreviewState(gbx_game_system_core.PreviewState):
    AIUseSlotComponent: AIUseSlotComponent
    PreviewFactories: unreal.WrappedArray[gbx_spawn.SpawnFactory]



class SmartAction:
    SmartObject: engine.Actor
    ActionTag: gameplay_tags.GameplayTag



class SmartObjectUseRequest: ...


class SmartObjectActionSet:
    Actions: gameplay_tags.GameplayTagContainer



class Default__AIActionBlueprintGeneratedClass: ...


class EAIActionResult(enum.Enum):
    Succeeded = 0
    Failed = 1
    Aborted = 2


class ECoverUserAnimState(enum.Enum):
    Idle = 0
    Exit = 1
    FireEnter = 2
    ViewSwitch = 3


class EScriptedActionRule(enum.Enum):
    All = 0
    EScriptedActionRule_MAX = 1


class ESmartActionResult(enum.Enum):
    Interrupt = 0
    Unreserve = 1


class EMeleeRotationOption(enum.Enum):
    AlignToTarget = 0
    FollowTarget = 1


class EAIActionSequenceCanStartCheck(enum.Enum):
    EachChild = 0
    EAIActionSequenceCanStartCheck_MAX = 1


class EAIActionCreationMethod(enum.Enum):
    EAIActionCreationMethod_MAX = 0
    Composition = 1
    PropertyPanel = 2


class EAIActionResultTransition(enum.Enum):
    Restart = 0
    Continue = 1


class EAIActionResultDirective(enum.Enum):
    Succeed = 0
    Fail = 1


class EAIActionExecutionStage(enum.Enum):
    Stopping = 0
    Running = 1
    CleaningUp = 2


class EAIActionState(enum.Enum):
    Starting = 0
    EAIActionState_MAX = 1
    Running = 2


class EAIActionLayer(enum.Enum):
    Script = 0
    Count = 1


class EAIGroupConditionType(enum.Enum):
    EAIGroupConditionType_MAX = 0
    SomeFalse = 1
    AllTrue = 2


class ECircleDirection(enum.Enum):
    Right = 0
    Random = 1


class EGbxQueryPreset(enum.Enum):
    TryCurrentLocation = 0
    OnlyCurrentLocation = 1
    QueryOnStart = 2


class ECompareMethod(enum.Enum):
    NotEquals = 0
    Smaller = 1
    Greater = 2


class EIsInRangeAspectDistanceTest(enum.Enum):
    Count = 0
    Horizontal = 1
    Vertical = 2


class EOrbitDirection(enum.Enum):
    Right = 0
    Random = 1


class EAIAspectSettingsDefaults_Rotation(enum.Enum):
    None_ = 0
    NoBodyRotationAllowed = 1
    AimOffsetsOnly = 2


class EAIAspectSettingsDefaults_Rotation_BodyHeadingOffset(enum.Enum):
    Left = 0
    Back = 1
    Custom = 2


class ESweepDirection(enum.Enum):
    Right = 0
    Random = 1


class ECloakAction(enum.Enum):
    OnStop = 0
    ECloakAction_MAX = 1


class EPlanMemberReplacement(enum.Enum):
    ReplaceMemberIfKilled = 0
    DoNotReplaceAndKeepGoing = 1


class EPlanValidityCode(enum.Enum):
    NoPlanData = 0
    MissingRoleTag = 1
    PlanIsValid = 2
    InsufficientCandidates = 3


class EPlanStage(enum.Enum):
    NeedFollowers = 0
    EveryoneCheckedIn = 1
    HasMinimumRoster = 2


class ESmartObjectLookAtRule(enum.Enum):
    ESmartObjectLookAtRule_MAX = 0
    ActorCenter = 1
    ActorEyes = 2


class ESlotAlignRule(enum.Enum):
    Center = 0
    Align = 1


class ESmartObjectNotify(enum.Enum):
    ESmartObjectNotify_MAX = 0
    LerpToGround = 1


class ECoverFaceDirection(enum.Enum):
    ECoverFaceDirection_MAX = 0
    Away = 1


class ECoverAdjustFailReason(enum.Enum):
    NoView = 0
    NoRoom = 1
    ECoverAdjustFailReason_MAX = 2


class ECoverSlotHeight(enum.Enum):
    ECoverSlotHeight_MAX = 0
    High = 1


class ECoverStyleAnimType(enum.Enum):
    TimedStayIn = 0
    SingleAnim = 1


class ECoverUserState(enum.Enum):
    Idling = 0
    Firing = 1


class ETerritoryMovementType(enum.Enum):
    Dynamic = 0
    Flight = 1


class EUberTraceMultiTraceRequirement(enum.Enum):
    EUberTraceMultiTraceRequirement_MAX = 0
    AllMustPassTest = 1


class ENavJumpStage(enum.Enum):
    Idle = 0
    Enter = 1
    End = 2


class ENavJumpRotation(enum.Enum):
    FaceJumpOrigin = 0
    FaceJumpTarget = 1
    ENavJumpRotation_MAX = 2


class ELookAtPointType(enum.Enum):
    Persist = 0
    Any = 1


class ESmartObjectTaskState(enum.Enum):
    Movement = 0
    Alignment = 1
    Complete = 2


class ESmartObjectTaskResult(enum.Enum):
    Succeeded = 0
    Failed = 1


class ESmartObjectUseResult(enum.Enum):
    ESmartObjectUseResult_MAX = 0
    Running = 1
    Blocking = 2


class EInitialPathAction(enum.Enum):
    ScriptedPath = 0
    PatrolPath = 1
    ScriptedWait = 2

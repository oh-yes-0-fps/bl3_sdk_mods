from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import gameplay_tasks
from . import navigation_system
from . import gameplay_tags


class BTNode(unreal.UObject):
    NodeName: str
    TreeAsset: BehaviorTree
    ParentNode: BTCompositeNode


class BTTaskNode(BTNode):
    Services: unreal.WrappedArray[BTService]
    bIgnoreRestartSelf: bool


class BrainComponent(engine.ActorComponent):
    BlackboardComp: BlackboardComponent
    AIOwner: AIController

    def StopLogic(self, Reason: str): ...
    def RestartLogic(self): ...
    def IsRunning(self) -> bool: ...
    def IsPaused(self) -> bool: ...


class AISense(unreal.UObject):
    DefaultExpirationAge: float
    NotifyType: EAISenseNotifyType
    bWantsNewPawnNotification: bool
    bAutoRegisterAllPawnsAsSources: bool
    PerceptionSystemInstance: AIPerceptionSystem


class AISenseConfig(unreal.UObject):
    DebugColor: core_uobject.Color
    MaxAge: float
    bStartsEnabled: bool


class AITask(gameplay_tasks.GameplayTask):
    OwnerController: AIController


class BlackboardKeyType(unreal.UObject): ...


class BTCompositeNode(BTNode):
    Children: unreal.WrappedArray[BTCompositeChild]
    Services: unreal.WrappedArray[BTService]
    bApplyDecoratorScope: bool


class BTComposite_Selector(BTCompositeNode): ...


class BTAuxiliaryNode(BTNode): ...


class BTDecorator(BTAuxiliaryNode):
    bInverseCondition: bool
    FlowAbortMode: int


class BTDecorator_BlackboardBase(BTDecorator):
    BlackboardKey: BlackboardKeySelector


class BTService(BTAuxiliaryNode):
    Interval: float
    RandomDeviation: float
    bCallTickOnSearchStart: bool
    bRestartTimerOnEachActivation: bool


class BTService_BlackboardBase(BTService):
    BlackboardKey: BlackboardKeySelector


class BTService_DefaultFocus(BTService_BlackboardBase):
    FocusPriority: int


class BTService_RunEQS(BTService_BlackboardBase):
    EQSRequest: EQSParametrizedQueryExecutionRequest
    bClearEntryOnFailure: bool


class BTTask_BlackboardBase(BTTaskNode):
    BlackboardKey: BlackboardKeySelector


class BTTask_MoveTo(BTTask_BlackboardBase):
    AcceptableRadius: float
    FilterClass: unreal.UClass
    ObservedBlackboardValueTolerance: float
    bObserveBlackboardValue: bool
    bAllowStrafe: bool
    bAllowPartialPath: bool
    bTrackMovingGoal: bool
    bProjectGoalLocation: bool
    bReachTestIncludesAgentRadius: bool
    bReachTestIncludesGoalRadius: bool
    bStopOnOverlap: bool
    bStopOnOverlapNeedsUpdate: bool


class EnvQueryContext(unreal.UObject): ...


class EnvQueryNode(unreal.UObject):
    VerNum: int
    ContextTypes: unreal.WrappedArray[unreal.UClass]


class EnvQueryGenerator(EnvQueryNode):
    OptionName: str
    ItemType: unreal.UClass
    bAutoSortTests: bool


class EnvQueryGenerator_ProjectedPoints(EnvQueryGenerator):
    ProjectionData: EnvTraceData
    bCaresAboutHotSpots: bool


class EnvQueryItemType(unreal.UObject): ...


class EnvQueryItemType_VectorBase(EnvQueryItemType): ...


class EnvQueryTest(EnvQueryNode):
    TestOrder: int
    TestPurpose: int
    TestComment: str
    MultipleContextFilterOp: int
    MultipleContextScoreOp: int
    FilterType: int
    BoolValue: AIDataProviderBoolValue
    FloatValueMin: AIDataProviderFloatValue
    FloatValueMax: AIDataProviderFloatValue
    ScoringEquation: int
    ClampMinType: int
    ClampMaxType: int
    NormalizationType: EEQSNormalizationType
    ScoreClampMin: AIDataProviderFloatValue
    ScoreClampMax: AIDataProviderFloatValue
    ScoringFactor: AIDataProviderFloatValue
    ReferenceValue: AIDataProviderFloatValue
    bDefineReferenceValue: bool
    bWorkOnFloatValues: bool
    CopiedFrom: EnvQueryTest


class EnvQueryTest_Trace(EnvQueryTest):
    TraceData: EnvTraceData
    TraceFromContext: AIDataProviderBoolValue
    ItemHeightOffset: AIDataProviderFloatValue
    ContextHeightOffset: AIDataProviderFloatValue
    Context: unreal.UClass


class AIController(engine.Controller):
    bStopAILogicOnUnposses: bool
    bLOSflag: bool
    bSkipExtraLOSChecks: bool
    bAllowStrafe: bool
    bWantsPlayerState: bool
    bSetControlRotationFromPawnOrientation: bool
    PathFollowingComponent: PathFollowingComponent
    BrainComponent: BrainComponent
    PerceptionComponent: AIPerceptionComponent
    ActionsComp: PawnActionsComponent
    Blackboard: BlackboardComponent
    CachedGameplayTasksComponent: gameplay_tasks.GameplayTasksComponent
    DefaultNavigationFilterClass: unreal.UClass
    ReceiveMoveCompleted: Any

    def UseBlackboard(
        self, BlackboardAsset: BlackboardData, BlackboardComponent: BlackboardComponent
    ) -> bool: ...
    def UnclaimTaskResource(self, ResourceClass: unreal.UClass): ...
    def SetMoveBlockDetection(self, bEnable: bool): ...
    def RunBehaviorTree(self, BTAsset: BehaviorTree) -> bool: ...
    def OnUsingBlackBoard(
        self, BlackboardComp: BlackboardComponent, BlackboardAsset: BlackboardData
    ): ...
    def OnUnpossess(self, UnpossessedPawn: engine.Pawn): ...
    def OnPossess(self, PossessedPawn: engine.Pawn): ...
    def OnGameplayTaskResourcesClaimed(
        self,
        NewlyClaimed: gameplay_tasks.GameplayResourceSet,
        FreshlyReleased: gameplay_tasks.GameplayResourceSet,
    ): ...
    def MoveToLocation(
        self,
        Dest: core_uobject.Vector,
        AcceptanceRadius: float,
        bStopOnOverlap: bool,
        bUsePathfinding: bool,
        bProjectDestinationToNavigation: bool,
        bCanStrafe: bool,
        FilterClass: unreal.UClass,
        bAllowPartialPath: bool,
    ) -> int: ...
    def MoveToActor(
        self,
        Goal: engine.Actor,
        AcceptanceRadius: float,
        bStopOnOverlap: bool,
        bUsePathfinding: bool,
        bCanStrafe: bool,
        FilterClass: unreal.UClass,
        bAllowPartialPath: bool,
    ) -> int: ...
    def K2_SetFocus(self, NewFocus: engine.Actor): ...
    def K2_SetFocalPoint(self, FP: core_uobject.Vector): ...
    def K2_ClearFocus(self): ...
    def HasPartialPath(self) -> bool: ...
    def GetPathFollowingComponent(self) -> PathFollowingComponent: ...
    def GetMoveStatus(self) -> int: ...
    def GetImmediateMoveDestination(self) -> core_uobject.Vector: ...
    def GetFocusActor(self) -> engine.Actor: ...
    def GetFocalPointOnActor(self, Actor: engine.Actor) -> core_uobject.Vector: ...
    def GetFocalPoint(self) -> core_uobject.Vector: ...
    def GetAIPerceptionComponent(self) -> AIPerceptionComponent: ...
    def ClaimTaskResource(self, ResourceClass: unreal.UClass): ...


class AISystem(engine.AISystemBase):
    PerceptionSystemClassName: core_uobject.SoftClassPath
    HotSpotManagerClassName: core_uobject.SoftClassPath
    AcceptanceRadius: float
    PathfollowingRegularPathPointAcceptanceRadius: float
    PathfollowingNavLinkAcceptanceRadius: float
    bFinishMoveOnGoalOverlap: bool
    bAcceptPartialPaths: bool
    bAllowStrafing: bool
    bEnableBTAITasks: bool
    bAllowControllersAsEQSQuerier: bool
    bEnableDebuggerPlugin: bool
    DefaultSightCollisionChannel: int
    BehaviorTreeManager: BehaviorTreeManager
    EnvironmentQueryManager: EnvQueryManager
    PerceptionSystem: AIPerceptionSystem
    AllProxyObjects: unreal.WrappedArray[AIAsyncTaskBlueprintProxy]
    HotSpotManager: AIHotSpotManager
    NavLocalGrids: NavLocalGridManager

    def AILoggingVerbose(self): ...
    def AIIgnorePlayers(self): ...


class BehaviorTreeComponent(BrainComponent):
    NodeInstances: unreal.WrappedArray[BTNode]

    def SetDynamicSubtree(
        self, InjectTag: gameplay_tags.GameplayTag, BehaviorAsset: BehaviorTree
    ): ...
    def GetTagCooldownEndTime(
        self, CooldownTag: gameplay_tags.GameplayTag
    ) -> float: ...
    def AddCooldownTagDuration(
        self,
        CooldownTag: gameplay_tags.GameplayTag,
        CooldownDuration: float,
        bAddToExistingDuration: bool,
    ): ...


class EQSTestingPawn(engine.Character):
    QueryTemplate: EnvQuery
    QueryParams: unreal.WrappedArray[EnvNamedValue]
    QueryConfig: unreal.WrappedArray[AIDynamicParam]
    QueryContexts: Any
    TimeLimitPerStep: float
    StepToDebugDraw: int
    HighlightMode: EEnvQueryHightlightMode
    bDrawLabels: bool
    bDrawFailedItems: bool
    bReRunQueryOnlyOnFinishedMove: bool
    bShouldBeVisibleInGame: bool
    bTickDuringGame: bool
    QueryingMode: int
    NavAgentProperties: engine.NavAgentProperties
    bDrawTraces: bool


class AIAsyncTaskBlueprintProxy(unreal.UObject):
    OnSuccess: Any
    OnFail: Any

    def OnMoveCompleted(self, RequestID: AIRequestID, MovementResult: int): ...


class AIBlueprintHelperLibrary(engine.BlueprintFunctionLibrary):

    def UnlockAIResourcesWithAnimation(
        self,
        AnimInstance: engine.AnimInstance,
        bUnlockMovement: bool,
        UnlockAILogic: bool,
    ): ...
    def SpawnAIFromClass(
        self,
        WorldContextObject: unreal.UObject,
        PawnClass: unreal.UClass,
        BehaviorTree: BehaviorTree,
        Location: core_uobject.Vector,
        Rotation: core_uobject.Rotator,
        bNoCollisionFail: bool,
    ) -> engine.Pawn: ...
    def SimpleMoveToLocation(
        self, Controller: engine.Controller, Goal: core_uobject.Vector
    ): ...
    def SimpleMoveToActor(self, Controller: engine.Controller, Goal: engine.Actor): ...
    def SendAIMessage(
        self,
        Target: engine.Pawn,
        MESSAGE: str,
        MessageSource: unreal.UObject,
        bSuccess: bool,
    ): ...
    def LockAIResourcesWithAnimation(
        self, AnimInstance: engine.AnimInstance, bLockMovement: bool, LockAILogic: bool
    ): ...
    def IsValidAIRotation(self, Rotation: core_uobject.Rotator) -> bool: ...
    def IsValidAILocation(self, Location: core_uobject.Vector) -> bool: ...
    def IsValidAIDirection(self, DirectionVector: core_uobject.Vector) -> bool: ...
    def GetCurrentPath(
        self, Controller: engine.Controller
    ) -> navigation_system.NavigationPath: ...
    def GetBlackboard(self, Target: engine.Actor) -> BlackboardComponent: ...
    def GetAIController(self, ControlledActor: engine.Actor) -> AIController: ...
    def CreateMoveToProxyObject(
        self,
        WorldContextObject: unreal.UObject,
        Pawn: engine.Pawn,
        Destination: core_uobject.Vector,
        TargetActor: engine.Actor,
        AcceptanceRadius: float,
        bStopOnOverlap: bool,
    ) -> AIAsyncTaskBlueprintProxy: ...


class AIDataProvider(unreal.UObject): ...


class AIDataProvider_QueryParams(AIDataProvider):
    ParamName: str
    FloatValue: float
    IntValue: int
    BoolValue: bool


class AIDataProvider_Random(AIDataProvider_QueryParams):
    Min: float
    Max: float
    bInteger: bool


class AIHotSpotManager(unreal.UObject): ...


class AIPerceptionComponent(engine.ActorComponent):
    SensesConfig: unreal.WrappedArray[AISenseConfig]
    DominantSense: unreal.UClass
    AIOwner: AIController
    OwnerTeamAgent: Any
    bOwnerIsStationary: bool
    OnPerceptionUpdated: Any
    OnTargetPerceptionUpdated: Any

    def SetSenseEnabled(self, SenseClass: unreal.UClass, bEnable: bool): ...
    def RequestStimuliListenerUpdate(self): ...
    def OnOwnerEndPlay(self, Actor: engine.Actor, EndPlayReason: int): ...
    def GetPerceivedHostileActors(
        self, OutActors: unreal.WrappedArray[engine.Actor]
    ): ...
    def GetPerceivedActors(
        self, SenseToUse: unreal.UClass, OutActors: unreal.WrappedArray[engine.Actor]
    ): ...
    def GetKnownPerceivedActors(
        self, SenseToUse: unreal.UClass, OutActors: unreal.WrappedArray[engine.Actor]
    ): ...
    def GetCurrentlyPerceivedActors(
        self, SenseToUse: unreal.UClass, OutActors: unreal.WrappedArray[engine.Actor]
    ): ...
    def GetActorsPerception(
        self, Actor: engine.Actor, Info: ActorPerceptionBlueprintInfo
    ) -> bool: ...


class AIPerceptionListenerInterface(core_uobject.Interface): ...


class AIPerceptionStimuliSourceComponent(engine.ActorComponent):
    bAutoRegisterAsSource: bool
    RegisterAsSourceForSenses: unreal.WrappedArray[unreal.UClass]

    def UnregisterFromSense(self, SenseClass: unreal.UClass): ...
    def UnregisterFromPerceptionSystem(self): ...
    def RegisterWithPerceptionSystem(self): ...
    def RegisterForSense(self, SenseClass: unreal.UClass): ...


class AIPerceptionSystem(unreal.UObject):
    Senses: unreal.WrappedArray[AISense]
    PerceptionAgingRate: float
    PerceptionSourceWhitelist: unreal.WrappedArray[str]
    PerceptionSourceBlacklist: unreal.WrappedArray[str]
    MustHaveAssociatedCharacter: unreal.WrappedArray[str]

    def ReportPerceptionEvent(
        self, WorldContextObject: unreal.UObject, PerceptionEvent: AISenseEvent
    ): ...
    def ReportEvent(self, PerceptionEvent: AISenseEvent): ...
    def RegisterPerceptionStimuliSource(
        self,
        WorldContextObject: unreal.UObject,
        Sense: unreal.UClass,
        Target: engine.Actor,
    ) -> bool: ...
    def OnPerceptionStimuliSourceEndPlay(
        self, Actor: engine.Actor, EndPlayReason: int
    ): ...
    def GetSenseClassForStimulus(
        self, WorldContextObject: unreal.UObject, Stimulus: AIStimulus
    ) -> unreal.UClass: ...


class AIResourceInterface(core_uobject.Interface): ...


class AIResource_Movement(gameplay_tasks.GameplayTaskResource): ...


class AIResource_Logic(gameplay_tasks.GameplayTaskResource): ...


class AISense_Blueprint(AISense):
    ListenerDataType: unreal.UClass
    ListenerContainer: unreal.WrappedArray[AIPerceptionComponent]
    UnprocessedEvents: unreal.WrappedArray[AISenseEvent]

    def OnUpdate(self, EventsToProcess: unreal.WrappedArray[AISenseEvent]) -> float: ...
    def OnListenerUpdated(
        self, ActorListener: engine.Actor, PerceptionComponent: AIPerceptionComponent
    ): ...
    def OnListenerUnregistered(
        self, ActorListener: engine.Actor, PerceptionComponent: AIPerceptionComponent
    ): ...
    def OnListenerRegistered(
        self, ActorListener: engine.Actor, PerceptionComponent: AIPerceptionComponent
    ): ...
    def K2_OnNewPawn(self, NewPawn: engine.Pawn): ...
    def GetAllListenerComponents(
        self, ListenerComponents: unreal.WrappedArray[AIPerceptionComponent]
    ): ...
    def GetAllListenerActors(
        self, ListenerActors: unreal.WrappedArray[engine.Actor]
    ): ...


class AISense_Damage(AISense):
    RegisteredEvents: unreal.WrappedArray[AIDamageEvent]

    def ReportDamageEvent(
        self,
        WorldContextObject: unreal.UObject,
        DamagedActor: engine.Actor,
        Instigator: engine.Actor,
        DamageAmount: float,
        EventLocation: core_uobject.Vector,
        HitLocation: core_uobject.Vector,
    ): ...


class AISense_Hearing(AISense):
    NoiseEvents: unreal.WrappedArray[AINoiseEvent]
    SpeedOfSoundSq: float

    def ReportNoiseEvent(
        self,
        WorldContextObject: unreal.UObject,
        NoiseLocation: core_uobject.Vector,
        Loudness: float,
        Instigator: engine.Actor,
        MaxRange: float,
        Tag: str,
    ): ...


class AISense_Prediction(AISense):
    RegisteredEvents: unreal.WrappedArray[AIPredictionEvent]

    def RequestPawnPredictionEvent(
        self,
        Requestor: engine.Pawn,
        PredictedActor: engine.Actor,
        PredictionTime: float,
    ): ...
    def RequestControllerPredictionEvent(
        self,
        Requestor: AIController,
        PredictedActor: engine.Actor,
        PredictionTime: float,
    ): ...


class AISense_Sight(AISense):
    MaxTracesPerTick: int
    MinQueriesPerTimeSliceCheck: int
    MaxTimeSlicePerTick: float
    HighImportanceQueryDistanceThreshold: float
    MaxQueryImportance: float
    SightLimitQueryImportance: float


class AISense_Team(AISense):
    RegisteredEvents: unreal.WrappedArray[AITeamStimulusEvent]


class AISense_Touch(AISense):
    RegisteredEvents: unreal.WrappedArray[AITouchEvent]


class AISenseBlueprintListener(engine.UserDefinedStruct): ...


class AISenseConfig_Blueprint(AISenseConfig):
    Implementation: unreal.UClass


class AISenseConfig_Damage(AISenseConfig):
    Implementation: unreal.UClass


class AISenseConfig_Hearing(AISenseConfig):
    Implementation: unreal.UClass
    HearingRange: float
    LoSHearingRange: float
    bUseLoSHearing: bool
    DetectionByAffiliation: AISenseAffiliationFilter


class AISenseConfig_Prediction(AISenseConfig): ...


class AISenseConfig_Sight(AISenseConfig):
    Implementation: unreal.UClass
    SightRadius: float
    LoseSightRadius: float
    PeripheralVisionAngleDegrees: float
    DetectionByAffiliation: AISenseAffiliationFilter
    AutoSuccessRangeFromLastSeenLocation: float


class AISenseConfig_Team(AISenseConfig): ...


class AISenseConfig_Touch(AISenseConfig): ...


class AISenseEvent(unreal.UObject): ...


class AISenseEvent_Damage(AISenseEvent):
    Event: AIDamageEvent


class AISenseEvent_Hearing(AISenseEvent):
    Event: AINoiseEvent


class AISightTargetInterface(core_uobject.Interface): ...


class AITask_LockLogic(AITask): ...


class AITask_MoveTo(AITask):
    OnRequestFailed: Any
    OnMoveFinished: Any
    MoveRequest: AIMoveRequest

    def AIMoveTo(
        self,
        Controller: AIController,
        GoalLocation: core_uobject.Vector,
        GoalActor: engine.Actor,
        AcceptanceRadius: float,
        StopOnOverlap: int,
        AcceptPartialPath: int,
        bUsePathfinding: bool,
        bLockAILogic: bool,
        bUseContinuosGoalTracking: bool,
    ) -> AITask_MoveTo: ...


class AITask_RunEQS(AITask):

    def RunEQS(
        self, Controller: AIController, QueryTemplate: EnvQuery
    ) -> AITask_RunEQS: ...


class BehaviorTree(unreal.UObject):
    RootNode: BTCompositeNode
    BlackboardAsset: BlackboardData
    RootDecorators: unreal.WrappedArray[BTDecorator]
    RootDecoratorOps: unreal.WrappedArray[BTDecoratorLogic]


class BehaviorTreeManager(unreal.UObject):
    MaxDebuggerSteps: int
    LoadedTemplates: unreal.WrappedArray[BehaviorTreeTemplateInfo]
    ActiveComponents: unreal.WrappedArray[BehaviorTreeComponent]


class BehaviorTreeTypes(unreal.UObject): ...


class BlackboardComponent(engine.ActorComponent):
    BrainComp: BrainComponent
    BlackboardAsset: BlackboardData
    KeyInstances: unreal.WrappedArray[BlackboardKeyType]
    RuntimeKeys: unreal.WrappedArray[BlackboardEntry]

    def SetValueAsVector(self, KeyName: str, VectorValue: core_uobject.Vector): ...
    def SetValueAsString(self, KeyName: str, StringValue: str): ...
    def SetValueAsRotator(self, KeyName: str, VectorValue: core_uobject.Rotator): ...
    def SetValueAsObject(self, KeyName: str, ObjectValue: unreal.UObject): ...
    def SetValueAsName(self, KeyName: str, NameValue: str): ...
    def SetValueAsInt(self, KeyName: str, IntValue: int): ...
    def SetValueAsFloat(self, KeyName: str, FloatValue: float): ...
    def SetValueAsEnum(self, KeyName: str, EnumValue: int): ...
    def SetValueAsClass(self, KeyName: str, ClassValue: unreal.UClass): ...
    def SetValueAsBool(self, KeyName: str, BoolValue: bool): ...
    def IsVectorValueSet(self, KeyName: str) -> bool: ...
    def HasValue(self, KeyName: str) -> bool: ...
    def GetValueAsVector(self, KeyName: str) -> core_uobject.Vector: ...
    def GetValueAsString(self, KeyName: str) -> str: ...
    def GetValueAsRotator(self, KeyName: str) -> core_uobject.Rotator: ...
    def GetValueAsObject(self, KeyName: str) -> unreal.UObject: ...
    def GetValueAsName(self, KeyName: str) -> str: ...
    def GetValueAsInt(self, KeyName: str) -> int: ...
    def GetValueAsFloat(self, KeyName: str) -> float: ...
    def GetValueAsEnum(self, KeyName: str) -> int: ...
    def GetValueAsClass(self, KeyName: str) -> unreal.UClass: ...
    def GetValueAsBool(self, KeyName: str) -> bool: ...
    def GetRotationFromEntry(
        self, KeyName: str, ResultRotation: core_uobject.Rotator
    ) -> bool: ...
    def GetLocationFromEntry(
        self, KeyName: str, ResultLocation: core_uobject.Vector
    ) -> bool: ...
    def ClearValue(self, KeyName: str): ...
    def AddRuntimeKey(self, KeyName: str, KeyType: BlackboardKeyType) -> int: ...


class BlackboardData(engine.DataAsset):
    Parent: BlackboardData
    Keys: unreal.WrappedArray[BlackboardEntry]
    bHasSynchronizedKeys: bool


class BlackboardKeyType_Bool(BlackboardKeyType):
    DefaultValue: bool


class BlackboardKeyType_Class(BlackboardKeyType):
    BaseClass: unreal.UClass


class BlackboardKeyType_Enum(BlackboardKeyType):
    EnumType: unreal.UEnum
    EnumName: str
    bIsEnumNameValid: bool


class BlackboardKeyType_Float(BlackboardKeyType):
    DefaultValue: float


class BlackboardKeyType_Int(BlackboardKeyType):
    DefaultValue: int


class BlackboardKeyType_Name(BlackboardKeyType):
    DefaultValue: str


class BlackboardKeyType_NativeEnum(BlackboardKeyType):
    EnumName: str
    EnumType: unreal.UEnum


class BlackboardKeyType_Object(BlackboardKeyType):
    BaseClass: unreal.UClass


class BlackboardKeyType_Rotator(BlackboardKeyType):
    DefaultValue: core_uobject.Rotator
    bUseDefaultValue: bool


class BlackboardKeyType_String(BlackboardKeyType):
    StringValue: str
    DefaultValue: str


class BlackboardKeyType_Vector(BlackboardKeyType):
    DefaultValue: core_uobject.Vector
    bUseDefaultValue: bool


class BTComposite_Sequence(BTCompositeNode): ...


class BTComposite_SimpleParallel(BTCompositeNode):
    FinishMode: int


class BTDecorator_Blackboard(BTDecorator_BlackboardBase):
    IntValue: int
    FloatValue: float
    StringValue: str
    CachedDescription: str
    OperationType: int
    NotifyObserver: int


class BTDecorator_BlueprintBase(BTDecorator):
    AIOwner: AIController
    ActorOwner: engine.Actor
    ObservedKeyNames: unreal.WrappedArray[str]
    bShowPropertyDetails: bool
    bCheckConditionOnlyBlackBoardChanges: bool
    bIsObservingBB: bool

    def ReceiveTickAI(
        self,
        OwnerController: AIController,
        ControlledPawn: engine.Pawn,
        DeltaSeconds: float,
    ): ...
    def ReceiveTick(self, OwnerActor: engine.Actor, DeltaSeconds: float): ...
    def ReceiveObserverDeactivatedAI(
        self, OwnerController: AIController, ControlledPawn: engine.Pawn
    ): ...
    def ReceiveObserverDeactivated(self, OwnerActor: engine.Actor): ...
    def ReceiveObserverActivatedAI(
        self, OwnerController: AIController, ControlledPawn: engine.Pawn
    ): ...
    def ReceiveObserverActivated(self, OwnerActor: engine.Actor): ...
    def ReceiveExecutionStartAI(
        self, OwnerController: AIController, ControlledPawn: engine.Pawn
    ): ...
    def ReceiveExecutionStart(self, OwnerActor: engine.Actor): ...
    def ReceiveExecutionFinishAI(
        self,
        OwnerController: AIController,
        ControlledPawn: engine.Pawn,
        NodeResult: int,
    ): ...
    def ReceiveExecutionFinish(self, OwnerActor: engine.Actor, NodeResult: int): ...
    def PerformConditionCheckAI(
        self, OwnerController: AIController, ControlledPawn: engine.Pawn
    ) -> bool: ...
    def PerformConditionCheck(self, OwnerActor: engine.Actor) -> bool: ...
    def IsDecoratorObserverActive(self) -> bool: ...
    def IsDecoratorExecutionActive(self) -> bool: ...


class BTDecorator_CheckGameplayTagsOnActor(BTDecorator):
    ActorToCheck: BlackboardKeySelector
    TagsToMatch: gameplay_tags.EGameplayContainerMatchType
    GameplayTags: gameplay_tags.GameplayTagContainer
    CachedDescription: str


class BTDecorator_CompareBBEntries(BTDecorator):
    Operator: int
    BlackboardKeyA: BlackboardKeySelector
    BlackboardKeyB: BlackboardKeySelector


class BTDecorator_ConditionalLoop(BTDecorator_Blackboard): ...


class BTDecorator_ConeCheck(BTDecorator):
    ConeHalfAngle: float
    ConeOrigin: BlackboardKeySelector
    ConeDirection: BlackboardKeySelector
    Observed: BlackboardKeySelector


class BTDecorator_Cooldown(BTDecorator):
    CooldownTime: float


class BTDecorator_DoesPathExist(BTDecorator):
    BlackboardKeyA: BlackboardKeySelector
    BlackboardKeyB: BlackboardKeySelector
    bUseSelf: bool
    PathQueryType: int
    FilterClass: unreal.UClass


class BTDecorator_ForceSuccess(BTDecorator): ...


class BTDecorator_IsAtLocation(BTDecorator_BlackboardBase):
    AcceptableRadius: float
    ParametrizedAcceptableRadius: AIDataProviderFloatValue
    GeometricDistanceType: FAIDistanceType
    bUseParametrizedRadius: bool
    bUseNavAgentGoalLocation: bool
    bPathFindingBasedTest: bool


class BTDecorator_IsBBEntryOfClass(BTDecorator_BlackboardBase):
    TestClass: unreal.UClass


class BTDecorator_KeepInCone(BTDecorator):
    ConeHalfAngle: float
    ConeOrigin: BlackboardKeySelector
    Observed: BlackboardKeySelector
    bUseSelfAsOrigin: bool
    bUseSelfAsObserved: bool


class BTDecorator_Loop(BTDecorator):
    NumLoops: int
    bInfiniteLoop: bool
    InfiniteLoopTimeoutTime: float


class BTDecorator_ReachedMoveGoal(BTDecorator): ...


class BTDecorator_SetTagCooldown(BTDecorator):
    CooldownTag: gameplay_tags.GameplayTag
    CooldownDuration: float
    bAddToExistingDuration: bool


class BTDecorator_TagCooldown(BTDecorator):
    CooldownTag: gameplay_tags.GameplayTag
    CooldownDuration: float
    bAddToExistingDuration: bool
    bActivatesCooldown: bool


class BTDecorator_TimeLimit(BTDecorator):
    TimeLimit: float


class BTFunctionLibrary(engine.BlueprintFunctionLibrary):

    def StopUsingExternalEvent(self, NodeOwner: BTNode): ...
    def StartUsingExternalEvent(self, NodeOwner: BTNode, OwningActor: engine.Actor): ...
    def SetBlackboardValueAsVector(
        self, NodeOwner: BTNode, Key: BlackboardKeySelector, Value: core_uobject.Vector
    ): ...
    def SetBlackboardValueAsString(
        self, NodeOwner: BTNode, Key: BlackboardKeySelector, Value: str
    ): ...
    def SetBlackboardValueAsRotator(
        self, NodeOwner: BTNode, Key: BlackboardKeySelector, Value: core_uobject.Rotator
    ): ...
    def SetBlackboardValueAsObject(
        self, NodeOwner: BTNode, Key: BlackboardKeySelector, Value: unreal.UObject
    ): ...
    def SetBlackboardValueAsName(
        self, NodeOwner: BTNode, Key: BlackboardKeySelector, Value: str
    ): ...
    def SetBlackboardValueAsInt(
        self, NodeOwner: BTNode, Key: BlackboardKeySelector, Value: int
    ): ...
    def SetBlackboardValueAsFloat(
        self, NodeOwner: BTNode, Key: BlackboardKeySelector, Value: float
    ): ...
    def SetBlackboardValueAsEnum(
        self, NodeOwner: BTNode, Key: BlackboardKeySelector, Value: int
    ): ...
    def SetBlackboardValueAsClass(
        self, NodeOwner: BTNode, Key: BlackboardKeySelector, Value: unreal.UClass
    ): ...
    def SetBlackboardValueAsBool(
        self, NodeOwner: BTNode, Key: BlackboardKeySelector, Value: bool
    ): ...
    def GetOwnersBlackboard(self, NodeOwner: BTNode) -> BlackboardComponent: ...
    def GetOwnerComponent(self, NodeOwner: BTNode) -> BehaviorTreeComponent: ...
    def GetBlackboardValueAsVector(
        self, NodeOwner: BTNode, Key: BlackboardKeySelector
    ) -> core_uobject.Vector: ...
    def GetBlackboardValueAsString(
        self, NodeOwner: BTNode, Key: BlackboardKeySelector
    ) -> str: ...
    def GetBlackboardValueAsRotator(
        self, NodeOwner: BTNode, Key: BlackboardKeySelector
    ) -> core_uobject.Rotator: ...
    def GetBlackboardValueAsObject(
        self, NodeOwner: BTNode, Key: BlackboardKeySelector
    ) -> unreal.UObject: ...
    def GetBlackboardValueAsName(
        self, NodeOwner: BTNode, Key: BlackboardKeySelector
    ) -> str: ...
    def GetBlackboardValueAsInt(
        self, NodeOwner: BTNode, Key: BlackboardKeySelector
    ) -> int: ...
    def GetBlackboardValueAsFloat(
        self, NodeOwner: BTNode, Key: BlackboardKeySelector
    ) -> float: ...
    def GetBlackboardValueAsEnum(
        self, NodeOwner: BTNode, Key: BlackboardKeySelector
    ) -> int: ...
    def GetBlackboardValueAsClass(
        self, NodeOwner: BTNode, Key: BlackboardKeySelector
    ) -> unreal.UClass: ...
    def GetBlackboardValueAsBool(
        self, NodeOwner: BTNode, Key: BlackboardKeySelector
    ) -> bool: ...
    def GetBlackboardValueAsActor(
        self, NodeOwner: BTNode, Key: BlackboardKeySelector
    ) -> engine.Actor: ...
    def ClearBlackboardValueAsVector(
        self, NodeOwner: BTNode, Key: BlackboardKeySelector
    ): ...
    def ClearBlackboardValue(self, NodeOwner: BTNode, Key: BlackboardKeySelector): ...


class BTService_BlueprintBase(BTService):
    AIOwner: AIController
    ActorOwner: engine.Actor
    bShowPropertyDetails: bool
    bShowEventDetails: bool

    def ReceiveTickAI(
        self,
        OwnerController: AIController,
        ControlledPawn: engine.Pawn,
        DeltaSeconds: float,
    ): ...
    def ReceiveTick(self, OwnerActor: engine.Actor, DeltaSeconds: float): ...
    def ReceiveSearchStartAI(
        self, OwnerController: AIController, ControlledPawn: engine.Pawn
    ): ...
    def ReceiveSearchStart(self, OwnerActor: engine.Actor): ...
    def ReceiveDeactivationAI(
        self, OwnerController: AIController, ControlledPawn: engine.Pawn
    ): ...
    def ReceiveDeactivation(self, OwnerActor: engine.Actor): ...
    def ReceiveActivationAI(
        self, OwnerController: AIController, ControlledPawn: engine.Pawn
    ): ...
    def ReceiveActivation(self, OwnerActor: engine.Actor): ...
    def IsServiceActive(self) -> bool: ...


class BTTask_BlueprintBase(BTTaskNode):
    AIOwner: AIController
    ActorOwner: engine.Actor
    bShowPropertyDetails: bool

    def SetFinishOnMessageWithId(self, MessageName: str, RequestID: int): ...
    def SetFinishOnMessage(self, MessageName: str): ...
    def ReceiveTickAI(
        self,
        OwnerController: AIController,
        ControlledPawn: engine.Pawn,
        DeltaSeconds: float,
    ): ...
    def ReceiveTick(self, OwnerActor: engine.Actor, DeltaSeconds: float): ...
    def ReceiveExecuteAI(
        self, OwnerController: AIController, ControlledPawn: engine.Pawn
    ): ...
    def ReceiveExecute(self, OwnerActor: engine.Actor): ...
    def ReceiveAbortAI(
        self, OwnerController: AIController, ControlledPawn: engine.Pawn
    ): ...
    def ReceiveAbort(self, OwnerActor: engine.Actor): ...
    def IsTaskExecuting(self) -> bool: ...
    def IsTaskAborting(self) -> bool: ...
    def FinishExecute(self, bSuccess: bool): ...
    def FinishAbort(self): ...


class BTTask_GameplayTaskBase(BTTaskNode):
    bWaitForGameplayTask: bool


class BTTask_MakeNoise(BTTaskNode):
    Loudnes: float


class BTTask_MoveDirectlyToward(BTTask_MoveTo):
    bDisablePathUpdateOnGoalLocationChange: bool
    bProjectVectorGoalToNavigation: bool
    bUpdatedDeprecatedProperties: bool


class BTTask_PawnActionBase(BTTaskNode): ...


class BTTask_PlayAnimation(BTTaskNode):
    AnimationToPlay: engine.AnimationAsset
    bLooping: bool
    bNonBlocking: bool
    MyOwnerComp: BehaviorTreeComponent
    CachedSkelMesh: engine.SkeletalMeshComponent


class BTTask_PlaySound(BTTaskNode):
    SoundToPlay: engine.SoundCue


class BTTask_PushPawnAction(BTTask_PawnActionBase):
    Action: PawnAction


class BTTask_RotateToFaceBBEntry(BTTask_BlackboardBase):
    Precision: float


class BTTask_RunBehavior(BTTaskNode):
    BehaviorAsset: BehaviorTree


class BTTask_RunBehaviorDynamic(BTTaskNode):
    InjectionTag: gameplay_tags.GameplayTag
    DefaultBehaviorAsset: BehaviorTree
    BehaviorAsset: BehaviorTree


class BTTask_RunEQSQuery(BTTask_BlackboardBase):
    QueryTemplate: EnvQuery
    QueryParams: unreal.WrappedArray[EnvNamedValue]
    QueryConfig: unreal.WrappedArray[AIDynamicParam]
    RunMode: int
    EQSQueryBlackboardKey: BlackboardKeySelector
    bUseBBKey: bool
    EQSRequest: EQSParametrizedQueryExecutionRequest


class BTTask_SetTagCooldown(BTTaskNode):
    CooldownTag: gameplay_tags.GameplayTag
    bAddToExistingDuration: bool
    CooldownDuration: float


class BTTask_Wait(BTTaskNode):
    WaitTime: float
    RandomDeviation: float


class BTTask_WaitBlackboardTime(BTTask_Wait):
    BlackboardKey: BlackboardKeySelector


class CrowdAgentInterface(core_uobject.Interface): ...


class PathFollowingComponent(engine.ActorComponent):
    MovementComp: engine.NavMovementComponent
    MyNavData: navigation_system.NavigationData

    def OnNavDataRegistered(self, NavData: navigation_system.NavigationData): ...
    def OnActorBump(
        self,
        SelfActor: engine.Actor,
        OtherActor: engine.Actor,
        NormalImpulse: core_uobject.Vector,
        Hit: engine.HitResult,
    ): ...
    def GetPathDestination(self) -> core_uobject.Vector: ...
    def GetPathActionType(self) -> int: ...


class CrowdFollowingComponent(PathFollowingComponent):
    CrowdAgentMoveDirection: core_uobject.Vector
    CharacterMovement: engine.CharacterMovementComponent
    AvoidanceGroup: engine.NavAvoidanceMask
    GroupsToAvoid: engine.NavAvoidanceMask
    GroupsToIgnore: engine.NavAvoidanceMask

    def SuspendCrowdSteering(self, bSuspend: bool): ...


class CrowdManager(navigation_system.CrowdManagerBase):
    MyNavData: navigation_system.NavigationData
    AvoidanceConfig: unreal.WrappedArray[CrowdAvoidanceConfig]
    SamplingPatterns: unreal.WrappedArray[CrowdAvoidanceSamplingPattern]
    MaxAgents: int
    MaxAgentRadius: float
    MaxAvoidedAgents: int
    MaxAvoidedWalls: int
    NavmeshCheckInterval: float
    PathOptimizationInterval: float
    SeparationDirClamp: float
    PathOffsetRadiusMultiplier: float
    bResolveCollisions: bool


class DetourCrowdAIController(AIController): ...


class EnvQuery(engine.DataAsset):
    QueryName: str
    Options: unreal.WrappedArray[EnvQueryOption]
    ContextTypes: Any


class EnvQueryContext_BlueprintBase(EnvQueryContext):

    def ProvideSingleLocation(
        self,
        QuerierObject: unreal.UObject,
        QuerierActor: engine.Actor,
        ResultingLocation: core_uobject.Vector,
    ): ...
    def ProvideSingleActor(
        self,
        QuerierObject: unreal.UObject,
        QuerierActor: engine.Actor,
        ResultingActor: engine.Actor,
    ): ...
    def ProvideLocationsSet(
        self,
        QuerierObject: unreal.UObject,
        QuerierActor: engine.Actor,
        ResultingLocationSet: unreal.WrappedArray[core_uobject.Vector],
    ): ...
    def ProvideActorsSet(
        self,
        QuerierObject: unreal.UObject,
        QuerierActor: engine.Actor,
        ResultingActorsSet: unreal.WrappedArray[engine.Actor],
    ): ...


class EnvQueryContext_Item(EnvQueryContext): ...


class EnvQueryContext_Querier(EnvQueryContext): ...


class EnvQueryDebugHelpers(unreal.UObject): ...


class EnvQueryGenerator_ActorsOfClass(EnvQueryGenerator):
    SearchedActorClass: unreal.UClass
    GenerateOnlyActorsInRadius: AIDataProviderBoolValue
    SearchRadius: AIDataProviderFloatValue
    SearchCenter: unreal.UClass


class EnvQueryGenerator_BlueprintBase(EnvQueryGenerator):
    GeneratorsActionDescription: str
    Context: unreal.UClass
    GeneratedItemType: unreal.UClass

    def GetQuerier(self) -> unreal.UObject: ...
    def DoItemGeneration(
        self, ContextLocations: unreal.WrappedArray[core_uobject.Vector]
    ): ...
    def AddGeneratedVector(self, GeneratedVector: core_uobject.Vector): ...
    def AddGeneratedActor(self, GeneratedActor: engine.Actor): ...


class EnvQueryGenerator_Composite(EnvQueryGenerator):
    Generators: unreal.WrappedArray[EnvQueryGenerator]
    bAllowDifferentItemTypes: bool
    bHasMatchingItemType: bool
    ForcedItemType: unreal.UClass


class EnvQueryGenerator_Cone(EnvQueryGenerator_ProjectedPoints):
    AlignedPointsDistance: AIDataProviderFloatValue
    ConeDegrees: AIDataProviderFloatValue
    AngleStep: AIDataProviderFloatValue
    Range: AIDataProviderFloatValue
    CenterActor: unreal.UClass
    bIncludeContextLocation: bool


class EnvQueryGenerator_CurrentLocation(EnvQueryGenerator):
    QueryContext: unreal.UClass


class EnvQueryGenerator_Donut(EnvQueryGenerator_ProjectedPoints):
    InnerRadius: AIDataProviderFloatValue
    OuterRadius: AIDataProviderFloatValue
    NumberOfRings: AIDataProviderIntValue
    PointsPerRing: AIDataProviderIntValue
    ArcDirection: EnvDirection
    ArcAngle: AIDataProviderFloatValue
    bUseSpiralPattern: bool
    Center: unreal.UClass
    bDefineArc: bool
    NumberOfLayers: AIDataProviderIntValue
    HighestLayerHeight: AIDataProviderFloatValue
    LowestLayerHeight: AIDataProviderFloatValue


class EnvQueryGenerator_OnCircle(EnvQueryGenerator_ProjectedPoints):
    CircleRadius: AIDataProviderFloatValue
    SpaceBetween: AIDataProviderFloatValue
    NumberOfPoints: AIDataProviderIntValue
    PointOnCircleSpacingMethod: EPointOnCircleSpacingMethod
    ArcDirection: EnvDirection
    ArcAngle: AIDataProviderFloatValue
    AngleRadians: float
    CircleCenter: unreal.UClass
    bIgnoreAnyContextActorsWhenGeneratingCircle: bool
    CircleCenterZOffset: AIDataProviderFloatValue
    TraceData: EnvTraceData
    bDefineArc: bool


class EnvQueryGenerator_SimpleGrid(EnvQueryGenerator_ProjectedPoints):
    GridSize: AIDataProviderFloatValue
    SpaceBetween: AIDataProviderFloatValue
    GenerateAround: unreal.UClass


class EnvQueryGenerator_PathingGrid(EnvQueryGenerator_SimpleGrid):
    PathToItem: AIDataProviderBoolValue
    NavigationFilter: unreal.UClass
    ScanRangeMultiplier: AIDataProviderFloatValue


class EnvQueryInstanceBlueprintWrapper(unreal.UObject):
    QueryID: int
    ItemType: unreal.UClass
    OptionIndex: int
    OnQueryFinishedEvent: Any

    def SetNamedParam(self, ParamName: str, Value: float): ...
    def GetResultsAsLocations(self) -> unreal.WrappedArray[core_uobject.Vector]: ...
    def GetResultsAsActors(self) -> unreal.WrappedArray[engine.Actor]: ...
    def GetItemScore(self, ItemIndex: int) -> float: ...
    def EQSQueryDoneSignature__DelegateSignature(
        self, QueryInstance: EnvQueryInstanceBlueprintWrapper, QueryStatus: int
    ): ...


class EnvQueryItemType_ActorBase(EnvQueryItemType_VectorBase): ...


class EnvQueryItemType_Actor(EnvQueryItemType_ActorBase): ...


class EnvQueryItemType_Component(EnvQueryItemType_ActorBase): ...


class EnvQueryItemType_Direction(EnvQueryItemType_VectorBase): ...


class EnvQueryItemType_Point(EnvQueryItemType_VectorBase): ...


class EnvQueryManager(unreal.UObject):
    InstanceCache: unreal.WrappedArray[EnvQueryInstanceCache]
    AdditionalTestsCache: unreal.WrappedArray[EnvQueryTest]
    LocalContexts: unreal.WrappedArray[EnvQueryContext]
    GCShieldedWrappers: unreal.WrappedArray[EnvQueryInstanceBlueprintWrapper]
    MaxAllowedTestingTime: float
    bTestQueriesUsingBreadth: bool
    QueryCountWarningThreshold: int
    QueryCountWarningInterval: float

    def RunEQSQuery(
        self,
        WorldContextObject: unreal.UObject,
        QueryTemplate: EnvQuery,
        Querier: unreal.UObject,
        RunMode: int,
        WrapperClass: unreal.UClass,
    ) -> EnvQueryInstanceBlueprintWrapper: ...


class EnvQueryOption(unreal.UObject):
    Generator: EnvQueryGenerator
    Tests: unreal.WrappedArray[EnvQueryTest]


class EnvQueryTest_Distance(EnvQueryTest):
    TestMode: int
    DistanceTo: unreal.UClass
    DistanceThreshold: float


class EnvQueryTest_Dot(EnvQueryTest):
    LineA: EnvDirection
    LineB: EnvDirection
    TestMode: EEnvTestDot
    bAbsoluteValue: bool


class EnvQueryTest_GameplayTags(EnvQueryTest):
    TagQueryToMatch: gameplay_tags.GameplayTagQuery
    bPassIfNoTags: bool
    bUpdatedToUseQuery: bool
    TagsToMatch: gameplay_tags.EGameplayContainerMatchType
    GameplayTags: gameplay_tags.GameplayTagContainer


class EnvQueryTest_Overlap(EnvQueryTest):
    OverlapData: EnvOverlapData


class EnvQueryTest_Pathfinding(EnvQueryTest):
    TestMode: int
    Context: unreal.UClass
    PathFromContext: AIDataProviderBoolValue
    SkipUnreachable: AIDataProviderBoolValue
    FilterClass: unreal.UClass


class EnvQueryTest_PathfindingBatch(EnvQueryTest_Pathfinding):
    ScanRangeMultiplier: AIDataProviderFloatValue


class EnvQueryTest_Project(EnvQueryTest):
    ProjectionData: EnvTraceData


class EnvQueryTest_Random(EnvQueryTest): ...


class EnvQueryTypes(unreal.UObject): ...


class EQSQueryResultSourceInterface(core_uobject.Interface): ...


class EQSRenderingComponent(engine.PrimitiveComponent): ...


class GenericTeamAgentInterface(core_uobject.Interface): ...


class GridPathAIController(AIController): ...


class GridPathFollowingComponent(PathFollowingComponent):
    GridManager: NavLocalGridManager


class NavFilter_AIControllerDefault(navigation_system.NavigationQueryFilter): ...


class NavLinkProxy(engine.Actor):
    PointLinks: unreal.WrappedArray[engine.NavigationLink]
    SegmentLinks: unreal.WrappedArray[engine.NavigationSegmentLink]
    SmartLinkComp: navigation_system.NavLinkCustomComponent
    bSmartLinkIsRelevant: bool
    OnSmartLinkReached: Any

    def SetSmartLinkEnabled(self, bEnabled: bool): ...
    def ResumePathFollowing(self, Agent: engine.Actor): ...
    def ReceiveSmartLinkReached(
        self, Agent: engine.Actor, Destination: core_uobject.Vector
    ): ...
    def IsSmartLinkEnabled(self) -> bool: ...
    def HasMovingAgents(self) -> bool: ...


class NavLocalGridManager(unreal.UObject):

    def SetLocalNavigationGridDensity(
        self, WorldContextObject: unreal.UObject, CellSize: float
    ) -> bool: ...
    def RemoveLocalNavigationGrid(
        self, WorldContextObject: unreal.UObject, GridId: int, bRebuildGrids: bool
    ): ...
    def FindLocalNavigationGridPath(
        self,
        WorldContextObject: unreal.UObject,
        Start: core_uobject.Vector,
        End: core_uobject.Vector,
        PathPoints: unreal.WrappedArray[core_uobject.Vector],
    ) -> bool: ...
    def AddLocalNavigationGridForPoints(
        self,
        WorldContextObject: unreal.UObject,
        Locations: unreal.WrappedArray[core_uobject.Vector],
        Radius2D: int,
        Height: float,
        bRebuildGrids: bool,
    ) -> int: ...
    def AddLocalNavigationGridForPoint(
        self,
        WorldContextObject: unreal.UObject,
        Location: core_uobject.Vector,
        Radius2D: int,
        Height: float,
        bRebuildGrids: bool,
    ) -> int: ...
    def AddLocalNavigationGridForCapsule(
        self,
        WorldContextObject: unreal.UObject,
        Location: core_uobject.Vector,
        CapsuleRadius: float,
        CapsuleHalfHeight: float,
        Radius2D: int,
        Height: float,
        bRebuildGrids: bool,
    ) -> int: ...
    def AddLocalNavigationGridForBox(
        self,
        WorldContextObject: unreal.UObject,
        Location: core_uobject.Vector,
        Extent: core_uobject.Vector,
        Rotation: core_uobject.Rotator,
        Radius2D: int,
        Height: float,
        bRebuildGrids: bool,
    ) -> int: ...


class PathFollowingManager(unreal.UObject): ...


class PawnAction(unreal.UObject):
    ChildAction: PawnAction
    ParentAction: PawnAction
    OwnerComponent: PawnActionsComponent
    Instigator: unreal.UObject
    BrainComp: BrainComponent
    bAllowNewSameClassInstance: bool
    bReplaceActiveSameClassInstance: bool
    bShouldPauseMovement: bool
    bAlwaysNotifyOnFinished: bool

    def GetActionPriority(self) -> int: ...
    def Finish(self, WithResult: int): ...
    def CreateActionInstance(
        self, WorldContextObject: unreal.UObject, ActionClass: unreal.UClass
    ) -> PawnAction: ...


class PawnAction_BlueprintBase(PawnAction):

    def ActionTick(self, ControlledPawn: engine.Pawn, DeltaSeconds: float): ...
    def ActionStart(self, ControlledPawn: engine.Pawn): ...
    def ActionResume(self, ControlledPawn: engine.Pawn): ...
    def ActionPause(self, ControlledPawn: engine.Pawn): ...
    def ActionFinished(self, ControlledPawn: engine.Pawn, WithResult: int): ...


class PawnAction_Move(PawnAction):
    GoalActor: engine.Actor
    GoalLocation: core_uobject.Vector
    AcceptableRadius: float
    FilterClass: unreal.UClass
    bAllowStrafe: bool
    bFinishOnOverlap: bool
    bUsePathfinding: bool
    bAllowPartialPath: bool
    bProjectGoalToNavigation: bool
    bUpdatePathToGoal: bool
    bAbortChildActionOnPathChange: bool


class PawnAction_Repeat(PawnAction):
    ActionToRepeat: PawnAction
    RecentActionCopy: PawnAction
    ChildFailureHandlingMode: int


class PawnAction_Sequence(PawnAction):
    ActionSequence: unreal.WrappedArray[PawnAction]
    ChildFailureHandlingMode: int
    RecentActionCopy: PawnAction


class PawnAction_Wait(PawnAction):
    TimeToWait: float


class PawnActionsComponent(engine.ActorComponent):
    ControlledPawn: engine.Pawn
    ActionStacks: unreal.WrappedArray[PawnActionStack]
    ActionEvents: unreal.WrappedArray[PawnActionEvent]
    CurrentAction: PawnAction

    def K2_PushAction(
        self, NewAction: PawnAction, Priority: int, Instigator: unreal.UObject
    ) -> bool: ...
    def K2_PerformAction(
        self, Pawn: engine.Pawn, Action: PawnAction, Priority: int
    ) -> bool: ...
    def K2_ForceAbortAction(self, ActionToAbort: PawnAction) -> int: ...
    def K2_AbortAction(self, ActionToAbort: PawnAction) -> int: ...


class PawnSensingComponent(engine.ActorComponent):
    HearingThreshold: float
    LOSHearingThreshold: float
    SightRadius: float
    SensingInterval: float
    HearingMaxSoundAge: float
    bEnableSensingUpdates: bool
    bOnlySensePlayers: bool
    bSeePawns: bool
    bHearNoises: bool
    OnSeePawn: Any
    OnHearNoise: Any
    PeripheralVisionAngle: float
    PeripheralVisionCosine: float

    def SetSensingUpdatesEnabled(self, bEnabled: bool): ...
    def SetSensingInterval(self, NewSensingInterval: float): ...
    def SetPeripheralVisionAngle(self, NewPeripheralVisionAngle: float): ...
    def SeePawnDelegate__DelegateSignature(self, Pawn: engine.Pawn): ...
    def HearNoiseDelegate__DelegateSignature(
        self, Instigator: engine.Pawn, Location: core_uobject.Vector, Volume: float
    ): ...
    def GetPeripheralVisionCosine(self) -> float: ...
    def GetPeripheralVisionAngle(self) -> float: ...


class VisualLoggerExtension(unreal.UObject): ...


class AIRequestID:
    RequestID: int


class AIStimulus:
    Age: float
    ExpirationAge: float
    Strength: float
    StimulusLocation: core_uobject.Vector
    ReceiverLocation: core_uobject.Vector
    Tag: str
    bSuccessfullySensed: bool
    SourceLocation: core_uobject.Vector


class EnvQueryResult:
    ItemType: unreal.UClass
    OptionIndex: int
    QueryID: int


class AIDataProviderValue:
    CachedProperty: core_uobject.Property
    DataBinding: AIDataProvider
    DataField: str


class AIDataProviderTypedValue(AIDataProviderValue):
    PropertyType: unreal.UClass


class AIDataProviderFloatValue(AIDataProviderTypedValue):
    DefaultValue: float


class EnvDirection:
    LineFrom: unreal.UClass
    LineTo: unreal.UClass
    Rotation: unreal.UClass
    DirMode: int


class EnvTraceData:
    VersionNum: int
    NavigationFilter: unreal.UClass
    ProjectDown: float
    ProjectUp: float
    ExtentX: float
    ExtentY: float
    ExtentZ: float
    PostProjectionVerticalOffset: float
    TraceChannel: int
    SerializedChannel: int
    TraceShape: int
    TraceMode: int
    bTraceComplex: bool
    bOnlyBlockingHits: bool
    bCanTraceOnNavMesh: bool
    bCanTraceOnGeometry: bool
    bCanDisableTrace: bool
    bCanProjectDown: bool
    bCanTraceOnFlight: bool


class AIDataProviderBoolValue(AIDataProviderTypedValue):
    DefaultValue: bool


class AIDataProviderIntValue(AIDataProviderTypedValue):
    DefaultValue: int


class AIDataProviderStructValue(AIDataProviderValue): ...


class ActorPerceptionBlueprintInfo:
    Target: engine.Actor
    LastSensedStimuli: unreal.WrappedArray[AIStimulus]
    bIsHostile: bool


class AISenseAffiliationFilter:
    bDetectEnemies: bool
    bDetectNeutrals: bool
    bDetectFriendlies: bool


class SenseMetadata: ...


class AIDamageEvent:
    Amount: float
    Location: core_uobject.Vector
    HitLocation: core_uobject.Vector
    DamagedActor: engine.Actor
    Instigator: engine.Actor


class AINoiseEvent:
    NoiseLocation: core_uobject.Vector
    Loudness: float
    MaxRange: float
    Instigator: engine.Actor
    Tag: str


class AIPredictionEvent:
    Requestor: engine.Actor
    PredictedActor: engine.Actor


class AISightEvent:
    SeenActor: engine.Actor
    Observer: engine.Actor


class AITeamStimulusEvent:
    Broadcaster: engine.Actor
    Enemy: engine.Actor


class AITouchEvent:
    TouchReceiver: engine.Actor
    OtherActor: engine.Actor


class AIMoveRequest:
    GoalActor: engine.Actor


class BehaviorTreeTemplateInfo:
    Asset: BehaviorTree
    Template: BTCompositeNode


class BlackboardKeySelector:
    AllowedTypes: unreal.WrappedArray[BlackboardKeyType]
    SelectedKeyName: str
    SelectedKeyType: unreal.UClass
    SelectedKeyID: int
    bNoneIsAllowedValue: bool


class BlackboardEntry:
    EntryName: str
    KeyType: BlackboardKeyType
    bInstanceSynced: bool


class BTCompositeChild:
    ChildComposite: BTCompositeNode
    ChildTask: BTTaskNode
    Decorators: unreal.WrappedArray[BTDecorator]
    DecoratorOps: unreal.WrappedArray[BTDecoratorLogic]


class BTDecoratorLogic:
    Operation: int
    Number: int


class CrowdAvoidanceSamplingPattern:
    Angles: unreal.WrappedArray[float]
    Radii: unreal.WrappedArray[float]


class CrowdAvoidanceConfig:
    VelocityBias: float
    DesiredVelocityWeight: float
    CurrentVelocityWeight: float
    SideBiasWeight: float
    ImpactTimeWeight: float
    ImpactTimeRange: float
    CustomPatternIdx: int
    AdaptiveDivisions: int
    AdaptiveRings: int
    AdaptiveDepth: int


class EnvQueryInstanceCache:
    Template: EnvQuery


class EnvQueryRequest:
    QueryTemplate: EnvQuery
    Owner: unreal.UObject
    World: engine.World


class EQSParametrizedQueryExecutionRequest:
    QueryTemplate: EnvQuery
    QueryConfig: unreal.WrappedArray[AIDynamicParam]
    EQSQueryBlackboardKey: BlackboardKeySelector
    RunMode: int
    bUseBBKeyForQueryTemplate: bool


class AIDynamicParam:
    ParamName: str
    ParamType: EAIParamType
    Value: float
    BBKey: BlackboardKeySelector


class EnvOverlapData:
    ExtentX: float
    ExtentY: float
    ExtentZ: float
    ShapeOffset: core_uobject.Vector
    OverlapChannel: int
    OverlapShape: int
    bOnlyBlockingHits: bool
    bOverlapComplex: bool


class EnvNamedValue:
    ParamName: str
    ParamType: EAIParamType
    Value: float


class GenericTeamId:
    TeamID: int


class PawnActionStack:
    TopAction: PawnAction


class PawnActionEvent:
    Action: PawnAction


class Default__AISenseBlueprintListener: ...


class EPathFollowingResult(enum.Enum):
    Blocked = 0
    Skipped_DEPRECATED = 1
    OffPath = 2


class EEnvQueryStatus(enum.Enum):
    Success = 0
    Failed = 1
    OwnerLost = 2


class EPathFollowingStatus(enum.Enum):
    Paused = 0
    Waiting = 1
    EPathFollowingStatus_MAX = 2


class EPathFollowingRequestResult(enum.Enum):
    AlreadyAtGoal = 0
    RequestSuccessful = 1


class ETeamAttitude(enum.Enum):
    Neutral = 0
    Hostile = 1


class EAISenseNotifyType(enum.Enum):
    EAISenseNotifyType_MAX = 0
    OnPerceptionChange = 1


class EAITaskPriority(enum.Enum):
    Low = 0


class EGenericAICheck(enum.Enum):
    GreaterOrEqual = 0
    Equal = 1
    LessOrEqual = 2


class EAILockSource(enum.Enum):
    MAX = 0
    Logic = 1
    Script = 2


class EAIRequestPriority(enum.Enum):
    Logic = 0
    HardScript = 1
    Ultimate = 2


class EPawnActionEventType(enum.Enum):
    FailedToStart = 0
    InstantAbort = 1
    FinishedExecution = 2


class EPawnActionResult(enum.Enum):
    InProgress = 0
    Aborted = 1
    Success = 2


class EPawnActionAbortState(enum.Enum):
    NotBeingAborted = 0
    MarkPendingAbort = 1
    AbortDone = 2


class FAIDistanceType(enum.Enum):
    Distance2D = 0
    DistanceZ = 1


class EAIOptionFlag(enum.Enum):
    Enable = 0
    Disable = 1


class EBTFlowAbortMode(enum.Enum):
    EBTFlowAbortMode_MAX = 0
    LowerPriority = 1
    Self = 2


class EBTNodeResult(enum.Enum):
    EBTNodeResult_MAX = 0
    Failed = 1
    Aborted = 2


class ETextKeyOperation(enum.Enum):
    NotEqual = 0
    Contain = 1
    ETextKeyOperation_MAX = 2


class EArithmeticKeyOperation(enum.Enum):
    NotEqual = 0
    Less = 1
    Greater = 2


class EBasicKeyOperation(enum.Enum):
    EBasicKeyOperation_MAX = 0
    NotSet = 1


class EBTParallelMode(enum.Enum):
    EBTParallelMode_MAX = 0
    WaitForBackground = 1


class EBTDecoratorLogic(enum.Enum):
    Test = 0
    And = 1
    Not = 2


class EBTChildIndex(enum.Enum):
    EBTChildIndex_MAX = 0
    TaskNode = 1


class EBTBlackboardRestart(enum.Enum):
    ResultChange = 0
    EBTBlackboardRestart_MAX = 1


class EBlackBoardEntryComparison(enum.Enum):
    NotEqual = 0
    EBlackBoardEntryComparison_MAX = 1


class EPathExistanceQueryType(enum.Enum):
    HierarchicalQuery = 0
    RegularPathFinding = 1


class EEqsTraceDrawMode(enum.Enum):
    DrawFailed = 0
    DrawSucceeded = 1
    Count = 2


class EPointOnCircleSpacingMethod(enum.Enum):
    ByNumberOfPoints = 0
    EPointOnCircleSpacingMethod_MAX = 1


class EEQSNormalizationType(enum.Enum):
    RelativeToScores = 0
    EEQSNormalizationType_MAX = 1


class EEnvTestDistance(enum.Enum):
    EEnvTestDistance_MAX = 0
    DistanceZ = 1
    Distance2D = 2


class EEnvTestDot(enum.Enum):
    Dot2D = 0
    EEnvTestDot_MAX = 1


class EEnvTestPathfinding(enum.Enum):
    PathCost = 0
    PathLength = 1


class EEnvQueryTestClamping(enum.Enum):
    SpecifiedValue = 0
    FilterThreshold = 1


class EEnvDirection(enum.Enum):
    Rotation = 0
    EEnvDirection_MAX = 1


class EEnvOverlapShape(enum.Enum):
    Sphere = 0
    Capsule = 1


class EEnvTraceShape(enum.Enum):
    Box = 0
    Sphere = 1
    EEnvTraceShape_MAX = 2


class EEnvQueryTrace(enum.Enum):
    NavigationOverLedges = 0
    Navigation = 1
    Geometry = 2


class EAIParamType(enum.Enum):
    Bool = 0
    Int = 1


class EEnvQueryParam(enum.Enum):
    Bool = 0
    Int = 1


class EEnvQueryRunMode(enum.Enum):
    RandomBest5Pct = 0
    EEnvQueryRunMode_MAX = 1
    RandomBest25Pct = 2


class EEnvTestScoreOperator(enum.Enum):
    MinScore = 0
    MaxScore = 1


class EEnvTestFilterOperator(enum.Enum):
    EEnvTestFilterOperator_MAX = 0
    AnyPass = 1


class EEnvTestCost(enum.Enum):
    Medium = 0
    High = 1


class EEnvTestWeight(enum.Enum):
    Inverse = 0
    Square = 1
    Constant = 2


class EEnvTestScoreEquation(enum.Enum):
    InverseLinear = 0
    Square = 1
    Constant = 2


class EEnvTestFilterType(enum.Enum):
    Maximum = 0
    Range = 1
    EEnvTestFilterType_MAX = 2


class EEnvTestPurpose(enum.Enum):
    Score = 0
    FilterAndScore = 1


class EEnvQueryHightlightMode(enum.Enum):
    Best25Pct = 0
    Best5Pct = 1


class EPathFollowingAction(enum.Enum):
    DirectMove = 0
    NoMove = 1
    PathToGoal = 2


class EPawnActionFailHandling(enum.Enum):
    IgnoreFailure = 0
    EPawnActionFailHandling_MAX = 1


class EPawnSubActionTriggeringPolicy(enum.Enum):
    ReuseInstances = 0
    EPawnSubActionTriggeringPolicy_MAX = 1


class EPawnActionMoveMode(enum.Enum):
    StraightLine = 0
    EPawnActionMoveMode_MAX = 1

from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import input_core
from . import slate_core
from . import slate
from . import packet_handler
from . import clothing_system_runtime_interface
from . import audio_platform_configuration



class ActorComponent(unreal.UObject):
    PrimaryComponentTick: ActorComponentTickFunction
    ComponentTags: unreal.WrappedArray[str]
    ComponentTickOptimizationData: TickOptimizationData
    AssetUserData: unreal.WrappedArray[AssetUserData]
    bReplicates: bool
    bNetAddressable: bool
    bExcludeFromReplicationProxy: bool
    bAutoActivate: bool
    bIsActive: bool
    bEditableWhenInherited: bool
    bSkipPropertyGeneration: bool
    bCanEverAffectNavigation: bool
    bIsEditorOnly: bool
    CreationMethod: EComponentCreationMethod
    OwningSceneCapture: SceneCaptureComponent
    UCSModifiedProperties: unreal.WrappedArray[SimpleMemberReference]
    ArchetypeOverride: ActorComponent
    EventConditionsReference: unreal.WrappedArray[unreal.UObject]
    def ToggleActive(self): ...
    def SetTickGroup(self, NewTickGroup: int): ...
    def SetTickableWhenPaused(self, bTickableWhenPaused: bool): ...
    def SetOwningSceneCapture(self, InOwningSceneCapture: SceneCaptureComponent): ...
    def SetIsReplicated(self, ShouldReplicate: bool): ...
    def SetComponentTickInterval(self, TickInterval: float): ...
    def SetComponentTickEnabled(self, bEnabled: bool): ...
    def SetAutoActivate(self, bNewAutoActivate: bool): ...
    def SetActive(self, bNewActive: bool, bReset: bool): ...
    def RemoveTickPrerequisiteComponent(self, PrerequisiteComponent: ActorComponent): ...
    def RemoveTickPrerequisiteActor(self, PrerequisiteActor: Actor): ...
    def ReceiveTick(self, DeltaSeconds: float): ...
    def ReceiveEndPlay(self, EndPlayReason: int): ...
    def ReceiveBeginPlay(self): ...
    def OnRep_IsActive(self): ...
    def MarkNetDirty(self): ...
    def K2_DestroyComponent(self, Object: unreal.UObject): ...
    def IsComponentTickEnabled(self, ReturnValue: bool) -> bool: ...
    def IsBeingDestroyed(self, ReturnValue: bool) -> bool: ...
    def IsActive(self, ReturnValue: bool) -> bool: ...
    def GetOwningSceneCapture(self, ReturnValue: SceneCaptureComponent) -> SceneCaptureComponent: ...
    def GetOwner(self, ReturnValue: Actor) -> Actor: ...
    def GetComponentTickInterval(self, ReturnValue: float) -> float: ...
    def Deactivate(self): ...
    def ComponentHasTag(self, Tag: str, ReturnValue: bool) -> bool: ...
    def AddTickPrerequisiteComponent(self, PrerequisiteComponent: ActorComponent): ...
    def AddTickPrerequisiteActor(self, PrerequisiteActor: Actor): ...
    def Activate(self, bReset: bool): ...


class BlueprintFunctionLibrary(unreal.UObject): ...


class Actor(unreal.UObject):
    PrimaryActorTick: ActorTickFunction
    bHidden: bool
    CullDistanceLODGroup: str
    bNetTemporary: bool
    bNetStartup: bool
    bOnlyRelevantToOwner: bool
    bAlwaysRelevant: bool
    bReplicateMovement: bool
    bTearOff: bool
    bExchangedRoles: bool
    bNetLoadOnClient: bool
    bNetUseOwnerRelevancy: bool
    bRelevantForNetworkReplays: bool
    bReplayRewindable: bool
    bAllowTickBeforeBeginPlay: bool
    bAutoDestroyWhenFinished: bool
    bBlockInput: bool
    bCanBeDamaged: bool
    bCollideWhenPlacing: bool
    bFindCameraComponentWhenViewTarget: bool
    bGenerateOverlapEventsDuringLevelStreaming: bool
    bIgnoresOriginShifting: bool
    bEnableAutoLODGeneration: bool
    bIsEditorOnlyActor: bool
    bActorSeamlessTraveled: bool
    bReplicates: bool
    bCanBeInCluster: bool
    bAllowReceiveTickEventOnDedicatedServer: bool
    bActorEnableCollision: bool
    bActorIsBeingDestroyed: bool
    RemoteRole: int
    ReplicatedMovement: RepMovement
    InitialLifeSpan: float
    CustomTimeDilation: float
    AttachmentReplication: RepAttachment
    Owner: Actor
    NetDriverName: str
    Role: int
    NetDormancy: int
    SpawnCollisionHandlingMethod: ESpawnActorCollisionHandlingMethod
    AutoReceiveInput: int
    InputPriority: int
    InputComponent: InputComponent
    NetCullDistanceSquared: float
    NetTag: int
    NetUpdateFrequency: float
    MinNetUpdateFrequency: float
    NetPriority: float
    Instigator: Pawn
    Children: unreal.WrappedArray[Actor]
    RootComponent: SceneComponent
    ControllingMatineeActors: unreal.WrappedArray[MatineeActor]
    Layers: unreal.WrappedArray[str]
    ParentComponent: ChildActorComponent
    Tags: unreal.WrappedArray[str]
    InstanceComponents: unreal.WrappedArray[ActorComponent]
    BlueprintCreatedComponents: unreal.WrappedArray[ActorComponent]
    EventConditionsReference: unreal.WrappedArray[unreal.UObject]
    bDebugTickOptimizations: bool
    bCheckForTickOptimizations: bool
    ActorTickOptimizationData: TickOptimizationData
    ArchetypeOverride: unreal.UObject
    bHiddenOnSpawn: bool
    bReplicateHidden: bool
    bDoNotWarnWhenDeletingWithSoftRef: bool
    bUseLagCompensation: bool
    bCollideWithLagCompensation: bool
    def WasRecentlyRendered(self, Tolerance: float, ReturnValue: bool) -> bool: ...
    def UserConstructionScript(self): ...
    def TearOff(self): ...
    def SnapRootComponentTo(self, InParentActor: Actor, InSocketName: str): ...
    def SetTickGroup(self, NewTickGroup: int): ...
    def SetTickableWhenPaused(self, bTickableWhenPaused: bool): ...
    def SetReplicates(self, bInReplicates: bool): ...
    def SetReplicateMovement(self, bInReplicateMovement: bool): ...
    def SetOwner(self, NewOwner: Actor): ...
    def SetOnlyRelevantToOwner(self, bNewOnlyRelevantToOwner: bool): ...
    def SetNetUseOwnerRelevancy(self, bNewNetUseOwnerRelevancy: bool): ...
    def SetNetUpdateFrequency(self, NewFrequency: float, NewMinFrequency: float): ...
    def SetNetDormancy(self, NewDormancy: int): ...
    def SetLifeSpan(self, InLifespan: float): ...
    def SetAlwaysRelevant(self, bNewAlwaysRelevant: bool): ...
    def SetActorTickInterval(self, TickInterval: float): ...
    def SetActorTickEnabled(self, bEnabled: bool): ...
    def SetActorScale3D(self, NewScale3D: core_uobject.Vector): ...
    def SetActorRelativeScale3D(self, NewRelativeScale: core_uobject.Vector): ...
    def SetActorHiddenInGame(self, bNewHidden: bool): ...
    def SetActorEnableCollision(self, bNewActorEnableCollision: bool): ...
    def RemoveTickPrerequisiteComponent(self, PrerequisiteComponent: ActorComponent): ...
    def RemoveTickPrerequisiteActor(self, PrerequisiteActor: Actor): ...
    def ReceiveTick(self, DeltaSeconds: float): ...
    def ReceiveRadialDamage(self, DamageReceived: float, DamageType: DamageType, Origin: core_uobject.Vector, HitInfo: HitResult, InstigatedBy: Controller, DamageCauser: Actor): ...
    def ReceivePointDamage(self, Damage: float, DamageType: DamageType, HitLocation: core_uobject.Vector, HitNormal: core_uobject.Vector, HitComponent: PrimitiveComponent, BoneName: str, ShotFromDirection: core_uobject.Vector, InstigatedBy: Controller, DamageCauser: Actor, HitInfo: HitResult): ...
    def ReceiveHit(self, MyComp: PrimitiveComponent, Other: Actor, OtherComp: PrimitiveComponent, bSelfMoved: bool, HitLocation: core_uobject.Vector, HitNormal: core_uobject.Vector, NormalImpulse: core_uobject.Vector, Hit: HitResult): ...
    def ReceiveEndPlay(self, EndPlayReason: int): ...
    def ReceiveDestroyed(self): ...
    def ReceiveBeginPlay(self): ...
    def ReceiveAnyDamage(self, Damage: float, DamageType: DamageType, InstigatedBy: Controller, DamageCauser: Actor): ...
    def ReceiveActorOnReleased(self, ButtonReleased: input_core.Key): ...
    def ReceiveActorOnInputTouchLeave(self, FingerIndex: int): ...
    def ReceiveActorOnInputTouchEnter(self, FingerIndex: int): ...
    def ReceiveActorOnInputTouchEnd(self, FingerIndex: int): ...
    def ReceiveActorOnInputTouchBegin(self, FingerIndex: int): ...
    def ReceiveActorOnClicked(self, ButtonPressed: input_core.Key): ...
    def ReceiveActorEndOverlap(self, OtherActor: Actor): ...
    def ReceiveActorEndCursorOver(self): ...
    def ReceiveActorBeginOverlap(self, OtherActor: Actor): ...
    def ReceiveActorBeginCursorOver(self): ...
    def PrestreamTextures(self, Seconds: float, bEnableStreaming: bool, CinematicTextureGroups: int): ...
    def OnRep_ReplicateMovement(self): ...
    def OnRep_ReplicatedMovement(self): ...
    def OnRep_Owner(self): ...
    def OnRep_Instigator(self): ...
    def OnRep_AttachmentReplication(self): ...
    def MakeNoise(self, Loudness: float, NoiseInstigator: Pawn, NoiseLocation: core_uobject.Vector, MaxRange: float, Tag: str): ...
    def MakeMIDForMaterial(self, Parent: MaterialInterface, ReturnValue: MaterialInstanceDynamic) -> MaterialInstanceDynamic: ...
    def K2_TeleportTo(self, DestLocation: core_uobject.Vector, DestRotation: core_uobject.Rotator, ReturnValue: bool) -> bool: ...
    def K2_SetActorTransform(self, NewTransform: core_uobject.Transform, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool, ReturnValue: bool) -> bool: ...
    def K2_SetActorRotation(self, NewRotation: core_uobject.Rotator, bTeleportPhysics: bool, ReturnValue: bool) -> bool: ...
    def K2_SetActorRelativeTransform(self, NewRelativeTransform: core_uobject.Transform, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def K2_SetActorRelativeRotation(self, NewRelativeRotation: core_uobject.Rotator, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def K2_SetActorRelativeLocation(self, NewRelativeLocation: core_uobject.Vector, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def K2_SetActorLocationAndRotation(self, NewLocation: core_uobject.Vector, NewRotation: core_uobject.Rotator, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool, ReturnValue: bool) -> bool: ...
    def K2_SetActorLocation(self, NewLocation: core_uobject.Vector, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool, ReturnValue: bool) -> bool: ...
    def K2_OnReset(self): ...
    def K2_OnEndViewTarget(self, pc: PlayerController): ...
    def K2_OnBecomeViewTarget(self, pc: PlayerController): ...
    def K2_GetRootComponent(self, ReturnValue: SceneComponent) -> SceneComponent: ...
    def K2_GetActorRotation(self, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def K2_GetActorLocation(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def K2_DetachFromActor(self, LocationRule: EDetachmentRule, RotationRule: EDetachmentRule, ScaleRule: EDetachmentRule): ...
    def K2_DestroyComponent(self, Component: ActorComponent): ...
    def K2_DestroyActor_DEPRECATED(self): ...
    def K2_AttachToComponent(self, Parent: SceneComponent, SocketName: str, LocationRule: EAttachmentRule, RotationRule: EAttachmentRule, ScaleRule: EAttachmentRule, bWeldSimulatedBodies: bool): ...
    def K2_AttachToActor(self, ParentActor: Actor, SocketName: str, LocationRule: EAttachmentRule, RotationRule: EAttachmentRule, ScaleRule: EAttachmentRule, bWeldSimulatedBodies: bool): ...
    def K2_AttachRootComponentToActor(self, InParentActor: Actor, InSocketName: str, AttachLocationType: int, bWeldSimulatedBodies: bool): ...
    def K2_AttachRootComponentTo(self, InParent: SceneComponent, InSocketName: str, AttachLocationType: int, bWeldSimulatedBodies: bool): ...
    def K2_AddActorWorldTransform(self, DeltaTransform: core_uobject.Transform, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def K2_AddActorWorldRotation(self, DeltaRotation: core_uobject.Rotator, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def K2_AddActorWorldOffset(self, DeltaLocation: core_uobject.Vector, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def K2_AddActorLocalTransform(self, NewTransform: core_uobject.Transform, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def K2_AddActorLocalRotation(self, DeltaRotation: core_uobject.Rotator, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def K2_AddActorLocalOffset(self, DeltaLocation: core_uobject.Vector, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def IsOverlappingActor(self, Other: Actor, ReturnValue: bool) -> bool: ...
    def IsChildActor(self, ReturnValue: bool) -> bool: ...
    def IsActorTickEnabled(self, ReturnValue: bool) -> bool: ...
    def IsActorBeingDestroyed(self, ReturnValue: bool) -> bool: ...
    def HasAuthority(self, ReturnValue: bool) -> bool: ...
    def GetVerticalDistanceTo(self, OtherActor: Actor, ReturnValue: float) -> float: ...
    def GetVelocity(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetTransform(self, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def GetTickableWhenPaused(self, ReturnValue: bool) -> bool: ...
    def GetSquaredDistanceTo(self, OtherActor: Actor, ReturnValue: float) -> float: ...
    def GetRemoteRole(self, ReturnValue: int) -> int: ...
    def GetParentComponent(self, ReturnValue: ChildActorComponent) -> ChildActorComponent: ...
    def GetParentActor(self, ReturnValue: Actor) -> Actor: ...
    def GetOwner(self, ReturnValue: Actor) -> Actor: ...
    def GetOverlappingComponents(self, OverlappingComponents: unreal.WrappedArray[PrimitiveComponent]): ...
    def GetOverlappingActors(self, OverlappingActors: unreal.WrappedArray[Actor], ClassFilter: unreal.UClass): ...
    def GetLocalRole(self, ReturnValue: int) -> int: ...
    def GetLifeSpan(self, ReturnValue: float) -> float: ...
    def GetInstigatorController(self, ReturnValue: Controller) -> Controller: ...
    def GetInstigator(self, ReturnValue: Pawn) -> Pawn: ...
    def GetInputVectorAxisValue(self, InputAxisKey: input_core.Key, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetInputAxisValue(self, InputAxisName: str, ReturnValue: float) -> float: ...
    def GetInputAxisKeyValue(self, InputAxisKey: input_core.Key, ReturnValue: float) -> float: ...
    def GetHorizontalDotProductTo(self, OtherActor: Actor, ReturnValue: float) -> float: ...
    def GetHorizontalDistanceTo(self, OtherActor: Actor, ReturnValue: float) -> float: ...
    def GetGameTimeSinceCreation(self, ReturnValue: float) -> float: ...
    def GetDotProductTo(self, OtherActor: Actor, ReturnValue: float) -> float: ...
    def GetDistanceTo(self, OtherActor: Actor, ReturnValue: float) -> float: ...
    def GetComponentsByTag(self, ComponentClass: unreal.UClass, Tag: str, ReturnValue: unreal.WrappedArray[ActorComponent]) -> unreal.WrappedArray[ActorComponent]: ...
    def GetComponentsByClass(self, ComponentClass: unreal.UClass, ReturnValue: unreal.WrappedArray[ActorComponent]) -> unreal.WrappedArray[ActorComponent]: ...
    def GetComponentByTag(self, ComponentClass: unreal.UClass, Tag: str, ReturnValue: ActorComponent) -> ActorComponent: ...
    def GetComponentByClass(self, ComponentClass: unreal.UClass, ReturnValue: ActorComponent) -> ActorComponent: ...
    def GetAttachParentSocketName(self, ReturnValue: str) -> str: ...
    def GetAttachParentActor(self, ReturnValue: Actor) -> Actor: ...
    def GetAttachedActors(self, OutActors: unreal.WrappedArray[Actor]): ...
    def GetAssociatedVehicle(self, ReturnValue: Pawn) -> Pawn: ...
    def GetAssociatedPlayerState(self, ReturnValue: PlayerState) -> PlayerState: ...
    def GetAssociatedPlayerController(self, ReturnValue: PlayerController) -> PlayerController: ...
    def GetAssociatedPawn(self, ReturnValue: Pawn) -> Pawn: ...
    def GetAssociatedController(self, ReturnValue: Controller) -> Controller: ...
    def GetAssociatedCharacter(self, ReturnValue: Character) -> Character: ...
    def GetAllChildActors(self, ChildActors: unreal.WrappedArray[Actor], bIncludeDescendants: bool): ...
    def GetActorUpVector(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetActorTimeDilation(self, ReturnValue: float) -> float: ...
    def GetActorTickInterval(self, ReturnValue: float) -> float: ...
    def GetActorScale3D(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetActorRightVector(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetActorRelativeScale3D(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetActorForwardVector(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetActorEyesViewPoint(self, OutLocation: core_uobject.Vector, OutRotation: core_uobject.Rotator): ...
    def GetActorEnableCollision(self, ReturnValue: bool) -> bool: ...
    def GetActorBounds(self, bOnlyCollidingComponents: bool, Origin: core_uobject.Vector, BoxExtent: core_uobject.Vector): ...
    def GetActorAimViewPoint(self, OutLocation: core_uobject.Vector, OutRotation: core_uobject.Rotator): ...
    def GbxDestroyActor(self, bDestroyImmediately: bool): ...
    def ForceNetUpdate(self): ...
    def FlushNetDormancy(self): ...
    def FindAttachComponent(self, SocketName: str, bForegroundLayer: bool, ReturnValue: SceneComponent) -> SceneComponent: ...
    def EnableInput(self, PlayerController: PlayerController): ...
    def DisableInput(self, PlayerController: PlayerController): ...
    def DetachRootComponentFromParent(self, bMaintainWorldPosition: bool): ...
    def AddTickPrerequisiteComponent(self, PrerequisiteComponent: ActorComponent): ...
    def AddTickPrerequisiteActor(self, PrerequisiteActor: Actor): ...
    def AddComponent(self, TemplateName: str, bManualAttachment: bool, RelativeTransform: core_uobject.Transform, ComponentTemplateContext: unreal.UObject, ReturnValue: ActorComponent) -> ActorComponent: ...
    def ActorPostBeginPlaySignature__DelegateSignature(self): ...
    def ActorHasTag(self, Tag: str, ReturnValue: bool) -> bool: ...


class HUD(Actor):
    PlayerOwner: PlayerController
    bLostFocusPaused: bool
    bShowHUD: bool
    bShowDebugInfo: bool
    CurrentTargetIndex: int
    bShowHitBoxDebugInfo: bool
    bShowOverlays: bool
    bEnableDebugTextShadow: bool
    PostRenderedActors: unreal.WrappedArray[Actor]
    DebugDisplay: unreal.WrappedArray[str]
    ToggledDebugCategories: unreal.WrappedArray[str]
    Canvas: Canvas
    DebugCanvas: Canvas
    DebugTextList: unreal.WrappedArray[DebugTextInfo]
    ShowDebugTargetDesiredClass: unreal.UClass
    ShowDebugTargetActor: Actor
    OverrideDebugTarget: Actor
    def ToggleOverrideDebugTarget(self): ...
    def ShowHUD(self, WantsVisible: int): ...
    def ShowDebugToggleSubCategory(self, Category: str): ...
    def ShowDebugForReticleTargetToggle(self, DesiredClass: unreal.UClass): ...
    def ShowDebugBonesReset(self): ...
    def ShowDebugBonesRemoveChildren(self, Arguments: str): ...
    def ShowDebugBonesAdd(self, Arguments: str): ...
    def ShowDebug(self, DebugType: str): ...
    def RemoveDebugText(self, SrcActor: Actor, bLeaveDurationText: bool): ...
    def RemoveAllDebugStrings(self): ...
    def ReceiveHitBoxRelease(self, BoxName: str): ...
    def ReceiveHitBoxEndCursorOver(self, BoxName: str): ...
    def ReceiveHitBoxClick(self, BoxName: str): ...
    def ReceiveHitBoxBeginCursorOver(self, BoxName: str): ...
    def ReceiveDrawHUD(self, SizeX: int, SizeY: int): ...
    def Project(self, Location: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def PreviousDebugTarget(self): ...
    def NextDebugTarget(self): ...
    def GetTextSize(self, Text: str, OutWidth: float, OutHeight: float, Font: Font, Scale: float): ...
    def GetOwningPlayerController(self, ReturnValue: PlayerController) -> PlayerController: ...
    def GetOwningPawn(self, ReturnValue: Pawn) -> Pawn: ...
    def GetActorsInSelectionRectangle(self, ClassFilter: unreal.UClass, FirstPoint: core_uobject.Vector2D, SecondPoint: core_uobject.Vector2D, OutActors: unreal.WrappedArray[Actor], bIncludeNonCollidingComponents: bool, bActorMustBeFullyEnclosed: bool): ...
    def DrawTextureSimple(self, Texture: Texture, ScreenX: float, ScreenY: float, Scale: float, bScalePosition: bool): ...
    def DrawTexture(self, Texture: Texture, ScreenX: float, ScreenY: float, ScreenW: float, ScreenH: float, TextureU: float, TextureV: float, TextureUWidth: float, TextureVHeight: float, TintColor: core_uobject.LinearColor, BlendMode: int, Scale: float, bScalePosition: bool, Rotation: float, RotPivot: core_uobject.Vector2D): ...
    def DrawText(self, Text: str, TextColor: core_uobject.LinearColor, ScreenX: float, ScreenY: float, Font: Font, Scale: float, bScalePosition: bool): ...
    def DrawRect(self, RectColor: core_uobject.LinearColor, ScreenX: float, ScreenY: float, ScreenW: float, ScreenH: float): ...
    def DrawMaterialSimple(self, Material: MaterialInterface, ScreenX: float, ScreenY: float, ScreenW: float, ScreenH: float, Scale: float, bScalePosition: bool): ...
    def DrawMaterial(self, Material: MaterialInterface, ScreenX: float, ScreenY: float, ScreenW: float, ScreenH: float, MaterialU: float, MaterialV: float, MaterialUWidth: float, MaterialVHeight: float, Scale: float, bScalePosition: bool, Rotation: float, RotPivot: core_uobject.Vector2D): ...
    def DrawLine(self, StartScreenX: float, StartScreenY: float, EndScreenX: float, EndScreenY: float, LineColor: core_uobject.LinearColor, LineThickness: float): ...
    def Deproject(self, ScreenX: float, ScreenY: float, WorldPosition: core_uobject.Vector, WorldDirection: core_uobject.Vector): ...
    def AddHitBox(self, Position: core_uobject.Vector2D, Size: core_uobject.Vector2D, InName: str, bConsumesInput: bool, Priority: int): ...
    def AddDebugText(self, DebugText: str, SrcActor: Actor, Duration: float, Offset: core_uobject.Vector, DesiredOffset: core_uobject.Vector, TextColor: core_uobject.Color, bSkipOverwriteCheck: bool, bAbsoluteLocation: bool, bKeepAttachedToActor: bool, InFont: Font, FontScale: float, bDrawShadow: bool): ...


class Channel(unreal.UObject):
    Connection: NetConnection



class DataAsset(unreal.UObject):
    NativeClass: unreal.UClass



class PrimaryDataAsset(DataAsset): ...


class NetDriver(unreal.UObject):
    NetConnectionClassName: str
    ReplicationDriverClassName: str
    MaxDownloadSize: int
    bClampListenServerTickRate: bool
    NetServerMaxTickRate: int
    MaxNetTickRate: int
    MaxInternetClientRate: int
    MaxClientRate: int
    ServerTravelPause: float
    SpawnPrioritySeconds: float
    RelevantTimeout: float
    KeepAliveTime: float
    InitialConnectTimeout: float
    ConnectionTimeout: float
    LagStateTimeout: float
    TimeoutMultiplierForUnoptimizedBuilds: float
    bNoTimeouts: bool
    ServerConnection: NetConnection
    ClientConnections: unreal.WrappedArray[NetConnection]
    World: World
    WorldPackage: core_uobject.Package
    NetConnectionClass: unreal.UClass
    ReplicationDriverClass: unreal.UClass
    RoleProperty: core_uobject.Property
    RemoteRoleProperty: core_uobject.Property
    NetDriverName: str
    Time: float
    ReplicationDriver: ReplicationDriver



class Player(unreal.UObject):
    PlayerController: PlayerController
    CurrentNetSpeed: int
    ConfiguredInternetSpeed: int
    ConfiguredLanSpeed: int



class NetConnection(Player):
    Children: unreal.WrappedArray[ChildConnection]
    Driver: NetDriver
    PackageMapClass: unreal.UClass
    PackageMap: core_uobject.PackageMap
    OpenChannels: unreal.WrappedArray[Channel]
    SentTemporaries: unreal.WrappedArray[Actor]
    ViewTarget: Actor
    OwningActor: Actor
    MaxPacket: int
    InternalAck: bool
    PlayerId: UniqueNetIdRepl
    LastReceiveTime: float
    ChannelsToTick: unreal.WrappedArray[Channel]



class OnlineEngineInterface(unreal.UObject): ...


class DeveloperSettings(unreal.UObject): ...


class OnlineSession(unreal.UObject): ...


class SceneComponent(ActorComponent):
    PhysicsVolume: unreal.WrappedArray[PhysicsVolume]
    AttachParent: SceneComponent
    AttachSocketName: str
    AttachChildren: unreal.WrappedArray[SceneComponent]
    ClientAttachedChildren: unreal.WrappedArray[SceneComponent]
    RelativeLocation: core_uobject.Vector
    RelativeRotation: core_uobject.Rotator
    RelativeScale3D: core_uobject.Vector
    ComponentVelocity: core_uobject.Vector
    bComponentToWorldUpdated: bool
    bAbsoluteLocation: bool
    bAbsoluteRotation: bool
    bAbsoluteScale: bool
    bVisible: bool
    bHiddenInGame: bool
    bShouldUpdatePhysicsVolume: bool
    bBoundsChangeTriggersStreamingDataRebuild: bool
    bUseAttachParentBound: bool
    bAbsoluteTranslation: bool
    Mobility: int
    DetailMode: int
    def ToggleVisibility(self, bPropagateToChildren: bool): ...
    def SnapTo(self, InParent: SceneComponent, InSocketName: str, ReturnValue: bool) -> bool: ...
    def SetWorldScale3D(self, NewScale: core_uobject.Vector): ...
    def SetVisibility(self, bNewVisibility: bool, bPropagateToChildren: bool): ...
    def SetShouldUpdatePhysicsVolume(self, bInShouldUpdatePhysicsVolume: bool): ...
    def SetRelativeScale3D(self, NewScale3D: core_uobject.Vector): ...
    def SetHiddenInGame(self, NewHidden: bool, bPropagateToChildren: bool): ...
    def SetAbsolute(self, bNewAbsoluteLocation: bool, bNewAbsoluteRotation: bool, bNewAbsoluteScale: bool): ...
    def ResetRelativeTransform(self): ...
    def OnRep_Visibility(self, OldValue: bool): ...
    def OnRep_Transform(self): ...
    def OnRep_AttachSocketName(self): ...
    def OnRep_AttachParent(self): ...
    def OnRep_AttachChildren(self): ...
    def K2_SetWorldTransform(self, NewTransform: core_uobject.Transform, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def K2_SetWorldRotation(self, NewRotation: core_uobject.Rotator, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def K2_SetWorldLocationAndRotation(self, NewLocation: core_uobject.Vector, NewRotation: core_uobject.Rotator, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def K2_SetWorldLocation(self, NewLocation: core_uobject.Vector, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def K2_SetRelativeTransform(self, NewTransform: core_uobject.Transform, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def K2_SetRelativeRotation(self, NewRotation: core_uobject.Rotator, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def K2_SetRelativeLocationAndRotation(self, NewLocation: core_uobject.Vector, NewRotation: core_uobject.Rotator, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def K2_SetRelativeLocation(self, NewLocation: core_uobject.Vector, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def K2_GetComponentToWorld(self, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def K2_GetComponentScale(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def K2_GetComponentRotation(self, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def K2_GetComponentLocation(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def K2_DetachFromComponent(self, LocationRule: EDetachmentRule, RotationRule: EDetachmentRule, ScaleRule: EDetachmentRule, bCallModify: bool): ...
    def K2_AttachToComponent(self, Parent: SceneComponent, SocketName: str, LocationRule: EAttachmentRule, RotationRule: EAttachmentRule, ScaleRule: EAttachmentRule, bWeldSimulatedBodies: bool, ReturnValue: bool) -> bool: ...
    def K2_AttachTo(self, InParent: SceneComponent, InSocketName: str, AttachType: int, bWeldSimulatedBodies: bool, ReturnValue: bool) -> bool: ...
    def K2_AddWorldTransform(self, DeltaTransform: core_uobject.Transform, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def K2_AddWorldRotation(self, DeltaRotation: core_uobject.Rotator, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def K2_AddWorldOffset(self, DeltaLocation: core_uobject.Vector, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def K2_AddRelativeRotation(self, DeltaRotation: core_uobject.Rotator, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def K2_AddRelativeLocation(self, DeltaLocation: core_uobject.Vector, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def K2_AddLocalTransform(self, DeltaTransform: core_uobject.Transform, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def K2_AddLocalRotation(self, DeltaRotation: core_uobject.Rotator, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def K2_AddLocalOffset(self, DeltaLocation: core_uobject.Vector, bSweep: bool, SweepHitResult: HitResult, bTeleport: bool): ...
    def IsVisible(self, ReturnValue: bool) -> bool: ...
    def IsSimulatingPhysics(self, BoneName: str, ReturnValue: bool) -> bool: ...
    def IsAnySimulatingPhysics(self, ReturnValue: bool) -> bool: ...
    def GetUpVector(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetSocketTransform(self, InSocketName: str, TransformSpace: int, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def GetSocketRotation(self, InSocketName: str, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def GetSocketQuaternion(self, InSocketName: str, ReturnValue: core_uobject.Quat) -> core_uobject.Quat: ...
    def GetSocketLocation(self, InSocketName: str, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetShouldUpdatePhysicsVolume(self, ReturnValue: bool) -> bool: ...
    def GetRightVector(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetRelativeTransform(self, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def GetPhysicsVolume(self, ReturnValue: PhysicsVolume) -> PhysicsVolume: ...
    def GetParentComponents(self, Parents: unreal.WrappedArray[SceneComponent]): ...
    def GetNumChildrenComponents(self, ReturnValue: int) -> int: ...
    def GetForwardVector(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetComponentVelocity(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetChildrenComponents(self, bIncludeAllDescendants: bool, Children: unreal.WrappedArray[SceneComponent]): ...
    def GetChildComponent(self, ChildIndex: int, ReturnValue: SceneComponent) -> SceneComponent: ...
    def GetAttachSocketName(self, ReturnValue: str) -> str: ...
    def GetAttachParent(self, ReturnValue: SceneComponent) -> SceneComponent: ...
    def GetAllSocketNames(self, ReturnValue: unreal.WrappedArray[str]) -> unreal.WrappedArray[str]: ...
    def DoesSocketExist(self, InSocketName: str, ReturnValue: bool) -> bool: ...
    def DetachFromParent(self, bMaintainWorldPosition: bool, bCallModify: bool): ...


class InterpTrackInst(unreal.UObject): ...


class InterpTrack(unreal.UObject):
    SubTracks: unreal.WrappedArray[InterpTrack]
    TrackInstClass: unreal.UClass
    ActiveCondition: int
    TrackTitle: str
    bOnePerGroup: bool
    bDirGroupOnly: bool
    bDisableTrack: bool
    bIsSelected: bool
    bIsAnimControlTrack: bool
    bSubTrackOnly: bool
    bVisible: bool
    bIsRecording: bool



class InterpTrackVectorBase(InterpTrack):
    VectorTrack: core_uobject.InterpCurveVector
    CurveTension: float



class InterpTrackFloatBase(InterpTrack):
    FloatTrack: core_uobject.InterpCurveFloat
    CurveTension: float



class AnimNotify(unreal.UObject):

    def Received_Notify(self, MeshComp: SkeletalMeshComponent, Animation: AnimSequenceBase, ReturnValue: bool) -> bool: ...
    def GetNotifyName(self, ReturnValue: str) -> str: ...


class AnimNotifyState(unreal.UObject):

    def Received_NotifyTick(self, MeshComp: SkeletalMeshComponent, Animation: AnimSequenceBase, FrameDeltaTime: float, ReturnValue: bool) -> bool: ...
    def Received_NotifyEnd(self, MeshComp: SkeletalMeshComponent, Animation: AnimSequenceBase, Reason: EAnimNotifyEndReason, ReturnValue: bool) -> bool: ...
    def Received_NotifyBegin(self, MeshComp: SkeletalMeshComponent, Animation: AnimSequenceBase, TotalDuration: float, ReturnValue: bool) -> bool: ...
    def GetNotifyName(self, ReturnValue: str) -> str: ...


class ParticleModule(unreal.UObject):
    bSpawnModule: bool
    bUpdateModule: bool
    bFinalUpdateModule: bool
    bUpdateForGPUEmitter: bool
    bCurvesAsColor: bool
    b3DDrawMode: bool
    bSupported3DDrawMode: bool
    bEnabled: bool
    bEditable: bool
    LODDuplicate: bool
    bSupportsRandomSeed: bool
    bRequiresLoopingNotification: bool
    LODValidity: int
    bFinalizeTickModule: bool
    bPreAsyncModule: bool



class PrimitiveComponent(SceneComponent):
    MinDrawDistance: float
    LDMaxDrawDistance: float
    CachedMaxDrawDistance: float
    DepthPriorityGroup: int
    ViewOwnerDepthPriorityGroup: int
    IndirectLightingCacheQuality: int
    LightmapType: ELightmapType
    PrimitiveFlagsGBX: int
    bSkipSyncToRBChildTransformUpdate: bool
    bUseLegacyPhysicsTicking: bool
    bNeverDistanceCull: bool
    bEnableGlobalIlluminationBoost: bool
    bAlwaysCreatePhysicsState: bool
    bGenerateOverlapEvents: bool
    bMultiBodyOverlap: bool
    bCheckAsyncSceneOnMove: bool
    bTraceComplexOnMove: bool
    bReturnMaterialOnMove: bool
    bUseViewOwnerDepthPriorityGroup: bool
    bAllowCullDistanceVolume: bool
    bHasMotionBlurVelocityMeshes: bool
    bVisibleInReflectionCaptures: bool
    bRenderInMainPass: bool
    bRenderInMono: bool
    bReceivesDecals: bool
    bReceivesSecondaryDecals: bool
    bOwnerNoSee: bool
    bOnlyOwnerSee: bool
    bTreatAsBackgroundForOcclusion: bool
    bUseAsOccluder: bool
    bSelectable: bool
    bForceMipStreaming: bool
    bHasPerInstanceHitProxies: bool
    CastShadow: bool
    bAffectDynamicIndirectLighting: bool
    bAffectDistanceFieldLighting: bool
    bCastDynamicShadow: bool
    bCastStaticShadow: bool
    bCastVolumetricTranslucentShadow: bool
    bSelfShadowOnly: bool
    bCastFarShadow: bool
    bCastInsetShadow: bool
    bCastCinematicShadow: bool
    bCastHiddenShadow: bool
    bCastShadowAsTwoSided: bool
    bLightAsIfStatic: bool
    bLightAttachmentsAsGroup: bool
    bReceiveMobileCSMShadows: bool
    bSingleSampleShadowFromStationaryLights: bool
    IndirectLightingContribution: float
    bIgnoreRadialImpulse: bool
    bIgnoreRadialForce: bool
    bApplyImpulseOnDamage: bool
    bReplicatePhysicsToAutonomousProxy: bool
    AlwaysLoadOnClient: bool
    AlwaysLoadOnServer: bool
    bUseEditorCompositing: bool
    bRenderCustomDepth: bool
    bRenderCustomDepthView1: bool
    bRenderCustomDepthView2: bool
    bRenderCustomDepthView3: bool
    bHasCustomNavigableGeometry: int
    CanCharacterStepUpOn: int
    LightingChannels: LightingChannels
    CustomDepthStencilWriteMask: ERendererStencilMask
    CustomDepthStencilValue: int
    CustomColorValueView1: core_uobject.LinearColor
    CustomColorValueView2: core_uobject.LinearColor
    CustomColorValueView3: core_uobject.LinearColor
    TranslucencySortPriority: int
    VisibilityId: int
    LpvBiasMultiplier: float
    BoundsScale: float
    LastSubmitTime: float
    LastRenderTime: float
    LastRenderTimeOnScreen: float
    MoveIgnoreActors: unreal.WrappedArray[Actor]
    MoveIgnoreComponents: unreal.WrappedArray[PrimitiveComponent]
    bForegroundLayer: bool
    bRenderIntoSkyEnvMap: bool
    BodyInstance: BodyInstance
    LODParentPrimitive: PrimitiveComponent
    PostPhysicsComponentTick: PrimitiveComponentPostPhysicsTickFunction
    ViewOwner: Actor
    ViewFlags: int
    def WakeRigidBody(self, BoneName: str): ...
    def WakeAllRigidBodies(self): ...
    def SetWalkableSlopeOverride(self, NewOverride: WalkableSlopeOverride): ...
    def SetViewOwner(self, NewViewOwner: Actor): ...
    def SetViewFlags(self, NewViewFlags: int, Method: EGbxViewFlagAction): ...
    def SetUseCCD(self, InUseCCD: bool, BoneName: str): ...
    def SetTranslucentSortPriority(self, NewTranslucentSortPriority: int): ...
    def SetSingleSampleShadowFromStationaryLights(self, bNewSingleSampleShadowFromStationaryLights: bool): ...
    def SetSimulatePhysics(self, bSimulate: bool): ...
    def SetRenderInMono(self, bValue: bool): ...
    def SetRenderInMainPass(self, bValue: bool): ...
    def SetRenderCustomDepth(self, bValue: bool): ...
    def SetReceivesSecondaryDecals(self, bNewReceivesSecondaryDecals: bool): ...
    def SetReceivesDecals(self, bNewReceivesDecals: bool): ...
    def SetPrimitiveFlags(self, InPrimitiveFlags: int, bEnabled: bool): ...
    def SetPhysMaterialOverride(self, NewPhysMaterial: PhysicalMaterial): ...
    def SetPhysicsMaxAngularVelocityInRadians(self, NewMaxAngVel: float, bAddToCurrent: bool, BoneName: str): ...
    def SetPhysicsMaxAngularVelocityInDegrees(self, NewMaxAngVel: float, bAddToCurrent: bool, BoneName: str): ...
    def SetPhysicsMaxAngularVelocity(self, NewMaxAngVel: float, bAddToCurrent: bool, BoneName: str): ...
    def SetPhysicsLinearVelocity(self, NewVel: core_uobject.Vector, bAddToCurrent: bool, BoneName: str): ...
    def SetPhysicsAngularVelocityInRadians(self, NewAngVel: core_uobject.Vector, bAddToCurrent: bool, BoneName: str): ...
    def SetPhysicsAngularVelocityInDegrees(self, NewAngVel: core_uobject.Vector, bAddToCurrent: bool, BoneName: str): ...
    def SetPhysicsAngularVelocity(self, NewAngVel: core_uobject.Vector, bAddToCurrent: bool, BoneName: str): ...
    def SetOwnerNoSee(self, bNewOwnerNoSee: bool): ...
    def SetOnlyOwnerSee(self, bNewOnlyOwnerSee: bool): ...
    def SetNotifyRigidBodyCollision(self, bNewNotifyRigidBodyCollision: bool): ...
    def SetMaterialByName(self, MaterialSlotName: str, Material: MaterialInterface): ...
    def SetMaterial(self, ElementIndex: int, Material: MaterialInterface): ...
    def SetMassScale(self, BoneName: str, InMassScale: float): ...
    def SetMassOverrideInKg(self, BoneName: str, MassInKg: float, bOverrideMass: bool): ...
    def SetLockedAxis(self, LockedAxis: int): ...
    def SetLinearDamping(self, InDamping: float): ...
    def SetGenerateWakeEvents(self, bGenerateWakeEvents: bool): ...
    def SetGenerateOverlapEvents(self, bInGenerateOverlapEvents: bool): ...
    def SetForegroundLayer(self, bNewForegroundLayer: bool): ...
    def SetEnableGravity(self, bGravityEnabled: bool): ...
    def SetCustomMaskMaterial(self, CustomMaskMaterial: MaterialInterface): ...
    def SetCustomGlowMaterial(self, CustomGlowMaterial: MaterialInterface): ...
    def SetCustomDepthStencilWriteMask(self, WriteMaskBit: ERendererStencilMask): ...
    def SetCustomDepthStencilValue(self, Value: int): ...
    def SetCustomDepthOnView(self, ViewIndex: int, Value: bool): ...
    def SetCustomColorValue(self, ViewIndex: int, Value: core_uobject.LinearColor): ...
    def SetCullDistance(self, NewCullDistance: float): ...
    def SetConstraintMode(self, ConstraintMode: int): ...
    def SetCollisionResponseToChannel(self, Channel: int, NewResponse: int): ...
    def SetCollisionResponseToAllChannels(self, NewResponse: int): ...
    def SetCollisionProfileName(self, InCollisionProfileName: str): ...
    def SetCollisionObjectType(self, Channel: int): ...
    def SetCollisionEnabled(self, NewType: int): ...
    def SetCenterOfMass(self, CenterOfMassOffset: core_uobject.Vector, BoneName: str): ...
    def SetCastShadow(self, NewCastShadow: bool): ...
    def SetBoundsScale(self, NewBoundsScale: float): ...
    def SetAngularDamping(self, InDamping: float): ...
    def SetAllUseCCD(self, InUseCCD: bool): ...
    def SetAllPhysicsLinearVelocity(self, NewVel: core_uobject.Vector, bAddToCurrent: bool): ...
    def SetAllPhysicsAngularVelocityInRadians(self, NewAngVel: core_uobject.Vector, bAddToCurrent: bool): ...
    def SetAllPhysicsAngularVelocityInDegrees(self, NewAngVel: core_uobject.Vector, bAddToCurrent: bool): ...
    def SetAllPhysicsAngularVelocity(self, NewAngVel: core_uobject.Vector, bAddToCurrent: bool): ...
    def SetAllMassScale(self, InMassScale: float): ...
    def ScaleByMomentOfInertia(self, InputVector: core_uobject.Vector, BoneName: str, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def PutRigidBodyToSleep(self, BoneName: str): ...
    def K2_LineTraceComponent(self, TraceStart: core_uobject.Vector, TraceEnd: core_uobject.Vector, bTraceComplex: bool, bShowTrace: bool, HitLocation: core_uobject.Vector, HitNormal: core_uobject.Vector, BoneName: str, OutHit: HitResult, ReturnValue: bool) -> bool: ...
    def K2_IsQueryCollisionEnabled(self, ReturnValue: bool) -> bool: ...
    def K2_IsPhysicsCollisionEnabled(self, ReturnValue: bool) -> bool: ...
    def K2_IsCollisionEnabled(self, ReturnValue: bool) -> bool: ...
    def IsOverlappingComponent(self, OtherComp: PrimitiveComponent, ReturnValue: bool) -> bool: ...
    def IsOverlappingActor(self, Other: Actor, ReturnValue: bool) -> bool: ...
    def IsGravityEnabled(self, ReturnValue: bool) -> bool: ...
    def IsAnyRigidBodyAwake(self, ReturnValue: bool) -> bool: ...
    def IgnoreComponentWhenMoving(self, Component: PrimitiveComponent, bShouldIgnore: bool): ...
    def IgnoreActorWhenMoving(self, Actor: Actor, bShouldIgnore: bool): ...
    def GetWalkableSlopeOverride(self, ReturnValue: WalkableSlopeOverride) -> WalkableSlopeOverride: ...
    def GetPhysicsLinearVelocityAtPoint(self, Point: core_uobject.Vector, BoneName: str, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetPhysicsLinearVelocity(self, BoneName: str, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetPhysicsAngularVelocityInRadians(self, BoneName: str, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetPhysicsAngularVelocityInDegrees(self, BoneName: str, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetPhysicsAngularVelocity(self, BoneName: str, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetOverlappingComponents(self, OutOverlappingComponents: unreal.WrappedArray[PrimitiveComponent]): ...
    def GetOverlappingActors(self, OverlappingActors: unreal.WrappedArray[Actor], ClassFilter: unreal.UClass): ...
    def GetNumMaterials(self, ReturnValue: int) -> int: ...
    def GetMaterialFromCollisionFaceIndex(self, FaceIndex: int, SectionIndex: int, ReturnValue: MaterialInterface) -> MaterialInterface: ...
    def GetMaterial(self, ElementIndex: int, ReturnValue: MaterialInterface) -> MaterialInterface: ...
    def GetMassScale(self, BoneName: str, ReturnValue: float) -> float: ...
    def GetMass(self, ReturnValue: float) -> float: ...
    def GetLinearDamping(self, ReturnValue: float) -> float: ...
    def GetInertiaTensor(self, BoneName: str, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetGenerateOverlapEvents(self, ReturnValue: bool) -> bool: ...
    def GetCustomMaskMaterial(self, ReturnValue: MaterialInterface) -> MaterialInterface: ...
    def GetCustomGlowMaterial(self, ReturnValue: MaterialInterface) -> MaterialInterface: ...
    def GetCollisionResponseToChannel(self, Channel: int, ReturnValue: int) -> int: ...
    def GetCollisionProfileName(self, ReturnValue: str) -> str: ...
    def GetCollisionObjectType(self, ReturnValue: int) -> int: ...
    def GetCollisionEnabled(self, ReturnValue: int) -> int: ...
    def GetClosestPointOnCollision(self, Point: core_uobject.Vector, OutPointOnBody: core_uobject.Vector, BoneName: str, ReturnValue: float) -> float: ...
    def GetCenterOfMass(self, BoneName: str, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetAngularDamping(self, ReturnValue: float) -> float: ...
    def CreateDynamicMaterialInstance(self, ElementIndex: int, SourceMaterial: MaterialInterface, OptionalName: str, ReturnValue: MaterialInstanceDynamic) -> MaterialInstanceDynamic: ...
    def CreateAndSetMaterialInstanceDynamicFromMaterial(self, ElementIndex: int, Parent: MaterialInterface, ReturnValue: MaterialInstanceDynamic) -> MaterialInstanceDynamic: ...
    def CreateAndSetMaterialInstanceDynamic(self, ElementIndex: int, ReturnValue: MaterialInstanceDynamic) -> MaterialInstanceDynamic: ...
    def CopyArrayOfMoveIgnoreComponents(self, ReturnValue: unreal.WrappedArray[PrimitiveComponent]) -> unreal.WrappedArray[PrimitiveComponent]: ...
    def CopyArrayOfMoveIgnoreActors(self, ReturnValue: unreal.WrappedArray[Actor]) -> unreal.WrappedArray[Actor]: ...
    def ClearMoveIgnoreComponents(self): ...
    def ClearMoveIgnoreActors(self): ...
    def CanCharacterStepUp(self, Pawn: Pawn, ReturnValue: bool) -> bool: ...
    def AddTorqueInRadians(self, Torque: core_uobject.Vector, BoneName: str, bAccelChange: bool): ...
    def AddTorqueInDegrees(self, Torque: core_uobject.Vector, BoneName: str, bAccelChange: bool): ...
    def AddTorque(self, Torque: core_uobject.Vector, BoneName: str, bAccelChange: bool): ...
    def AddRadialImpulse(self, Origin: core_uobject.Vector, Radius: float, Strength: float, Falloff: int, bVelChange: bool): ...
    def AddRadialForce(self, Origin: core_uobject.Vector, Radius: float, Strength: float, Falloff: int, bAccelChange: bool): ...
    def AddImpulseAtLocation(self, Impulse: core_uobject.Vector, Location: core_uobject.Vector, BoneName: str): ...
    def AddImpulse(self, Impulse: core_uobject.Vector, BoneName: str, bVelChange: bool): ...
    def AddForceAtLocationLocal(self, Force: core_uobject.Vector, Location: core_uobject.Vector, BoneName: str): ...
    def AddForceAtLocation(self, Force: core_uobject.Vector, Location: core_uobject.Vector, BoneName: str): ...
    def AddForce(self, Force: core_uobject.Vector, BoneName: str, bAccelChange: bool): ...
    def AddAngularImpulseInRadians(self, Impulse: core_uobject.Vector, BoneName: str, bVelChange: bool): ...
    def AddAngularImpulseInDegrees(self, Impulse: core_uobject.Vector, BoneName: str, bVelChange: bool): ...
    def AddAngularImpulse(self, Impulse: core_uobject.Vector, BoneName: str, bVelChange: bool): ...


class MeshComponent(PrimitiveComponent):
    OverrideMaterials: unreal.WrappedArray[MaterialInterface]
    bIgnoredByFXCoordinator: bool
    def SetVectorParameterValueOnMaterials(self, ParameterName: str, ParameterValue: core_uobject.Vector): ...
    def SetTextureParameterValueOnMaterials(self, ParameterName: str, ParameterValue: Texture): ...
    def SetScalarParameterValueOnMaterials(self, ParameterName: str, ParameterValue: float): ...
    def SetLinearColorParameterValueOnMaterials(self, ParameterName: str, ParameterValue: core_uobject.LinearColor): ...
    def PrestreamTextures(self, Seconds: float, bPrioritizeCharacterTextures: bool, CinematicTextureGroups: int): ...
    def IsMaterialSlotNameValid(self, MaterialSlotName: str, ReturnValue: bool) -> bool: ...
    def GetMaterialSlotNames(self, ReturnValue: unreal.WrappedArray[str]) -> unreal.WrappedArray[str]: ...
    def GetMaterials(self, ReturnValue: unreal.WrappedArray[MaterialInterface]) -> unreal.WrappedArray[MaterialInterface]: ...
    def GetMaterialIndex(self, MaterialSlotName: str, ReturnValue: int) -> int: ...


class SkinnedMeshComponent(MeshComponent):
    SkeletalMesh: SkeletalMesh
    MasterPoseComponent: SkinnedMeshComponent
    CustomMaskMaterial: MaterialInterface
    CustomGlowMaterial: MaterialInterface
    PhysicsAssetOverride: PhysicsAsset
    ForcedLodModel: int
    bOverrideMinLod: bool
    MinLodModel: int
    StreamingDistanceMultiplier: float
    LODInfo: unreal.WrappedArray[SkelMeshComponentLODInfo]
    MeshComponentUpdateFlag: int
    bUseBoundsFromMasterPoseComponent: bool
    bForceWireframe: bool
    bDisplayBones: bool
    bDisableMorphTarget: bool
    bHideSkin: bool
    bPerBoneMotionBlur: bool
    bComponentUseFixedSkelBounds: bool
    bConsiderAllBodiesForBounds: bool
    bSyncAttachParentLOD: bool
    bCanHighlightSelectedSections: bool
    bRecentlyRendered: bool
    bCastCapsuleDirectShadow: bool
    bCastCapsuleIndirectShadow: bool
    bCPUSkinning: bool
    bEnableUpdateRateOptimizations: bool
    bDisplayDebugUpdateRateOptimizations: bool
    bRenderStatic: bool
    bCachedLocalBoundsUpToDate: bool
    bForceMeshObjectUpdate: bool
    bSelfOwnedUpdateRateOptimizations: bool
    CapsuleIndirectShadowMinVisibility: float
    GestaltData: GestaltDataContainer
    DesignerSocketMappings: unreal.WrappedArray[SocketRemapEntry]
    bIgnoreUpdateRateOptimizationsWhenPlayingMontage: bool
    bCheckAttachedComponentsForRecentlyRendered: bool
    def UnHideBoneByName(self, BoneName: str): ...
    def TransformToBoneSpace(self, BoneName: str, InPosition: core_uobject.Vector, InRotation: core_uobject.Rotator, OutPosition: core_uobject.Vector, OutRotation: core_uobject.Rotator): ...
    def TransformFromBoneSpace(self, BoneName: str, InPosition: core_uobject.Vector, InRotation: core_uobject.Rotator, OutPosition: core_uobject.Vector, OutRotation: core_uobject.Rotator): ...
    def ShowMaterialSection(self, MaterialID: int, bShow: bool, LODIndex: int): ...
    def ShowAllMaterialSections(self, LODIndex: int): ...
    def SetVertexColorOverride_LinearColor(self, ColorChannelIndex: int, LODIndex: int, VertexColors: unreal.WrappedArray[core_uobject.LinearColor]): ...
    def SetSkinWeightOverride(self, LODIndex: int, SkinWeights: unreal.WrappedArray[SkelMeshSkinWeightInfo]): ...
    def SetSkeletalMesh(self, NewMesh: SkeletalMesh, bReinitPose: bool): ...
    def SetRenderStatic(self, bNewValue: bool): ...
    def SetPhysicsAsset(self, NewPhysicsAsset: PhysicsAsset, bForceReInit: bool): ...
    def SetMinLOD(self, InNewMinLOD: int): ...
    def SetMasterPoseComponent(self, NewMasterBoneComponent: SkinnedMeshComponent, bForceUpdate: bool): ...
    def SetForcedLOD(self, InNewForcedLOD: int): ...
    def SetCastCapsuleIndirectShadow(self, bNewValue: bool): ...
    def SetCastCapsuleDirectShadow(self, bNewValue: bool): ...
    def SetCapsuleIndirectShadowMinVisibility(self, NewValue: float): ...
    def IsMaterialSectionShown(self, MaterialID: int, LODIndex: int, ReturnValue: bool) -> bool: ...
    def IsBoneHiddenByName(self, BoneName: str, ReturnValue: bool) -> bool: ...
    def HideBoneByName(self, BoneName: str, PhysBodyOption: int): ...
    def GetSocketBoneName(self, InSocketName: str, ReturnValue: str) -> str: ...
    def GetRefPosePosition(self, BoneIndex: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetParentBone(self, BoneName: str, ReturnValue: str) -> str: ...
    def GetNumLODs(self, ReturnValue: int) -> int: ...
    def GetNumBones(self, ReturnValue: int) -> int: ...
    def GetBoneName(self, BoneIndex: int, ReturnValue: str) -> str: ...
    def GetBoneIndex(self, BoneName: str, ReturnValue: int) -> int: ...
    def FindClosestBone_K2(self, TestLocation: core_uobject.Vector, BoneLocation: core_uobject.Vector, IgnoreScale: float, bRequirePhysicsAsset: bool, ReturnValue: str) -> str: ...
    def ClearVertexColorOverride(self, ColorChannelIndex: int, LODIndex: int): ...
    def ClearSkinWeightOverride(self, LODIndex: int): ...
    def BoneIsChildOf(self, BoneName: str, ParentBoneName: str, ReturnValue: bool) -> bool: ...


class SkeletalMesh(unreal.UObject):
    Skeleton: Skeleton
    ImportedBounds: core_uobject.BoxSphereBounds
    ExtendedBounds: core_uobject.BoxSphereBounds
    PositiveBoundsExtension: core_uobject.Vector
    NegativeBoundsExtension: core_uobject.Vector
    Materials: unreal.WrappedArray[SkeletalMaterial]
    SkelMirrorTable: unreal.WrappedArray[BoneMirrorInfo]
    SkelMirrorAxis: int
    SkelMirrorFlipAxis: int
    LODInfo: unreal.WrappedArray[SkeletalMeshLODInfo]
    MinLOD: PerPlatformInt
    CullDistanceLODGroup: str
    bUseFullPrecisionUVs: bool
    bUseHighPrecisionTangentBasis: bool
    bHasBeenSimplified: bool
    bHasVertexColors: bool
    NumVertexColorChannels: int
    DefaultVertexColors: EDefaultVertexColor
    bEnablePerPolyCollision: bool
    BodySetup: BodySetup
    PhysicsAsset: PhysicsAsset
    ShadowPhysicsAsset: PhysicsAsset
    NodeMappingData: unreal.WrappedArray[NodeMappingContainer]
    MorphTargets: unreal.WrappedArray[MorphTarget]
    ClothingAssets: unreal.WrappedArray[ClothingAssetData_Legacy]
    PostProcessAnimBlueprint: unreal.UClass
    MeshClothingAssets: unreal.WrappedArray[clothing_system_runtime_interface.ClothingAssetBase]
    SamplingInfo: SkeletalMeshSamplingInfo
    AssetUserData: unreal.WrappedArray[AssetUserData]
    Sockets: unreal.WrappedArray[SkeletalMeshSocket]
    TightBounds: core_uobject.BoxSphereBounds
    BoundsGenerationType: int
    GestaltData: GestaltData
    LODGroup: str
    RetargetingAsset: GbxRetargetAsset
    def SetLODSettings(self, InLODSettings: SkeletalMeshLODSettings): ...
    def PrestreamTextures(self, Seconds: float, bPrioritizeCharacterTextures: bool, CinematicTextureGroups: int, WorldContext: unreal.UObject): ...
    def NumSockets(self, ReturnValue: int) -> int: ...
    def IsSectionUsingCloth(self, InSectionIndex: int, bCheckCorrespondingSections: bool, ReturnValue: bool) -> bool: ...
    def GetSocketByIndex(self, Index: int, ReturnValue: SkeletalMeshSocket) -> SkeletalMeshSocket: ...
    def GetNodeMappingContainer(self, SourceAsset: Blueprint, ReturnValue: NodeMappingContainer) -> NodeMappingContainer: ...
    def GetImportedBounds(self, ReturnValue: core_uobject.BoxSphereBounds) -> core_uobject.BoxSphereBounds: ...
    def GetBounds(self, ReturnValue: core_uobject.BoxSphereBounds) -> core_uobject.BoxSphereBounds: ...
    def FindSocketAndIndex(self, InSocketName: str, OutIndex: int, ReturnValue: SkeletalMeshSocket) -> SkeletalMeshSocket: ...
    def FindSocket(self, InSocketName: str, ReturnValue: SkeletalMeshSocket) -> SkeletalMeshSocket: ...


class Commandlet(unreal.UObject):
    HelpDescription: str
    HelpUsage: str
    HelpWebLink: str
    HelpParamNames: unreal.WrappedArray[str]
    HelpParamDescriptions: unreal.WrappedArray[str]
    IsServer: bool
    IsClient: bool
    IsEditor: bool
    LogToConsole: bool
    ShowErrorCount: bool
    ShowProgress: bool



class DynamicBlueprintBinding(unreal.UObject): ...


class InputComponent(ActorComponent):
    CachedKeyToActionInfo: unreal.WrappedArray[CachedKeyToActionInfo]
    def WasControllerKeyJustReleased(self, Key: input_core.Key, ReturnValue: bool) -> bool: ...
    def WasControllerKeyJustPressed(self, Key: input_core.Key, ReturnValue: bool) -> bool: ...
    def IsControllerKeyDown(self, Key: input_core.Key, ReturnValue: bool) -> bool: ...
    def GetTouchState(self, FingerIndex: int, LocationX: float, LocationY: float, bIsCurrentlyPressed: bool): ...
    def GetControllerVectorKeyState(self, Key: input_core.Key, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetControllerMouseDelta(self, DeltaX: float, DeltaY: float): ...
    def GetControllerKeyTimeDown(self, Key: input_core.Key, ReturnValue: float) -> float: ...
    def GetControllerAnalogStickState(self, WhichStick: int, StickX: float, StickY: float): ...
    def GetControllerAnalogKeyState(self, Key: input_core.Key, ReturnValue: float) -> float: ...


class Controller(Actor):
    PlayerState: PlayerState
    StateName: str
    Pawn: Pawn
    Character: Character
    TransformComponent: SceneComponent
    ControlRotation: core_uobject.Rotator
    bAttachToPawn: bool
    bIsPlayerController: bool
    def UnPossess(self): ...
    def StopMovement(self): ...
    def SetInitialLocationAndRotation(self, NewLocation: core_uobject.Vector, NewRotation: core_uobject.Rotator): ...
    def SetIgnoreMoveInput(self, bNewMoveInput: bool): ...
    def SetIgnoreLookInput(self, bNewLookInput: bool): ...
    def SetControlRotation(self, NewRotation: core_uobject.Rotator, bResetCamera: bool): ...
    def ResetIgnoreMoveInput(self): ...
    def ResetIgnoreLookInput(self): ...
    def ResetIgnoreInputFlags(self): ...
    def ReceiveInstigatedAnyDamage(self, Damage: float, DamageType: DamageType, DamagedActor: Actor, DamageCauser: Actor): ...
    def Possess(self, InPawn: Pawn): ...
    def OnRep_PlayerState(self): ...
    def OnRep_Pawn(self): ...
    def LineOfSightTo(self, Other: Actor, ViewPoint: core_uobject.Vector, bAlternateChecks: bool, ReturnValue: bool) -> bool: ...
    def K2_GetPawn(self, ReturnValue: Pawn) -> Pawn: ...
    def IsPlayerController(self, ReturnValue: bool) -> bool: ...
    def IsMoveInputIgnored(self, ReturnValue: bool) -> bool: ...
    def IsLookInputIgnored(self, ReturnValue: bool) -> bool: ...
    def IsLocalPlayerController(self, ReturnValue: bool) -> bool: ...
    def IsLocalController(self, ReturnValue: bool) -> bool: ...
    def GetViewTarget(self, ReturnValue: Actor) -> Actor: ...
    def GetDesiredRotation(self, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def GetControlRotation(self, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def ClientSetRotation(self, NewRotation: core_uobject.Rotator, bResetCamera: bool): ...
    def ClientSetLocation(self, NewLocation: core_uobject.Vector, NewRotation: core_uobject.Rotator): ...
    def CastToPlayerController(self, ReturnValue: PlayerController) -> PlayerController: ...


class PlayerController(Controller):
    Player: Player
    AcknowledgedPawn: Pawn
    ControllingDirTrackInst: InterpTrackInstDirector
    MyHUD: HUD
    PlayerCameraManager: PlayerCameraManager
    PlayerCameraManagerClass: unreal.UClass
    bAutoManageActiveCameraTarget: bool
    TargetViewRotation: core_uobject.Rotator
    SmoothTargetViewRotationSpeed: float
    HiddenActors: unreal.WrappedArray[Actor]
    HiddenPrimitiveComponents: unreal.WrappedArray[PrimitiveComponent]
    LastSpectatorStateSynchTime: float
    LastSpectatorSyncLocation: core_uobject.Vector
    LastSpectatorSyncRotation: core_uobject.Rotator
    ClientCap: int
    CheatManager: CheatManager
    CheatClass: unreal.UClass
    PlayerInput: PlayerInput
    ActiveForceFeedbackEffects: unreal.WrappedArray[ActiveForceFeedbackEffect]
    bPlayerIsWaiting: bool
    NetPlayerIndex: int
    PendingSwapConnection: NetConnection
    NetConnection: NetConnection
    InputYawScale: float
    InputPitchScale: float
    InputRollScale: float
    bShowMouseCursor: bool
    bEnableClickEvents: bool
    bEnableTouchEvents: bool
    bEnableMouseOverEvents: bool
    bEnableTouchOverEvents: bool
    bForceFeedbackEnabled: bool
    ForceFeedbackScale: float
    ClickEventKeys: unreal.WrappedArray[input_core.Key]
    DefaultMouseCursor: int
    CurrentMouseCursor: int
    DefaultClickTraceChannel: int
    CurrentClickTraceChannel: int
    HitResultTraceDistance: float
    bEnableVibration: bool
    bEnableTriggerFeedback: bool
    InactiveStateInputComponent: InputComponent
    bShouldPerformFullTickWhenPaused: bool
    CurrentTouchInterface: TouchInterface
    SpectatorPawn: SpectatorPawn
    bIsLocalPlayerController: bool
    SpawnLocation: core_uobject.Vector
    LevelSequenceRestoreViewTarget: Actor
    ActiveGbxForceFeedbackEffects: unreal.WrappedArray[ActiveGbxForceFeedbackEffect]
    bPlayerViewRenderingEnabled: bool
    def WasInputKeyJustReleased(self, Key: input_core.Key, ReturnValue: bool) -> bool: ...
    def WasInputKeyJustPressed(self, Key: input_core.Key, ReturnValue: bool) -> bool: ...
    def ToggleSpeaking(self, bInSpeaking: bool): ...
    def SwitchLevel(self, URL: str): ...
    def StopHapticEffect(self, Hand: input_core.EControllerHand): ...
    def StartFire(self, FireModeNum: int): ...
    def SetVirtualJoystickVisibility(self, bVisible: bool): ...
    def SetViewTargetWithBlend(self, NewViewTarget: Actor, BlendTime: float, BlendFunc: int, BlendExp: float, bLockOutgoing: bool): ...
    def SetPlayerViewRenderingEnabled(self, bInViewRenderingEnabled: bool): ...
    def SetName(self, S: str): ...
    def SetMouseLocation(self, X: int, Y: int): ...
    def SetMouseCursorWidget(self, Cursor: int, CursorWidget: unreal.UObject): ...
    def SetHapticsByValue(self, Frequency: float, Amplitude: float, Hand: input_core.EControllerHand): ...
    def SetDisableHaptics(self, bNewDisabled: bool): ...
    def SetControllerLightColor(self, Color: core_uobject.Color): ...
    def SetCinematicMode(self, bInCinematicMode: bool, bHidePlayer: bool, bAffectsHUD: bool, bAffectsMovement: bool, bAffectsTurning: bool): ...
    def SetAudioListenerOverride(self, AttachToComponent: SceneComponent, Location: core_uobject.Vector, Rotation: core_uobject.Rotator): ...
    def SetAudioListenerAttenuationOverride(self, AttachToComponent: SceneComponent, AttenuationLocationOVerride: core_uobject.Vector): ...
    def ServerViewSelf(self, TransitionParams: ViewTargetTransitionParams): ...
    def ServerViewPrevPlayer(self): ...
    def ServerViewNextPlayer(self): ...
    def ServerVerifyViewTarget(self): ...
    def ServerUpdateMultipleLevelsVisibility(self, LevelVisibilities: unreal.WrappedArray[UpdateLevelVisibilityLevelInfo], WorldName: str): ...
    def ServerUpdateLevelVisibility(self, PackageName: str, WorldName: str, bIsVisible: bool): ...
    def ServerUpdateCamera(self, CamLoc: Vector_NetQuantize, CamPitchAndYaw: int, CamFOV: float): ...
    def ServerUnmutePlayer(self, PlayerId: UniqueNetIdRepl): ...
    def ServerToggleAILogging(self): ...
    def ServerShortTimeout(self): ...
    def ServerSetSpectatorWaiting(self, bWaiting: bool): ...
    def ServerSetSpectatorLocation(self, NewLoc: core_uobject.Vector, NewRot: core_uobject.Rotator): ...
    def ServerRestartPlayer(self): ...
    def ServerPause(self): ...
    def ServerNotifyLoadedWorld(self, WorldPackageName: str): ...
    def ServerMutePlayer(self, PlayerId: UniqueNetIdRepl): ...
    def ServerGbxConsoleCommand(self, InContext: ReplicatedConsoleCommandContext): ...
    def ServerDestroy(self): ...
    def ServerCheckClientPossessionReliable(self): ...
    def ServerCheckClientPossession(self): ...
    def ServerChangeName(self, S: str): ...
    def ServerCamera(self, NewMode: str): ...
    def ServerAcknowledgePossession(self, P: Pawn): ...
    def SendToConsole(self, Command: str): ...
    def RestartLevel(self): ...
    def ResetControllerLightColor(self): ...
    def ProjectWorldLocationToScreen(self, WorldLocation: core_uobject.Vector, ScreenLocation: core_uobject.Vector2D, bPlayerViewportRelative: bool, bUseForegroundProjection: bool, ReturnValue: bool) -> bool: ...
    def PlayHapticEffect(self, HapticEffect: HapticFeedbackEffect_Base, Hand: input_core.EControllerHand, Scale: float, bLoop: bool): ...
    def PlayDynamicForceFeedback(self, Intensity: float, Duration: float, bAffectsLeftLarge: bool, bAffectsLeftSmall: bool, bAffectsRightLarge: bool, bAffectsRightSmall: bool, Action: int, LatentInfo: LatentActionInfo): ...
    def Pause(self): ...
    def OnServerStartedVisualLogger(self, bIsLogging: bool): ...
    def LocalTravel(self, URL: str): ...
    def IsInputKeyDown(self, Key: input_core.Key, ReturnValue: bool) -> bool: ...
    def GetViewportSize(self, SizeX: int, SizeY: int): ...
    def GetSpectatorPawn(self, ReturnValue: SpectatorPawn) -> SpectatorPawn: ...
    def GetMousePosition(self, LocationX: float, LocationY: float, ReturnValue: bool) -> bool: ...
    def GetInputVectorKeyState(self, Key: input_core.Key, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetInputTouchState(self, FingerIndex: int, LocationX: float, LocationY: float, bIsCurrentlyPressed: bool): ...
    def GetInputMouseDelta(self, DeltaX: float, DeltaY: float): ...
    def GetInputMotionState(self, Tilt: core_uobject.Vector, RotationRate: core_uobject.Vector, Gravity: core_uobject.Vector, Acceleration: core_uobject.Vector): ...
    def GetInputKeyTimeDown(self, Key: input_core.Key, ReturnValue: float) -> float: ...
    def GetInputAnalogStickState(self, WhichStick: int, StickX: float, StickY: float): ...
    def GetInputAnalogKeyState(self, Key: input_core.Key, ReturnValue: float) -> float: ...
    def GetHUD(self, ReturnValue: HUD) -> HUD: ...
    def GetHitResultUnderFingerForObjects(self, FingerIndex: int, ObjectTypes: unreal.WrappedArray[int], bTraceComplex: bool, HitResult: HitResult, ReturnValue: bool) -> bool: ...
    def GetHitResultUnderFingerByChannel(self, FingerIndex: int, TraceChannel: int, bTraceComplex: bool, HitResult: HitResult, ReturnValue: bool) -> bool: ...
    def GetHitResultUnderFinger(self, FingerIndex: int, TraceChannel: int, bTraceComplex: bool, HitResult: HitResult, ReturnValue: bool) -> bool: ...
    def GetHitResultUnderCursorForObjects(self, ObjectTypes: unreal.WrappedArray[int], bTraceComplex: bool, HitResult: HitResult, ReturnValue: bool) -> bool: ...
    def GetHitResultUnderCursorByChannel(self, TraceChannel: int, bTraceComplex: bool, HitResult: HitResult, ReturnValue: bool) -> bool: ...
    def GetHitResultUnderCursor(self, TraceChannel: int, bTraceComplex: bool, HitResult: HitResult, ReturnValue: bool) -> bool: ...
    def GetFocalLocation(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def FOV(self, NewFOV: float): ...
    def DeprojectScreenPositionToWorld(self, ScreenX: float, ScreenY: float, WorldLocation: core_uobject.Vector, WorldDirection: core_uobject.Vector, bUseForegroundProjection: bool, bTruncateScreenPosition: bool, ReturnValue: bool) -> bool: ...
    def DeprojectMousePositionToWorld(self, WorldLocation: core_uobject.Vector, WorldDirection: core_uobject.Vector, ReturnValue: bool) -> bool: ...
    def ConsoleKey(self, Key: input_core.Key): ...
    def ClientWasKicked(self, KickReason: str): ...
    def ClientVoiceHandshakeComplete(self): ...
    def ClientUpdateMultipleLevelsStreamingStatus(self, LevelStatuses: unreal.WrappedArray[UpdateLevelStreamingLevelStatus]): ...
    def ClientUpdateLevelStreamingStatus(self, PackageName: str, bNewShouldBeLoaded: bool, bNewShouldBeVisible: bool, bNewShouldBlockOnLoad: bool, LODIndex: int): ...
    def ClientUnmutePlayer(self, PlayerId: UniqueNetIdRepl): ...
    def ClientTravelInternal(self, URL: str, TravelType: int, bSeamless: bool, MapPackageGuid: core_uobject.Guid): ...
    def ClientTravel(self, URL: str, TravelType: int, bSeamless: bool, MapPackageGuid: core_uobject.Guid): ...
    def ClientTeamMessage(self, SenderPlayerState: PlayerState, S: str, Type: str, MsgLifeTime: float): ...
    def ClientStopGbxForceFeedback(self, Tag: str): ...
    def ClientStopForceFeedback(self, ForceFeedbackEffect: ForceFeedbackEffect, Tag: str): ...
    def ClientStopCameraShake(self, Shake: unreal.UClass, bImmediately: bool): ...
    def ClientStopCameraAnim(self, AnimToStop: CameraAnim): ...
    def ClientStartOnlineSession(self): ...
    def ClientSpawnCameraLensEffect(self, LensEffectEmitterClass: unreal.UClass): ...
    def ClientSetViewTarget(self, A: Actor, TransitionParams: ViewTargetTransitionParams): ...
    def ClientSetSpectatorWaiting(self, bWaiting: bool): ...
    def ClientSetHUD(self, NewHUDClass: unreal.UClass): ...
    def ClientSetForceMipLevelsToBeResident(self, Material: MaterialInterface, ForceDuration: float, CinematicTextureGroups: int): ...
    def ClientSetCinematicMode(self, bInCinematicMode: bool, bAffectsMovement: bool, bAffectsTurning: bool, bAffectsHUD: bool): ...
    def ClientSetCameraMode(self, NewCamMode: str): ...
    def ClientSetCameraFade(self, bEnableFading: bool, FadeColor: core_uobject.Color, FadeAlpha: core_uobject.Vector2D, FadeTime: float, bFadeAudio: bool): ...
    def ClientSetBlockOnAsyncLoading(self): ...
    def ClientReturnToMainMenuWithTextReason(self, ReturnReason: str): ...
    def ClientReturnToMainMenu(self, ReturnReason: str): ...
    def ClientRetryClientRestart(self, NewPawn: Pawn): ...
    def ClientRestart(self, NewPawn: Pawn): ...
    def ClientReset(self): ...
    def ClientRepObjRef(self, Object: unreal.UObject): ...
    def ClientReceiveLocalizedMessage(self, MESSAGE: unreal.UClass, Switch: int, RelatedPlayerState_1: PlayerState, RelatedPlayerState_2: PlayerState, OptionalObject: unreal.UObject): ...
    def ClientPrestreamTextures(self, ForcedActor: Actor, ForceDuration: float, bEnableStreaming: bool, CinematicTextureGroups: int): ...
    def ClientPrepareMapChange(self, LevelName: str, bFirst: bool, bLast: bool): ...
    def ClientPlaySoundAtLocation(self, Sound: SoundBase, Location: core_uobject.Vector, VolumeMultiplier: float, PitchMultiplier: float): ...
    def ClientPlaySound(self, Sound: SoundBase, VolumeMultiplier: float, PitchMultiplier: float): ...
    def ClientPlayRadialBlur(self, BlurInfo: RadialBlurSelection, bOverrideCenter: bool, WorldSpaceCenter: core_uobject.Vector, MaxDistance: float): ...
    def ClientPlayGbxForceFeedback(self, ForceFeedbackEffect: GbxForceFeedbackEffect, bLooping: bool, bIgnoreTimeDilation: bool, Tag: str): ...
    def ClientPlayForceFeedback(self, ForceFeedbackEffect: ForceFeedbackEffect, bLooping: bool, bIgnoreTimeDilation: bool, Tag: str): ...
    def ClientPlayCameraShake(self, Shake: unreal.UClass, Scale: float, PlaySpace: int, UserPlaySpaceRot: core_uobject.Rotator): ...
    def ClientPlayCameraAnim(self, AnimToPlay: CameraAnim, Scale: float, Rate: float, BlendInTime: float, BlendOutTime: float, bLoop: bool, bRandomStartTime: bool, Space: int, CustomPlaySpace: core_uobject.Rotator): ...
    def ClientMutePlayer(self, PlayerId: UniqueNetIdRepl): ...
    def ClientMessage(self, S: str, Type: str, MsgLifeTime: float): ...
    def ClientIgnoreMoveInput(self, bIgnore: bool): ...
    def ClientIgnoreLookInput(self, bIgnore: bool): ...
    def ClientGotoState(self, NewState: str): ...
    def ClientGameEnded(self, EndGameFocus: Actor, bIsWinner: bool): ...
    def ClientForceGarbageCollection(self): ...
    def ClientFlushLevelStreaming(self): ...
    def ClientEndOnlineSession(self): ...
    def ClientEnableNetworkVoice(self, bEnable: bool): ...
    def ClientCommitMapChange(self): ...
    def ClientClearCameraLensEffects(self): ...
    def ClientCapBandwidth(self, Cap: int): ...
    def ClientCancelPendingMapChange(self): ...
    def ClientAddTextureStreamingLoc(self, InLoc: core_uobject.Vector, Duration: float, bOverrideLocation: bool): ...
    def ClearAudioListenerOverride(self): ...
    def ClearAudioListenerAttenuationOverride(self): ...
    def CanRestartPlayer(self, ReturnValue: bool) -> bool: ...
    def Camera(self, NewMode: str): ...
    def AddYawInput(self, Val: float): ...
    def AddRollInput(self, Val: float): ...
    def AddPitchInput(self, Val: float): ...
    def ActivateTouchInterface(self, NewTouchInterface: TouchInterface): ...


class PlayerInput(unreal.UObject):
    DebugExecBindings: unreal.WrappedArray[KeyBind]
    InvertedAxis: unreal.WrappedArray[str]
    bDisableDebugExecTestBuilds: bool
    DebugExecTestBuildsWhiteList: unreal.WrappedArray[input_core.Key]
    def SetMouseSensitivity(self, Sensitivity: float): ...
    def SetBind(self, BindName: str, Command: str): ...
    def InvertAxisKey(self, AxisKey: input_core.Key): ...
    def InvertAxis(self, AxisName: str): ...
    def ClearSmoothing(self): ...


class BlueprintCore(unreal.UObject):
    SkeletonGeneratedClass: unreal.UClass
    GeneratedClass: unreal.UClass
    bLegacyNeedToPurgeSkelRefs: bool
    bLegacyGeneratedClassIsAuthoritative: bool
    BlueprintGuid: core_uobject.Guid



class Blueprint(BlueprintCore):
    bRecompileOnLoad: bool
    ParentClass: unreal.UClass
    PRIVATE_InnermostPreviousCDO: unreal.UObject
    bHasBeenRegenerated: bool
    bIsRegeneratingOnLoad: bool
    SimpleConstructionScript: SimpleConstructionScript
    ComponentTemplates: unreal.WrappedArray[ActorComponent]
    Timelines: unreal.WrappedArray[TimelineTemplate]
    InheritableComponentHandler: InheritableComponentHandler
    BlueprintType: int
    BlueprintSystemVersion: int
    bNativize: bool
    bGenerateEditInlineNewClass: bool



class BlueprintGeneratedClass(unreal.UClass):
    NumReplicatedProperties: int
    bHasNativizedParent: bool
    DynamicBindingObjects: unreal.WrappedArray[DynamicBlueprintBinding]
    ComponentTemplates: unreal.WrappedArray[ActorComponent]
    Timelines: unreal.WrappedArray[TimelineTemplate]
    SimpleConstructionScript: SimpleConstructionScript
    InheritableComponentHandler: InheritableComponentHandler
    UberGraphFramePointerProperty: core_uobject.StructProperty
    UberGraphFunction: core_uobject.Function



class World(unreal.UObject):
    PersistentLevel: Level
    NetDriver: NetDriver
    LineBatcher: LineBatchComponent
    PersistentLineBatcher: LineBatchComponent
    ForegroundLineBatcher: LineBatchComponent
    NetworkManager: GameNetworkManager
    PhysicsCollisionHandler: PhysicsCollisionHandler
    ExtraReferencedObjects: unreal.WrappedArray[unreal.UObject]
    PerModuleDataObjects: unreal.WrappedArray[unreal.UObject]
    StreamingLevels: unreal.WrappedArray[LevelStreaming]
    StreamingLevelsPrefix: str
    CurrentLevelPendingVisibility: Level
    CurrentLevelPendingInvisibility: Level
    DemoNetDriver: DemoNetDriver
    MyParticleEventManager: ParticleEventManager
    DefaultPhysicsVolume: PhysicsVolume
    NavigationSystem: NavigationSystemBase
    AuthorityGameMode: GameModeBase
    GameState: GameStateBase
    AISystem: AISystemBase
    AvoidanceManager: AvoidanceManager
    Levels: unreal.WrappedArray[Level]
    LevelCollections: unreal.WrappedArray[LevelCollection]
    CurrentLevel: Level
    OwningGameInstance: GameInstance
    ParameterCollectionInstances: unreal.WrappedArray[MaterialParameterCollectionInstance]
    CanvasForRenderingToTarget: Canvas
    CanvasForDrawMaterialToRenderTarget: Canvas
    WorldComposition: WorldComposition
    bAreConstraintsDirty: bool
    CullDistanceVolumes: unreal.WrappedArray[CullDistanceVolume]
    DominantCullDistanceVolume: CullDistanceVolume
    PSCPool: WorldPSCPool
    StaticLightingLevelInfo_Build: StaticLightingLevelInfo
    StaticLightingLevelInfo_Current: StaticLightingLevelInfo
    MasterSettingsType: unreal.UClass
    LagCompensationManager: GbxLagCompensationManager
    SpawnActorAsyncManager: GbxSpawnActorAsyncManager
    GbxMediaManager: GbxBaseMediaManager
    def HandleTimelineScrubbed(self): ...


class NavigationSystemBase(unreal.UObject): ...


class AISystemBase(unreal.UObject):
    AISystemClassName: core_uobject.SoftClassPath
    AISystemModuleName: str
    bInstantiateAISystemOnClient: bool



class GbxAnimStateManager(unreal.UObject): ...


class Pawn(Actor):
    bUseControllerRotationPitch: bool
    bUseControllerRotationYaw: bool
    bUseControllerRotationRoll: bool
    bCanAffectNavigationGeneration: bool
    bClearOwnerWhenUnPossessed: bool
    BaseEyeHeight: float
    AutoPossessPlayer: int
    AutoPossessAI: EAutoPossessAI
    AIControllerClass: unreal.UClass
    PlayerState: PlayerState
    RemoteViewPitch: int
    LastHitBy: Controller
    Controller: Controller
    ControlInputVector: core_uobject.Vector
    LastControlInputVector: core_uobject.Vector
    def SpawnDefaultController(self): ...
    def SetCanAffectNavigationGeneration(self, bNewValue: bool, bForceUpdate: bool): ...
    def ReceiveUnpossessed(self, OldController: Controller): ...
    def ReceivePossessed(self, NewController: Controller): ...
    def PawnMakeNoise(self, Loudness: float, NoiseLocation: core_uobject.Vector, bUseNoiseMakerLocation: bool, NoiseMaker: Actor): ...
    def OnRep_PlayerState(self): ...
    def OnRep_Controller(self): ...
    def LaunchPawn(self, LaunchVelocity: core_uobject.Vector, bXYOverride: bool, bZOverride: bool): ...
    def K2_GetMovementInputVector(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def IsPlayerControlled(self, ReturnValue: bool) -> bool: ...
    def IsMoveInputIgnored(self, ReturnValue: bool) -> bool: ...
    def IsLocallyControlled(self, ReturnValue: bool) -> bool: ...
    def IsControlled(self, ReturnValue: bool) -> bool: ...
    def GetPendingMovementInputVector(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetNavAgentLocation(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetMovementComponent(self, ReturnValue: PawnMovementComponent) -> PawnMovementComponent: ...
    def GetMovementBaseActor(self, Pawn: Pawn, ReturnValue: Actor) -> Actor: ...
    def GetLastMovementInputVector(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetControlRotation(self, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def GetController(self, ReturnValue: Controller) -> Controller: ...
    def GetBaseAimRotation(self, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def DetachFromControllerPendingDestroy(self): ...
    def ConsumeMovementInputVector(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def AddMovementInput(self, WorldDirection: core_uobject.Vector, ScaleValue: float, bForce: bool): ...
    def AddControllerYawInput(self, Val: float): ...
    def AddControllerRollInput(self, Val: float): ...
    def AddControllerPitchInput(self, Val: float): ...


class Character(Pawn):
    Mesh: SkeletalMeshComponent
    CharacterMovement: CharacterMovementComponent
    CapsuleComponent: CapsuleComponent
    BasedMovement: BasedMovementInfo
    ReplicatedBasedMovement: BasedMovementInfo
    AnimRootMotionTranslationScale: float
    BaseTranslationOffset: core_uobject.Vector
    BaseRotationOffset: core_uobject.Quat
    ReplicatedServerLastTransformUpdateTimeStamp: float
    ReplicatedMovementMode: int
    bInBaseReplication: bool
    CrouchedEyeHeight: float
    bIsCrouched: bool
    bProxyIsJumpForceApplied: bool
    bPressedJump: bool
    bClientUpdating: bool
    bClientWasFalling: bool
    bClientResimulateRootMotion: bool
    bClientResimulateRootMotionSources: bool
    bSimGravityDisabled: bool
    bClientCheckEncroachmentOnNetUpdate: bool
    bServerMoveIgnoreRootMotion: bool
    bWasJumping: bool
    JumpKeyHoldTime: float
    JumpForceTimeRemaining: float
    ProxyJumpForceStartedTime: float
    JumpMaxHoldTime: float
    JumpMaxCount: int
    JumpCurrentCount: int
    SavedRootMotion: RootMotionSourceGroup
    ClientRootMotionParams: RootMotionMovementParams
    RootMotionRepMoves: unreal.WrappedArray[SimulatedRootMotionReplicatedMove]
    RepRootMotion: RepRootMotionMontage
    AnimRootMotionTranslationScale3D: core_uobject.Vector
    def UnCrouch(self, bClientSimulation: bool): ...
    def StopJumping(self): ...
    def StopAnimMontage(self, AnimMontage: AnimMontage): ...
    def SetAnimRootMotionTranslationScale3D(self, InAnimRootMotionTranslationScale3D: core_uobject.Vector): ...
    def RootMotionDebugClientPrintOnScreen(self, inString: str): ...
    def PlayAnimMontage(self, AnimMontage: AnimMontage, InPlayRate: float, StartSectionName: str, ReturnValue: float) -> float: ...
    def OnWalkingOffLedge(self, PreviousFloorImpactNormal: core_uobject.Vector, PreviousFloorContactNormal: core_uobject.Vector, PreviousLocation: core_uobject.Vector, TimeDelta: float): ...
    def OnRep_RootMotion(self): ...
    def OnRep_ReplicatedBasedMovement(self): ...
    def OnRep_IsCrouched(self): ...
    def OnLaunched(self, LaunchVelocity: core_uobject.Vector, bXYOverride: bool, bZOverride: bool): ...
    def OnLanded(self, Hit: HitResult): ...
    def OnJumped(self): ...
    def LaunchCharacter(self, LaunchVelocity: core_uobject.Vector, bXYOverride: bool, bZOverride: bool): ...
    def K2_UpdateCustomMovement(self, DeltaTime: float): ...
    def K2_OnStartCrouch(self, HalfHeightAdjust: float, ScaledHalfHeightAdjust: float): ...
    def K2_OnMovementModeChanged(self, PrevMovementMode: int, NewMovementMode: int, PrevCustomMode: int, NewCustomMode: int): ...
    def K2_OnEndCrouch(self, HalfHeightAdjust: float, ScaledHalfHeightAdjust: float): ...
    def Jump(self): ...
    def IsPlayingRootMotion(self, ReturnValue: bool) -> bool: ...
    def IsPlayingNetworkedRootMotionMontage(self, ReturnValue: bool) -> bool: ...
    def IsJumpProvidingForce(self, ReturnValue: bool) -> bool: ...
    def GetCurrentMontage(self, ReturnValue: AnimMontage) -> AnimMontage: ...
    def GetBaseTranslationOffset(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetBaseRotationOffsetRotator(self, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def GetAnimRootMotionTranslationScale3D(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetAnimRootMotionTranslationScale(self, ReturnValue: float) -> float: ...
    def GetActorSocket(self, Actor: Actor, Socket: str, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def Crouch(self, bClientSimulation: bool): ...
    def ClientVeryShortAdjustPosition(self, Timestamp: float, NewLoc: core_uobject.Vector, NewBase: PrimitiveComponent, NewBaseBoneName: str, bHasBase: bool, bBaseRelativePosition: bool, ServerMovementMode: int): ...
    def ClientCheatWalk(self): ...
    def ClientCheatGhost(self): ...
    def ClientCheatFly(self): ...
    def ClientAdjustRootMotionSourcePosition(self, Timestamp: float, ServerRootMotion: RootMotionSourceGroup, bHasAnimRootMotion: bool, ServerMontageTrackPosition: float, ServerLoc: core_uobject.Vector, ServerRotation: Vector_NetQuantizeNormal, ServerVelZ: float, ServerBase: PrimitiveComponent, ServerBoneName: str, bHasBase: bool, bBaseRelativePosition: bool, ServerMovementMode: int): ...
    def ClientAdjustRootMotionPosition(self, Timestamp: float, ServerMontageTrackPosition: float, ServerLoc: core_uobject.Vector, ServerRotation: Vector_NetQuantizeNormal, ServerVelZ: float, ServerBase: PrimitiveComponent, ServerBoneName: str, bHasBase: bool, bBaseRelativePosition: bool, ServerMovementMode: int): ...
    def ClientAdjustPosition(self, Timestamp: float, NewLoc: core_uobject.Vector, NewVel: core_uobject.Vector, NewBase: PrimitiveComponent, NewBaseBoneName: str, bHasBase: bool, bBaseRelativePosition: bool, ServerMovementMode: int): ...
    def ClientAckGoodMove(self, Timestamp: float): ...
    def CanJumpInternal(self, ReturnValue: bool) -> bool: ...
    def CanJump(self, ReturnValue: bool) -> bool: ...
    def CacheInitialMeshOffset(self, MeshRelativeLocation: core_uobject.Vector, MeshRelativeRotation: core_uobject.Rotator): ...


class Info(Actor): ...


class Brush(Actor):
    BrushType: int
    BrushColor: core_uobject.Color
    PolyFlags: int
    bColored: bool
    bSolidWhenSelected: bool
    bPlaceableFromClassBrowser: bool
    bNotForClientOrServer: bool
    Brush: Model
    BrushComponent: BrushComponent
    bInManipulation: bool
    SavedSelections: unreal.WrappedArray[GeomSelection]



class Volume(Brush): ...


class MaterialExpression(unreal.UObject):
    Material: Material
    Function: MaterialFunction
    bIsParameterExpression: bool
    bImmuneToClean: bool



class MaterialExpressionTextureBase(MaterialExpression):
    Texture: Texture
    SamplerType: int
    IsDefaultMeshpaintTexture: bool



class MaterialExpressionTextureSample(MaterialExpressionTextureBase):
    Coordinates: ExpressionInput
    TextureArrayIndex: ExpressionInput
    TextureObject: ExpressionInput
    MipValue: ExpressionInput
    CoordinatesDX: ExpressionInput
    CoordinatesDY: ExpressionInput
    AutomaticViewMipBiasValue: ExpressionInput
    MipValueMode: int
    SamplerSource: int
    ConstMipValue: int
    AutomaticViewMipBias: bool



class MaterialExpressionTextureSampleParameter(MaterialExpressionTextureSample):
    ParameterName: str
    ExpressionGUID: core_uobject.Guid
    Group: str



class MaterialExpressionTextureSampleParameter2D(MaterialExpressionTextureSampleParameter): ...


class SplineComponent(PrimitiveComponent):
    SplineCurves: SplineCurves
    SplineInfo: core_uobject.InterpCurveVector
    SplineRotInfo: core_uobject.InterpCurveQuat
    SplineScaleInfo: core_uobject.InterpCurveVector
    SplineReparamTable: core_uobject.InterpCurveFloat
    bAllowSplineEditingPerInstance: bool
    ReparamStepsPerSegment: int
    Duration: float
    bStationaryEndpoints: bool
    bSplineHasBeenEdited: bool
    bModifiedByConstructionScript: bool
    bInputSplinePointsToConstructionScript: bool
    bDrawDebug: bool
    bClosedLoop: bool
    bLoopPositionOverride: bool
    LoopPosition: float
    DefaultUpVector: core_uobject.Vector
    def UpdateSpline(self): ...
    def SetWorldLocationAtSplinePoint(self, PointIndex: int, InLocation: core_uobject.Vector): ...
    def SetUpVectorAtSplinePoint(self, PointIndex: int, InUpVector: core_uobject.Vector, CoordinateSpace: int, bUpdateSpline: bool): ...
    def SetUnselectedSplineSegmentColor(self, SegmentColor: core_uobject.LinearColor): ...
    def SetTangentsAtSplinePoint(self, PointIndex: int, InArriveTangent: core_uobject.Vector, InLeaveTangent: core_uobject.Vector, CoordinateSpace: int, bUpdateSpline: bool): ...
    def SetTangentAtSplinePoint(self, PointIndex: int, InTangent: core_uobject.Vector, CoordinateSpace: int, bUpdateSpline: bool): ...
    def SetSplineWorldPoints(self, Points: unreal.WrappedArray[core_uobject.Vector]): ...
    def SetSplinePointType(self, PointIndex: int, Type: int, bUpdateSpline: bool): ...
    def SetSplinePoints(self, Points: unreal.WrappedArray[core_uobject.Vector], CoordinateSpace: int, bUpdateSpline: bool): ...
    def SetSplineLocalPoints(self, Points: unreal.WrappedArray[core_uobject.Vector]): ...
    def SetSelectedSplineSegmentColor(self, SegmentColor: core_uobject.LinearColor): ...
    def SetLocationAtSplinePoint(self, PointIndex: int, InLocation: core_uobject.Vector, CoordinateSpace: int, bUpdateSpline: bool): ...
    def SetDrawDebug(self, bShow: bool): ...
    def SetDefaultUpVector(self, UpVector: core_uobject.Vector, CoordinateSpace: int): ...
    def SetClosedLoopAtPosition(self, bInClosedLoop: bool, Key: float, bUpdateSpline: bool): ...
    def SetClosedLoop(self, bInClosedLoop: bool, bUpdateSpline: bool): ...
    def RemoveSplinePoint(self, Index: int, bUpdateSpline: bool): ...
    def IsClosedLoop(self, ReturnValue: bool) -> bool: ...
    def GetWorldTangentAtDistanceAlongSpline(self, Distance: float, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetWorldRotationAtTime(self, Time: float, bUseConstantVelocity: bool, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def GetWorldRotationAtDistanceAlongSpline(self, Distance: float, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def GetWorldLocationAtTime(self, Time: float, bUseConstantVelocity: bool, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetWorldLocationAtSplinePoint(self, PointIndex: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetWorldLocationAtDistanceAlongSpline(self, Distance: float, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetWorldDirectionAtTime(self, Time: float, bUseConstantVelocity: bool, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetWorldDirectionAtDistanceAlongSpline(self, Distance: float, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetUpVectorAtTime(self, Time: float, CoordinateSpace: int, bUseConstantVelocity: bool, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetUpVectorAtSplinePoint(self, PointIndex: int, CoordinateSpace: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetUpVectorAtDistanceAlongSpline(self, Distance: float, CoordinateSpace: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetTransformAtTime(self, Time: float, CoordinateSpace: int, bUseConstantVelocity: bool, bUseScale: bool, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def GetTransformAtSplinePoint(self, PointIndex: int, CoordinateSpace: int, bUseScale: bool, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def GetTransformAtDistanceAlongSpline(self, Distance: float, CoordinateSpace: int, bUseScale: bool, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def GetTangentAtTime(self, Time: float, CoordinateSpace: int, bUseConstantVelocity: bool, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetTangentAtSplinePoint(self, PointIndex: int, CoordinateSpace: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetTangentAtDistanceAlongSpline(self, Distance: float, CoordinateSpace: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetSplinePointType(self, PointIndex: int, ReturnValue: int) -> int: ...
    def GetSplineLength(self, ReturnValue: float) -> float: ...
    def GetScaleAtTime(self, Time: float, bUseConstantVelocity: bool, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetScaleAtSplinePoint(self, PointIndex: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetScaleAtDistanceAlongSpline(self, Distance: float, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetRotationAtTime(self, Time: float, CoordinateSpace: int, bUseConstantVelocity: bool, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def GetRotationAtSplinePoint(self, PointIndex: int, CoordinateSpace: int, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def GetRotationAtDistanceAlongSpline(self, Distance: float, CoordinateSpace: int, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def GetRollAtTime(self, Time: float, CoordinateSpace: int, bUseConstantVelocity: bool, ReturnValue: float) -> float: ...
    def GetRollAtSplinePoint(self, PointIndex: int, CoordinateSpace: int, ReturnValue: float) -> float: ...
    def GetRollAtDistanceAlongSpline(self, Distance: float, CoordinateSpace: int, ReturnValue: float) -> float: ...
    def GetRightVectorAtTime(self, Time: float, CoordinateSpace: int, bUseConstantVelocity: bool, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetRightVectorAtSplinePoint(self, PointIndex: int, CoordinateSpace: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetRightVectorAtDistanceAlongSpline(self, Distance: float, CoordinateSpace: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetNumberOfSplinePoints(self, ReturnValue: int) -> int: ...
    def GetLocationAtTime(self, Time: float, CoordinateSpace: int, bUseConstantVelocity: bool, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetLocationAtSplinePoint(self, PointIndex: int, CoordinateSpace: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetLocationAtDistanceAlongSpline(self, Distance: float, CoordinateSpace: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetLocationAndTangentAtSplinePoint(self, PointIndex: int, Location: core_uobject.Vector, Tangent: core_uobject.Vector, CoordinateSpace: int): ...
    def GetLocalLocationAndTangentAtSplinePoint(self, PointIndex: int, LocalLocation: core_uobject.Vector, LocalTangent: core_uobject.Vector): ...
    def GetLeaveTangentAtSplinePoint(self, PointIndex: int, CoordinateSpace: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetInputKeyAtDistanceAlongSpline(self, Distance: float, ReturnValue: float) -> float: ...
    def GetDistanceAlongSplineAtSplinePoint(self, PointIndex: int, ReturnValue: float) -> float: ...
    def GetDirectionAtTime(self, Time: float, CoordinateSpace: int, bUseConstantVelocity: bool, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetDirectionAtSplinePoint(self, PointIndex: int, CoordinateSpace: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetDirectionAtDistanceAlongSpline(self, Distance: float, CoordinateSpace: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetDefaultUpVector(self, CoordinateSpace: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetArriveTangentAtSplinePoint(self, PointIndex: int, CoordinateSpace: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def FindUpVectorClosestToWorldLocation(self, WorldLocation: core_uobject.Vector, CoordinateSpace: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def FindTransformClosestToWorldLocation(self, WorldLocation: core_uobject.Vector, CoordinateSpace: int, bUseScale: bool, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def FindTangentClosestToWorldLocation(self, WorldLocation: core_uobject.Vector, CoordinateSpace: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def FindScaleClosestToWorldLocation(self, WorldLocation: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def FindRotationClosestToWorldLocation(self, WorldLocation: core_uobject.Vector, CoordinateSpace: int, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def FindRollClosestToWorldLocation(self, WorldLocation: core_uobject.Vector, CoordinateSpace: int, ReturnValue: float) -> float: ...
    def FindRightVectorClosestToWorldLocation(self, WorldLocation: core_uobject.Vector, CoordinateSpace: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def FindLocationClosestToWorldLocation(self, WorldLocation: core_uobject.Vector, CoordinateSpace: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def FindInputKeyClosestToWorldLocation(self, WorldLocation: core_uobject.Vector, ReturnValue: float) -> float: ...
    def FindDirectionClosestToWorldLocation(self, WorldLocation: core_uobject.Vector, CoordinateSpace: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def ClearSplinePoints(self, bUpdateSpline: bool): ...
    def AddSplineWorldPoint(self, Position: core_uobject.Vector): ...
    def AddSplinePointWithRotationAtIndex(self, Position: core_uobject.Vector, Rotation: core_uobject.Rotator, Index: int, CoordinateSpace: int, bUpdateSpline: bool): ...
    def AddSplinePointAtIndex(self, Position: core_uobject.Vector, Index: int, CoordinateSpace: int, bUpdateSpline: bool): ...
    def AddSplinePoint(self, Position: core_uobject.Vector, CoordinateSpace: int, bUpdateSpline: bool): ...
    def AddSplineLocalPoint(self, Position: core_uobject.Vector): ...
    def AddPoints(self, Points: unreal.WrappedArray[SplinePoint], bUpdateSpline: bool): ...
    def AddPoint(self, Point: SplinePoint, bUpdateSpline: bool): ...


class AnimCompress(unreal.UObject):
    Description: str
    bNeedsSkeleton: bool
    TranslationCompressionFormat: int
    RotationCompressionFormat: int
    ScaleCompressionFormat: int
    MaxCurveError: float



class SkeletalMeshComponent(SkinnedMeshComponent):
    AnimBlueprintGeneratedClass: AnimBlueprintGeneratedClass
    AnimClass: unreal.UClass
    AnimScriptInstance: AnimInstance
    SubInstances: unreal.WrappedArray[AnimInstance]
    PostProcessAnimInstance: AnimInstance
    bDisablePostProcessBlueprint: bool
    AnimationData: SingleAnimationPlayData
    RootBoneTranslation: core_uobject.Vector
    LineCheckBoundsScale: core_uobject.Vector
    CachedBoneSpaceTransforms: unreal.WrappedArray[core_uobject.Transform]
    CachedComponentSpaceTransforms: unreal.WrappedArray[core_uobject.Transform]
    GlobalAnimRateScale: float
    UseAsyncScene: EDynamicActorScene
    KinematicBonesUpdateType: int
    PhysicsTransformUpdateMode: int
    AnimationMode: int
    bHasValidBodies: bool
    bBlendPhysics: bool
    bEnablePhysicsOnDedicatedServer: bool
    bUpdateJointsFromAnimation: bool
    bDisableClothSimulation: bool
    bAllowAnimCurveEvaluation: bool
    bDisableAnimCurves: bool
    bCollideWithEnvironment: bool
    bCollideWithAttachedChildren: bool
    bLocalSpaceSimulation: bool
    bResetAfterTeleport: bool
    bDeferMovementFromSceneQueries: bool
    bNoSkeletonUpdate: bool
    bPauseAnims: bool
    bUseRefPoseOnInitAnim: bool
    bEnablePerPolyCollision: bool
    bForceRefpose: bool
    bOnlyAllowAutonomousTickPose: bool
    bIsAutonomousTickPose: bool
    bOldForceRefPose: bool
    bShowPrePhysBones: bool
    bRequiredBonesUpToDate: bool
    bAnimTreeInitialised: bool
    bIncludeComponentLocationIntoBounds: bool
    bEnableLineCheckWithBounds: bool
    bNeedsQueuedAnimEventsDispatched: bool
    DisallowedAnimCurves: unreal.WrappedArray[str]
    ClothBlendWeight: float
    EdgeStiffness: float
    BendingStiffness: float
    AreaStiffness: float
    VolumeStiffness: float
    StrainLimitingStiffness: float
    ShapeTargetStiffness: float
    bUseBendingElements: bool
    bUseTetrahedralConstraints: bool
    bUseThinShellVolumeConstraints: bool
    bUseSelfCollisions: bool
    bUseContinuousCollisionDetection: bool
    BodySetup: BodySetup
    ClothMaxDistanceScale: float
    ClothingSimulationFactory: unreal.UClass
    TeleportDistanceThreshold: float
    TeleportRotationThreshold: float
    ClothingInteractor: clothing_system_runtime_interface.ClothingSimulationInteractor
    WindInfluenceMultiplier: float
    bAnimInstanceNeedsReinit: bool
    bSkipMassComputationOnInit: bool
    bNeverInterpolateSkippedFrames: bool
    bEnableSleepingTickOptimization: bool
    AnimSets: unreal.WrappedArray[GbxAnimSetPair]
    bRecomputeJointAnchorPoseOnBodyScale: bool
    def UnbindClothFromMasterPoseComponent(self, bRestoreSimulationSpace: bool): ...
    def ToggleDisablePostProcessBlueprint(self): ...
    def TermBodiesBelow(self, ParentBoneName: str): ...
    def SuspendClothingSimulation(self): ...
    def Stop(self): ...
    def SnapshotPose(self, Snapshot: PoseSnapshot): ...
    def SetUpdateAnimationInEditor(self, NewUpdateState: bool): ...
    def SetTeleportRotationThreshold(self, Threshold: float): ...
    def SetTeleportDistanceThreshold(self, Threshold: float): ...
    def SetPosition(self, InPos: float, bFireNotifies: bool): ...
    def SetPlayRate(self, Rate: float): ...
    def SetPhysicsBlendWeight(self, PhysicsBlendWeight: float): ...
    def SetPauseAnims(self, bPaused: bool): ...
    def SetNotifyRigidBodyCollisionBelow(self, bNewNotifyRigidBodyCollision: bool, BoneName: str, bIncludeSelf: bool): ...
    def SetMorphTarget(self, MorphTargetName: str, Value: float, bRemoveZeroWeight: bool): ...
    def SetEnablePhysicsBlending(self, bNewBlendPhysics: bool): ...
    def SetEnableGravityOnAllBodiesBelow(self, bEnableGravity: bool, BoneName: str, bIncludeSelf: bool): ...
    def SetEnableBodyGravity(self, bEnableGravity: bool, BoneName: str): ...
    def SetDisablePostProcessBlueprint(self, bInDisablePostProcess: bool): ...
    def SetDisableAnimCurves(self, bInDisableAnimCurves: bool): ...
    def SetConstraintProfileForAll(self, ProfileName: str, bDefaultIfNotFound: bool): ...
    def SetConstraintProfile(self, JointName: str, ProfileName: str, bDefaultIfNotFound: bool): ...
    def SetCollisionResponse(self, CollisionEnabled: int, BodyName: str, bIncludeChildren: bool): ...
    def SetClothMaxDistanceScale(self, Scale: float): ...
    def SetBodyNotifyRigidBodyCollision(self, bNewNotifyRigidBodyCollision: bool, BoneName: str): ...
    def SetAnimationMode(self, InAnimationMode: int): ...
    def SetAnimation(self, NewAnimToPlay: AnimationAsset): ...
    def SetAngularLimits(self, InBoneName: str, Swing1LimitAngle: float, TwistLimitAngle: float, Swing2LimitAngle: float): ...
    def SetAllowedAnimCurvesEvaluation(self, List: unreal.WrappedArray[str], bAllow: bool): ...
    def SetAllowAnimCurveEvaluation(self, bInAllow: bool): ...
    def SetAllMotorsAngularVelocityDrive(self, bEnableSwingDrive: bool, bEnableTwistDrive: bool, bSkipCustomPhysicsType: bool): ...
    def SetAllMotorsAngularPositionDrive(self, bEnableSwingDrive: bool, bEnableTwistDrive: bool, bSkipCustomPhysicsType: bool): ...
    def SetAllMotorsAngularDriveParams(self, InSpring: float, InDamping: float, InForceLimit: float, bSkipCustomPhysicsType: bool): ...
    def SetAllBodiesSimulatePhysics(self, bNewSimulate: bool): ...
    def SetAllBodiesPhysicsBlendWeight(self, PhysicsBlendWeight: float, bSkipCustomPhysicsType: bool): ...
    def SetAllBodiesBelowSimulatePhysics(self, InBoneName: str, bNewSimulate: bool, bIncludeSelf: bool): ...
    def SetAllBodiesBelowPhysicsBlendWeight(self, InBoneName: str, PhysicsBlendWeight: float, bSkipCustomPhysicsType: bool, bIncludeSelf: bool): ...
    def ResumeClothingSimulation(self): ...
    def ResetClothTeleportMode(self): ...
    def ResetAnimInstanceDynamics(self, InTeleportType: ETeleportType): ...
    def ResetAllowedAnimCurveEvaluation(self): ...
    def ResetAllBodiesSimulatePhysics(self): ...
    def PlaySingleAnimation(self, InAnimToPlay: AnimationAsset, bIsLooping: bool, bIsPlaying: bool, Position: float, PlayRate: float): ...
    def PlayAnimation(self, NewAnimToPlay: AnimationAsset, bLooping: bool): ...
    def Play(self, bLooping: bool): ...
    def OverrideAnimationData(self, InAnimToPlay: AnimationAsset, bIsLooping: bool, bIsPlaying: bool, Position: float, PlayRate: float): ...
    def K2_SetAnimInstanceClass(self, NewClass: unreal.UClass): ...
    def K2_GetClosestPointOnPhysicsAsset(self, WorldPosition: core_uobject.Vector, ClosestWorldPosition: core_uobject.Vector, Normal: core_uobject.Vector, BoneName: str, Distance: float, ReturnValue: bool) -> bool: ...
    def IsPlaying(self, ReturnValue: bool) -> bool: ...
    def IsClothingSimulationSuspended(self, ReturnValue: bool) -> bool: ...
    def IsBodyGravityEnabled(self, BoneName: str, ReturnValue: bool) -> bool: ...
    def HasValidAnimationInstance(self, ReturnValue: bool) -> bool: ...
    def GetTeleportRotationThreshold(self, ReturnValue: float) -> float: ...
    def GetTeleportDistanceThreshold(self, ReturnValue: float) -> float: ...
    def GetSkeletalCenterOfMass(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetPostProcessInstance(self, ReturnValue: AnimInstance) -> AnimInstance: ...
    def GetPosition(self, ReturnValue: float) -> float: ...
    def GetPlayRate(self, ReturnValue: float) -> float: ...
    def GetMorphTarget(self, MorphTargetName: str, ReturnValue: float) -> float: ...
    def GetDisablePostProcessBlueprint(self, ReturnValue: bool) -> bool: ...
    def GetDisableAnimCurves(self, ReturnValue: bool) -> bool: ...
    def GetCurrentJointAngles(self, InBoneName: str, Swing1Angle: float, TwistAngle: float, Swing2Angle: float): ...
    def GetClothMaxDistanceScale(self, ReturnValue: float) -> float: ...
    def GetClothingSimulationInteractor(self, ReturnValue: clothing_system_runtime_interface.ClothingSimulationInteractor) -> clothing_system_runtime_interface.ClothingSimulationInteractor: ...
    def GetBoneMass(self, BoneName: str, bScaleMass: bool, ReturnValue: float) -> float: ...
    def GetAnimInstance(self, ReturnValue: AnimInstance) -> AnimInstance: ...
    def GetAnimationMode(self, ReturnValue: int) -> int: ...
    def GetAllowedAnimCurveEvaluate(self, ReturnValue: bool) -> bool: ...
    def ForceClothNextUpdateTeleportAndReset(self): ...
    def ForceClothNextUpdateTeleport(self): ...
    def FindConstraintBoneName(self, ConstraintIndex: int, ReturnValue: str) -> str: ...
    def EnableTickingDueToWake(self, WakingComponent: PrimitiveComponent, BoneName: str): ...
    def EnableAnimSetByGenericName(self, GenericName: str): ...
    def EnableAnimSet(self, AnimSet: GbxAnimSet): ...
    def DisableTickingDueToSleep(self, SleepingComponent: PrimitiveComponent, BoneName: str): ...
    def DisableAnimSetByGenericName(self, GenericName: str): ...
    def DisableAnimSet(self, AnimSet: GbxAnimSet): ...
    def ClearMorphTargets(self): ...
    def BreakConstraint(self, Impulse: core_uobject.Vector, HitLocation: core_uobject.Vector, InBoneName: str): ...
    def BindClothToMasterPoseComponent(self): ...
    def AllowAnimCurveEvaluation(self, NameOfCurve: str, bAllow: bool): ...
    def AddImpulseToAllBodiesBelow(self, Impulse: core_uobject.Vector, BoneName: str, bVelChange: bool, bIncludeSelf: bool): ...
    def AddForceToAllBodiesBelow(self, Force: core_uobject.Vector, BoneName: str, bAccelChange: bool, bIncludeSelf: bool): ...
    def AccumulateAllBodiesBelowPhysicsBlendWeight(self, InBoneName: str, AddPhysicsBlendWeight: float, bSkipCustomPhysicsType: bool): ...


class AnimInstance(unreal.UObject):
    CurrentSkeleton: Skeleton
    RootMotionMode: int
    bUseMultiThreadedAnimationUpdate: bool
    bUsingCopyPoseFromMesh: bool
    bQueueMontageEvents: bool
    NotifyQueue: AnimNotifyQueue
    AnimationEndedNotifies: unreal.WrappedArray[AnimationAsset]
    ActiveAnimNotifyState: unreal.WrappedArray[AnimNotifyEvent]
    AnimSets: unreal.WrappedArray[GbxAnimSetPair]
    AnimSetStack: unreal.WrappedArray[GbxAnimSet]
    def UnlockAIResources(self, bUnlockMovement: bool, UnlockAILogic: bool): ...
    def TryGetPawnOwner(self, ReturnValue: Pawn) -> Pawn: ...
    def StopSlotAnimation(self, InBlendOutTime: float, SlotNodeName: str): ...
    def SnapshotPose(self, Snapshot: PoseSnapshot): ...
    def SetRootMotionMode(self, Value: int): ...
    def SetMorphTarget(self, MorphTargetName: str, Value: float): ...
    def SavePoseSnapshot(self, SnapshotName: str): ...
    def ResetDynamics(self, InTeleportType: ETeleportType): ...
    def PlaySlotAnimationAsDynamicMontage(self, Asset: AnimSequenceBase, SlotNodeName: str, BlendInTime: float, BlendOutTime: float, InPlayRate: float, LoopCount: int, BlendOutTriggerTime: float, InTimeToStartMontageAt: float, ReturnValue: AnimMontage) -> AnimMontage: ...
    def PlaySlotAnimation(self, Asset: AnimSequenceBase, SlotNodeName: str, BlendInTime: float, BlendOutTime: float, InPlayRate: float, LoopCount: int, ReturnValue: float) -> float: ...
    def Montage_Stop(self, InBlendOutTime: float, Montage: AnimMontage): ...
    def Montage_SetPosition(self, Montage: AnimMontage, NewPosition: float): ...
    def Montage_SetPlayRate(self, Montage: AnimMontage, NewPlayRate: float): ...
    def Montage_SetNextSection(self, SectionNameToChange: str, NextSection: str, Montage: AnimMontage): ...
    def Montage_Resume(self, Montage: AnimMontage): ...
    def Montage_Play(self, MontageToPlay: AnimMontage, InPlayRate: float, ReturnValueType: EMontagePlayReturnType, InTimeToStartMontageAt: float, bStopAllMontages: bool, BlendInOverride: float, BlendOutOverride: float, ReturnValue: float) -> float: ...
    def Montage_Pause(self, Montage: AnimMontage): ...
    def Montage_JumpToSectionsEnd(self, SectionName: str, Montage: AnimMontage): ...
    def Montage_JumpToSection(self, SectionName: str, Montage: AnimMontage): ...
    def Montage_IsPlaying(self, Montage: AnimMontage, bIncludeInactiveInstances: bool, ReturnValue: bool) -> bool: ...
    def Montage_IsActive(self, Montage: AnimMontage, ReturnValue: bool) -> bool: ...
    def Montage_GetPosition(self, Montage: AnimMontage, bIncludeInactiveInstances: bool, ReturnValue: float) -> float: ...
    def Montage_GetPlayRate(self, Montage: AnimMontage, ReturnValue: float) -> float: ...
    def Montage_GetIsStopped(self, Montage: AnimMontage, ReturnValue: bool) -> bool: ...
    def Montage_GetCurrentSection(self, Montage: AnimMontage, ReturnValue: str) -> str: ...
    def Montage_GetBlendTime(self, Montage: AnimMontage, ReturnValue: float) -> float: ...
    def LockAIResources(self, bLockMovement: bool, LockAILogic: bool): ...
    def IsSyncGroupBetweenMarkers(self, InSyncGroupName: str, PreviousMarker: str, NextMarker: str, bRespectMarkerOrder: bool, ReturnValue: bool) -> bool: ...
    def IsPlayingSlotAnimation(self, Asset: AnimSequenceBase, SlotNodeName: str, ReturnValue: bool) -> bool: ...
    def IsAnyMontagePlaying(self, ReturnValue: bool) -> bool: ...
    def IsAnyBlendSpaceInstancePlaying(self, ReturnValue: bool) -> bool: ...
    def HasMarkerBeenHitThisFrame(self, SyncGroup: str, MarkerName: str, ReturnValue: bool) -> bool: ...
    def GetTimeToClosestMarker(self, SyncGroup: str, MarkerName: str, OutMarkerTime: float, ReturnValue: bool) -> bool: ...
    def GetSyncGroupPosition(self, InSyncGroupName: str, ReturnValue: MarkerSyncAnimPosition) -> MarkerSyncAnimPosition: ...
    def GetRelevantAnimTimeRemainingFraction(self, MachineIndex: int, StateIndex: int, ReturnValue: float) -> float: ...
    def GetRelevantAnimTimeRemaining(self, MachineIndex: int, StateIndex: int, ReturnValue: float) -> float: ...
    def GetRelevantAnimTimeFraction(self, MachineIndex: int, StateIndex: int, ReturnValue: float) -> float: ...
    def GetRelevantAnimTime(self, MachineIndex: int, StateIndex: int, ReturnValue: float) -> float: ...
    def GetRelevantAnimRootMotionRemaining(self, MachineIndex: int, StateIndex: int, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def GetRelevantAnimLength(self, MachineIndex: int, StateIndex: int, ReturnValue: float) -> float: ...
    def GetOwningComponent(self, ReturnValue: SkeletalMeshComponent) -> SkeletalMeshComponent: ...
    def GetOwningActor(self, ReturnValue: Actor) -> Actor: ...
    def GetInstanceTransitionTimeElapsedFraction(self, MachineIndex: int, TransitionIndex: int, ReturnValue: float) -> float: ...
    def GetInstanceTransitionTimeElapsed(self, MachineIndex: int, TransitionIndex: int, ReturnValue: float) -> float: ...
    def GetInstanceTransitionCrossfadeDuration(self, MachineIndex: int, TransitionIndex: int, ReturnValue: float) -> float: ...
    def GetInstanceStateWeight(self, MachineIndex: int, StateIndex: int, ReturnValue: float) -> float: ...
    def GetInstanceMachineWeight(self, MachineIndex: int, ReturnValue: float) -> float: ...
    def GetInstanceCurrentStateElapsedTime(self, MachineIndex: int, ReturnValue: float) -> float: ...
    def GetInstanceAssetPlayerTimeFromEndFraction(self, AssetPlayerIndex: int, ReturnValue: float) -> float: ...
    def GetInstanceAssetPlayerTimeFromEnd(self, AssetPlayerIndex: int, ReturnValue: float) -> float: ...
    def GetInstanceAssetPlayerTimeFraction(self, AssetPlayerIndex: int, ReturnValue: float) -> float: ...
    def GetInstanceAssetPlayerTime(self, AssetPlayerIndex: int, ReturnValue: float) -> float: ...
    def GetInstanceAssetPlayerLength(self, AssetPlayerIndex: int, ReturnValue: float) -> float: ...
    def GetCurveValue(self, CurveName: str, ReturnValue: float) -> float: ...
    def GetCurrentStateName(self, MachineIndex: int, ReturnValue: str) -> str: ...
    def GetCurrentActiveMontage(self, ReturnValue: AnimMontage) -> AnimMontage: ...
    def GetBlendSpaceBaseFromAnimSet(self, AnimAssetName: str, bIsValid: bool, ReturnValue: BlendSpaceBase) -> BlendSpaceBase: ...
    def GetAnimSeqBaseFromAnimSet(self, AnimAssetName: str, bIsValid: bool, ReturnValue: AnimSequenceBase) -> AnimSequenceBase: ...
    def GetAnimationSlotWeight(self, SlotNodeName: str, ReturnValue: float) -> float: ...
    def GetAllCurveNames(self, OutNames: unreal.WrappedArray[str]): ...
    def GetActiveCurveNames(self, CurveType: EAnimCurveType, OutNames: unreal.WrappedArray[str]): ...
    def EnableAnimSetByGenericName(self, GenericName: str): ...
    def EnableAnimSet(self, AnimSet: GbxAnimSet): ...
    def DoesCurveExist(self, CurveName: str, ReturnValue: bool) -> bool: ...
    def DisableAnimSetByGenericName(self, GenericName: str): ...
    def DisableAnimSet(self, AnimSet: GbxAnimSet): ...
    def ClearMorphTargets(self): ...
    def CalculateDirection(self, Velocity: core_uobject.Vector, BaseRotation: core_uobject.Rotator, ReturnValue: float) -> float: ...
    def BlueprintUpdateAnimation(self, DeltaTimeX: float): ...
    def BlueprintPostEvaluateAnimation(self): ...
    def BlueprintInitializeAnimation(self): ...
    def BlueprintBeginPlay(self): ...


class AudioComponent(SceneComponent):
    Sound: SoundBase
    InstanceParameters: unreal.WrappedArray[AudioComponentParam]
    SoundClassOverride: SoundClass
    bAutoDestroy: bool
    bStopWhenOwnerDestroyed: bool
    bShouldRemainActiveIfDropped: bool
    bAllowSpatialization: bool
    bOverrideAttenuation: bool
    bOverrideSubtitlePriority: bool
    bIsUISound: bool
    bEnableLowPassFilter: bool
    bOverridePriority: bool
    bSuppressSubtitles: bool
    bAutoManageAttachment: bool
    AudioComponentUserID: str
    PitchModulationMin: float
    PitchModulationMax: float
    VolumeModulationMin: float
    VolumeModulationMax: float
    VolumeMultiplier: float
    EnvelopeFollowerAttackTime: int
    EnvelopeFollowerReleaseTime: int
    Priority: float
    SubtitlePriority: float
    PitchMultiplier: float
    LowPassFilterFrequency: float
    AttenuationSettings: SoundAttenuation
    AttenuationOverrides: SoundAttenuationSettings
    ConcurrencySettings: SoundConcurrency
    AutoAttachLocationRule: EAttachmentRule
    AutoAttachRotationRule: EAttachmentRule
    AutoAttachScaleRule: EAttachmentRule
    AutoAttachParent: SceneComponent
    AutoAttachSocketName: str
    def Stop(self): ...
    def SetWaveParameter(self, InName: str, InWave: SoundWave): ...
    def SetVolumeMultiplier(self, NewVolumeMultiplier: float): ...
    def SetUISound(self, bInUISound: bool): ...
    def SetSubmixSend(self, Submix: SoundSubmix, SendLevel: float): ...
    def SetSound(self, NewSound: SoundBase): ...
    def SetPitchMultiplier(self, NewPitchMultiplier: float): ...
    def SetPaused(self, bPause: bool): ...
    def SetLowPassFilterFrequency(self, InLowPassFilterFrequency: float): ...
    def SetLowPassFilterEnabled(self, InLowPassFilterEnabled: bool): ...
    def SetIntParameter(self, InName: str, inInt: int): ...
    def SetFloatParameter(self, InName: str, InFloat: float): ...
    def SetBoolParameter(self, InName: str, InBool: bool): ...
    def Play(self, StartTime: float): ...
    def IsPlaying(self, ReturnValue: bool) -> bool: ...
    def FadeOut(self, FadeOutDuration: float, FadeVolumeLevel: float): ...
    def FadeIn(self, FadeInDuration: float, FadeVolumeLevel: float, StartTime: float): ...
    def BP_GetAttenuationSettingsToApply(self, OutAttenuationSettings: SoundAttenuationSettings, ReturnValue: bool) -> bool: ...
    def AdjustVolume(self, AdjustVolumeDuration: float, AdjustVolumeLevel: float): ...
    def AdjustAttenuation(self, InAttenuationSettings: SoundAttenuationSettings): ...


class AssetImportData(unreal.UObject): ...


class AssetUserData(unreal.UObject): ...


class MovementComponent(ActorComponent):
    UpdatedComponent: SceneComponent
    UpdatedPrimitive: PrimitiveComponent
    Velocity: core_uobject.Vector
    bConstrainToPlane: bool
    bSnapToPlaneAtStart: bool
    PlaneConstraintAxisSetting: EPlaneConstraintAxisSetting
    PlaneConstraintNormal: core_uobject.Vector
    PlaneConstraintOrigin: core_uobject.Vector
    bUpdateOnlyIfRendered: bool
    bAutoUpdateTickRegistration: bool
    bTickBeforeOwner: bool
    bAutoRegisterUpdatedComponent: bool
    def StopMovementImmediately(self): ...
    def SnapUpdatedComponentToPlane(self): ...
    def SetUpdatedComponent(self, NewUpdatedComponent: SceneComponent): ...
    def SetPlaneConstraintOrigin(self, PlaneOrigin: core_uobject.Vector): ...
    def SetPlaneConstraintNormal(self, PlaneNormal: core_uobject.Vector): ...
    def SetPlaneConstraintFromVectors(self, Forward: core_uobject.Vector, Up: core_uobject.Vector): ...
    def SetPlaneConstraintEnabled(self, bEnabled: bool): ...
    def SetPlaneConstraintAxisSetting(self, NewAxisSetting: EPlaneConstraintAxisSetting): ...
    def PhysicsVolumeChanged(self, NewVolume: PhysicsVolume): ...
    def K2_MoveUpdatedComponent(self, Delta: core_uobject.Vector, NewRotation: core_uobject.Rotator, OutHit: HitResult, bSweep: bool, bTeleport: bool, ReturnValue: bool) -> bool: ...
    def K2_GetModifiedMaxSpeed(self, ReturnValue: float) -> float: ...
    def K2_GetMaxSpeedModifier(self, ReturnValue: float) -> float: ...
    def IsExceedingMaxSpeed(self, MaxSpeed: float, ReturnValue: bool) -> bool: ...
    def GetPlaneConstraintOrigin(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetPlaneConstraintNormal(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetPlaneConstraintAxisSetting(self, ReturnValue: EPlaneConstraintAxisSetting) -> EPlaneConstraintAxisSetting: ...
    def GetPhysicsVolume(self, ReturnValue: PhysicsVolume) -> PhysicsVolume: ...
    def GetMaxSpeed(self, ReturnValue: float) -> float: ...
    def GetGravityZ(self, ReturnValue: float) -> float: ...
    def ConstrainNormalToPlane(self, Normal: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def ConstrainLocationToPlane(self, Location: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def ConstrainDirectionToPlane(self, Direction: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...


class NavMovementComponent(MovementComponent):
    NavAgentProps: NavAgentProperties
    FixedPathBrakingDistance: float
    bUpdateNavAgentWithOwnersCollision: bool
    bUseAccelerationForPaths: bool
    bUseFixedBrakingDistanceForPaths: bool
    PathFollowingComp: unreal.UObject
    MovementState: MovementProperties
    def StopMovementKeepPathing(self): ...
    def StopActiveMovement(self): ...
    def IsSwimming(self, ReturnValue: bool) -> bool: ...
    def IsMovingOnGround(self, ReturnValue: bool) -> bool: ...
    def IsFlying(self, ReturnValue: bool) -> bool: ...
    def IsFalling(self, ReturnValue: bool) -> bool: ...
    def IsCrouching(self, ReturnValue: bool) -> bool: ...


class PawnMovementComponent(NavMovementComponent):
    PawnOwner: Pawn
    def K2_GetInputVector(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def IsMoveInputIgnored(self, ReturnValue: bool) -> bool: ...
    def GetPendingInputVector(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetPawnOwner(self, ReturnValue: Pawn) -> Pawn: ...
    def GetLastInputVector(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def ConsumeInputVector(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def AddInputVector(self, WorldVector: core_uobject.Vector, bForce: bool): ...


class ChildActorComponent(SceneComponent):
    ChildActorClass: unreal.UClass
    ChildActor: Actor
    ChildActorTemplate: Actor
    def SetChildActorClass(self, InClass: unreal.UClass): ...


class ShapeComponent(PrimitiveComponent):
    ShapeColor: core_uobject.Color
    ShapeBodySetup: BodySetup
    bDrawOnlyIfSelected: bool
    bShouldCollideWhenPlacing: bool
    bDynamicObstacle: bool
    AreaClass: unreal.UClass



class BoxComponent(ShapeComponent):
    BoxExtent: core_uobject.Vector
    def SetBoxExtent(self, InBoxExtent: core_uobject.Vector, bUpdateOverlaps: bool): ...
    def GetUnscaledBoxExtent(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetScaledBoxExtent(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...


class TriggerVolume(Volume): ...


class StaticMeshComponent(MeshComponent):
    ForcedLodModel: int
    PreviousLODLevel: int
    MinLOD: int
    SubDivisionStepSize: int
    StaticMesh: StaticMesh
    CustomMaskMaterial: MaterialInterface
    CustomGlowMaterial: MaterialInterface
    WireframeColorOverride: core_uobject.Color
    bOverrideWireframeColor: bool
    bOverrideMinLod: bool
    bOverrideNavigationExport: bool
    bForceNavigationObstacle: bool
    bDisallowMeshPaintPerInstance: bool
    bIgnoreInstanceForTextureStreaming: bool
    bOverrideLightMapRes: bool
    bCastDistanceFieldIndirectShadow: bool
    bOverrideDistanceFieldSelfShadowBias: bool
    bUseSubDivisions: bool
    bUseDefaultCollision: bool
    bReverseCulling: bool
    OverriddenLightMapRes: int
    DistanceFieldIndirectShadowMinVisibility: float
    DistanceFieldSelfShadowBias: float
    StreamingDistanceMultiplier: float
    LODData: unreal.WrappedArray[StaticMeshComponentLODInfo]
    BaseLODMapBuildDataGUID: core_uobject.Guid
    StreamingTextureData: unreal.WrappedArray[StreamingTextureBuildInfo]
    LightmassSettings: LightmassPrimitiveSettings
    AutoLightMapResFactor: float
    def SetStaticMesh(self, NewMesh: StaticMesh, ReturnValue: bool) -> bool: ...
    def SetReverseCulling(self, ReverseCulling: bool): ...
    def SetForcedLodModel(self, NewForcedLodModel: int): ...
    def SetDistanceFieldSelfShadowBias(self, NewValue: float): ...
    def OnRep_StaticMesh(self, OldStaticMesh: StaticMesh): ...
    def GetLocalBounds(self, Min: core_uobject.Vector, Max: core_uobject.Vector): ...


class GameModeBase(Info):
    OptionsString: str
    GameSessionClass: unreal.UClass
    GameStateClass: unreal.UClass
    PlayerControllerClass: unreal.UClass
    PlayerStateClass: unreal.UClass
    HUDClass: unreal.UClass
    DefaultPawnClass: unreal.UClass
    SpectatorClass: unreal.UClass
    ReplaySpectatorPlayerControllerClass: unreal.UClass
    ServerStatReplicatorClass: unreal.UClass
    GameSession: GameSession
    GameState: GameStateBase
    ServerStatReplicator: ServerStatReplicator
    DefaultPlayerName: str
    bUseSeamlessTravel: bool
    bStartPlayersAsSpectators: bool
    bPauseable: bool
    bSpectatorDuringTravel: bool
    def StartPlay(self): ...
    def SpawnDefaultPawnFor(self, NewPlayer: Controller, StartSpot: Actor, ReturnValue: Pawn) -> Pawn: ...
    def SpawnDefaultPawnAtTransform(self, NewPlayer: Controller, SpawnTransform: core_uobject.Transform, ReturnValue: Pawn) -> Pawn: ...
    def ShouldReset(self, ActorToReset: Actor, ReturnValue: bool) -> bool: ...
    def ReturnToMainMenuHost(self): ...
    def RestartPlayerAtTransform(self, NewPlayer: Controller, SpawnTransform: core_uobject.Transform): ...
    def RestartPlayerAtPlayerStart(self, NewPlayer: Controller, StartSpot: Actor): ...
    def RestartPlayer(self, NewPlayer: Controller): ...
    def ResetLevel(self): ...
    def PlayerCanRestart(self, Player: PlayerController, ReturnValue: bool) -> bool: ...
    def MustSpectate(self, NewPlayerController: PlayerController, ReturnValue: bool) -> bool: ...
    def K2_PostLogin(self, NewPlayer: PlayerController): ...
    def K2_OnSwapPlayerControllers(self, OldPC: PlayerController, NewPC: PlayerController): ...
    def K2_OnRestartPlayer(self, NewPlayer: Controller): ...
    def K2_OnLogout(self, ExitingController: Controller): ...
    def K2_OnChangeName(self, Other: Controller, NewName: str, bNameChange: bool): ...
    def K2_FindPlayerStart(self, Player: Controller, IncomingName: str, ReturnValue: Actor) -> Actor: ...
    def InitStartSpot(self, StartSpot: Actor, NewPlayer: Controller): ...
    def InitializeHUDForPlayer(self, NewPlayer: PlayerController): ...
    def HasMatchStarted(self, ReturnValue: bool) -> bool: ...
    def HandleStartingNewPlayer(self, NewPlayer: PlayerController): ...
    def GetNumSpectators(self, ReturnValue: int) -> int: ...
    def GetNumPlayers(self, ReturnValue: int) -> int: ...
    def GetDefaultPawnClassForController(self, InController: Controller, ReturnValue: unreal.UClass) -> unreal.UClass: ...
    def FindPlayerStart(self, Player: Controller, IncomingName: str, ReturnValue: Actor) -> Actor: ...
    def ChoosePlayerStart(self, Player: Controller, ReturnValue: Actor) -> Actor: ...
    def ChangeName(self, Controller: Controller, NewName: str, bNameChange: bool): ...
    def CanSpectate(self, Viewer: PlayerController, ViewTarget: PlayerState, ReturnValue: bool) -> bool: ...


class GameMode(GameModeBase):
    MatchState: str
    bDelayedStart: bool
    NumSpectators: int
    NumPlayers: int
    NumBots: int
    MinRespawnDelay: float
    NumTravellingPlayers: int
    EngineMessageClass: unreal.UClass
    InactivePlayerArray: unreal.WrappedArray[PlayerState]
    InactivePlayerStateLifeSpan: float
    MaxInactivePlayers: int
    bHandleDedicatedServerReplays: bool
    def StartMatch(self): ...
    def SetBandwidthLimit(self, AsyncIOBandwidthLimit: float): ...
    def Say(self, Msg: str): ...
    def RestartGame(self): ...
    def ReadyToStartMatch(self, ReturnValue: bool) -> bool: ...
    def ReadyToEndMatch(self, ReturnValue: bool) -> bool: ...
    def K2_OnSetMatchState(self, NewState: str): ...
    def IsMatchInProgress(self, ReturnValue: bool) -> bool: ...
    def HasMatchEnded(self, ReturnValue: bool) -> bool: ...
    def GetMatchState(self, ReturnValue: str) -> str: ...
    def EndMatch(self): ...
    def AbortMatch(self): ...


class GameStateBase(Info):
    GameModeClass: unreal.UClass
    AuthorityGameMode: GameModeBase
    SpectatorClass: unreal.UClass
    PlayerArray: unreal.WrappedArray[PlayerState]
    bReplicatedHasBegunPlay: bool
    ReplicatedWorldTimeSeconds: float
    ServerWorldTimeSecondsDelta: float
    ServerWorldTimeSecondsUpdateFrequency: float
    def OnRep_SpectatorClass(self): ...
    def OnRep_ReplicatedWorldTimeSeconds(self): ...
    def OnRep_ReplicatedHasBegunPlay(self): ...
    def OnRep_GameModeClass(self): ...
    def HasMatchStarted(self, ReturnValue: bool) -> bool: ...
    def HasBegunPlay(self, ReturnValue: bool) -> bool: ...
    def GetServerWorldTimeSeconds(self, ReturnValue: float) -> float: ...
    def GetPlayerStartTime(self, Controller: Controller, ReturnValue: float) -> float: ...
    def GetPlayerRespawnDelay(self, Controller: Controller, ReturnValue: float) -> float: ...


class GameState(GameStateBase):
    MatchState: str
    PreviousMatchState: str
    ElapsedTime: int
    def OnRep_MatchState(self): ...
    def OnRep_ElapsedTime(self): ...


class SphereComponent(ShapeComponent):
    SphereRadius: float
    bForceZeroExtent: bool
    def SetSphereRadius(self, InSphereRadius: float, bUpdateOverlaps: bool): ...
    def GetUnscaledSphereRadius(self, ReturnValue: float) -> float: ...
    def GetShapeScale(self, ReturnValue: float) -> float: ...
    def GetScaledSphereRadius(self, ReturnValue: float) -> float: ...


class ProjectileMovementComponent(MovementComponent):
    InitialSpeed: float
    MaxSpeed: float
    bRotationFollowsVelocity: bool
    bShouldBounce: bool
    bInitialVelocityInLocalSpace: bool
    bForceSubStepping: bool
    bIsHomingProjectile: bool
    bBounceAngleAffectsFriction: bool
    bIsSliding: bool
    PreviousHitTime: float
    PreviousHitNormal: core_uobject.Vector
    ProjectileGravityScale: float
    Buoyancy: float
    Bounciness: float
    Friction: float
    BounceVelocityStopSimulatingThreshold: float
    HomingAccelerationMagnitude: float
    HomingTargetComponent: SceneComponent
    MaxSimulationTimeStep: float
    MaxSimulationIterations: int
    BounceAdditionalIterations: int
    BaseRotationOffset: core_uobject.Rotator
    def StopSimulating(self, HitResult: HitResult): ...
    def SetVelocityInLocalSpace(self, NewVelocity: core_uobject.Vector): ...
    def OnProjectileStopDelegate__DelegateSignature(self, ImpactResult: HitResult): ...
    def OnProjectileBounceDelegate__DelegateSignature(self, ImpactResult: HitResult, ImpactVelocity: core_uobject.Vector): ...
    def LimitVelocity(self, NewVelocity: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...


class PrimaryAssetLabel(PrimaryDataAsset):
    Rules: PrimaryAssetRules
    bLabelAssetsInMyDirectory: bool
    bIsRuntimeLabel: bool
    AssetCollection: CollectionReference



class PlayerCameraManager(Actor):
    PCOwner: PlayerController
    TransformComponent: SceneComponent
    DefaultFOV: float
    DefaultOrthoWidth: float
    DefaultAspectRatio: float
    CameraCache: CameraCacheEntry
    LastFrameCameraCache: CameraCacheEntry
    ViewTarget: TViewTarget
    PendingViewTarget: TViewTarget
    CameraCachePrivate: CameraCacheEntry
    LastFrameCameraCachePrivate: CameraCacheEntry
    ModifierList: unreal.WrappedArray[CameraModifier]
    DefaultModifiers: unreal.WrappedArray[unreal.UClass]
    FreeCamDistance: float
    FreeCamOffset: core_uobject.Vector
    ViewTargetOffset: core_uobject.Vector
    CameraLensEffects: unreal.WrappedArray[EmitterCameraLensEffectBase]
    CachedCameraShakeMod: CameraModifier_CameraShake
    AnimInstPool: CameraAnimInst
    PostProcessBlendCache: unreal.WrappedArray[PostProcessSettings]
    ActiveAnims: unreal.WrappedArray[CameraAnimInst]
    FreeAnims: unreal.WrappedArray[CameraAnimInst]
    AnimCameraActor: CameraActor
    bIsOrthographic: bool
    bDefaultConstrainAspectRatio: bool
    bClientSimulatingViewTarget: bool
    bUseClientSideCameraUpdates: bool
    bGameCameraCutThisFrame: bool
    ViewPitchMin: float
    ViewPitchMax: float
    ViewYawMin: float
    ViewYawMax: float
    ViewRollMin: float
    ViewRollMax: float
    DefaultForegroundFOV: float
    def StopCameraShake(self, ShakeInstance: CameraShake, bImmediately: bool): ...
    def StopCameraFade(self): ...
    def StopCameraAnimInst(self, AnimInst: CameraAnimInst, bImmediate: bool): ...
    def StopAllInstancesOfCameraShake(self, Shake: unreal.UClass, bImmediately: bool): ...
    def StopAllInstancesOfCameraAnim(self, Anim: CameraAnim, bImmediate: bool): ...
    def StopAllCameraShakes(self, bImmediately: bool): ...
    def StopAllCameraAnims(self, bImmediate: bool): ...
    def StartCameraFade(self, FromAlpha: float, ToAlpha: float, Duration: float, Color: core_uobject.LinearColor, bShouldFadeAudio: bool, bHoldWhenFinished: bool): ...
    def SetManualCameraFade(self, InFadeAmount: float, Color: core_uobject.LinearColor, bInFadeAudio: bool): ...
    def RemoveCameraModifier(self, ModifierToRemove: CameraModifier, ReturnValue: bool) -> bool: ...
    def RemoveCameraLensEffect(self, Emitter: EmitterCameraLensEffectBase): ...
    def PlayCameraShakeData(self, ShakeClass: unreal.UClass, OutCameraShake: CameraShakeData, Scale: float, PlaySpace: int, UserPlaySpaceRot: core_uobject.Rotator, bLoopingShake: bool): ...
    def PlayCameraShake(self, ShakeClass: unreal.UClass, Scale: float, PlaySpace: int, UserPlaySpaceRot: core_uobject.Rotator, ReturnValue: CameraShake) -> CameraShake: ...
    def PlayCameraAnim(self, Anim: CameraAnim, Rate: float, Scale: float, BlendInTime: float, BlendOutTime: float, bLoop: bool, bRandomStartTime: bool, Duration: float, PlaySpace: int, UserPlaySpaceRot: core_uobject.Rotator, ReturnValue: CameraAnimInst) -> CameraAnimInst: ...
    def PhotographyCameraModify(self, NewCameraLocation: core_uobject.Vector, PreviousCameraLocation: core_uobject.Vector, OriginalCameraLocation: core_uobject.Vector, ResultCameraLocation: core_uobject.Vector): ...
    def OnPhotographySessionStart(self): ...
    def OnPhotographySessionEnd(self): ...
    def OnPhotographyMultiPartCaptureStart(self): ...
    def OnPhotographyMultiPartCaptureEnd(self): ...
    def GetOwningPlayerController(self, ReturnValue: PlayerController) -> PlayerController: ...
    def GetFOVAngle(self, ReturnValue: float) -> float: ...
    def GetForegroundFOVAngle(self, ReturnValue: float) -> float: ...
    def GetCameraRotation(self, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def GetCameraLocation(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def FindCameraModifierByClass(self, ModifierClass: unreal.UClass, ReturnValue: CameraModifier) -> CameraModifier: ...
    def ClearCameraLensEffects(self): ...
    def BlueprintUpdateCamera(self, CameraTarget: Actor, NewCameraLocation: core_uobject.Vector, NewCameraRotation: core_uobject.Rotator, NewCameraFOV: float, ReturnValue: bool) -> bool: ...
    def AddNewCameraModifier(self, ModifierClass: unreal.UClass, ReturnValue: CameraModifier) -> CameraModifier: ...
    def AddCameraLensEffect(self, LensEffectEmitterClass: unreal.UClass, ReturnValue: EmitterCameraLensEffectBase) -> EmitterCameraLensEffectBase: ...


class AssetManager(unreal.UObject):
    ObjectReferenceList: unreal.WrappedArray[unreal.UObject]
    bIsGlobalAsyncScanEnvironment: bool
    bShouldGuessTypeAndName: bool
    bShouldUseSynchronousLoad: bool
    bIsLoadingFromPakFiles: bool
    bShouldAcquireMissingChunksOnLoad: bool
    bOnlyCookProductionAssets: bool
    bIsBulkScanning: bool
    bIsManagementDatabaseCurrent: bool
    bUpdateManagementDatabaseAfterScan: bool
    bIncludeOnlyOnDiskAssets: bool
    NumberOfSpawnedNotifications: int



class PlayerState(Info):
    Score: float
    Ping: int
    PlayerName: str
    PlayerId: int
    bIsSpectator: bool
    bOnlySpectator: bool
    bIsABot: bool
    bIsInactive: bool
    bFromPreviousLevel: bool
    StartTime: int
    EngineMessageClass: unreal.UClass
    SavedNetworkAddress: str
    UniqueId: UniqueNetIdRepl
    PlayerNamePrivate: str
    bShouldUpdateReplicatedPing: bool
    ParentPlayerId: int
    HardwareIdentifier: int
    def ReceiveOverrideWith(self, OldPlayerState: PlayerState): ...
    def ReceiveCopyProperties(self, NewPlayerState: PlayerState): ...
    def OnRep_UniqueId(self): ...
    def OnRep_Score(self): ...
    def OnRep_PlayerName(self): ...
    def OnRep_PlayerId(self): ...
    def OnRep_ParentPlayerId(self): ...
    def OnRep_bIsInactive(self): ...
    def GetPlayerName(self, ReturnValue: str) -> str: ...


class CapsuleComponent(ShapeComponent):
    CapsuleHalfHeight: float
    CapsuleRadius: float
    CapsuleHeight: float
    def SetCapsuleSize(self, InRadius: float, InHalfHeight: float, bUpdateOverlaps: bool): ...
    def SetCapsuleRadius(self, Radius: float, bUpdateOverlaps: bool): ...
    def SetCapsuleHalfHeight(self, HalfHeight: float, bUpdateOverlaps: bool): ...
    def GetUnscaledCapsuleSize_WithoutHemisphere(self, OutRadius: float, OutHalfHeightWithoutHemisphere: float): ...
    def GetUnscaledCapsuleSize(self, OutRadius: float, OutHalfHeight: float): ...
    def GetUnscaledCapsuleRadius(self, ReturnValue: float) -> float: ...
    def GetUnscaledCapsuleHalfHeight_WithoutHemisphere(self, ReturnValue: float) -> float: ...
    def GetUnscaledCapsuleHalfHeight(self, ReturnValue: float) -> float: ...
    def GetShapeScale(self, ReturnValue: float) -> float: ...
    def GetScaledCapsuleSize_WithoutHemisphere(self, OutRadius: float, OutHalfHeightWithoutHemisphere: float): ...
    def GetScaledCapsuleSize(self, OutRadius: float, OutHalfHeight: float): ...
    def GetScaledCapsuleRadius(self, ReturnValue: float) -> float: ...
    def GetScaledCapsuleHalfHeight_WithoutHemisphere(self, ReturnValue: float) -> float: ...
    def GetScaledCapsuleHalfHeight(self, ReturnValue: float) -> float: ...


class CharacterMovementComponent(PawnMovementComponent):
    CharacterOwner: Character
    bApplyGravityWhileJumping: bool
    bCanBeLaunched: bool
    GravityScale: float
    MaxStepHeight: float
    JumpZVelocity: float
    JumpOffJumpZFactor: float
    WalkableFloorAngle: float
    WalkableFloorZ: float
    MovementMode: int
    CustomMovementMode: int
    GroundFriction: float
    MaxWalkSpeed: GbxAttributeFloat
    MaxWalkSpeedCrouched: GbxAttributeFloat
    MaxSwimSpeed: GbxAttributeFloat
    MaxFlySpeed: GbxAttributeFloat
    MaxCustomMovementSpeed: GbxAttributeFloat
    MaxAcceleration: float
    MinAnalogWalkSpeed: float
    BrakingFrictionFactor: float
    BrakingFriction: float
    bUseSeparateBrakingFriction: bool
    BrakingDecelerationWalking: float
    BrakingDecelerationFalling: float
    BrakingDecelerationSwimming: float
    BrakingDecelerationFlying: float
    AirControl: float
    AirControlBoostMultiplier: float
    AirControlBoostVelocityThreshold: float
    FallingLateralFriction: float
    CrouchedHalfHeight: float
    Buoyancy: float
    PerchRadiusThreshold: float
    PerchAdditionalHeight: float
    RotationRate: core_uobject.Rotator
    bUseControllerDesiredRotation: bool
    bOrientRotationToMovement: bool
    bSweepWhileNavWalking: bool
    bMovementInProgress: bool
    bEnableScopedMovementUpdates: bool
    bForceMaxAccel: bool
    bRunPhysicsWithNoController: bool
    bForceNextFloorCheck: bool
    bShrinkProxyCapsule: bool
    bCanWalkOffLedges: bool
    bCanWalkOffLedgesWhenCrouching: bool
    bNetworkSkipProxyPredictionOnNetUpdate: bool
    bNetworkAlwaysReplicateTransformUpdateTimestamp: bool
    bDeferUpdateMoveComponent: bool
    DeferredUpdatedMoveComponent: SceneComponent
    MaxOutOfWaterStepHeight: float
    OutofWaterZ: float
    Mass: float
    bEnablePhysicsInteraction: bool
    bTouchForceScaledToMass: bool
    bPushForceScaledToMass: bool
    bPushForceUsingZOffset: bool
    bScalePushForceToVelocity: bool
    StandingDownwardForceScale: float
    InitialPushForceFactor: float
    PushForceFactor: float
    PushForcePointZOffsetFactor: float
    TouchForceFactor: float
    MinTouchForce: float
    MaxTouchForce: float
    RepulsionForce: float
    bForceBraking: bool
    CrouchedSpeedMultiplier: float
    UpperImpactNormalScale: float
    Acceleration: core_uobject.Vector
    LastUpdateLocation: core_uobject.Vector
    LastUpdateRotation: core_uobject.Quat
    LastUpdateVelocity: core_uobject.Vector
    ServerLastTransformUpdateTimeStamp: float
    ServerLastClientGoodMoveAckTime: float
    ServerLastClientAdjustmentTime: float
    PendingImpulseToApply: core_uobject.Vector
    PendingForceToApply: core_uobject.Vector
    AnalogInputModifier: float
    MaxSimulationTimeStep: float
    MaxSimulationIterations: int
    MaxDepenetrationWithGeometry: float
    MaxDepenetrationWithGeometryAsProxy: float
    MaxDepenetrationWithPawn: float
    MaxDepenetrationWithPawnAsProxy: float
    NetworkSimulatedSmoothLocationTime: float
    NetworkSimulatedSmoothRotationTime: float
    ListenServerNetworkSimulatedSmoothLocationTime: float
    ListenServerNetworkSimulatedSmoothRotationTime: float
    NetProxyShrinkRadius: float
    NetProxyShrinkHalfHeight: float
    NetworkMaxSmoothUpdateDistance: float
    NetworkNoSmoothUpdateDistance: float
    NetworkSmoothingMode: ENetworkSmoothingMode
    NetworkMinTimeBetweenClientAckGoodMoves: float
    NetworkMinTimeBetweenClientAdjustments: float
    NetworkMinTimeBetweenClientAdjustmentsLargeCorrection: float
    NetworkLargeClientCorrectionDistance: float
    LedgeCheckThreshold: float
    JumpOutOfWaterPitch: float
    CurrentFloor: FindFloorResult
    DefaultLandMovementMode: int
    DefaultWaterMovementMode: int
    GroundMovementMode: int
    bMaintainHorizontalGroundVelocity: bool
    bImpartBaseVelocityX: bool
    bImpartBaseVelocityY: bool
    bImpartBaseVelocityZ: bool
    bImpartBaseAngularVelocity: bool
    bJustTeleported: bool
    bNetworkUpdateReceived: bool
    bNetworkMovementModeChanged: bool
    bIgnoreClientMovementErrorChecksAndCorrection: bool
    bNotifyApex: bool
    bCheatFlying: bool
    bWantsToCrouch: bool
    bCrouchMaintainsBaseLocation: bool
    bIgnoreBaseRotation: bool
    bFastAttachedMove: bool
    bAlwaysCheckFloor: bool
    bUseFlatBaseForFloorChecks: bool
    bPerformingJumpOff: bool
    bWantsToLeaveNavWalking: bool
    bUseRVOAvoidance: bool
    bRequestedMoveUseAcceleration: bool
    bHasRequestedVelocity: bool
    bRequestedMoveWithMaxSpeed: bool
    bWasAvoidanceUpdated: bool
    bProjectNavMeshWalking: bool
    bProjectNavMeshOnBothWorldChannels: bool
    AvoidanceConsiderationRadius: float
    RequestedVelocity: core_uobject.Vector
    AvoidanceUID: int
    AvoidanceGroup: NavAvoidanceMask
    GroupsToAvoid: NavAvoidanceMask
    GroupsToIgnore: NavAvoidanceMask
    AvoidanceWeight: float
    PendingLaunchVelocity: core_uobject.Vector
    NavMeshProjectionInterval: float
    NavMeshProjectionTimer: float
    NavMeshProjectionInterpSpeed: float
    NavMeshProjectionHeightScaleUp: float
    NavMeshProjectionHeightScaleDown: float
    NavWalkingFloorDistTolerance: float
    PostPhysicsTickFunction: CharacterMovementComponentPostPhysicsTickFunction
    MinTimeBetweenTimeStampResets: float
    CurrentRootMotion: RootMotionSourceGroup
    RootMotionParams: RootMotionMovementParams
    AnimRootMotionVelocity: core_uobject.Vector
    bWasSimulatingRootMotion: bool
    bAllowPhysicsRotationDuringAnimRootMotion: bool
    bDelayRootMotionOneFrame: bool
    LastClientUpdateTime: float
    WalkableLedgeAngle: float
    WalkableLedgeZ: float
    bAdjustVelocityRelativeToBaseWhenLanding: bool
    def SetWalkableFloorZ(self, InWalkableFloorZ: float): ...
    def SetWalkableFloorAngle(self, InWalkableFloorAngle: float): ...
    def SetNavWalkingPhysics(self, bEnable: bool): ...
    def SetMovementMode(self, NewMovementMode: int, NewCustomMode: int): ...
    def SetGroupsToIgnoreMask(self, GroupMask: NavAvoidanceMask): ...
    def SetGroupsToIgnore(self, GroupFlags: int): ...
    def SetGroupsToAvoidMask(self, GroupMask: NavAvoidanceMask): ...
    def SetGroupsToAvoid(self, GroupFlags: int): ...
    def SetAvoidanceGroupMask(self, GroupMask: NavAvoidanceMask): ...
    def SetAvoidanceGroup(self, GroupFlags: int): ...
    def SetAvoidanceEnabled(self, bEnable: bool): ...
    def K2_GetWalkableFloorZ(self, ReturnValue: float) -> float: ...
    def K2_GetWalkableFloorAngle(self, ReturnValue: float) -> float: ...
    def K2_GetModifiedMaxAcceleration(self, ReturnValue: float) -> float: ...
    def K2_FindFloor(self, CapsuleLocation: core_uobject.Vector, FloorResult: FindFloorResult): ...
    def K2_ComputeFloorDist(self, CapsuleLocation: core_uobject.Vector, LineDistance: float, SweepDistance: float, SweepRadius: float, FloorResult: FindFloorResult): ...
    def IsWalking(self, ReturnValue: bool) -> bool: ...
    def IsWalkable(self, Hit: HitResult, ReturnValue: bool) -> bool: ...
    def GetValidPerchRadius(self, ReturnValue: float) -> float: ...
    def GetPerchRadiusThreshold(self, ReturnValue: float) -> float: ...
    def GetMovementBase(self, ReturnValue: PrimitiveComponent) -> PrimitiveComponent: ...
    def GetMinAnalogSpeed(self, ReturnValue: float) -> float: ...
    def GetMaxJumpHeightWithJumpTime(self, ReturnValue: float) -> float: ...
    def GetMaxJumpHeight(self, ReturnValue: float) -> float: ...
    def GetMaxBrakingDeceleration(self, ReturnValue: float) -> float: ...
    def GetMaxAcceleration(self, ReturnValue: float) -> float: ...
    def GetImpartedMovementBaseVelocity(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetCurrentAcceleration(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetCharacterOwner(self, ReturnValue: Character) -> Character: ...
    def GetAnalogInputModifier(self, ReturnValue: float) -> float: ...
    def DisableMovement(self): ...
    def ClearAccumulatedForces(self): ...
    def CapsuleTouched(self, OverlappedComp: PrimitiveComponent, Other: Actor, OtherComp: PrimitiveComponent, OtherBodyIndex: int, bFromSweep: bool, SweepResult: HitResult): ...
    def CalcVelocity(self, DeltaTime: float, Friction: float, bFluid: bool, BrakingDeceleration: float): ...
    def AddImpulse(self, Impulse: core_uobject.Vector, bVelocityChange: bool): ...
    def AddForce(self, Force: core_uobject.Vector): ...


class CheatManager(unreal.UObject):
    DebugCameraControllerRef: DebugCameraController
    DebugCameraControllerClass: unreal.UClass
    def Walk(self): ...
    def ViewSelf(self): ...
    def ViewPlayer(self, S: str): ...
    def ViewClass(self, DesiredClass: unreal.UClass): ...
    def ViewActor(self, ActorName: str): ...
    def UpdateSafeArea(self): ...
    def ToggleServerStatReplicatorUpdateStatNet(self): ...
    def ToggleServerStatReplicatorClientOverwrite(self): ...
    def ToggleDebugCamera(self): ...
    def ToggleAILogging(self): ...
    def TestCollisionDistance(self): ...
    def Teleport(self): ...
    def Summon(self, ClassName: str): ...
    def StreamLevelOut(self, PackageName: str): ...
    def StreamLevelIn(self, PackageName: str): ...
    def SpawnServerStatReplicator(self): ...
    def Slomo(self, NewTimeDilation: float): ...
    def SetWorldOrigin(self): ...
    def SetMouseSensitivityToDefault(self): ...
    def ServerToggleAILogging(self): ...
    def ReceiveInitCheatManager(self): ...
    def ReceiveEndPlay(self): ...
    def PlayersOnly(self): ...
    def OnlyLoadLevel(self, PackageName: str): ...
    def LogLoc(self): ...
    def InvertMouse(self): ...
    def FreezeFrame(self, Delay: float): ...
    def Fly(self): ...
    def FlushLog(self): ...
    def EnableDebugCamera(self): ...
    def DumpVoiceMutingState(self): ...
    def DumpPartyState(self): ...
    def DumpOnlineSessionState(self): ...
    def DumpChatState(self): ...
    def DisableDebugCamera(self): ...
    def DestroyTarget(self): ...
    def DestroyServerStatReplicator(self): ...
    def DestroyPawns(self, aClass: unreal.UClass): ...
    def DestroyAllPawnsExceptTarget(self): ...
    def DestroyAll(self, aClass: unreal.UClass): ...
    def DebugCapsuleSweepSize(self, HalfHeight: float, Radius: float): ...
    def DebugCapsuleSweepPawn(self): ...
    def DebugCapsuleSweepComplex(self, bTraceComplex: bool): ...
    def DebugCapsuleSweepClear(self): ...
    def DebugCapsuleSweepChannel(self, Channel: int): ...
    def DebugCapsuleSweepCapture(self): ...
    def DebugCapsuleSweep(self): ...
    def DamageTarget(self, DamageAmount: float): ...
    def CheatScript(self, ScriptName: str): ...
    def ChangeSize(self, F: float): ...
    def BugItStringCreator(self, ViewLocation: core_uobject.Vector, ViewRotation: core_uobject.Rotator, GoString: str, LocString: str): ...
    def BugIt(self, ScreenShotDescription: str): ...


class DamageType(unreal.UObject):
    bCausedByWorld: bool
    bScaleMomentumByMass: bool
    bRadialDamageVelChange: bool
    DamageImpulse: float
    DestructibleImpulse: float
    DestructibleDamageSpreadScale: float
    DamageFalloff: float



class Engine(unreal.UObject):
    TinyFont: Font
    TinyFontName: core_uobject.SoftObjectPath
    SmallFont: Font
    SmallFontName: core_uobject.SoftObjectPath
    MediumFont: Font
    MediumFontName: core_uobject.SoftObjectPath
    LargeFont: Font
    LargeFontName: core_uobject.SoftObjectPath
    SubtitleFont: Font
    SubtitleFontName: core_uobject.SoftObjectPath
    MonospaceFont: Font
    MonospaceFontName: core_uobject.SoftObjectPath
    AdditionalFonts: unreal.WrappedArray[Font]
    AdditionalFontNames: unreal.WrappedArray[str]
    ConsoleClass: unreal.UClass
    ConsoleClassName: core_uobject.SoftClassPath
    GameViewportClientClass: unreal.UClass
    GameViewportClientClassName: core_uobject.SoftClassPath
    LocalPlayerClass: unreal.UClass
    LocalPlayerClassName: core_uobject.SoftClassPath
    WorldSettingsClass: unreal.UClass
    WorldSettingsClassName: core_uobject.SoftClassPath
    NavigationSystemClassName: core_uobject.SoftClassPath
    NavigationSystemClass: unreal.UClass
    NavigationSystemConfigClassName: core_uobject.SoftClassPath
    AvoidanceManagerClassName: core_uobject.SoftClassPath
    AvoidanceManagerClass: unreal.UClass
    PhysicsCollisionHandlerClass: unreal.UClass
    PhysicsCollisionHandlerClassName: core_uobject.SoftClassPath
    GameUserSettingsClassName: core_uobject.SoftClassPath
    GameUserSettingsClass: unreal.UClass
    AIControllerClassName: core_uobject.SoftClassPath
    GameUserSettings: GameUserSettings
    LevelScriptActorClass: unreal.UClass
    LevelScriptActorClassName: core_uobject.SoftClassPath
    DefaultBlueprintBaseClassName: core_uobject.SoftClassPath
    GameSingletonClassName: core_uobject.SoftClassPath
    GameSingleton: unreal.UObject
    AssetManagerClassName: core_uobject.SoftClassPath
    AssetManager: AssetManager
    DefaultTexture: Texture2D
    DefaultTextureName: core_uobject.SoftObjectPath
    DefaultBrightnessTexture: Texture2D
    DefaultBrightnessTextureName: core_uobject.SoftObjectPath
    DefaultDiffuseTexture: Texture
    DefaultDiffuseTextureName: core_uobject.SoftObjectPath
    DefaultBSPVertexTexture: Texture2D
    DefaultBSPVertexTextureName: core_uobject.SoftObjectPath
    HighFrequencyNoiseTexture: Texture2D
    HighFrequencyNoiseTextureName: core_uobject.SoftObjectPath
    DefaultBokehTexture: Texture2D
    DefaultBokehTextureName: core_uobject.SoftObjectPath
    DefaultBloomKernelTexture: Texture2D
    DefaultBloomKernelTextureName: core_uobject.SoftObjectPath
    WireframeMaterial: Material
    WireframeMaterialName: str
    DebugMeshMaterial: Material
    DebugMeshMaterialName: core_uobject.SoftObjectPath
    LevelColorationLitMaterial: Material
    LevelColorationLitMaterialName: str
    LevelColorationUnlitMaterial: Material
    LevelColorationUnlitMaterialName: str
    LevelColorationUnlitMaterialWithVertexShift: Material
    LevelColorationUnlitMaterialWithVertexShiftName: str
    BlockingVolumeColorationMaterial: Material
    BlockingVolumeColorationMaterialName: str
    LightingTexelDensityMaterial: Material
    LightingTexelDensityName: str
    ShadedLevelColorationLitMaterial: Material
    ShadedLevelColorationLitMaterialName: str
    ShadedLevelColorationUnlitMaterial: Material
    ShadedLevelColorationUnlitMaterialName: str
    RemoveSurfaceMaterial: Material
    RemoveSurfaceMaterialName: core_uobject.SoftObjectPath
    VertexColorMaterial: Material
    VertexColorMaterialName: str
    VertexColorViewModeMaterial_ColorOnly: Material
    VertexColorViewModeMaterialName_ColorOnly: str
    VertexColorViewModeMaterial_AlphaAsColor: Material
    VertexColorViewModeMaterialName_AlphaAsColor: str
    VertexColorViewModeMaterial_RedOnly: Material
    VertexColorViewModeMaterialName_RedOnly: str
    VertexColorViewModeMaterial_GreenOnly: Material
    VertexColorViewModeMaterialName_GreenOnly: str
    VertexColorViewModeMaterial_BlueOnly: Material
    VertexColorViewModeMaterialName_BlueOnly: str
    DebugEditorMaterialName: core_uobject.SoftObjectPath
    ConstraintLimitMaterial: Material
    ConstraintLimitMaterialX: MaterialInstanceDynamic
    ConstraintLimitMaterialXAxis: MaterialInstanceDynamic
    ConstraintLimitMaterialY: MaterialInstanceDynamic
    ConstraintLimitMaterialYAxis: MaterialInstanceDynamic
    ConstraintLimitMaterialZ: MaterialInstanceDynamic
    ConstraintLimitMaterialZAxis: MaterialInstanceDynamic
    ConstraintLimitMaterialPrismatic: MaterialInstanceDynamic
    InvalidLightmapSettingsMaterial: Material
    InvalidLightmapSettingsMaterialName: core_uobject.SoftObjectPath
    PreviewShadowsIndicatorMaterial: Material
    PreviewShadowsIndicatorMaterialName: core_uobject.SoftObjectPath
    ArrowMaterial: Material
    ArrowMaterialName: core_uobject.SoftObjectPath
    LightingOnlyBrightness: core_uobject.LinearColor
    ShaderComplexityColors: unreal.WrappedArray[core_uobject.LinearColor]
    QuadComplexityColors: unreal.WrappedArray[core_uobject.LinearColor]
    LightComplexityColors: unreal.WrappedArray[core_uobject.LinearColor]
    StationaryLightOverlapColors: unreal.WrappedArray[core_uobject.LinearColor]
    LODColorationColors: unreal.WrappedArray[core_uobject.LinearColor]
    HLODColorationColors: unreal.WrappedArray[core_uobject.LinearColor]
    StreamingAccuracyColors: unreal.WrappedArray[core_uobject.LinearColor]
    MaxPixelShaderAdditiveComplexityCount: float
    MaxES2PixelShaderAdditiveComplexityCount: float
    MaxES3PixelShaderAdditiveComplexityCount: float
    MinLightMapDensity: float
    IdealLightMapDensity: float
    MaxLightMapDensity: float
    bRenderLightMapDensityGrayscale: bool
    RenderLightMapDensityGrayscaleScale: float
    RenderLightMapDensityColorScale: float
    LightMapDensityVertexMappedColor: core_uobject.LinearColor
    LightMapDensitySelectedColor: core_uobject.LinearColor
    StatColorMappings: unreal.WrappedArray[StatColorMapping]
    DefaultPhysMaterial: PhysicalMaterial
    DefaultPhysMaterialName: core_uobject.SoftObjectPath
    ActiveGameNameRedirects: unreal.WrappedArray[GameNameRedirect]
    ActiveClassRedirects: unreal.WrappedArray[ClassRedirect]
    ActivePluginRedirects: unreal.WrappedArray[PluginRedirect]
    ActiveStructRedirects: unreal.WrappedArray[StructRedirect]
    PreIntegratedSkinBRDFTexture: Texture2D
    PreIntegratedSkinBRDFTextureName: core_uobject.SoftObjectPath
    MiniFontTexture: Texture2D
    MiniFontTextureName: core_uobject.SoftObjectPath
    WeightMapPlaceholderTexture: Texture
    WeightMapPlaceholderTextureName: core_uobject.SoftObjectPath
    LightMapDensityTexture: Texture2D
    LightMapDensityTextureName: core_uobject.SoftObjectPath
    GameViewport: GameViewportClient
    DeferredCommands: unreal.WrappedArray[str]
    TickCycles: int
    GameCycles: int
    ClientCycles: int
    NearClipPlane: float
    bHardwareSurveyEnabled: bool
    bSubtitlesEnabled: bool
    bSubtitlesForcedOff: bool
    MaximumLoopIterationCount: int
    bCanBlueprintsTickByDefault: bool
    bOptimizeAnimBlueprintMemberVariableAccess: bool
    bAllowMultiThreadedAnimationUpdate: bool
    bEnableEditorPSysRealtimeLOD: bool
    bSmoothFrameRate: bool
    bUseFixedFrameRate: bool
    FixedFrameRate: float
    SmoothedFrameRateRange: core_uobject.FloatRange
    CustomTimeStep: EngineCustomTimeStep
    CustomTimeStepClassName: core_uobject.SoftClassPath
    TimecodeProvider: TimecodeProvider
    TimecodeFrameRateClassName: core_uobject.SoftClassPath
    DefaultTimecodeFrameRate: core_uobject.FrameRate
    bCheckForMultiplePawnsSpawnedInAFrame: bool
    NumPawnsAllowedToBeSpawnedInAFrame: int
    bShouldGenerateLowQualityLightmaps: bool
    C_WorldBox: core_uobject.Color
    C_BrushWire: core_uobject.Color
    C_AddWire: core_uobject.Color
    C_SubtractWire: core_uobject.Color
    C_SemiSolidWire: core_uobject.Color
    C_NonSolidWire: core_uobject.Color
    C_WireBackground: core_uobject.Color
    C_ScaleBoxHi: core_uobject.Color
    C_VolumeCollision: core_uobject.Color
    C_BSPCollision: core_uobject.Color
    C_OrthoBackground: core_uobject.Color
    C_Volume: core_uobject.Color
    C_BrushShape: core_uobject.Color
    StreamingDistanceFactor: float
    GameScreenshotSaveDirectory: DirectoryPath
    TransitionType: ETransitionType
    TransitionDescription: str
    TransitionGameMode: str
    MeshLODRange: float
    bAllowMatureLanguage: bool
    CameraRotationThreshold: float
    CameraTranslationThreshold: float
    PrimitiveProbablyVisibleTime: float
    MaxOcclusionPixelsFraction: float
    bPauseOnLossOfFocus: bool
    MaxParticleResize: int
    MaxParticleResizeWarn: int
    PendingDroppedNotes: unreal.WrappedArray[DropNoteInfo]
    NetClientTicksPerSecond: float
    DisplayGamma: float
    MinDesiredFrameRate: float
    DefaultSelectedMaterialColor: core_uobject.LinearColor
    SelectedMaterialColor: core_uobject.LinearColor
    SelectionOutlineColor: core_uobject.LinearColor
    SubduedSelectionOutlineColor: core_uobject.LinearColor
    SelectedMaterialColorOverride: core_uobject.LinearColor
    bIsOverridingSelectedColor: bool
    bEnableOnScreenDebugMessages: bool
    bEnableOnScreenDebugMessagesDisplay: bool
    bSuppressMapWarnings: bool
    bDisableAILogging: bool
    ScreenSaverInhibitorSemaphore: int
    bLockReadOnlyLevels: bool
    ParticleEventManagerClassPath: str
    SelectionHighlightIntensity: float
    SelectionMeshSectionHighlightIntensity: float
    BSPSelectionHighlightIntensity: float
    HoverHighlightIntensity: float
    SelectionHighlightIntensityBillboards: float
    NetDriverDefinitions: unreal.WrappedArray[NetDriverDefinition]
    ChannelClassOverrides: unreal.WrappedArray[NetDriverChannelClassOverride]
    ServerActors: unreal.WrappedArray[str]
    RuntimeServerActors: unreal.WrappedArray[str]
    bStartedLoadMapMovie: bool
    NextWorldContextHandle: int
    GameObjectPoolManager: GameObjectPoolManager
    bSkipReconstructionDuringSeamlessTravel: bool
    MediaManagerClassName: core_uobject.SoftClassPath
    MediaManagerClass: unreal.UClass
    DefaultCullDistanceData: DataAsset
    DefaultCullDistanceDataName: core_uobject.SoftObjectPath
    HideClassInEditor: unreal.WrappedArray[str]



class GameEngine(Engine):
    MaxDeltaTime: float
    ServerFlushLogInterval: float
    GameInstance: GameInstance



class GameInstance(unreal.UObject):
    LocalPlayers: unreal.WrappedArray[LocalPlayer]
    OnlineSession: OnlineSession
    ReferencedObjects: unreal.WrappedArray[unreal.UObject]
    ScreenSizePresets: core_uobject.SoftObjectPath
    CachedScreenSizePresets: DataTable
    def ReceiveShutdown(self): ...
    def ReceiveInit(self): ...
    def HandleTravelError(self, FailureType: int): ...
    def HandleNetworkError(self, FailureType: int, bIsServer: bool): ...
    def DebugRemovePlayer(self, ControllerId: int): ...
    def DebugCreatePlayer(self, ControllerId: int): ...


class GameSession(Info):
    MaxSpectators: int
    MaxPlayers: int
    MaxPartySize: int
    MaxSplitscreensPerConnection: int
    bRequiresPushToTalk: bool
    SessionName: str



class GameUserSettings(unreal.UObject):
    bUseVSync: bool
    bUseDynamicResolution: bool
    WindowPosX: int
    WindowPosY: int
    FullscreenMode: int
    LastConfirmedFullscreenMode: int
    PreferredFullscreenMode: int
    AudioQualityLevel: int
    FrameRateLimit: float
    DesiredScreenWidth: int
    bUseDesiredScreenHeight: bool
    DesiredScreenHeight: int
    LastUserConfirmedDesiredScreenWidth: int
    LastUserConfirmedDesiredScreenHeight: int
    LastRecommendedScreenWidth: float
    LastRecommendedScreenHeight: float
    PreferredMonitor: str
    PreferredMonitorDeviceName: str
    bPrimaryIsPreferredMonitor: bool
    LastCPUBenchmarkResult: float
    LastGPUBenchmarkResult: float
    LastCPUBenchmarkSteps: unreal.WrappedArray[float]
    LastGPUBenchmarkSteps: unreal.WrappedArray[float]
    LastGPUBenchmarkMultiplier: float
    LastBenchmarkResultCPUName: str
    LastBenchmarkResultGPUName: str
    bUseHDRDisplayOutput: bool
    HDRDisplayOutputNits: int
    bUsePerformanceMode: bool
    PreferredGraphicsAPI: str
    PreferredRefreshRate: int
    def ValidateSettings(self): ...
    def SupportsHDRDisplayOutput(self, ReturnValue: bool) -> bool: ...
    def SetVSyncEnabled(self, bEnable: bool): ...
    def SetVisualEffectQuality(self, Value: int): ...
    def SetViewDistanceQuality(self, Value: int): ...
    def SetToDefaults(self): ...
    def SetTextureQuality(self, Value: int): ...
    def SetShadowQuality(self, Value: int): ...
    def SetScreenResolution(self, Resolution: core_uobject.IntPoint): ...
    def SetResolutionScaleValueEx(self, NewScaleValue: float): ...
    def SetResolutionScaleValue(self, NewScaleValue: int): ...
    def SetResolutionScaleNormalized(self, NewScaleNormalized: float): ...
    def SetPreferredRefreshRate(self, NewMode: int): ...
    def SetPreferredMonitor(self, NewMonitor: str): ...
    def SetPreferredGraphicsAPI(self, NewMode: str): ...
    def SetPostProcessingQuality(self, Value: int): ...
    def SetOverallScalabilityLevel(self, Value: int): ...
    def SetFullscreenMode(self, InFullscreenMode: int): ...
    def SetFrameRateLimit(self, NewLimit: float): ...
    def SetFoliageQuality(self, Value: int): ...
    def SetDynamicResolutionEnabled(self, bEnable: bool): ...
    def SetBenchmarkFallbackValues(self): ...
    def SetAudioQualityLevel(self, QualityLevel: int): ...
    def SetAntiAliasingQuality(self, Value: int): ...
    def SaveSettings(self): ...
    def RunHardwareBenchmark(self, WorkScale: int, CPUMultiplier: float, GPUMultiplier: float): ...
    def RevertVideoMode(self): ...
    def ResetToCurrentSettings(self): ...
    def LoadSettings(self, bForceReload: bool): ...
    def IsVSyncEnabled(self, ReturnValue: bool) -> bool: ...
    def IsVSyncDirty(self, ReturnValue: bool) -> bool: ...
    def IsScreenResolutionDirty(self, ReturnValue: bool) -> bool: ...
    def IsHDREnabled(self, ReturnValue: bool) -> bool: ...
    def IsFullscreenModeDirty(self, ReturnValue: bool) -> bool: ...
    def IsDynamicResolutionEnabled(self, ReturnValue: bool) -> bool: ...
    def IsDynamicResolutionDirty(self, ReturnValue: bool) -> bool: ...
    def IsDirty(self, ReturnValue: bool) -> bool: ...
    def GetVisualEffectQuality(self, ReturnValue: int) -> int: ...
    def GetViewDistanceQuality(self, ReturnValue: int) -> int: ...
    def GetTextureQuality(self, ReturnValue: int) -> int: ...
    def GetShadowQuality(self, ReturnValue: int) -> int: ...
    def GetScreenResolution(self, ReturnValue: core_uobject.IntPoint) -> core_uobject.IntPoint: ...
    def GetResolutionScaleInformationEx(self, CurrentScaleNormalized: float, CurrentScaleValue: float, MinScaleValue: float, MaxScaleValue: float): ...
    def GetResolutionScaleInformation(self, CurrentScaleNormalized: float, CurrentScaleValue: int, MinScaleValue: int, MaxScaleValue: int): ...
    def GetRecommendedResolutionScale(self, ReturnValue: float) -> float: ...
    def GetPreferredRefreshRate(self, ReturnValue: int) -> int: ...
    def GetPreferredMonitorDeviceName(self, ReturnValue: str) -> str: ...
    def GetPreferredMonitor(self, ReturnValue: str) -> str: ...
    def GetPreferredGraphicsAPI(self, ReturnValue: str) -> str: ...
    def GetPreferredFullscreenMode(self, ReturnValue: int) -> int: ...
    def GetPostProcessingQuality(self, ReturnValue: int) -> int: ...
    def GetOverallScalabilityLevel(self, ReturnValue: int) -> int: ...
    def GetMonitorDisplayName(self, MonitorIndex: int, ReturnValue: str) -> str: ...
    def GetLastConfirmedScreenResolution(self, ReturnValue: core_uobject.IntPoint) -> core_uobject.IntPoint: ...
    def GetLastConfirmedFullscreenMode(self, ReturnValue: int) -> int: ...
    def GetGraphicsAPIName(self, GraphicsAPIName: str, ReturnValue: str) -> str: ...
    def GetGameUserSettings(self, ReturnValue: GameUserSettings) -> GameUserSettings: ...
    def GetFullscreenMode(self, ReturnValue: int) -> int: ...
    def GetFrameRateLimit(self, ReturnValue: float) -> float: ...
    def GetFoliageQuality(self, ReturnValue: int) -> int: ...
    def GetDesktopResolution(self, ReturnValue: core_uobject.IntPoint) -> core_uobject.IntPoint: ...
    def GetDefaultWindowPosition(self, ReturnValue: core_uobject.IntPoint) -> core_uobject.IntPoint: ...
    def GetDefaultWindowMode(self, ReturnValue: int) -> int: ...
    def GetDefaultResolutionScale(self, ReturnValue: float) -> float: ...
    def GetDefaultResolution(self, ReturnValue: core_uobject.IntPoint) -> core_uobject.IntPoint: ...
    def GetDefaultRefreshRate(self, ReturnValue: int) -> int: ...
    def GetDefaultPreferredMonitor(self, ReturnValue: str) -> str: ...
    def GetDefaultPreferredGraphicsAPI(self, ReturnValue: str) -> str: ...
    def GetCurrentlySupportedGraphicsAPIs(self, OutSupportedAPIs: unreal.WrappedArray[str]): ...
    def GetCurrentHDRDisplayNits(self, ReturnValue: int) -> int: ...
    def GetAudioQualityLevel(self, ReturnValue: int) -> int: ...
    def GetAntiAliasingQuality(self, ReturnValue: int) -> int: ...
    def EnableHDRDisplayOutput(self, bEnable: bool, DisplayNits: int): ...
    def ConfirmVideoMode(self): ...
    def ApplySettings(self, bCheckForCommandLineOverrides: bool): ...
    def ApplyResolutionSettings(self, bCheckForCommandLineOverrides: bool): ...
    def ApplyNonResolutionSettings(self): ...
    def ApplyHardwareBenchmarkResults(self): ...


class ScriptViewportClient(unreal.UObject): ...


class GameViewportClient(ScriptViewportClient):
    ViewportConsole: Console
    DebugProperties: unreal.WrappedArray[DebugDisplayProperty]
    World: World
    GameInstance: GameInstance
    def SSSwapControllers(self): ...
    def ShowTitleSafeArea(self): ...
    def SetConsoleTarget(self, PlayerIndex: int): ...


class LevelScriptActor(Actor):
    bAllowInputBindingsInReleaseBuilds: bool
    bInputEnabled: bool
    def WorldOriginLocationChanged(self, OldOriginLocation: core_uobject.IntVector, NewOriginLocation: core_uobject.IntVector): ...
    def SetCinematicMode(self, bCinematicMode: bool, bHidePlayer: bool, bAffectsHUD: bool, bAffectsMovement: bool, bAffectsTurning: bool): ...
    def RemoteEvent(self, EventName: str, ReturnValue: bool) -> bool: ...
    def LevelReset(self): ...


class LevelStreaming(unreal.UObject):
    PackageNameToLoad: str
    LODPackageNames: unreal.WrappedArray[str]
    LevelTransform: core_uobject.Transform
    LevelLODIndex: int
    bShouldBeVisible: bool
    bShouldBeLoaded: bool
    bLocked: bool
    bIsStatic: bool
    bShouldBlockOnLoad: bool
    bShouldBlockOnUnload: bool
    bDisableDistanceStreaming: bool
    bDrawOnLevelStatusMap: bool
    LevelColor: core_uobject.LinearColor
    EditorStreamingVolumes: unreal.WrappedArray[LevelStreamingVolume]
    MinTimeBetweenVolumeUnloadRequests: float
    LoadedLevel: Level
    PendingUnloadLevel: Level
    def ShouldBeLoaded(self, ReturnValue: bool) -> bool: ...
    def SetShouldBeVisible(self, bInShouldBeVisible: bool): ...
    def SetShouldBeLoaded(self, bInShouldBeLoaded: bool): ...
    def SetLevelLODIndex(self, LODIndex: int): ...
    def IsStreamingStatePending(self, ReturnValue: bool) -> bool: ...
    def IsLevelVisible(self, ReturnValue: bool) -> bool: ...
    def IsLevelLoaded(self, ReturnValue: bool) -> bool: ...
    def GetWorldAssetPackageFName(self, ReturnValue: str) -> str: ...
    def GetLevelScriptActor(self, ReturnValue: LevelScriptActor) -> LevelScriptActor: ...
    def CreateInstance(self, UniqueInstanceName: str, ReturnValue: LevelStreaming) -> LevelStreaming: ...


class GbxLevelStreamingBase(LevelStreaming): ...


class LocalMessage(unreal.UObject): ...


class LocalPlayer(Player):
    ViewportClient: GameViewportClient
    AspectRatioAxisConstraint: int
    PendingLevelPlayerControllerClass: unreal.UClass
    bSentSplitJoin: bool
    ControllerId: int



class MapData(unreal.UObject): ...


class TriggerBase(Actor):
    CollisionComponent: ShapeComponent



class TriggerSphere(TriggerBase): ...


class TriggerBox(TriggerBase): ...


class SaveGame(unreal.UObject): ...


class ReplicationDriver(unreal.UObject): ...


class ReplicationConnectionDriver(unreal.UObject): ...


class TriggerCapsule(TriggerBase): ...


class WindDirectionalSource(Info):
    Component: WindDirectionalSourceComponent



class GbxWindActor(WindDirectionalSource): ...


class ParticleModuleLocationBase(ParticleModule): ...


class StaticMeshActor(Actor):
    StaticMeshComponent: StaticMeshComponent
    bStaticMeshReplicateMovement: bool
    NavigationGeometryGatheringMode: ENavDataGatheringMode
    def SetMobility(self, InMobility: int): ...


class ParticleParameterEvaluator(unreal.UObject): ...


class MaterialBillboardComponent(PrimitiveComponent):
    Elements: unreal.WrappedArray[MaterialSpriteElement]
    def SetElements(self, NewElements: unreal.WrappedArray[MaterialSpriteElement]): ...
    def AddElement(self, Material: MaterialInterface, DistanceToOpacityCurve: CurveFloat, bSizeIsInScreenSpace: bool, BaseSizeX: float, BaseSizeY: float, DistanceToSizeCurve: CurveFloat): ...


class BlueprintAsyncActionBase(unreal.UObject):

    def Activate(self): ...


class InstancedStaticMeshComponent(StaticMeshComponent):
    PerInstanceSMData: unreal.WrappedArray[InstancedStaticMeshInstanceData]
    InstancingRandomSeed: int
    InstanceStartCullDistance: int
    InstanceEndCullDistance: int
    InstanceReorderTable: unreal.WrappedArray[int]
    GbxAllowNegativeScaleForInstances: bool
    NumPendingLightmaps: int
    CachedMappings: unreal.WrappedArray[InstancedStaticMeshMappingInfo]
    def UpdateInstanceTransform(self, InstanceIndex: int, NewInstanceTransform: core_uobject.Transform, bWorldSpace: bool, bMarkRenderStateDirty: bool, bTeleport: bool, ReturnValue: bool) -> bool: ...
    def SetCullDistances(self, StartCullDistance: int, EndCullDistance: int): ...
    def RemoveInstance(self, InstanceIndex: int, ReturnValue: bool) -> bool: ...
    def GetInstanceTransform(self, InstanceIndex: int, OutInstanceTransform: core_uobject.Transform, bWorldSpace: bool, ReturnValue: bool) -> bool: ...
    def GetInstancesOverlappingSphere(self, Center: core_uobject.Vector, Radius: float, bSphereInWorldSpace: bool, ReturnValue: unreal.WrappedArray[int]) -> unreal.WrappedArray[int]: ...
    def GetInstancesOverlappingBox(self, Box: core_uobject.Box, bBoxInWorldSpace: bool, ReturnValue: unreal.WrappedArray[int]) -> unreal.WrappedArray[int]: ...
    def GetInstanceCount(self, ReturnValue: int) -> int: ...
    def ClearInstances(self): ...
    def AddInstanceWorldSpace(self, WorldTransform: core_uobject.Transform, ReturnValue: int) -> int: ...
    def AddInstance(self, InstanceTransform: core_uobject.Transform, ReturnValue: int) -> int: ...


class HierarchicalInstancedStaticMeshComponent(InstancedStaticMeshComponent):
    SortedInstances: unreal.WrappedArray[int]
    NumBuiltInstances: int
    BuiltInstanceBounds: core_uobject.Box
    UnbuiltInstanceBounds: core_uobject.Box
    UnbuiltInstanceBoundsList: unreal.WrappedArray[core_uobject.Box]
    bEnableDensityScaling: bool
    OcclusionLayerNumNodes: int
    CacheMeshExtendedBounds: core_uobject.BoxSphereBounds
    bOverrideFoliageCVars: bool
    MaxInstancesPerLeaf: int
    MinInstancesPerOcclusionQuery: int
    MinOcclusionQueriesPerComponent: int
    MaxOcclusionQueriesPerComponent: int
    ClusterSplitFactor: int
    bDisableCollision: bool
    InstanceCountToRender: int
    def RemoveInstances(self, InstancesToRemove: unreal.WrappedArray[int], ReturnValue: bool) -> bool: ...


class MaterialInterface(unreal.UObject):
    SubsurfaceProfile: SubsurfaceProfile
    LightmassSettings: LightmassMaterialInterfaceSettings
    TextureStreamingData: unreal.WrappedArray[MaterialTextureInfo]
    AssetUserData: unreal.WrappedArray[AssetUserData]
    def SetForceMipLevelsToBeResident(self, OverrideForceMiplevelsToBeResident: bool, bForceMiplevelsToBeResidentValue: bool, ForceDuration: float, CinematicTextureGroups: int): ...
    def GetPhysicalMaterial(self, ReturnValue: PhysicalMaterial) -> PhysicalMaterial: ...
    def GetBaseMaterial(self, ReturnValue: Material) -> Material: ...


class MaterialInstance(MaterialInterface):
    PhysMaterial: PhysicalMaterial
    Parent: MaterialInterface
    bHasStaticPermutationResource: bool
    bOverrideSubsurfaceProfile: bool
    bOverride_IgnoredByFXCoordinator: bool
    bIgnoredByFXCoordinator: bool
    bOverride_IgnoreCustomMask: bool
    bIgnoreCustomMask: bool
    bOverride_IgnoreCustomGlow: bool
    bIgnoreCustomGlow: bool
    ScalarParameterValues: unreal.WrappedArray[ScalarParameterValue]
    VectorParameterValues: unreal.WrappedArray[VectorParameterValue]
    TextureParameterValues: unreal.WrappedArray[TextureParameterValue]
    FontParameterValues: unreal.WrappedArray[FontParameterValue]
    bOverrideBaseProperties: bool
    BasePropertyOverrides: MaterialInstanceBasePropertyOverrides
    PermutationTextureReferences: unreal.WrappedArray[Texture]
    StaticParameters: StaticParameterSet



class MaterialInstanceConstant(MaterialInstance):

    def K2_GetVectorParameterValue(self, ParameterName: str, ReturnValue: core_uobject.LinearColor) -> core_uobject.LinearColor: ...
    def K2_GetTextureParameterValue(self, ParameterName: str, ReturnValue: Texture) -> Texture: ...
    def K2_GetScalarParameterValue(self, ParameterName: str, ReturnValue: float) -> float: ...


class MaterialExpressionCustomOutput(MaterialExpression): ...


class EngineCustomTimeStep(unreal.UObject): ...


class CameraActor(Actor):
    AutoActivateForPlayer: int
    CameraComponent: CameraComponent
    SceneComponent: SceneComponent
    bConstrainAspectRatio: bool
    AspectRatio: float
    FOVAngle: float
    PostProcessBlendWeight: float
    PostProcessSettings: PostProcessSettings
    def GetAutoActivatePlayerIndex(self, ReturnValue: int) -> int: ...


class CameraComponent(SceneComponent):
    FieldOfView: float
    FieldOfViewScalar: float
    OrthoWidth: float
    OrthoNearClipPlane: float
    OrthoFarClipPlane: float
    AspectRatio: float
    bConstrainAspectRatio: bool
    bUseFieldOfViewForLOD: bool
    bLockToHmd: bool
    bUsePawnControlRotation: bool
    ProjectionMode: int
    PostProcessBlendWeight: float
    PostProcessSettings: PostProcessSettings
    bUseControllerViewRotation: bool
    def SetUseFieldOfViewForLOD(self, bInUseFieldOfViewForLOD: bool): ...
    def SetProjectionMode(self, InProjectionMode: int): ...
    def SetPostProcessBlendWeight(self, InPostProcessBlendWeight: float): ...
    def SetOrthoWidth(self, InOrthoWidth: float): ...
    def SetOrthoNearClipPlane(self, InOrthoNearClipPlane: float): ...
    def SetOrthoFarClipPlane(self, InOrthoFarClipPlane: float): ...
    def SetFieldOfView(self, InFieldOfView: float): ...
    def SetConstraintAspectRatio(self, bInConstrainAspectRatio: bool): ...
    def SetAspectRatio(self, InAspectRatio: float): ...
    def GetCameraView(self, DeltaTime: float, DesiredView: MinimalViewInfo): ...


class Model(unreal.UObject): ...


class ActorArchetypeProviderInterface(core_uobject.Interface): ...


class ActorChannel(Channel):
    Actor: Actor
    CreateSubObjects: unreal.WrappedArray[unreal.UObject]



class AnimationAsset(unreal.UObject):
    Skeleton: Skeleton
    MetaData: unreal.WrappedArray[AnimMetaData]
    AssetUserData: unreal.WrappedArray[AssetUserData]



class BlendSpaceBase(AnimationAsset):
    bRotationBlendInMeshSpace: bool
    AnimLength: float
    InterpolationParam: InterpolationParameter
    TargetWeightInterpolationSpeedPerSec: float
    NotifyTriggerMode: int
    PerBoneBlend: unreal.WrappedArray[PerBoneInterpolation]
    SampleIndexWithMarkers: int
    SampleData: unreal.WrappedArray[BlendSample]
    GridSamples: unreal.WrappedArray[EditorElement]
    BlendParameters: BlendParameter



class BlendSpace(BlendSpaceBase):
    AxisToScaleAnimation: int



class AimOffsetBlendSpace(BlendSpace): ...


class BlendSpace1D(BlendSpaceBase):
    bScaleAnimation: bool



class AimOffsetBlendSpace1D(BlendSpace1D): ...


class AmbientSound(Actor):
    AudioComponent: AudioComponent
    def Stop(self): ...
    def Play(self, StartTime: float): ...
    def FadeOut(self, FadeOutDuration: float, FadeVolumeLevel: float): ...
    def FadeIn(self, FadeInDuration: float, FadeVolumeLevel: float): ...
    def AdjustVolume(self, AdjustVolumeDuration: float, AdjustVolumeLevel: float): ...


class AnimationSettings(DeveloperSettings):
    CompressCommandletVersion: int
    KeyEndEffectorsMatchNameArray: unreal.WrappedArray[str]
    DefaultCompressionAlgorithm: unreal.UClass
    RotationCompressionFormat: int
    TranslationCompressionFormat: int
    MaxCurveError: float
    AlternativeCompressionThreshold: float
    ForceRecompression: bool
    bOnlyCheckForMissingSkeletalMeshes: bool
    bForceBelowThreshold: bool
    bFirstRecompressUsingCurrentOrDefault: bool
    bRaiseMaxErrorToExisting: bool
    bTryFixedBitwiseCompression: bool
    bTryPerTrackBitwiseCompression: bool
    bTryLinearKeyRemovalCompression: bool
    bTryIntervalKeyRemoval: bool
    bEnablePerformanceLog: bool
    bStripAnimationDataOnDedicatedServer: bool
    bTickAnimationOnSkeletalMeshInit: bool



class AnimBlueprint(Blueprint):
    TargetSkeleton: Skeleton
    Groups: unreal.WrappedArray[AnimGroupInfo]
    bUseMultiThreadedAnimationUpdate: bool
    bWarnAboutBlueprintUsage: bool



class AnimBlueprintGeneratedClass(BlueprintGeneratedClass):
    BakedStateMachines: unreal.WrappedArray[BakedAnimationStateMachine]
    TargetSkeleton: Skeleton
    AnimNotifies: unreal.WrappedArray[AnimNotifyEvent]
    RootAnimNodeIndex: int
    OrderedSavedPoseIndices: unreal.WrappedArray[int]
    SyncGroupNames: unreal.WrappedArray[str]



class AnimClassData(unreal.UObject):
    BakedStateMachines: unreal.WrappedArray[BakedAnimationStateMachine]
    TargetSkeleton: Skeleton
    AnimNotifies: unreal.WrappedArray[AnimNotifyEvent]
    RootAnimNodeIndex: int
    OrderedSavedPoseIndices: unreal.WrappedArray[int]
    RootAnimNodeProperty: core_uobject.StructProperty
    AnimNodeProperties: unreal.WrappedArray[core_uobject.StructProperty]
    SyncGroupNames: unreal.WrappedArray[str]



class AnimClassInterface(core_uobject.Interface): ...


class AnimSequenceBase(AnimationAsset):
    Notifies: unreal.WrappedArray[AnimNotifyEvent]
    SequenceLength: float
    RateScale: float
    RawCurveData: RawCurveTracks
    def GetPlayLength(self, ReturnValue: float) -> float: ...


class AnimCompositeBase(AnimSequenceBase): ...


class AnimComposite(AnimCompositeBase):
    AnimationTrack: AnimTrack



class AnimCompress_Automatic(AnimCompress):
    MaxEndEffectorError: float
    bTryFixedBitwiseCompression: bool
    bTryPerTrackBitwiseCompression: bool
    bTryLinearKeyRemovalCompression: bool
    bTryIntervalKeyRemoval: bool
    bRunCurrentDefaultCompressor: bool
    bAutoReplaceIfExistingErrorTooGreat: bool
    bRaiseMaxErrorToExisting: bool



class AnimCompress_BitwiseCompressOnly(AnimCompress): ...


class AnimCompress_LeastDestructive(AnimCompress): ...


class AnimCompress_RemoveLinearKeys(AnimCompress):
    MaxPosDiff: float
    MaxAngleDiff: float
    MaxScaleDiff: float
    MaxEffectorDiff: float
    MinEffectorDiff: float
    EffectorDiffSocket: float
    ParentKeyScale: float
    bRetarget: bool
    bActuallyFilterLinearKeys: bool



class AnimCompress_PerTrackCompression(AnimCompress_RemoveLinearKeys):
    MaxZeroingThreshold: float
    MaxPosDiffBitwise: float
    MaxAngleDiffBitwise: float
    MaxScaleDiffBitwise: float
    AllowedRotationFormats: unreal.WrappedArray[int]
    AllowedTranslationFormats: unreal.WrappedArray[int]
    AllowedScaleFormats: unreal.WrappedArray[int]
    bResampleAnimation: bool
    ResampledFramerate: float
    MinKeysForResampling: int
    bUseAdaptiveError: bool
    bUseOverrideForEndEffectors: bool
    TrackHeightBias: int
    ParentingDivisor: float
    ParentingDivisorExponent: float
    bUseAdaptiveError2: bool
    RotationErrorSourceRatio: float
    TranslationErrorSourceRatio: float
    ScaleErrorSourceRatio: float
    MaxErrorPerTrackRatio: float
    PerturbationProbeSize: float



class AnimCompress_RemoveEverySecondKey(AnimCompress):
    MinKeys: int
    bStartAtSecondKey: bool



class AnimCompress_RemoveTrivialKeys(AnimCompress):
    MaxPosDiff: float
    MaxAngleDiff: float
    MaxScaleDiff: float



class AnimMetaData(unreal.UObject): ...


class AnimMontage(AnimCompositeBase):
    BlendIn: AlphaBlend
    BlendInTime: float
    BlendOut: AlphaBlend
    BlendOutTime: float
    BlendOutTriggerTime: float
    SyncGroup: str
    SyncSlotIndex: int
    MarkerData: MarkerSyncData
    CompositeSections: unreal.WrappedArray[CompositeSection]
    SlotAnimTracks: unreal.WrappedArray[SlotAnimationTrack]
    BranchingPoints: unreal.WrappedArray[BranchingPoint]
    bEnableRootMotionTranslation: bool
    bEnableRootMotionRotation: bool
    bEnableAutoBlendOut: bool
    RootMotionRootLock: int
    BranchingPointMarkers: unreal.WrappedArray[BranchingPointMarker]
    BranchingPointStateNotifyIndices: unreal.WrappedArray[int]
    TimeStretchCurve: TimeStretchCurve
    TimeStretchCurveName: str



class AnimNotify_PlayParticleEffect(AnimNotify):
    PSTemplate: ParticleSystem
    LocationOffset: core_uobject.Vector
    RotationOffset: core_uobject.Rotator
    Scale: core_uobject.Vector
    Attached: bool
    bInheritViewFlags: bool
    SocketName: str
    bInheritScale: bool
    FilterMeshes: unreal.WrappedArray[SkeletalMesh]



class AnimNotify_PlaySound(AnimNotify):
    Sound: SoundBase
    VolumeMultiplier: float
    PitchMultiplier: float
    bFollow: bool
    AttachName: str



class AnimNotify_ResetClothingSimulation(AnimNotify): ...


class AnimNotifyState_DisableRootMotion(AnimNotifyState): ...


class AnimNotifyState_TimedParticleEffect(AnimNotifyState):
    PSTemplate: ParticleSystem
    SocketName: str
    LocationOffset: core_uobject.Vector
    RotationOffset: core_uobject.Rotator
    bDestroyAtEnd: bool
    bInheritViewFlags: bool



class AnimNotifyState_Trail(AnimNotifyState):
    PSTemplate: ParticleSystem
    FirstSocketName: str
    SecondSocketName: str
    WidthScaleMode: int
    WidthScaleCurve: str
    bRecycleSpawnedSystems: bool
    def OverridePSTemplate(self, MeshComp: SkeletalMeshComponent, Animation: AnimSequenceBase, ReturnValue: ParticleSystem) -> ParticleSystem: ...


class AnimSequence(AnimSequenceBase):
    NumFrames: int
    TrackToSkeletonMapTable: unreal.WrappedArray[TrackToSkeletonMap]
    AdditiveAnimType: int
    RefPoseType: int
    RefPoseSeq: AnimSequence
    RefFrameIndex: int
    EncodingPkgVersion: int
    RetargetSource: str
    Interpolation: EAnimInterpolationType
    bEnableRootMotion: bool
    RootMotionRootLock: int
    bForceRootLock: bool
    bRootMotionSettingsCopiedFromMontage: bool
    AuthoredSyncMarkers: unreal.WrappedArray[AnimSyncMarker]
    bEnableGbxRootMotionSync: bool
    BlendStartMarker: AnimSyncMarker
    bKeepAnimatedScale: bool
    CachedRootSpeed: float
    def GetBoneTransform(self, BoneName: str, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...


class AnimSet(unreal.UObject):
    bAnimRotationOnly: bool
    TrackBoneNames: unreal.WrappedArray[str]
    LinkupCache: unreal.WrappedArray[AnimSetMeshLinkup]
    BoneUseAnimTranslation: unreal.WrappedArray[int]
    ForceUseMeshTranslation: unreal.WrappedArray[int]
    UseTranslationBoneNames: unreal.WrappedArray[str]
    ForceMeshTranslationBoneNames: unreal.WrappedArray[str]
    PreviewSkelMeshName: str
    BestRatioSkelMeshName: str



class AnimSingleNodeInstance(AnimInstance):
    CurrentAsset: AnimationAsset
    def StopAnim(self): ...
    def SetReverse(self, bInReverse: bool): ...
    def SetPreviewCurveOverride(self, PoseName: str, Value: float, bRemoveIfZero: bool): ...
    def SetPositionWithPreviousTime(self, InPosition: float, InPreviousTime: float, bFireNotifies: bool): ...
    def SetPosition(self, InPosition: float, bFireNotifies: bool): ...
    def SetPlayRate(self, InPlayRate: float): ...
    def SetPlaying(self, bIsPlaying: bool): ...
    def SetLooping(self, bIsLooping: bool): ...
    def SetBlendSpaceInput(self, InBlendInput: core_uobject.Vector): ...
    def SetAnimationAsset(self, NewAsset: AnimationAsset, bIsLooping: bool, InPlayRate: float): ...
    def PlayAnim(self, bIsLooping: bool, InPlayRate: float, InStartPosition: float): ...
    def GetLength(self, ReturnValue: float) -> float: ...
    def GetAnimationAsset(self, ReturnValue: AnimationAsset) -> AnimationAsset: ...


class AnimStateMachineTypes(unreal.UObject): ...


class ApplicationLifecycleComponent(ActorComponent): ...


class ArrowComponent(PrimitiveComponent):
    ArrowColor: core_uobject.Color
    ArrowSize: float
    bIsScreenSizeScaled: bool
    ScreenSize: float
    bTreatAsASprite: bool
    def SetArrowColor(self, NewColor: core_uobject.LinearColor): ...


class AssetExportTask(unreal.UObject):
    Object: unreal.UObject
    Exporter: Exporter
    Filename: str
    bSelected: bool
    bReplaceIdentical: bool
    bPrompt: bool
    bAutomated: bool
    bUseFileArchive: bool
    bWriteEmptyFiles: bool
    IgnoreObjectList: unreal.WrappedArray[unreal.UObject]
    Options: unreal.UObject
    Errors: unreal.WrappedArray[str]



class AssetManagerSettings(DeveloperSettings):
    PrimaryAssetTypesToScan: unreal.WrappedArray[PrimaryAssetTypeInfo]
    DirectoriesToExclude: unreal.WrappedArray[DirectoryPath]
    PrimaryAssetRules: unreal.WrappedArray[PrimaryAssetRulesOverride]
    bOnlyCookProductionAssets: bool
    bShouldManagerDetermineTypeAndName: bool
    bShouldGuessTypeAndNameInEditor: bool
    bShouldAcquireMissingChunksOnLoad: bool
    PrimaryAssetIdRedirects: unreal.WrappedArray[AssetManagerRedirect]
    PrimaryAssetTypeRedirects: unreal.WrappedArray[AssetManagerRedirect]
    AssetPathRedirects: unreal.WrappedArray[AssetManagerRedirect]



class AssetMappingTable(unreal.UObject):
    MappedAssets: unreal.WrappedArray[AssetMapping]



class AsyncActionLoadPrimaryAssetBase(BlueprintAsyncActionBase): ...


class AsyncActionLoadPrimaryAsset(AsyncActionLoadPrimaryAssetBase):

    def AsyncLoadPrimaryAsset(self, WorldContextObject: unreal.UObject, PrimaryAsset: core_uobject.PrimaryAssetId, LoadBundles: unreal.WrappedArray[str], ReturnValue: AsyncActionLoadPrimaryAsset) -> AsyncActionLoadPrimaryAsset: ...


class AsyncActionLoadPrimaryAssetClass(AsyncActionLoadPrimaryAssetBase):

    def AsyncLoadPrimaryAssetClass(self, WorldContextObject: unreal.UObject, PrimaryAsset: core_uobject.PrimaryAssetId, LoadBundles: unreal.WrappedArray[str], ReturnValue: AsyncActionLoadPrimaryAssetClass) -> AsyncActionLoadPrimaryAssetClass: ...


class AsyncActionLoadPrimaryAssetList(AsyncActionLoadPrimaryAssetBase):

    def AsyncLoadPrimaryAssetList(self, WorldContextObject: unreal.UObject, PrimaryAssetList: unreal.WrappedArray[core_uobject.PrimaryAssetId], LoadBundles: unreal.WrappedArray[str], ReturnValue: AsyncActionLoadPrimaryAssetList) -> AsyncActionLoadPrimaryAssetList: ...


class AsyncActionLoadPrimaryAssetClassList(AsyncActionLoadPrimaryAssetBase):

    def AsyncLoadPrimaryAssetClassList(self, WorldContextObject: unreal.UObject, PrimaryAssetList: unreal.WrappedArray[core_uobject.PrimaryAssetId], LoadBundles: unreal.WrappedArray[str], ReturnValue: AsyncActionLoadPrimaryAssetClassList) -> AsyncActionLoadPrimaryAssetClassList: ...


class AsyncActionChangePrimaryAssetBundles(AsyncActionLoadPrimaryAssetBase):

    def AsyncChangeBundleStateForPrimaryAssetList(self, WorldContextObject: unreal.UObject, PrimaryAssetList: unreal.WrappedArray[core_uobject.PrimaryAssetId], AddBundles: unreal.WrappedArray[str], RemoveBundles: unreal.WrappedArray[str], ReturnValue: AsyncActionChangePrimaryAssetBundles) -> AsyncActionChangePrimaryAssetBundles: ...
    def AsyncChangeBundleStateForMatchingPrimaryAssets(self, WorldContextObject: unreal.UObject, NewBundles: unreal.WrappedArray[str], OldBundles: unreal.WrappedArray[str], ReturnValue: AsyncActionChangePrimaryAssetBundles) -> AsyncActionChangePrimaryAssetBundles: ...


class AtmosphericFog(Info):
    AtmosphericFogComponent: AtmosphericFogComponent



class AtmosphericFogComponent(SceneComponent):
    SunMultiplier: float
    FogMultiplier: float
    DensityMultiplier: float
    DensityOffset: float
    DistanceScale: float
    AltitudeScale: float
    DistanceOffset: float
    GroundOffset: float
    StartDistance: float
    SunDiscScale: float
    DefaultBrightness: float
    DefaultLightColor: core_uobject.Color
    bDisableSunDisk: bool
    bDisableGroundScattering: bool
    PrecomputeParams: AtmospherePrecomputeParameters
    TransmittanceTexture: Texture2D
    IrradianceTexture: Texture2D
    PitchOffset: float
    def StartPrecompute(self): ...
    def SetSunMultiplier(self, NewSunMultiplier: float): ...
    def SetStartDistance(self, NewStartDistance: float): ...
    def SetPrecomputeParams(self, DensityHeight: float, MaxScatteringOrder: int, InscatterAltitudeSampleNum: int): ...
    def SetFogMultiplier(self, NewFogMultiplier: float): ...
    def SetDistanceScale(self, NewDistanceScale: float): ...
    def SetDistanceOffset(self, NewDistanceOffset: float): ...
    def SetDensityOffset(self, NewDensityOffset: float): ...
    def SetDensityMultiplier(self, NewDensityMultiplier: float): ...
    def SetDefaultLightColor(self, NewLightColor: core_uobject.LinearColor): ...
    def SetDefaultBrightness(self, NewBrightness: float): ...
    def SetAltitudeScale(self, NewAltitudeScale: float): ...
    def DisableSunDisk(self, NewSunDisk: bool): ...
    def DisableGroundScattering(self, NewGroundScattering: bool): ...


class AudioSettings(DeveloperSettings):
    DefaultSoundClassName: core_uobject.SoftObjectPath
    DefaultMediaSoundClassName: core_uobject.SoftObjectPath
    DefaultSoundConcurrencyName: core_uobject.SoftObjectPath
    DefaultBaseSoundMix: core_uobject.SoftObjectPath
    VoiPSoundClass: core_uobject.SoftObjectPath
    VoiPSampleRate: EVoiceSampleRate
    VoipBufferingDelay: float
    DefaultReverbSendLevel: float
    MaximumConcurrentStreams: int
    QualityLevels: unreal.WrappedArray[AudioQualitySettings]
    bAllowVirtualizedSounds: bool
    bDisableMasterEQ: bool
    bAllowCenterChannel3DPanning: bool
    PanningMethod: EPanningMethod
    MonoChannelUpmixMethod: EMonoChannelUpmixMethod
    DialogueFilenameFormat: str



class AudioVolume(Volume):
    Priority: float
    bEnabled: bool
    Settings: ReverbSettings
    AmbientZoneSettings: InteriorSettings
    def SetReverbSettings(self, NewReverbSettings: ReverbSettings): ...
    def SetPriority(self, NewPriority: float): ...
    def SetInteriorSettings(self, NewInteriorSettings: InteriorSettings): ...
    def SetEnabled(self, bNewEnabled: bool): ...
    def OnRep_bEnabled(self): ...


class AutomationTestSettings(unreal.UObject):
    EngineTestModules: unreal.WrappedArray[str]
    EditorTestModules: unreal.WrappedArray[str]
    AutomationTestmap: core_uobject.SoftObjectPath
    EditorPerformanceTestMaps: unreal.WrappedArray[EditorMapPerformanceTestDefinition]
    AssetsToOpen: unreal.WrappedArray[core_uobject.SoftObjectPath]
    BuildPromotionTest: BuildPromotionTestSettings
    MaterialEditorPromotionTest: MaterialEditorPromotionSettings
    ParticleEditorPromotionTest: ParticleEditorPromotionSettings
    BlueprintEditorPromotionTest: BlueprintEditorPromotionSettings
    TestLevelFolders: unreal.WrappedArray[str]
    ExternalTools: unreal.WrappedArray[ExternalToolDefinition]
    ImportExportTestDefinitions: unreal.WrappedArray[EditorImportExportTestDefinition]
    LaunchOnSettings: unreal.WrappedArray[LaunchOnTestSettings]
    DefaultScreenshotResolution: core_uobject.IntPoint



class AvoidanceManager(unreal.UObject):
    DefaultTimeToLive: float
    LockTimeAfterAvoid: float
    LockTimeAfterClean: float
    DeltaTimeToPredict: float
    ArtificialRadiusExpansion: float
    TestHeightDifference: float
    HeightCheckMargin: float
    def RegisterMovementComponent(self, MovementComp: MovementComponent, AvoidanceWeight: float, ReturnValue: bool) -> bool: ...
    def GetObjectCount(self, ReturnValue: int) -> int: ...
    def GetNewAvoidanceUID(self, ReturnValue: int) -> int: ...
    def GetAvoidanceVelocityForComponent(self, MovementComp: MovementComponent, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...


class BillboardComponent(PrimitiveComponent):
    Sprite: Texture
    bIsScreenSizeScaled: bool
    ScreenSize: float
    U: float
    UL: float
    V: float
    VL: float
    def SetUV(self, NewU: int, NewUL: int, NewV: int, NewVL: int): ...
    def SetSpriteAndUV(self, NewSprite: Texture2D, NewU: int, NewUL: int, NewV: int, NewVL: int): ...
    def SetSprite(self, NewSprite: Texture2D): ...


class BlendableInterface(core_uobject.Interface): ...


class Skeleton(unreal.UObject):
    BoneTree: unreal.WrappedArray[BoneNode]
    RefLocalPoses: unreal.WrappedArray[core_uobject.Transform]
    VirtualBoneGuid: core_uobject.Guid
    VirtualBones: unreal.WrappedArray[VirtualBone]
    Sockets: unreal.WrappedArray[SkeletalMeshSocket]
    SmartNames: SmartNameContainer
    BlendProfiles: unreal.WrappedArray[BlendProfile]
    SlotGroups: unreal.WrappedArray[AnimSlotGroup]
    AssetUserData: unreal.WrappedArray[AssetUserData]



class BlendProfile(unreal.UObject):
    OwningSkeleton: Skeleton
    ProfileEntries: unreal.WrappedArray[BlendProfileBoneEntry]



class BlockingVolume(Volume): ...


class BlueprintMapLibrary(BlueprintFunctionLibrary): ...


class PlatformGameInstance(GameInstance): ...


class BlueprintPlatformLibrary(BlueprintFunctionLibrary):

    def ScheduleLocalNotificationFromNow(self, inSecondsFromNow: int, Title: str, Body: str, Action: str, ActivationEvent: str): ...
    def ScheduleLocalNotificationBadgeFromNow(self, inSecondsFromNow: int, ActivationEvent: str): ...
    def ScheduleLocalNotificationBadgeAtTime(self, FireDateTime: core_uobject.DateTime, LocalTime: bool, ActivationEvent: str): ...
    def ScheduleLocalNotificationAtTime(self, FireDateTime: core_uobject.DateTime, LocalTime: bool, Title: str, Body: str, Action: str, ActivationEvent: str): ...
    def GetLaunchNotification(self, NotificationLaunchedApp: bool, ActivationEvent: str, FireDate: int): ...
    def ClearAllLocalNotifications(self): ...
    def CancelLocalNotification(self, ActivationEvent: str): ...


class BlueprintSetLibrary(BlueprintFunctionLibrary): ...


class BodySetup(unreal.UObject):
    AggGeom: KAggregateGeom
    BoneName: str
    PhysicsType: int
    bAlwaysFullAnimWeight: bool
    bConsiderForBounds: bool
    bMeshCollideAll: bool
    bDoubleSidedGeometry: bool
    bGenerateNonMirroredCollision: bool
    bSharedCookedData: bool
    bGenerateMirroredCollision: bool
    CollisionReponse: int
    CollisionTraceFlag: int
    PhysMaterial: PhysicalMaterial
    WalkableSlopeOverride: WalkableSlopeOverride
    NavGeometrySettings: HavokNavGeometrySettings
    DefaultInstance: BodyInstance
    BuildScale3D: core_uobject.Vector



class BoneMaskFilter(unreal.UObject):
    BlendPoses: unreal.WrappedArray[InputBlendPose]



class BookMark(unreal.UObject):
    Location: core_uobject.Vector
    Rotation: core_uobject.Rotator
    HiddenLevels: unreal.WrappedArray[str]



class BookMark2D(unreal.UObject):
    Zoom2D: float
    Location: core_uobject.IntPoint



class ReflectionCapture(Actor):
    CaptureComponent: ReflectionCaptureComponent



class BoxReflectionCapture(ReflectionCapture): ...


class ReflectionCaptureComponent(SceneComponent):
    CaptureOffsetComponent: BillboardComponent
    ReflectionSourceType: EReflectionSourceType
    Cubemap: TextureCube
    SourceCubemapAngle: float
    Brightness: float
    CaptureOffset: core_uobject.Vector
    MapBuildDataId: core_uobject.Guid



class BoxReflectionCaptureComponent(ReflectionCaptureComponent):
    BoxTransitionDistance: float
    PreviewInfluenceBox: BoxComponent
    PreviewCaptureBox: BoxComponent



class Breakpoint(unreal.UObject):
    bEnabled: bool
    Node: EdGraphNode
    bStepOnce: bool
    bStepOnce_WasPreviouslyDisabled: bool
    bStepOnce_RemoveAfterHit: bool



class BrushBuilder(unreal.UObject):
    BitmapFilename: str
    Tooltip: str
    NotifyBadParams: bool
    Vertices: unreal.WrappedArray[core_uobject.Vector]
    Polys: unreal.WrappedArray[BuilderPoly]
    Layer: str
    MergeCoplanars: bool



class BrushComponent(PrimitiveComponent):
    Brush: Model
    BrushBodySetup: BodySetup
    PrePivot: core_uobject.Vector



class BrushShape(Brush): ...


class ButtonStyleAsset(unreal.UObject):
    ButtonStyle: slate_core.ButtonStyle



class CameraAnim(unreal.UObject):
    CameraInterpGroup: InterpGroup
    AnimLength: float
    BoundingBox: core_uobject.Box
    bRelativeToInitialTransform: bool
    bRelativeToInitialFOV: bool
    BaseFOV: float
    BasePostProcessSettings: PostProcessSettings
    BasePostProcessBlendWeight: float



class CameraAnimInst(unreal.UObject):
    CamAnim: CameraAnim
    InterpGroupInst: InterpGroupInst
    PlayRate: float
    MoveTrack: InterpTrackMove
    MoveInst: InterpTrackInstMove
    PlaySpace: int
    def Stop(self, bImmediate: bool): ...
    def SetScale(self, NewDuration: float): ...
    def SetDuration(self, NewDuration: float): ...


class CameraBlockingVolume(Volume): ...


class CameraModifier(unreal.UObject):
    bDebug: bool
    bExclusive: bool
    Priority: int
    CameraOwner: PlayerCameraManager
    AlphaInTime: float
    AlphaOutTime: float
    Alpha: float
    def IsDisabled(self, ReturnValue: bool) -> bool: ...
    def GetViewTarget(self, ReturnValue: Actor) -> Actor: ...
    def EnableModifier(self): ...
    def DisableModifier(self, bImmediate: bool): ...
    def BlueprintModifyPostProcess(self, DeltaTime: float, PostProcessBlendWeight: float, PostProcessSettings: PostProcessSettings): ...
    def BlueprintModifyCamera(self, DeltaTime: float, ViewLocation: core_uobject.Vector, ViewRotation: core_uobject.Rotator, FOV: float, NewViewLocation: core_uobject.Vector, NewViewRotation: core_uobject.Rotator, NewFOV: float): ...


class CameraModifier_CameraShake(CameraModifier):
    ActiveShakes: unreal.WrappedArray[CameraShake]
    ActiveShakeDatas: unreal.WrappedArray[CameraShakeData]
    SplitScreenShakeScale: float



class CameraShake(unreal.UObject):
    bSingleInstance: bool
    OscillationDuration: float
    OscillationBlendInTime: float
    OscillationBlendOutTime: float
    RotOscillation: ROscillator
    LocOscillation: VOscillator
    FOVOscillation: FOscillator
    AnimPlayRate: float
    AnimScale: float
    AnimBlendInTime: float
    AnimBlendOutTime: float
    RandomAnimSegmentDuration: float
    Anim: CameraAnim
    bRandomAnimSegment: bool
    CameraOwner: PlayerCameraManager
    ShakeScale: float
    OscillatorTimeRemaining: float
    AnimInst: CameraAnimInst
    def ReceiveStopShake(self, bImmediately: bool): ...
    def ReceivePlayShake(self, Scale: float): ...
    def ReceiveIsFinished(self, ReturnValue: bool) -> bool: ...
    def BlueprintUpdateCameraShake(self, DeltaTime: float, Alpha: float, POV: MinimalViewInfo, ModifiedPOV: MinimalViewInfo): ...


class Canvas(unreal.UObject):
    OrgX: float
    OrgY: float
    ClipX: float
    ClipY: float
    DrawColor: core_uobject.Color
    bCenterX: bool
    bCenterY: bool
    bNoSmooth: bool
    SizeX: int
    SizeY: int
    ColorModulate: core_uobject.Plane
    DefaultTexture: Texture2D
    ReporterGraph: ReporterGraph
    def K2_TextSize(self, RenderFont: Font, RenderText: str, Scale: core_uobject.Vector2D, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def K2_StrLen(self, RenderFont: Font, RenderText: str, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def K2_Project(self, WorldLocation: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def K2_DrawTriangle(self, RenderTexture: Texture, Triangles: unreal.WrappedArray[CanvasUVTri]): ...
    def K2_DrawTexture(self, RenderTexture: Texture, ScreenPosition: core_uobject.Vector2D, ScreenSize: core_uobject.Vector2D, CoordinatePosition: core_uobject.Vector2D, CoordinateSize: core_uobject.Vector2D, RenderColor: core_uobject.LinearColor, BlendMode: int, Rotation: float, PivotPoint: core_uobject.Vector2D): ...
    def K2_DrawText(self, RenderFont: Font, RenderText: str, ScreenPosition: core_uobject.Vector2D, RenderColor: core_uobject.LinearColor, Kerning: float, ShadowColor: core_uobject.LinearColor, ShadowOffset: core_uobject.Vector2D, bCentreX: bool, bCentreY: bool, bOutlined: bool, OutlineColor: core_uobject.LinearColor): ...
    def K2_DrawPolygon(self, RenderTexture: Texture, ScreenPosition: core_uobject.Vector2D, Radius: core_uobject.Vector2D, NumberOfSides: int, RenderColor: core_uobject.LinearColor): ...
    def K2_DrawMaterialTriangle(self, RenderMaterial: MaterialInterface, Triangles: unreal.WrappedArray[CanvasUVTri]): ...
    def K2_DrawMaterial(self, RenderMaterial: MaterialInterface, ScreenPosition: core_uobject.Vector2D, ScreenSize: core_uobject.Vector2D, CoordinatePosition: core_uobject.Vector2D, CoordinateSize: core_uobject.Vector2D, Rotation: float, PivotPoint: core_uobject.Vector2D): ...
    def K2_DrawLine(self, ScreenPositionA: core_uobject.Vector2D, ScreenPositionB: core_uobject.Vector2D, Thickness: float, RenderColor: core_uobject.LinearColor): ...
    def K2_DrawBox(self, ScreenPosition: core_uobject.Vector2D, ScreenSize: core_uobject.Vector2D, Thickness: float, RenderColor: core_uobject.LinearColor): ...
    def K2_DrawBorder(self, BorderTexture: Texture, BackgroundTexture: Texture, LeftBorderTexture: Texture, RightBorderTexture: Texture, TopBorderTexture: Texture, BottomBorderTexture: Texture, ScreenPosition: core_uobject.Vector2D, ScreenSize: core_uobject.Vector2D, CoordinatePosition: core_uobject.Vector2D, CoordinateSize: core_uobject.Vector2D, RenderColor: core_uobject.LinearColor, BorderScale: core_uobject.Vector2D, BackgroundScale: core_uobject.Vector2D, Rotation: float, PivotPoint: core_uobject.Vector2D, CornerSize: core_uobject.Vector2D): ...
    def K2_Deproject(self, ScreenPosition: core_uobject.Vector2D, WorldOrigin: core_uobject.Vector, WorldDirection: core_uobject.Vector): ...


class Texture(unreal.UObject):
    LightingGuid: core_uobject.Guid
    LODBias: int
    NumCinematicMipLevels: int
    CompressionSettings: int
    Filter: int
    LODGroup: int
    SRGB: bool
    NeverStream: bool
    bNoTiling: bool
    bUseCinematicMipLevels: bool
    bAsyncResourceReleaseHasBeenStarted: bool
    CachedCombinedLODBias: int
    AssetUserData: unreal.WrappedArray[AssetUserData]



class TextureRenderTarget(Texture):
    TargetGamma: float



class TextureRenderTarget2D(TextureRenderTarget):
    SizeX: int
    SizeY: int
    ClearColor: core_uobject.LinearColor
    AddressX: int
    AddressY: int
    bForceLinearGamma: bool
    bOverwriteScaleformSRGB: bool
    bHDR: bool
    bGPUSharedFlag: bool
    bAutoGenerateMips: bool
    RenderTargetFormat: int
    OverrideFormat: int



class CanvasRenderTarget2D(TextureRenderTarget2D):
    World: World
    bShouldClearRenderTargetOnReceiveUpdate: bool
    def UpdateResource(self): ...
    def ReceiveUpdate(self, Canvas: Canvas, Width: int, Height: int): ...
    def GetSize(self, Width: int, Height: int): ...
    def CreateCanvasRenderTarget2D(self, WorldContextObject: unreal.UObject, CanvasRenderTarget2DClass: unreal.UClass, Width: int, Height: int, ReturnValue: CanvasRenderTarget2D) -> CanvasRenderTarget2D: ...


class CheckBoxStyleAsset(unreal.UObject):
    CheckBoxStyle: slate_core.CheckBoxStyle



class ChildConnection(NetConnection):
    Parent: NetConnection



class PlatformInterfaceBase(unreal.UObject):
    AllDelegates: unreal.WrappedArray[DelegateArray]



class CloudStorageBase(PlatformInterfaceBase):
    LocalCloudFiles: unreal.WrappedArray[str]
    bSuppressDelegateCalls: bool



class CollisionProfile(DeveloperSettings):
    Profiles: unreal.WrappedArray[CollisionResponseTemplate]
    DefaultChannelResponses: unreal.WrappedArray[CustomChannelSetup]
    EditProfiles: unreal.WrappedArray[CustomProfile]
    ProfileRedirects: unreal.WrappedArray[Redirector]
    CollisionChannelRedirects: unreal.WrappedArray[Redirector]



class ComponentDelegateBinding(DynamicBlueprintBinding):
    ComponentDelegateBindings: unreal.WrappedArray[BlueprintComponentDelegateBinding]



class Console(unreal.UObject):
    ConsoleTargetPlayer: LocalPlayer
    DefaultTexture_Black: Texture2D
    DefaultTexture_White: Texture2D
    HistoryBuffer: unreal.WrappedArray[str]



class ControlChannel(Channel): ...


class ControlRigInterface(core_uobject.Interface): ...


class StreamingSettings(DeveloperSettings):
    AsyncLoadingThreadEnabled: bool
    WarnIfTimeLimitExceeded: bool
    TimeLimitExceededMultiplier: float
    TimeLimitExceededMinTime: float
    MinBulkDataSizeForAsyncLoading: int
    UseBackgroundLevelStreaming: bool
    AsyncLoadingUseFullTimeLimit: bool
    AsyncLoadingTimeLimit: float
    PriorityAsyncLoadingExtraTime: float
    LevelStreamingActorsUpdateTimeLimit: float
    PriorityLevelStreamingActorsUpdateExtraTime: float
    LevelStreamingComponentsRegistrationGranularity: int
    LevelStreamingUnregisterComponentsTimeLimit: float
    LevelStreamingComponentsUnregistrationGranularity: int
    EventDrivenLoaderEnabled: bool



class GarbageCollectionSettings(DeveloperSettings):
    TimeBetweenPurgingPendingKillObjects: float
    FlushStreamingOnGC: bool
    AllowParallelGC: bool
    IncrementalBeginDestroyEnabled: bool
    CreateGCClusters: bool
    MergeGCClusters: bool
    ActorClusteringEnabled: bool
    BlueprintClusteringEnabled: bool
    UseDisregardForGCOnDedicatedServers: bool
    MinGCClusterSize: int
    NumRetriesBeforeForcingGC: int
    MaxObjectsNotConsideredByGC: int
    SizeOfPermanentObjectPool: int
    MaxObjectsInGame: int
    MaxObjectsInEditor: int
    DissolveClustersOnTransitions: int



class CullDistanceData(DataAsset):
    CullDistances: unreal.WrappedArray[CullDistanceSizePair]



class CullDistanceVolume(Volume):
    CullingMethod: ECullMethod
    CullDistances: unreal.WrappedArray[CullDistanceSizePair]
    bEnabled: bool
    bDominantLevelVolume: bool



class CurveBase(unreal.UObject):

    def GetValueRange(self, MinValue: float, MaxValue: float): ...
    def GetTimeRange(self, MinTime: float, MaxTime: float): ...


class CurveEdPresetCurve(unreal.UObject): ...


class CurveFloat(CurveBase):
    FloatCurve: RichCurve
    bIsEventCurve: bool
    def GetFloatValue(self, InTime: float, ReturnValue: float) -> float: ...


class CurveLinearColor(CurveBase):
    FloatCurves: RichCurve
    AdjustHue: float
    AdjustSaturation: float
    AdjustBrightness: float
    AdjustBrightnessCurve: float
    AdjustVibrance: float
    AdjustMinAlpha: float
    AdjustMaxAlpha: float
    def GetLinearColorValue(self, InTime: float, ReturnValue: core_uobject.LinearColor) -> core_uobject.LinearColor: ...


class TextureStreaming(Texture):
    StreamingIndex: int
    LevelIndex: int
    FirstResourceMemMip: int
    bTemporarilyDisableStreaming: bool
    bIsStreamable: bool
    bHasStreamingUpdatePending: bool
    bForceMiplevelsToBeResident: bool
    bIgnoreStreamingMipBias: bool
    bGlobalForceMipLevelsToBeResident: bool
    ImportedSize: core_uobject.IntPoint
    ForceMipLevelsToBeResidentTimestamp: float
    ForceResidentMiplevelBias: int



class Texture2D(TextureStreaming):
    AddressX: int
    AddressY: int
    def Blueprint_GetSizeY(self, ReturnValue: int) -> int: ...
    def Blueprint_GetSizeX(self, ReturnValue: int) -> int: ...


class CurveLinearColorAtlas(Texture2D):
    GradientCurves: unreal.WrappedArray[CurveLinearColor]
    def GetCurvePosition(self, InCurve: CurveLinearColor, Position: float, ReturnValue: bool) -> bool: ...
    def GetCurveIndex(self, InCurve: CurveLinearColor, Index: int, ReturnValue: bool) -> bool: ...


class CurveSourceInterface(core_uobject.Interface):

    def GetCurveValue(self, CurveName: str, ReturnValue: float) -> float: ...
    def GetCurves(self, OutValues: unreal.WrappedArray[NamedCurveValue]): ...
    def GetBindingName(self, ReturnValue: str) -> str: ...


class CurveTable(unreal.UObject): ...


class CurveVector(CurveBase):
    FloatCurves: RichCurve
    def GetVectorValue(self, InTime: float, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...


class DataTable(unreal.UObject):
    RowStruct: core_uobject.ScriptStruct
    bStripFromClientBuilds: bool



class DataTableFunctionLibrary(BlueprintFunctionLibrary):

    def GetRowHandleSummaryString(self, RowHandle: DataTableRowHandle, ReturnValue: str) -> str: ...
    def GetDataTableRowNames(self, Table: DataTable, OutRowNames: unreal.WrappedArray[str]): ...
    def GetDataTableRowFromName(self, Table: DataTable, RowName: str, OutRow: TableRowBase, ReturnValue: bool) -> bool: ...
    def GetDataTableRowFromHandle(self, RowHandle: DataTableRowHandle, RequiredDataTableStruct: core_uobject.ScriptStruct, OutRow: TableRowBase, ReturnValue: bool) -> bool: ...
    def GetDataTableColumnAsString(self, DataTable: DataTable, PropertyName: str, ReturnValue: unreal.WrappedArray[str]) -> unreal.WrappedArray[str]: ...
    def EvaluateCurveTableRow(self, CurveTable: CurveTable, RowName: str, InXY: float, OutResult: int, OutXY: float, ContextString: str): ...


class DebugCameraController(PlayerController):
    bShowSelectedInfo: bool
    bIsFrozenRendering: bool
    DrawFrustum: DrawFrustumComponent
    SpeedScale: float
    InitialMaxSpeed: float
    InitialAccel: float
    InitialDecel: float
    def ToggleDisplay(self): ...
    def ShowDebugSelectedInfo(self): ...
    def SetPawnMovementSpeedScale(self, NewSpeedScale: float): ...
    def ReceiveOnDeactivate(self, RestoredPC: PlayerController): ...
    def ReceiveOnActorSelected(self, NewSelectedActor: Actor, SelectHitLocation: core_uobject.Vector, SelectHitNormal: core_uobject.Vector, Hit: HitResult): ...
    def ReceiveOnActivate(self, OriginalPC: PlayerController): ...
    def GetSelectedActor(self, ReturnValue: Actor) -> Actor: ...


class DebugCameraHUD(HUD): ...


class DebugDrawService(BlueprintFunctionLibrary): ...


class DecalActor(Actor):
    Decal: DecalComponent
    def SetDecalMaterial(self, NewDecalMaterial: MaterialInterface): ...
    def GetDecalMaterial(self, ReturnValue: MaterialInterface) -> MaterialInterface: ...
    def CreateDynamicMaterialInstance(self, ReturnValue: MaterialInstanceDynamic) -> MaterialInstanceDynamic: ...


class DecalComponent(PrimitiveComponent):
    DecalMaterial: MaterialInterface
    SortOrder: int
    FadeScreenSize: float
    FadeStartDelay: float
    FadeDuration: float
    bDestroyOwnerAfterFade: bool
    bUseSecondaryChannel: bool
    DecalSize: core_uobject.Vector
    def SetSortOrder(self, Value: int): ...
    def SetSecondaryChannel(self, bUseChannel: bool): ...
    def SetFadeScreenSize(self, NewFadeScreenSize: float): ...
    def SetFadeOut(self, StartDelay: float, Duration: float, DestroyOwnerAfterFade: bool): ...
    def SetDecalMaterial(self, NewDecalMaterial: MaterialInterface): ...
    def IsFadingOut(self, ReturnValue: bool) -> bool: ...
    def GetRemainingLifeSpan(self, ReturnValue: float) -> float: ...
    def GetFadeStartDelay(self, ReturnValue: float) -> float: ...
    def GetFadeDuration(self, ReturnValue: float) -> float: ...
    def GetDecalMaterial(self, ReturnValue: MaterialInterface) -> MaterialInterface: ...


class DefaultPawn(Pawn):
    BaseTurnRate: float
    BaseLookUpRate: float
    MovementComponent: PawnMovementComponent
    CollisionComponent: SphereComponent
    MeshComponent: StaticMeshComponent
    bAddDefaultMovementBindings: bool
    def TurnAtRate(self, Rate: float): ...
    def MoveUp_World(self, Val: float): ...
    def MoveRight(self, Val: float): ...
    def MoveForward(self, Val: float): ...
    def LookUpAtRate(self, Rate: float): ...


class PhysicsVolume(Volume):
    TerminalVelocity: float
    Priority: int
    FluidFriction: float
    bWaterVolume: bool
    bPhysicsOnContact: bool
    def OnActorLeftVolume(self, OverlappedComponent: PrimitiveComponent, OtherActor: Actor, OtherComp: PrimitiveComponent, OtherBodyIndex: int): ...
    def OnActorEnteredVolume(self, OverlappedComp: PrimitiveComponent, Other: Actor, OtherComp: PrimitiveComponent, OtherBodyIndex: int, bFromSweep: bool, OverlapInfo: HitResult): ...


class DefaultPhysicsVolume(PhysicsVolume): ...


class DemoNetConnection(NetConnection): ...


class DemoNetDriver(NetDriver):
    CheckpointSaveMaxMSPerFrame: float
    bIsLocalReplay: bool



class PendingNetGame(unreal.UObject):
    NetDriver: NetDriver
    DemoNetDriver: DemoNetDriver



class DemoPendingNetGame(PendingNetGame): ...


class DestructibleInterface(core_uobject.Interface): ...


class DestructibleMeshCustomBuilder(unreal.UObject): ...


class TextureLODSettings(unreal.UObject):
    TextureLODGroups: unreal.WrappedArray[TextureLODGroup]



class DeviceProfile(TextureLODSettings):
    DeviceType: str
    BaseProfileName: str
    Parent: unreal.UObject
    CVars: unreal.WrappedArray[str]



class DeviceProfileManager(unreal.UObject):
    Profiles: unreal.WrappedArray[unreal.UObject]



class SoundBase(unreal.UObject):
    SoundClassObject: SoundClass
    bDebug: bool
    bOverrideConcurrency: bool
    bOutputToBusOnly: bool
    bIgnoreFocus: bool
    bHasDelayNode: bool
    bHasConcatenatorNode: bool
    bHasVirtualizeWhenSilent: bool
    bBypassVolumeScaleForPriority: bool
    SoundConcurrencySettings: SoundConcurrency
    ConcurrencyOverrides: SoundConcurrencySettings
    Duration: float
    MaxDistance: float
    TotalSamples: float
    Priority: float
    AttenuationSettings: SoundAttenuation
    SoundSubmixObject: SoundSubmix
    SoundSubmixSends: unreal.WrappedArray[SoundSubmixSendInfo]
    SourceEffectChain: SoundEffectSourcePresetChain
    BusSends: unreal.WrappedArray[SoundSourceBusSendInfo]
    PreEffectBusSends: unreal.WrappedArray[SoundSourceBusSendInfo]



class DialogueSoundWaveProxy(SoundBase): ...


class DialogueVoice(unreal.UObject):
    Gender: int
    Plurality: int
    LocalizationGUID: core_uobject.Guid



class DialogueWave(unreal.UObject):
    bMature: bool
    bOverride_SubtitleOverride: bool
    SpokenText: str
    SubtitleOverride: str
    ContextMappings: unreal.WrappedArray[DialogueContextMapping]
    LocalizationGUID: core_uobject.Guid



class Light(Actor):
    LightComponent: LightComponent
    bEnabled: bool
    def ToggleEnabled(self): ...
    def SetLightFunctionScale(self, NewLightFunctionScale: core_uobject.Vector): ...
    def SetLightFunctionMaterial(self, NewLightFunctionMaterial: MaterialInterface): ...
    def SetLightFunctionFadeDistance(self, NewLightFunctionFadeDistance: float): ...
    def SetLightColor(self, NewLightColor: core_uobject.LinearColor): ...
    def SetEnabled(self, bSetEnabled: bool): ...
    def SetCastShadows(self, bNewValue: bool): ...
    def SetBrightness(self, NewBrightness: float): ...
    def SetAffectTranslucentLighting(self, bNewValue: bool): ...
    def OnRep_bEnabled(self): ...
    def IsEnabled(self, ReturnValue: bool) -> bool: ...
    def GetLightColor(self, ReturnValue: core_uobject.LinearColor) -> core_uobject.LinearColor: ...
    def GetBrightness(self, ReturnValue: float) -> float: ...


class DirectionalLight(Light): ...


class LightComponentBase(SceneComponent):
    LightGuid: core_uobject.Guid
    Brightness: float
    Intensity: float
    LightColor: core_uobject.Color
    bAffectsWorld: bool
    CastShadows: bool
    CastStaticShadows: bool
    CastDynamicShadows: bool
    bAffectTranslucentLighting: bool
    bTransmission: bool
    bCastVolumetricShadow: bool
    IndirectLightingIntensity: float
    VolumetricScatteringIntensity: float
    def SetCastVolumetricShadow(self, bNewValue: bool): ...
    def SetCastShadows(self, bNewValue: bool): ...
    def GetLightColor(self, ReturnValue: core_uobject.LinearColor) -> core_uobject.LinearColor: ...


class LightComponent(LightComponentBase):
    Temperature: float
    MaxDrawDistance: float
    MaxDistanceFadeRange: float
    bUseTemperature: bool
    ShadowMapChannel: int
    MinRoughness: float
    SpecularScale: float
    ShadowResolutionScale: float
    ShadowResolutionLightMass: str
    ShadowResolutionEditorEstimate: str
    ShadowBias: float
    ShadowSharpen: float
    ContactShadowLength: float
    ContactShadowLengthInWS: bool
    InverseSquaredFalloff: bool
    CastTranslucentShadows: bool
    bCastShadowsFromCinematicObjectsOnly: bool
    bAffectDynamicIndirectLighting: bool
    bForceCachedShadowsForMovablePrimitives: bool
    bIgnoredByFXCoordinator: bool
    LightingChannels: LightingChannels
    bExposureCompensation: bool
    LightFunctionMaterial: MaterialInterface
    LightFunctionScale: core_uobject.Vector
    IESTexture: TextureLightProfile
    bUseIESBrightness: bool
    IESBrightnessScale: float
    LightFunctionFadeDistance: float
    DisabledBrightness: float
    bEnableLightShaftBloom: bool
    BloomScale: float
    BloomThreshold: float
    BloomTint: core_uobject.Color
    bUseRayTracedDistanceFieldShadows: bool
    RayStartOffsetDepthScale: float
    bUseMaximumShadowMapResolution: bool
    MaximumShadowMapResolution: int
    def SetVolumetricScatteringIntensity(self, NewIntensity: float): ...
    def SetTransmission(self, bNewValue: bool): ...
    def SetTemperature(self, NewTemperature: float): ...
    def SetShadowBias(self, NewValue: float): ...
    def SetLightFunctionScale(self, NewLightFunctionScale: core_uobject.Vector): ...
    def SetLightFunctionMaterial(self, NewLightFunctionMaterial: MaterialInterface): ...
    def SetLightFunctionFadeDistance(self, NewLightFunctionFadeDistance: float): ...
    def SetLightFunctionDisabledBrightness(self, NewValue: float): ...
    def SetLightColor(self, NewLightColor: core_uobject.LinearColor, bSRGB: bool): ...
    def SetIntensity(self, NewIntensity: float): ...
    def SetIndirectLightingIntensity(self, NewIntensity: float): ...
    def SetIESTexture(self, NewValue: TextureLightProfile): ...
    def SetForceCachedShadowsForMovablePrimitives(self, bNewValue: bool): ...
    def SetEnableLightShaftBloom(self, bNewValue: bool): ...
    def SetBloomTint(self, NewValue: core_uobject.Color): ...
    def SetBloomThreshold(self, NewValue: float): ...
    def SetBloomScale(self, NewValue: float): ...
    def SetAffectTranslucentLighting(self, bNewValue: bool): ...
    def SetAffectDynamicIndirectLighting(self, bNewValue: bool): ...


class DirectionalLightComponent(LightComponent):
    bEnableLightShaftOcclusion: bool
    OcclusionMaskDarkness: float
    OcclusionDepthRange: float
    LightShaftOverrideDirection: core_uobject.Vector
    WholeSceneDynamicShadowRadius: float
    DynamicShadowDistanceMovableLight: float
    DynamicShadowDistanceStationaryLight: float
    DynamicShadowCascades: int
    CascadeDistributionExponent: float
    CascadeTransitionFraction: float
    ShadowDistanceFadeoutFraction: float
    bUseInsetShadowsForMovableObjects: bool
    FarShadowCascadeCount: int
    FarShadowDistance: float
    DistanceFieldShadowDistance: float
    LightSourceAngle: float
    LightSourceSoftAngle: float
    TraceDistance: float
    LightmassSettings: LightmassDirectionalLightSettings
    bCastModulatedShadows: bool
    ModulatedShadowColor: core_uobject.Color
    bUsedAsAtmosphereSunLight: bool
    def SetShadowDistanceFadeoutFraction(self, NewValue: float): ...
    def SetOcclusionMaskDarkness(self, NewValue: float): ...
    def SetLightShaftOverrideDirection(self, NewValue: core_uobject.Vector): ...
    def SetEnableLightShaftOcclusion(self, bNewValue: bool): ...
    def SetDynamicShadowDistanceStationaryLight(self, NewValue: float): ...
    def SetDynamicShadowDistanceMovableLight(self, NewValue: float): ...
    def SetDynamicShadowCascades(self, NewValue: int): ...
    def SetCascadeTransitionFraction(self, NewValue: float): ...
    def SetCascadeDistributionExponent(self, NewValue: float): ...


class Distribution(unreal.UObject): ...


class DistributionFloat(Distribution):
    bCanBeBaked: bool
    bBakedDataSuccesfully: bool



class DistributionFloatConstant(DistributionFloat):
    Constant: float



class DistributionFloatConstantCurve(DistributionFloat):
    ConstantCurve: core_uobject.InterpCurveFloat



class DistributionFloatParameterBase(DistributionFloatConstant):
    ParameterName: str
    MinInput: float
    MaxInput: float
    MinOutput: float
    MaxOutput: float
    ParamMode: int



class DistributionFloatParticleParameter(DistributionFloatParameterBase): ...


class DistributionFloatUniform(DistributionFloat):
    Min: float
    Max: float



class DistributionFloatUniformCurve(DistributionFloat):
    ConstantCurve: core_uobject.InterpCurveVector2D



class DistributionVector(Distribution):
    bCanBeBaked: bool
    bIsDirty: bool
    bBakedDataSuccesfully: bool



class DistributionVectorConstant(DistributionVector):
    Constant: core_uobject.Vector
    bLockAxes: bool
    LockedAxes: int



class DistributionVectorConstantCurve(DistributionVector):
    ConstantCurve: core_uobject.InterpCurveVector
    bLockAxes: bool
    LockedAxes: int



class DistributionVectorParameterBase(DistributionVectorConstant):
    ParameterName: str
    MinInput: core_uobject.Vector
    MaxInput: core_uobject.Vector
    MinOutput: core_uobject.Vector
    MaxOutput: core_uobject.Vector
    ParamModes: int



class DistributionVectorParticleParameter(DistributionVectorParameterBase): ...


class DistributionVectorUniform(DistributionVector):
    Max: core_uobject.Vector
    Min: core_uobject.Vector
    bLockAxes: bool
    LockedAxes: int
    MirrorFlags: int
    bUseExtremes: bool



class DistributionVectorUniformCurve(DistributionVector):
    ConstantCurve: core_uobject.InterpCurveTwoVectors
    bLockAxes1: bool
    bLockAxes2: bool
    LockedAxes: int
    MirrorFlags: int
    bUseExtremes: bool



class DocumentationActor(Actor): ...


class DPICustomScalingRule(unreal.UObject): ...


class DrawFrustumComponent(PrimitiveComponent):
    FrustumColor: core_uobject.Color
    FrustumAngle: float
    FrustumAspectRatio: float
    FrustumStartDist: float
    FrustumEndDist: float
    Texture: Texture



class DrawSphereComponent(SphereComponent): ...


class EdGraph(unreal.UObject):
    Schema: unreal.UClass
    Nodes: unreal.WrappedArray[EdGraphNode]
    bEditable: bool
    bAllowDeletion: bool
    bAllowRenaming: bool



class FollowingNodeInterface(core_uobject.Interface): ...


class EdGraphNode(unreal.UObject):
    DeprecatedPins: unreal.WrappedArray[EdGraphPin_Deprecated]
    NodePosX: int
    NodePosY: int
    NodeWidth: int
    NodeHeight: int
    AdvancedPinDisplay: int
    EnabledState: ENodeEnabledState
    bUserSetEnabledState: bool
    bIsNodeEnabled: bool
    bHasCompilerMessage: bool
    bCommentBubblePinned: bool
    bCommentBubbleVisible: bool
    bCommentBubbleMakeVisible: bool
    NodeComment: str
    ErrorType: int
    ErrorMsg: str
    NodeGuid: core_uobject.Guid
    bEnableAutoLogComment: bool



class EdGraphNode_Documentation(EdGraphNode):
    Link: str
    Excerpt: str



class EdGraphPin_Deprecated(unreal.UObject):
    PinName: str
    PinToolTip: str
    Direction: int
    PinType: EdGraphPinType
    DefaultValue: str
    AutogeneratedDefaultValue: str
    DefaultObject: unreal.UObject
    DefaultTextValue: str
    LinkedTo: unreal.WrappedArray[EdGraphPin_Deprecated]
    SubPins: unreal.WrappedArray[EdGraphPin_Deprecated]
    ParentPin: EdGraphPin_Deprecated
    ReferencePassThroughConnection: EdGraphPin_Deprecated



class EdGraphSchema(unreal.UObject): ...


class Emitter(Actor):
    ParticleSystemComponent: ParticleSystemComponent
    bDestroyOnSystemFinish: bool
    bPostUpdateTickGroup: bool
    bCurrentlyActive: bool
    def ToggleActive(self): ...
    def SetVectorParameter(self, ParameterName: str, Param: core_uobject.Vector): ...
    def SetTemplate(self, NewTemplate: ParticleSystem): ...
    def SetMaterialParameter(self, ParameterName: str, Param: MaterialInterface): ...
    def SetFloatParameter(self, ParameterName: str, Param: float): ...
    def SetColorParameter(self, ParameterName: str, Param: core_uobject.LinearColor): ...
    def SetActorParameter(self, ParameterName: str, Param: Actor): ...
    def OnRep_bCurrentlyActive(self): ...
    def OnParticleSystemFinished(self, FinishedComponent: ParticleSystemComponent): ...
    def IsActive(self, ReturnValue: bool) -> bool: ...
    def Deactivate(self): ...
    def Activate(self): ...


class EmitterCameraLensEffectBase(Emitter):
    PS_CameraEffect: ParticleSystem
    PS_CameraEffectNonExtremeContent: ParticleSystem
    BaseCamera: PlayerCameraManager
    RelativeTransform: core_uobject.Transform
    BaseFOV: float
    bAllowMultipleInstances: bool
    bResetWhenRetriggered: bool
    EmittersToTreatAsSame: unreal.WrappedArray[unreal.UClass]
    DistFromCamera: float



class EngineBaseTypes(unreal.UObject): ...


class EngineHandlerComponentFactory(packet_handler.HandlerComponentFactory): ...


class EngineMessage(LocalMessage):
    FailedPlaceMessage: str
    MaxedOutMessage: str
    EnteredMessage: str
    LeftMessage: str
    GlobalNameChange: str
    SpecEnteredMessage: str
    NewPlayerMessage: str
    NewSpecMessage: str



class EngineTypes(unreal.UObject): ...


class ExponentialHeightFog(Info):
    Component: ExponentialHeightFogComponent
    bEnabled: bool
    def OnRep_bEnabled(self): ...


class ExponentialHeightFogComponent(SceneComponent):
    FogDensity: float
    bCameraRelative: bool
    FogRelativeOffset: float
    FogInscatteringColor: core_uobject.LinearColor
    InscatteringColorCubemap: TextureCube
    InscatteringColorCubemapAngle: float
    InscatteringTextureTint: core_uobject.LinearColor
    FullyDirectionalInscatteringColorDistance: float
    NonDirectionalInscatteringColorDistance: float
    DirectionalInscatteringExponent: float
    DirectionalInscatteringStartDistance: float
    DirectionalInscatteringColor: core_uobject.LinearColor
    FogHeightFalloff: float
    FogMaxOpacity: float
    StartDistance: float
    FogCutoffDistance: float
    bEnableVolumetricFog: bool
    VolumetricFogScatteringDistribution: float
    VolumetricFogAlbedo: core_uobject.Color
    VolumetricFogEmissive: core_uobject.LinearColor
    VolumetricFogExtinctionScale: float
    VolumetricFogDistance: float
    VolumetricFogStaticLightingScatteringIntensity: float
    bOverrideLightColorsWithFogInscatteringColors: bool
    bShouldOverrideHeight: bool
    OverrideHeight: float
    def SetVolumetricFogScatteringDistribution(self, NewValue: float): ...
    def SetVolumetricFogExtinctionScale(self, NewValue: float): ...
    def SetVolumetricFogEmissive(self, NewValue: core_uobject.LinearColor): ...
    def SetVolumetricFogDistance(self, NewValue: float): ...
    def SetVolumetricFogAlbedo(self, NewValue: core_uobject.Color): ...
    def SetVolumetricFog(self, bNewValue: bool): ...
    def SetStartDistance(self, Value: float): ...
    def SetNonDirectionalInscatteringColorDistance(self, Value: float): ...
    def SetInscatteringTextureTint(self, Value: core_uobject.LinearColor): ...
    def SetInscatteringColorCubemapAngle(self, Value: float): ...
    def SetInscatteringColorCubemap(self, Value: TextureCube): ...
    def SetFullyDirectionalInscatteringColorDistance(self, Value: float): ...
    def SetFogMaxOpacity(self, Value: float): ...
    def SetFogInscatteringColor(self, Value: core_uobject.LinearColor): ...
    def SetFogHeightFalloff(self, Value: float): ...
    def SetFogDensity(self, Value: float): ...
    def SetFogCutoffDistance(self, Value: float): ...
    def SetDirectionalInscatteringStartDistance(self, Value: float): ...
    def SetDirectionalInscatteringExponent(self, Value: float): ...
    def SetDirectionalInscatteringColor(self, Value: core_uobject.LinearColor): ...


class Exporter(unreal.UObject):
    SupportedClass: unreal.UClass
    ExportRootScope: unreal.UObject
    FormatExtension: unreal.WrappedArray[str]
    FormatDescription: unreal.WrappedArray[str]
    PreferredFormatIndex: int
    TextIndent: int
    bText: bool
    bSelectedOnly: bool
    bForceFileOperations: bool
    ExportTask: AssetExportTask
    def RunAssetExportTasks(self, ExportTasks: unreal.WrappedArray[AssetExportTask], ReturnValue: bool) -> bool: ...
    def RunAssetExportTask(self, Task: AssetExportTask, ReturnValue: bool) -> bool: ...


class FloatingPawnMovement(PawnMovementComponent):
    MaxSpeed: GbxAttributeFloat
    Acceleration: float
    Deceleration: float
    TurningBoost: float
    bPositionCorrected: bool



class Font(unreal.UObject):
    FontCacheType: EFontCacheType
    Characters: unreal.WrappedArray[FontCharacter]
    Textures: unreal.WrappedArray[Texture2D]
    IsRemapped: int
    EmScale: float
    Ascent: float
    Descent: float
    Leading: float
    Kerning: int
    ImportOptions: FontImportOptionsData
    NumCharacters: int
    MaxCharHeight: unreal.WrappedArray[int]
    ScalingFactor: float
    LegacyFontSize: int
    LegacyFontName: str
    CompositeFont: slate_core.CompositeFont



class FontFace(unreal.UObject):
    SourceFilename: str
    Hinting: slate_core.EFontHinting
    LoadingPolicy: slate_core.EFontLoadingPolicy
    LayoutMethod: slate_core.EFontLayoutMethod



class FontImportOptions(unreal.UObject):
    Data: FontImportOptionsData



class ForceFeedbackAttenuation(unreal.UObject):
    Attenuation: ForceFeedbackAttenuationSettings



class ForceFeedbackComponent(SceneComponent):
    ForceFeedbackEffect: ForceFeedbackEffect
    bAutoDestroy: bool
    bStopWhenOwnerDestroyed: bool
    bLooping: bool
    bIgnoreTimeDilation: bool
    bOverrideAttenuation: bool
    IntensityMultiplier: float
    AttenuationSettings: ForceFeedbackAttenuation
    AttenuationOverrides: ForceFeedbackAttenuationSettings
    def Stop(self): ...
    def SetIntensityMultiplier(self, NewIntensityMultiplier: float): ...
    def SetForceFeedbackEffect(self, NewForceFeedbackEffect: ForceFeedbackEffect): ...
    def Play(self, StartTime: float): ...
    def BP_GetAttenuationSettingsToApply(self, OutAttenuationSettings: ForceFeedbackAttenuationSettings, ReturnValue: bool) -> bool: ...
    def AdjustAttenuation(self, InAttenuationSettings: ForceFeedbackAttenuationSettings): ...


class ForceFeedbackEffect(unreal.UObject):
    ChannelDetails: unreal.WrappedArray[ForceFeedbackChannelDetails]
    Duration: float



class GameNetworkManager(Info):
    AdjustedNetSpeed: int
    LastNetSpeedUpdateTime: float
    TotalNetBandwidth: int
    MinDynamicBandwidth: int
    MaxDynamicBandwidth: int
    bIsStandbyCheckingEnabled: bool
    bHasStandbyCheatTriggered: bool
    StandbyRxCheatTime: float
    StandbyTxCheatTime: float
    BadPingThreshold: int
    PercentMissingForRxStandby: float
    PercentMissingForTxStandby: float
    PercentForBadPing: float
    JoinInProgressStandbyWaitTime: float
    MoveRepSize: float
    MAXPOSITIONERRORSQUARED: float
    MAXNEARZEROVELOCITYSQUARED: float
    CLIENTADJUSTUPDATECOST: float
    MAXCLIENTUPDATEINTERVAL: float
    MaxMoveDeltaTime: float
    ClientNetSendMoveDeltaTime: float
    ClientNetSendMoveDeltaTimeThrottled: float
    ClientNetSendMoveDeltaTimeStationary: float
    ClientNetSendMoveThrottleAtNetSpeed: int
    ClientNetSendMoveThrottleOverPlayerCount: int
    ClientAuthorativePosition: bool
    ClientErrorUpdateRateLimit: float
    bMovementTimeDiscrepancyDetection: bool
    bMovementTimeDiscrepancyResolution: bool
    MovementTimeDiscrepancyMaxTimeMargin: float
    MovementTimeDiscrepancyMinTimeMargin: float
    MovementTimeDiscrepancyResolutionRate: float
    MovementTimeDiscrepancyDriftAllowance: float
    bMovementTimeDiscrepancyForceCorrectionsDuringResolution: bool
    bUseDistanceBasedRelevancy: bool



class GameObjectPoolManagerExt(unreal.UObject):

    def OnComponentUnregistered(self, Component: ActorComponent): ...


class GameplayStatics(BlueprintFunctionLibrary):

    def UnloadStreamLevel(self, WorldContextObject: unreal.UObject, LevelName: str, LatentInfo: LatentActionInfo, bShouldBlockOnUnload: bool): ...
    def SuggestProjectileVelocity_CustomArc(self, WorldContextObject: unreal.UObject, OutLaunchVelocity: core_uobject.Vector, StartPos: core_uobject.Vector, EndPos: core_uobject.Vector, OverrideGravityZ: float, ArcParam: float, ReturnValue: bool) -> bool: ...
    def SpawnSoundAttached(self, Sound: SoundBase, AttachToComponent: SceneComponent, AttachPointName: str, Location: core_uobject.Vector, Rotation: core_uobject.Rotator, LocationType: int, bStopWhenAttachedToDestroyed: bool, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, AttenuationSettings: SoundAttenuation, ConcurrencySettings: SoundConcurrency, bAutoDestroy: bool, ReturnValue: AudioComponent) -> AudioComponent: ...
    def SpawnSoundAtLocation(self, WorldContextObject: unreal.UObject, Sound: SoundBase, Location: core_uobject.Vector, Rotation: core_uobject.Rotator, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, AttenuationSettings: SoundAttenuation, ConcurrencySettings: SoundConcurrency, bAutoDestroy: bool, ReturnValue: AudioComponent) -> AudioComponent: ...
    def SpawnSound2D(self, WorldContextObject: unreal.UObject, Sound: SoundBase, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, ConcurrencySettings: SoundConcurrency, bPersistAcrossLevelTransition: bool, bAutoDestroy: bool, ReturnValue: AudioComponent) -> AudioComponent: ...
    def SpawnObject(self, ObjectClass: unreal.UClass, Outer: unreal.UObject, ReturnValue: unreal.UObject) -> unreal.UObject: ...
    def SpawnForceFeedbackAttached(self, ForceFeedbackEffect: ForceFeedbackEffect, AttachToComponent: SceneComponent, AttachPointName: str, Location: core_uobject.Vector, Rotation: core_uobject.Rotator, LocationType: int, bStopWhenAttachedToDestroyed: bool, bLooping: bool, IntensityMultiplier: float, StartTime: float, AttenuationSettings: ForceFeedbackAttenuation, bAutoDestroy: bool, ReturnValue: ForceFeedbackComponent) -> ForceFeedbackComponent: ...
    def SpawnForceFeedbackAtLocation(self, WorldContextObject: unreal.UObject, ForceFeedbackEffect: ForceFeedbackEffect, Location: core_uobject.Vector, Rotation: core_uobject.Rotator, bLooping: bool, IntensityMultiplier: float, StartTime: float, AttenuationSettings: ForceFeedbackAttenuation, bAutoDestroy: bool, ReturnValue: ForceFeedbackComponent) -> ForceFeedbackComponent: ...
    def SpawnEmitterAttached(self, EmitterTemplate: ParticleSystem, AttachToComponent: SceneComponent, AttachPointName: str, Location: core_uobject.Vector, Rotation: core_uobject.Rotator, Scale: core_uobject.Vector, LocationType: int, bAutoDestroy: bool, PoolingMethod: EPSCPoolMethod, bInheritViewFlags: bool, ParameterEvaluationContext: unreal.UObject, ReturnValue: ParticleSystemComponent) -> ParticleSystemComponent: ...
    def SpawnEmitterAtLocation(self, WorldContextObject: unreal.UObject, EmitterTemplate: ParticleSystem, Location: core_uobject.Vector, Rotation: core_uobject.Rotator, Scale: core_uobject.Vector, bAutoDestroy: bool, PoolingMethod: EPSCPoolMethod, ParameterEvaluationContext: unreal.UObject, ReturnValue: ParticleSystemComponent) -> ParticleSystemComponent: ...
    def SpawnDialogueAttached(self, Dialogue: DialogueWave, Context: DialogueContext, AttachToComponent: SceneComponent, AttachPointName: str, Location: core_uobject.Vector, Rotation: core_uobject.Rotator, LocationType: int, bStopWhenAttachedToDestroyed: bool, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, AttenuationSettings: SoundAttenuation, bAutoDestroy: bool, ReturnValue: AudioComponent) -> AudioComponent: ...
    def SpawnDialogueAtLocation(self, WorldContextObject: unreal.UObject, Dialogue: DialogueWave, Context: DialogueContext, Location: core_uobject.Vector, Rotation: core_uobject.Rotator, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, AttenuationSettings: SoundAttenuation, bAutoDestroy: bool, ReturnValue: AudioComponent) -> AudioComponent: ...
    def SpawnDialogue2D(self, WorldContextObject: unreal.UObject, Dialogue: DialogueWave, Context: DialogueContext, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, bAutoDestroy: bool, ReturnValue: AudioComponent) -> AudioComponent: ...
    def SpawnDecalAttached(self, DecalMaterial: MaterialInterface, DecalSize: core_uobject.Vector, AttachToComponent: SceneComponent, AttachPointName: str, Location: core_uobject.Vector, Rotation: core_uobject.Rotator, LocationType: int, LifeSpan: float, FadeDuration: float, FadeStartDelay: float, FadeScreenSize: float, ReturnValue: DecalComponent) -> DecalComponent: ...
    def SpawnDecalAtLocation(self, WorldContextObject: unreal.UObject, DecalMaterial: MaterialInterface, DecalSize: core_uobject.Vector, Location: core_uobject.Vector, Rotation: core_uobject.Rotator, LifeSpan: float, FadeDuration: float, FadeStartDelay: float, FadeScreenSize: float, ReturnValue: DecalComponent) -> DecalComponent: ...
    def SetWorldOriginLocation(self, WorldContextObject: unreal.UObject, NewLocation: core_uobject.IntVector): ...
    def SetSubtitlesEnabled(self, bEnabled: bool): ...
    def SetSoundMixClassOverride(self, WorldContextObject: unreal.UObject, InSoundMixModifier: SoundMix, InSoundClass: SoundClass, Volume: float, Pitch: float, FadeInTime: float, bApplyToChildren: bool): ...
    def SetPlayerControllerID(self, Player: PlayerController, ControllerId: int): ...
    def SetGlobalTimeDilation(self, WorldContextObject: unreal.UObject, TimeDilation: float): ...
    def SetGlobalPitchModulation(self, WorldContextObject: unreal.UObject, PitchModulation: float, TimeSec: float): ...
    def SetGlobalListenerFocusParameters(self, WorldContextObject: unreal.UObject, FocusAzimuthScale: float, NonFocusAzimuthScale: float, FocusDistanceScale: float, NonFocusDistanceScale: float, FocusVolumeScale: float, NonFocusVolumeScale: float, FocusPriorityScale: float, NonFocusPriorityScale: float): ...
    def SetGamePaused(self, WorldContextObject: unreal.UObject, bPaused: bool, ReturnValue: bool) -> bool: ...
    def SetBaseSoundMix(self, WorldContextObject: unreal.UObject, InSoundMix: SoundMix): ...
    def SaveGameToSlot(self, SaveGameObject: SaveGame, SlotName: str, UserIndex: int, ReturnValue: bool) -> bool: ...
    def RemovePlayer(self, Player: PlayerController, bDestroyPawn: bool): ...
    def RebaseZeroOriginOntoLocal(self, WorldContextObject: unreal.UObject, WorldLocation: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def RebaseLocalOriginOntoZero(self, WorldContextObject: unreal.UObject, WorldLocation: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def PushSoundMixModifier(self, WorldContextObject: unreal.UObject, InSoundMixModifier: SoundMix): ...
    def ProjectWorldToScreen(self, Player: PlayerController, WorldPosition: core_uobject.Vector, ScreenPosition: core_uobject.Vector2D, bPlayerViewportRelative: bool, bUseForgroundProjection: bool, ReturnValue: bool) -> bool: ...
    def PopSoundMixModifier(self, WorldContextObject: unreal.UObject, InSoundMixModifier: SoundMix): ...
    def PlayWorldCameraShake(self, WorldContextObject: unreal.UObject, Shake: unreal.UClass, Epicenter: core_uobject.Vector, InnerRadius: float, OuterRadius: float, Falloff: float, bOrientShakeTowardsEpicenter: bool): ...
    def PlaySoundAtLocation(self, WorldContextObject: unreal.UObject, Sound: SoundBase, Location: core_uobject.Vector, Rotation: core_uobject.Rotator, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, AttenuationSettings: SoundAttenuation, ConcurrencySettings: SoundConcurrency, OwningActor: Actor): ...
    def PlaySound2D(self, WorldContextObject: unreal.UObject, Sound: SoundBase, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, ConcurrencySettings: SoundConcurrency, OwningActor: Actor): ...
    def PlayDialogueAtLocation(self, WorldContextObject: unreal.UObject, Dialogue: DialogueWave, Context: DialogueContext, Location: core_uobject.Vector, Rotation: core_uobject.Rotator, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, AttenuationSettings: SoundAttenuation): ...
    def PlayDialogue2D(self, WorldContextObject: unreal.UObject, Dialogue: DialogueWave, Context: DialogueContext, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float): ...
    def ParseOption(self, Options: str, Key: str, ReturnValue: str) -> str: ...
    def OpenLevel(self, WorldContextObject: unreal.UObject, LevelName: str, bAbsolute: bool, Options: str): ...
    def MakeHitResult(self, bBlockingHit: bool, bInitialOverlap: bool, Time: float, Distance: float, Location: core_uobject.Vector, ImpactPoint: core_uobject.Vector, Normal: core_uobject.Vector, ImpactNormal: core_uobject.Vector, PhysMat: PhysicalMaterial, HitActor: Actor, HitComponent: PrimitiveComponent, HitBoneName: str, HitItem: int, FaceIndex: int, TraceStart: core_uobject.Vector, TraceEnd: core_uobject.Vector, ReturnValue: HitResult) -> HitResult: ...
    def LoadStreamLevel(self, WorldContextObject: unreal.UObject, LevelName: str, bMakeVisibleAfterLoad: bool, bShouldBlockOnLoad: bool, LatentInfo: LatentActionInfo): ...
    def LoadGameFromSlot(self, SlotName: str, UserIndex: int, ReturnValue: SaveGame) -> SaveGame: ...
    def IsGamePaused(self, WorldContextObject: unreal.UObject, ReturnValue: bool) -> bool: ...
    def HasOption(self, Options: str, InKey: str, ReturnValue: bool) -> bool: ...
    def HasLaunchOption(self, OptionToCheck: str, ReturnValue: bool) -> bool: ...
    def GrassOverlappingSphereCount(self, WorldContextObject: unreal.UObject, StaticMesh: StaticMesh, CenterPosition: core_uobject.Vector, Radius: float, ReturnValue: int) -> int: ...
    def GetWorldOriginLocation(self, WorldContextObject: unreal.UObject, ReturnValue: core_uobject.IntVector) -> core_uobject.IntVector: ...
    def GetWorldDeltaSeconds(self, WorldContextObject: unreal.UObject, ReturnValue: float) -> float: ...
    def GetUnpausedTimeSeconds(self, WorldContextObject: unreal.UObject, ReturnValue: float) -> float: ...
    def GetTimeSeconds(self, WorldContextObject: unreal.UObject, ReturnValue: float) -> float: ...
    def GetSurfaceType(self, Hit: HitResult, ReturnValue: int) -> int: ...
    def GetStreamingLevel(self, WorldContextObject: unreal.UObject, PackageName: str, ReturnValue: LevelStreaming) -> LevelStreaming: ...
    def GetRealTimeSeconds(self, WorldContextObject: unreal.UObject, ReturnValue: float) -> float: ...
    def GetPlayerPawn(self, WorldContextObject: unreal.UObject, PlayerIndex: int, ReturnValue: Pawn) -> Pawn: ...
    def GetPlayerControllerID(self, Player: PlayerController, ReturnValue: int) -> int: ...
    def GetPlayerController(self, WorldContextObject: unreal.UObject, PlayerIndex: int, ReturnValue: PlayerController) -> PlayerController: ...
    def GetPlayerCharacter(self, WorldContextObject: unreal.UObject, PlayerIndex: int, ReturnValue: Character) -> Character: ...
    def GetPlayerCameraManager(self, WorldContextObject: unreal.UObject, PlayerIndex: int, ReturnValue: PlayerCameraManager) -> PlayerCameraManager: ...
    def GetPlatformName(self, ReturnValue: str) -> str: ...
    def GetObjectClass(self, Object: unreal.UObject, ReturnValue: unreal.UClass) -> unreal.UClass: ...
    def GetKeyValue(self, Pair: str, Key: str, Value: str): ...
    def GetIntOption(self, Options: str, Key: str, DefaultValue: int, ReturnValue: int) -> int: ...
    def GetGlobalTimeDilation(self, WorldContextObject: unreal.UObject, ReturnValue: float) -> float: ...
    def GetGameState(self, WorldContextObject: unreal.UObject, ReturnValue: GameStateBase) -> GameStateBase: ...
    def GetGameMode(self, WorldContextObject: unreal.UObject, ReturnValue: GameModeBase) -> GameModeBase: ...
    def GetGameInstance(self, WorldContextObject: unreal.UObject, ReturnValue: GameInstance) -> GameInstance: ...
    def GetCurrentReverbEffect(self, WorldContextObject: unreal.UObject, ReturnValue: ReverbEffect) -> ReverbEffect: ...
    def GetCurrentLevelName(self, WorldContextObject: unreal.UObject, bRemovePrefixString: bool, ReturnValue: str) -> str: ...
    def GetAudioTimeSeconds(self, WorldContextObject: unreal.UObject, ReturnValue: float) -> float: ...
    def GetAllActorsWithTag(self, WorldContextObject: unreal.UObject, Tag: str, OutActors: unreal.WrappedArray[Actor]): ...
    def GetAllActorsWithInterface(self, WorldContextObject: unreal.UObject, Interface: unreal.UClass, OutActors: unreal.WrappedArray[Actor]): ...
    def GetAllActorsOfClass(self, WorldContextObject: unreal.UObject, ActorClass: unreal.UClass, OutActors: unreal.WrappedArray[Actor]): ...
    def GetActorArrayBounds(self, Actors: unreal.WrappedArray[Actor], bOnlyCollidingComponents: bool, Center: core_uobject.Vector, BoxExtent: core_uobject.Vector): ...
    def GetActorArrayAverageLocation(self, Actors: unreal.WrappedArray[Actor], ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetAccurateRealTime(self, WorldContextObject: unreal.UObject, Seconds: int, PartialSeconds: float): ...
    def FlushLevelStreaming(self, WorldContextObject: unreal.UObject): ...
    def FinishSpawningActor(self, Actor: Actor, SpawnTransform: core_uobject.Transform, ReturnValue: Actor) -> Actor: ...
    def FindCollisionUV(self, Hit: HitResult, UVChannel: int, UV: core_uobject.Vector2D, ReturnValue: bool) -> bool: ...
    def EnableLiveStreaming(self, Enable: bool): ...
    def DoesSaveGameExist(self, SlotName: str, UserIndex: int, ReturnValue: bool) -> bool: ...
    def DeprojectScreenToWorld(self, Player: PlayerController, ScreenPosition: core_uobject.Vector2D, WorldPosition: core_uobject.Vector, WorldDirection: core_uobject.Vector, bUseForgroundProjection: bool, bTruncateScreenPosition: bool, ReturnValue: bool) -> bool: ...
    def DeleteGameInSlot(self, SlotName: str, UserIndex: int, ReturnValue: bool) -> bool: ...
    def DeactivateReverbEffect(self, WorldContextObject: unreal.UObject, TagName: str): ...
    def CreateSound2D(self, WorldContextObject: unreal.UObject, Sound: SoundBase, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, ConcurrencySettings: SoundConcurrency, bPersistAcrossLevelTransition: bool, bAutoDestroy: bool, ReturnValue: AudioComponent) -> AudioComponent: ...
    def CreateSaveGameObjectFromBlueprint(self, SaveGameBlueprint: Blueprint, ReturnValue: SaveGame) -> SaveGame: ...
    def CreateSaveGameObject(self, SaveGameClass: unreal.UClass, ReturnValue: SaveGame) -> SaveGame: ...
    def CreatePlayer(self, WorldContextObject: unreal.UObject, ControllerId: int, bSpawnPawn: bool, ReturnValue: PlayerController) -> PlayerController: ...
    def ClearSoundMixModifiers(self, WorldContextObject: unreal.UObject): ...
    def ClearSoundMixClassOverride(self, WorldContextObject: unreal.UObject, InSoundMixModifier: SoundMix, InSoundClass: SoundClass, FadeOutTime: float): ...
    def CancelAsyncLoading(self): ...
    def BreakHitResult(self, Hit: HitResult, bBlockingHit: bool, bInitialOverlap: bool, Time: float, Distance: float, Location: core_uobject.Vector, ImpactPoint: core_uobject.Vector, Normal: core_uobject.Vector, ImpactNormal: core_uobject.Vector, PhysMat: PhysicalMaterial, HitActor: Actor, HitComponent: PrimitiveComponent, HitBoneName: str, HitItem: int, FaceIndex: int, TraceStart: core_uobject.Vector, TraceEnd: core_uobject.Vector): ...
    def BlueprintSuggestProjectileVelocity(self, WorldContextObject: unreal.UObject, TossVelocity: core_uobject.Vector, StartLocation: core_uobject.Vector, EndLocation: core_uobject.Vector, LaunchSpeed: float, OverrideGravityZ: float, TraceOption: int, CollisionRadius: float, bFavorHighArc: bool, bDrawDebug: bool, ReturnValue: bool) -> bool: ...
    def Blueprint_PredictProjectilePath_ByTraceChannel(self, WorldContextObject: unreal.UObject, OutHit: HitResult, OutPathPositions: unreal.WrappedArray[core_uobject.Vector], OutLastTraceDestination: core_uobject.Vector, StartPos: core_uobject.Vector, LaunchVelocity: core_uobject.Vector, bTracePath: bool, ProjectileRadius: float, TraceChannel: int, bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, DrawDebugTime: float, SimFrequency: float, MaxSimTime: float, OverrideGravityZ: float, ReturnValue: bool) -> bool: ...
    def Blueprint_PredictProjectilePath_ByObjectType(self, WorldContextObject: unreal.UObject, OutHit: HitResult, OutPathPositions: unreal.WrappedArray[core_uobject.Vector], OutLastTraceDestination: core_uobject.Vector, StartPos: core_uobject.Vector, LaunchVelocity: core_uobject.Vector, bTracePath: bool, ProjectileRadius: float, ObjectTypes: unreal.WrappedArray[int], bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, DrawDebugTime: float, SimFrequency: float, MaxSimTime: float, OverrideGravityZ: float, ReturnValue: bool) -> bool: ...
    def Blueprint_PredictProjectilePath_Advanced(self, WorldContextObject: unreal.UObject, PredictParams: PredictProjectilePathParams, PredictResult: PredictProjectilePathResult, ReturnValue: bool) -> bool: ...
    def BeginSpawningActorFromClass(self, WorldContextObject: unreal.UObject, ActorClass: unreal.UClass, SpawnTransform: core_uobject.Transform, bNoCollisionFail: bool, Owner: Actor, ReturnValue: Actor) -> Actor: ...
    def BeginSpawningActorFromBlueprint(self, WorldContextObject: unreal.UObject, Blueprint: Blueprint, SpawnTransform: core_uobject.Transform, bNoCollisionFail: bool, ReturnValue: Actor) -> Actor: ...
    def BeginDeferredActorSpawnFromClass(self, WorldContextObject: unreal.UObject, ActorClass: unreal.UClass, SpawnTransform: core_uobject.Transform, CollisionHandlingOverride: ESpawnActorCollisionHandlingMethod, Owner: Actor, ReturnValue: Actor) -> Actor: ...
    def AreSubtitlesEnabled(self, ReturnValue: bool) -> bool: ...
    def AreAnyListenersWithinRange(self, WorldContextObject: unreal.UObject, Location: core_uobject.Vector, MaximumRange: float, ReturnValue: bool) -> bool: ...
    def ApplyRadialDamageWithFalloff(self, WorldContextObject: unreal.UObject, BaseDamage: float, MinimumDamage: float, Origin: core_uobject.Vector, DamageInnerRadius: float, DamageOuterRadius: float, DamageFalloff: float, DamageTypeClass: unreal.UClass, IgnoreActors: unreal.WrappedArray[Actor], DamageCauser: Actor, InstigatedByController: Controller, DamagePreventionChannel: int, ReturnValue: bool) -> bool: ...
    def ApplyRadialDamage(self, WorldContextObject: unreal.UObject, BaseDamage: float, Origin: core_uobject.Vector, DamageRadius: float, DamageTypeClass: unreal.UClass, IgnoreActors: unreal.WrappedArray[Actor], DamageCauser: Actor, InstigatedByController: Controller, bDoFullDamage: bool, DamagePreventionChannel: int, ReturnValue: bool) -> bool: ...
    def ApplyPointDamage(self, DamagedActor: Actor, BaseDamage: float, HitFromDirection: core_uobject.Vector, HitInfo: HitResult, EventInstigator: Controller, DamageCauser: Actor, DamageTypeClass: unreal.UClass, ReturnValue: float) -> float: ...
    def ApplyDamage(self, DamagedActor: Actor, BaseDamage: float, EventInstigator: Controller, DamageCauser: Actor, DamageTypeClass: unreal.UClass, ReturnValue: float) -> float: ...
    def ActivateReverbEffect(self, WorldContextObject: unreal.UObject, ReverbEffect: ReverbEffect, TagName: str, Priority: float, Volume: float, FadeTime: float): ...


class GbxActionAnimInstance(AnimInstance): ...


class GbxAnimManagerSettings(unreal.UObject):
    RenderedWeight: float
    ScreenSizeWeight: float
    MissedFrameWeight: float
    DefaultData: GbxAnimManagerData



class GbxAnimSet(DataAsset):
    GenericName: str



class GbxAnimBlueprintLibrary(BlueprintFunctionLibrary):

    def EnableAnimDebugChannel(self, Channel: EAnimDebugChannel): ...
    def DisableAnimDebugChannel(self, Channel: EAnimDebugChannel): ...


class GbxBaseMediaManager(unreal.UObject): ...


class GbxBlueprintActionInterface(core_uobject.Interface): ...


class GbxBoneSet(DataAsset):
    Guid: core_uobject.Guid
    BoneList: unreal.WrappedArray[GbxBoneSetEntry]
    CurveOverrides: unreal.WrappedArray[CurveWeightOverride]
    EnterTransitionBlendType: EBoneSetTransitionBlendType
    ExitTransitionBlendType: EBoneSetTransitionBlendType
    ActionBlendSpeed: float
    bOverrideActionBlendSpeed: bool
    BoneSetBlendSpeed: float
    bOverrideBoneSetBlendSpeed: bool



class GbxColorRemapLUT(unreal.UObject):
    LUTSource: int
    FlattenedLUT: Texture2D
    PostProcessSettings: PostProcessSettings



class GbxColorRemapLUTSet(unreal.UObject): ...


class GbxConvexComponent(ShapeComponent):
    Vertices: unreal.WrappedArray[core_uobject.Vector]



class GbxExternalTexture(Texture): ...


class GbxLagCompensationManager(unreal.UObject):
    bEnabled: bool
    FrameHistoryTime: float
    SampleRate: float
    RewindTimeBias: float
    def OnActorEndPlay(self, Actor: Actor, EndPlayReason: int): ...


class GbxMeshSettings(DeveloperSettings):
    bEnableAutoLightMapResolution: bool
    bEnableAutoLightMapResOnPostLoad: bool
    bEnableAutoLightMapResOnPreSave: bool
    AutoLightMapResNonUniform: unreal.WrappedArray[AutoLightMapResEntry]
    AutoLightMapResUniform: unreal.WrappedArray[AutoLightMapResEntry]



class GbxOrientedBoxComponent(SceneComponent):
    InnerBoxFactor: core_uobject.Vector
    OuterBoxExtent: core_uobject.Vector
    def SetOuterBoxExtent(self, InBoxExtent: core_uobject.Vector): ...
    def SetInnerBoxFactor(self, InBoxFactor: core_uobject.Vector): ...
    def GetOuterUnscaledBoxExtent(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetOuterScaledBoxExtent(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetInnerBoxFactor(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...


class GbxRetargetAsset(DataAsset):
    Skeleton: Skeleton
    RefPose: ReferencePose
    BoneTree: unreal.WrappedArray[BoneNode]



class GbxSkyActor(Actor):
    GbxSkyComponent: GbxSkyComponent
    DirectionalLightComponent: DirectionalLightComponent
    bAutoSetLight: bool
    TransientSkyDefinition: GbxSkyDefinition



class GbxSkyComponent(PrimitiveComponent):
    GbxSkyDefinition: GbxSkyDefinition
    TimeScale: float
    AbsoluteTime: float
    bCompositeToSkyEnvMap: bool
    bUseAlphaForSkyEnvMapComp: bool
    SkyDomeStaticMesh: StaticMesh
    BaseMaterial: MaterialInterface
    CloudDensityTexture: Texture
    NoiseTexture: Texture
    CurlNoiseTexture: Texture
    WeatherTexture: Texture
    CirrusTexture: Texture
    TempTextureA: Texture
    TempTextureB: Texture



class GbxSkyDefinition(unreal.UObject):
    CloudHeightKM: float
    CloudThicknessKM: float
    FogDistanceFalloffKM: float
    HorizonDistanceKM: float
    CirrusDensity: float
    CirrusHeightKM: float
    CirrusScaleKM: float
    CirrusCloudColor: core_uobject.LinearColor
    CirrusWindDirectionOverride: core_uobject.Vector4
    CirrusWindSpeedOverride: float
    Coverage: float
    Density: float
    HighFreqNoiseScaleKM: float
    NoiseScaleKM: float
    HighFreqNoiseBreakup: float
    LowFreqNoiseBreakup: float
    CurlNoiseStrength: float
    CurlNoiseScaleKM: float
    Shear: float
    WeatherMapScaleKM: float
    WindDirectionOverride: core_uobject.Vector4
    WindSpeedOverride: float
    SunLightColorOverride: core_uobject.LinearColor
    SunLightColorOverrideWeight: float
    AmbientColor: core_uobject.LinearColor
    LightExtinctionColor: core_uobject.LinearColor
    HGScatterringConstant: float
    ShadowDensity: float
    ShadowStepSize: float
    ConeSizeMultiplier: float
    PowderSugarBias: float
    SunIntensity: float
    SkyEnvironmentWeight: float
    SkyDomeRadiusKM: float
    ZKillThreshold: float
    TempFloatsA: core_uobject.Vector4
    TempFloatsB: core_uobject.Vector4
    TempIntsA: core_uobject.IntVector
    TempIntsB: core_uobject.IntVector



class GbxSpawnActorAsyncManager(unreal.UObject):
    Requests: unreal.WrappedArray[GbxSpawnActorAsyncRequestEntry]
    def SpawnActorAsync(self, WorldContext: unreal.UObject, Request: GbxSpawnActorAsyncRequest, ReturnValue: int) -> int: ...
    def CancelSpawnActorAsyncRequest(self, WorldContext: unreal.UObject, RequestID: int): ...
    def CacheExposeOnSpawnValue(self, Cache: GbxExposeOnSpawnValueCache, Property: core_uobject.Property, Value: int): ...


class GbxTraceAsyncLibrary(BlueprintFunctionLibrary):

    def TraceAsync(self, WorldContext: unreal.UObject, Request: GbxTraceAsyncRequest): ...


class GbxViewFilterManager(DeveloperSettings):
    CustomViewFlags: unreal.WrappedArray[GbxViewFlagSettings]



class GbxZoneMapFODSaveGameData(unreal.UObject): ...


class SpotLight(Light):
    SpotLightComponent: SpotLightComponent
    def SetOuterConeAngle(self, NewOuterConeAngle: float): ...
    def SetInnerConeAngle(self, NewInnerConeAngle: float): ...


class GeneratedMeshAreaLight(SpotLight): ...


class GestaltData(DataAsset):
    GestaltMesh: SkeletalMesh
    GestaltInfos: unreal.WrappedArray[GestaltInfo]
    GestaltPartBounds: unreal.WrappedArray[GestaltPartBoundsEntry]
    DefaultPartList: unreal.WrappedArray[str]
    CachedSocketMappings: unreal.WrappedArray[GestaltSocketMapping]
    def EnumeratePartNames(self, OutPartNames: unreal.WrappedArray[str]): ...


class HapticFeedbackEffect_Base(unreal.UObject): ...


class HapticFeedbackEffect_Buffer(HapticFeedbackEffect_Base):
    Amplitudes: unreal.WrappedArray[int]
    SampleRate: int



class HapticFeedbackEffect_Curve(HapticFeedbackEffect_Base):
    HapticDetails: HapticFeedbackDetails_Curve



class HapticFeedbackEffect_SoundWave(HapticFeedbackEffect_Base):
    SoundWave: SoundWave



class HavokNavLayerBase(unreal.UObject): ...


class HLODProxy(unreal.UObject):
    ProxyMeshes: unreal.WrappedArray[HLODProxyMesh]



class AmbisonicsSubmixSettingsBase(unreal.UObject): ...


class SpatializationPluginSourceSettingsBase(unreal.UObject): ...


class OcclusionPluginSourceSettingsBase(unreal.UObject): ...


class ReverbPluginSourceSettingsBase(unreal.UObject): ...


class HavokNavSeed(core_uobject.Interface): ...


class ImportanceSamplingLibrary(BlueprintFunctionLibrary):

    def RandomSobolFloat(self, Index: int, Dimension: int, Seed: float, ReturnValue: float) -> float: ...
    def RandomSobolCell3D(self, Index: int, NumCells: int, Cell: core_uobject.Vector, Seed: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def RandomSobolCell2D(self, Index: int, NumCells: int, Cell: core_uobject.Vector2D, Seed: core_uobject.Vector2D, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def NextSobolFloat(self, Index: int, Dimension: int, PreviousValue: float, ReturnValue: float) -> float: ...
    def NextSobolCell3D(self, Index: int, NumCells: int, PreviousValue: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def NextSobolCell2D(self, Index: int, NumCells: int, PreviousValue: core_uobject.Vector2D, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def MakeImportanceTexture(self, Texture: Texture2D, WeightingFunc: int, ReturnValue: ImportanceTexture) -> ImportanceTexture: ...
    def ImportanceSample(self, Texture: ImportanceTexture, Rand: core_uobject.Vector2D, Samples: int, Intensity: float, SamplePosition: core_uobject.Vector2D, SampleColor: core_uobject.LinearColor, SampleIntensity: float, SampleSize: float): ...
    def BreakImportanceTexture(self, ImportanceTexture: ImportanceTexture, Texture: Texture2D, WeightingFunc: int): ...


class ImportantToggleSettingInterface(core_uobject.Interface): ...


class InGameAdManager(PlatformInterfaceBase):
    bShouldPauseWhileAdOpen: bool



class InheritableComponentHandler(unreal.UObject):
    Records: unreal.WrappedArray[ComponentOverrideRecord]
    UnnecessaryComponents: unreal.WrappedArray[ActorComponent]



class InputDelegateBinding(DynamicBlueprintBinding): ...


class InputActionDelegateBinding(InputDelegateBinding):
    InputActionDelegateBindings: unreal.WrappedArray[BlueprintInputActionDelegateBinding]



class InputAxisDelegateBinding(InputDelegateBinding):
    InputAxisDelegateBindings: unreal.WrappedArray[BlueprintInputAxisDelegateBinding]



class InputAxisKeyDelegateBinding(InputDelegateBinding):
    InputAxisKeyDelegateBindings: unreal.WrappedArray[BlueprintInputAxisKeyDelegateBinding]



class InputKeyDelegateBinding(InputDelegateBinding):
    InputKeyDelegateBindings: unreal.WrappedArray[BlueprintInputKeyDelegateBinding]



class InputSettings(unreal.UObject):
    AxisConfig: unreal.WrappedArray[InputAxisConfigEntry]
    bAltEnterTogglesFullscreen: bool
    bF11TogglesFullscreen: bool
    bUseMouseForTouch: bool
    bEnableMouseSmoothing: bool
    bEnableFOVScaling: bool
    bCaptureMouseOnLaunch: bool
    bDefaultViewportMouseLock: bool
    bAlwaysShowTouchInterface: bool
    bShowConsoleOnFourFingerTap: bool
    bEnableGestureRecognizer: bool
    bUseAutocorrect: bool
    ExcludedAutocorrectOS: unreal.WrappedArray[str]
    ExcludedAutocorrectCultures: unreal.WrappedArray[str]
    ExcludedAutocorrectDeviceModels: unreal.WrappedArray[str]
    DefaultViewportMouseCaptureMode: EMouseCaptureMode
    DefaultViewportMouseLockMode: EMouseLockMode
    FOVScale: float
    DoubleClickTime: float
    ActionMappings: unreal.WrappedArray[InputActionKeyMapping]
    AxisMappings: unreal.WrappedArray[InputAxisKeyMapping]
    DefaultTouchInterface: core_uobject.SoftObjectPath
    ConsoleKey: input_core.Key
    ConsoleKeys: unreal.WrappedArray[input_core.Key]
    def SaveKeyMappings(self): ...
    def RemoveAxisMapping(self, KeyMapping: InputAxisKeyMapping, bForceRebuildKeymaps: bool): ...
    def RemoveActionMapping(self, KeyMapping: InputActionKeyMapping, bForceRebuildKeymaps: bool): ...
    def GetInputSettings(self, ReturnValue: InputSettings) -> InputSettings: ...
    def GetAxisNames(self, AxisNames: unreal.WrappedArray[str]): ...
    def GetAxisMappingByName(self, InAxisName: str, OutMappings: unreal.WrappedArray[InputAxisKeyMapping]): ...
    def GetActionNames(self, ActionNames: unreal.WrappedArray[str]): ...
    def GetActionMappingByName(self, InActionName: str, OutMappings: unreal.WrappedArray[InputActionKeyMapping]): ...
    def ForceRebuildKeymaps(self): ...
    def AddAxisMapping(self, KeyMapping: InputAxisKeyMapping, bForceRebuildKeymaps: bool): ...
    def AddActionMapping(self, KeyMapping: InputActionKeyMapping, bForceRebuildKeymaps: bool): ...


class InputTouchDelegateBinding(InputDelegateBinding):
    InputTouchDelegateBindings: unreal.WrappedArray[BlueprintInputTouchDelegateBinding]



class InputVectorAxisDelegateBinding(InputAxisKeyDelegateBinding): ...


class Interface_AssetUserData(core_uobject.Interface): ...


class Interface_CollisionDataProvider(core_uobject.Interface): ...


class Interface_PostProcessVolume(core_uobject.Interface): ...


class Interface_PreviewMeshProvider(core_uobject.Interface): ...


class InterpCurveEdSetup(unreal.UObject):
    Tabs: unreal.WrappedArray[CurveEdTab]
    ActiveTab: int



class InterpData(unreal.UObject):
    InterpLength: float
    PathBuildTime: float
    InterpGroups: unreal.WrappedArray[InterpGroup]
    CurveEdSetup: InterpCurveEdSetup
    EdSectionStart: float
    EdSectionEnd: float
    bShouldBakeAndPrune: bool
    CachedDirectorGroup: InterpGroupDirector
    AllEventNames: unreal.WrappedArray[str]



class InterpFilter(unreal.UObject):
    Caption: str



class InterpFilter_Classes(InterpFilter): ...


class InterpFilter_Custom(InterpFilter): ...


class InterpGroup(unreal.UObject):
    InterpTracks: unreal.WrappedArray[InterpTrack]
    GroupName: str
    GroupColor: core_uobject.Color
    bCollapsed: bool
    bVisible: bool
    bIsFolder: bool
    bIsParented: bool
    bIsSelected: bool



class InterpGroupCamera(InterpGroup):
    CameraAnimInst: CameraAnim
    CompressTolerance: float



class InterpGroupDirector(InterpGroup): ...


class InterpGroupInst(unreal.UObject):
    Group: InterpGroup
    GroupActor: Actor
    TrackInst: unreal.WrappedArray[InterpTrackInst]



class InterpGroupInstCamera(InterpGroupInst): ...


class InterpGroupInstDirector(InterpGroupInst): ...


class InterpToMovementComponent(MovementComponent):
    Duration: float
    bPauseOnImpact: bool
    BehaviourType: EInterpToBehaviourType
    bIgnoreCollisionWhenMoving: bool
    bForceSubStepping: bool
    MaxSimulationTimeStep: float
    MaxSimulationIterations: int
    ControlPoints: unreal.WrappedArray[InterpControlPoint]
    def StopSimulating(self, HitResult: HitResult): ...
    def RestartMovement(self, InitialDirection: float): ...
    def OnInterpToWaitEndDelegate__DelegateSignature(self, ImpactResult: HitResult, Time: float): ...
    def OnInterpToWaitBeginDelegate__DelegateSignature(self, ImpactResult: HitResult, Time: float): ...
    def OnInterpToStopDelegate__DelegateSignature(self, ImpactResult: HitResult, Time: float): ...
    def OnInterpToReverseDelegate__DelegateSignature(self, ImpactResult: HitResult, Time: float): ...
    def OnInterpToResetDelegate__DelegateSignature(self, ImpactResult: HitResult, Time: float): ...
    def FinaliseControlPoints(self): ...


class InterpTrackAnimControl(InterpTrackFloatBase):
    SlotName: str
    AnimSeqs: unreal.WrappedArray[AnimControlTrackKey]
    bSkipAnimNotifiers: bool



class InterpTrackAudioMaster(InterpTrackVectorBase): ...


class InterpTrackBoolProp(InterpTrack):
    BoolTrack: unreal.WrappedArray[BoolTrackKey]
    PropertyName: str



class InterpTrackColorProp(InterpTrackVectorBase):
    PropertyName: str



class InterpTrackColorScale(InterpTrackVectorBase): ...


class InterpTrackDirector(InterpTrack):
    CutTrack: unreal.WrappedArray[DirectorTrackCut]
    bSimulateCameraCutsOnClients: bool



class InterpTrackEvent(InterpTrack):
    EventTrack: unreal.WrappedArray[EventTrackKey]
    bFireEventsWhenForwards: bool
    bFireEventsWhenBackwards: bool
    bFireEventsWhenJumpingForwards: bool
    bUseCustomEventName: bool



class InterpTrackFade(InterpTrackFloatBase):
    bPersistFade: bool
    bFadeAudio: bool
    FadeColor: core_uobject.LinearColor



class InterpTrackFloatAnimBPParam(InterpTrackFloatBase):
    AnimBlueprintClass: AnimBlueprintGeneratedClass
    AnimClass: unreal.UClass
    ParamName: str



class InterpTrackFloatMaterialParam(InterpTrackFloatBase):
    TargetMaterials: unreal.WrappedArray[MaterialInterface]
    ParamName: str



class InterpTrackFloatParticleParam(InterpTrackFloatBase):
    ParamName: str



class InterpTrackFloatProp(InterpTrackFloatBase):
    PropertyName: str



class InterpTrackInstAnimControl(InterpTrackInst):
    LastUpdatePosition: float



class InterpTrackInstAudioMaster(InterpTrackInst): ...


class InterpTrackInstProperty(InterpTrackInst):
    InterpProperty: core_uobject.Property
    PropertyOuterObjectInst: unreal.UObject



class InterpTrackInstBoolProp(InterpTrackInstProperty):
    BoolProperty: core_uobject.BoolProperty
    ResetBool: bool



class InterpTrackInstColorProp(InterpTrackInstProperty):
    ResetColor: core_uobject.Color



class InterpTrackInstColorScale(InterpTrackInst): ...


class InterpTrackInstDirector(InterpTrackInst):
    OldViewTarget: Actor



class InterpTrackInstEvent(InterpTrackInst):
    LastUpdatePosition: float



class InterpTrackInstFade(InterpTrackInst): ...


class InterpTrackInstFloatAnimBPParam(InterpTrackInst):
    AnimScriptInstance: AnimInstance
    ResetFloat: float



class InterpTrackInstFloatMaterialParam(InterpTrackInst):
    MaterialInstances: unreal.WrappedArray[MaterialInstanceDynamic]
    ResetFloats: unreal.WrappedArray[float]
    PrimitiveMaterialRefs: unreal.WrappedArray[PrimitiveMaterialRef]
    InstancedTrack: InterpTrackFloatMaterialParam



class InterpTrackInstFloatParticleParam(InterpTrackInst):
    ResetFloat: float



class InterpTrackInstFloatProp(InterpTrackInstProperty):
    ResetFloat: float



class InterpTrackInstLinearColorProp(InterpTrackInstProperty):
    ResetColor: core_uobject.LinearColor



class InterpTrackInstMove(InterpTrackInst):
    ResetLocation: core_uobject.Vector
    ResetRotation: core_uobject.Rotator



class InterpTrackInstParticleReplay(InterpTrackInst):
    LastUpdatePosition: float



class InterpTrackInstSlomo(InterpTrackInst):
    OldTimeDilation: float



class InterpTrackInstSound(InterpTrackInst):
    LastUpdatePosition: float
    PlayAudioComp: AudioComponent



class InterpTrackInstToggle(InterpTrackInst):
    Action: int
    LastUpdatePosition: float
    bSavedActiveState: bool



class InterpTrackInstVectorMaterialParam(InterpTrackInst):
    MaterialInstances: unreal.WrappedArray[MaterialInstanceDynamic]
    ResetVectors: unreal.WrappedArray[core_uobject.Vector]
    PrimitiveMaterialRefs: unreal.WrappedArray[PrimitiveMaterialRef]
    InstancedTrack: InterpTrackVectorMaterialParam



class InterpTrackInstVectorProp(InterpTrackInstProperty):
    ResetVector: core_uobject.Vector



class InterpTrackInstVisibility(InterpTrackInst):
    Action: int
    LastUpdatePosition: float



class InterpTrackLinearColorBase(InterpTrack):
    LinearColorTrack: core_uobject.InterpCurveLinearColor
    CurveTension: float



class InterpTrackLinearColorProp(InterpTrackLinearColorBase):
    PropertyName: str



class InterpTrackMove(InterpTrack):
    PosTrack: core_uobject.InterpCurveVector
    EulerTrack: core_uobject.InterpCurveVector
    LookupTrack: InterpLookupTrack
    LookAtGroupName: str
    LinCurveTension: float
    AngCurveTension: float
    bUseQuatInterpolation: bool
    bShowArrowAtKeys: bool
    bDisableMovement: bool
    bShowTranslationOnCurveEd: bool
    bShowRotationOnCurveEd: bool
    bHide3DTrack: bool
    RotMode: int



class InterpTrackMoveAxis(InterpTrackFloatBase):
    MoveAxis: int
    LookupTrack: InterpLookupTrack



class InterpTrackParticleReplay(InterpTrack):
    TrackKeys: unreal.WrappedArray[ParticleReplayTrackKey]



class InterpTrackSlomo(InterpTrackFloatBase): ...


class InterpTrackSound(InterpTrackVectorBase):
    Sounds: unreal.WrappedArray[SoundTrackKey]
    bPlayOnReverse: bool
    bContinueSoundOnMatineeEnd: bool
    bSuppressSubtitles: bool
    bTreatAsDialogue: bool
    bAttach: bool



class InterpTrackToggle(InterpTrack):
    ToggleTrack: unreal.WrappedArray[ToggleTrackKey]
    bActivateSystemEachUpdate: bool
    bActivateWithJustAttachedFlag: bool
    bFireEventsWhenForwards: bool
    bFireEventsWhenBackwards: bool
    bFireEventsWhenJumpingForwards: bool



class InterpTrackVectorMaterialParam(InterpTrackVectorBase):
    TargetMaterials: unreal.WrappedArray[MaterialInterface]
    ParamName: str



class InterpTrackVectorProp(InterpTrackVectorBase):
    PropertyName: str



class InterpTrackVisibility(InterpTrack):
    VisibilityTrack: unreal.WrappedArray[VisibilityTrackKey]
    bFireEventsWhenForwards: bool
    bFireEventsWhenBackwards: bool
    bFireEventsWhenJumpingForwards: bool



class IntSerialization(unreal.UObject):
    SignedInt8Variable: int
    SignedInt16Variable: int
    SignedInt64Variable: int
    UnsignedInt8Variable: int
    SignedInt32Variable: int



class KillZVolume(PhysicsVolume): ...


class KismetArrayLibrary(BlueprintFunctionLibrary):

    def SetArrayPropertyByName(self, Object: unreal.UObject, PropertyName: str, Value: unreal.WrappedArray[int]): ...
    def FilterArray(self, TargetArray: unreal.WrappedArray[Actor], FilterClass: unreal.UClass, FilteredArray: unreal.WrappedArray[Actor]): ...
    def Array_Swap(self, TargetArray: unreal.WrappedArray[int], FirstIndex: int, SecondIndex: int): ...
    def Array_Shuffle(self, TargetArray: unreal.WrappedArray[int]): ...
    def Array_Set(self, TargetArray: unreal.WrappedArray[int], Index: int, Item: int, bSizeToFit: bool): ...
    def Array_Resize(self, TargetArray: unreal.WrappedArray[int], Size: int): ...
    def Array_RemoveItem(self, TargetArray: unreal.WrappedArray[int], Item: int, ReturnValue: bool) -> bool: ...
    def Array_Remove(self, TargetArray: unreal.WrappedArray[int], IndexToRemove: int): ...
    def Array_Length(self, TargetArray: unreal.WrappedArray[int], ReturnValue: int) -> int: ...
    def Array_LastIndex(self, TargetArray: unreal.WrappedArray[int], ReturnValue: int) -> int: ...
    def Array_IsValidIndex(self, TargetArray: unreal.WrappedArray[int], IndexToTest: int, ReturnValue: bool) -> bool: ...
    def Array_Insert(self, TargetArray: unreal.WrappedArray[int], NewItem: int, Index: int): ...
    def Array_Get(self, TargetArray: unreal.WrappedArray[int], Index: int, Item: int): ...
    def Array_Find(self, TargetArray: unreal.WrappedArray[int], ItemToFind: int, ReturnValue: int) -> int: ...
    def Array_Contains(self, TargetArray: unreal.WrappedArray[int], ItemToFind: int, ReturnValue: bool) -> bool: ...
    def Array_Clear(self, TargetArray: unreal.WrappedArray[int]): ...
    def Array_Append(self, TargetArray: unreal.WrappedArray[int], SourceArray: unreal.WrappedArray[int]): ...
    def Array_AddUnique(self, TargetArray: unreal.WrappedArray[int], NewItem: int, ReturnValue: int) -> int: ...
    def Array_Add(self, TargetArray: unreal.WrappedArray[int], NewItem: int, ReturnValue: int) -> int: ...


class KismetGuidLibrary(BlueprintFunctionLibrary):

    def Parse_StringToGuid(self, GuidString: str, OutGuid: core_uobject.Guid, Success: bool): ...
    def NotEqual_GuidGuid(self, A: core_uobject.Guid, B: core_uobject.Guid, ReturnValue: bool) -> bool: ...
    def NewGuid(self, ReturnValue: core_uobject.Guid) -> core_uobject.Guid: ...
    def IsValid_Guid(self, InGuid: core_uobject.Guid, ReturnValue: bool) -> bool: ...
    def Invalidate_Guid(self, InGuid: core_uobject.Guid): ...
    def EqualEqual_GuidGuid(self, A: core_uobject.Guid, B: core_uobject.Guid, ReturnValue: bool) -> bool: ...
    def Conv_GuidToString(self, InGuid: core_uobject.Guid, ReturnValue: str) -> str: ...


class KismetInputLibrary(BlueprintFunctionLibrary):

    def PointerEvent_IsTouchEvent(self, Input: slate_core.PointerEvent, ReturnValue: bool) -> bool: ...
    def PointerEvent_IsMouseButtonDown(self, Input: slate_core.PointerEvent, MouseButton: input_core.Key, ReturnValue: bool) -> bool: ...
    def PointerEvent_GetWheelDelta(self, Input: slate_core.PointerEvent, ReturnValue: float) -> float: ...
    def PointerEvent_GetUserIndex(self, Input: slate_core.PointerEvent, ReturnValue: int) -> int: ...
    def PointerEvent_GetTouchpadIndex(self, Input: slate_core.PointerEvent, ReturnValue: int) -> int: ...
    def PointerEvent_GetScreenSpacePosition(self, Input: slate_core.PointerEvent, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def PointerEvent_GetPointerIndex(self, Input: slate_core.PointerEvent, ReturnValue: int) -> int: ...
    def PointerEvent_GetLastScreenSpacePosition(self, Input: slate_core.PointerEvent, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def PointerEvent_GetGestureType(self, Input: slate_core.PointerEvent, ReturnValue: ESlateGesture) -> ESlateGesture: ...
    def PointerEvent_GetGestureDelta(self, Input: slate_core.PointerEvent, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def PointerEvent_GetEffectingButton(self, Input: slate_core.PointerEvent, ReturnValue: input_core.Key) -> input_core.Key: ...
    def PointerEvent_GetCursorDelta(self, Input: slate_core.PointerEvent, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def Key_IsVectorAxis(self, Key: input_core.Key, ReturnValue: bool) -> bool: ...
    def Key_IsValid(self, Key: input_core.Key, ReturnValue: bool) -> bool: ...
    def Key_IsMouseButton(self, Key: input_core.Key, ReturnValue: bool) -> bool: ...
    def Key_IsModifierKey(self, Key: input_core.Key, ReturnValue: bool) -> bool: ...
    def Key_IsKeyboardKey(self, Key: input_core.Key, ReturnValue: bool) -> bool: ...
    def Key_IsGamepadKey(self, Key: input_core.Key, ReturnValue: bool) -> bool: ...
    def Key_IsFloatAxis(self, Key: input_core.Key, ReturnValue: bool) -> bool: ...
    def Key_GetDisplayName(self, Key: input_core.Key, ReturnValue: str) -> str: ...
    def InputEvent_IsShiftDown(self, Input: slate_core.InputEvent, ReturnValue: bool) -> bool: ...
    def InputEvent_IsRightShiftDown(self, Input: slate_core.InputEvent, ReturnValue: bool) -> bool: ...
    def InputEvent_IsRightControlDown(self, Input: slate_core.InputEvent, ReturnValue: bool) -> bool: ...
    def InputEvent_IsRightCommandDown(self, Input: slate_core.InputEvent, ReturnValue: bool) -> bool: ...
    def InputEvent_IsRightAltDown(self, Input: slate_core.InputEvent, ReturnValue: bool) -> bool: ...
    def InputEvent_IsRepeat(self, Input: slate_core.InputEvent, ReturnValue: bool) -> bool: ...
    def InputEvent_IsLeftShiftDown(self, Input: slate_core.InputEvent, ReturnValue: bool) -> bool: ...
    def InputEvent_IsLeftControlDown(self, Input: slate_core.InputEvent, ReturnValue: bool) -> bool: ...
    def InputEvent_IsLeftCommandDown(self, Input: slate_core.InputEvent, ReturnValue: bool) -> bool: ...
    def InputEvent_IsLeftAltDown(self, Input: slate_core.InputEvent, ReturnValue: bool) -> bool: ...
    def InputEvent_IsControlDown(self, Input: slate_core.InputEvent, ReturnValue: bool) -> bool: ...
    def InputEvent_IsCommandDown(self, Input: slate_core.InputEvent, ReturnValue: bool) -> bool: ...
    def InputEvent_IsAltDown(self, Input: slate_core.InputEvent, ReturnValue: bool) -> bool: ...
    def GetUserIndex(self, Input: slate_core.KeyEvent, ReturnValue: int) -> int: ...
    def GetKey(self, Input: slate_core.KeyEvent, ReturnValue: input_core.Key) -> input_core.Key: ...
    def GetAnalogValue(self, Input: slate_core.AnalogInputEvent, ReturnValue: float) -> float: ...
    def EqualEqual_KeyKey(self, A: input_core.Key, B: input_core.Key, ReturnValue: bool) -> bool: ...
    def EqualEqual_InputChordInputChord(self, A: slate.InputChord, B: slate.InputChord, ReturnValue: bool) -> bool: ...
    def CalibrateTilt(self): ...


class KismetInternationalizationLibrary(BlueprintFunctionLibrary):

    def SetCurrentLocale(self, Culture: str, SaveToConfig: bool, ReturnValue: bool) -> bool: ...
    def SetCurrentLanguageAndLocale(self, Culture: str, SaveToConfig: bool, ReturnValue: bool) -> bool: ...
    def SetCurrentLanguage(self, Culture: str, SaveToConfig: bool, ReturnValue: bool) -> bool: ...
    def SetCurrentCulture(self, Culture: str, SaveToConfig: bool, ReturnValue: bool) -> bool: ...
    def SetCurrentAssetGroupCulture(self, AssetGroup: str, Culture: str, SaveToConfig: bool, ReturnValue: bool) -> bool: ...
    def GetCurrentLocale(self, ReturnValue: str) -> str: ...
    def GetCurrentLanguage(self, ReturnValue: str) -> str: ...
    def GetCurrentCulture(self, ReturnValue: str) -> str: ...
    def GetCurrentAssetGroupCulture(self, AssetGroup: str, ReturnValue: str) -> str: ...
    def ClearCurrentAssetGroupCulture(self, AssetGroup: str, SaveToConfig: bool): ...


class KismetMaterialLibrary(BlueprintFunctionLibrary):

    def SetVectorParameterValue(self, WorldContextObject: unreal.UObject, Collection: MaterialParameterCollection, ParameterName: str, ParameterValue: core_uobject.LinearColor): ...
    def SetScalarParameterValue(self, WorldContextObject: unreal.UObject, Collection: MaterialParameterCollection, ParameterName: str, ParameterValue: float): ...
    def GetVectorParameterValue(self, WorldContextObject: unreal.UObject, Collection: MaterialParameterCollection, ParameterName: str, ReturnValue: core_uobject.LinearColor) -> core_uobject.LinearColor: ...
    def GetScalarParameterValue(self, WorldContextObject: unreal.UObject, Collection: MaterialParameterCollection, ParameterName: str, ReturnValue: float) -> float: ...
    def CreateDynamicMaterialInstance(self, WorldContextObject: unreal.UObject, Parent: MaterialInterface, OptionalName: str, ReturnValue: MaterialInstanceDynamic) -> MaterialInstanceDynamic: ...


class KismetMathLibrary(BlueprintFunctionLibrary):

    def Xor_IntInt(self, A: int, B: int, ReturnValue: int) -> int: ...
    def VSizeXY(self, A: core_uobject.Vector, ReturnValue: float) -> float: ...
    def VSizeSquared(self, A: core_uobject.Vector, ReturnValue: float) -> float: ...
    def VSize2DSquared(self, A: core_uobject.Vector2D, ReturnValue: float) -> float: ...
    def VSize2D(self, A: core_uobject.Vector2D, ReturnValue: float) -> float: ...
    def VSize(self, A: core_uobject.Vector, ReturnValue: float) -> float: ...
    def VLerp(self, A: core_uobject.Vector, B: core_uobject.Vector, Alpha: float, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def VInterpTo_Constant(self, Current: core_uobject.Vector, Target: core_uobject.Vector, DeltaTime: float, InterpSpeed: float, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def VInterpTo(self, Current: core_uobject.Vector, Target: core_uobject.Vector, DeltaTime: float, InterpSpeed: float, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def VectorSpringInterp(self, Current: core_uobject.Vector, Target: core_uobject.Vector, SpringState: VectorSpringState, Stiffness: float, CriticalDampingFactor: float, DeltaTime: float, Mass: float, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def Vector2DInterpTo_Constant(self, Current: core_uobject.Vector2D, Target: core_uobject.Vector2D, DeltaTime: float, InterpSpeed: float, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def Vector2DInterpTo(self, Current: core_uobject.Vector2D, Target: core_uobject.Vector2D, DeltaTime: float, InterpSpeed: float, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def VEase(self, A: core_uobject.Vector, B: core_uobject.Vector, Alpha: float, EasingFunc: int, BlendExp: float, Steps: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def UtcNow(self, ReturnValue: core_uobject.DateTime) -> core_uobject.DateTime: ...
    def TransformRotation(self, T: core_uobject.Transform, Rotation: core_uobject.Rotator, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def TransformLocation(self, T: core_uobject.Transform, Location: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def TransformDirection(self, T: core_uobject.Transform, Direction: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def Transform_Determinant(self, Transform: core_uobject.Transform, ReturnValue: float) -> float: ...
    def Today(self, ReturnValue: core_uobject.DateTime) -> core_uobject.DateTime: ...
    def TLerp(self, A: core_uobject.Transform, B: core_uobject.Transform, Alpha: float, InterpMode: int, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def TInterpTo(self, Current: core_uobject.Transform, Target: core_uobject.Transform, DeltaTime: float, InterpSpeed: float, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def TimespanZeroValue(self, ReturnValue: core_uobject.Timespan) -> core_uobject.Timespan: ...
    def TimespanRatio(self, A: core_uobject.Timespan, B: core_uobject.Timespan, ReturnValue: float) -> float: ...
    def TimespanMinValue(self, ReturnValue: core_uobject.Timespan) -> core_uobject.Timespan: ...
    def TimespanMaxValue(self, ReturnValue: core_uobject.Timespan) -> core_uobject.Timespan: ...
    def TimespanFromString(self, TimespanString: str, Result: core_uobject.Timespan, ReturnValue: bool) -> bool: ...
    def TEase(self, A: core_uobject.Transform, B: core_uobject.Transform, Alpha: float, EasingFunc: int, BlendExp: float, Steps: int, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def Tan(self, A: float, ReturnValue: float) -> float: ...
    def Subtract_VectorVector(self, A: core_uobject.Vector, B: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def Subtract_VectorInt(self, A: core_uobject.Vector, B: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def Subtract_VectorFloat(self, A: core_uobject.Vector, B: float, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def Subtract_Vector2DVector2D(self, A: core_uobject.Vector2D, B: core_uobject.Vector2D, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def Subtract_Vector2DFloat(self, A: core_uobject.Vector2D, B: float, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def Subtract_TimespanTimespan(self, A: core_uobject.Timespan, B: core_uobject.Timespan, ReturnValue: core_uobject.Timespan) -> core_uobject.Timespan: ...
    def Subtract_IntInt(self, A: int, B: int, ReturnValue: int) -> int: ...
    def Subtract_FloatFloat(self, A: float, B: float, ReturnValue: float) -> float: ...
    def Subtract_DateTimeTimespan(self, A: core_uobject.DateTime, B: core_uobject.Timespan, ReturnValue: core_uobject.DateTime) -> core_uobject.DateTime: ...
    def Subtract_DateTimeDateTime(self, A: core_uobject.DateTime, B: core_uobject.DateTime, ReturnValue: core_uobject.Timespan) -> core_uobject.Timespan: ...
    def Subtract_ByteByte(self, A: int, B: int, ReturnValue: int) -> int: ...
    def Square(self, A: float, ReturnValue: float) -> float: ...
    def Sqrt(self, A: float, ReturnValue: float) -> float: ...
    def Sin(self, A: float, ReturnValue: float) -> float: ...
    def SignOfInteger(self, A: int, ReturnValue: int) -> int: ...
    def SignOfFloat(self, A: float, ReturnValue: float) -> float: ...
    def SetRandomStreamSeed(self, Stream: core_uobject.RandomStream, NewSeed: int): ...
    def SelectVector(self, A: core_uobject.Vector, B: core_uobject.Vector, bPickA: bool, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def SelectTransform(self, A: core_uobject.Transform, B: core_uobject.Transform, bPickA: bool, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def SelectString(self, A: str, B: str, bPickA: bool, ReturnValue: str) -> str: ...
    def SelectRotator(self, A: core_uobject.Rotator, B: core_uobject.Rotator, bPickA: bool, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def SelectObject(self, A: unreal.UObject, B: unreal.UObject, bSelectA: bool, ReturnValue: unreal.UObject) -> unreal.UObject: ...
    def SelectInt(self, A: int, B: int, bPickA: bool, ReturnValue: int) -> int: ...
    def SelectFloat(self, A: float, B: float, bPickA: bool, ReturnValue: float) -> float: ...
    def SelectColor(self, A: core_uobject.LinearColor, B: core_uobject.LinearColor, bPickA: bool, ReturnValue: core_uobject.LinearColor) -> core_uobject.LinearColor: ...
    def SelectClass(self, A: unreal.UClass, B: unreal.UClass, bSelectA: bool, ReturnValue: unreal.UClass) -> unreal.UClass: ...
    def SeedRandomStream(self, Stream: core_uobject.RandomStream): ...
    def Round(self, A: float, ReturnValue: int) -> int: ...
    def RotatorFromAxisAndAngle(self, AXIS: core_uobject.Vector, Angle: float, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def RotateAngleAxis(self, InVect: core_uobject.Vector, AngleDeg: float, AXIS: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def RLerp(self, A: core_uobject.Rotator, B: core_uobject.Rotator, Alpha: float, bShortestPath: bool, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def RInterpTo_Constant(self, Current: core_uobject.Rotator, Target: core_uobject.Rotator, DeltaTime: float, InterpSpeed: float, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def RInterpTo(self, Current: core_uobject.Rotator, Target: core_uobject.Rotator, DeltaTime: float, InterpSpeed: float, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def RGBToHSV_Vector(self, RGB: core_uobject.LinearColor, HSV: core_uobject.LinearColor): ...
    def RGBToHSV(self, InColor: core_uobject.LinearColor, H: float, S: float, V: float, A: float): ...
    def ResetVectorSpringState(self, SpringState: VectorSpringState): ...
    def ResetRandomStream(self, Stream: core_uobject.RandomStream): ...
    def ResetFloatSpringState(self, SpringState: FloatSpringState): ...
    def REase(self, A: core_uobject.Rotator, B: core_uobject.Rotator, Alpha: float, bShortestPath: bool, EasingFunc: int, BlendExp: float, Steps: int, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def RandomUnitVectorInEllipticalConeInRadiansFromStream(self, ConeDir: core_uobject.Vector, MaxYawInRadians: float, MaxPitchInRadians: float, Stream: core_uobject.RandomStream, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def RandomUnitVectorInEllipticalConeInRadians(self, ConeDir: core_uobject.Vector, MaxYawInRadians: float, MaxPitchInRadians: float, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def RandomUnitVectorInEllipticalConeInDegreesFromStream(self, ConeDir: core_uobject.Vector, MaxYawInDegrees: float, MaxPitchInDegrees: float, Stream: core_uobject.RandomStream, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def RandomUnitVectorInEllipticalConeInDegrees(self, ConeDir: core_uobject.Vector, MaxYawInDegrees: float, MaxPitchInDegrees: float, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def RandomUnitVectorInConeInRadiansFromStream(self, ConeDir: core_uobject.Vector, ConeHalfAngleInRadians: float, Stream: core_uobject.RandomStream, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def RandomUnitVectorInConeInRadians(self, ConeDir: core_uobject.Vector, ConeHalfAngleInRadians: float, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def RandomUnitVectorInConeInDegreesFromStream(self, ConeDir: core_uobject.Vector, ConeHalfAngleInDegrees: float, Stream: core_uobject.RandomStream, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def RandomUnitVectorInConeInDegrees(self, ConeDir: core_uobject.Vector, ConeHalfAngleInDegrees: float, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def RandomUnitVectorFromStream(self, Stream: core_uobject.RandomStream, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def RandomUnitVector(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def RandomRotatorFromStream(self, bRoll: bool, Stream: core_uobject.RandomStream, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def RandomRotator(self, bRoll: bool, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def RandomPointInBoundingBox(self, Origin: core_uobject.Vector, BoxExtent: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def RandomIntegerInRangeFromStream(self, Min: int, Max: int, Stream: core_uobject.RandomStream, ReturnValue: int) -> int: ...
    def RandomIntegerInRange(self, Min: int, Max: int, ReturnValue: int) -> int: ...
    def RandomIntegerFromStream(self, Max: int, Stream: core_uobject.RandomStream, ReturnValue: int) -> int: ...
    def RandomInteger(self, Max: int, ReturnValue: int) -> int: ...
    def RandomFloatInRangeFromStream(self, Min: float, Max: float, Stream: core_uobject.RandomStream, ReturnValue: float) -> float: ...
    def RandomFloatInRange(self, Min: float, Max: float, ReturnValue: float) -> float: ...
    def RandomFloatFromStream(self, Stream: core_uobject.RandomStream, ReturnValue: float) -> float: ...
    def RandomFloat(self, ReturnValue: float) -> float: ...
    def RandomBoolWithWeightFromStream(self, Weight: float, RandomStream: core_uobject.RandomStream, ReturnValue: bool) -> bool: ...
    def RandomBoolWithWeight(self, Weight: float, ReturnValue: bool) -> bool: ...
    def RandomBoolFromStream(self, Stream: core_uobject.RandomStream, ReturnValue: bool) -> bool: ...
    def RandomBool(self, ReturnValue: bool) -> bool: ...
    def RadiansToDegrees(self, A: float, ReturnValue: float) -> float: ...
    def ProjectVectorOnToVector(self, V: core_uobject.Vector, Target: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def ProjectVectorOnToPlane(self, V: core_uobject.Vector, PlaneNormal: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def ProjectPointOnToPlane(self, Point: core_uobject.Vector, PlaneBase: core_uobject.Vector, PlaneNormal: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def PointsAreCoplanar(self, Points: unreal.WrappedArray[core_uobject.Vector], Tolerance: float, ReturnValue: bool) -> bool: ...
    def Percent_IntInt(self, A: int, B: int, ReturnValue: int) -> int: ...
    def Percent_FloatFloat(self, A: float, B: float, ReturnValue: float) -> float: ...
    def Percent_ByteByte(self, A: int, B: int, ReturnValue: int) -> int: ...
    def Or_IntInt(self, A: int, B: int, ReturnValue: int) -> int: ...
    def Now(self, ReturnValue: core_uobject.DateTime) -> core_uobject.DateTime: ...
    def NotEqual_VectorVector(self, A: core_uobject.Vector, B: core_uobject.Vector, ErrorTolerance: float, ReturnValue: bool) -> bool: ...
    def NotEqual_Vector2DVector2D(self, A: core_uobject.Vector2D, B: core_uobject.Vector2D, ErrorTolerance: float, ReturnValue: bool) -> bool: ...
    def NotEqual_TimespanTimespan(self, A: core_uobject.Timespan, B: core_uobject.Timespan, ReturnValue: bool) -> bool: ...
    def NotEqual_RotatorRotator(self, A: core_uobject.Rotator, B: core_uobject.Rotator, ErrorTolerance: float, ReturnValue: bool) -> bool: ...
    def NotEqual_ObjectObject(self, A: unreal.UObject, B: unreal.UObject, ReturnValue: bool) -> bool: ...
    def NotEqual_NameName(self, A: str, B: str, ReturnValue: bool) -> bool: ...
    def NotEqual_IntInt(self, A: int, B: int, ReturnValue: bool) -> bool: ...
    def NotEqual_FloatFloat(self, A: float, B: float, ReturnValue: bool) -> bool: ...
    def NotEqual_DateTimeDateTime(self, A: core_uobject.DateTime, B: core_uobject.DateTime, ReturnValue: bool) -> bool: ...
    def NotEqual_ClassClass(self, A: unreal.UClass, B: unreal.UClass, ReturnValue: bool) -> bool: ...
    def NotEqual_ByteByte(self, A: int, B: int, ReturnValue: bool) -> bool: ...
    def NotEqual_BoolBool(self, A: bool, B: bool, ReturnValue: bool) -> bool: ...
    def Not_PreBool(self, A: bool, ReturnValue: bool) -> bool: ...
    def Not_Int(self, A: int, ReturnValue: int) -> int: ...
    def NormalizeToRange(self, Value: float, RangeMin: float, RangeMax: float, ReturnValue: float) -> float: ...
    def NormalizedDeltaRotator(self, A: core_uobject.Rotator, B: core_uobject.Rotator, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def NormalizeAxis(self, Angle: float, ReturnValue: float) -> float: ...
    def Normal2D(self, A: core_uobject.Vector2D, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def Normal(self, A: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def NegateVector(self, A: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def NegateRotator(self, A: core_uobject.Rotator, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def NearlyEqual_TransformTransform(self, A: core_uobject.Transform, B: core_uobject.Transform, LocationTolerance: float, RotationTolerance: float, Scale3DTolerance: float, ReturnValue: bool) -> bool: ...
    def NearlyEqual_FloatFloat(self, A: float, B: float, ErrorTolerance: float, ReturnValue: bool) -> bool: ...
    def MultiplyMultiply_FloatFloat(self, Base: float, Exp: float, ReturnValue: float) -> float: ...
    def MultiplyByPi(self, Value: float, ReturnValue: float) -> float: ...
    def Multiply_VectorVector(self, A: core_uobject.Vector, B: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def Multiply_VectorInt(self, A: core_uobject.Vector, B: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def Multiply_VectorFloat(self, A: core_uobject.Vector, B: float, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def Multiply_Vector2DVector2D(self, A: core_uobject.Vector2D, B: core_uobject.Vector2D, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def Multiply_Vector2DFloat(self, A: core_uobject.Vector2D, B: float, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def Multiply_TimespanFloat(self, A: core_uobject.Timespan, Scalar: float, ReturnValue: core_uobject.Timespan) -> core_uobject.Timespan: ...
    def Multiply_RotatorInt(self, A: core_uobject.Rotator, B: int, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def Multiply_RotatorFloat(self, A: core_uobject.Rotator, B: float, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def Multiply_LinearColorLinearColor(self, A: core_uobject.LinearColor, B: core_uobject.LinearColor, ReturnValue: core_uobject.LinearColor) -> core_uobject.LinearColor: ...
    def Multiply_LinearColorFloat(self, A: core_uobject.LinearColor, B: float, ReturnValue: core_uobject.LinearColor) -> core_uobject.LinearColor: ...
    def Multiply_IntInt(self, A: int, B: int, ReturnValue: int) -> int: ...
    def Multiply_IntFloat(self, A: int, B: float, ReturnValue: float) -> float: ...
    def Multiply_FloatFloat(self, A: float, B: float, ReturnValue: float) -> float: ...
    def Multiply_ByteByte(self, A: int, B: int, ReturnValue: int) -> int: ...
    def MirrorVectorByNormal(self, InVect: core_uobject.Vector, InNormal: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def MinOfIntArray(self, IntArray: unreal.WrappedArray[int], IndexOfMinValue: int, MinValue: int): ...
    def MinOfFloatArray(self, FloatArray: unreal.WrappedArray[float], IndexOfMinValue: int, MinValue: float): ...
    def MinOfByteArray(self, ByteArray: unreal.WrappedArray[int], IndexOfMinValue: int, MinValue: int): ...
    def MinimumAreaRectangle(self, WorldContextObject: unreal.UObject, InVerts: unreal.WrappedArray[core_uobject.Vector], SampleSurfaceNormal: core_uobject.Vector, OutRectCenter: core_uobject.Vector, OutRectRotation: core_uobject.Rotator, OutSideLengthX: float, OutSideLengthY: float, bDebugDraw: bool): ...
    def Min(self, A: int, B: int, ReturnValue: int) -> int: ...
    def MaxOfIntArray(self, IntArray: unreal.WrappedArray[int], IndexOfMaxValue: int, MaxValue: int): ...
    def MaxOfFloatArray(self, FloatArray: unreal.WrappedArray[float], IndexOfMaxValue: int, MaxValue: float): ...
    def MaxOfByteArray(self, ByteArray: unreal.WrappedArray[int], IndexOfMaxValue: int, MaxValue: int): ...
    def Max(self, A: int, B: int, ReturnValue: int) -> int: ...
    def MapRangeUnclamped(self, Value: float, InRangeA: float, InRangeB: float, OutRangeA: float, OutRangeB: float, ReturnValue: float) -> float: ...
    def MapRangeClamped(self, Value: float, InRangeA: float, InRangeB: float, OutRangeA: float, OutRangeB: float, ReturnValue: float) -> float: ...
    def MakeVector2D(self, X: float, Y: float, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def MakeVector(self, X: float, Y: float, Z: float, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def MakeTransform(self, Location: core_uobject.Vector, Rotation: core_uobject.Rotator, Scale: core_uobject.Vector, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def MakeTimespan2(self, Days: int, Hours: int, Minutes: int, Seconds: int, FractionNano: int, ReturnValue: core_uobject.Timespan) -> core_uobject.Timespan: ...
    def MakeTimespan(self, Days: int, Hours: int, Minutes: int, Seconds: int, Milliseconds: int, ReturnValue: core_uobject.Timespan) -> core_uobject.Timespan: ...
    def MakeRotFromZY(self, Z: core_uobject.Vector, Y: core_uobject.Vector, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def MakeRotFromZX(self, Z: core_uobject.Vector, X: core_uobject.Vector, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def MakeRotFromZ(self, Z: core_uobject.Vector, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def MakeRotFromYZ(self, Y: core_uobject.Vector, Z: core_uobject.Vector, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def MakeRotFromYX(self, Y: core_uobject.Vector, X: core_uobject.Vector, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def MakeRotFromY(self, Y: core_uobject.Vector, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def MakeRotFromXZ(self, X: core_uobject.Vector, Z: core_uobject.Vector, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def MakeRotFromXY(self, X: core_uobject.Vector, Y: core_uobject.Vector, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def MakeRotFromX(self, X: core_uobject.Vector, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def MakeRotator(self, Roll: float, Pitch: float, Yaw: float, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def MakeRotationFromAxes(self, Forward: core_uobject.Vector, Right: core_uobject.Vector, Up: core_uobject.Vector, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def MakeRandomStream(self, InitialSeed: int, ReturnValue: core_uobject.RandomStream) -> core_uobject.RandomStream: ...
    def MakePulsatingValue(self, InCurrentTime: float, InPulsesPerSecond: float, InPhase: float, ReturnValue: float) -> float: ...
    def MakePlaneFromPointAndNormal(self, Point: core_uobject.Vector, Normal: core_uobject.Vector, ReturnValue: core_uobject.Plane) -> core_uobject.Plane: ...
    def MakeDateTime(self, Year: int, Month: int, Day: int, Hour: int, Minute: int, Second: int, Millisecond: int, ReturnValue: core_uobject.DateTime) -> core_uobject.DateTime: ...
    def MakeColor(self, R: float, G: float, B: float, A: float, ReturnValue: core_uobject.LinearColor) -> core_uobject.LinearColor: ...
    def MakeBox2D(self, Min: core_uobject.Vector2D, Max: core_uobject.Vector2D, ReturnValue: core_uobject.Box2D) -> core_uobject.Box2D: ...
    def MakeBox(self, Min: core_uobject.Vector, Max: core_uobject.Vector, ReturnValue: core_uobject.Box) -> core_uobject.Box: ...
    def Loge(self, A: float, ReturnValue: float) -> float: ...
    def Log(self, A: float, Base: float, ReturnValue: float) -> float: ...
    def LinePlaneIntersection_OriginNormal(self, LineStart: core_uobject.Vector, LineEnd: core_uobject.Vector, PlaneOrigin: core_uobject.Vector, PlaneNormal: core_uobject.Vector, T: float, Intersection: core_uobject.Vector, ReturnValue: bool) -> bool: ...
    def LinePlaneIntersection(self, LineStart: core_uobject.Vector, LineEnd: core_uobject.Vector, APlane: core_uobject.Plane, T: float, Intersection: core_uobject.Vector, ReturnValue: bool) -> bool: ...
    def LinearColorLerpUsingHSV(self, A: core_uobject.LinearColor, B: core_uobject.LinearColor, Alpha: float, ReturnValue: core_uobject.LinearColor) -> core_uobject.LinearColor: ...
    def LinearColorLerp(self, A: core_uobject.LinearColor, B: core_uobject.LinearColor, Alpha: float, ReturnValue: core_uobject.LinearColor) -> core_uobject.LinearColor: ...
    def LessLess_VectorRotator(self, A: core_uobject.Vector, B: core_uobject.Rotator, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def LessEqual_TimespanTimespan(self, A: core_uobject.Timespan, B: core_uobject.Timespan, ReturnValue: bool) -> bool: ...
    def LessEqual_IntInt(self, A: int, B: int, ReturnValue: bool) -> bool: ...
    def LessEqual_FloatFloat(self, A: float, B: float, ReturnValue: bool) -> bool: ...
    def LessEqual_DateTimeDateTime(self, A: core_uobject.DateTime, B: core_uobject.DateTime, ReturnValue: bool) -> bool: ...
    def LessEqual_ByteByte(self, A: int, B: int, ReturnValue: bool) -> bool: ...
    def Less_TimespanTimespan(self, A: core_uobject.Timespan, B: core_uobject.Timespan, ReturnValue: bool) -> bool: ...
    def Less_IntInt(self, A: int, B: int, ReturnValue: bool) -> bool: ...
    def Less_FloatFloat(self, A: float, B: float, ReturnValue: bool) -> bool: ...
    def Less_DateTimeDateTime(self, A: core_uobject.DateTime, B: core_uobject.DateTime, ReturnValue: bool) -> bool: ...
    def Less_ByteByte(self, A: int, B: int, ReturnValue: bool) -> bool: ...
    def Lerp(self, A: float, B: float, Alpha: float, ReturnValue: float) -> float: ...
    def IsPointInBoxWithTransform(self, Point: core_uobject.Vector, BoxWorldTransform: core_uobject.Transform, BoxExtent: core_uobject.Vector, ReturnValue: bool) -> bool: ...
    def IsPointInBox(self, Point: core_uobject.Vector, BoxOrigin: core_uobject.Vector, BoxExtent: core_uobject.Vector, ReturnValue: bool) -> bool: ...
    def IsMorning(self, A: core_uobject.DateTime, ReturnValue: bool) -> bool: ...
    def IsLeapYear(self, Year: int, ReturnValue: bool) -> bool: ...
    def IsAfternoon(self, A: core_uobject.DateTime, ReturnValue: bool) -> bool: ...
    def InvertTransform(self, T: core_uobject.Transform, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def InverseTransformRotation(self, T: core_uobject.Transform, Rotation: core_uobject.Rotator, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def InverseTransformLocation(self, T: core_uobject.Transform, Location: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def InverseTransformDirection(self, T: core_uobject.Transform, Direction: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def InRange_IntInt(self, Value: int, Min: int, Max: int, InclusiveMin: bool, InclusiveMax: bool, ReturnValue: bool) -> bool: ...
    def InRange_FloatFloat(self, Value: float, Min: float, Max: float, InclusiveMin: bool, InclusiveMax: bool, ReturnValue: bool) -> bool: ...
    def Hypotenuse(self, Width: float, Height: float, ReturnValue: float) -> float: ...
    def HSVToRGB_Vector(self, HSV: core_uobject.LinearColor, RGB: core_uobject.LinearColor): ...
    def HSVToRGB(self, H: float, S: float, V: float, A: float, ReturnValue: core_uobject.LinearColor) -> core_uobject.LinearColor: ...
    def GridSnap_Float(self, Location: float, GridSize: float, ReturnValue: float) -> float: ...
    def GreaterGreater_VectorRotator(self, A: core_uobject.Vector, B: core_uobject.Rotator, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GreaterEqual_TimespanTimespan(self, A: core_uobject.Timespan, B: core_uobject.Timespan, ReturnValue: bool) -> bool: ...
    def GreaterEqual_IntInt(self, A: int, B: int, ReturnValue: bool) -> bool: ...
    def GreaterEqual_FloatFloat(self, A: float, B: float, ReturnValue: bool) -> bool: ...
    def GreaterEqual_DateTimeDateTime(self, A: core_uobject.DateTime, B: core_uobject.DateTime, ReturnValue: bool) -> bool: ...
    def GreaterEqual_ByteByte(self, A: int, B: int, ReturnValue: bool) -> bool: ...
    def Greater_TimespanTimespan(self, A: core_uobject.Timespan, B: core_uobject.Timespan, ReturnValue: bool) -> bool: ...
    def Greater_IntInt(self, A: int, B: int, ReturnValue: bool) -> bool: ...
    def Greater_FloatFloat(self, A: float, B: float, ReturnValue: bool) -> bool: ...
    def Greater_DateTimeDateTime(self, A: core_uobject.DateTime, B: core_uobject.DateTime, ReturnValue: bool) -> bool: ...
    def Greater_ByteByte(self, A: int, B: int, ReturnValue: bool) -> bool: ...
    def GetYear(self, A: core_uobject.DateTime, ReturnValue: int) -> int: ...
    def GetYawPitchFromVector(self, InVec: core_uobject.Vector, Yaw: float, Pitch: float): ...
    def GetVectorArrayAverage(self, Vectors: unreal.WrappedArray[core_uobject.Vector], ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetUpVector(self, InRot: core_uobject.Rotator, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetTotalSeconds(self, A: core_uobject.Timespan, ReturnValue: float) -> float: ...
    def GetTotalMinutes(self, A: core_uobject.Timespan, ReturnValue: float) -> float: ...
    def GetTotalMilliseconds(self, A: core_uobject.Timespan, ReturnValue: float) -> float: ...
    def GetTotalHours(self, A: core_uobject.Timespan, ReturnValue: float) -> float: ...
    def GetTotalDays(self, A: core_uobject.Timespan, ReturnValue: float) -> float: ...
    def GetTimeOfDay(self, A: core_uobject.DateTime, ReturnValue: core_uobject.Timespan) -> core_uobject.Timespan: ...
    def GetTAU(self, ReturnValue: float) -> float: ...
    def GetSlopeDegreeAngles(self, MyRightYAxis: core_uobject.Vector, FloorNormal: core_uobject.Vector, UpVector: core_uobject.Vector, OutSlopePitchDegreeAngle: float, OutSlopeRollDegreeAngle: float): ...
    def GetSeconds(self, A: core_uobject.Timespan, ReturnValue: int) -> int: ...
    def GetSecond(self, A: core_uobject.DateTime, ReturnValue: int) -> int: ...
    def GetRightVector(self, InRot: core_uobject.Rotator, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetReflectionVector(self, Direction: core_uobject.Vector, SurfaceNormal: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetPointDistanceToSegment(self, Point: core_uobject.Vector, SegmentStart: core_uobject.Vector, SegmentEnd: core_uobject.Vector, ReturnValue: float) -> float: ...
    def GetPointDistanceToLine(self, Point: core_uobject.Vector, LineOrigin: core_uobject.Vector, LineDirection: core_uobject.Vector, ReturnValue: float) -> float: ...
    def GetPI(self, ReturnValue: float) -> float: ...
    def GetMonth(self, A: core_uobject.DateTime, ReturnValue: int) -> int: ...
    def GetMinutes(self, A: core_uobject.Timespan, ReturnValue: int) -> int: ...
    def GetMinute(self, A: core_uobject.DateTime, ReturnValue: int) -> int: ...
    def GetMinElement(self, A: core_uobject.Vector, ReturnValue: float) -> float: ...
    def GetMilliseconds(self, A: core_uobject.Timespan, ReturnValue: int) -> int: ...
    def GetMillisecond(self, A: core_uobject.DateTime, ReturnValue: int) -> int: ...
    def GetMaxElement(self, A: core_uobject.Vector, ReturnValue: float) -> float: ...
    def GetHours(self, A: core_uobject.Timespan, ReturnValue: int) -> int: ...
    def GetHour12(self, A: core_uobject.DateTime, ReturnValue: int) -> int: ...
    def GetHour(self, A: core_uobject.DateTime, ReturnValue: int) -> int: ...
    def GetForwardVector(self, InRot: core_uobject.Rotator, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetDuration(self, A: core_uobject.Timespan, ReturnValue: core_uobject.Timespan) -> core_uobject.Timespan: ...
    def GetDirectionUnitVector(self, From: core_uobject.Vector, To: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetDays(self, A: core_uobject.Timespan, ReturnValue: int) -> int: ...
    def GetDayOfYear(self, A: core_uobject.DateTime, ReturnValue: int) -> int: ...
    def GetDay(self, A: core_uobject.DateTime, ReturnValue: int) -> int: ...
    def GetDate(self, A: core_uobject.DateTime, ReturnValue: core_uobject.DateTime) -> core_uobject.DateTime: ...
    def GetAzimuthAndElevation(self, InDirection: core_uobject.Vector, ReferenceFrame: core_uobject.Transform, Azimuth: float, Elevation: float): ...
    def GetAxes(self, A: core_uobject.Rotator, X: core_uobject.Vector, Y: core_uobject.Vector, Z: core_uobject.Vector): ...
    def FTruncVector(self, InVector: core_uobject.Vector, ReturnValue: core_uobject.IntVector) -> core_uobject.IntVector: ...
    def FTrunc(self, A: float, ReturnValue: int) -> int: ...
    def FromSeconds(self, Seconds: float, ReturnValue: core_uobject.Timespan) -> core_uobject.Timespan: ...
    def FromMinutes(self, Minutes: float, ReturnValue: core_uobject.Timespan) -> core_uobject.Timespan: ...
    def FromMilliseconds(self, Milliseconds: float, ReturnValue: core_uobject.Timespan) -> core_uobject.Timespan: ...
    def FromHours(self, Hours: float, ReturnValue: core_uobject.Timespan) -> core_uobject.Timespan: ...
    def FromDays(self, Days: float, ReturnValue: core_uobject.Timespan) -> core_uobject.Timespan: ...
    def Fraction(self, A: float, ReturnValue: float) -> float: ...
    def FMod(self, Dividend: float, Divisor: float, Remainder: float, ReturnValue: int) -> int: ...
    def FMin(self, A: float, B: float, ReturnValue: float) -> float: ...
    def FMax(self, A: float, B: float, ReturnValue: float) -> float: ...
    def FloatSpringInterp(self, Current: float, Target: float, SpringState: FloatSpringState, Stiffness: float, CriticalDampingFactor: float, DeltaTime: float, Mass: float, ReturnValue: float) -> float: ...
    def FixedTurn(self, InCurrent: float, InDesired: float, InDeltaRate: float, ReturnValue: float) -> float: ...
    def FInterpTo_Constant(self, Current: float, Target: float, DeltaTime: float, InterpSpeed: float, ReturnValue: float) -> float: ...
    def FInterpTo(self, Current: float, Target: float, DeltaTime: float, InterpSpeed: float, ReturnValue: float) -> float: ...
    def FInterpEaseInOut(self, A: float, B: float, Alpha: float, Exponent: float, ReturnValue: float) -> float: ...
    def FindNearestPointsOnLineSegments(self, Segment1Start: core_uobject.Vector, Segment1End: core_uobject.Vector, Segment2Start: core_uobject.Vector, Segment2End: core_uobject.Vector, Segment1Point: core_uobject.Vector, Segment2Point: core_uobject.Vector): ...
    def FindLookAtRotation(self, Start: core_uobject.Vector, Target: core_uobject.Vector, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def FindClosestPointOnSegment(self, Point: core_uobject.Vector, SegmentStart: core_uobject.Vector, SegmentEnd: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def FindClosestPointOnLine(self, Point: core_uobject.Vector, LineOrigin: core_uobject.Vector, LineDirection: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def FFloor(self, A: float, ReturnValue: int) -> int: ...
    def FClamp(self, Value: float, Min: float, Max: float, ReturnValue: float) -> float: ...
    def FCeil(self, A: float, ReturnValue: int) -> int: ...
    def Exp(self, A: float, ReturnValue: float) -> float: ...
    def EqualEqual_VectorVector(self, A: core_uobject.Vector, B: core_uobject.Vector, ErrorTolerance: float, ReturnValue: bool) -> bool: ...
    def EqualEqual_Vector2DVector2D(self, A: core_uobject.Vector2D, B: core_uobject.Vector2D, ErrorTolerance: float, ReturnValue: bool) -> bool: ...
    def EqualEqual_TransformTransform(self, A: core_uobject.Transform, B: core_uobject.Transform, ReturnValue: bool) -> bool: ...
    def EqualEqual_TimespanTimespan(self, A: core_uobject.Timespan, B: core_uobject.Timespan, ReturnValue: bool) -> bool: ...
    def EqualEqual_RotatorRotator(self, A: core_uobject.Rotator, B: core_uobject.Rotator, ErrorTolerance: float, ReturnValue: bool) -> bool: ...
    def EqualEqual_ObjectObject(self, A: unreal.UObject, B: unreal.UObject, ReturnValue: bool) -> bool: ...
    def EqualEqual_NameName(self, A: str, B: str, ReturnValue: bool) -> bool: ...
    def EqualEqual_IntInt(self, A: int, B: int, ReturnValue: bool) -> bool: ...
    def EqualEqual_FloatFloat(self, A: float, B: float, ReturnValue: bool) -> bool: ...
    def EqualEqual_DateTimeDateTime(self, A: core_uobject.DateTime, B: core_uobject.DateTime, ReturnValue: bool) -> bool: ...
    def EqualEqual_ClassClass(self, A: unreal.UClass, B: unreal.UClass, ReturnValue: bool) -> bool: ...
    def EqualEqual_ByteByte(self, A: int, B: int, ReturnValue: bool) -> bool: ...
    def EqualEqual_BoolBool(self, A: bool, B: bool, ReturnValue: bool) -> bool: ...
    def Ease(self, A: float, B: float, Alpha: float, EasingFunc: int, BlendExp: float, Steps: int, ReturnValue: float) -> float: ...
    def DotProduct2D(self, A: core_uobject.Vector2D, B: core_uobject.Vector2D, ReturnValue: float) -> float: ...
    def Dot_VectorVector(self, A: core_uobject.Vector, B: core_uobject.Vector, ReturnValue: float) -> float: ...
    def Divide_VectorVector(self, A: core_uobject.Vector, B: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def Divide_VectorInt(self, A: core_uobject.Vector, B: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def Divide_VectorFloat(self, A: core_uobject.Vector, B: float, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def Divide_Vector2DVector2D(self, A: core_uobject.Vector2D, B: core_uobject.Vector2D, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def Divide_Vector2DFloat(self, A: core_uobject.Vector2D, B: float, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def Divide_TimespanFloat(self, A: core_uobject.Timespan, Scalar: float, ReturnValue: core_uobject.Timespan) -> core_uobject.Timespan: ...
    def Divide_IntInt(self, A: int, B: int, ReturnValue: int) -> int: ...
    def Divide_FloatFloat(self, A: float, B: float, ReturnValue: float) -> float: ...
    def Divide_ByteByte(self, A: int, B: int, ReturnValue: int) -> int: ...
    def DegTan(self, A: float, ReturnValue: float) -> float: ...
    def DegSin(self, A: float, ReturnValue: float) -> float: ...
    def DegreesToRadians(self, A: float, ReturnValue: float) -> float: ...
    def DegCos(self, A: float, ReturnValue: float) -> float: ...
    def DegAtan2(self, A: float, B: float, ReturnValue: float) -> float: ...
    def DegAtan(self, A: float, ReturnValue: float) -> float: ...
    def DegAsin(self, A: float, ReturnValue: float) -> float: ...
    def DegAcos(self, A: float, ReturnValue: float) -> float: ...
    def DaysInYear(self, Year: int, ReturnValue: int) -> int: ...
    def DaysInMonth(self, Year: int, Month: int, ReturnValue: int) -> int: ...
    def DateTimeMinValue(self, ReturnValue: core_uobject.DateTime) -> core_uobject.DateTime: ...
    def DateTimeMaxValue(self, ReturnValue: core_uobject.DateTime) -> core_uobject.DateTime: ...
    def DateTimeFromString(self, DateTimeString: str, Result: core_uobject.DateTime, ReturnValue: bool) -> bool: ...
    def DateTimeFromIsoString(self, IsoString: str, Result: core_uobject.DateTime, ReturnValue: bool) -> bool: ...
    def CrossProduct2D(self, A: core_uobject.Vector2D, B: core_uobject.Vector2D, ReturnValue: float) -> float: ...
    def Cross_VectorVector(self, A: core_uobject.Vector, B: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def CreateVectorFromYawPitch(self, Yaw: float, Pitch: float, Length: float, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def Cos(self, A: float, ReturnValue: float) -> float: ...
    def ConvertTransformToRelative(self, Transform: core_uobject.Transform, ParentTransform: core_uobject.Transform, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def Conv_VectorToVector2D(self, InVector: core_uobject.Vector, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def Conv_VectorToTransform(self, InLocation: core_uobject.Vector, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def Conv_VectorToRotator(self, InVec: core_uobject.Vector, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def Conv_VectorToLinearColor(self, InVec: core_uobject.Vector, ReturnValue: core_uobject.LinearColor) -> core_uobject.LinearColor: ...
    def Conv_Vector2DToVector(self, InVector2D: core_uobject.Vector2D, Z: float, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def Conv_RotatorToVector(self, InRot: core_uobject.Rotator, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def Conv_LinearColorToVector(self, InLinearColor: core_uobject.LinearColor, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def Conv_LinearColorToColor(self, InLinearColor: core_uobject.LinearColor, ReturnValue: core_uobject.Color) -> core_uobject.Color: ...
    def Conv_IntVectorToVector(self, InIntVector: core_uobject.IntVector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def Conv_IntToIntVector(self, inInt: int, ReturnValue: core_uobject.IntVector) -> core_uobject.IntVector: ...
    def Conv_IntToFloat(self, inInt: int, ReturnValue: float) -> float: ...
    def Conv_IntToByte(self, inInt: int, ReturnValue: int) -> int: ...
    def Conv_IntToBool(self, inInt: int, ReturnValue: bool) -> bool: ...
    def Conv_FloatToVector(self, InFloat: float, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def Conv_FloatToLinearColor(self, InFloat: float, ReturnValue: core_uobject.LinearColor) -> core_uobject.LinearColor: ...
    def Conv_ColorToLinearColor(self, InColor: core_uobject.Color, ReturnValue: core_uobject.LinearColor) -> core_uobject.LinearColor: ...
    def Conv_ByteToInt(self, InByte: int, ReturnValue: int) -> int: ...
    def Conv_ByteToFloat(self, InByte: int, ReturnValue: float) -> float: ...
    def Conv_BoolToInt(self, InBool: bool, ReturnValue: int) -> int: ...
    def Conv_BoolToFloat(self, InBool: bool, ReturnValue: float) -> float: ...
    def Conv_BoolToByte(self, InBool: bool, ReturnValue: int) -> int: ...
    def ComposeTransforms(self, A: core_uobject.Transform, B: core_uobject.Transform, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def ComposeRotators(self, A: core_uobject.Rotator, B: core_uobject.Rotator, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def ClassIsChildOf(self, TestClass: unreal.UClass, ParentClass: unreal.UClass, ReturnValue: bool) -> bool: ...
    def ClampVectorSize(self, A: core_uobject.Vector, Min: float, Max: float, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def ClampAxis(self, Angle: float, ReturnValue: float) -> float: ...
    def ClampAngle(self, AngleDegrees: float, MinAngleDegrees: float, MaxAngleDegrees: float, ReturnValue: float) -> float: ...
    def Clamp(self, Value: int, Min: int, Max: int, ReturnValue: int) -> int: ...
    def CInterpTo(self, Current: core_uobject.LinearColor, Target: core_uobject.LinearColor, DeltaTime: float, InterpSpeed: float, ReturnValue: core_uobject.LinearColor) -> core_uobject.LinearColor: ...
    def BreakVector2D(self, InVec: core_uobject.Vector2D, X: float, Y: float): ...
    def BreakVector(self, InVec: core_uobject.Vector, X: float, Y: float, Z: float): ...
    def BreakTransform(self, InTransform: core_uobject.Transform, Location: core_uobject.Vector, Rotation: core_uobject.Rotator, Scale: core_uobject.Vector): ...
    def BreakTimespan2(self, InTimespan: core_uobject.Timespan, Days: int, Hours: int, Minutes: int, Seconds: int, FractionNano: int): ...
    def BreakTimespan(self, InTimespan: core_uobject.Timespan, Days: int, Hours: int, Minutes: int, Seconds: int, Milliseconds: int): ...
    def BreakRotIntoAxes(self, InRot: core_uobject.Rotator, X: core_uobject.Vector, Y: core_uobject.Vector, Z: core_uobject.Vector): ...
    def BreakRotator(self, InRot: core_uobject.Rotator, Roll: float, Pitch: float, Yaw: float): ...
    def BreakRandomStream(self, InRandomStream: core_uobject.RandomStream, InitialSeed: int): ...
    def BreakDateTime(self, InDateTime: core_uobject.DateTime, Year: int, Month: int, Day: int, Hour: int, Minute: int, Second: int, Millisecond: int): ...
    def BreakColor(self, InColor: core_uobject.LinearColor, R: float, G: float, B: float, A: float): ...
    def BooleanXOR(self, A: bool, B: bool, ReturnValue: bool) -> bool: ...
    def BooleanOR(self, A: bool, B: bool, ReturnValue: bool) -> bool: ...
    def BooleanNOR(self, A: bool, B: bool, ReturnValue: bool) -> bool: ...
    def BooleanNAND(self, A: bool, B: bool, ReturnValue: bool) -> bool: ...
    def BooleanAND(self, A: bool, B: bool, ReturnValue: bool) -> bool: ...
    def BMin(self, A: int, B: int, ReturnValue: int) -> int: ...
    def BMax(self, A: int, B: int, ReturnValue: int) -> int: ...
    def Atan2(self, A: float, B: float, ReturnValue: float) -> float: ...
    def Atan(self, A: float, ReturnValue: float) -> float: ...
    def Asin(self, A: float, ReturnValue: float) -> float: ...
    def And_IntInt(self, A: int, B: int, ReturnValue: int) -> int: ...
    def Add_VectorVector(self, A: core_uobject.Vector, B: core_uobject.Vector, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def Add_VectorInt(self, A: core_uobject.Vector, B: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def Add_VectorFloat(self, A: core_uobject.Vector, B: float, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def Add_Vector2DVector2D(self, A: core_uobject.Vector2D, B: core_uobject.Vector2D, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def Add_Vector2DFloat(self, A: core_uobject.Vector2D, B: float, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def Add_TimespanTimespan(self, A: core_uobject.Timespan, B: core_uobject.Timespan, ReturnValue: core_uobject.Timespan) -> core_uobject.Timespan: ...
    def Add_IntInt(self, A: int, B: int, ReturnValue: int) -> int: ...
    def Add_FloatFloat(self, A: float, B: float, ReturnValue: float) -> float: ...
    def Add_DateTimeTimespan(self, A: core_uobject.DateTime, B: core_uobject.Timespan, ReturnValue: core_uobject.DateTime) -> core_uobject.DateTime: ...
    def Add_ByteByte(self, A: int, B: int, ReturnValue: int) -> int: ...
    def Acos(self, A: float, ReturnValue: float) -> float: ...
    def Abs_Int(self, A: int, ReturnValue: int) -> int: ...
    def Abs(self, A: float, ReturnValue: float) -> float: ...


class KismetNodeHelperLibrary(BlueprintFunctionLibrary):

    def MarkBit(self, Data: int, Index: int): ...
    def HasUnmarkedBit(self, Data: int, NumBits: int, ReturnValue: bool) -> bool: ...
    def HasMarkedBit(self, Data: int, NumBits: int, ReturnValue: bool) -> bool: ...
    def GetValidValue(self, Enum: unreal.UEnum, EnumeratorValue: int, ReturnValue: int) -> int: ...
    def GetUnmarkedBit(self, Data: int, StartIdx: int, NumBits: int, bRandom: bool, ReturnValue: int) -> int: ...
    def GetRandomUnmarkedBit(self, Data: int, StartIdx: int, NumBits: int, ReturnValue: int) -> int: ...
    def GetFirstUnmarkedBit(self, Data: int, StartIdx: int, NumBits: int, ReturnValue: int) -> int: ...
    def GetEnumeratorValueFromIndex(self, Enum: unreal.UEnum, EnumeratorIndex: int, ReturnValue: int) -> int: ...
    def GetEnumeratorUserFriendlyName(self, Enum: unreal.UEnum, EnumeratorValue: int, ReturnValue: str) -> str: ...
    def GetEnumeratorName(self, Enum: unreal.UEnum, EnumeratorValue: int, ReturnValue: str) -> str: ...
    def ClearBit(self, Data: int, Index: int): ...
    def ClearAllBits(self, Data: int): ...
    def BitIsMarked(self, Data: int, Index: int, ReturnValue: bool) -> bool: ...


class KismetRenderingLibrary(BlueprintFunctionLibrary):

    def RenderTargetCreateStaticTexture2DEditorOnly(self, RenderTarget: TextureRenderTarget2D, Name: str, CompressionSettings: int, MipSettings: int, ReturnValue: Texture2D) -> Texture2D: ...
    def ReleaseRenderTarget2D(self, TextureRenderTarget: TextureRenderTarget2D): ...
    def ReadRenderTargetUV(self, WorldContextObject: unreal.UObject, TextureRenderTarget: TextureRenderTarget2D, U: float, V: float, ReturnValue: core_uobject.Color) -> core_uobject.Color: ...
    def ReadRenderTargetRawUV(self, WorldContextObject: unreal.UObject, TextureRenderTarget: TextureRenderTarget2D, U: float, V: float, ReturnValue: core_uobject.LinearColor) -> core_uobject.LinearColor: ...
    def ReadRenderTargetRawPixel(self, WorldContextObject: unreal.UObject, TextureRenderTarget: TextureRenderTarget2D, X: int, Y: int, ReturnValue: core_uobject.LinearColor) -> core_uobject.LinearColor: ...
    def ReadRenderTargetPixel(self, WorldContextObject: unreal.UObject, TextureRenderTarget: TextureRenderTarget2D, X: int, Y: int, ReturnValue: core_uobject.Color) -> core_uobject.Color: ...
    def ImportFileAsTexture2D(self, WorldContextObject: unreal.UObject, Filename: str, ReturnValue: Texture2D) -> Texture2D: ...
    def ExportTexture2D(self, WorldContextObject: unreal.UObject, Texture: Texture2D, FilePath: str, Filename: str): ...
    def ExportRenderTarget(self, WorldContextObject: unreal.UObject, TextureRenderTarget: TextureRenderTarget2D, FilePath: str, Filename: str): ...
    def EndDrawCanvasToRenderTarget(self, WorldContextObject: unreal.UObject, Context: DrawToRenderTargetContext): ...
    def DrawMaterialToRenderTarget(self, WorldContextObject: unreal.UObject, TextureRenderTarget: TextureRenderTarget2D, Material: MaterialInterface, bForceSetSceneRenderTargets: bool): ...
    def CreateRenderTarget2D(self, WorldContextObject: unreal.UObject, Width: int, Height: int, Format: int, ReturnValue: TextureRenderTarget2D) -> TextureRenderTarget2D: ...
    def ConvertRenderTargetToTexture2DEditorOnly(self, WorldContextObject: unreal.UObject, RenderTarget: TextureRenderTarget2D, Texture: Texture2D): ...
    def ClearRenderTarget2D(self, WorldContextObject: unreal.UObject, TextureRenderTarget: TextureRenderTarget2D, ClearColor: core_uobject.LinearColor): ...
    def BeginDrawCanvasToRenderTarget(self, WorldContextObject: unreal.UObject, TextureRenderTarget: TextureRenderTarget2D, Canvas: Canvas, Size: core_uobject.Vector2D, Context: DrawToRenderTargetContext): ...


class KismetStringLibrary(BlueprintFunctionLibrary):

    def TrimTrailing(self, SourceString: str, ReturnValue: str) -> str: ...
    def Trim(self, SourceString: str, ReturnValue: str) -> str: ...
    def ToUpper(self, SourceString: str, ReturnValue: str) -> str: ...
    def ToLower(self, SourceString: str, ReturnValue: str) -> str: ...
    def TimeSecondsToString(self, InSeconds: float, ReturnValue: str) -> str: ...
    def StartsWith(self, SourceString: str, InPrefix: str, SearchCase: int, ReturnValue: bool) -> bool: ...
    def Split(self, SourceString: str, InStr: str, LeftS: str, RightS: str, SearchCase: int, SearchDir: int, ReturnValue: bool) -> bool: ...
    def RightPad(self, SourceString: str, ChCount: int, ReturnValue: str) -> str: ...
    def RightChop(self, SourceString: str, Count: int, ReturnValue: str) -> str: ...
    def Right(self, SourceString: str, Count: int, ReturnValue: str) -> str: ...
    def Reverse(self, SourceString: str, ReturnValue: str) -> str: ...
    def ReplaceInline(self, SourceString: str, SearchText: str, ReplacementText: str, SearchCase: int, ReturnValue: int) -> int: ...
    def Replace(self, SourceString: str, From: str, To: str, SearchCase: int, ReturnValue: str) -> str: ...
    def ParseIntoArray(self, SourceString: str, Delimiter: str, CullEmptyStrings: bool, ReturnValue: unreal.WrappedArray[str]) -> unreal.WrappedArray[str]: ...
    def NotEqual_StrStr(self, A: str, B: str, ReturnValue: bool) -> bool: ...
    def NotEqual_StriStri(self, A: str, B: str, ReturnValue: bool) -> bool: ...
    def Mid(self, SourceString: str, Start: int, Count: int, ReturnValue: str) -> str: ...
    def MatchesWildcard(self, SourceString: str, Wildcard: str, SearchCase: int, ReturnValue: bool) -> bool: ...
    def Len(self, S: str, ReturnValue: int) -> int: ...
    def LeftPad(self, SourceString: str, ChCount: int, ReturnValue: str) -> str: ...
    def LeftChop(self, SourceString: str, Count: int, ReturnValue: str) -> str: ...
    def Left(self, SourceString: str, Count: int, ReturnValue: str) -> str: ...
    def JoinStringArray(self, SourceArray: unreal.WrappedArray[str], Separator: str, ReturnValue: str) -> str: ...
    def IsNumeric(self, SourceString: str, ReturnValue: bool) -> bool: ...
    def GetSubstring(self, SourceString: str, StartIndex: int, Length: int, ReturnValue: str) -> str: ...
    def GetCharacterAsNumber(self, SourceString: str, Index: int, ReturnValue: int) -> int: ...
    def GetCharacterArrayFromString(self, SourceString: str, ReturnValue: unreal.WrappedArray[str]) -> unreal.WrappedArray[str]: ...
    def FindSubstring(self, SearchIn: str, Substring: str, bUseCase: bool, bSearchFromEnd: bool, StartPosition: int, ReturnValue: int) -> int: ...
    def EqualEqual_StrStr(self, A: str, B: str, ReturnValue: bool) -> bool: ...
    def EqualEqual_StriStri(self, A: str, B: str, ReturnValue: bool) -> bool: ...
    def EndsWith(self, SourceString: str, InSuffix: str, SearchCase: int, ReturnValue: bool) -> bool: ...
    def CullArray(self, SourceString: str, inArray: unreal.WrappedArray[str], ReturnValue: int) -> int: ...
    def Conv_VectorToString(self, InVec: core_uobject.Vector, ReturnValue: str) -> str: ...
    def Conv_Vector2dToString(self, InVec: core_uobject.Vector2D, ReturnValue: str) -> str: ...
    def Conv_TransformToString(self, InTrans: core_uobject.Transform, ReturnValue: str) -> str: ...
    def Conv_StringToVector2D(self, inString: str, OutConvertedVector2D: core_uobject.Vector2D, OutIsValid: bool): ...
    def Conv_StringToVector(self, inString: str, OutConvertedVector: core_uobject.Vector, OutIsValid: bool): ...
    def Conv_StringToRotator(self, inString: str, OutConvertedRotator: core_uobject.Rotator, OutIsValid: bool): ...
    def Conv_StringToName(self, inString: str, ReturnValue: str) -> str: ...
    def Conv_StringToInt(self, inString: str, ReturnValue: int) -> int: ...
    def Conv_StringToFloat(self, inString: str, ReturnValue: float) -> float: ...
    def Conv_StringToColor(self, inString: str, OutConvertedColor: core_uobject.LinearColor, OutIsValid: bool): ...
    def Conv_RotatorToString(self, InRot: core_uobject.Rotator, ReturnValue: str) -> str: ...
    def Conv_ObjectToString(self, InObj: unreal.UObject, ReturnValue: str) -> str: ...
    def Conv_NameToString(self, InName: str, ReturnValue: str) -> str: ...
    def Conv_IntVectorToString(self, InIntVec: core_uobject.IntVector, ReturnValue: str) -> str: ...
    def Conv_IntToString(self, inInt: int, ReturnValue: str) -> str: ...
    def Conv_FloatToString(self, InFloat: float, ReturnValue: str) -> str: ...
    def Conv_ColorToString(self, InColor: core_uobject.LinearColor, ReturnValue: str) -> str: ...
    def Conv_ByteToString(self, InByte: int, ReturnValue: str) -> str: ...
    def Conv_BoolToString(self, InBool: bool, ReturnValue: str) -> str: ...
    def Contains(self, SearchIn: str, Substring: str, bUseCase: bool, bSearchFromEnd: bool, ReturnValue: bool) -> bool: ...
    def Concat_StrStr(self, A: str, B: str, ReturnValue: str) -> str: ...
    def BuildString_Vector2d(self, AppendTo: str, Prefix: str, InVector2D: core_uobject.Vector2D, Suffix: str, ReturnValue: str) -> str: ...
    def BuildString_Vector(self, AppendTo: str, Prefix: str, InVector: core_uobject.Vector, Suffix: str, ReturnValue: str) -> str: ...
    def BuildString_Rotator(self, AppendTo: str, Prefix: str, InRot: core_uobject.Rotator, Suffix: str, ReturnValue: str) -> str: ...
    def BuildString_Object(self, AppendTo: str, Prefix: str, InObj: unreal.UObject, Suffix: str, ReturnValue: str) -> str: ...
    def BuildString_Name(self, AppendTo: str, Prefix: str, InName: str, Suffix: str, ReturnValue: str) -> str: ...
    def BuildString_IntVector(self, AppendTo: str, Prefix: str, InIntVector: core_uobject.IntVector, Suffix: str, ReturnValue: str) -> str: ...
    def BuildString_Int(self, AppendTo: str, Prefix: str, inInt: int, Suffix: str, ReturnValue: str) -> str: ...
    def BuildString_Float(self, AppendTo: str, Prefix: str, InFloat: float, Suffix: str, ReturnValue: str) -> str: ...
    def BuildString_Color(self, AppendTo: str, Prefix: str, InColor: core_uobject.LinearColor, Suffix: str, ReturnValue: str) -> str: ...
    def BuildString_Bool(self, AppendTo: str, Prefix: str, InBool: bool, Suffix: str, ReturnValue: str) -> str: ...


class KismetStringTableLibrary(BlueprintFunctionLibrary):

    def IsRegisteredTableId(self, TableId: str, ReturnValue: bool) -> bool: ...
    def IsRegisteredTableEntry(self, TableId: str, Key: str, ReturnValue: bool) -> bool: ...
    def GetTableNamespace(self, TableId: str, ReturnValue: str) -> str: ...
    def GetTableEntrySourceString(self, TableId: str, Key: str, ReturnValue: str) -> str: ...
    def GetTableEntryMetaData(self, TableId: str, Key: str, MetaDataId: str, ReturnValue: str) -> str: ...
    def GetRegisteredStringTables(self, ReturnValue: unreal.WrappedArray[str]) -> unreal.WrappedArray[str]: ...
    def GetMetaDataIdsFromStringTableEntry(self, TableId: str, Key: str, ReturnValue: unreal.WrappedArray[str]) -> unreal.WrappedArray[str]: ...
    def GetKeysFromStringTable(self, TableId: str, ReturnValue: unreal.WrappedArray[str]) -> unreal.WrappedArray[str]: ...


class KismetSystemLibrary(BlueprintFunctionLibrary):

    def UnregisterForRemoteNotifications(self): ...
    def UnloadPrimaryAssetList(self, PrimaryAssetIdList: unreal.WrappedArray[core_uobject.PrimaryAssetId]): ...
    def UnloadPrimaryAsset(self, PrimaryAssetId: core_uobject.PrimaryAssetId): ...
    def StackTrace(self): ...
    def SphereTraceSingleForObjects(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, Radius: float, ObjectTypes: unreal.WrappedArray[int], bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHit: HitResult, bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def SphereTraceSingleByProfile(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, Radius: float, ProfileName: str, bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHit: HitResult, bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def SphereTraceSingle(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, Radius: float, TraceChannel: int, bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHit: HitResult, bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def SphereTraceMultiForObjects(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, Radius: float, ObjectTypes: unreal.WrappedArray[int], bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHits: unreal.WrappedArray[HitResult], bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def SphereTraceMultiByProfile(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, Radius: float, ProfileName: str, bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHits: unreal.WrappedArray[HitResult], bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def SphereTraceMulti(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, Radius: float, TraceChannel: int, bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHits: unreal.WrappedArray[HitResult], bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def SphereOverlapComponents(self, WorldContextObject: unreal.UObject, SpherePos: core_uobject.Vector, SphereRadius: float, ObjectTypes: unreal.WrappedArray[int], ComponentClassFilter: unreal.UClass, ActorsToIgnore: unreal.WrappedArray[Actor], OutComponents: unreal.WrappedArray[PrimitiveComponent], ReturnValue: bool) -> bool: ...
    def SphereOverlapActors(self, WorldContextObject: unreal.UObject, SpherePos: core_uobject.Vector, SphereRadius: float, ObjectTypes: unreal.WrappedArray[int], ActorClassFilter: unreal.UClass, ActorsToIgnore: unreal.WrappedArray[Actor], OutActors: unreal.WrappedArray[Actor], ReturnValue: bool) -> bool: ...
    def ShowPlatformSpecificLeaderboardScreen(self, CategoryName: str): ...
    def ShowPlatformSpecificAchievementsScreen(self, SpecificPlayer: PlayerController): ...
    def ShowInterstitialAd(self): ...
    def ShowAdBanner(self, AdIdIndex: int, bShowOnBottomOfScreen: bool): ...
    def SetWindowTitle(self, Title: str): ...
    def SetVolumeButtonsHandledBySystem(self, bEnabled: bool): ...
    def SetVectorPropertyByName(self, Object: unreal.UObject, PropertyName: str, Value: core_uobject.Vector): ...
    def SetUserActivity(self, UserActivity: UserActivity): ...
    def SetTransformPropertyByName(self, Object: unreal.UObject, PropertyName: str, Value: core_uobject.Transform): ...
    def SetTextPropertyByName(self, Object: unreal.UObject, PropertyName: str, Value: str): ...
    def SetSuppressViewportTransitionMessage(self, WorldContextObject: unreal.UObject, bState: bool): ...
    def SetStructurePropertyByName(self, Object: unreal.UObject, PropertyName: str, Value: GenericStruct): ...
    def SetStringPropertyByName(self, Object: unreal.UObject, PropertyName: str, Value: str): ...
    def SetRotatorPropertyByName(self, Object: unreal.UObject, PropertyName: str, Value: core_uobject.Rotator): ...
    def SetObjectPropertyByName(self, Object: unreal.UObject, PropertyName: str, Value: unreal.UObject): ...
    def SetNamePropertyByName(self, Object: unreal.UObject, PropertyName: str, Value: str): ...
    def SetLinearColorPropertyByName(self, Object: unreal.UObject, PropertyName: str, Value: core_uobject.LinearColor): ...
    def SetIntPropertyByName(self, Object: unreal.UObject, PropertyName: str, Value: int): ...
    def SetFloatPropertyByName(self, Object: unreal.UObject, PropertyName: str, Value: float): ...
    def SetCollisionProfileNameProperty(self, Object: unreal.UObject, PropertyName: str, Value: CollisionProfileName): ...
    def SetClassPropertyByName(self, Object: unreal.UObject, PropertyName: str, Value: unreal.UClass): ...
    def SetBytePropertyByName(self, Object: unreal.UObject, PropertyName: str, Value: int): ...
    def SetBoolPropertyByName(self, Object: unreal.UObject, PropertyName: str, Value: bool): ...
    def RetriggerableDelay(self, WorldContextObject: unreal.UObject, Duration: float, LatentInfo: LatentActionInfo): ...
    def ResetGamepadAssignmentToController(self, ControllerId: int): ...
    def ResetGamepadAssignments(self): ...
    def RegisterForRemoteNotifications(self): ...
    def QuitGame(self, WorldContextObject: unreal.UObject, SpecificPlayer: PlayerController, QuitPreference: int): ...
    def PrintWarning(self, inString: str): ...
    def PrintText(self, WorldContextObject: unreal.UObject, InText: str, bPrintToScreen: bool, bPrintToLog: bool, TextColor: core_uobject.LinearColor, Duration: float): ...
    def PrintString(self, WorldContextObject: unreal.UObject, inString: str, bPrintToScreen: bool, bPrintToLog: bool, TextColor: core_uobject.LinearColor, Duration: float): ...
    def OnAssetLoaded__DelegateSignature(self, Loaded: unreal.UObject): ...
    def OnAssetClassLoaded__DelegateSignature(self, Loaded: unreal.UClass): ...
    def NotEqual_PrimaryAssetType(self, A: core_uobject.PrimaryAssetType, B: core_uobject.PrimaryAssetType, ReturnValue: bool) -> bool: ...
    def NotEqual_PrimaryAssetId(self, A: core_uobject.PrimaryAssetId, B: core_uobject.PrimaryAssetId, ReturnValue: bool) -> bool: ...
    def MoveComponentTo(self, Component: SceneComponent, TargetRelativeLocation: core_uobject.Vector, TargetRelativeRotation: core_uobject.Rotator, bEaseOut: bool, bEaseIn: bool, OverTime: float, bForceShortestRotationPath: bool, MoveAction: int, LatentInfo: LatentActionInfo): ...
    def MakeSoftObjectPath(self, PathString: str, ReturnValue: core_uobject.SoftObjectPath) -> core_uobject.SoftObjectPath: ...
    def MakeSoftClassPath(self, PathString: str, ReturnValue: core_uobject.SoftClassPath) -> core_uobject.SoftClassPath: ...
    def MakeLiteralText(self, Value: str, ReturnValue: str) -> str: ...
    def MakeLiteralString(self, Value: str, ReturnValue: str) -> str: ...
    def MakeLiteralName(self, Value: str, ReturnValue: str) -> str: ...
    def MakeLiteralInt(self, Value: int, ReturnValue: int) -> int: ...
    def MakeLiteralFloat(self, Value: float, ReturnValue: float) -> float: ...
    def MakeLiteralByte(self, Value: int, ReturnValue: int) -> int: ...
    def MakeLiteralBool(self, Value: bool, ReturnValue: bool) -> bool: ...
    def LoadInterstitialAd(self, AdIdIndex: int): ...
    def LineTraceSingleForObjects(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, ObjectTypes: unreal.WrappedArray[int], bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHit: HitResult, bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def LineTraceSingleByProfile(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, ProfileName: str, bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHit: HitResult, bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def LineTraceSingle(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, TraceChannel: int, bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHit: HitResult, bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def LineTraceMultiForObjects(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, ObjectTypes: unreal.WrappedArray[int], bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHits: unreal.WrappedArray[HitResult], bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def LineTraceMultiByProfile(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, ProfileName: str, bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHits: unreal.WrappedArray[HitResult], bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def LineTraceMulti(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, TraceChannel: int, bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHits: unreal.WrappedArray[HitResult], bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def LaunchURL(self, URL: str): ...
    def K2_UnPauseTimerHandle(self, WorldContextObject: unreal.UObject, Handle: TimerHandle): ...
    def K2_UnPauseTimer(self, Object: unreal.UObject, FunctionName: str): ...
    def K2_TimerExistsHandle(self, WorldContextObject: unreal.UObject, Handle: TimerHandle, ReturnValue: bool) -> bool: ...
    def K2_TimerExists(self, Object: unreal.UObject, FunctionName: str, ReturnValue: bool) -> bool: ...
    def K2_SetTimer(self, Object: unreal.UObject, FunctionName: str, Time: float, bLooping: bool, ReturnValue: TimerHandle) -> TimerHandle: ...
    def K2_PauseTimerHandle(self, WorldContextObject: unreal.UObject, Handle: TimerHandle): ...
    def K2_PauseTimer(self, Object: unreal.UObject, FunctionName: str): ...
    def K2_IsValidTimerHandle(self, Handle: TimerHandle, ReturnValue: bool) -> bool: ...
    def K2_IsTimerPausedHandle(self, WorldContextObject: unreal.UObject, Handle: TimerHandle, ReturnValue: bool) -> bool: ...
    def K2_IsTimerPaused(self, Object: unreal.UObject, FunctionName: str, ReturnValue: bool) -> bool: ...
    def K2_IsTimerActiveHandle(self, WorldContextObject: unreal.UObject, Handle: TimerHandle, ReturnValue: bool) -> bool: ...
    def K2_IsTimerActive(self, Object: unreal.UObject, FunctionName: str, ReturnValue: bool) -> bool: ...
    def K2_InvalidateTimerHandle(self, Handle: TimerHandle, ReturnValue: TimerHandle) -> TimerHandle: ...
    def K2_GetTimerRemainingTimeHandle(self, WorldContextObject: unreal.UObject, Handle: TimerHandle, ReturnValue: float) -> float: ...
    def K2_GetTimerRemainingTime(self, Object: unreal.UObject, FunctionName: str, ReturnValue: float) -> float: ...
    def K2_GetTimerElapsedTimeHandle(self, WorldContextObject: unreal.UObject, Handle: TimerHandle, ReturnValue: float) -> float: ...
    def K2_GetTimerElapsedTime(self, Object: unreal.UObject, FunctionName: str, ReturnValue: float) -> float: ...
    def K2_ClearTimerHandle(self, WorldContextObject: unreal.UObject, Handle: TimerHandle): ...
    def K2_ClearTimer(self, Object: unreal.UObject, FunctionName: str): ...
    def K2_ClearAndInvalidateTimerHandle(self, WorldContextObject: unreal.UObject, Handle: TimerHandle): ...
    def IsValidPrimaryAssetType(self, PrimaryAssetType: core_uobject.PrimaryAssetType, ReturnValue: bool) -> bool: ...
    def IsValidPrimaryAssetId(self, PrimaryAssetId: core_uobject.PrimaryAssetId, ReturnValue: bool) -> bool: ...
    def IsValidClass(self, Class: unreal.UClass, ReturnValue: bool) -> bool: ...
    def IsValid(self, Object: unreal.UObject, ReturnValue: bool) -> bool: ...
    def IsStandalone(self, WorldContextObject: unreal.UObject, ReturnValue: bool) -> bool: ...
    def IsServer(self, WorldContextObject: unreal.UObject, ReturnValue: bool) -> bool: ...
    def IsPackagedForDistribution(self, ReturnValue: bool) -> bool: ...
    def IsLoggedIn(self, SpecificPlayer: PlayerController, ReturnValue: bool) -> bool: ...
    def IsInterstitialAdRequested(self, ReturnValue: bool) -> bool: ...
    def IsInterstitialAdAvailable(self, ReturnValue: bool) -> bool: ...
    def IsDedicatedServer(self, WorldContextObject: unreal.UObject, ReturnValue: bool) -> bool: ...
    def IsControllerAssignedToGamepad(self, ControllerId: int, ReturnValue: bool) -> bool: ...
    def HideAdBanner(self): ...
    def GetVolumeButtonsHandledBySystem(self, ReturnValue: bool) -> bool: ...
    def GetUniqueDeviceId(self, ReturnValue: str) -> str: ...
    def GetSupportedFullscreenResolutions(self, Resolutions: unreal.WrappedArray[core_uobject.IntPoint], ReturnValue: bool) -> bool: ...
    def GetRenderingMaterialQualityLevel(self, ReturnValue: int) -> int: ...
    def GetRenderingDetailMode(self, ReturnValue: int) -> int: ...
    def GetProjectSavedDirectory(self, ReturnValue: str) -> str: ...
    def GetProjectDirectory(self, ReturnValue: str) -> str: ...
    def GetProjectContentDirectory(self, ReturnValue: str) -> str: ...
    def GetPrimaryAssetsWithBundleState(self, RequiredBundles: unreal.WrappedArray[str], ExcludedBundles: unreal.WrappedArray[str], ValidTypes: unreal.WrappedArray[core_uobject.PrimaryAssetType], bForceCurrentState: bool, OutPrimaryAssetIdList: unreal.WrappedArray[core_uobject.PrimaryAssetId]): ...
    def GetPrimaryAssetIdList(self, PrimaryAssetType: core_uobject.PrimaryAssetType, OutPrimaryAssetIdList: unreal.WrappedArray[core_uobject.PrimaryAssetId]): ...
    def GetPrimaryAssetIdFromObject(self, Object: unreal.UObject, ReturnValue: core_uobject.PrimaryAssetId) -> core_uobject.PrimaryAssetId: ...
    def GetPrimaryAssetIdFromClass(self, Class: unreal.UClass, ReturnValue: core_uobject.PrimaryAssetId) -> core_uobject.PrimaryAssetId: ...
    def GetPreferredLanguages(self, ReturnValue: unreal.WrappedArray[str]) -> unreal.WrappedArray[str]: ...
    def GetPlatformUserName(self, ReturnValue: str) -> str: ...
    def GetPathName(self, Object: unreal.UObject, ReturnValue: str) -> str: ...
    def GetObjectName(self, Object: unreal.UObject, ReturnValue: str) -> str: ...
    def GetObjectFromPrimaryAssetId(self, PrimaryAssetId: core_uobject.PrimaryAssetId, ReturnValue: unreal.UObject) -> unreal.UObject: ...
    def GetMinYResolutionForUI(self, ReturnValue: int) -> int: ...
    def GetMinYResolutionFor3DView(self, ReturnValue: int) -> int: ...
    def GetLocalCurrencySymbol(self, ReturnValue: str) -> str: ...
    def GetLocalCurrencyCode(self, ReturnValue: str) -> str: ...
    def GetGameTimeInSeconds(self, WorldContextObject: unreal.UObject, ReturnValue: float) -> float: ...
    def GetGameName(self, ReturnValue: str) -> str: ...
    def GetGameBundleId(self, ReturnValue: str) -> str: ...
    def GetEngineVersion(self, ReturnValue: str) -> str: ...
    def GetDisplayName(self, Object: unreal.UObject, ReturnValue: str) -> str: ...
    def GetDeviceId(self, ReturnValue: str) -> str: ...
    def GetDefaultLocale(self, ReturnValue: str) -> str: ...
    def GetDefaultLanguage(self, ReturnValue: str) -> str: ...
    def GetCurrentBundleState(self, PrimaryAssetId: core_uobject.PrimaryAssetId, bForceCurrentState: bool, OutBundles: unreal.WrappedArray[str], ReturnValue: bool) -> bool: ...
    def GetConvenientWindowedResolutions(self, Resolutions: unreal.WrappedArray[core_uobject.IntPoint], ReturnValue: bool) -> bool: ...
    def GetConsoleVariableIntValue(self, WorldContextObject: unreal.UObject, VariableName: str, ReturnValue: int) -> int: ...
    def GetConsoleVariableFloatValue(self, WorldContextObject: unreal.UObject, VariableName: str, ReturnValue: float) -> float: ...
    def GetComponentBounds(self, Component: SceneComponent, Origin: core_uobject.Vector, BoxExtent: core_uobject.Vector, SphereRadius: float): ...
    def GetCommandLine(self, ReturnValue: str) -> str: ...
    def GetClassFromPrimaryAssetId(self, PrimaryAssetId: core_uobject.PrimaryAssetId, ReturnValue: unreal.UClass) -> unreal.UClass: ...
    def GetClassDisplayName(self, Class: unreal.UClass, ReturnValue: str) -> str: ...
    def GetAdIDCount(self, ReturnValue: int) -> int: ...
    def GetActorListFromComponentList(self, ComponentList: unreal.WrappedArray[PrimitiveComponent], ActorClassFilter: unreal.UClass, OutActorList: unreal.WrappedArray[Actor]): ...
    def GetActorBounds(self, Actor: Actor, Origin: core_uobject.Vector, BoxExtent: core_uobject.Vector): ...
    def ForceCloseAdBanner(self): ...
    def FlushPersistentDebugLines(self, WorldContextObject: unreal.UObject): ...
    def FlushDebugStrings(self, WorldContextObject: unreal.UObject): ...
    def ExecuteConsoleCommand(self, WorldContextObject: unreal.UObject, Command: str, SpecificPlayer: PlayerController): ...
    def EqualEqual_PrimaryAssetType(self, A: core_uobject.PrimaryAssetType, B: core_uobject.PrimaryAssetType, ReturnValue: bool) -> bool: ...
    def EqualEqual_PrimaryAssetId(self, A: core_uobject.PrimaryAssetId, B: core_uobject.PrimaryAssetId, ReturnValue: bool) -> bool: ...
    def DrawDebugString(self, WorldContextObject: unreal.UObject, TextLocation: core_uobject.Vector, Text: str, TestBaseActor: Actor, TextColor: core_uobject.LinearColor, Duration: float): ...
    def DrawDebugSphere(self, WorldContextObject: unreal.UObject, Center: core_uobject.Vector, Radius: float, Segments: int, LineColor: core_uobject.LinearColor, Duration: float, Thickness: float): ...
    def DrawDebugPoint(self, WorldContextObject: unreal.UObject, Position: core_uobject.Vector, Size: float, PointColor: core_uobject.LinearColor, Duration: float): ...
    def DrawDebugPlane(self, WorldContextObject: unreal.UObject, PlaneCoordinates: core_uobject.Plane, Location: core_uobject.Vector, Size: float, PlaneColor: core_uobject.LinearColor, Duration: float): ...
    def DrawDebugLine(self, WorldContextObject: unreal.UObject, LineStart: core_uobject.Vector, LineEnd: core_uobject.Vector, LineColor: core_uobject.LinearColor, Duration: float, Thickness: float): ...
    def DrawDebugFrustum(self, WorldContextObject: unreal.UObject, FrustumTransform: core_uobject.Transform, FrustumColor: core_uobject.LinearColor, Duration: float, Thickness: float): ...
    def DrawDebugFloatHistoryTransform(self, WorldContextObject: unreal.UObject, FloatHistory: DebugFloatHistory, DrawTransform: core_uobject.Transform, DrawSize: core_uobject.Vector2D, DrawColor: core_uobject.LinearColor, Duration: float): ...
    def DrawDebugFloatHistoryLocation(self, WorldContextObject: unreal.UObject, FloatHistory: DebugFloatHistory, DrawLocation: core_uobject.Vector, DrawSize: core_uobject.Vector2D, DrawColor: core_uobject.LinearColor, Duration: float): ...
    def DrawDebugCylinder(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, Radius: float, Segments: int, LineColor: core_uobject.LinearColor, Duration: float, Thickness: float): ...
    def DrawDebugCoordinateSystem(self, WorldContextObject: unreal.UObject, AxisLoc: core_uobject.Vector, AxisRot: core_uobject.Rotator, Scale: float, Duration: float, Thickness: float): ...
    def DrawDebugConeInDegrees(self, WorldContextObject: unreal.UObject, Origin: core_uobject.Vector, Direction: core_uobject.Vector, Length: float, AngleWidth: float, AngleHeight: float, NumSides: int, LineColor: core_uobject.LinearColor, Duration: float, Thickness: float): ...
    def DrawDebugCone(self, WorldContextObject: unreal.UObject, Origin: core_uobject.Vector, Direction: core_uobject.Vector, Length: float, AngleWidth: float, AngleHeight: float, NumSides: int, LineColor: core_uobject.LinearColor, Duration: float, Thickness: float): ...
    def DrawDebugCircle(self, WorldContextObject: unreal.UObject, Center: core_uobject.Vector, Radius: float, NumSegments: int, LineColor: core_uobject.LinearColor, Duration: float, Thickness: float, YAxis: core_uobject.Vector, ZAxis: core_uobject.Vector, bDrawAxis: bool): ...
    def DrawDebugCapsule(self, WorldContextObject: unreal.UObject, Center: core_uobject.Vector, HalfHeight: float, Radius: float, Rotation: core_uobject.Rotator, LineColor: core_uobject.LinearColor, Duration: float, Thickness: float): ...
    def DrawDebugCamera(self, CameraActor: CameraActor, CameraColor: core_uobject.LinearColor, Duration: float): ...
    def DrawDebugBox(self, WorldContextObject: unreal.UObject, Center: core_uobject.Vector, Extent: core_uobject.Vector, LineColor: core_uobject.LinearColor, Rotation: core_uobject.Rotator, Duration: float, Thickness: float): ...
    def DrawDebugArrow(self, WorldContextObject: unreal.UObject, LineStart: core_uobject.Vector, LineEnd: core_uobject.Vector, ArrowSize: float, LineColor: core_uobject.LinearColor, Duration: float, Thickness: float): ...
    def DoesImplementInterface(self, TestObject: unreal.UObject, Interface: unreal.UClass, ReturnValue: bool) -> bool: ...
    def Delay(self, WorldContextObject: unreal.UObject, Duration: float, LatentInfo: LatentActionInfo): ...
    def CreateCopyForUndoBuffer(self, ObjectToModify: unreal.UObject): ...
    def Conv_PrimaryAssetTypeToString(self, PrimaryAssetType: core_uobject.PrimaryAssetType, ReturnValue: str) -> str: ...
    def Conv_PrimaryAssetIdToString(self, PrimaryAssetId: core_uobject.PrimaryAssetId, ReturnValue: str) -> str: ...
    def ControlScreensaver(self, bAllowScreenSaver: bool): ...
    def ComponentOverlapComponents(self, Component: PrimitiveComponent, ComponentTransform: core_uobject.Transform, ObjectTypes: unreal.WrappedArray[int], ComponentClassFilter: unreal.UClass, ActorsToIgnore: unreal.WrappedArray[Actor], OutComponents: unreal.WrappedArray[PrimitiveComponent], ReturnValue: bool) -> bool: ...
    def ComponentOverlapActors(self, Component: PrimitiveComponent, ComponentTransform: core_uobject.Transform, ObjectTypes: unreal.WrappedArray[int], ActorClassFilter: unreal.UClass, ActorsToIgnore: unreal.WrappedArray[Actor], OutActors: unreal.WrappedArray[Actor], ReturnValue: bool) -> bool: ...
    def CollectGarbage(self): ...
    def CapsuleTraceSingleForObjects(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, Radius: float, HalfHeight: float, ObjectTypes: unreal.WrappedArray[int], bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHit: HitResult, bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def CapsuleTraceSingleByProfile(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, Radius: float, HalfHeight: float, ProfileName: str, bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHit: HitResult, bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def CapsuleTraceSingle(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, Radius: float, HalfHeight: float, TraceChannel: int, bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHit: HitResult, bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def CapsuleTraceMultiForObjects(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, Radius: float, HalfHeight: float, ObjectTypes: unreal.WrappedArray[int], bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHits: unreal.WrappedArray[HitResult], bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def CapsuleTraceMultiByProfile(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, Radius: float, HalfHeight: float, ProfileName: str, bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHits: unreal.WrappedArray[HitResult], bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def CapsuleTraceMulti(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, Radius: float, HalfHeight: float, TraceChannel: int, bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHits: unreal.WrappedArray[HitResult], bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def CapsuleOverlapComponents(self, WorldContextObject: unreal.UObject, CapsulePos: core_uobject.Vector, Radius: float, HalfHeight: float, ObjectTypes: unreal.WrappedArray[int], ComponentClassFilter: unreal.UClass, ActorsToIgnore: unreal.WrappedArray[Actor], OutComponents: unreal.WrappedArray[PrimitiveComponent], ReturnValue: bool) -> bool: ...
    def CapsuleOverlapActors(self, WorldContextObject: unreal.UObject, CapsulePos: core_uobject.Vector, Radius: float, HalfHeight: float, ObjectTypes: unreal.WrappedArray[int], ActorClassFilter: unreal.UClass, ActorsToIgnore: unreal.WrappedArray[Actor], OutActors: unreal.WrappedArray[Actor], ReturnValue: bool) -> bool: ...
    def CanLaunchURL(self, URL: str, ReturnValue: bool) -> bool: ...
    def BreakSoftObjectPath(self, InSoftObjectPath: core_uobject.SoftObjectPath, PathString: str): ...
    def BreakSoftClassPath(self, InSoftClassPath: core_uobject.SoftClassPath, PathString: str): ...
    def BoxTraceSingleForObjects(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, HalfSize: core_uobject.Vector, Orientation: core_uobject.Rotator, ObjectTypes: unreal.WrappedArray[int], bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHit: HitResult, bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def BoxTraceSingleByProfile(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, HalfSize: core_uobject.Vector, Orientation: core_uobject.Rotator, ProfileName: str, bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHit: HitResult, bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def BoxTraceSingle(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, HalfSize: core_uobject.Vector, Orientation: core_uobject.Rotator, TraceChannel: int, bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHit: HitResult, bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def BoxTraceMultiForObjects(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, HalfSize: core_uobject.Vector, Orientation: core_uobject.Rotator, ObjectTypes: unreal.WrappedArray[int], bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHits: unreal.WrappedArray[HitResult], bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def BoxTraceMultiByProfile(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, HalfSize: core_uobject.Vector, Orientation: core_uobject.Rotator, ProfileName: str, bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHits: unreal.WrappedArray[HitResult], bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def BoxTraceMulti(self, WorldContextObject: unreal.UObject, Start: core_uobject.Vector, End: core_uobject.Vector, HalfSize: core_uobject.Vector, Orientation: core_uobject.Rotator, TraceChannel: int, bTraceComplex: bool, ActorsToIgnore: unreal.WrappedArray[Actor], DrawDebugType: int, OutHits: unreal.WrappedArray[HitResult], bIgnoreSelf: bool, TraceColor: core_uobject.LinearColor, TraceHitColor: core_uobject.LinearColor, DrawTime: float, ReturnValue: bool) -> bool: ...
    def BoxOverlapComponents(self, WorldContextObject: unreal.UObject, BoxPos: core_uobject.Vector, Extent: core_uobject.Vector, ObjectTypes: unreal.WrappedArray[int], ComponentClassFilter: unreal.UClass, ActorsToIgnore: unreal.WrappedArray[Actor], OutComponents: unreal.WrappedArray[PrimitiveComponent], ReturnValue: bool) -> bool: ...
    def BoxOverlapActors(self, WorldContextObject: unreal.UObject, BoxPos: core_uobject.Vector, BoxExtent: core_uobject.Vector, ObjectTypes: unreal.WrappedArray[int], ActorClassFilter: unreal.UClass, ActorsToIgnore: unreal.WrappedArray[Actor], OutActors: unreal.WrappedArray[Actor], ReturnValue: bool) -> bool: ...
    def AddFloatHistorySample(self, Value: float, FloatHistory: DebugFloatHistory, ReturnValue: DebugFloatHistory) -> DebugFloatHistory: ...


class KismetTextLibrary(BlueprintFunctionLibrary):

    def TextTrimTrailing(self, InText: str, ReturnValue: str) -> str: ...
    def TextTrimPrecedingAndTrailing(self, InText: str, ReturnValue: str) -> str: ...
    def TextTrimPreceding(self, InText: str, ReturnValue: str) -> str: ...
    def TextToUpper(self, InText: str, ReturnValue: str) -> str: ...
    def TextToLower(self, InText: str, ReturnValue: str) -> str: ...
    def TextIsTransient(self, InText: str, ReturnValue: bool) -> bool: ...
    def TextIsFromStringTable(self, Text: str, ReturnValue: bool) -> bool: ...
    def TextIsEmpty(self, InText: str, ReturnValue: bool) -> bool: ...
    def TextIsCultureInvariant(self, InText: str, ReturnValue: bool) -> bool: ...
    def TextFromStringTable(self, TableId: str, Key: str, ReturnValue: str) -> str: ...
    def StringTableIdAndKeyFromText(self, Text: str, OutTableId: str, OutKey: str, ReturnValue: bool) -> bool: ...
    def PolyglotDataToText(self, PolyglotData: core_uobject.PolyglotTextData, ReturnValue: str) -> str: ...
    def NotEqual_TextText(self, A: str, B: str, ReturnValue: bool) -> bool: ...
    def NotEqual_IgnoreCase_TextText(self, A: str, B: str, ReturnValue: bool) -> bool: ...
    def IsPolyglotDataValid(self, PolyglotData: core_uobject.PolyglotTextData, IsValid: bool, ErrorMessage: str): ...
    def GetEmptyText(self, ReturnValue: str) -> str: ...
    def Format(self, InPattern: str, InArgs: unreal.WrappedArray[FormatArgumentData], ReturnValue: str) -> str: ...
    def FindTextInLocalizationTable(self, Namespace: str, Key: str, OutText: str, ReturnValue: bool) -> bool: ...
    def EqualEqual_TextText(self, A: str, B: str, ReturnValue: bool) -> bool: ...
    def EqualEqual_IgnoreCase_TextText(self, A: str, B: str, ReturnValue: bool) -> bool: ...
    def Conv_VectorToText(self, InVec: core_uobject.Vector, ReturnValue: str) -> str: ...
    def Conv_Vector2dToText(self, InVec: core_uobject.Vector2D, ReturnValue: str) -> str: ...
    def Conv_TransformToText(self, InTrans: core_uobject.Transform, ReturnValue: str) -> str: ...
    def Conv_TextToString(self, InText: str, ReturnValue: str) -> str: ...
    def Conv_StringToText(self, inString: str, ReturnValue: str) -> str: ...
    def Conv_RotatorToText(self, InRot: core_uobject.Rotator, ReturnValue: str) -> str: ...
    def Conv_ObjectToText(self, InObj: unreal.UObject, ReturnValue: str) -> str: ...
    def Conv_NameToText(self, InName: str, ReturnValue: str) -> str: ...
    def Conv_IntToText(self, Value: int, bAlwaysSign: bool, bUseGrouping: bool, MinimumIntegralDigits: int, MaximumIntegralDigits: int, ReturnValue: str) -> str: ...
    def Conv_FloatToText(self, Value: float, RoundingMode: int, bAlwaysSign: bool, bUseGrouping: bool, MinimumIntegralDigits: int, MaximumIntegralDigits: int, MinimumFractionalDigits: int, MaximumFractionalDigits: int, ReturnValue: str) -> str: ...
    def Conv_ColorToText(self, InColor: core_uobject.LinearColor, ReturnValue: str) -> str: ...
    def Conv_ByteToText(self, Value: int, ReturnValue: str) -> str: ...
    def Conv_BoolToText(self, InBool: bool, ReturnValue: str) -> str: ...
    def AsTimeZoneTime_DateTime(self, InDateTime: core_uobject.DateTime, InTimeZone: str, ReturnValue: str) -> str: ...
    def AsTimeZoneDateTime_DateTime(self, InDateTime: core_uobject.DateTime, InTimeZone: str, ReturnValue: str) -> str: ...
    def AsTimeZoneDate_DateTime(self, InDateTime: core_uobject.DateTime, InTimeZone: str, ReturnValue: str) -> str: ...
    def AsTimespan_Timespan(self, InTimespan: core_uobject.Timespan, ReturnValue: str) -> str: ...
    def AsTime_DateTime(self, In: core_uobject.DateTime, ReturnValue: str) -> str: ...
    def AsPercent_Float(self, Value: float, RoundingMode: int, bAlwaysSign: bool, bUseGrouping: bool, MinimumIntegralDigits: int, MaximumIntegralDigits: int, MinimumFractionalDigits: int, MaximumFractionalDigits: int, ReturnValue: str) -> str: ...
    def AsDateTime_DateTime(self, In: core_uobject.DateTime, ReturnValue: str) -> str: ...
    def AsDate_DateTime(self, InDateTime: core_uobject.DateTime, ReturnValue: str) -> str: ...
    def AsCurrencyBase(self, BaseValue: int, CurrencyCode: str, ReturnValue: str) -> str: ...
    def AsCurrency_Integer(self, Value: int, RoundingMode: int, bAlwaysSign: bool, bUseGrouping: bool, MinimumIntegralDigits: int, MaximumIntegralDigits: int, MinimumFractionalDigits: int, MaximumFractionalDigits: int, CurrencyCode: str, ReturnValue: str) -> str: ...
    def AsCurrency_Float(self, Value: float, RoundingMode: int, bAlwaysSign: bool, bUseGrouping: bool, MinimumIntegralDigits: int, MaximumIntegralDigits: int, MinimumFractionalDigits: int, MaximumFractionalDigits: int, CurrencyCode: str, ReturnValue: str) -> str: ...


class Layer(unreal.UObject):
    LayerName: str
    bIsVisible: bool
    ActorStats: unreal.WrappedArray[LayerActorStats]



class Level(unreal.UObject):
    OwningWorld: World
    Model: Model
    ModelComponents: unreal.WrappedArray[ModelComponent]
    ActorCluster: LevelActorContainer
    NumTextureStreamingUnbuiltComponents: int
    NumTextureStreamingDirtyResources: int
    LevelScriptActor: LevelScriptActor
    NavListStart: NavigationObjectBase
    NavListEnd: NavigationObjectBase
    NavDataChunks: unreal.WrappedArray[NavigationDataChunk]
    LightmapTotalSize: float
    ShadowmapTotalSize: float
    StaticNavigableGeometry: unreal.WrappedArray[core_uobject.Vector]
    StreamingTextureGuids: unreal.WrappedArray[core_uobject.Guid]
    bIsLightingScenario: bool
    LevelBuildDataId: core_uobject.Guid
    MapBuildData: MapBuildDataRegistry
    LightBuildLevelOffset: core_uobject.IntVector
    bTextureStreamingRotationChanged: bool
    bStaticComponentsRegisteredInStreamingManager: bool
    bIsVisible: bool
    WorldSettings: WorldSettings
    AssetUserData: unreal.WrappedArray[AssetUserData]
    DestroyedReplicatedStaticActors: unreal.WrappedArray[ReplicatedStaticActorDestructionInfo]
    StaticLightingLevelInfo_Build: StaticLightingLevelInfo
    StaticLightingLevelInfo_Current: StaticLightingLevelInfo



class LevelActorContainer(unreal.UObject):
    Actors: unreal.WrappedArray[Actor]



class LevelBounds(Actor):
    bAutoUpdateBounds: bool



class LevelScriptBlueprint(Blueprint): ...


class LevelStreamingAlwaysLoaded(LevelStreaming): ...


class LevelStreamingKismet(LevelStreaming):
    bInitiallyLoaded: bool
    bInitiallyVisible: bool
    def LoadLevelInstance(self, WorldContextObject: unreal.UObject, LevelName: str, Location: core_uobject.Vector, Rotation: core_uobject.Rotator, bOutSuccess: bool, ReturnValue: LevelStreamingKismet) -> LevelStreamingKismet: ...


class LevelStreamingPersistent(LevelStreaming): ...


class LevelStreamingVolume(Volume):
    StreamingLevelNames: unreal.WrappedArray[str]
    bEditorPreVisOnly: bool
    bDisabled: bool
    StreamingUsage: int



class LightmappedSurfaceCollection(unreal.UObject):
    SourceModel: Model
    Surfaces: unreal.WrappedArray[int]



class LightMapTexture2D(Texture2D): ...


class LightmassCharacterIndirectDetailVolume(Volume): ...


class LightmassImportanceVolume(Volume):
    bAffectsVolumetricLightMapCellRefinement: bool



class LightmassPortal(Actor):
    PortalComponent: LightmassPortalComponent



class LightmassPortalComponent(SceneComponent):
    PreviewBox: BoxComponent



class LightmassPrimitiveSettingsObject(unreal.UObject):
    LightmassSettings: LightmassPrimitiveSettings



class LineBatchComponent(PrimitiveComponent): ...


class LocalLightComponent(LightComponent):
    IntensityUnits: ELightUnits
    bForegroundLayer: bool
    DynamicShadowFadeStartDistance: float
    DynamicShadowFadeEndDistance: float
    Radius: float
    AttenuationRadius: float
    LightmassSettings: LightmassPointLightSettings
    def SetAttenuationRadius(self, NewRadius: float): ...
    def GetUnitsConversionFactor(self, SrcUnits: ELightUnits, TargetUnits: ELightUnits, CosHalfConeAngle: float, ReturnValue: float) -> float: ...


class LODActor(Actor):
    StaticMeshComponent: StaticMeshComponent
    Proxy: HLODProxy
    Key: str
    LODDrawDistance: float
    SubActors: unreal.WrappedArray[Actor]
    LODLevel: int
    CachedNumHLODLevels: int



class MapBuildDataRegistry(unreal.UObject):
    LevelLightingQuality: int



class Material(MaterialInterface):
    PhysMaterial: PhysicalMaterial
    Metallic: ScalarMaterialInput
    Specular: ScalarMaterialInput
    Normal: VectorMaterialInput
    MaterialDomain: int
    BlendMode: int
    DecalBlendMode: int
    MaterialDecalResponse: int
    ShadingModel: int
    bCastDynamicShadowAsMasked: bool
    bDisableNormalPreProcessing: bool
    bIgnoredByFXCoordinator: bool
    OpacityMaskClipValue: float
    WorldPositionOffset: VectorMaterialInput
    WorldDisplacement: VectorMaterialInput
    TessellationMultiplier: ScalarMaterialInput
    SubsurfaceColor: ColorMaterialInput
    ClearCoat: ScalarMaterialInput
    ClearCoatRoughness: ScalarMaterialInput
    AmbientOcclusion: ScalarMaterialInput
    Refraction: ScalarMaterialInput
    CustomizedUVs: Vector2MaterialInput
    CustomizedColors: Vector2MaterialInput
    MaterialAttributes: MaterialAttributesInput
    PixelDepthOffset: ScalarMaterialInput
    CustomDataGBX: ScalarMaterialInput
    bEnableSeparateTranslucency: bool
    bEnableMobileSeparateTranslucency: bool
    bEnableResponsiveAA: bool
    bScreenSpaceReflections: bool
    bContactShadows: bool
    TwoSided: bool
    bDisableEdgeDetection: bool
    bDisableDefaultVertexFactory: bool
    bShouldDoOuterEdge: bool
    bEnableWorldPositionOffset: bool
    bEnablePixelDepthOffset: bool
    bEnableRefraction: bool
    DitheredLODTransition: bool
    DitherOpacityMask: bool
    bAllowNegativeEmissiveColor: bool
    NumCustomizedUVs: int
    NumCustomizedColors: int
    GbxColorRemapLUTCategory: int
    TranslucencyLightingMode: int
    TranslucencyDirectionalLightingIntensity: float
    AllowTranslucentCustomDepthWrites: bool
    TranslucentShadowDensityScale: float
    TranslucentSelfShadowDensityScale: float
    TranslucentSelfShadowSecondDensityScale: float
    TranslucentSelfShadowSecondOpacity: float
    TranslucentBackscatteringExponent: float
    TranslucentMultipleScatteringExtinction: core_uobject.LinearColor
    TranslucentShadowStartOffset: float
    bDisableDepthTest: bool
    bWriteOnlyAlpha: bool
    bGenerateSphericalParticleNormals: bool
    bTangentSpaceNormal: bool
    bUseEmissiveForDynamicAreaLighting: bool
    bBlockGI: bool
    bUsedAsSpecialEngineMaterial: bool
    bUsedWithSkeletalMesh: bool
    bUsedWithEditorCompositing: bool
    bUsedWithParticleSprites: bool
    bUsedWithGPUParticleSprites: bool
    bUsedWithBeamTrails: bool
    bUsedWithMeshParticles: bool
    bUsedWithNiagaraSprites: bool
    bUsedWithNiagaraRibbons: bool
    bUsedWithNiagaraMeshParticles: bool
    bUsedWithGeometryCache: bool
    bUsedWithStaticLighting: bool
    bUsedWithMorphTargets: bool
    bUsedWithSplineMeshes: bool
    bUsedWithInstancedStaticMeshes: bool
    bUsedWithSkyEnvMap: bool
    bUsedWithClothing: bool
    bUsedWithUI: bool
    bUsedWithSkeletalMeshParticles: bool
    bUsedWithCables: bool
    bUsedWithVolumetricTranslucentShadow: bool
    bAutomaticallySetUsageInEditor: bool
    bFullyRough: bool
    bUseFullPrecision: bool
    bUseLightmapDirectionality: bool
    bUseHQForwardReflections: bool
    bUsePlanarForwardReflections: bool
    bNormalCurvatureToRoughness: bool
    D3D11TessellationMode: int
    bEnableCrackFreeDisplacement: bool
    bEnableAdaptiveTessellation: bool
    MaxDisplacement: float
    Wireframe: bool
    bOutputVelocityOnBasePass: bool
    SkipRenderingDepth: bool
    bShouldCompileDebug: bool
    bSkipRenderingGbxCustomData: bool
    bIgnoreCustomMask: bool
    bIgnoreCustomGlow: bool
    CustomIncludeFiles: unreal.WrappedArray[str]
    EditorX: int
    EditorY: int
    EditorPitch: int
    EditorYaw: int
    Expressions: unreal.WrappedArray[MaterialExpression]
    MaterialFunctionInfos: unreal.WrappedArray[MaterialFunctionInfo]
    MaterialParameterCollectionInfos: unreal.WrappedArray[MaterialParameterCollectionInfo]
    bCanMaskedBeAssumedOpaque: bool
    bIsMasked: bool
    bIsPreviewMaterial: bool
    bIsFunctionPreviewMaterial: bool
    bUseMaterialAttributes: bool
    bUseTranslucencyVertexFog: bool
    bComputeFogPerPixel: bool
    bAllowDevelopmentShaderCompile: bool
    bIsMaterialEditorStatsMaterial: bool
    BlendableLocation: int
    BlendablePriority: int
    BlendableOutputAlpha: bool
    RefractionMode: int
    RefractionDepthBias: float
    StateId: core_uobject.Guid
    CachedQualityLevelsUsed: unreal.WrappedArray[bool]
    ExpressionTextureReferences: unreal.WrappedArray[Texture]



class MaterialExpressionAbs(MaterialExpression):
    Input: ExpressionInput



class MaterialExpressionActorOrientation(MaterialExpression):
    AXIS: int



class MaterialExpressionActorPositionWS(MaterialExpression): ...


class MaterialExpressionAdd(MaterialExpression):
    A: ExpressionInput
    B: ExpressionInput
    ConstA: float
    ConstB: float



class MaterialExpressionAnd(MaterialExpression):
    A: ExpressionInput
    B: ExpressionInput



class MaterialExpressionAntialiasedTextureMask(MaterialExpressionTextureSampleParameter2D):
    Threshold: float
    Channel: int



class MaterialExpressionAppendVector(MaterialExpression):
    A: ExpressionInput
    B: ExpressionInput



class MaterialExpressionArccosine(MaterialExpression):
    Input: ExpressionInput



class MaterialExpressionArccosineFast(MaterialExpression):
    Input: ExpressionInput



class MaterialExpressionArcsine(MaterialExpression):
    Input: ExpressionInput



class MaterialExpressionArcsineFast(MaterialExpression):
    Input: ExpressionInput



class MaterialExpressionArctangent(MaterialExpression):
    Input: ExpressionInput



class MaterialExpressionArctangent2(MaterialExpression):
    Y: ExpressionInput
    X: ExpressionInput



class MaterialExpressionArctangent2Fast(MaterialExpression):
    Y: ExpressionInput
    X: ExpressionInput



class MaterialExpressionArctangentFast(MaterialExpression):
    Input: ExpressionInput



class MaterialExpressionAtmosphericFogColor(MaterialExpression):
    WorldPosition: ExpressionInput



class MaterialExpressionAtmosphericLightColor(MaterialExpression): ...


class MaterialExpressionAtmosphericLightVector(MaterialExpression): ...


class MaterialExpressionBentNormalCustomOutput(MaterialExpressionCustomOutput):
    Input: ExpressionInput



class MaterialExpressionBlackBody(MaterialExpression):
    Temp: ExpressionInput



class MaterialExpressionBlendMaterialAttributes(MaterialExpression):
    A: MaterialAttributesInput
    B: MaterialAttributesInput
    Alpha: ExpressionInput
    PixelAttributeBlendType: int
    VertexAttributeBlendType: int



class MaterialExpressionBreakMaterialAttributes(MaterialExpression):
    MaterialAttributes: MaterialAttributesInput



class MaterialExpressionBumpOffset(MaterialExpression):
    Coordinate: ExpressionInput
    Height: ExpressionInput
    HeightRatioInput: ExpressionInput
    HeightRatio: float
    ReferencePlane: float



class MaterialExpressionCameraPositionWS(MaterialExpression): ...


class MaterialExpressionCameraVectorWS(MaterialExpression): ...


class MaterialExpressionCeil(MaterialExpression):
    Input: ExpressionInput



class MaterialExpressionParameter(MaterialExpression):
    ParameterName: str
    ExpressionGUID: core_uobject.Guid
    Group: str



class MaterialExpressionVectorParameter(MaterialExpressionParameter):
    DefaultValue: core_uobject.LinearColor



class MaterialExpressionChannelMaskParameter(MaterialExpressionVectorParameter):
    MaskChannel: int
    Input: ExpressionInput



class MaterialExpressionChoose(MaterialExpression):
    Bool: ExpressionInput
    A: ExpressionInput
    B: ExpressionInput



class MaterialExpressionClamp(MaterialExpression):
    Input: ExpressionInput
    Min: ExpressionInput
    Max: ExpressionInput
    ClampMode: int
    MinDefault: float
    MaxDefault: float



class MaterialExpressionClearCoatNormalCustomOutput(MaterialExpressionCustomOutput):
    Input: ExpressionInput



class MaterialExpressionCollectionParameter(MaterialExpression):
    Collection: MaterialParameterCollection
    ParameterName: str
    ParameterId: core_uobject.Guid



class MaterialExpressionComment(MaterialExpression):
    SizeX: int
    SizeY: int
    Text: str
    CommentColor: core_uobject.LinearColor
    FontSize: int



class MaterialExpressionCompare(MaterialExpression):
    A: ExpressionInput
    B: ExpressionInput
    CompareType: EShaderCompareType



class MaterialExpressionComponentMask(MaterialExpression):
    Input: ExpressionInput
    R: bool
    G: bool
    B: bool
    A: bool



class MaterialExpressionConstant(MaterialExpression):
    R: float



class MaterialExpressionConstant2Vector(MaterialExpression):
    R: float
    G: float



class MaterialExpressionConstant3Vector(MaterialExpression):
    Constant: core_uobject.LinearColor



class MaterialExpressionConstant4Vector(MaterialExpression):
    Constant: core_uobject.LinearColor



class MaterialExpressionConstantBiasScale(MaterialExpression):
    Input: ExpressionInput
    Bias: float
    Scale: float



class MaterialExpressionCosine(MaterialExpression):
    Input: ExpressionInput
    Period: float



class MaterialExpressionCrossProduct(MaterialExpression):
    A: ExpressionInput
    B: ExpressionInput



class MaterialExpressionScalarParameter(MaterialExpressionParameter):
    DefaultValue: float
    SliderMin: float
    SliderMax: float



class MaterialExpressionCurveAtlasRowParameter(MaterialExpressionScalarParameter):
    Curve: CurveLinearColor
    Atlas: CurveLinearColorAtlas
    InputTime: ExpressionInput



class MaterialExpressionCustom(MaterialExpression):
    Code: str
    OutputType: int
    Description: str
    Inputs: unreal.WrappedArray[CustomInput]



class MaterialExpressionCustomGBX(MaterialExpressionCustom):
    OutParamNames: unreal.WrappedArray[str]



class MaterialExpressionDDX(MaterialExpression):
    Value: ExpressionInput



class MaterialExpressionDDY(MaterialExpression):
    Value: ExpressionInput



class MaterialExpressionDecalDerivative(MaterialExpression): ...


class MaterialExpressionDecalLifetimeOpacity(MaterialExpression): ...


class MaterialExpressionDecalMipmapLevel(MaterialExpression):
    TextureSize: ExpressionInput
    ConstWidth: float
    ConstHeight: float



class MaterialExpressionDegrees(MaterialExpression):
    X: ExpressionInput



class MaterialExpressionDepthFade(MaterialExpression):
    InOpacity: ExpressionInput
    FadeDistance: ExpressionInput
    OpacityDefault: float
    FadeDistanceDefault: float



class MaterialExpressionDepthOfFieldFunction(MaterialExpression):
    FunctionValue: int
    Depth: ExpressionInput



class MaterialExpressionDeriveNormalZ(MaterialExpression):
    InXY: ExpressionInput



class MaterialExpressionDesaturation(MaterialExpression):
    Input: ExpressionInput
    Fraction: ExpressionInput
    LuminanceFactors: core_uobject.LinearColor



class MaterialExpressionDistance(MaterialExpression):
    A: ExpressionInput
    B: ExpressionInput



class MaterialExpressionDistanceCullFade(MaterialExpression): ...


class MaterialExpressionDistanceFieldGradient(MaterialExpression):
    Position: ExpressionInput



class MaterialExpressionDistanceToNearestSurface(MaterialExpression):
    Position: ExpressionInput



class MaterialExpressionDivide(MaterialExpression):
    A: ExpressionInput
    B: ExpressionInput
    ConstA: float
    ConstB: float



class MaterialExpressionDotProduct(MaterialExpression):
    A: ExpressionInput
    B: ExpressionInput



class MaterialExpressionDynamicParameter(MaterialExpression):
    ParamNames: unreal.WrappedArray[str]
    DefaultValue: core_uobject.LinearColor



class MaterialExpressionExponent(MaterialExpression):
    X: ExpressionInput



class MaterialExpressionExponent2(MaterialExpression):
    X: ExpressionInput



class MaterialExpressionEyeAdaptation(MaterialExpression): ...


class MaterialExpressionFeatureLevelSwitch(MaterialExpression):
    Default: ExpressionInput
    Inputs: ExpressionInput



class MaterialExpressionFloor(MaterialExpression):
    Input: ExpressionInput



class MaterialExpressionFmod(MaterialExpression):
    A: ExpressionInput
    B: ExpressionInput



class MaterialExpressionFontSample(MaterialExpression):
    Font: Font
    FontTexturePage: int



class MaterialExpressionFontSampleParameter(MaterialExpressionFontSample):
    ParameterName: str
    ExpressionGUID: core_uobject.Guid
    Group: str



class MaterialExpressionFrac(MaterialExpression):
    Input: ExpressionInput



class MaterialExpressionFresnel(MaterialExpression):
    ExponentIn: ExpressionInput
    Exponent: float
    BaseReflectFractionIn: ExpressionInput
    BaseReflectFraction: float
    Normal: ExpressionInput



class MaterialExpressionFunctionInput(MaterialExpression):
    Preview: ExpressionInput
    InputName: str
    Description: str
    ID: core_uobject.Guid
    InputType: int
    PreviewValue: core_uobject.Vector4
    bUsePreviewValueAsDefault: bool
    SortPriority: int
    bCompilingFunctionPreview: bool



class MaterialExpressionFunctionOutput(MaterialExpression):
    OutputName: str
    Description: str
    SortPriority: int
    A: ExpressionInput
    bLastPreviewed: bool
    ID: core_uobject.Guid



class MaterialExpressionGbxColorRemapLUT(MaterialExpression):
    InColor: ExpressionInput



class MaterialExpressionGetMaterialAttributes(MaterialExpression):
    MaterialAttributes: MaterialAttributesInput
    AttributeGetTypes: unreal.WrappedArray[core_uobject.Guid]



class MaterialExpressionGIReplace(MaterialExpression):
    Default: ExpressionInput
    StaticIndirect: ExpressionInput
    DynamicIndirect: ExpressionInput



class MaterialExpressionIf(MaterialExpression):
    A: ExpressionInput
    B: ExpressionInput
    AGreaterThanB: ExpressionInput
    AEqualsB: ExpressionInput
    ALessThanB: ExpressionInput
    EqualsThreshold: float
    ConstB: float
    ConstAEqualsB: float



class MaterialExpressionIsPrimitiveMasked(MaterialExpression):
    ScreenPosition: ExpressionInput



class MaterialExpressionLightmapUVs(MaterialExpression): ...


class MaterialExpressionLightmassReplace(MaterialExpression):
    Realtime: ExpressionInput
    Lightmass: ExpressionInput



class MaterialExpressionLightVector(MaterialExpression): ...


class MaterialExpressionLinearInterpolate(MaterialExpression):
    A: ExpressionInput
    B: ExpressionInput
    Alpha: ExpressionInput
    ConstA: float
    ConstB: float
    ConstAlpha: float



class MaterialExpressionLogarithm(MaterialExpression):
    X: ExpressionInput



class MaterialExpressionLogarithm1_(MaterialExpression):
    X: ExpressionInput



class MaterialExpressionLogarithm2(MaterialExpression):
    X: ExpressionInput



class MaterialExpressionMakeMaterialAttributes(MaterialExpression):
    MaterialAttributes: ExpressionInput
    BaseColor: ExpressionInput
    Metallic: ExpressionInput
    Specular: ExpressionInput
    Roughness: ExpressionInput
    EmissiveColor: ExpressionInput
    Opacity: ExpressionInput
    OpacityMask: ExpressionInput
    Normal: ExpressionInput
    WorldPositionOffset: ExpressionInput
    WorldDisplacement: ExpressionInput
    TessellationMultiplier: ExpressionInput
    SubsurfaceColor: ExpressionInput
    ClearCoat: ExpressionInput
    ClearCoatRoughness: ExpressionInput
    AmbientOcclusion: ExpressionInput
    Refraction: ExpressionInput
    CustomizedUVs: ExpressionInput
    PixelDepthOffset: ExpressionInput
    CustomDataGBX: ExpressionInput
    CustomizedColors: ExpressionInput



class MaterialExpressionMaterialAttributeLayers(MaterialExpression):
    ParameterName: str
    ExpressionGUID: core_uobject.Guid
    Input: MaterialAttributesInput
    DefaultLayers: MaterialLayersFunctions
    LayerCallers: unreal.WrappedArray[MaterialExpressionMaterialFunctionCall]
    NumActiveLayerCallers: int
    BlendCallers: unreal.WrappedArray[MaterialExpressionMaterialFunctionCall]
    NumActiveBlendCallers: int
    bIsLayerGraphBuilt: bool



class MaterialExpressionMaterialFunctionCall(MaterialExpression):
    MaterialFunction: MaterialFunctionInterface
    FunctionParameterInfo: MaterialParameterInfo



class MaterialExpressionMaterialLayerOutput(MaterialExpressionFunctionOutput): ...


class MaterialExpressionMaterialProxyReplace(MaterialExpression):
    Realtime: ExpressionInput
    MaterialProxy: ExpressionInput



class MaterialExpressionMax(MaterialExpression):
    A: ExpressionInput
    B: ExpressionInput
    ConstA: float
    ConstB: float



class MaterialExpressionMin(MaterialExpression):
    A: ExpressionInput
    B: ExpressionInput
    ConstA: float
    ConstB: float



class MaterialExpressionMultiply(MaterialExpression):
    A: ExpressionInput
    B: ExpressionInput
    ConstA: float
    ConstB: float



class MaterialExpressionNoise(MaterialExpression):
    Position: ExpressionInput
    FilterWidth: ExpressionInput
    Scale: float
    Quality: int
    NoiseFunction: int
    bTurbulence: bool
    Levels: int
    OutputMin: float
    OutputMax: float
    LevelScale: float
    bTiling: bool



class MaterialExpressionNormalize(MaterialExpression):
    VectorInput: ExpressionInput



class MaterialExpressionNot(MaterialExpression):
    A: ExpressionInput



class MaterialExpressionObjectBounds(MaterialExpression): ...


class MaterialExpressionObjectOrientation(MaterialExpression): ...


class MaterialExpressionObjectOrientationX(MaterialExpression): ...


class MaterialExpressionObjectOrientationY(MaterialExpression): ...


class MaterialExpressionObjectPositionWS(MaterialExpression): ...


class MaterialExpressionObjectRadius(MaterialExpression): ...


class MaterialExpressionOneMinus(MaterialExpression):
    Input: ExpressionInput



class MaterialExpressionOr(MaterialExpression):
    A: ExpressionInput
    B: ExpressionInput



class MaterialExpressionPanner(MaterialExpression):
    Coordinate: ExpressionInput
    Time: ExpressionInput
    Speed: ExpressionInput
    SpeedX: float
    SpeedY: float
    bFractionalPart: bool



class MaterialExpressionParticleColor(MaterialExpression): ...


class MaterialExpressionParticleDirection(MaterialExpression): ...


class MaterialExpressionParticleIndex(MaterialExpression): ...


class MaterialExpressionParticleMacroUV(MaterialExpression): ...


class MaterialExpressionParticleMotionBlurFade(MaterialExpression): ...


class MaterialExpressionParticlePositionWS(MaterialExpression): ...


class MaterialExpressionParticleRadius(MaterialExpression): ...


class MaterialExpressionParticleRandom(MaterialExpression): ...


class MaterialExpressionParticleRelativeTime(MaterialExpression): ...


class MaterialExpressionParticleSize(MaterialExpression): ...


class MaterialExpressionParticleSpeed(MaterialExpression): ...


class MaterialExpressionParticleSubUV(MaterialExpressionTextureSample):
    bBlend: bool



class MaterialExpressionPerInstanceFadeAmount(MaterialExpression): ...


class MaterialExpressionPerInstanceRandom(MaterialExpression): ...


class MaterialExpressionPixelDepth(MaterialExpression): ...


class MaterialExpressionPixelNormalWS(MaterialExpression): ...


class MaterialExpressionPower(MaterialExpression):
    Base: ExpressionInput
    Exponent: ExpressionInput
    ConstExponent: float
    PowerFunction: EMaterialPowerFunction



class MaterialExpressionPrecomputedAOMask(MaterialExpression): ...


class MaterialExpressionPreSkinnedNormal(MaterialExpression): ...


class MaterialExpressionPreSkinnedPosition(MaterialExpression): ...


class MaterialExpressionPreviousFrameSwitch(MaterialExpression):
    CurrentFrame: ExpressionInput
    PreviousFrame: ExpressionInput



class MaterialExpressionPrimitiveComponentRandom(MaterialExpression): ...


class MaterialExpressionPrimitiveFlag(MaterialExpression):
    PrimitiveFlag: EPrimitiveSpecificDataFlags



class MaterialExpressionQualitySwitch(MaterialExpression):
    Default: ExpressionInput
    Inputs: ExpressionInput



class MaterialExpressionRadians(MaterialExpression):
    X: ExpressionInput



class MaterialExpressionReflectionVectorWS(MaterialExpression):
    CustomWorldNormal: ExpressionInput
    bNormalizeCustomWorldNormal: bool



class MaterialExpressionReroute(MaterialExpression):
    Input: ExpressionInput



class MaterialExpressionRotateAboutAxis(MaterialExpression):
    NormalizedRotationAxis: ExpressionInput
    RotationAngle: ExpressionInput
    PivotPoint: ExpressionInput
    Position: ExpressionInput
    Period: float



class MaterialExpressionRotator(MaterialExpression):
    Coordinate: ExpressionInput
    Time: ExpressionInput
    CenterX: float
    CenterY: float
    Speed: float



class MaterialExpressionRound(MaterialExpression):
    Input: ExpressionInput



class MaterialExpressionSaturate(MaterialExpression):
    Input: ExpressionInput



class MaterialExpressionSceneColor(MaterialExpression):
    InputMode: int
    Input: ExpressionInput
    OffsetFraction: ExpressionInput
    ConstInput: core_uobject.Vector2D



class MaterialExpressionSceneDepth(MaterialExpression):
    InputMode: int
    Input: ExpressionInput
    bUseRawDepth: bool
    Coordinates: ExpressionInput
    ConstInput: core_uobject.Vector2D



class MaterialExpressionSceneTexelSize(MaterialExpression): ...


class MaterialExpressionSceneTexture(MaterialExpression):
    Coordinates: ExpressionInput
    SceneTextureId: int
    bFiltered: bool



class MaterialExpressionScreenPosition(MaterialExpression): ...


class MaterialExpressionSetMaterialAttributes(MaterialExpression):
    Inputs: unreal.WrappedArray[ExpressionInput]
    AttributeSetTypes: unreal.WrappedArray[core_uobject.Guid]



class MaterialExpressionSign(MaterialExpression):
    Input: ExpressionInput



class MaterialExpressionSine(MaterialExpression):
    Input: ExpressionInput
    Period: float



class MaterialExpressionSkyColorFromEnvMap(MaterialExpression):
    Direction: ExpressionInput
    Roughness: ExpressionInput



class MaterialExpressionSkyColorFromSH(MaterialExpression):
    Direction: ExpressionInput
    bIncludeOcclusion: bool
    bLowQuality: bool



class MaterialExpressionSmoothStep(MaterialExpression):
    A: ExpressionInput
    B: ExpressionInput
    Alpha: ExpressionInput
    ConstA: float
    ConstB: float
    ConstAlpha: float



class MaterialExpressionSobol(MaterialExpression):
    Cell: ExpressionInput
    Index: ExpressionInput
    Seed: ExpressionInput
    ConstSeed: core_uobject.Vector2D



class MaterialExpressionSpeedTree(MaterialExpression):
    GeometryInput: ExpressionInput
    WindInput: ExpressionInput
    LODInput: ExpressionInput
    ExtraBendWS: ExpressionInput
    GeometryType: int
    WindType: int
    LODType: int
    BillboardThreshold: float
    bAccurateWindVelocities: bool



class MaterialExpressionSphereMask(MaterialExpression):
    A: ExpressionInput
    B: ExpressionInput
    Radius: ExpressionInput
    Hardness: ExpressionInput
    AttenuationRadius: float
    HardnessPercent: float



class MaterialExpressionSphericalParticleOpacity(MaterialExpression):
    Density: ExpressionInput
    ConstantDensity: float



class MaterialExpressionSquareRoot(MaterialExpression):
    Input: ExpressionInput



class MaterialExpressionStaticBool(MaterialExpression):
    Value: bool



class MaterialExpressionStaticBoolParameter(MaterialExpressionParameter):
    DefaultValue: bool



class MaterialExpressionStaticComponentMaskParameter(MaterialExpressionParameter):
    Input: ExpressionInput
    DefaultR: bool
    DefaultG: bool
    DefaultB: bool
    DefaultA: bool



class MaterialExpressionStaticSwitch(MaterialExpression):
    DefaultValue: bool
    A: ExpressionInput
    B: ExpressionInput
    Value: ExpressionInput



class MaterialExpressionStaticSwitchParameter(MaterialExpressionStaticBoolParameter):
    A: ExpressionInput
    B: ExpressionInput



class MaterialExpressionSubtract(MaterialExpression):
    A: ExpressionInput
    B: ExpressionInput
    ConstA: float
    ConstB: float



class MaterialExpressionTangent(MaterialExpression):
    Input: ExpressionInput
    Period: float



class MaterialExpressionTangentOutput(MaterialExpressionCustomOutput):
    Input: ExpressionInput



class MaterialExpressionTemporalSobol(MaterialExpression):
    Index: ExpressionInput
    Seed: ExpressionInput
    ConstSeed: core_uobject.Vector2D



class MaterialExpressionTextureCoordinate(MaterialExpression):
    CoordinateIndex: int
    UTiling: float
    VTiling: float
    UnMirrorU: bool
    UnMirrorV: bool



class MaterialExpressionTextureLoad(MaterialExpression):
    TextureObject: ExpressionInput
    Coordinates: ExpressionInput



class MaterialExpressionTextureObject(MaterialExpressionTextureBase): ...


class MaterialExpressionTextureObjectParameter(MaterialExpressionTextureSampleParameter): ...


class MaterialExpressionTextureProperty(MaterialExpression):
    TextureObject: ExpressionInput
    Property: int



class MaterialExpressionTextureSampleParameter2DArray(MaterialExpressionTextureSampleParameter): ...


class MaterialExpressionTextureSampleParameterCube(MaterialExpressionTextureSampleParameter): ...


class MaterialExpressionTextureSampleParameterSubUV(MaterialExpressionTextureSampleParameter2D):
    bBlend: bool



class MaterialExpressionTextureSampleParameterVolume(MaterialExpressionTextureSampleParameter): ...


class MaterialExpressionTime(MaterialExpression):
    Source: ETimeSource
    Origin: ETimeOrigin
    bIgnorePause: bool
    bOverride_Period: bool
    Period: float



class MaterialExpressionTransform(MaterialExpression):
    Input: ExpressionInput
    TransformSourceType: int
    TransformType: int



class MaterialExpressionTransformPosition(MaterialExpression):
    Input: ExpressionInput
    TransformSourceType: int
    TransformType: int



class MaterialExpressionTruncate(MaterialExpression):
    Input: ExpressionInput



class MaterialExpressionTwoSidedSign(MaterialExpression): ...


class MaterialExpressionVectorNoise(MaterialExpression):
    Position: ExpressionInput
    NoiseFunction: int
    Quality: int
    bTiling: bool



class MaterialExpressionVertexColor(MaterialExpression): ...


class MaterialExpressionVertexInterpolator(MaterialExpressionCustomOutput):
    Input: ExpressionInput



class MaterialExpressionVertexNormalWS(MaterialExpression): ...


class MaterialExpressionViewOwnerLocationWS(MaterialExpression): ...


class MaterialExpressionViewProperty(MaterialExpression):
    Property: int



class MaterialExpressionViewSize(MaterialExpression): ...


class MaterialExpressionVisiblePercentage(MaterialExpression): ...


class MaterialExpressionWindDirection(MaterialExpression):
    WorldPosition: ExpressionInput



class MaterialExpressionWindGust(MaterialExpression): ...


class MaterialExpressionWindSpeed(MaterialExpression): ...


class MaterialExpressionWorldPosition(MaterialExpression):
    WorldPositionShaderOffset: int



class MaterialFunctionInterface(unreal.UObject):
    StateId: core_uobject.Guid
    MaterialFunctionUsage: EMaterialFunctionUsage



class MaterialFunction(MaterialFunctionInterface):
    Description: str
    bExposeToLibrary: bool
    bPrefixParameterNames: bool
    FunctionExpressions: unreal.WrappedArray[MaterialExpression]
    bReentrantFlag: bool



class MaterialFunctionInstance(MaterialFunctionInterface):
    Parent: MaterialFunctionInterface
    Base: MaterialFunctionInterface
    ScalarParameterValues: unreal.WrappedArray[ScalarParameterValue]
    VectorParameterValues: unreal.WrappedArray[VectorParameterValue]
    TextureParameterValues: unreal.WrappedArray[TextureParameterValue]
    FontParameterValues: unreal.WrappedArray[FontParameterValue]
    StaticSwitchParameterValues: unreal.WrappedArray[StaticSwitchParameter]
    StaticComponentMaskParameterValues: unreal.WrappedArray[StaticComponentMaskParameter]



class MaterialFunctionMaterialLayer(MaterialFunction): ...


class MaterialFunctionMaterialLayerInstance(MaterialFunctionInstance): ...


class MaterialFunctionMaterialLayerBlend(MaterialFunction): ...


class MaterialFunctionMaterialLayerBlendInstance(MaterialFunctionInstance): ...


class MaterialInstanceActor(Actor):
    TargetActors: unreal.WrappedArray[Actor]



class MaterialInstanceDynamic(MaterialInstance):

    def SetVectorParameterValue(self, ParameterName: str, Value: core_uobject.LinearColor): ...
    def SetTextureParameterValue(self, ParameterName: str, Value: Texture): ...
    def SetScalarParameterValue(self, ParameterName: str, Value: float): ...
    def K2_InterpolateMaterialInstanceParams(self, SourceA: MaterialInstance, SourceB: MaterialInstance, Alpha: float): ...
    def K2_GetVectorParameterValue(self, ParameterName: str, ReturnValue: core_uobject.LinearColor) -> core_uobject.LinearColor: ...
    def K2_GetTextureParameterValue(self, ParameterName: str, ReturnValue: Texture) -> Texture: ...
    def K2_GetScalarParameterValue(self, ParameterName: str, ReturnValue: float) -> float: ...
    def K2_CopyMaterialInstanceParameters(self, Source: MaterialInterface, bQuickParametersOnly: bool): ...
    def CopyParameterOverrides(self, MaterialInstance: MaterialInstance): ...
    def CopyInterpParameters(self, Source: MaterialInstance): ...


class MaterialParameterCollection(unreal.UObject):
    StateId: core_uobject.Guid
    ScalarParameters: unreal.WrappedArray[CollectionScalarParameter]
    VectorParameters: unreal.WrappedArray[CollectionVectorParameter]



class MaterialParameterCollectionInstance(unreal.UObject):
    Collection: MaterialParameterCollection
    World: World



class MatineeActor(Actor):
    MatineeData: InterpData
    MatineeControllerName: str
    PlayRate: float
    bPlayOnLevelLoad: bool
    bForceStartPos: bool
    ForceStartPosition: float
    bLooping: bool
    bRewindOnPlay: bool
    bNoResetOnRewind: bool
    bRewindIfAlreadyPlaying: bool
    bDisableRadioFilter: bool
    bClientSideOnly: bool
    bSkipUpdateIfNotVisible: bool
    bIsSkippable: bool
    PreferredSplitScreenNum: int
    bDisableMovementInput: bool
    bDisableLookAtInput: bool
    bHidePlayer: bool
    bHideHud: bool
    GroupActorInfos: unreal.WrappedArray[InterpGroupActorInfo]
    bShouldShowGore: bool
    GroupInst: unreal.WrappedArray[InterpGroupInst]
    CameraCuts: unreal.WrappedArray[CameraCutInfo]
    bIsPlaying: bool
    bReversePlayback: bool
    bPaused: bool
    bPendingStop: bool
    InterpPosition: float
    ReplicationForceIsPlaying: int
    def Stop(self): ...
    def SetPosition(self, NewPosition: float, bJump: bool): ...
    def SetLoopingState(self, bNewLooping: bool): ...
    def Reverse(self): ...
    def Play(self): ...
    def Pause(self): ...
    def EnableGroupByName(self, GroupName: str, bEnable: bool): ...
    def ChangePlaybackDirection(self): ...


class MatineeActorCameraAnim(MatineeActor):
    CameraAnim: CameraAnim



class MatineeAnimInterface(core_uobject.Interface): ...


class MatineeInterface(core_uobject.Interface): ...


class MeshMergeCullingVolume(Volume): ...


class MeshSimplificationSettings(DeveloperSettings):
    MeshReductionModuleName: str



class MeshVertexPainterKismetLibrary(BlueprintFunctionLibrary):

    def RemovePaintedVertices(self, StaticMeshComponent: StaticMeshComponent): ...
    def PaintVerticesSingleColor(self, StaticMeshComponent: StaticMeshComponent, FillColor: core_uobject.LinearColor, bConvertToSRGB: bool): ...
    def PaintVerticesLerpAlongAxis(self, StaticMeshComponent: StaticMeshComponent, StartColor: core_uobject.LinearColor, EndColor: core_uobject.LinearColor, AXIS: EVertexPaintAxis, bConvertToSRGB: bool): ...


class MicroTransactionBase(PlatformInterfaceBase):
    AvailableProducts: unreal.WrappedArray[PurchaseInfo]
    LastError: str
    LastErrorSolution: str



class ModelComponent(PrimitiveComponent):
    ModelBodySetup: BodySetup



class MorphTarget(unreal.UObject):
    BaseSkelMesh: SkeletalMesh



class NavAgentInterface(core_uobject.Interface): ...


class GbxNavAreaBase(DataAsset): ...


class NavAreaBase(unreal.UObject): ...


class NavCollisionBase(unreal.UObject):
    bIsDynamicObstacle: bool



class NavEdgeProviderInterface(core_uobject.Interface): ...


class NavigationDataChunk(unreal.UObject):
    NavigationDataName: str



class NavigationDataInterface(core_uobject.Interface): ...


class NavigationObjectBase(Actor):
    CapsuleComponent: CapsuleComponent
    GoodSprite: BillboardComponent
    BadSprite: BillboardComponent
    bIsPIEPlayerStart: bool



class NavigationSystem(unreal.UObject): ...


class NavigationSystemConfig(unreal.UObject):
    NavigationSystemClass: core_uobject.SoftClassPath



class NullNavSysConfig(NavigationSystemConfig): ...


class NavLinkDefinition(unreal.UObject):
    Links: unreal.WrappedArray[NavigationLink]
    SegmentLinks: unreal.WrappedArray[NavigationSegmentLink]



class NavPathObserverInterface(core_uobject.Interface): ...


class NavRelevantInterface(core_uobject.Interface): ...


class SimulatedClientNetConnection(NetConnection): ...


class NetworkPredictionInterface(core_uobject.Interface): ...


class NetworkSettings(DeveloperSettings):
    bVerifyPeer: bool
    bEnableMultiplayerWorldOriginRebasing: bool
    MaxRepArraySize: int
    MaxRepArrayMemory: int



class NodeMappingContainer(unreal.UObject): ...


class NodeMappingProviderInterface(core_uobject.Interface): ...


class Note(Actor): ...


class ObjectLibrary(unreal.UObject):
    ObjectBaseClass: unreal.UClass
    bHasBlueprintClasses: bool
    Objects: unreal.WrappedArray[unreal.UObject]
    WeakObjects: unreal.WrappedArray[unreal.UObject]
    bUseWeakReferences: bool
    bIsFullyLoaded: bool



class ObjectReferencer(unreal.UObject):
    ReferencedObjects: unreal.WrappedArray[unreal.UObject]



class Interface_ObjectTagProvider(core_uobject.Interface): ...


class OnlineBlueprintCallProxyBase(unreal.UObject):

    def Activate(self): ...


class PackageMapClient(core_uobject.PackageMap): ...


class PainCausingVolume(PhysicsVolume):
    bPainCausing: bool
    DamagePerSec: float
    DamageType: unreal.UClass
    PainInterval: float
    bEntryPain: bool
    BACKUP_bPainCausing: bool
    DamageInstigator: Controller



class ParticleEmitter(unreal.UObject):
    EmitterName: str
    SubUVDataOffset: int
    EmitterRenderMode: int
    PerformanceCategories: int
    LODLevels: unreal.WrappedArray[ParticleLODLevel]
    ConvertedModules: bool
    PeakActiveParticles: int
    InitialAllocationCount: int
    MediumDetailSpawnRateScale: float
    QualityLevelSpawnRateScale: float
    DetailMode: int
    DistanceSpawnRamp: RawDistributionFloat
    bIsSoloing: bool
    bCookedOut: bool
    bDisabledLODsKeepEmitterAlive: bool
    bDisableWhenInsignficant: bool
    SignificanceLevel: EParticleSignificanceLevel
    bUseLegacySpawningBehavior: bool



class ParticleEventManager(Actor): ...


class ParticleLODLevel(unreal.UObject):
    Level: int
    bEnabled: bool
    RequiredModule: ParticleModuleRequired
    Modules: unreal.WrappedArray[ParticleModule]
    TypeDataModule: ParticleModuleTypeDataBase
    SpawnModule: ParticleModuleSpawn
    EventGenerator: ParticleModuleEventGenerator
    SpawningModules: unreal.WrappedArray[ParticleModuleSpawnBase]
    SpawnModules: unreal.WrappedArray[ParticleModule]
    UpdateModules: unreal.WrappedArray[ParticleModule]
    OrbitModules: unreal.WrappedArray[ParticleModuleOrbit]
    EventReceiverModules: unreal.WrappedArray[ParticleModuleEventReceiverBase]
    ConvertedModules: bool
    PeakActiveParticles: int
    FinalizeTickModules: unreal.WrappedArray[ParticleModule]
    PreAsyncModules: unreal.WrappedArray[ParticleModule]



class ParticleModuleAccelerationBase(ParticleModule):
    bAlwaysInWorldSpace: bool



class ParticleModuleAcceleration(ParticleModuleAccelerationBase):
    Acceleration: RawDistributionVector
    bApplyOwnerScale: bool



class ParticleModuleAccelerationConstant(ParticleModuleAccelerationBase):
    Acceleration: core_uobject.Vector



class ParticleModuleAccelerationDrag(ParticleModuleAccelerationBase):
    DragCoefficient: DistributionFloat
    DragCoefficientRaw: RawDistributionFloat



class ParticleModuleAccelerationDragScaleOverLife(ParticleModuleAccelerationBase):
    DragScale: DistributionFloat
    DragScaleRaw: RawDistributionFloat



class ParticleModuleAccelerationOverLifetime(ParticleModuleAccelerationBase):
    AccelOverLife: RawDistributionVector



class ParticleModuleAttractorBase(ParticleModule): ...


class ParticleModuleAttractorLine(ParticleModuleAttractorBase):
    EndPoint1: core_uobject.Vector
    Range: RawDistributionFloat
    Strength: RawDistributionFloat



class ParticleModuleAttractorParticle(ParticleModuleAttractorBase):
    EmitterName: str
    Range: RawDistributionFloat
    bStrengthByDistance: bool
    Strength: RawDistributionFloat
    bAffectBaseVelocity: bool
    SelectionMethod: int
    bRenewSource: bool
    bInheritSourceVel: bool
    LastSelIndex: int



class ParticleModuleAttractorPoint(ParticleModuleAttractorBase):
    Position: RawDistributionVector
    Range: RawDistributionFloat
    Strength: RawDistributionFloat
    StrengthByDistance: bool
    bAffectBaseVelocity: bool
    bOverrideVelocity: bool
    bUseWorldSpacePosition: bool
    Positive_X: bool
    Positive_Y: bool
    Positive_Z: bool
    Negative_X: bool
    Negative_Y: bool
    Negative_Z: bool



class ParticleModuleAttractorPointGravity(ParticleModuleAttractorBase):
    Position: core_uobject.Vector
    Radius: float
    Strength: DistributionFloat
    StrengthRaw: RawDistributionFloat



class ParticleModuleSpawnBase(ParticleModule):
    bProcessSpawnRate: bool
    bProcessBurstList: bool



class ParticleModuleBeam(ParticleModuleSpawnBase):
    BeamMethod: EBeamMethod
    BeamInterpolation: EBeamInterpolation
    TaperMethod: EBeamModuleTaperMethod
    bAllowWander: bool
    Speed: float
    TangentScalePower: float
    NumBeamParticles: int
    SplineMidpoints: unreal.WrappedArray[RawDistributionVector]
    TessellationSplineTension: float
    Distance: RawDistributionFloat
    TaperFactor: RawDistributionFloat
    TaperScale: RawDistributionFloat



class ParticleModuleBeamBase(ParticleModule): ...


class ParticleModuleRibbonBeamSource(ParticleModuleBeamBase):
    SourceMethod: int
    SourceName: str
    bSourceAbsolute: bool
    Source: RawDistributionVector
    bLockSource: bool
    SourceTangentMethod: int
    SourceTangent: RawDistributionVector
    bLockSourceTangent: bool
    SourceStrength: RawDistributionFloat
    bLockSourceStength: bool
    bUpdateEveryFrame: bool



class ParticleModuleRibbonBeamTarget(ParticleModuleBeamBase):
    TargetMethod: int
    TargetName: str
    Target: RawDistributionVector
    bTargetAbsolute: bool
    bLockTarget: bool
    TargetTangentMethod: int
    TargetTangent: RawDistributionVector
    bLockTargetTangent: bool
    TargetStrength: RawDistributionFloat
    bLockTargetStength: bool
    LockRadius: float
    bUpdateEveryFrame: bool



class ParticleModuleRibbonBeamNoise(ParticleModuleBeamBase):
    bLowFreq_Enabled: bool
    Frequency: int
    Frequency_LowRange: int
    NoiseRange: RawDistributionVector
    NoiseRangeScale: RawDistributionFloat
    bNRScaleEmitterTime: bool
    NoiseSpeed: RawDistributionVector
    bSmooth: bool
    NoiseLockRadius: float
    bNoiseLock: bool
    bOscillate: bool
    NoiseLockTime: float
    NoiseTension: float
    bUseNoiseTangents: bool
    NoiseTangentStrength: RawDistributionFloat
    NoiseTessellation: int
    bTargetNoise: bool
    FrequencyDistance: float
    bApplyNoiseScale: bool
    NoiseScale: RawDistributionFloat



class ParticleModuleBeamLocationOverLife(ParticleModuleLocationBase):
    BeamEmitterName: str
    StartOffset: RawDistributionFloat
    EndOffset: RawDistributionFloat
    SpeedMultiplier: RawDistributionFloat
    bReleaseParticlesAtEnd: bool
    bApplyVelocity: bool
    bOrientMeshEmitters: bool



class ParticleModuleBeamModifier(ParticleModuleBeamBase):
    ModifierType: int
    PositionOptions: BeamModifierOptions
    Position: RawDistributionVector
    TangentOptions: BeamModifierOptions
    Tangent: RawDistributionVector
    bAbsoluteTangent: bool
    StrengthOptions: BeamModifierOptions
    Strength: RawDistributionFloat



class ParticleModuleBeamNoise(ParticleModuleBeamBase):
    bLowFreq_Enabled: bool
    Frequency: int
    Frequency_LowRange: int
    NoiseRange: RawDistributionVector
    NoiseRangeScale: RawDistributionFloat
    bNRScaleEmitterTime: bool
    NoiseSpeed: RawDistributionVector
    bSmooth: bool
    NoiseLockRadius: float
    bNoiseLock: bool
    bOscillate: bool
    NoiseLockTime: float
    NoiseTension: float
    bUseNoiseTangents: bool
    NoiseTangentStrength: RawDistributionFloat
    NoiseTessellation: int
    bTargetNoise: bool
    FrequencyDistance: float
    bApplyNoiseScale: bool
    NoiseScale: RawDistributionFloat



class ParticleModuleBeamSource(ParticleModuleBeamBase):
    SourceMethod: int
    SourceName: str
    bSourceAbsolute: bool
    Source: RawDistributionVector
    bLockSource: bool
    SourceTangentMethod: int
    SourceTangent: RawDistributionVector
    bLockSourceTangent: bool
    SourceStrength: RawDistributionFloat
    bLockSourceStength: bool



class ParticleModuleBeamTarget(ParticleModuleBeamBase):
    TargetMethod: int
    TargetName: str
    Target: RawDistributionVector
    bTargetAbsolute: bool
    bLockTarget: bool
    TargetTangentMethod: int
    TargetTangent: RawDistributionVector
    bLockTargetTangent: bool
    TargetStrength: RawDistributionFloat
    bLockTargetStength: bool
    LockRadius: float



class ParticleModuleBeamTargetTrace(ParticleModuleBeamBase):
    TraceDirection: RawDistributionVector
    MaxTraceDistance: float
    bUseLocalSpace: bool
    CollisionTypes: unreal.WrappedArray[int]
    bUpdateEveryFrame: bool
    bIgnoreSourceActor: bool
    bIgnoreSourceActorOwner: bool



class ParticleModuleCameraBase(ParticleModule): ...


class ParticleModuleCameraOffset(ParticleModuleCameraBase):
    CameraOffset: RawDistributionFloat
    bSpawnTimeOnly: bool
    UpdateMethod: int



class ParticleModuleCollisionBase(ParticleModule): ...


class ParticleModuleCollision(ParticleModuleCollisionBase):
    DampingFactor: RawDistributionVector
    DampingFactorRotation: RawDistributionVector
    MaxCollisions: RawDistributionFloat
    CollisionCompletionOption: int
    CollisionTypes: unreal.WrappedArray[int]
    bApplyPhysics: bool
    bIgnoreTriggerVolumes: bool
    ParticleMass: RawDistributionFloat
    DirScalar: float
    bPawnsDoNotDecrementCount: bool
    bOnlyVerticalNormalsDecrementCount: bool
    VerticalFudgeFactor: float
    DelayAmount: RawDistributionFloat
    bDropDetail: bool
    bCollideOnlyIfVisible: bool
    bIgnoreSourceActor: bool
    MaxCollisionDistance: float



class ParticleModuleCollisionGPU(ParticleModuleCollisionBase):
    Resilience: RawDistributionFloat
    ResilienceScaleOverLife: RawDistributionFloat
    Friction: float
    RandomSpread: float
    RandomDistribution: float
    RadiusScale: float
    RadiusBias: float
    Response: int
    CollisionMode: int



class ParticleModuleColorBase(ParticleModule): ...


class ParticleModuleColor(ParticleModuleColorBase):
    StartColor: RawDistributionVector
    StartAlpha: RawDistributionFloat
    bClampAlpha: bool



class ParticleModuleColor_Seeded(ParticleModuleColor):
    RandomSeedInfo: ParticleRandomSeedInfo



class ParticleModuleColorOverLife(ParticleModuleColorBase):
    ColorOverLife: RawDistributionVector
    AlphaOverLife: RawDistributionFloat
    bClampAlpha: bool
    bColorOverParticleIndex: bool



class ParticleModuleColorScaleOverLife(ParticleModuleColorBase):
    ColorScaleOverLife: RawDistributionVector
    AlphaScaleOverLife: RawDistributionFloat
    bEmitterTime: bool
    bScaleOverParticleIndex: bool



class ParticleModuleEventBase(ParticleModule): ...


class ParticleModuleEventGenerator(ParticleModuleEventBase):
    Events: unreal.WrappedArray[ParticleEvent_GenerateInfo]



class ParticleModuleEventGeneratorDecal(ParticleModuleEventGenerator):
    DecalMaterials: unreal.WrappedArray[MaterialInterface]
    Size: core_uobject.Vector
    LifeSpan: float
    FadeDuration: float
    Rotation: RawDistributionFloat



class ParticleModuleEventReceiverBase(ParticleModuleEventBase):
    EventGeneratorType: int
    EventName: str



class ParticleModuleEventReceiverKillParticles(ParticleModuleEventReceiverBase):
    bStopSpawning: bool



class ParticleModuleEventReceiverSpawn(ParticleModuleEventReceiverBase):
    SpawnCount: RawDistributionFloat
    bUseParticleTime: bool
    bUsePSysLocation: bool
    bInheritVelocity: bool
    InheritVelocityScale: RawDistributionVector
    PhysicalMaterials: unreal.WrappedArray[PhysicalMaterial]
    bBanPhysicalMaterials: bool



class ParticleModuleEventSendToGame(unreal.UObject): ...


class ParticleModuleSkeletalMeshBase(ParticleModule): ...


class ParticleModuleInheritOwnerPose(ParticleModuleSkeletalMeshBase): ...


class ParticleModuleKillBase(ParticleModule): ...


class ParticleModuleKillBox(ParticleModuleKillBase):
    LowerLeftCorner: RawDistributionVector
    UpperRightCorner: RawDistributionVector
    bAbsolute: bool
    bKillInside: bool
    bAxisAlignedAndFixedSize: bool



class ParticleModuleKillHeight(ParticleModuleKillBase):
    Height: RawDistributionFloat
    bAbsolute: bool
    bFloor: bool
    bApplyPSysScale: bool



class ParticleModuleLifetimeBase(ParticleModule): ...


class ParticleModuleLifetime(ParticleModuleLifetimeBase):
    LifeTime: RawDistributionFloat



class ParticleModuleLifetime_Seeded(ParticleModuleLifetime):
    RandomSeedInfo: ParticleRandomSeedInfo



class ParticleModuleLightBase(ParticleModule): ...


class ParticleModuleLight(ParticleModuleLightBase):
    bUseInverseSquaredFalloff: bool
    bAffectsTranslucency: bool
    bPreviewLightRadius: bool
    SpawnFraction: float
    ColorScaleOverLife: RawDistributionVector
    BrightnessOverLife: RawDistributionFloat
    RadiusScale: RawDistributionFloat
    LightExponent: RawDistributionFloat
    LightingChannels: LightingChannels
    VolumetricScatteringIntensity: float
    bHighQualityLights: bool
    bShadowCastingLights: bool
    bExposureCompensation: bool



class ParticleModuleLight_Seeded(ParticleModuleLight):
    RandomSeedInfo: ParticleRandomSeedInfo



class ParticleModuleLocation(ParticleModuleLocationBase):
    StartLocation: RawDistributionVector
    DistributeOverNPoints: float
    DistributeThreshold: float



class ParticleModuleLocation_Seeded(ParticleModuleLocation):
    RandomSeedInfo: ParticleRandomSeedInfo



class ParticleModuleLocationBoneSocket(ParticleModuleLocationBase):
    SourceType: int
    UniversalOffset: core_uobject.Vector
    UniversalOffsetDistribution: RawDistributionVector
    SourceLocations: unreal.WrappedArray[LocationBoneSocketInfo]
    SelectionMethod: int
    ManualSelectionIndex: RawDistributionFloat
    bUpdatePositionEachFrame: bool
    bOrientMeshEmitters: bool
    bOrientVelocity: bool
    bInheritBoneVelocity: bool
    InheritVelocityScale: float
    SkelMeshActorParamName: str
    NumPreSelectedIndices: int



class ParticleModuleLocationDirect(ParticleModuleLocationBase):
    Location: RawDistributionVector
    LocationOffset: RawDistributionVector
    ScaleFactor: RawDistributionVector
    Direction: RawDistributionVector



class ParticleModuleLocationEmitter(ParticleModuleLocationBase):
    EmitterName: str
    SelectionMethod: int
    InheritSourceVelocity: bool
    InheritSourceVelocityScale: float
    bInheritSourceRotation: bool
    InheritSourceRotationScale: float
    bInheritSourceMeshRotation: bool
    ManualAlpha: RawDistributionFloat



class ParticleModuleLocationEmitterDirect(ParticleModuleLocationBase):
    EmitterName: str
    LocationMode: EmitterLocationMode
    ManualAlpha: RawDistributionFloat



class ParticleModuleLocationPrimitiveBase(ParticleModuleLocationBase):
    Positive_X: bool
    Positive_Y: bool
    Positive_Z: bool
    Negative_X: bool
    Negative_Y: bool
    Negative_Z: bool
    SurfaceOnly: bool
    Velocity: bool
    VelocityScale: RawDistributionFloat
    StartLocation: RawDistributionVector



class ParticleModuleLocationPrimitiveBox(ParticleModuleLocationPrimitiveBase):
    BoxSize: RawDistributionVector
    ValidFaceBitmask: int



class ParticleModuleLocationPrimitiveCylinder(ParticleModuleLocationPrimitiveBase):
    RadialVelocity: bool
    StartRadius: RawDistributionFloat
    StartHeight: RawDistributionFloat
    HeightAxis: int



class ParticleModuleLocationPrimitiveCylinder_Seeded(ParticleModuleLocationPrimitiveCylinder):
    RandomSeedInfo: ParticleRandomSeedInfo



class ParticleModuleLocationPrimitiveSphere(ParticleModuleLocationPrimitiveBase):
    StartRadius: RawDistributionFloat



class ParticleModuleLocationPrimitiveSphere_Seeded(ParticleModuleLocationPrimitiveSphere):
    RandomSeedInfo: ParticleRandomSeedInfo



class ParticleModuleLocationPrimitiveTriangle(ParticleModuleLocationBase):
    StartOffset: RawDistributionVector
    Height: RawDistributionFloat
    Angle: RawDistributionFloat
    Thickness: RawDistributionFloat



class ParticleModuleLocationSkelVertSurface(ParticleModuleLocationBase):
    SourceType: int
    UniversalOffset: core_uobject.Vector
    bUpdatePositionEachFrame: bool
    bOrientMeshEmitters: bool
    bInheritBoneVelocity: bool
    InheritVelocityScale: float
    SkelMeshActorParamName: str
    ValidAssociatedBones: unreal.WrappedArray[str]
    bUseSocketNames: bool
    bEnforceNormalCheck: bool
    NormalToCompare: core_uobject.Vector
    NormalCheckToleranceDegrees: float
    NormalCheckTolerance: float
    ValidMaterialIndices: unreal.WrappedArray[int]
    bInheritVertexColor: bool
    bInheritUV: bool



class ParticleModuleLocationWorldOffset(ParticleModuleLocation): ...


class ParticleModuleLocationWorldOffset_Seeded(ParticleModuleLocationWorldOffset):
    RandomSeedInfo: ParticleRandomSeedInfo



class ParticleModuleMaterialBase(ParticleModule): ...


class ParticleModuleMeshMaterial(ParticleModuleMaterialBase):
    MeshMaterials: unreal.WrappedArray[MaterialInterface]



class ParticleModuleRotationBase(ParticleModule): ...


class ParticleModuleMeshRotation(ParticleModuleRotationBase):
    StartRotation: RawDistributionVector
    bInheritParent: bool



class ParticleModuleMeshRotation_Seeded(ParticleModuleMeshRotation):
    RandomSeedInfo: ParticleRandomSeedInfo



class ParticleModuleRotationRateBase(ParticleModule): ...


class ParticleModuleMeshRotationRate(ParticleModuleRotationRateBase):
    StartRotationRate: RawDistributionVector



class ParticleModuleMeshRotationRate_Seeded(ParticleModuleMeshRotationRate):
    RandomSeedInfo: ParticleRandomSeedInfo



class ParticleModuleMeshRotationRateMultiplyLife(ParticleModuleRotationRateBase):
    LifeMultiplier: RawDistributionVector



class ParticleModuleMeshRotationRateOverLife(ParticleModuleRotationRateBase):
    RotRate: RawDistributionVector
    bScaleRotRate: bool



class ParticleModuleOrbitBase(ParticleModule):
    bUseEmitterTime: bool



class ParticleModuleOrbit(ParticleModuleOrbitBase):
    ChainMode: int
    OffsetAmount: RawDistributionVector
    OffsetOptions: OrbitOptions
    RotationAmount: RawDistributionVector
    RotationOptions: OrbitOptions
    RotationRateAmount: RawDistributionVector
    RotationRateOptions: OrbitOptions



class ParticleModuleOrientationBase(ParticleModule): ...


class ParticleModuleOrientationAxisLock(ParticleModuleOrientationBase):
    LockAxisFlags: int



class ParticleModuleParameterBase(ParticleModule): ...


class ParticleModuleParameterDynamic(ParticleModuleParameterBase):
    DynamicParams: unreal.WrappedArray[EmitterDynamicParameter]
    bApplyOverParticleIndex: bool
    bSingleValue: bool
    UpdateFlags: int
    bUsesVelocity: bool



class ParticleModuleParameterDynamic_Seeded(ParticleModuleParameterDynamic):
    RandomSeedInfo: ParticleRandomSeedInfo



class ParticleModulePivotOffset(ParticleModuleLocationBase):
    PivotOffset: core_uobject.Vector2D



class ParticleModulePlaySkeletalAnim(ParticleModuleSkeletalMeshBase):
    SelectionMethod: AnimationSelectionMethod
    AnimSequences: unreal.WrappedArray[AnimSequence]
    bPlayOverParticleLifetime: bool
    StartTimeMethod: StartTimeSelectionMethod
    StartTime: RawDistributionFloat
    Rate: RawDistributionFloat
    bLoop: bool



class ParticleModuleRequired(ParticleModule):
    Material: MaterialInterface
    EmitterOrigin: core_uobject.Vector
    EmitterRotation: core_uobject.Rotator
    ScreenAlignment: int
    MinFacingCameraBlendDistance: float
    MaxFacingCameraBlendDistance: float
    bUseLocalSpace: bool
    bKillOnDeactivate: bool
    bKillOnCompleted: bool
    SortMode: int
    bUseLegacyEmitterTime: bool
    bRemoveHMDRoll: bool
    EmitterDuration: float
    EmitterDurationLow: float
    bEmitterDurationUseRange: bool
    bDurationRecalcEachLoop: bool
    EmitterLoops: int
    SpawnRate: RawDistributionFloat
    ParticleBurstMethod: int
    BurstList: unreal.WrappedArray[ParticleBurst]
    EmitterDelay: float
    EmitterDelayLow: float
    bEmitterDelayUseRange: bool
    bDelayFirstLoopOnly: bool
    InterpolationMethod: int
    SubImages_Horizontal: int
    SubImages_Vertical: int
    bScaleUV: bool
    RandomImageTime: float
    RandomImageChanges: int
    bOverrideSystemMacroUV: bool
    MacroUVPosition: core_uobject.Vector
    MacroUVRadius: float
    bUseMaxDrawCount: bool
    MaxDrawCount: int
    UVFlippingMode: EParticleUVFlipMode
    CutoutTexture: Texture2D
    BoundingMode: int
    OpacitySourceMode: int
    AlphaThreshold: float
    EmitterNormalsMode: int
    NormalsSphereCenter: core_uobject.Vector
    NormalsCylinderDirection: core_uobject.Vector
    bOrbitModuleAffectsVelocityAlignment: bool
    bExcludeFromBoundsCalculation: bool
    NamedMaterialOverrides: unreal.WrappedArray[str]



class ParticleModuleRotation(ParticleModuleRotationBase):
    StartRotation: RawDistributionFloat



class ParticleModuleRotation_Seeded(ParticleModuleRotation):
    RandomSeedInfo: ParticleRandomSeedInfo



class ParticleModuleRotationOverLifetime(ParticleModuleRotationBase):
    RotationOverLife: RawDistributionFloat
    Scale: bool
    bRotateOverParticleIndex: bool
    bFullRotationPerParticle: bool



class ParticleModuleRotationRate(ParticleModuleRotationRateBase):
    StartRotationRate: RawDistributionFloat



class ParticleModuleRotationRate_Seeded(ParticleModuleRotationRate):
    RandomSeedInfo: ParticleRandomSeedInfo



class ParticleModuleRotationRateMultiplyLife(ParticleModuleRotationRateBase):
    LifeMultiplier: RawDistributionFloat



class ParticleModuleSizeBase(ParticleModule): ...


class ParticleModuleSize(ParticleModuleSizeBase):
    StartSize: RawDistributionVector



class ParticleModuleSize_Seeded(ParticleModuleSize):
    RandomSeedInfo: ParticleRandomSeedInfo



class ParticleModuleSizeMultiplyLife(ParticleModuleSizeBase):
    LifeMultiplier: RawDistributionVector
    MultiplyX: bool
    MultiplyY: bool
    MultiplyZ: bool
    bSizeByParticleIndex: bool



class ParticleModuleSizeScale(ParticleModuleSizeBase):
    SizeScale: RawDistributionVector
    EnableX: bool
    EnableY: bool
    EnableZ: bool
    bScaleOverParticleIndex: bool



class ParticleModuleSizeScaleBySpeed(ParticleModuleSizeBase):
    SpeedScale: core_uobject.Vector2D
    MaxScale: core_uobject.Vector2D



class ParticleModuleSizeScaleByTime(ParticleModuleSizeBase):
    SizeScaleByTime: RawDistributionVector
    bEnableX: bool
    bEnableY: bool
    bEnableZ: bool



class ParticleModuleSourceMovement(ParticleModuleLocationBase):
    SourceMovementScale: RawDistributionVector



class ParticleModuleSpawn(ParticleModuleSpawnBase):
    Rate: RawDistributionFloat
    RateScale: RawDistributionFloat
    ParticleBurstMethod: int
    BurstList: unreal.WrappedArray[ParticleBurst]
    BurstScale: RawDistributionFloat
    bBurstOnceOnLoop: bool
    bApplyGlobalSpawnRateScale: bool



class ParticleModuleSpawnPerUnit(ParticleModuleSpawnBase):
    UnitScalar: float
    SpawnPerUnit: RawDistributionFloat
    bSpawnPerMovement: bool
    bIgnoreSpawnRateWhenMoving: bool
    MovementTolerance: float
    MaxFrameDistance: float
    MinFrameDistance: float
    bIgnoreMovementAlongX: bool
    bIgnoreMovementAlongY: bool
    bIgnoreMovementAlongZ: bool



class ParticleModuleSubUVBase(ParticleModule): ...


class ParticleModuleSubUV(ParticleModuleSubUVBase):
    Animation: SubUVAnimation
    SubImageIndex: RawDistributionFloat
    bUseRealTime: bool



class ParticleModuleSubUVMovie(ParticleModuleSubUV):
    bUseEmitterTime: bool
    FrameRate: RawDistributionFloat
    StartingFrame: int



class ParticleModuleTrailBase(ParticleModule): ...


class ParticleModuleTrailSource(ParticleModuleTrailBase):
    SourceMethod: int
    SourceName: str
    SourceStrength: RawDistributionFloat
    bLockSourceStength: bool
    SourceOffsetCount: int
    SourceOffsetDefaults: unreal.WrappedArray[core_uobject.Vector]
    SelectionMethod: int
    bInheritRotation: bool



class ParticleModuleTypeDataBase(ParticleModule): ...


class ParticleModuleTypeDataAnimTrail(ParticleModuleTypeDataBase):
    bDeadTrailsOnDeactivate: bool
    bEnablePreviousTangentRecalculation: bool
    bTangentRecalculationEveryFrame: bool
    TilingDistance: float
    DistanceTessellationStepSize: float
    TangentTessellationStepSize: float
    WidthTessellationStepSize: float



class ParticleModuleTypeDataBeam2(ParticleModuleTypeDataBase):
    BeamMethod: int
    TextureTile: int
    TextureTileDistance: float
    Sheets: int
    MaxBeamCount: int
    Speed: float
    InterpolationPoints: int
    bAlwaysOn: bool
    UpVectorStepSize: int
    BranchParentName: str
    Distance: RawDistributionFloat
    TaperMethod: int
    TaperFactor: RawDistributionFloat
    TaperScale: RawDistributionFloat
    RenderGeometry: bool
    RenderDirectLine: bool
    RenderLines: bool
    RenderTessellation: bool



class ParticleModuleTypeDataGpu(ParticleModuleTypeDataBase):
    EmitterInfo: GPUSpriteEmitterInfo
    ResourceData: GPUSpriteResourceData
    CameraMotionBlurAmount: float
    bClearExistingParticlesOnInit: bool



class ParticleModuleTypeDataMesh(ParticleModuleTypeDataBase):
    Mesh: StaticMesh
    Meshes: unreal.WrappedArray[StaticMesh]
    SelectionMethod: MeshSelectionMethod
    bUseStaticMeshLODs: bool
    LODSizeScale: float
    CastShadows: bool
    DoCollisions: bool
    MeshAlignment: int
    bOverrideMaterial: bool
    bOverrideDefaultMotionBlurSettings: bool
    bEnableMotionBlur: bool
    Pitch: float
    Roll: float
    Yaw: float
    RollPitchYawRange: RawDistributionVector
    AxisLockOption: int
    bCameraFacing: bool
    CameraFacingUpAxisOption: int
    CameraFacingOption: int
    bApplyParticleRotationAsSpin: bool
    bFaceCameraDirectionRatherThanPosition: bool
    bCollisionsConsiderPartilceSize: bool



class ParticleModuleTypeDataRibbon(ParticleModuleTypeDataBase):
    MaxTessellationBetweenParticles: int
    SheetsPerTrail: int
    MaxTrailCount: int
    MaxParticleInTrailCount: int
    bDeadTrailsOnDeactivate: bool
    bDeadTrailsOnSourceLoss: bool
    bClipSourceSegement: bool
    bEnablePreviousTangentRecalculation: bool
    bTangentRecalculationEveryFrame: bool
    bSpawnInitialParticle: bool
    RenderAxis: int
    TangentSpawningScalar: float
    bRenderGeometry: bool
    bRenderSpawnPoints: bool
    bRenderTangents: bool
    bRenderTessellation: bool
    TilingDistance: float
    DistanceTessellationStepSize: float
    bEnableTangentDiffInterpScale: bool
    TangentTessellationScalar: float
    MotionSmoothing: float
    bAllowPerParticleInitialSize: bool



class ParticleModuleTypeDataSkeletalMesh(ParticleModuleTypeDataBase):
    SkeletalMesh: SkeletalMesh
    bInheritMeshFromOwner: bool
    SkeletalMeshLODLevel: int
    RollPitchYawRange: RawDistributionVector
    AxisLockOption: int
    bCameraFacing: bool
    CameraFacingOption: int
    bApplyParticleRotationAsSpin: bool
    bFaceCameraDirectionRatherThanPosition: bool
    bOverrideMaterial: bool



class ParticleModuleVectorFieldBase(ParticleModule): ...


class ParticleModuleVectorFieldGlobal(ParticleModuleVectorFieldBase):
    bOverrideGlobalVectorFieldTightness: bool
    GlobalVectorFieldScale: float
    GlobalVectorFieldTightness: float



class ParticleModuleVectorFieldLocal(ParticleModuleVectorFieldBase):
    VectorField: VectorField
    RelativeTranslation: core_uobject.Vector
    RelativeRotation: core_uobject.Rotator
    RelativeScale3D: core_uobject.Vector
    Intensity: float
    Tightness: float
    bIgnoreComponentTransform: bool
    bTileX: bool
    bTileY: bool
    bTileZ: bool
    bUseFixDT: bool



class ParticleModuleVectorFieldRotation(ParticleModuleVectorFieldBase):
    MinInitialRotation: core_uobject.Vector
    MaxInitialRotation: core_uobject.Vector



class ParticleModuleVectorFieldRotationRate(ParticleModuleVectorFieldBase):
    RotationRate: core_uobject.Vector



class ParticleModuleVectorFieldScale(ParticleModuleVectorFieldBase):
    VectorFieldScale: DistributionFloat
    VectorFieldScaleRaw: RawDistributionFloat



class ParticleModuleVectorFieldScaleOverLife(ParticleModuleVectorFieldBase):
    VectorFieldScaleOverLife: DistributionFloat
    VectorFieldScaleOverLifeRaw: RawDistributionFloat



class ParticleModuleVelocityBase(ParticleModule):
    bInWorldSpace: bool
    bApplyOwnerScale: bool



class ParticleModuleVelocity(ParticleModuleVelocityBase):
    StartVelocity: RawDistributionVector
    StartVelocityRadial: RawDistributionFloat



class ParticleModuleVelocity_Seeded(ParticleModuleVelocity):
    RandomSeedInfo: ParticleRandomSeedInfo



class ParticleModuleVelocityCone(ParticleModuleVelocityBase):
    Angle: RawDistributionFloat
    Velocity: RawDistributionFloat
    Direction: core_uobject.Vector



class ParticleModuleVelocityCurlNoise(ParticleModuleVelocityBase):
    NoiseScale: RawDistributionVector
    bScaleUniformSeed: bool
    bScaleOverEmitterTime: bool
    NoiseOffset: RawDistributionVector
    bOffsetUniformSeed: bool
    bOffsetOverEmitterTime: bool
    bOffsetIsContinuous: bool
    NoiseStrength: RawDistributionVector
    bStrengthUniformSeed: bool
    bStrengthOverEmitterTime: bool
    bStrengthScaleOverEmitterTime: bool
    bHighFidelity: bool
    HighFidelityFPS: float
    NoiseStrengthScale: RawDistributionVector



class ParticleModuleVelocityInheritParent(ParticleModuleVelocityBase):
    Scale: RawDistributionVector



class ParticleModuleVelocityOverLifetime(ParticleModuleVelocityBase):
    VelOverLife: RawDistributionVector
    Absolute: bool



class ParticleModuleVelocityVortex(ParticleModuleVelocityBase):
    AxialStrength: RawDistributionFloat
    RadialStrength: RawDistributionFloat
    RotationalStrength: RawDistributionFloat
    DistanceFalloff: RawDistributionFloat
    WorldSpaceRelaxation: RawDistributionFloat
    WorldSpaceRelaxSensitivity: float
    bUseWorldSpaceRelaxation: bool
    CenterOffset: core_uobject.Vector
    bDontInheritCenterOffset: bool
    bUseCenterFocalPoint: bool
    AxisAlignment: EVortexAxisAlignment
    bUseEmitterTime: bool



class ParticleModuleWaveNoise(ParticleModuleTrailBase):
    NoiseType: ParticleWaveNoiseType
    bInWorldSpace: bool
    bUseFramePosition: bool
    Frequency: NoiseModifier
    bFrequencyIsRelative: bool
    Phase: NoiseModifier
    bPhaseIsContinuous: bool
    Amplitude: NoiseModifier



class ParticleModuleWindVelocity(ParticleModuleVelocityBase):
    VelocityScale: RawDistributionFloat



class ParticleSpriteEmitter(ParticleEmitter): ...


class ParticleSystem(unreal.UObject):
    SystemUpdateMode: int
    UpdateTime_FPS: float
    UpdateTime_Delta: float
    WarmupTime: float
    WarmupTickRate: float
    Emitters: unreal.WrappedArray[ParticleEmitter]
    PreviewComponent: ParticleSystemComponent
    CurveEdSetup: InterpCurveEdSetup
    bOrientZAxisTowardCamera: bool
    LODDistanceCheckTime: float
    LODMethod: int
    LODDistances: unreal.WrappedArray[float]
    bRegenerateLODDuplicate: bool
    LODSettings: unreal.WrappedArray[ParticleSystemLOD]
    bUseFixedRelativeBoundingBox: bool
    FixedRelativeBoundingBox: core_uobject.Box
    SecondsBeforeInactive: float
    bShouldResetPeakCounts: bool
    bHasPhysics: bool
    bUseRealtimeThumbnail: bool
    ThumbnailImageOutOfDate: bool
    Delay: float
    DelayLow: float
    bUseDelayRange: bool
    bAutoDeactivate: bool
    InsignificantReaction: EParticleSystemInsignificanceReaction
    InsignificanceDelay: float
    MaxSignificanceLevel: EParticleSignificanceLevel
    KillParticlesOnDeactivateThreshold: EForceKillParticlesThreshold
    MacroUVPosition: core_uobject.Vector
    MacroUVRadius: float
    OcclusionBoundsMethod: int
    CustomOcclusionBounds: core_uobject.Box
    SoloTracking: unreal.WrappedArray[LODSoloTrack]
    NamedMaterialSlots: unreal.WrappedArray[NamedEmitterMaterial]
    ParameterEvaluators: unreal.WrappedArray[ParticleParameterEvaluator]
    bRotationFollowsVelocity: bool
    SmoothedRotationFollowRate: float
    bNeedsPreAsyncTick: bool
    bRegisterWithSignificanceManager: bool
    bTickInPostPhysics: bool
    def ContainsEmitterType(self, TypeData: unreal.UClass, ReturnValue: bool) -> bool: ...


class ParticleSystemComponent(PrimitiveComponent):
    Template: ParticleSystem
    EmitterMaterials: unreal.WrappedArray[MaterialInterface]
    SkelMeshComponents: unreal.WrappedArray[SkeletalMeshComponent]
    bResetOnDetach: bool
    bUpdateOnDedicatedServer: bool
    bAllowRecycling: bool
    bAutoManageAttachment: bool
    bWarmingUp: bool
    bOverrideLODMethod: bool
    bSkipUpdateDynamicDataDuringTick: bool
    LODMethod: int
    RequiredSignificance: EParticleSignificanceLevel
    InstanceParameters: unreal.WrappedArray[ParticleSysParam]
    OldPosition: core_uobject.Vector
    PartSysVelocity: core_uobject.Vector
    WarmupTime: float
    WarmupTickRate: float
    SecondsBeforeInactive: float
    MaxTimeBeforeForceUpdateTransform: float
    ReplayClips: unreal.WrappedArray[ParticleSystemReplay]
    CustomTimeDilation: float
    ParameterEvaluationContext: unreal.UObject
    ParameterEvaluationOverrideContext: unreal.UObject
    AutoAttachParent: SceneComponent
    AutoAttachSocketName: str
    AutoAttachLocationRule: EAttachmentRule
    AutoAttachRotationRule: EAttachmentRule
    AutoAttachScaleRule: EAttachmentRule
    bIgnoredByFXCoordinator: bool
    bPersistAfterOwnerIsDestroyed: bool
    NamedMaterials: unreal.WrappedArray[MaterialInterface]
    def SetVectorParameter(self, ParameterName: str, Param: core_uobject.Vector): ...
    def SetTrailSourceData(self, InFirstSocketName: str, InSecondSocketName: str, InWidthMode: int, InWidth: float): ...
    def SetTemplate(self, NewTemplate: ParticleSystem): ...
    def SetMaterialParameter(self, ParameterName: str, Param: MaterialInterface): ...
    def SetFloatParameter(self, ParameterName: str, Param: float): ...
    def SetEmitterEnable(self, EmitterName: str, bNewEnableState: bool): ...
    def SetColorParameter(self, ParameterName: str, Param: core_uobject.LinearColor): ...
    def SetBeamTargetTangent(self, EmitterName: str, NewTangentPoint: core_uobject.Vector, TargetIndex: int): ...
    def SetBeamTargetStrength(self, EmitterName: str, NewTargetStrength: float, TargetIndex: int): ...
    def SetBeamTargetPoint(self, EmitterName: str, NewTargetPoint: core_uobject.Vector, TargetIndex: int): ...
    def SetBeamTarget(self, AttachmentType: EBeamAttachmentType, EmitterName: str, Actor: Actor, Component: SceneComponent, Socket: str, Location: core_uobject.Vector): ...
    def SetBeamSourceTangent(self, EmitterName: str, NewTangentPoint: core_uobject.Vector, SourceIndex: int): ...
    def SetBeamSourceStrength(self, EmitterName: str, NewSourceStrength: float, SourceIndex: int): ...
    def SetBeamSourcePoint(self, EmitterName: str, NewSourcePoint: core_uobject.Vector, SourceIndex: int): ...
    def SetBeamSource(self, AttachmentType: EBeamAttachmentType, EmitterName: str, Actor: Actor, Component: SceneComponent, Socket: str, Location: core_uobject.Vector): ...
    def SetBeamEndPoint(self, EmitterName: str, NewEndPoint: core_uobject.Vector): ...
    def SetAutoAttachParams(self, Parent: SceneComponent, SocketName: str, LocationType: int): ...
    def SetAutoAttachmentParameters(self, Parent: SceneComponent, SocketName: str, LocationRule: EAttachmentRule, RotationRule: EAttachmentRule, ScaleRule: EAttachmentRule): ...
    def SetActorParameter(self, ParameterName: str, Param: Actor): ...
    def ReleaseToPool(self): ...
    def GetVectorParameter(self, InName: str, OutVector: core_uobject.Vector, ReturnValue: bool) -> bool: ...
    def GetNumActiveParticles(self, ReturnValue: int) -> int: ...
    def GetNamedMaterial(self, InName: str, ReturnValue: MaterialInterface) -> MaterialInterface: ...
    def GetMaterialParameter(self, InName: str, OutMaterial: MaterialInterface, ReturnValue: bool) -> bool: ...
    def GetFloatParameter(self, InName: str, OutFloat: float, ReturnValue: bool) -> bool: ...
    def GetColorParameter(self, InName: str, OutColor: core_uobject.LinearColor, ReturnValue: bool) -> bool: ...
    def GetBeamTargetTangent(self, EmitterIndex: int, TargetIndex: int, OutTangentPoint: core_uobject.Vector, ReturnValue: bool) -> bool: ...
    def GetBeamTargetStrength(self, EmitterIndex: int, TargetIndex: int, OutTargetStrength: float, ReturnValue: bool) -> bool: ...
    def GetBeamTargetPoint(self, EmitterIndex: int, TargetIndex: int, OutTargetPoint: core_uobject.Vector, ReturnValue: bool) -> bool: ...
    def GetBeamSourceTangent(self, EmitterIndex: int, SourceIndex: int, OutTangentPoint: core_uobject.Vector, ReturnValue: bool) -> bool: ...
    def GetBeamSourceStrength(self, EmitterIndex: int, SourceIndex: int, OutSourceStrength: float, ReturnValue: bool) -> bool: ...
    def GetBeamSourcePoint(self, EmitterIndex: int, SourceIndex: int, OutSourcePoint: core_uobject.Vector, ReturnValue: bool) -> bool: ...
    def GetBeamEndPoint(self, EmitterIndex: int, OutEndPoint: core_uobject.Vector, ReturnValue: bool) -> bool: ...
    def GetActorParameter(self, InName: str, OutActor: Actor, ReturnValue: bool) -> bool: ...
    def GenerateParticleEvent(self, InEventName: str, InEmitterTime: float, InLocation: core_uobject.Vector, InDirection: core_uobject.Vector, InVelocity: core_uobject.Vector, Color: core_uobject.LinearColor, DynamicParameter: core_uobject.LinearColor): ...
    def EndTrails(self): ...
    def CreateNamedDynamicMaterialInstance(self, InName: str, SourceMaterial: MaterialInterface, ReturnValue: MaterialInstanceDynamic) -> MaterialInstanceDynamic: ...
    def BeginTrails(self, InFirstSocketName: str, InSecondSocketName: str, InWidthMode: int, InWidth: float): ...


class ParticleSystemReplay(unreal.UObject):
    ClipIDNumber: int



class PathFollowingAgentInterface(core_uobject.Interface): ...


class PawnNoiseEmitterComponent(ActorComponent):
    bAIPerceptionSystemCompatibilityMode: bool
    LastRemoteNoisePosition: core_uobject.Vector
    NoiseLifetime: float
    LastRemoteNoiseVolume: float
    LastRemoteNoiseTime: float
    LastLocalNoiseVolume: float
    LastLocalNoiseTime: float
    def MakeNoise(self, NoiseMaker: Actor, Loudness: float, NoiseLocation: core_uobject.Vector): ...


class PerfMapVolume(Volume): ...


class PhysicalAnimationComponent(ActorComponent):
    StrengthMultiplyer: float
    SkeletalMeshComponent: SkeletalMeshComponent
    def SetStrengthMultiplyer(self, InStrengthMultiplyer: float): ...
    def SetSkeletalMeshComponent(self, InSkeletalMeshComponent: SkeletalMeshComponent): ...
    def GetBodyTargetTransform(self, BodyName: str, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def ApplyPhysicalAnimationSettingsBelow(self, BodyName: str, PhysicalAnimationData: PhysicalAnimationData, bIncludeSelf: bool): ...
    def ApplyPhysicalAnimationSettings(self, BodyName: str, PhysicalAnimationData: PhysicalAnimationData): ...
    def ApplyPhysicalAnimationProfileBelow(self, BodyName: str, ProfileName: str, bIncludeSelf: bool, bClearNotFound: bool): ...


class PhysicalMaterial(unreal.UObject):
    Friction: float
    FrictionCombineMode: int
    bOverrideFrictionCombineMode: bool
    Restitution: float
    RestitutionCombineMode: int
    bOverrideRestitutionCombineMode: bool
    Density: float
    RaiseMassToPower: float
    DestructibleDamageThresholdScale: float
    PhysicalMaterialProperty: PhysicalMaterialPropertyBase
    SurfaceType: int
    TireFrictionScale: float
    TireFrictionScales: unreal.WrappedArray[TireFrictionScalePair]



class PhysicalMaterialPropertyBase(unreal.UObject): ...


class PhysicsAsset(unreal.UObject):
    BoundsBodies: unreal.WrappedArray[int]
    SkeletalBodySetups: unreal.WrappedArray[SkeletalBodySetup]
    ConstraintSetup: unreal.WrappedArray[PhysicsConstraintTemplate]
    bUseAsyncScene: bool
    bNotForDedicatedServer: bool
    ThumbnailInfo: ThumbnailInfo
    BodySetup: unreal.WrappedArray[BodySetup]



class SkeletalBodySetup(BodySetup):
    bSkipScaleFromAnimation: bool
    PhysicalAnimationData: unreal.WrappedArray[PhysicalAnimationProfile]



class PhysicsCollisionHandler(unreal.UObject):
    ImpactThreshold: float
    ImpactReFireDelay: float
    DefaultImpactSound: SoundBase
    LastImpactSoundTime: float



class RigidBodyBase(Actor): ...


class PhysicsConstraintActor(RigidBodyBase):
    ConstraintComp: PhysicsConstraintComponent
    ConstraintActor1: Actor
    ConstraintActor2: Actor
    bDisableCollision: bool



class PhysicsConstraintComponent(SceneComponent):
    ConstraintActor1: Actor
    ComponentName1: ConstrainComponentPropName
    ConstraintActor2: Actor
    ComponentName2: ConstrainComponentPropName
    ConstraintSetup: PhysicsConstraintTemplate
    ConstraintInstance: ConstraintInstance
    def SetOrientationDriveTwistAndSwing(self, bEnableTwistDrive: bool, bEnableSwingDrive: bool): ...
    def SetOrientationDriveSLERP(self, bEnableSLERP: bool): ...
    def SetLinearZLimit(self, ConstraintType: int, LimitSize: float): ...
    def SetLinearYLimit(self, ConstraintType: int, LimitSize: float): ...
    def SetLinearXLimit(self, ConstraintType: int, LimitSize: float): ...
    def SetLinearVelocityTarget(self, InVelTarget: core_uobject.Vector): ...
    def SetLinearVelocityDrive(self, bEnableDriveX: bool, bEnableDriveY: bool, bEnableDriveZ: bool): ...
    def SetLinearPositionTarget(self, InPosTarget: core_uobject.Vector): ...
    def SetLinearPositionDrive(self, bEnableDriveX: bool, bEnableDriveY: bool, bEnableDriveZ: bool): ...
    def SetLinearDriveParams(self, PositionStrength: float, VelocityStrength: float, InForceLimit: float): ...
    def SetLinearBreakable(self, bLinearBreakable: bool, LinearBreakThreshold: float): ...
    def SetDisableCollision(self, bDisableCollision: bool): ...
    def SetConstraintReferencePosition(self, Frame: int, RefPosition: core_uobject.Vector): ...
    def SetConstraintReferenceOrientation(self, Frame: int, PriAxis: core_uobject.Vector, SecAxis: core_uobject.Vector): ...
    def SetConstraintReferenceFrame(self, Frame: int, RefFrame: core_uobject.Transform): ...
    def SetConstrainedComponents(self, Component1: PrimitiveComponent, BoneName1: str, Component2: PrimitiveComponent, BoneName2: str): ...
    def SetAngularVelocityTarget(self, InVelTarget: core_uobject.Vector): ...
    def SetAngularVelocityDriveTwistAndSwing(self, bEnableTwistDrive: bool, bEnableSwingDrive: bool): ...
    def SetAngularVelocityDriveSLERP(self, bEnableSLERP: bool): ...
    def SetAngularVelocityDrive(self, bEnableSwingDrive: bool, bEnableTwistDrive: bool): ...
    def SetAngularTwistLimit(self, ConstraintType: int, TwistLimitAngle: float): ...
    def SetAngularSwing2Limit(self, MotionType: int, Swing2LimitAngle: float): ...
    def SetAngularSwing1Limit(self, MotionType: int, Swing1LimitAngle: float): ...
    def SetAngularOrientationTarget(self, InPosTarget: core_uobject.Rotator): ...
    def SetAngularOrientationDrive(self, bEnableSwingDrive: bool, bEnableTwistDrive: bool): ...
    def SetAngularDriveParams(self, PositionStrength: float, VelocityStrength: float, InForceLimit: float): ...
    def SetAngularDriveMode(self, DriveMode: int): ...
    def SetAngularBreakable(self, bAngularBreakable: bool, AngularBreakThreshold: float): ...
    def IsConstraintActive(self, ReturnValue: bool) -> bool: ...
    def IsBroken(self, ReturnValue: bool) -> bool: ...
    def GetCurrentTwist(self, ReturnValue: float) -> float: ...
    def GetCurrentSwing2(self, ReturnValue: float) -> float: ...
    def GetCurrentSwing1(self, ReturnValue: float) -> float: ...
    def GetConstraintForce(self, OutLinearForce: core_uobject.Vector, OutAngularForce: core_uobject.Vector): ...
    def BreakConstraint(self): ...


class PhysicsConstraintTemplate(unreal.UObject):
    DefaultInstance: ConstraintInstance
    ProfileHandles: unreal.WrappedArray[PhysicsConstraintProfileHandle]
    DefaultProfile: ConstraintProfileProperties



class PhysicsHandleComponent(ActorComponent):
    GrabbedComponent: PrimitiveComponent
    bSoftAngularConstraint: bool
    bSoftLinearConstraint: bool
    bInterpolateTarget: bool
    LinearDamping: float
    LinearStiffness: float
    AngularDamping: float
    AngularStiffness: float
    InterpolationSpeed: float
    def SetTargetRotation(self, NewRotation: core_uobject.Rotator): ...
    def SetTargetLocationAndRotation(self, NewLocation: core_uobject.Vector, NewRotation: core_uobject.Rotator): ...
    def SetTargetLocation(self, NewLocation: core_uobject.Vector): ...
    def SetLinearStiffness(self, NewLinearStiffness: float): ...
    def SetLinearDamping(self, NewLinearDamping: float): ...
    def SetInterpolationSpeed(self, NewInterpolationSpeed: float): ...
    def SetAngularStiffness(self, NewAngularStiffness: float): ...
    def SetAngularDamping(self, NewAngularDamping: float): ...
    def ReleaseComponent(self): ...
    def GrabComponentAtLocationWithRotation(self, Component: PrimitiveComponent, InBoneName: str, Location: core_uobject.Vector, Rotation: core_uobject.Rotator): ...
    def GrabComponentAtLocation(self, Component: PrimitiveComponent, InBoneName: str, GrabLocation: core_uobject.Vector): ...
    def GrabComponent(self, Component: PrimitiveComponent, InBoneName: str, GrabLocation: core_uobject.Vector, bConstrainRotation: bool): ...
    def GetTargetLocationAndRotation(self, TargetLocation: core_uobject.Vector, TargetRotation: core_uobject.Rotator): ...
    def GetGrabbedComponent(self, ReturnValue: PrimitiveComponent) -> PrimitiveComponent: ...


class PhysicsSettings(DeveloperSettings):
    DefaultGravityZ: float
    DefaultTerminalVelocity: float
    DefaultFluidFriction: float
    SimulateScratchMemorySize: int
    RagdollAggregateThreshold: int
    TriangleMeshTriangleMinAreaThreshold: float
    bEnableAsyncScene: bool
    bEnableShapeSharing: bool
    bEnablePCM: bool
    bEnableStabilization: bool
    bWarnMissingLocks: bool
    bEnable2DPhysics: bool
    PhysicErrorCorrection: RigidBodyErrorCorrection
    LockedAxis: int
    DefaultDegreesOfFreedom: int
    BounceThresholdVelocity: float
    FrictionCombineMode: int
    RestitutionCombineMode: int
    MaxAngularVelocity: float
    MaxDepenetrationVelocity: float
    ContactOffsetMultiplier: float
    MinContactOffset: float
    MaxContactOffset: float
    bSimulateSkeletalMeshOnDedicatedServer: bool
    DefaultShapeComplexity: int
    bDefaultHasComplexCollision: bool
    bSuppressFaceRemapTable: bool
    bSupportUVFromHitResults: bool
    bDisableActiveActors: bool
    bDisableKinematicStaticPairs: bool
    bDisableKinematicKinematicPairs: bool
    bDisableCCD: bool
    bEnableEnhancedDeterminism: bool
    MaxPhysicsDeltaTime: float
    bSubstepping: bool
    bSubsteppingAsync: bool
    MaxSubstepDeltaTime: float
    MaxSubsteps: int
    SyncSceneSmoothingFactor: float
    AsyncSceneSmoothingFactor: float
    InitialAverageFrameRate: float
    PhysXTreeRebuildRate: int
    PhysicalSurfaces: unreal.WrappedArray[PhysicalSurfaceName]
    DefaultBroadphaseSettings: BroadphaseSettings
    WheelFullUpdateDist: float
    WheelUpdateByTraceDist: float
    WheelMinimalUpdateDist: float
    WheelFullUpdateDelta: float
    WheelMinimalUpdateDelta: float
    WheelSweepsRadialScale: float
    WheelSweepsWidthScale: float
    WheelContactsNoImpulseAngle: float
    BroadPhaseType: EBroadPhaseType
    StaticPruningStructure: EStaticPruningStructure



class PhysicsSpringComponent(SceneComponent):
    SpringStiffness: float
    SpringDamping: float
    SpringLengthAtRest: float
    SpringRadius: float
    SpringChannel: int
    bIgnoreSelf: bool
    SpringCompression: float
    def GetSpringRestingPoint(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetSpringDirection(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetSpringCurrentEndPoint(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetNormalizedCompressionScalar(self, ReturnValue: float) -> float: ...


class PhysicsThruster(RigidBodyBase):
    ThrusterComponent: PhysicsThrusterComponent



class PhysicsThrusterComponent(SceneComponent):
    ThrustStrength: float



class SceneCapture(Actor):
    MeshComp: StaticMeshComponent



class PlanarReflection(SceneCapture):
    PlanarReflectionComponent: PlanarReflectionComponent
    bShowPreviewPlane: bool
    def OnInterpToggle(self, bEnable: bool): ...


class SceneCaptureComponent(SceneComponent):
    PrimitiveRenderMode: ESceneCapturePrimitiveRenderMode
    HiddenComponents: unreal.WrappedArray[PrimitiveComponent]
    HiddenActors: unreal.WrappedArray[Actor]
    ShowOnlyComponents: unreal.WrappedArray[PrimitiveComponent]
    ShowOnlyActors: unreal.WrappedArray[Actor]
    bCaptureEveryFrame: bool
    bCaptureOnMovement: bool
    bAlwaysPersistRenderingState: bool
    LODDistanceFactor: float
    MaxViewDistanceOverride: float
    CaptureSortPriority: int
    bGbxRuntimeCapture: bool
    bGbxShouldOutputHDR: bool
    bGbxIsLoadingScene: bool
    bPersistentSceneRenderer: bool
    bForceTonemapAlphaWhite: bool
    bDisablePrePass: bool
    bDisableFrustumCulling: bool
    bMinimalBasePass: bool
    bUnlitSimpleScene: bool
    bNoWorldTick: bool
    bUseBudgetedPersistentRendering: bool
    bOverrideViewLocationAndRotation: bool
    OverrideViewLocation: core_uobject.Vector
    OverrideViewRotation: core_uobject.Rotator
    DebugID: int
    ViewOwnerLocationWS: core_uobject.Vector
    bDisableGrainQuantization: bool
    ShowFlagSettings: unreal.WrappedArray[EngineShowFlagsSetting]
    ProfilingEventName: str
    def ShowOnlyComponent(self, InComponent: PrimitiveComponent): ...
    def ShowOnlyActorComponents(self, InActor: Actor): ...
    def SetCaptureSortPriority(self, NewCaptureSortPriority: int): ...
    def RemoveShowOnlyComponent(self, InComponent: PrimitiveComponent): ...
    def RemoveShowOnlyActorComponents(self, InActor: Actor): ...
    def HideComponent(self, InComponent: PrimitiveComponent): ...
    def HideActorComponents(self, InActor: Actor): ...
    def ClearShowOnlyComponents(self, InComponent: PrimitiveComponent): ...
    def ClearHiddenComponents(self): ...


class PlanarReflectionComponent(SceneCaptureComponent):
    PreviewBox: BoxComponent
    NormalDistortionStrength: float
    PrefilterRoughness: float
    PrefilterRoughnessDistance: float
    ScreenPercentage: int
    ExtraFOV: float
    DistanceFromPlaneFadeStart: float
    DistanceFromPlaneFadeEnd: float
    DistanceFromPlaneFadeoutStart: float
    DistanceFromPlaneFadeoutEnd: float
    AngleFromPlaneFadeStart: float
    AngleFromPlaneFadeEnd: float
    bRenderSceneTwoSided: bool



class PlaneReflectionCapture(ReflectionCapture): ...


class PlaneReflectionCaptureComponent(ReflectionCaptureComponent):
    InfluenceRadiusScale: float
    PreviewInfluenceRadius: DrawSphereComponent
    PreviewCaptureBox: BoxComponent



class PlatformEventsComponent(ActorComponent):

    def SupportsConvertibleLaptops(self, ReturnValue: bool) -> bool: ...
    def PlatformEventDelegate__DelegateSignature(self): ...
    def IsInTabletMode(self, ReturnValue: bool) -> bool: ...
    def IsInLaptopMode(self, ReturnValue: bool) -> bool: ...


class PlatformInterfaceWebResponse(unreal.UObject):
    OriginalURL: str
    ResponseCode: int
    Tag: int
    StringResponse: str
    BinaryResponse: unreal.WrappedArray[int]
    def GetNumHeaders(self, ReturnValue: int) -> int: ...
    def GetHeaderValue(self, HeaderName: str, ReturnValue: str) -> str: ...
    def GetHeader(self, HeaderIndex: int, Header: str, Value: str): ...


class PlayerStart(NavigationObjectBase):
    PlayerStartTag: str



class PlayerStartPIE(PlayerStart): ...


class PluginCommandlet(Commandlet): ...


class PointLight(Light):
    PointLightComponent: PointLightComponent
    def SetRadius(self, NewRadius: float): ...
    def SetLightFalloffExponent(self, NewLightFalloffExponent: float): ...


class PointLightComponent(LocalLightComponent):
    bUseInverseSquaredFalloff: bool
    LightFalloffExponent: float
    SourceRadius: float
    SoftSourceRadius: float
    SourceLength: float
    OrientedBoxComponent: GbxOrientedBoxComponent
    bAccumulateLightDistortion: bool
    def SetUseInverseSquaredFalloff(self, NewValue: bool): ...
    def SetSourceRadius(self, bNewValue: float): ...
    def SetSourceLength(self, NewValue: float): ...
    def SetSoftSourceRadius(self, bNewValue: float): ...
    def SetLightFalloffExponent(self, NewLightFalloffExponent: float): ...


class Polys(unreal.UObject): ...


class PoseableMeshComponent(SkinnedMeshComponent):

    def SetBoneTransformByName(self, BoneName: str, InTransform: core_uobject.Transform, BoneSpace: int): ...
    def SetBoneScaleByName(self, BoneName: str, InScale3D: core_uobject.Vector, BoneSpace: int): ...
    def SetBoneRotationByName(self, BoneName: str, InRotation: core_uobject.Rotator, BoneSpace: int): ...
    def SetBoneLocationByName(self, BoneName: str, InLocation: core_uobject.Vector, BoneSpace: int): ...
    def ResetBoneTransformByName(self, BoneName: str): ...
    def GetBoneTransformByName(self, BoneName: str, BoneSpace: int, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def GetBoneScaleByName(self, BoneName: str, BoneSpace: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetBoneRotationByName(self, BoneName: str, BoneSpace: int, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...
    def GetBoneLocationByName(self, BoneName: str, BoneSpace: int, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def CopyPoseFromSkeletalComponent(self, InComponentToCopy: SkeletalMeshComponent): ...


class PoseAsset(AnimationAsset):
    PoseContainer: PoseDataContainer
    bAdditivePose: bool
    BasePoseIndex: int
    RetargetSource: str



class PoseWatch(unreal.UObject):
    Node: EdGraphNode
    PoseWatchColour: core_uobject.Color



class PostProcessComponent(SceneComponent):
    Settings: PostProcessSettings
    Priority: float
    BlendRadius: float
    BlendWeight: float
    bEnabled: bool
    bUnbound: bool



class PostProcessSettingsTemplate(unreal.UObject):
    Settings: PostProcessSettingsWithBlocker



class PostProcessVolume(Volume):
    Settings: PostProcessSettingsWithInheritance
    Priority: float
    BlendRadius: float
    BlendWeight: float
    bEnabled: bool
    bUnbound: bool



class PrecomputedVisibilityOverrideVolume(Volume):
    OverrideVisibleActors: unreal.WrappedArray[Actor]
    OverrideInvisibleActors: unreal.WrappedArray[Actor]
    OverrideInvisibleLevels: unreal.WrappedArray[str]



class PrecomputedVisibilityVolume(Volume): ...


class PreviewCollectionInterface(core_uobject.Interface): ...


class PreviewMeshCollection(DataAsset):
    Skeleton: Skeleton
    SkeletalMeshes: unreal.WrappedArray[PreviewMeshCollectionEntry]



class ProxyLODMeshSimplificationSettings(DeveloperSettings):
    ProxyLODMeshReductionModuleName: str



class RadialForceActor(RigidBodyBase):
    ForceComponent: RadialForceComponent
    def ToggleForce(self): ...
    def FireImpulse(self): ...
    def EnableForce(self): ...
    def DisableForce(self): ...


class RadialForceComponent(SceneComponent):
    Radius: float
    Falloff: int
    ImpulseStrength: float
    bImpulseVelChange: bool
    bIgnoreOwningActor: bool
    ForceStrength: float
    DestructibleDamage: float
    ObjectTypesToAffect: unreal.WrappedArray[int]
    def RemoveObjectTypeToAffect(self, ObjectType: int): ...
    def FireImpulse(self): ...
    def AddObjectTypeToAffect(self, ObjectType: int): ...


class RectLight(Light):
    RectLightComponent: RectLightComponent



class RectLightComponent(LocalLightComponent):
    SourceWidth: float
    SourceHeight: float
    OrientedBoxComponent: GbxOrientedBoxComponent
    def SetSourceWidth(self, bNewValue: float): ...
    def SetSourceHeight(self, NewValue: float): ...


class RegionOfInterest(BoxComponent): ...


class RendererSettings(DeveloperSettings):
    bMobileHDR: bool
    bMobileDisableVertexFog: bool
    MaxMobileCascades: int
    MobileMSAASampleCount: int
    bMobileUseLegacyShadingModel: bool
    bDiscardUnusedQualityLevels: bool
    bOcclusionCulling: bool
    MinScreenRadiusForLights: float
    MinScreenRadiusForEarlyZPass: float
    MinScreenRadiusForCSMdepth: float
    bPrecomputedVisibilityWarning: bool
    bTextureStreaming: bool
    bUseDXT5NormalMaps: bool
    bClearCoatEnableSecondNormal: bool
    ReflectionCaptureResolution: int
    ReflectionEnvironmentLightmapMixBasedOnRoughness: bool
    bForwardShading: bool
    bVertexFoggingForOpaque: bool
    bAllowStaticLighting: bool
    bAllowVelocityBuffer: bool
    bAllowReflectiveShadowMaps: bool
    bFullQualitySphericalHarmonics: bool
    bCaptureAmbientCubemapInReflectionEnvironment: bool
    bUseNormalMapsForStaticLighting: bool
    bGenerateMeshDistanceFields: bool
    bEightBitMeshDistanceFields: bool
    bGenerateLandscapeGIData: bool
    bCompressMeshDistanceFields: bool
    MaxGameNits: float
    bAllowTessellation: bool
    TessellationAdaptivePixelsPerTriangle: float
    bSeparateTranslucency: bool
    TranslucentSortPolicy: int
    TranslucentSortAxis: core_uobject.Vector
    CustomDepthStencil: int
    bCustomDepthTaaJitter: bool
    bEnableAlphaChannelInPostProcessing: int
    bUseNewAlgorithm: bool
    bUsePreExposure: bool
    bDefaultFeatureBloom: bool
    bDefaultFeatureAmbientOcclusion: bool
    bDefaultFeatureAmbientOcclusionStaticFraction: bool
    bDefaultFeatureAutoExposure: bool
    DefaultFeatureAutoExposure: int
    bDefaultFeatureMotionBlur: bool
    bDefaultFeatureLensFlare: bool
    bTemporalUpsampling: bool
    DefaultFeatureAntiAliasing: int
    DefaultPointLightUnits: ELightUnits
    DefaultSpotLightUnits: ELightUnits
    DefaultBackBufferPixelFormat: int
    bRenderUnbuiltPreviewShadowsInGame: bool
    bStencilForLODDither: bool
    EarlyZPass: int
    bEarlyZPassMovable: bool
    bEarlyZPassOnlyMaterialMasking: bool
    bDBuffer: bool
    ClearSceneMethod: int
    bBasePassOutputsVelocity: bool
    bSelectiveBasePassOutputs: bool
    bDefaultParticleCutouts: bool
    GPUSimulationTextureSizeX: int
    GPUSimulationTextureSizeY: int
    bGlobalClipPlane: bool
    GBufferFormat: int
    bUseGPUMorphTargets: bool
    bNvidiaAftermathEnabled: bool
    bInstancedStereo: bool
    bMultiView: bool
    bMobileMultiView: bool
    bMobileMultiViewDirect: bool
    bMonoscopicFarField: bool
    bODSCapture: bool
    bDebugCanvasInLayer: bool
    WireframeCullThreshold: float
    bSupportStationarySkylight: bool
    bSupportLowQualityLightmaps: bool
    bSupportPointLightWholeSceneShadows: bool
    bSupportAtmosphericFog: bool
    bSupportSkinCacheShaders: bool
    bMobileEnableStaticAndCSMShadowReceivers: bool
    bMobileEnableMovableLightCSMShaderCulling: bool
    bMobileAllowDistanceFieldShadows: bool
    bMobileAllowMovableDirectionalLights: bool
    bMobileDynamicPointLightsUseStaticBranch: bool
    SkinCacheSceneMemoryLimitInMB: float
    bGPUSkinLimit2BoneInfluences: bool
    bSupportDepthOnlyIndexBuffers: bool
    bSupportReversedIndexBuffers: bool
    bSupportMaterialLayers: bool



class RendererOverrideSettings(DeveloperSettings):
    bSupportAllShaderPermutations: bool
    bForceRecomputeTangents: bool



class ReporterBase(unreal.UObject): ...


class ReporterGraph(ReporterBase): ...


class ReverbEffect(unreal.UObject):
    Density: float
    Diffusion: float
    Gain: float
    GainHF: float
    DecayTime: float
    DecayHFRatio: float
    ReflectionsGain: float
    ReflectionsDelay: float
    LateGain: float
    LateDelay: float
    AirAbsorptionGainHF: float
    RoomRolloffFactor: float



class Rig(unreal.UObject):
    TransformBases: unreal.WrappedArray[TransformBase]
    Nodes: unreal.WrappedArray[Node]



class RigidBodyErrorCorrectionProviderInterface(core_uobject.Interface): ...


class RotatingMovementComponent(MovementComponent):
    bUseRotationInterpolation: bool
    RotationRate: core_uobject.Rotator
    TotalRotation: core_uobject.Rotator
    Duration: float
    PivotTranslation: core_uobject.Vector
    bRotationInLocalSpace: bool
    def StartTotalRotationFromCurrentPosition(self, Rotation: core_uobject.Rotator, RotationDuration: float): ...
    def SetDuration(self, RotationDuration: float): ...


class RVOAvoidanceInterface(core_uobject.Interface): ...


class Scene(unreal.UObject): ...


class SceneCapture2D(SceneCapture):
    CaptureComponent2D: SceneCaptureComponent2D
    DrawFrustum: DrawFrustumComponent
    def OnInterpToggle(self, bEnable: bool): ...


class SceneCaptureComponent2D(SceneCaptureComponent):
    ProjectionType: int
    FOVAngle: float
    OrthoWidth: float
    TextureTarget: TextureRenderTarget2D
    CaptureSource: int
    CompositeMode: int
    PostProcessSettings: PostProcessSettings
    PostProcessBlendWeight: float
    bUseCustomProjectionMatrix: bool
    CustomProjectionMatrix: core_uobject.Matrix
    bEnableClipPlane: bool
    ClipPlaneBase: core_uobject.Vector
    ClipPlaneNormal: core_uobject.Vector
    bCameraCutThisFrame: bool
    def CaptureSceneDeferred(self): ...
    def CaptureScene(self): ...


class SceneCaptureComponentCube(SceneCaptureComponent):
    TextureTarget: TextureRenderTargetCube
    TextureTargetLeft: TextureRenderTargetCube
    TextureTargetRight: TextureRenderTargetCube
    TextureTargetODS: TextureRenderTarget2D
    IPD: float
    CaptureSource: int
    CompositeMode: int
    def CaptureScene(self): ...


class SceneCaptureCube(SceneCapture):
    CaptureComponentCube: SceneCaptureComponentCube
    DrawFrustum: DrawFrustumComponent
    def OnInterpToggle(self, bEnable: bool): ...


class ClassActorThumbnailRenderer(Actor):

    def TickScene(self, DeltaTime: float): ...
    def SpawnActorCenteredFromClass(self, Actor: unreal.UClass): ...
    def SpawnActorCentered(self, Object: Actor): ...
    def Render(self, RenderTarget: TextureRenderTarget2D, Parameters: ThumbnailParameters): ...
    def ClearWorld(self): ...


class SCS_Node(unreal.UObject):
    ComponentClass: unreal.UClass
    ComponentTemplate: ActorComponent
    CookedComponentInstancingData: BlueprintCookedComponentInstancingData
    VariableName: str
    AttachToName: str
    ParentComponentOrVariableName: str
    ParentComponentOwnerClassName: str
    bIsParentComponentNative: bool
    ChildNodes: unreal.WrappedArray[SCS_Node]
    MetaDataArray: unreal.WrappedArray[BPVariableMetaDataEntry]
    VariableGuid: core_uobject.Guid
    bIsFalseRoot: bool
    bIsNative: bool
    NativeComponentName: str
    bVariableNameAutoGenerated: bool
    InternalVariableName: str



class Selection(unreal.UObject): ...


class ServerStatReplicator(Info):
    bUpdateStatNet: bool
    bOverwriteClientStats: bool



class ShadowMapTexture2D(Texture2D):
    ShadowmapFlags: int



class SimpleConstructionScript(unreal.UObject):
    RootNodes: unreal.WrappedArray[SCS_Node]
    AllNodes: unreal.WrappedArray[SCS_Node]
    DefaultSceneRootNode: SCS_Node
    RootNode: SCS_Node
    ActorComponentNodes: unreal.WrappedArray[SCS_Node]



class SkeletalMeshActor(Actor):
    bSkeletalActorIsPoseOnly: bool
    bShouldDoAnimNotifies: bool
    bWakeOnLevelStart: bool
    SkeletalMeshComponent: SkeletalMeshComponent
    ReplicatedMesh: SkeletalMesh
    ReplicatedPhysAsset: PhysicsAsset
    ReplicatedMaterial1: MaterialInterface
    def OnRep_ReplicatedPhysAsset(self): ...
    def OnRep_ReplicatedMesh(self): ...
    def OnRep_ReplicatedMaterial1(self): ...


class SkeletalMeshLODSettings(DataAsset):
    MinLOD: PerPlatformInt
    LODGroups: unreal.WrappedArray[SkeletalMeshLODGroupSettings]



class SkeletalMeshSocket(unreal.UObject):
    SocketName: str
    BoneName: str
    RelativeLocation: core_uobject.Vector
    RelativeRotation: core_uobject.Rotator
    RelativeScale: core_uobject.Vector
    bForceAlwaysAnimated: bool
    BoxExtent: core_uobject.Vector
    def InitializeSocketFromLocation(self, SkelComp: SkeletalMeshComponent, WorldLocation: core_uobject.Vector, WorldNormal: core_uobject.Vector): ...
    def GetSocketLocation(self, SkelComp: SkeletalMeshComponent, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...


class SkyLight(Info):
    LightComponent: SkyLightComponent
    bEnabled: bool
    def OnRep_bEnabled(self): ...


class SkyLightComponent(LightComponentBase):
    SourceType: int
    Cubemap: TextureCube
    SourceCubemapAngle: float
    CubemapResolution: int
    SkyDistanceThreshold: float
    bCaptureEmissiveOnly: bool
    bRealtimeSky: bool
    bGroundBounce: bool
    GroundColor: core_uobject.Color
    bLowerHemisphereIsBlack: bool
    bCaptureEmissiveIrradiance: bool
    LowerHemisphereColor: core_uobject.LinearColor
    OcclusionMaxDistance: float
    Contrast: float
    OcclusionExponent: float
    MinOcclusion: float
    OcclusionTint: core_uobject.Color
    OcclusionCombineMode: int
    BlendDestinationCubemap: TextureCube
    def SetVolumetricScatteringIntensity(self, NewIntensity: float): ...
    def SetOcclusionTint(self, InTint: core_uobject.Color): ...
    def SetOcclusionExponent(self, InOcclusionExponent: float): ...
    def SetOcclusionContrast(self, InOcclusionContrast: float): ...
    def SetMinOcclusion(self, InMinOcclusion: float): ...
    def SetLowerHemisphereColor(self, InLowerHemisphereColor: core_uobject.LinearColor): ...
    def SetLightColor(self, NewLightColor: core_uobject.LinearColor): ...
    def SetIntensity(self, NewIntensity: float): ...
    def SetIndirectLightingIntensity(self, NewIntensity: float): ...
    def SetCubemapBlend(self, SourceCubemap: TextureCube, DestinationCubemap: TextureCube, InBlendFraction: float): ...
    def SetCubemap(self, NewCubemap: TextureCube): ...
    def RecaptureSky(self): ...


class SlateBrushAsset(unreal.UObject):
    Brush: slate_core.SlateBrush



class SlateTextureAtlasInterface(core_uobject.Interface): ...


class SmokeTestCommandlet(Commandlet): ...


class SoundAttenuation(unreal.UObject):
    Attenuation: SoundAttenuationSettings



class SoundClass(unreal.UObject):
    Properties: SoundClassProperties
    ChildClasses: unreal.WrappedArray[SoundClass]
    PassiveSoundMixModifiers: unreal.WrappedArray[PassiveSoundMixModifier]
    ParentClass: SoundClass



class SoundConcurrency(unreal.UObject):
    Concurrency: SoundConcurrencySettings



class SoundCue(SoundBase):
    bOverrideAttenuation: bool
    bExcludeFromRandomNodeBranchCulling: bool
    FirstNode: SoundNode
    VolumeMultiplier: float
    PitchMultiplier: float
    AttenuationOverrides: SoundAttenuationSettings
    SubtitlePriority: float



class SoundEffectPreset(unreal.UObject): ...


class SoundEffectSourcePreset(SoundEffectPreset): ...


class SoundEffectSourcePresetChain(unreal.UObject):
    Chain: unreal.WrappedArray[SourceEffectChainEntry]
    bPlayEffectChainTails: bool



class SoundEffectSubmixPreset(SoundEffectPreset): ...


class SoundGroups(unreal.UObject):
    SoundGroupProfiles: unreal.WrappedArray[SoundGroup]



class SoundMix(unreal.UObject):
    bApplyEQ: bool
    EQPriority: float
    EQSettings: AudioEQEffect
    SoundClassEffects: unreal.WrappedArray[SoundClassAdjuster]
    InitialDelay: float
    FadeInTime: float
    Duration: float
    FadeOutTime: float



class SoundNode(unreal.UObject):
    ChildNodes: unreal.WrappedArray[SoundNode]



class SoundNodeAssetReferencer(SoundNode): ...


class SoundNodeAttenuation(SoundNode):
    AttenuationSettings: SoundAttenuation
    AttenuationOverrides: SoundAttenuationSettings
    bOverrideAttenuation: bool



class SoundNodeBranch(SoundNode):
    BoolParameterName: str



class SoundNodeConcatenator(SoundNode):
    InputVolume: unreal.WrappedArray[float]



class SoundNodeDelay(SoundNode):
    DelayMin: float
    DelayMax: float



class SoundNodeDialoguePlayer(SoundNode):
    DialogueWaveParameter: DialogueWaveParameter
    bLooping: bool



class SoundNodeDistanceCrossFade(SoundNode):
    CrossFadeInput: unreal.WrappedArray[DistanceDatum]



class SoundNodeDoppler(SoundNode):
    DopplerIntensity: float



class SoundNodeEnveloper(SoundNode):
    LoopStart: float
    LoopEnd: float
    DurationAfterLoop: float
    LoopCount: int
    bLoopIndefinitely: bool
    bLoop: bool
    VolumeInterpCurve: DistributionFloatConstantCurve
    PitchInterpCurve: DistributionFloatConstantCurve
    VolumeCurve: RuntimeFloatCurve
    PitchCurve: RuntimeFloatCurve
    PitchMin: float
    PitchMax: float
    VolumeMin: float
    VolumeMax: float



class SoundNodeGroupControl(SoundNode):
    GroupSizes: unreal.WrappedArray[int]



class SoundNodeLooping(SoundNode):
    LoopCount: int
    bLoopIndefinitely: bool



class SoundNodeMature(SoundNode): ...


class SoundNodeMixer(SoundNode):
    InputVolume: unreal.WrappedArray[float]



class SoundNodeModulator(SoundNode):
    PitchMin: float
    PitchMax: float
    VolumeMin: float
    VolumeMax: float



class SoundNodeModulatorContinuous(SoundNode):
    PitchModulationParams: ModulatorContinuousParams
    VolumeModulationParams: ModulatorContinuousParams



class SoundNodeOscillator(SoundNode):
    bModulateVolume: bool
    bModulatePitch: bool
    AmplitudeMin: float
    AmplitudeMax: float
    FrequencyMin: float
    FrequencyMax: float
    OffsetMin: float
    OffsetMax: float
    CenterMin: float
    CenterMax: float



class SoundNodeParamCrossFade(SoundNodeDistanceCrossFade):
    ParamName: str



class SoundNodeQualityLevel(SoundNode): ...


class SoundNodeRandom(SoundNode):
    Weights: unreal.WrappedArray[float]
    PreselectAtLevelLoad: int
    bShouldExcludeFromBranchCulling: bool
    bSoundCueExcludedFromBranchCulling: bool
    bRandomizeWithoutReplacement: bool
    HasBeenUsed: unreal.WrappedArray[bool]
    NumRandomUsed: int



class SoundNodeSoundClass(SoundNode):
    SoundClassOverride: SoundClass



class SoundNodeSwitch(SoundNode):
    IntParameterName: str



class SoundNodeWaveParam(SoundNode):
    WaveParameterName: str



class SoundNodeWavePlayer(SoundNodeAssetReferencer):
    SoundWave: SoundWave
    bLooping: bool



class SoundWave(SoundBase):
    CompressionQuality: int
    StreamingPriority: int
    SampleRateQuality: audio_platform_configuration.ESoundwaveSampleRateSettings
    SoundGroup: int
    bLooping: bool
    bStreaming: bool
    bMature: bool
    bManualWordWrap: bool
    bSingleLine: bool
    bVirtualizeWhenSilent: bool
    bIsAmbisonics: bool
    SpokenText: str
    SubtitlePriority: float
    Volume: float
    Pitch: float
    NumChannels: int
    RawPCMDataSize: int
    SampleRate: int
    Subtitles: unreal.WrappedArray[SubtitleCue]
    LocalizedSubtitles: unreal.WrappedArray[LocalizedSubtitle]
    Curves: CurveTable
    InternalCurves: CurveTable



class SoundSourceBus(SoundWave):
    SourceBusChannels: ESourceBusChannels
    SourceBusDuration: float
    bAutoDeactivateWhenSilent: bool



class SoundSubmix(unreal.UObject):
    ChildSubmixes: unreal.WrappedArray[SoundSubmix]
    ParentSubmix: SoundSubmix
    ChannelFormat: ESubmixChannelFormat
    SubmixEffectChain: unreal.WrappedArray[SoundEffectSubmixPreset]
    AmbisonicsPluginSettings: AmbisonicsSubmixSettingsBase
    def StopRecordingOutput(self, WorldContextObject: unreal.UObject, ExportType: EAudioRecordingExportType, Name: str, Path: str, ExistingSoundWaveToOverwrite: SoundWave): ...
    def StartRecordingOutput(self, WorldContextObject: unreal.UObject, ExpectedDuration: float): ...


class SoundWaveProcedural(SoundWave): ...


class SpectatorPawn(DefaultPawn): ...


class SpectatorPawnMovement(FloatingPawnMovement):
    bIgnoreTimeDilation: bool



class SphereReflectionCapture(ReflectionCapture):
    DrawCaptureRadius: DrawSphereComponent



class SphereReflectionCaptureComponent(ReflectionCaptureComponent):
    InfluenceRadius: float
    CaptureDistanceScale: float
    PreviewInfluenceRadius: DrawSphereComponent



class SplineMeshActor(Actor):
    SplineMeshComponent: SplineMeshComponent



class SplineMeshComponent(StaticMeshComponent):
    SplineParams: SplineMeshParams
    SplineUpDir: core_uobject.Vector
    bAllowSplineEditingPerInstance: bool
    bSmoothInterpRollScale: bool
    ForwardAxis: int
    SplineBoundaryMin: float
    SplineBoundaryMax: float
    BodySetup: BodySetup
    CachedMeshBodySetupGuid: core_uobject.Guid
    bMeshDirty: bool
    def UpdateMesh(self): ...
    def SetStartTangent(self, StartTangent: core_uobject.Vector, bUpdateMesh: bool): ...
    def SetStartScale(self, StartScale: core_uobject.Vector2D, bUpdateMesh: bool): ...
    def SetStartRoll(self, StartRoll: float, bUpdateMesh: bool): ...
    def SetStartPosition(self, StartPos: core_uobject.Vector, bUpdateMesh: bool): ...
    def SetStartOffset(self, StartOffset: core_uobject.Vector2D, bUpdateMesh: bool): ...
    def SetStartAndEnd(self, StartPos: core_uobject.Vector, StartTangent: core_uobject.Vector, EndPos: core_uobject.Vector, EndTangent: core_uobject.Vector, bUpdateMesh: bool): ...
    def SetSplineUpDir(self, InSplineUpDir: core_uobject.Vector, bUpdateMesh: bool): ...
    def SetForwardAxis(self, InForwardAxis: int, bUpdateMesh: bool): ...
    def SetEndTangent(self, EndTangent: core_uobject.Vector, bUpdateMesh: bool): ...
    def SetEndScale(self, EndScale: core_uobject.Vector2D, bUpdateMesh: bool): ...
    def SetEndRoll(self, EndRoll: float, bUpdateMesh: bool): ...
    def SetEndPosition(self, EndPos: core_uobject.Vector, bUpdateMesh: bool): ...
    def SetEndOffset(self, EndOffset: core_uobject.Vector2D, bUpdateMesh: bool): ...
    def SetBoundaryMin(self, InBoundaryMin: float, bUpdateMesh: bool): ...
    def SetBoundaryMax(self, InBoundaryMax: float, bUpdateMesh: bool): ...
    def GetStartTangent(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetStartScale(self, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def GetStartRoll(self, ReturnValue: float) -> float: ...
    def GetStartPosition(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetStartOffset(self, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def GetSplineUpDir(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetForwardAxis(self, ReturnValue: int) -> int: ...
    def GetEndTangent(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetEndScale(self, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def GetEndRoll(self, ReturnValue: float) -> float: ...
    def GetEndPosition(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetEndOffset(self, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def GetBoundaryMin(self, ReturnValue: float) -> float: ...
    def GetBoundaryMax(self, ReturnValue: float) -> float: ...


class SpotLightComponent(PointLightComponent):
    InnerConeAngle: float
    OuterConeAngle: float
    LightShaftConeAngle: float
    def SetOuterConeAngle(self, NewOuterConeAngle: float): ...
    def SetInnerConeAngle(self, NewInnerConeAngle: float): ...


class SpringArmComponent(SceneComponent):
    TargetArmLength: float
    SocketOffset: core_uobject.Vector
    TargetOffset: core_uobject.Vector
    ProbeSize: float
    ProbeChannel: int
    bDoCollisionTest: bool
    bUsePawnControlRotation: bool
    bInheritPitch: bool
    bInheritYaw: bool
    bInheritRoll: bool
    bEnableCameraLag: bool
    bEnableCameraRotationLag: bool
    bUseCameraLagSubstepping: bool
    bDrawDebugLagMarkers: bool
    CameraLagSpeed: float
    CameraRotationLagSpeed: float
    CameraLagMaxTimeStep: float
    CameraLagMaxDistance: float
    def IsCollisionFixApplied(self, ReturnValue: bool) -> bool: ...
    def GetUnfixedCameraPosition(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetTargetRotation(self, ReturnValue: core_uobject.Rotator) -> core_uobject.Rotator: ...


class StaticMeshDescriptions(unreal.UObject): ...


class StaticMesh(unreal.UObject):
    LODGroup: str
    CullDistanceLODGroup: str
    MinLOD: PerPlatformInt
    Materials: unreal.WrappedArray[MaterialInterface]
    StaticMaterials: unreal.WrappedArray[StaticMaterial]
    LightmapUVDensity: float
    DefaultVertexColors: EDefaultVertexColor
    LightMapResolution: int
    bForceLODsShareStaticLighting: bool
    LightMapCoordinateIndex: int
    MinResolutionForPrePaddedLightmapUV: int
    DistanceFieldSelfShadowBias: float
    bGenerateMeshDistanceField: bool
    BodySetup: BodySetup
    LODForCollision: int
    bStripComplexCollisionForConsole: bool
    bHasNavigationData: bool
    bSupportUniformlyDistributedSampling: bool
    LpvBiasMultiplier: float
    bAllowCPUAccess: bool
    Sockets: unreal.WrappedArray[StaticMeshSocket]
    PositiveBoundsExtension: core_uobject.Vector
    NegativeBoundsExtension: core_uobject.Vector
    ExtendedBounds: core_uobject.BoxSphereBounds
    ElementToIgnoreForTexFactor: int
    AssetUserData: unreal.WrappedArray[AssetUserData]
    EditableMesh: unreal.UObject
    NavCollision: NavCollisionBase
    def PrestreamTextures(self, Seconds: float, bPrioritizeCharacterTextures: bool, CinematicTextureGroups: int, WorldContext: unreal.UObject): ...
    def GetNumSections(self, InLOD: int, ReturnValue: int) -> int: ...
    def GetNumLODs(self, ReturnValue: int) -> int: ...
    def GetMaterialIndex(self, MaterialSlotName: str, ReturnValue: int) -> int: ...
    def GetMaterial(self, MaterialIndex: int, ReturnValue: MaterialInterface) -> MaterialInterface: ...
    def GetBounds(self, ReturnValue: core_uobject.BoxSphereBounds) -> core_uobject.BoxSphereBounds: ...
    def GetBoundingBox(self, ReturnValue: core_uobject.Box) -> core_uobject.Box: ...


class StaticMeshSocket(unreal.UObject):
    SocketName: str
    RelativeLocation: core_uobject.Vector
    RelativeRotation: core_uobject.Rotator
    RelativeScale: core_uobject.Vector
    Tag: str



class StaticWorldBounds(Actor):
    Regions: unreal.WrappedArray[RegionOfInterest]



class StereoLayerComponent(SceneComponent):
    bLiveTexture: bool
    bSupportsDepth: bool
    bNoAlphaChannel: bool
    Texture: Texture
    LeftTexture: Texture
    bQuadPreserveTextureRatio: bool
    QuadSize: core_uobject.Vector2D
    UVRect: core_uobject.Box2D
    CylinderRadius: float
    CylinderOverlayArc: float
    CylinderHeight: int
    StereoLayerType: int
    StereoLayerShape: int
    Priority: int
    def SetUVRect(self, InUVRect: core_uobject.Box2D): ...
    def SetTexture(self, InTexture: Texture): ...
    def SetQuadSize(self, InQuadSize: core_uobject.Vector2D): ...
    def SetPriority(self, InPriority: int): ...
    def MarkTextureForUpdate(self): ...
    def GetUVRect(self, ReturnValue: core_uobject.Box2D) -> core_uobject.Box2D: ...
    def GetTexture(self, ReturnValue: Texture) -> Texture: ...
    def GetQuadSize(self, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def GetPriority(self, ReturnValue: int) -> int: ...


class StereoLayerFunctionLibrary(BlueprintFunctionLibrary):

    def ShowSplashScreen(self): ...
    def SetSplashScreen(self, Texture: Texture, Scale: core_uobject.Vector2D, Offset: core_uobject.Vector2D, bShowLoadingMovie: bool, bShowOnSet: bool): ...
    def HideSplashScreen(self): ...
    def EnableAutoLoadingSplashScreen(self, InAutoShowEnabled: bool): ...


class StreamingLevelRemap(unreal.UObject):
    StreamingLevelRemaps: unreal.WrappedArray[StreamingLevelRemapData]



class StringTable(unreal.UObject): ...


class SubsurfaceProfile(unreal.UObject):
    Settings: SubsurfaceProfileStruct



class SubUVAnimation(unreal.UObject):
    SubUVTexture: Texture2D
    SubImages_Horizontal: int
    SubImages_Vertical: int
    BoundingMode: int
    OpacitySourceMode: int
    AlphaThreshold: float



class TargetPoint(Actor): ...


class TextPropertyTestObject(unreal.UObject):
    DefaultedText: str
    UndefaultedText: str
    TransientText: str



class TextRenderActor(Actor):
    TextRender: TextRenderComponent



class TextRenderComponent(PrimitiveComponent):
    Text: str
    TextMaterial: MaterialInterface
    Font: Font
    HorizontalAlignment: int
    VerticalAlignment: int
    TextRenderColor: core_uobject.Color
    XScale: float
    YScale: float
    WorldSize: float
    InvDefaultSize: float
    HorizSpacingAdjust: float
    VertSpacingAdjust: float
    bAlwaysRenderAsText: bool
    def SetYScale(self, Value: float): ...
    def SetXScale(self, Value: float): ...
    def SetWorldSize(self, Value: float): ...
    def SetVertSpacingAdjust(self, Value: float): ...
    def SetVerticalAlignment(self, Value: int): ...
    def SetTextRenderColor(self, Value: core_uobject.Color): ...
    def SetTextMaterial(self, Material: MaterialInterface): ...
    def SetText(self, Value: str): ...
    def SetHorizSpacingAdjust(self, Value: float): ...
    def SetHorizontalAlignment(self, Value: int): ...
    def SetFont(self, Value: Font): ...
    def K2_SetText(self, Value: str): ...
    def GetTextWorldSize(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...
    def GetTextLocalSize(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...


class Texture2DArray(TextureStreaming):
    AddressX: int
    AddressY: int



class Texture2DDynamic(Texture):
    Format: int



class Texture3D(Texture):
    AddressX: int
    AddressY: int
    AddressZ: int



class TextureCube(Texture): ...


class TextureLightProfile(Texture2D):
    Brightness: float
    TextureMultiplier: float



class TextureRenderTargetCube(TextureRenderTarget):
    SizeX: int
    ClearColor: core_uobject.LinearColor
    RenderTargetFormat: int
    OverrideFormat: int
    bHDR: bool
    bForceLinearGamma: bool



class TextureUtilities(unreal.UObject):

    def UpdateTexture(self, Texture: TextureRenderTarget2D, ReturnValue: bool) -> bool: ...
    def SetSizeInternalArray(self, Size: int): ...
    def SetData4(self, Index: int, Vector: core_uobject.Vector4): ...
    def SetData3(self, Index: int, Vector: core_uobject.Vector): ...
    def ClearInternalArray(self, Size: int): ...


class ThumbnailInfo(unreal.UObject): ...


class TimecodeProvider(unreal.UObject):

    def GetTimecode(self, ReturnValue: core_uobject.Timecode) -> core_uobject.Timecode: ...
    def GetSynchronizationState(self, ReturnValue: ETimecodeProviderSynchronizationState) -> ETimecodeProviderSynchronizationState: ...
    def GetFrameRate(self, ReturnValue: core_uobject.FrameRate) -> core_uobject.FrameRate: ...


class TimelineComponent(ActorComponent):
    TheTimeline: Timeline
    bIgnoreTimeDilation: bool
    def Stop(self): ...
    def SetVectorCurve(self, NewVectorCurve: CurveVector, VectorTrackName: str): ...
    def SetTimelineLengthMode(self, NewLengthMode: int): ...
    def SetTimelineLength(self, NewLength: float): ...
    def SetPlayRate(self, NewRate: float): ...
    def SetPlaybackPosition(self, NewPosition: float, bFireEvents: bool, bFireUpdate: bool): ...
    def SetNewTime(self, NewTime: float): ...
    def SetLooping(self, bNewLooping: bool): ...
    def SetLinearColorCurve(self, NewLinearColorCurve: CurveLinearColor, LinearColorTrackName: str): ...
    def SetIgnoreTimeDilation(self, bNewIgnoreTimeDilation: bool): ...
    def SetFloatCurve(self, NewFloatCurve: CurveFloat, FloatTrackName: str): ...
    def ReverseFromEnd(self): ...
    def Reverse(self): ...
    def PlayFromStart(self): ...
    def Play(self): ...
    def OnRep_Timeline(self): ...
    def IsReversing(self, ReturnValue: bool) -> bool: ...
    def IsPlaying(self, ReturnValue: bool) -> bool: ...
    def IsLooping(self, ReturnValue: bool) -> bool: ...
    def GetTimelineLength(self, ReturnValue: float) -> float: ...
    def GetPlayRate(self, ReturnValue: float) -> float: ...
    def GetPlaybackPosition(self, ReturnValue: float) -> float: ...
    def GetIgnoreTimeDilation(self, ReturnValue: bool) -> bool: ...


class TimelineTemplate(unreal.UObject):
    TimelineLength: float
    LengthMode: int
    bAutoPlay: bool
    bLoop: bool
    bReplicated: bool
    bValidatedAsWired: bool
    bIgnoreTimeDilation: bool
    EventTracks: unreal.WrappedArray[TTEventTrack]
    FloatTracks: unreal.WrappedArray[TTFloatTrack]
    VectorTracks: unreal.WrappedArray[TTVectorTrack]
    LinearColorTracks: unreal.WrappedArray[TTLinearColorTrack]
    MetaDataArray: unreal.WrappedArray[BPVariableMetaDataEntry]
    TimelineGuid: core_uobject.Guid



class TireType(DataAsset):
    FrictionScale: float



class TouchInterface(unreal.UObject):
    Controls: unreal.WrappedArray[TouchInputControl]
    ActiveOpacity: float
    InactiveOpacity: float
    TimeUntilDeactive: float
    TimeUntilReset: float
    ActivationDelay: float
    bPreventRecenter: bool
    StartupDelay: float



class TwitterIntegrationBase(PlatformInterfaceBase):

    def TwitterRequest(self, URL: str, ParamKeysAndValues: unreal.WrappedArray[str], RequestMethod: int, AccountIndex: int, ReturnValue: bool) -> bool: ...
    def ShowTweetUI(self, InitialMessage: str, URL: str, Picture: str, ReturnValue: bool) -> bool: ...
    def Init(self): ...
    def GetNumAccounts(self, ReturnValue: int) -> int: ...
    def GetAccountName(self, AccountIndex: int, ReturnValue: str) -> str: ...
    def CanShowTweetUI(self, ReturnValue: bool) -> bool: ...
    def AuthorizeAccounts(self, ReturnValue: bool) -> bool: ...


class UserDefinedEnum(unreal.UEnum): ...


class UserDefinedStruct(core_uobject.ScriptStruct):
    Status: int
    Guid: core_uobject.Guid



class UserInterfaceSettings(DeveloperSettings):
    RenderFocusRule: ERenderFocusRule
    DefaultCursor: core_uobject.SoftClassPath
    TextEditBeamCursor: core_uobject.SoftClassPath
    CrosshairsCursor: core_uobject.SoftClassPath
    HandCursor: core_uobject.SoftClassPath
    GrabHandCursor: core_uobject.SoftClassPath
    GrabHandClosedCursor: core_uobject.SoftClassPath
    SlashedCircleCursor: core_uobject.SoftClassPath
    ApplicationScale: float
    UIScaleRule: EUIScalingRule
    CustomScalingRuleClass: core_uobject.SoftClassPath
    UIScaleCurve: RuntimeFloatCurve
    bAllowHighDPIInGameMode: bool
    bLoadWidgetsOnDedicatedServer: bool
    CursorClasses: unreal.WrappedArray[unreal.UObject]
    CustomScalingRuleClassInstance: unreal.UClass
    CustomScalingRule: DPICustomScalingRule



class VectorField(unreal.UObject):
    Bounds: core_uobject.Box
    Intensity: float



class VectorFieldAnimated(VectorField):
    Texture: Texture2D
    ConstructionOp: int
    VolumeSizeX: int
    VolumeSizeY: int
    VolumeSizeZ: int
    SubImagesX: int
    SubImagesY: int
    FrameCount: int
    FramesPerSecond: float
    bLoop: bool
    NoiseField: VectorFieldStatic
    NoiseScale: float
    NoiseMax: float



class VectorFieldComponent(PrimitiveComponent):
    VectorField: VectorField
    Intensity: float
    Tightness: float
    bPreviewVectorField: bool
    def SetIntensity(self, NewIntensity: float): ...


class VectorFieldStatic(VectorField):
    SizeX: int
    SizeY: int
    SizeZ: int



class VectorFieldVolume(Actor):
    VectorFieldComponent: VectorFieldComponent



class VisualLoggerAutomationTests(unreal.UObject): ...


class VisualLoggerDebugSnapshotInterface(core_uobject.Interface): ...


class VisualLoggerKismetLibrary(BlueprintFunctionLibrary):

    def RedirectVislog(self, SourceOwner: unreal.UObject, DestinationOwner: unreal.UObject): ...
    def LogText(self, WorldContextObject: unreal.UObject, Text: str, LogCategory: str, bAddToMessageLog: bool): ...
    def LogSegment(self, WorldContextObject: unreal.UObject, SegmentStart: core_uobject.Vector, SegmentEnd: core_uobject.Vector, Text: str, ObjectColor: core_uobject.LinearColor, Thickness: float, CategoryName: str, bAddToMessageLog: bool): ...
    def LogLocation(self, WorldContextObject: unreal.UObject, Location: core_uobject.Vector, Text: str, ObjectColor: core_uobject.LinearColor, Radius: float, LogCategory: str, bAddToMessageLog: bool): ...
    def LogBox(self, WorldContextObject: unreal.UObject, BoxShape: core_uobject.Box, Text: str, ObjectColor: core_uobject.LinearColor, LogCategory: str, bAddToMessageLog: bool): ...
    def EnableRecording(self, bEnabled: bool): ...


class VoiceChannel(Channel): ...


class VOIPTalker(ActorComponent):
    Settings: VoiceSettings
    def RegisterWithPlayerState(self, OwningState: PlayerState): ...
    def GetVoiceLevel(self, ReturnValue: float) -> float: ...
    def CreateTalkerForPlayer(self, OwningState: PlayerState, ReturnValue: VOIPTalker) -> VOIPTalker: ...
    def BPOnTalkingEnd(self): ...
    def BPOnTalkingBegin(self, AudioComponent: AudioComponent): ...


class VOIPStatics(BlueprintFunctionLibrary):

    def SetMicThreshold(self, InThreshold: float): ...


class VolumeTexture(Texture): ...


class VolumetricLightmapDensityVolume(Volume):
    AllowedMipLevelRange: core_uobject.Int32Interval



class VolumetricLightMapVolume(Volume):
    bValidVolumetricLightMapVolume: bool
    bDebugLogging: bool
    bShowActorScaleBox: bool
    bShowActualVolumeBox: bool
    bShowTopLevelCells: bool
    bForceLightmassIniRefresh: bool
    DebugCellIndex: core_uobject.IntVector
    DebugCellLevels: core_uobject.IntVector
    bAllowNonUniformScale: bool
    BrickSize: int
    MaxRefinementLevels: int
    TopLevelGridSize: core_uobject.IntVector
    TargetDetailCellSize: float
    EffectiveDetailCellSize: float
    IndirectionTextureDimensions: core_uobject.IntVector
    IndirectionTextureSizeMB: float
    TopLevelBrickSize: float
    TopLevelCellSize: float
    ActualVolumeBounds: core_uobject.Box
    VolumeSize: core_uobject.Vector
    CachedScale: core_uobject.Vector
    VolumetricLightMapComponent: VolumetricLightMapVolumeComponent



class VolumetricLightMapVolumeComponent(PrimitiveComponent): ...


class WindDirectionalSourceComponent(SceneComponent):
    Strength: float
    Speed: float
    MinGustAmount: float
    MaxGustAmount: float
    Radius: float
    bPointWind: bool
    def SetWindType(self, InNewType: EWindSourceType): ...
    def SetStrength(self, InNewStrength: float): ...
    def SetSpeed(self, InNewSpeed: float): ...
    def SetRadius(self, InNewRadius: float): ...
    def SetMinimumGustAmount(self, InNewMinGust: float): ...
    def SetMaximumGustAmount(self, InNewMaxGust: float): ...


class WorldComposition(unreal.UObject):
    TilesStreaming: unreal.WrappedArray[LevelStreaming]
    TilesStreamingTimeThreshold: float
    bLoadAllTilesDuringCinematic: bool
    bRebaseOriginIn3DSpace: bool
    RebaseOriginDistance: float



class HierarchicalLODSetup(unreal.UObject):
    HierarchicalLODSetup: unreal.WrappedArray[HierarchicalSimplification]



class WorldSettings(Info):
    bEnableWorldBoundsChecks: bool
    bEnableNavigationSystem: bool
    bEnableAISystem: bool
    bEnableWorldComposition: bool
    bUseClientSideLevelStreamingVolumes: bool
    bEnableWorldOriginRebasing: bool
    bWorldGravitySet: bool
    bGlobalGravitySet: bool
    NavigationSystemConfig: NavigationSystemConfig
    KillZ: float
    KillZDamageType: unreal.UClass
    WorldGravityZ: float
    GlobalGravityZ: float
    DefaultPhysicsVolumeClass: unreal.UClass
    PhysicsCollisionHandlerClass: unreal.UClass
    DefaultGameMode: unreal.UClass
    GameNetworkManagerClass: unreal.UClass
    PackedLightAndShadowMapTextureSize: int
    bMinimizeBSPSections: bool
    DefaultColorScale: core_uobject.Vector
    DefaultMaxDistanceFieldOcclusionDistance: float
    GlobalDistanceFieldViewDistance: float
    DynamicIndirectShadowsSelfShadowingIntensity: float
    bPrecomputeVisibility: bool
    bPlaceCellsOnlyAlongCameraTracks: bool
    bPlaceCellsOnSurfaces: bool
    VisibilityCellHeight: int
    VisibilityCellSize: int
    VisibilityAggressiveness: int
    bForceNoPrecomputedLighting: bool
    LightmassSettings: LightmassWorldInfoSettings
    DefaultReverbSettings: ReverbSettings
    DefaultAmbientZoneSettings: InteriorSettings
    DefaultBaseSoundMix: SoundMix
    WorldToMeters: float
    MonoCullingDistance: float
    BookMarks: BookMark
    TimeDilation: float
    MatineeTimeDilation: float
    DemoPlayTimeDilation: float
    MinGlobalTimeDilation: float
    MaxGlobalTimeDilation: float
    MinUndilatedFrameTime: float
    MaxUndilatedFrameTime: float
    Pauser: PlayerState
    bHighPriorityLoading: bool
    bHighPriorityLoadingLocal: bool
    ReplicationViewers: unreal.WrappedArray[NetViewer]
    bOverrideDefaultBroadphaseSettings: bool
    BroadphaseSettings: BroadphaseSettings
    AssetUserData: unreal.WrappedArray[AssetUserData]
    MapData: MapData
    DevAssetReferences: unreal.WrappedArray[unreal.UObject]
    MaxLightMapMemory: float
    bStaticLightingUsesSkyOcclusionMaps: bool
    bStaticLightingUsesAmbientOcclusionMaps: bool
    GbxColorRemapLUTSet: GbxColorRemapLUTSet
    def OnRep_WorldGravityZ(self): ...


class DistributionLookupTable:
    Op: int
    EntryCount: int
    EntryStride: int
    SubEntryStride: int
    TimeScale: float
    TimeBias: float
    Values: unreal.WrappedArray[float]
    LockFlag: int



class RawDistribution:
    Table: DistributionLookupTable



class FloatDistribution:
    Table: DistributionLookupTable



class VectorDistribution:
    Table: DistributionLookupTable



class Vector4Distribution:
    Table: DistributionLookupTable



class ReplicatedConsoleCommandContext:
    CommandAndArgs: str



class FloatRK4SpringInterpolator:
    StiffnessConstant: float
    DampeningRatio: float



class VectorRK4SpringInterpolator:
    StiffnessConstant: float
    DampeningRatio: float



class ExpressionInput:
    OutputIndex: int
    InputName: str
    Mask: int
    MaskR: int
    MaskG: int
    MaskB: int
    MaskA: int
    ExpressionName: str



class MaterialAttributesInput(ExpressionInput):
    PropertyConnectedBitmask: int



class ExpressionOutput:
    OutputName: str
    Mask: int
    MaskR: int
    MaskG: int
    MaskB: int
    MaskA: int



class FormatArgumentData:
    ArgumentName: str
    ArgumentValueType: int
    ArgumentValue: str
    ArgumentValueInt: int
    ArgumentValueFloat: float
    ArgumentValueGender: ETextGender



class MaterialInput:
    OutputIndex: int
    InputName: str
    Mask: int
    MaskR: int
    MaskG: int
    MaskB: int
    MaskA: int
    ExpressionName: str



class ColorMaterialInput(MaterialInput):
    UseConstant: bool
    Constant: core_uobject.Color



class ScalarMaterialInput(MaterialInput):
    UseConstant: bool
    Constant: float



class VectorMaterialInput(MaterialInput):
    UseConstant: bool
    Constant: core_uobject.Vector



class Vector2MaterialInput(MaterialInput):
    UseConstant: bool
    ConstantX: float
    ConstantY: float



class HitResult:
    bBlockingHit: bool
    bStartPenetrating: bool
    FaceIndex: int
    bLagCompensated: bool
    Time: float
    Distance: float
    Location: Vector_NetQuantize
    ImpactPoint: Vector_NetQuantize
    Normal: Vector_NetQuantizeNormal
    ImpactNormal: Vector_NetQuantizeNormal
    TraceStart: Vector_NetQuantize
    TraceEnd: Vector_NetQuantize
    PenetrationDepth: float
    Item: int
    PhysMaterial: PhysicalMaterial
    Actor: Actor
    Component: PrimitiveComponent
    BoneName: str
    MyBoneName: str



class Vector_NetQuantize(core_uobject.Vector): ...


class Vector_NetQuantizeNormal(core_uobject.Vector): ...


class TickOptimizationData:
    bCheckForTickOptimizations: bool
    bMatchActorOwnerTickState: bool
    TickOptimDistanceFromLocalPlayers: float
    bTickOptimizationOn: bool



class RepAttachment:
    AttachParent: Actor
    RotationOffset: core_uobject.Rotator
    AttachSocket: str
    AttachComponent: SceneComponent



class Vector_NetQuantize1__(core_uobject.Vector): ...


class RepMovement:
    LinearVelocity: core_uobject.Vector
    AngularVelocity: core_uobject.Vector
    Location: core_uobject.Vector
    Rotation: core_uobject.Rotator
    bSimulatedPhysicSleep: bool
    bRepPhysics: bool
    LocationQuantizationLevel: EVectorQuantization
    VelocityQuantizationLevel: EVectorQuantization
    RotationQuantizationLevel: ERotatorQuantization



class TickFunction:
    TickGroup: int
    EndTickGroup: int
    bTickEvenWhenPaused: bool
    bCanEverTick: bool
    bStartWithTickEnabled: bool
    bAllowTickOnDedicatedServer: bool
    TickInterval: float



class ActorTickFunction(TickFunction): ...


class BranchingPointNotifyPayload: ...


class SimpleMemberReference:
    MemberParent: unreal.UObject
    MemberName: str
    MemberGuid: core_uobject.Guid



class ActorComponentTickFunction(TickFunction): ...


class SubtitleCue:
    Text: str
    Time: float



class InterpControlPoint:
    PositionControlPoint: core_uobject.Vector
    bPositionIsRelative: bool



class PlatformInterfaceDelegateResult:
    bSuccessful: bool
    Data: PlatformInterfaceData



class PlatformInterfaceData:
    DataName: str
    Type: int
    IntValue: int
    FloatValue: float
    StringValue: str
    ObjectValue: unreal.UObject



class DebugFloatHistory:
    Samples: unreal.WrappedArray[float]
    MaxSamples: float
    MinValue: float
    MaxValue: float
    bAutoAdjustMinMax: bool



class LatentActionInfo:
    Linkage: int
    UUID: int
    ExecutionFunction: str
    CallbackTarget: unreal.UObject



class TimerHandle: ...


class CollisionProfileName:
    Name: str



class GenericStruct:
    Data: int



class UserActivity:
    ActionName: str



class MovementProperties:
    bCanCrouch: bool
    bCanJump: bool
    bCanWalk: bool
    bCanSwim: bool
    bCanFly: bool



class NavAgentProperties(MovementProperties):
    AgentRadius: float
    AgentHeight: float
    AgentStepHeight: float
    NavWalkingSearchHeightScale: float
    PreferredNavData: core_uobject.SoftClassPath



class FindFloorResult:
    bBlockingHit: bool
    bWalkableFloor: bool
    bLineTrace: bool
    FloorDist: float
    LineDist: float
    HitResult: HitResult



class NavAvoidanceMask:
    bGroup1: bool
    bGroup2: bool
    bGroup3: bool
    bGroup4: bool
    bGroup5: bool
    bGroup6: bool
    bGroup7: bool
    bGroup8: bool
    bGroup9: bool
    bGroup11: bool
    bGroup12: bool
    bGroup13: bool
    bGroup14: bool
    bGroup15: bool
    bGroup16: bool
    bGroup17: bool
    bGroup18: bool
    bGroup19: bool
    bGroup21: bool
    bGroup22: bool
    bGroup23: bool
    bGroup24: bool
    bGroup25: bool
    bGroup26: bool
    bGroup27: bool
    bGroup28: bool
    bGroup29: bool
    bGroup31: bool



class RootMotionMovementParams:
    bHasRootMotion: bool
    BlendWeight: float
    RootMotionTransform: core_uobject.Transform



class RootMotionSourceGroup:
    bHasAdditiveSources: bool
    bHasOverrideSources: bool
    bIsAdditiveVelocityApplied: bool
    LastAccumulatedSettings: RootMotionSourceSettings



class RootMotionSourceSettings:
    Flags: int



class Vector_NetQuantize1_(core_uobject.Vector): ...


class CharacterMovementComponentPostPhysicsTickFunction(TickFunction): ...


class GbxAttributeBase: ...


class GbxAttributeFloat(GbxAttributeBase):
    Value: float
    BaseValue: float



class AnimCurveBase:
    LastObservedName: str
    Name: SmartName
    CurveTypeFlags: int



class SmartName:
    DisplayName: str



class FloatCurve(AnimCurveBase):
    FloatCurve: RichCurve



class IndexedCurve:
    KeyHandlesToIndices: KeyHandleMap



class KeyHandleMap: ...


class RichCurve(IndexedCurve):
    PreInfinityExtrap: int
    PostInfinityExtrap: int
    DefaultValue: float
    Keys: unreal.WrappedArray[RichCurveKey]



class RichCurveKey:
    InterpMode: int
    TangentMode: int
    TangentWeightMode: int
    Time: float
    Value: float
    ArriveTangent: float
    ArriveTangentWeight: float
    LeaveTangent: float
    LeaveTangentWeight: float



class RuntimeFloatCurve:
    EditorCurveData: RichCurve
    ExternalCurve: CurveFloat



class UniqueNetIdRepl(core_uobject.UniqueNetIdWrapper):
    ReplicationBytes: unreal.WrappedArray[int]



class GbxForceFeedbackEffect:
    ChannelDetails: unreal.WrappedArray[ForceFeedbackChannelDetails]



class ForceFeedbackChannelDetails:
    bAffectsLeftLarge: bool
    bAffectsLeftSmall: bool
    bAffectsRightLarge: bool
    bAffectsRightSmall: bool
    Curve: RuntimeFloatCurve



class RadialBlurSelection:
    Selection: int
    Duration: float
    BlurDistance: float



class ViewTargetTransitionParams:
    BlendTime: float
    BlendFunction: int
    BlendExp: float
    bLockOutgoing: bool



class UpdateLevelStreamingLevelStatus:
    PackageName: str
    LODIndex: int
    bNewShouldBeLoaded: bool
    bNewShouldBeVisible: bool
    bNewShouldBlockOnLoad: bool



class UpdateLevelVisibilityLevelInfo:
    PackageName: str
    bIsVisible: bool



class ActiveGbxForceFeedbackEffect:
    ForceFeedbackEffect: GbxForceFeedbackEffect



class ActiveForceFeedbackEffect:
    ForceFeedbackEffect: ForceFeedbackEffect



class PostProcessSettings:
    bOverride_WhiteTemp: bool
    bOverride_WhiteTint: bool
    bOverride_ColorSaturation: bool
    bOverride_ColorContrast: bool
    bOverride_ColorGamma: bool
    bOverride_ColorGain: bool
    bOverride_ColorOffset: bool
    bOverride_ColorSaturationShadows: bool
    bOverride_ColorContrastShadows: bool
    bOverride_ColorGammaShadows: bool
    bOverride_ColorGainShadows: bool
    bOverride_ColorOffsetShadows: bool
    bOverride_ColorSaturationMidtones: bool
    bOverride_ColorContrastMidtones: bool
    bOverride_ColorGammaMidtones: bool
    bOverride_ColorGainMidtones: bool
    bOverride_ColorOffsetMidtones: bool
    bOverride_ColorSaturationHighlights: bool
    bOverride_ColorContrastHighlights: bool
    bOverride_ColorGammaHighlights: bool
    bOverride_ColorGainHighlights: bool
    bOverride_ColorOffsetHighlights: bool
    bOverride_ColorCorrectionShadowsMax: bool
    bOverride_ColorCorrectionHighlightsMin: bool
    bOverride_BlueCorrection: bool
    bOverride_ExpandGamut: bool
    bOverride_FilmWhitePoint: bool
    bOverride_FilmSaturation: bool
    bOverride_FilmChannelMixerRed: bool
    bOverride_FilmChannelMixerGreen: bool
    bOverride_FilmChannelMixerBlue: bool
    bOverride_FilmContrast: bool
    bOverride_FilmDynamicRange: bool
    bOverride_FilmHealAmount: bool
    bOverride_FilmToeAmount: bool
    bOverride_FilmShadowTint: bool
    bOverride_FilmShadowTintBlend: bool
    bOverride_FilmShadowTintAmount: bool
    bOverride_FilmSlope: bool
    bOverride_FilmToe: bool
    bOverride_FilmShoulder: bool
    bOverride_FilmBlackClip: bool
    bOverride_FilmWhiteClip: bool
    bOverride_SceneColorTint: bool
    bOverride_SceneFringeIntensity: bool
    bOverride_ChromaticAberrationStartOffset: bool
    bOverride_AmbientCubemapTint: bool
    bOverride_AmbientCubemapIntensity: bool
    bOverride_AmbientCubemapGBXCustomLitLightingChannel: bool
    bOverride_BloomMethod: bool
    bOverride_BloomIntensity: bool
    bOverride_BloomThreshold: bool
    bOverride_Bloom1Tint: bool
    bOverride_Bloom1Size: bool
    bOverride_Bloom2Size: bool
    bOverride_Bloom2Tint: bool
    bOverride_Bloom3Tint: bool
    bOverride_Bloom3Size: bool
    bOverride_Bloom4Tint: bool
    bOverride_Bloom4Size: bool
    bOverride_Bloom5Tint: bool
    bOverride_Bloom5Size: bool
    bOverride_Bloom6Tint: bool
    bOverride_Bloom6Size: bool
    bOverride_BloomSizeScale: bool
    bOverride_BloomConvolutionTexture: bool
    bOverride_BloomConvolutionSize: bool
    bOverride_BloomConvolutionCenterUV: bool
    bOverride_BloomConvolutionPreFilter: bool
    bOverride_BloomConvolutionPreFilterMin: bool
    bOverride_BloomConvolutionPreFilterMax: bool
    bOverride_BloomConvolutionPreFilterMult: bool
    bOverride_BloomConvolutionBufferScale: bool
    bOverride_BloomDirtMaskIntensity: bool
    bOverride_BloomDirtMaskTint: bool
    bOverride_BloomDirtMask: bool
    bOverride_CameraShutterSpeed: bool
    bOverride_CameraISO: bool
    bOverride_AutoExposureMethod: bool
    bOverride_AutoExposureLowPercent: bool
    bOverride_AutoExposureHighPercent: bool
    bOverride_AutoExposureMinBrightness: bool
    bOverride_AutoExposureMaxBrightness: bool
    bOverride_AutoExposureMinBrightnessHDR: bool
    bOverride_AutoExposureMaxBrightnessHDR: bool
    bOverride_AutoExposureCalibrationConstant: bool
    bOverride_AutoExposureSpeedUp: bool
    bOverride_AutoExposureSpeedDown: bool
    bOverride_AutoExposureBias: bool
    bOverride_AutoExposureBiasHDR: bool
    bOverride_HistogramLogMin: bool
    bOverride_HistogramLogMax: bool
    bOverride_LensFlareIntensity: bool
    bOverride_LensFlareTint: bool
    bOverride_LensFlareTints: bool
    bOverride_LensFlareBokehSize: bool
    bOverride_LensFlareBokehShape: bool
    bOverride_LensFlareThreshold: bool
    bOverride_VignetteIntensity: bool
    bOverride_VignetteFeathering: bool
    bOverride_GrainIntensity: bool
    bOverride_GrainJitter: bool
    bOverride_AmbientOcclusionIntensity: bool
    bOverride_AmbientOcclusionStaticFraction: bool
    bOverride_AmbientOcclusionRadius: bool
    bOverride_AmbientOcclusionFadeDistance: bool
    bOverride_AmbientOcclusionFadeRadius: bool
    bOverride_AmbientOcclusionDistance: bool
    bOverride_AmbientOcclusionRadiusInWS: bool
    bOverride_AmbientOcclusionPower: bool
    bOverride_AmbientOcclusionBias: bool
    bOverride_AmbientOcclusionQuality: bool
    bOverride_AmbientOcclusionMipBlend: bool
    bOverride_AmbientOcclusionMipScale: bool
    bOverride_AmbientOcclusionMipThreshold: bool
    bOverride_ComputeAOEnable: bool
    bOverride_ComputeAOBlurTolerance: bool
    bOverride_ComputeAOUpsampleTolerance: bool
    bOverride_ComputeAONoiseFilterTolerance: bool
    bOverride_ComputeAORejectionFalloff: bool
    bOverride_ComputeAOStartFadeDistance: bool
    bOverride_ComputeAOFadeExponent: bool
    bOverride_ComputeAODepthDifference: bool
    bOverride_ComputeAOHierarchyDepth: bool
    bOverride_ComputeAOQualityLevel: bool
    bOverride_ComputeAOApplyCurve: bool
    bOverride_LPVIntensity: bool
    bOverride_LPVDirectionalOcclusionIntensity: bool
    bOverride_LPVDirectionalOcclusionRadius: bool
    bOverride_LPVDiffuseOcclusionExponent: bool
    bOverride_LPVSpecularOcclusionExponent: bool
    bOverride_LPVDiffuseOcclusionIntensity: bool
    bOverride_LPVSpecularOcclusionIntensity: bool
    bOverride_LPVSize: bool
    bOverride_LPVSecondaryOcclusionIntensity: bool
    bOverride_LPVSecondaryBounceIntensity: bool
    bOverride_LPVGeometryVolumeBias: bool
    bOverride_LPVVplInjectionBias: bool
    bOverride_LPVEmissiveInjectionIntensity: bool
    bOverride_LPVFadeRange: bool
    bOverride_LPVDirectionalOcclusionFadeRange: bool
    bOverride_IndirectLightingColor: bool
    bOverride_IndirectLightingIntensity: bool
    bOverride_IndoorReflectionEnvironmentColor: bool
    bOverride_IndoorReflectionEnvironmentIntensity: bool
    bOverride_OutdoorReflectionEnvironmentColor: bool
    bOverride_OutdoorReflectionEnvironmentIntensity: bool
    bOverride_ColorGradingIntensity: bool
    bOverride_ColorGradingLUT: bool
    bOverride_SecondaryColorGradingIntensity: bool
    bOverride_SecondaryColorGradingLUT: bool
    bOverride_DepthOfFieldFocalDistance: bool
    bOverride_DepthOfFieldFstop: bool
    bOverride_DepthOfFieldMinFstop: bool
    bOverride_DepthOfFieldBladeCount: bool
    bOverride_DepthOfFieldSensorWidth: bool
    bOverride_DepthOfFieldDepthBlurRadius: bool
    bOverride_DepthOfFieldDepthBlurAmount: bool
    bOverride_DepthOfFieldFocalRegion: bool
    bOverride_DepthOfFieldNearTransitionRegion: bool
    bOverride_DepthOfFieldFarTransitionRegion: bool
    bOverride_DepthOfFieldScale: bool
    bOverride_DepthOfFieldMaxBokehSize: bool
    bOverride_DepthOfFieldNearBlurSize: bool
    bOverride_DepthOfFieldFarBlurSize: bool
    bOverride_DepthOfFieldNearSampleCount: bool
    bOverride_DepthOfFieldFarSampleCount: bool
    bOverride_DepthOfFieldMethod: bool
    bOverride_MobileHQGaussian: bool
    bOverride_DepthOfFieldBokehShape: bool
    bOverride_DepthOfFieldOcclusion: bool
    bOverride_DepthOfFieldColorThreshold: bool
    bOverride_DepthOfFieldSizeThreshold: bool
    bOverride_DepthOfFieldSkyFocusDistance: bool
    bOverride_DepthOfFieldNearBlendFactor: bool
    bOverride_DepthOfFieldFarBlendFactor: bool
    bOverride_DepthOfFieldVignetteSize: bool
    bOverride_DepthOfFieldVignetteFeathering: bool
    bOverride_DepthOfFieldVignetteFarScale: bool
    bOverride_MotionBlurAmount: bool
    bOverride_MotionBlurMax: bool
    bOverride_MotionBlurPerObjectSize: bool
    bOverride_MotionBlurStaticIntensity: bool
    bOverride_MotionBlurDynamicIntensity: bool
    bOverride_ScreenPercentage: bool
    bOverride_ScreenCenterOffset: bool
    bOverride_ScreenSpaceReflectionIntensity: bool
    bOverride_ScreenSpaceReflectionQuality: bool
    bOverride_ScreenSpaceReflectionMaxRoughness: bool
    bOverride_ScreenSpaceReflectionRoughnessScale: bool
    bOverride_EdgeDetectionEnable: bool
    bOverride_EdgeDetectionHFilterAxisCoeff: bool
    bOverride_EdgeDetectionHFilterDiagCoeff: bool
    bOverride_EdgeDetectionVFilterAxisCoeff: bool
    bOverride_EdgeDetectionVFilterDiagCoeff: bool
    bOverride_EdgeDetectionFarDistance: bool
    bOverride_EdgeDetectionNearDistance: bool
    bOverride_EdgeDetectionSobelPower: bool
    bOverride_EdgeDetectionTexelOffset: bool
    bOverride_EdgeDetectionTransitionDistance: bool
    bOverride_EdgeDetectionTransitionDistanceFar: bool
    bOverride_EdgeDetectionApplyThreshold: bool
    WhiteTemp: float
    WhiteTint: float
    ColorSaturation: core_uobject.Vector4
    ColorContrast: core_uobject.Vector4
    ColorGamma: core_uobject.Vector4
    ColorGain: core_uobject.Vector4
    ColorOffset: core_uobject.Vector4
    ColorSaturationShadows: core_uobject.Vector4
    ColorContrastShadows: core_uobject.Vector4
    ColorGammaShadows: core_uobject.Vector4
    ColorGainShadows: core_uobject.Vector4
    ColorOffsetShadows: core_uobject.Vector4
    ColorCorrectionShadowsMax: float
    ColorSaturationMidtones: core_uobject.Vector4
    ColorContrastMidtones: core_uobject.Vector4
    ColorGammaMidtones: core_uobject.Vector4
    ColorGainMidtones: core_uobject.Vector4
    ColorOffsetMidtones: core_uobject.Vector4
    ColorSaturationHighlights: core_uobject.Vector4
    ColorContrastHighlights: core_uobject.Vector4
    ColorGammaHighlights: core_uobject.Vector4
    ColorGainHighlights: core_uobject.Vector4
    ColorOffsetHighlights: core_uobject.Vector4
    ColorCorrectionHighlightsMin: float
    BlueCorrection: float
    ExpandGamut: float
    FilmSlope: float
    FilmToe: float
    FilmShoulder: float
    FilmBlackClip: float
    FilmWhiteClip: float
    FilmWhitePoint: core_uobject.LinearColor
    FilmShadowTint: core_uobject.LinearColor
    FilmShadowTintBlend: float
    FilmShadowTintAmount: float
    FilmSaturation: float
    FilmChannelMixerRed: core_uobject.LinearColor
    FilmChannelMixerGreen: core_uobject.LinearColor
    FilmChannelMixerBlue: core_uobject.LinearColor
    FilmContrast: float
    FilmToeAmount: float
    FilmHealAmount: float
    FilmDynamicRange: float
    SceneColorTint: core_uobject.LinearColor
    SceneFringeIntensity: float
    ChromaticAberrationStartOffset: float
    BloomMethod: int
    BloomIntensity: float
    BloomThreshold: float
    BloomSizeScale: float
    Bloom1Size: float
    Bloom2Size: float
    Bloom3Size: float
    Bloom4Size: float
    Bloom5Size: float
    Bloom6Size: float
    Bloom1Tint: core_uobject.LinearColor
    Bloom2Tint: core_uobject.LinearColor
    Bloom3Tint: core_uobject.LinearColor
    Bloom4Tint: core_uobject.LinearColor
    Bloom5Tint: core_uobject.LinearColor
    Bloom6Tint: core_uobject.LinearColor
    BloomConvolutionTexture: Texture2D
    BloomConvolutionSize: float
    BloomConvolutionCenterUV: core_uobject.Vector2D
    BloomConvolutionPreFilter: core_uobject.Vector
    BloomConvolutionPreFilterMin: float
    BloomConvolutionPreFilterMax: float
    BloomConvolutionPreFilterMult: float
    BloomConvolutionBufferScale: float
    BloomDirtMask: Texture
    BloomDirtMaskIntensity: float
    BloomDirtMaskTint: core_uobject.LinearColor
    AmbientCubemapTint: core_uobject.LinearColor
    AmbientCubemapGBXCustomLitLightingChannel: int
    AmbientCubemapIntensity: float
    AmbientCubemap: TextureCube
    CameraShutterSpeed: float
    CameraISO: float
    DepthOfFieldFstop: float
    DepthOfFieldMinFstop: float
    DepthOfFieldBladeCount: int
    AutoExposureBias: float
    AutoExposureBiasHDR: float
    AutoExposureMethod: int
    AutoExposureLowPercent: float
    AutoExposureHighPercent: float
    AutoExposureMinBrightness: float
    AutoExposureMaxBrightness: float
    AutoExposureMinBrightnessHDR: float
    AutoExposureMaxBrightnessHDR: float
    AutoExposureSpeedUp: float
    AutoExposureSpeedDown: float
    HistogramLogMin: float
    HistogramLogMax: float
    AutoExposureCalibrationConstant: float
    LensFlareIntensity: float
    LensFlareTint: core_uobject.LinearColor
    LensFlareBokehSize: float
    LensFlareThreshold: float
    LensFlareBokehShape: Texture
    LensFlareTints: core_uobject.LinearColor
    VignetteIntensity: float
    VignetteFeathering: float
    GrainJitter: float
    GrainIntensity: float
    AmbientOcclusionIntensity: float
    AmbientOcclusionStaticFraction: float
    AmbientOcclusionRadius: float
    AmbientOcclusionRadiusInWS: bool
    AmbientOcclusionFadeDistance: float
    AmbientOcclusionFadeRadius: float
    AmbientOcclusionDistance: float
    AmbientOcclusionPower: float
    AmbientOcclusionBias: float
    AmbientOcclusionQuality: float
    AmbientOcclusionMipBlend: float
    AmbientOcclusionMipScale: float
    AmbientOcclusionMipThreshold: float
    bComputeAOEnable: bool
    ComputeAOBlurTolerance: float
    ComputeAOUpsampleTolerance: float
    ComputeAONoiseFilterTolerance: float
    ComputeAORejectionFalloff: float
    ComputeAOStartFadeDistance: float
    ComputeAOFadeExponent: float
    ComputeAODepthDifference: float
    ComputeAOHierarchyDepth: int
    ComputeAOQualityLevel: int
    ComputeAOApplyCurve: float
    IndirectLightingColor: core_uobject.LinearColor
    IndirectLightingIntensity: float
    IndoorReflectionEnvironmentColor: core_uobject.LinearColor
    IndoorReflectionEnvironmentIntensity: float
    OutdoorReflectionEnvironmentColor: core_uobject.LinearColor
    OutdoorReflectionEnvironmentIntensity: float
    ColorGradingIntensity: float
    ColorGradingLUT: Texture
    SecondaryColorGradingLUT: Texture
    SecondaryColorGradingIntensity: float
    DepthOfFieldMethod: int
    bMobileHQGaussian: bool
    DepthOfFieldSensorWidth: float
    DepthOfFieldFocalDistance: float
    DepthOfFieldDepthBlurAmount: float
    DepthOfFieldDepthBlurRadius: float
    DepthOfFieldFocalRegion: float
    DepthOfFieldNearTransitionRegion: float
    DepthOfFieldFarTransitionRegion: float
    DepthOfFieldScale: float
    DepthOfFieldMaxBokehSize: float
    DepthOfFieldNearBlurSize: float
    DepthOfFieldFarBlurSize: float
    DepthOfFieldNearSampleCount: int
    DepthOfFieldFarSampleCount: int
    DepthOfFieldBokehShape: Texture
    DepthOfFieldOcclusion: float
    DepthOfFieldColorThreshold: float
    DepthOfFieldSizeThreshold: float
    DepthOfFieldSkyFocusDistance: float
    DepthOfFieldNearBlendFactor: float
    DepthOfFieldFarBlendFactor: float
    DepthOfFieldVignetteSize: float
    DepthOfFieldVignetteFeathering: float
    DepthOfFieldVignetteFarScale: float
    MotionBlurAmount: float
    MotionBlurMax: float
    MotionBlurPerObjectSize: float
    MotionBlurStaticIntensity: float
    MotionBlurDynamicIntensity: float
    LPVIntensity: float
    LPVVplInjectionBias: float
    LPVSize: float
    LPVSecondaryOcclusionIntensity: float
    LPVSecondaryBounceIntensity: float
    LPVGeometryVolumeBias: float
    LPVEmissiveInjectionIntensity: float
    LPVDirectionalOcclusionIntensity: float
    LPVDirectionalOcclusionRadius: float
    LPVDiffuseOcclusionExponent: float
    LPVSpecularOcclusionExponent: float
    LPVDiffuseOcclusionIntensity: float
    LPVSpecularOcclusionIntensity: float
    ScreenSpaceReflectionIntensity: float
    ScreenSpaceReflectionQuality: float
    ScreenSpaceReflectionMaxRoughness: float
    LPVFadeRange: float
    LPVDirectionalOcclusionFadeRange: float
    EdgeDetectionEnable: bool
    EdgeDetectionHFilterAxisCoeff: float
    EdgeDetectionHFilterDiagCoeff: float
    EdgeDetectionVFilterAxisCoeff: float
    EdgeDetectionVFilterDiagCoeff: float
    EdgeDetectionFarDistance: float
    EdgeDetectionNearDistance: float
    EdgeDetectionSobelPower: float
    EdgeDetectionTexelOffset: float
    EdgeDetectionTransitionDistance: float
    EdgeDetectionTransitionDistanceFar: float
    EdgeDetectionApplyThreshold: float
    ScreenPercentage: float
    ScreenCenterOffset: core_uobject.Vector2D
    WeightedBlendables: WeightedBlendables
    Blendables: unreal.WrappedArray[unreal.UObject]



class WeightedBlendables:
    Array: unreal.WrappedArray[WeightedBlendable]



class WeightedBlendable:
    Weight: float
    Object: unreal.UObject



class ParticleSysParam:
    Name: str
    ParamType: int
    Scalar: float
    Scalar_Low: float
    Vector: core_uobject.Vector
    Vector_Low: core_uobject.Vector
    Color: core_uobject.Color
    Actor: Actor
    Material: MaterialInterface
    BoneSocketName: str



class GbxAttributeInteger(GbxAttributeBase):
    Value: int
    BaseValue: int



class DataTableRowHandle:
    DataTable: DataTable
    RowName: str



class RepRootMotionMontage:
    bIsActive: bool
    AnimMontage: AnimMontage
    Position: float
    Rotation: core_uobject.Rotator
    MovementBase: PrimitiveComponent
    MovementBaseBoneName: str
    bRelativePosition: bool
    bRelativeRotation: bool
    AuthoritativeRootMotion: RootMotionSourceGroup
    CurrentSlotAnimInfo: SlotAnimationTrackAnimInfo



class SlotAnimationTrackAnimInfo:
    SlotName: str
    SlotAnim: str
    NumTracks: int



class SimulatedRootMotionReplicatedMove:
    Time: float
    RootMotion: RepRootMotionMontage



class BasedMovementInfo:
    MovementBase: PrimitiveComponent
    BoneName: str
    Rotation: core_uobject.Rotator
    bServerHasBaseComponent: bool
    bRelativeRotation: bool
    bServerHasVelocity: bool



class CollisionResponseContainer:
    WorldStatic: int
    WorldDynamic: int
    Pawn: int
    Visibility: int
    Camera: int
    PhysicsBody: int
    Vehicle: int
    Destructible: int
    EngineTraceChannel1: int
    EngineTraceChannel2: int
    EngineTraceChannel3: int
    EngineTraceChannel4: int
    EngineTraceChannel5: int
    EngineTraceChannel6: int
    GameTraceChannel1: int
    GameTraceChannel2: int
    GameTraceChannel3: int
    GameTraceChannel4: int
    GameTraceChannel5: int
    GameTraceChannel6: int
    GameTraceChannel7: int
    GameTraceChannel8: int
    GameTraceChannel9: int
    GameTraceChannel11: int
    GameTraceChannel12: int
    GameTraceChannel13: int
    GameTraceChannel14: int
    GameTraceChannel15: int
    GameTraceChannel16: int
    GameTraceChannel17: int
    GameTraceChannel18: int



class PredictProjectilePathResult:
    PathData: unreal.WrappedArray[PredictProjectilePathPointData]
    LastTraceDestination: PredictProjectilePathPointData
    HitResult: HitResult



class PredictProjectilePathPointData:
    Location: core_uobject.Vector
    Velocity: core_uobject.Vector
    Time: float



class FastArraySerializer: ...


class FastArraySerializerItem:
    ReplicationID: int
    ReplicationKey: int
    MostRecentArrayReplicationKey: int



class DebugTextInfo:
    SrcActor: Actor
    SrcActorOffset: core_uobject.Vector
    SrcActorDesiredOffset: core_uobject.Vector
    DebugText: str
    TimeRemaining: float
    Duration: float
    TextColor: core_uobject.Color
    bAbsoluteLocation: bool
    bKeepAttachedToActor: bool
    bDrawShadow: bool
    OrigActorLocation: core_uobject.Vector
    Font: Font
    FontScale: float



class WalkableSlopeOverride:
    WalkableSlopeBehavior: int
    WalkableSlopeAngle: float



class PrimitiveComponentPostPhysicsTickFunction(TickFunction): ...


class BodyInstance:
    ObjectType: int
    CollisionEnabled: int
    SleepFamily: ESleepFamily
    DOFMode: int
    bUseCCD: bool
    bNotifyRigidBodyCollision: bool
    bSimulatePhysics: bool
    bOverrideMass: bool
    bEnableGravity: bool
    bAutoWeld: bool
    bStartAwake: bool
    bGenerateWakeEvents: bool
    bUpdateMassWhenScaleChanges: bool
    bLockTranslation: bool
    bLockRotation: bool
    bLockXTranslation: bool
    bLockYTranslation: bool
    bLockZTranslation: bool
    bLockXRotation: bool
    bLockYRotation: bool
    bLockZRotation: bool
    bOverrideMaxAngularVelocity: bool
    bUseAsyncScene: bool
    bReportQueriesAsBelongingToWelded: bool
    bOverrideMaxDepenetrationVelocity: bool
    bOverrideWalkableSlopeOnInstance: bool
    bInterpolateWhenSubStepping: bool
    CollisionProfileName: str
    CollisionResponses: CollisionResponse
    MaxDepenetrationVelocity: float
    MassInKgOverride: float
    LinearDamping: float
    AngularDamping: float
    CustomDOFPlaneNormal: core_uobject.Vector
    COMNudge: core_uobject.Vector
    MassScale: float
    InertiaTensorScale: core_uobject.Vector
    NavUsePreset: EHavokNavPresets
    bOverrideNavGeometrySettingsOnInstance: bool
    NavGeometrySettings: HavokNavGeometrySettings
    WalkableSlopeOverride: WalkableSlopeOverride
    PhysMaterialOverride: PhysicalMaterial
    MaxAngularVelocity: float
    CustomSleepThresholdMultiplier: float
    StabilizationThresholdMultiplier: float
    PhysicsBlendWeight: float
    PositionSolverIterationCount: int
    VelocitySolverIterationCount: int
    bForceUseCollisionPropertiesInBody: bool



class HavokNavGeometrySettings:
    NavigationGeometrySource: int
    NavigationGeometryUsage: int
    GbxNavArea: GbxNavAreaBase
    Mobility: EHavokNavMobility
    PainterId: int
    NavArea: unreal.UClass



class CollisionResponse:
    ResponseToChannels: CollisionResponseContainer
    ResponseArray: unreal.WrappedArray[ResponseChannel]



class ResponseChannel:
    Channel: str
    Response: int



class LightingChannels:
    bChannel1: bool
    bChannel2: bool



class ConstraintInstance:
    JointName: str
    ConstraintBone1: str
    ConstraintBone2: str
    Pos1: core_uobject.Vector
    PriAxis1: core_uobject.Vector
    SecAxis1: core_uobject.Vector
    Pos2: core_uobject.Vector
    PriAxis2: core_uobject.Vector
    SecAxis2: core_uobject.Vector
    AngularRotationOffset: core_uobject.Rotator
    bScaleLinearLimits: bool
    ProfileInstance: ConstraintProfileProperties



class ConstraintProfileProperties:
    ProjectionLinearTolerance: float
    ProjectionAngularTolerance: float
    LinearBreakThreshold: float
    AngularBreakThreshold: float
    LinearLimit: LinearConstraint
    ConeLimit: ConeConstraint
    TwistLimit: TwistConstraint
    LinearDrive: LinearDriveConstraint
    AngularDrive: AngularDriveConstraint
    bDisableCollision: bool
    bParentDominates: bool
    bEnableProjection: bool
    bAngularBreakable: bool
    bLinearBreakable: bool



class AngularDriveConstraint:
    TwistDrive: ConstraintDrive
    SwingDrive: ConstraintDrive
    SlerpDrive: ConstraintDrive
    OrientationTarget: core_uobject.Rotator
    AngularVelocityTarget: core_uobject.Vector
    AngularDriveMode: int



class ConstraintDrive:
    Stiffness: float
    Damping: float
    MaxForce: float
    bEnablePositionDrive: bool
    bEnableVelocityDrive: bool



class LinearDriveConstraint:
    PositionTarget: core_uobject.Vector
    VelocityTarget: core_uobject.Vector
    XDrive: ConstraintDrive
    YDrive: ConstraintDrive
    ZDrive: ConstraintDrive
    bEnablePositionDrive: bool



class ConstraintBaseParams:
    Stiffness: float
    Damping: float
    Restitution: float
    ContactDistance: float
    bSoftConstraint: bool



class TwistConstraint(ConstraintBaseParams):
    TwistLimitDegrees: float
    TwistMotion: int



class ConeConstraint(ConstraintBaseParams):
    Swing1LimitDegrees: float
    Swing2LimitDegrees: float
    Swing1Motion: int
    Swing2Motion: int



class LinearConstraint(ConstraintBaseParams):
    Limit: float
    XMotion: int
    YMotion: int
    ZMotion: int



class ConstrainComponentPropName:
    ComponentName: str



class TableRowBase: ...


class MemberReference:
    MemberParent: unreal.UObject
    MemberScope: str
    MemberName: str
    MemberGuid: core_uobject.Guid
    bSelfContext: bool
    bWasDeprecated: bool



class AnimNode_Base:
    EvaluateGraphExposedInputs: ExposedValueHandler



class ExposedValueHandler:
    BoundFunction: str
    CopyRecords: unreal.WrappedArray[ExposedValueCopyRecord]
    Function: core_uobject.Function



class ExposedValueCopyRecord:
    SourceProperty: core_uobject.Property
    SourcePropertyName: str
    SourceSubPropertyName: str
    SourceArrayIndex: int
    DestProperty: core_uobject.Property
    DestArrayIndex: int
    Size: int
    bInstanceIsTarget: bool
    PostCopyOperation: EPostCopyOperation
    CopyType: ECopyType
    CachedSourceProperty: core_uobject.Property
    CachedSourceStructSubProperty: core_uobject.Property



class PoseLinkBase:
    LinkID: int



class ComponentSpacePoseLink(PoseLinkBase): ...


class DirectoryPath:
    Path: str



class AnimInstanceProxy: ...


class CollectionParameterBase:
    ParameterName: str
    ID: core_uobject.Guid



class InputScaleBiasClamp:
    bMapRange: bool
    InRange: InputRange
    OutRange: InputRange
    Scale: float
    Bias: float
    bClampResult: bool
    ClampMin: float
    ClampMax: float
    bInterpResult: bool
    InterpSpeedIncreasing: float
    InterpSpeedDecreasing: float
    InterpolatedResult: float
    bInitialized: bool



class InputRange:
    Min: float
    Max: float



class InputAlphaBoolBlend:
    BlendInTime: float
    BlendOutTime: float
    BlendOption: EAlphaBlendOption
    CustomCurve: CurveFloat
    AlphaBlend: AlphaBlend
    bInitialized: bool



class AlphaBlend:
    BlendOption: EAlphaBlendOption
    CustomCurve: CurveFloat
    BlendTime: float



class InputScaleBias:
    Scale: float
    Bias: float



class BoneReference:
    BoneName: str



class ThumbnailParameters:
    Pitch: float
    Yaw: float
    Zoom: float
    FOV: float



class PerPlatformInt:
    Default: int



class PerPlatformFloat:
    Default: float



class KeyHandleLookupTable: ...


class AnimNode_AssetPlayerBase(AnimNode_Base):
    bIgnoreForRelevancyTest: bool
    GroupIndex: int
    GroupRole: int
    BlendWeight: float
    InternalTimeAccumulator: float
    AnimAssetName: str
    LastAnimAssetName: str



class NodeGaitScalingData:
    bUseGaitScaling: bool



class BlendSampleData:
    SampleDataIndex: int
    Animation: AnimSequence
    TotalWeight: float
    Time: float
    PreviousTime: float
    SamplePlayRate: float



class BlendFilter: ...


class PoseLink(PoseLinkBase): ...


class PerBoneBlendWeight:
    SourceIndex: int
    BlendWeight: float



class InputBlendPose:
    BranchFilters: unreal.WrappedArray[BranchFilter]



class BranchFilter:
    BoneName: str
    BlendDepth: int



class BoneSetWeight:
    SourceIndex: int
    BlendWeight: float
    bAdditive: bool
    bMeshSpaceRotation: bool



class PoseSnapshot:
    LocalTransforms: unreal.WrappedArray[core_uobject.Transform]
    BoneNames: unreal.WrappedArray[str]
    SkeletalMeshName: str
    SnapshotName: str
    bIsValid: bool



class SplineCurves:
    Position: core_uobject.InterpCurveVector
    Rotation: core_uobject.InterpCurveQuat
    Scale: core_uobject.InterpCurveVector
    ReparamTable: core_uobject.InterpCurveFloat



class AnimCurveParam:
    Name: str



class KAggregateGeom:
    SphereElems: unreal.WrappedArray[KSphereElem]
    BoxElems: unreal.WrappedArray[KBoxElem]
    SphylElems: unreal.WrappedArray[KSphylElem]
    ConvexElems: unreal.WrappedArray[KConvexElem]
    TaperedCapsuleElems: unreal.WrappedArray[KTaperedCapsuleElem]



class KShapeElem:
    RestOffset: float
    Name: str
    bContributeToMass: bool
    CollisionEnabled: int
    PrimitivePhysicalMaterial: PhysicalMaterial
    bIsGestaltCollision: bool
    GestaltPartName: str
    GestaltPartNames: unreal.WrappedArray[str]



class KTaperedCapsuleElem(KShapeElem):
    Center: core_uobject.Vector
    Rotation: core_uobject.Rotator
    Radius1: float
    Length: float



class KConvexElem(KShapeElem):
    VertexData: unreal.WrappedArray[core_uobject.Vector]
    ElemBox: core_uobject.Box
    Transform: core_uobject.Transform



class KSphylElem(KShapeElem):
    TM: core_uobject.Matrix
    Orientation: core_uobject.Quat
    Center: core_uobject.Vector
    Rotation: core_uobject.Rotator
    Radius: float
    Length: float



class KBoxElem(KShapeElem):
    TM: core_uobject.Matrix
    Orientation: core_uobject.Quat
    Center: core_uobject.Vector
    Rotation: core_uobject.Rotator
    X: float
    Y: float
    Z: float



class KSphereElem(KShapeElem):
    TM: core_uobject.Matrix
    Center: core_uobject.Vector
    Radius: float



class AnimationGroupReference:
    GroupName: str
    GroupRole: int



class AnimGroupInstance: ...


class AnimTickRecord:
    SourceAsset: AnimationAsset



class MarkerSyncAnimPosition:
    PreviousMarkerName: str
    NextMarkerName: str
    PositionBetweenMarkers: float



class AnimationRecordingSettings:
    bRecordInWorldSpace: bool
    bRemoveRootAnimation: bool
    bAutoSaveAsset: bool
    SampleRate: float
    Length: float
    InterpMode: int
    TangentMode: int



class AnimCompressProfile:
    DefaultVirtualVertexDistance: float
    SafeVirtualVertexDistance: float
    SafetyFallbackThreshold: float
    ErrorThreshold: float
    BoneToIgnores: unreal.WrappedArray[str]



class ComponentSpacePose:
    Transforms: unreal.WrappedArray[core_uobject.Transform]
    Names: unreal.WrappedArray[str]



class LocalSpacePose:
    Transforms: unreal.WrappedArray[core_uobject.Transform]
    Names: unreal.WrappedArray[str]



class NamedTransform:
    Value: core_uobject.Transform
    Name: str



class NamedColor:
    Value: core_uobject.Color
    Name: str



class NamedVector:
    Value: core_uobject.Vector
    Name: str



class NamedFloat:
    Value: float
    Name: str



class AnimParentNodeAssetOverride:
    NewAsset: AnimationAsset
    ParentNodeGuid: core_uobject.Guid



class AnimGroupInfo:
    Name: str
    Color: core_uobject.LinearColor



class AnimBlueprintDebugData: ...


class AnimationFrameSnapshot: ...


class StateMachineDebugData: ...


class AnimTrack:
    AnimSegments: unreal.WrappedArray[AnimSegment]



class AnimSegment:
    AnimReference: AnimSequenceBase
    StartPos: float
    AnimStartTime: float
    AnimEndTime: float
    AnimPlayRate: float
    LoopingCount: int



class RootMotionExtractionStep:
    AnimSequence: AnimSequence
    StartPosition: float
    EndPosition: float



class RawCurveTracks:
    FloatCurves: unreal.WrappedArray[FloatCurve]
    RootMotionCurves: unreal.WrappedArray[TransformCurve]



class TransformCurve(AnimCurveBase):
    TranslationCurve: VectorCurve
    RotationCurve: VectorCurve
    ScaleCurve: VectorCurve



class VectorCurve(AnimCurveBase):
    FloatCurves: RichCurve



class SlotEvaluationPose:
    AdditiveType: int
    Weight: float



class A2Pose:
    Bones: unreal.WrappedArray[core_uobject.Transform]



class A2CSPose(A2Pose):
    ComponentSpaceFlags: unreal.WrappedArray[int]



class QueuedDrawDebugItem:
    ItemType: int
    StartLoc: core_uobject.Vector
    EndLoc: core_uobject.Vector
    Center: core_uobject.Vector
    Rotation: core_uobject.Rotator
    Radius: float
    Size: float
    Segments: int
    Color: core_uobject.Color
    bPersistentLines: bool
    LifeTime: float
    Thickness: float
    MESSAGE: str
    TextScale: core_uobject.Vector2D



class AnimLinkableElement:
    LinkedMontage: AnimMontage
    SlotIndex: int
    SegmentIndex: int
    LinkMethod: int
    CachedLinkMethod: int
    SegmentBeginTime: float
    SegmentLength: float
    LinkValue: float
    LinkedSequence: AnimSequenceBase



class AnimMontageInstance:
    Montage: AnimMontage
    bPlaying: bool
    DefaultBlendTimeMultiplier: float
    NextSections: unreal.WrappedArray[int]
    PrevSections: unreal.WrappedArray[int]
    ActiveStateBranchingPoints: unreal.WrappedArray[AnimNotifyEvent]
    Position: float
    PlayRate: float
    Blend: AlphaBlend
    DisableRootMotionCount: int



class AnimNotifyEvent(AnimLinkableElement):
    DisplayTime: float
    TriggerTimeOffset: float
    EndTriggerTimeOffset: float
    TriggerWeightThreshold: float
    NotifyName: str
    Notify: AnimNotify
    NotifyStateClass: AnimNotifyState
    Duration: float
    EndLink: AnimLinkableElement
    bConvertedFromBranchingPoint: bool
    MontageTickType: int
    NotifyTriggerChance: float
    NotifyFilterType: int
    NotifyFilterLOD: int
    bTriggerOnDedicatedServer: bool
    bTriggerOnFollower: bool
    TrackIndex: int



class BranchingPointMarker:
    NotifyIndex: int
    TriggerTime: float
    NotifyEventType: int



class BranchingPoint(AnimLinkableElement):
    EventName: str
    DisplayTime: float
    TriggerTimeOffset: float



class SlotAnimationTrack:
    SlotName: str
    AnimTrack: AnimTrack



class CompositeSection(AnimLinkableElement):
    SectionName: str
    StartTime: float
    NextSectionName: str
    MetaData: unreal.WrappedArray[AnimMetaData]



class AnimNode_ApplyMeshSpaceAdditive(AnimNode_Base):
    Base: PoseLink
    Additive: PoseLink
    Alpha: float
    AlphaScaleBias: InputScaleBias
    LODThreshold: int
    ActualAlpha: float
    bBoolAlpha: bool
    bUseBoolAlpha: bool
    bInvertAlpha: bool



class AnimNode_SaveCachedPose(AnimNode_Base):
    Pose: PoseLink
    CachePoseName: str
    GlobalWeight: float



class AnimNode_SequencePlayer(AnimNode_AssetPlayerBase):
    Sequence: AnimSequenceBase
    bLoopAnimation: bool
    PlayRateBasis: float
    PlayRate: float
    PlayRateScaleBiasClamp: InputScaleBiasClamp
    StartPosition: float
    bUseRateScaleSpeed: bool
    RateScaleSpeed: float
    Duration: float
    GaitScalingData: NodeGaitScalingData
    bCalcStartPositionFromCurrentPose: bool
    bStartAtRandomPosition: bool
    MinMaxPlayRate: core_uobject.Vector2D



class AnimNode_StateMachine(AnimNode_Base):
    StateMachineIndexInClass: int
    MaxTransitionsPerFrame: int
    bSkipFirstUpdateTransition: bool
    bReinitializeOnBecomingRelevant: bool
    CurrentState: int
    ElapsedTime: float
    BoneSetPriority: int



class AnimationPotentialTransition: ...


class AnimationActiveTransitionEntry:
    BlendProfile: BlendProfile



class AnimNode_SubInput(AnimNode_Base): ...


class AnimNode_SubInstance(AnimNode_Base):
    InPose: PoseLink
    InstanceClass: unreal.UClass
    InstanceToRun: AnimInstance
    InstanceProperties: unreal.WrappedArray[core_uobject.Property]
    SubInstanceProperties: unreal.WrappedArray[core_uobject.Property]
    SourcePropertyNames: unreal.WrappedArray[str]
    DestPropertyNames: unreal.WrappedArray[str]



class AnimNode_TransitionPoseEvaluator(AnimNode_Base):
    DataSource: int
    EvaluatorMode: int
    FramesToCachePose: int
    CacheFramesRemaining: int



class AnimNode_TransitionResult(AnimNode_Base):
    bCanEnterTransition: bool



class AnimNode_UseCachedPose(AnimNode_Base):
    LinkToCachingNode: PoseLink
    CachePoseName: str



class AnimNode_ConvertLocalToComponentSpace(AnimNode_Base):
    LocalPose: PoseLink



class AnimNode_ConvertComponentToLocalSpace(AnimNode_Base):
    ComponentPose: ComponentSpacePoseLink



class AnimNotifyQueue:
    AnimNotifies: unreal.WrappedArray[AnimNotifyEventReference]



class AnimNotifyArray:
    Notifies: unreal.WrappedArray[AnimNotifyEventReference]



class AnimNotifyEventReference:
    NotifySource: unreal.UObject



class CompressedTrack:
    ByteStream: unreal.WrappedArray[int]
    Times: unreal.WrappedArray[float]
    Mins: float
    Ranges: float



class CurveTrack:
    CurveName: str
    CurveWeights: unreal.WrappedArray[float]



class ScaleTrack:
    ScaleKeys: unreal.WrappedArray[core_uobject.Vector]
    Times: unreal.WrappedArray[float]



class RotationTrack:
    RotKeys: unreal.WrappedArray[core_uobject.Quat]
    Times: unreal.WrappedArray[float]



class TranslationTrack:
    PosKeys: unreal.WrappedArray[core_uobject.Vector]
    Times: unreal.WrappedArray[float]



class TrackToSkeletonMap:
    BoneTreeIndex: int



class AnimSequenceTrackContainer:
    AnimationTracks: unreal.WrappedArray[RawAnimSequenceTrack]
    TrackNames: unreal.WrappedArray[str]



class RawAnimSequenceTrack:
    PosKeys: unreal.WrappedArray[core_uobject.Vector]
    RotKeys: unreal.WrappedArray[core_uobject.Quat]
    ScaleKeys: unreal.WrappedArray[core_uobject.Vector]



class AnimSetMeshLinkup:
    BoneToTrackTable: unreal.WrappedArray[int]



class AnimSingleNodeInstanceProxy(AnimInstanceProxy): ...


class AnimNode_SingleNode(AnimNode_Base):
    SourcePose: PoseLink



class BakedAnimationStateMachine:
    MachineName: str
    InitialState: int
    States: unreal.WrappedArray[BakedAnimationState]
    Transitions: unreal.WrappedArray[AnimationTransitionBetweenStates]
    BoneSetPriority: int



class AnimationStateBase:
    StateName: str



class AnimationTransitionBetweenStates(AnimationStateBase):
    PreviousState: int
    NextState: int
    CrossfadeDuration: float
    StartNotify: int
    EndNotify: int
    InterruptNotify: int
    BlendMode: EAlphaBlendOption
    CustomCurve: CurveFloat
    BlendProfile: BlendProfile
    LogicType: int
    BlendStartTime: int
    bResetDestinationState: bool
    RootMotionBlendType: ERootMotionBlendType



class BakedAnimationState:
    StateName: str
    Transitions: unreal.WrappedArray[BakedStateExitTransition]
    StateRootNodeIndex: int
    StartNotify: int
    EndNotify: int
    FullyBlendedNotify: int
    bIsAConduit: bool
    EntryRuleNodeIndex: int
    PlayerNodeIndices: unreal.WrappedArray[int]
    bAlwaysResetOnEntry: bool
    Manager: GbxAnimStateManager
    AnimStateBoneSet: GbxBoneSet



class BakedStateExitTransition:
    CanTakeDelegateIndex: int
    CustomResultNodeIndex: int
    TransitionIndex: int
    bDesiredTransitionReturnValue: bool
    bAutomaticRemainingTimeRule: bool
    PoseEvaluatorLinks: unreal.WrappedArray[int]



class AnimationState(AnimationStateBase):
    Transitions: unreal.WrappedArray[AnimationTransitionRule]
    StateRootNodeIndex: int
    StartNotify: int
    EndNotify: int
    FullyBlendedNotify: int



class AnimationTransitionRule:
    RuleToExecute: str
    TransitionReturnVal: bool
    TransitionIndex: int



class MarkerSyncData:
    AuthoredSyncMarkers: unreal.WrappedArray[AnimSyncMarker]



class AnimSyncMarker:
    MarkerName: str
    Time: float



class AnimNotifyTrack:
    TrackName: str
    TrackColor: core_uobject.LinearColor
    LockState: FAnimNotifyTrackLockState
    bIsAutoGenerated: bool



class PerBoneBlendWeights:
    BoneBlendWeights: unreal.WrappedArray[PerBoneBlendWeight]



class AssetImportInfo: ...


class PrimaryAssetRulesOverride:
    PrimaryAssetId: core_uobject.PrimaryAssetId
    Rules: PrimaryAssetRules



class PrimaryAssetRules:
    Priority: int
    bApplyRecursively: bool
    ChunkId: int
    CookRule: EPrimaryAssetCookRule



class AssetManagerRedirect:
    Old: str
    New: str



class PrimaryAssetTypeInfo:
    PrimaryAssetType: str
    AssetBaseClassLoaded: unreal.UClass
    bHasBlueprintClasses: bool
    bIsEditorOnly: bool
    Directories: unreal.WrappedArray[DirectoryPath]
    SpecificAssets: unreal.WrappedArray[core_uobject.SoftObjectPath]
    Rules: PrimaryAssetRules
    AssetScanPaths: unreal.WrappedArray[str]
    bIsDynamicAsset: bool
    NumberOfAssets: int
    bSearchAllDirectories: bool



class AssetMapping:
    SourceAsset: AnimationAsset
    TargetAsset: AnimationAsset



class AtmospherePrecomputeParameters:
    DensityHeight: float
    DecayHeight: float
    MaxScatteringOrder: int
    TransmittanceTexWidth: int
    TransmittanceTexHeight: int
    IrradianceTexWidth: int
    IrradianceTexHeight: int
    InscatterAltitudeSampleNum: int
    InscatterMuNum: int
    InscatterMuSNum: int
    InscatterNuNum: int



class BaseAttenuationSettings:
    DistanceAlgorithm: EAttenuationDistanceModel
    AttenuationShape: int
    dBAttenuationAtMax: float
    AttenuationShapeExtents: core_uobject.Vector
    ConeOffset: float
    FalloffDistance: float
    CustomAttenuationCurve: RuntimeFloatCurve



class AudioComponentParam:
    ParamName: str
    FloatParam: float
    BoolParam: bool
    IntParam: int
    SoundWaveParam: SoundWave



class AudioQualitySettings:
    DisplayName: str
    MaxChannels: int



class InteriorSettings:
    bIsWorldSettings: bool
    ExteriorVolume: float
    ExteriorTime: float
    ExteriorLPF: float
    ExteriorLPFTime: float
    InteriorVolume: float
    InteriorTime: float
    InteriorLPF: float
    InteriorLPFTime: float



class ReverbSettings:
    bApplyReverb: bool
    ReverbType: int
    ReverbEffect: ReverbEffect
    ReverbPluginEffect: SoundEffectSubmixPreset
    Volume: float
    FadeTime: float



class LaunchOnTestSettings:
    LaunchOnTestmap: FilePath
    DeviceID: str



class FilePath:
    FilePath: str



class EditorMapPerformanceTestDefinition:
    PerformanceTestmap: core_uobject.SoftObjectPath
    TestTimer: int



class BuildPromotionTestSettings:
    DefaultStaticMeshAsset: FilePath
    ImportWorkflow: BuildPromotionImportWorkflowSettings
    OpenAssets: BuildPromotionOpenAssetSettings
    NewProjectSettings: BuildPromotionNewProjectSettings
    SourceControlMaterial: FilePath



class BuildPromotionNewProjectSettings:
    NewProjectFolderOverride: DirectoryPath
    NewProjectNameOverride: str



class BuildPromotionOpenAssetSettings:
    BlueprintAsset: FilePath
    MaterialAsset: FilePath
    ParticleSystemAsset: FilePath
    SkeletalMeshAsset: FilePath
    StaticMeshAsset: FilePath
    TextureAsset: FilePath



class BuildPromotionImportWorkflowSettings:
    Diffuse: EditorImportWorkflowDefinition
    Normal: EditorImportWorkflowDefinition
    StaticMesh: EditorImportWorkflowDefinition
    ReimportStaticMesh: EditorImportWorkflowDefinition
    BlendShapeMesh: EditorImportWorkflowDefinition
    MorphMesh: EditorImportWorkflowDefinition
    SkeletalMesh: EditorImportWorkflowDefinition
    Animation: EditorImportWorkflowDefinition
    Sound: EditorImportWorkflowDefinition
    SurroundSound: EditorImportWorkflowDefinition
    OtherAssetsToImport: unreal.WrappedArray[EditorImportWorkflowDefinition]



class EditorImportWorkflowDefinition:
    ImportFilePath: FilePath
    FactorySettings: unreal.WrappedArray[ImportFactorySettingValues]



class ImportFactorySettingValues:
    SettingName: str
    Value: str



class BlueprintEditorPromotionSettings:
    FirstMeshPath: FilePath
    SecondMeshPath: FilePath
    DefaultParticleAsset: FilePath



class ParticleEditorPromotionSettings:
    DefaultParticleAsset: FilePath



class MaterialEditorPromotionSettings:
    DefaultMaterialAsset: FilePath
    DefaultDiffuseTexture: FilePath
    DefaultNormalTexture: FilePath



class EditorImportExportTestDefinition:
    ImportFilePath: FilePath
    ExportFileExtension: str
    bSkipExport: bool
    FactorySettings: unreal.WrappedArray[ImportFactorySettingValues]



class ExternalToolDefinition:
    ToolName: str
    ExecutablePath: FilePath
    CommandLineOptions: str
    WorkingDirectory: DirectoryPath
    ScriptExtension: str
    ScriptDirectory: DirectoryPath



class NavAvoidanceData: ...


class BlendProfileBoneEntry:
    BoneReference: BoneReference
    BlendScale: float



class BlendSpaceInstance:
    BlendSpace: BlendSpaceBase



class PerBoneInterpolation:
    BoneReference: BoneReference
    InterpolationSpeedPerSec: float



class GridBlendSample:
    GridElement: EditorElement
    BlendWeight: float



class EditorElement:
    Indices: int
    Weights: float



class BlendSample:
    Animation: AnimSequence
    SampleValue: core_uobject.Vector
    RateScale: float



class BlendParameter:
    DisplayName: str
    Min: float
    Max: float
    GridNum: int



class InterpolationParameter:
    InterpolationTime: float
    InterpolationType: int



class BPEditorBookmarkNode:
    NodeGuid: core_uobject.Guid
    ParentGuid: core_uobject.Guid
    DisplayName: str



class EditedDocumentInfo:
    EditedObjectPath: core_uobject.SoftObjectPath
    SavedViewOffset: core_uobject.Vector2D
    SavedZoomAmount: float
    EditedObject: unreal.UObject



class BPInterfaceDescription:
    Interface: unreal.UClass
    Graphs: unreal.WrappedArray[EdGraph]



class BPVariableDescription:
    VarName: str
    VarGuid: core_uobject.Guid
    VarType: EdGraphPinType
    FriendlyName: str
    Category: str
    RepNotifyFunc: str
    ReplicationCondition: int
    MetaDataArray: unreal.WrappedArray[BPVariableMetaDataEntry]
    DefaultValue: str
    AssociatedBlueprintVariableGuid: core_uobject.Guid



class BPVariableMetaDataEntry:
    DataKey: str
    DataValue: str



class EdGraphPinType:
    PinCategory: str
    PinSubCategory: str
    PinSubCategoryObject: unreal.UObject
    PinSubCategoryMemberReference: SimpleMemberReference
    PinValueType: EdGraphTerminalType
    ContainerType: EPinContainerType
    bIsArray: bool
    bIsReference: bool
    bIsConst: bool
    bIsWeakPointer: bool
    bAllowMultipleConnection: bool



class EdGraphTerminalType:
    TerminalCategory: str
    TerminalSubCategory: str
    TerminalSubCategoryObject: unreal.UObject
    bTerminalIsConst: bool
    bTerminalIsWeakPointer: bool



class BlueprintMacroCosmeticInfo: ...


class CompilerNativizationOptions:
    PlatformName: str
    ServerOnlyPlatform: bool
    ClientOnlyPlatform: bool
    bExcludeMonolithicHeaders: bool
    ExcludedModules: unreal.WrappedArray[str]
    ExcludedFolderPaths: unreal.WrappedArray[str]



class BlueprintCookedComponentInstancingData:
    bIsValid: bool
    ChangedPropertyList: unreal.WrappedArray[BlueprintComponentChangedPropertyInfo]



class BlueprintComponentChangedPropertyInfo:
    PropertyName: str
    ArrayIndex: int
    PropertyScope: unreal.UStruct



class EventGraphFastCallPair:
    FunctionToPatch: core_uobject.Function
    EventGraphCallOffset: int



class BlueprintDebugData: ...


class PointerToUberGraphFrame: ...


class DebuggingInfoForSingleFunction: ...


class NodeToCodeAssociation: ...


class BoneModInstance:
    BoneName: str
    ComponentName: str
    Translation: core_uobject.Vector
    Rotation: core_uobject.Rotator
    Scale: core_uobject.Vector
    Blend: AlphaBlend
    bUseTranslation: bool
    bUseRotation: bool
    bUseScale: bool
    bReplaceTranslation: bool
    bReplaceRotation: bool
    bReplaceScale: bool
    bStartActive: bool
    TranslationSpace: int
    RotationSpace: int



class GeomSelection:
    Type: int
    Index: int
    SelectionIndex: int



class BuilderPoly:
    VertexIndices: unreal.WrappedArray[int]
    Direction: int
    ItemName: str
    PolyFlags: int



class CachedAnimTransitionData:
    StateMachineName: str
    FromStateName: str
    ToStateName: str



class CachedAnimRelevancyData:
    StateMachineName: str
    StateName: str



class CachedAnimAssetPlayerData:
    StateMachineName: str
    StateName: str



class CachedAnimStateArray:
    States: unreal.WrappedArray[CachedAnimStateData]



class CachedAnimStateData:
    StateMachineName: str
    StateName: str



class CameraShakeData: ...


class VOscillator:
    X: FOscillator
    Y: FOscillator
    Z: FOscillator



class FOscillator:
    Amplitude: float
    Frequency: float
    InitialOffset: int
    InitialOffsetValue: float



class ROscillator:
    Pitch: FOscillator
    Yaw: FOscillator
    Roll: FOscillator



class DummySpacerCameraTypes: ...


class MinimalViewInfo:
    Location: core_uobject.Vector
    Rotation: core_uobject.Rotator
    FOV: float
    ForegroundFOV: float
    DesiredFOV: float
    OrthoWidth: float
    OrthoNearClipPlane: float
    OrthoFarClipPlane: float
    AspectRatio: float
    bConstrainAspectRatio: bool
    bUseFieldOfViewForLOD: bool
    ProjectionMode: int
    PostProcessBlendWeight: float
    PostProcessSettings: PostProcessSettings
    OffCenterProjectionOffset: core_uobject.Vector2D
    bDisableSeparateTranslucency: bool



class CanvasIcon:
    Texture: Texture
    U: float
    V: float
    UL: float
    VL: float



class WrappedStringElement:
    Value: str
    LineExtent: core_uobject.Vector2D



class TextSizingParameters:
    DrawX: float
    DrawY: float
    DrawXL: float
    DrawYL: float
    Scaling: core_uobject.Vector2D
    DrawFont: Font
    SpacingAdjust: core_uobject.Vector2D



class CustomProfile:
    Name: str
    CustomResponses: unreal.WrappedArray[ResponseChannel]



class CustomChannelSetup:
    Channel: int
    Name: str
    DefaultResponse: int
    bTraceType: bool
    bStaticObject: bool



class CollisionResponseTemplate:
    Name: str
    CollisionEnabled: int
    ObjectTypeName: str
    CustomResponses: unreal.WrappedArray[ResponseChannel]
    HelpMessage: str
    bCanModify: bool



class BlueprintComponentDelegateBinding:
    ComponentPropertyName: str
    DelegatePropertyName: str
    FunctionNameToBind: str



class MeshUVChannelInfo:
    bInitialized: bool
    bOverrideDensities: bool
    LocalUVDensities: float



class AutoCompleteNode:
    IndexChar: int
    AutoCompleteListIndices: unreal.WrappedArray[int]



class CullDistanceSizePair:
    Size: float
    CullDistance: float



class RuntimeCurveLinearColor:
    ColorCurves: RichCurve
    ExternalCurve: CurveLinearColor



class NamedCurveValue:
    Name: str
    Value: float



class CurveTableRowHandle:
    CurveTable: CurveTable
    RowName: str



class DataTableCategoryHandle:
    DataTable: DataTable
    ColumnName: str
    RowContents: str



class DebugDisplayProperty:
    Obj: unreal.UObject
    WithinClass: unreal.UClass



class RollbackNetStartupActorInfo:
    Archetype: unreal.UObject
    Level: Level
    ObjReferences: unreal.WrappedArray[unreal.UObject]



class LevelNameAndTime:
    LevelName: str



class DialogueWaveParameter:
    DialogueWave: DialogueWave
    Context: DialogueContext



class DialogueContext:
    Speaker: DialogueVoice
    Targets: unreal.WrappedArray[DialogueVoice]



class DialogueContextMapping:
    Context: DialogueContext
    SoundWave: SoundWave
    LocalizationKeyFormat: str
    Proxy: DialogueSoundWaveProxy



class RawDistributionFloat(RawDistribution):
    MinValue: float
    MaxValue: float
    Distribution: DistributionFloat



class RawDistributionVector(RawDistribution):
    MinValue: float
    MaxValue: float
    MinValueVec: core_uobject.Vector
    MaxValueVec: core_uobject.Vector
    Distribution: DistributionVector



class GraphReference:
    MacroGraph: EdGraph
    GraphBlueprint: Blueprint
    GraphGuid: core_uobject.Guid



class EdGraphPinReference:
    OwningNode: EdGraphNode
    PinId: core_uobject.Guid



class EdGraphSchemaAction:
    MenuDescription: str
    TooltipDescription: str
    Category: str
    Keywords: str
    Grouping: int
    SectionID: int
    MenuDescriptionArray: unreal.WrappedArray[str]
    FullSearchTitlesArray: unreal.WrappedArray[str]
    FullSearchKeywordsArray: unreal.WrappedArray[str]
    FullSearchCategoryArray: unreal.WrappedArray[str]
    LocalizedMenuDescriptionArray: unreal.WrappedArray[str]
    LocalizedFullSearchTitlesArray: unreal.WrappedArray[str]
    LocalizedFullSearchKeywordsArray: unreal.WrappedArray[str]
    LocalizedFullSearchCategoryArray: unreal.WrappedArray[str]
    SearchText: str



class EdGraphSchemaAction_NewNode(EdGraphSchemaAction):
    NodeTemplate: EdGraphNode



class PluginRedirect:
    OldPluginName: str
    NewPluginName: str



class StructRedirect:
    OldStructName: str
    NewStructName: str



class ClassRedirect:
    ObjectName: str
    OldClassName: str
    NewClassName: str
    OldSubobjName: str
    NewSubobjName: str
    NewClassClass: str
    NewClassPackage: str
    InstanceOnly: bool



class GameNameRedirect:
    OldGameName: str
    NewGameName: str



class ScreenMessageString:
    ScreenMessage: str
    DisplayColor: core_uobject.Color
    TimeToDisplay: float
    CurrentTimeDisplayed: float
    TextScale: core_uobject.Vector2D



class DropNoteInfo:
    Location: core_uobject.Vector
    Rotation: core_uobject.Rotator
    Comment: str



class StatColorMapping:
    StatName: str
    ColorMap: unreal.WrappedArray[StatColorMapEntry]
    DisableBlend: bool



class StatColorMapEntry:
    In: float
    Out: core_uobject.Color



class WorldContext:
    LastURL: URL
    LastRemoteURL: URL
    PendingNetGame: PendingNetGame
    PackagesToFullyLoad: unreal.WrappedArray[FullyLoadedPackagesInfo]
    LoadedLevelsForPendingMapChange: unreal.WrappedArray[Level]
    ObjectReferencers: unreal.WrappedArray[ObjectReferencer]
    PendingLevelStreamingStatusUpdates: unreal.WrappedArray[LevelStreamingStatus]
    GameViewport: GameViewportClient
    OwningGameInstance: GameInstance
    ActiveNetDrivers: unreal.WrappedArray[NamedNetDriver]
    BeaconNetDrivers: unreal.WrappedArray[NamedNetDriver]



class NamedNetDriver:
    NetDriver: NetDriver



class LevelStreamingStatus:
    PackageName: str
    bShouldBeLoaded: bool
    bShouldBeVisible: bool



class FullyLoadedPackagesInfo:
    FullyLoadType: int
    Tag: str
    PackagesToLoad: unreal.WrappedArray[str]
    LoadedObjects: unreal.WrappedArray[unreal.UObject]



class URL:
    Protocol: str
    Host: str
    Port: int
    Map: str
    RedirectUrl: str
    Op: unreal.WrappedArray[str]
    Portal: str
    Valid: int



class NetDriverDefinition:
    DefName: str
    DriverClassName: str
    DriverClassNameFallback: str
    ChannelClassOverrides: unreal.WrappedArray[NetDriverChannelClassOverride]



class NetDriverChannelClassOverride:
    ChannelType: int
    ChannelClassName: str



class ExposureSettings:
    bFixed: bool



class TickPrerequisite: ...


class LODPlatformSettings:
    QualitySettings: LODPerDetailSettings
    NumSettings: int



class LODPerDetailSettings:
    bEnabled: bool
    bOverrideScreenSize: bool
    OverrideScreenSize: float



class ClosestPointResult:
    Location: core_uobject.Vector
    Distance: float
    Component: PrimitiveComponent
    BoneName: str



class CanvasUVTri:
    V1_Pos: core_uobject.Vector2D
    V1_UV: core_uobject.Vector2D
    V1_Color: core_uobject.LinearColor
    V2_Pos: core_uobject.Vector2D
    V2_UV: core_uobject.Vector2D
    V2_Color: core_uobject.LinearColor



class FontRenderInfo:
    bClipText: bool
    bEnableShadow: bool
    GlowInfo: DepthFieldGlowInfo



class DepthFieldGlowInfo:
    bEnableGlow: bool
    GlowColor: core_uobject.LinearColor
    GlowOuterRadius: core_uobject.Vector2D
    GlowInnerRadius: core_uobject.Vector2D



class Redirector:
    OldName: str
    NewName: str



class CollectionReference:
    CollectionName: str



class ComponentReference:
    OtherActor: Actor
    ComponentProperty: str



class DamageEvent:
    DamageTypeClass: unreal.UClass



class RadialDamageEvent(DamageEvent):
    Params: RadialDamageParams
    Origin: core_uobject.Vector
    ComponentHits: unreal.WrappedArray[HitResult]



class RadialDamageParams:
    BaseDamage: float
    MinimumDamage: float
    InnerRadius: float
    OuterRadius: float
    DamageFalloff: float



class PointDamageEvent(DamageEvent):
    Damage: float
    ShotDirection: Vector_NetQuantizeNormal
    HitInfo: HitResult



class MeshBuildSettings:
    bUseMikkTSpace: bool
    bRecomputeNormals: bool
    bRecomputeTangents: bool
    bRemoveDegenerates: bool
    bBuildAdjacencyBuffer: bool
    bBuildReversedIndexBuffer: bool
    bUseHighPrecisionTangentBasis: bool
    bUseFullPrecisionUVs: bool
    bGenerateLightmapUVs: bool
    bGenerateDistanceFieldAsIfTwoSided: bool
    MinLightmapResolution: int
    SrcLightmapIndex: int
    DstLightmapIndex: int
    BuildScale: float
    BuildScale3D: core_uobject.Vector
    DistanceFieldResolutionScale: float
    DistanceFieldReplacementMesh: StaticMesh



class POV:
    Location: core_uobject.Vector
    Rotation: core_uobject.Rotator
    FOV: float



class AnimUpdateRateParameters:
    ShiftBucket: EUpdateRateShiftBucket
    bInterpolateSkippedFrames: bool
    bShouldUseLodMap: bool
    bShouldUseMinLod: bool
    bSkipUpdate: bool
    bSkipEvaluation: bool
    UpdateRate: int
    EvaluationRate: int
    TickedPoseOffestTime: float
    AdditionalTime: float
    BaseNonRenderedUpdateRate: int
    MaxEvalRateForInterpolation: int
    BaseVisibleDistanceFactorThesholds: unreal.WrappedArray[float]
    SkippedUpdateFrames: int
    SkippedEvalFrames: int



class AnimSlotDesc:
    SlotName: str
    NumChannels: int



class AnimSlotInfo:
    SlotName: str
    ChannelWeights: unreal.WrappedArray[float]



class MTDResult:
    Direction: core_uobject.Vector
    Distance: float



class OverlapResult:
    Actor: Actor
    Component: PrimitiveComponent
    bBlockingHit: bool



class PrimitiveMaterialRef:
    Primitive: PrimitiveComponent
    Decal: DecalComponent
    ElementIndex: int



class SwarmDebugOptions:
    bDistributionEnabled: bool
    bForceContentExport: bool
    bInitialized: bool



class LightmassDebugOptions:
    bDebugMode: bool
    bStatsEnabled: bool
    bGatherBSPSurfacesAcrossComponents: bool
    CoplanarTolerance: float
    bUseImmediateImport: bool
    bImmediateProcessMappings: bool
    bSortMappings: bool
    bDumpBinaryFiles: bool
    bDebugMaterials: bool
    bPadMappings: bool
    bDebugPaddings: bool
    bOnlyCalcDebugTexelMappings: bool
    bUseRandomColors: bool
    bColorBordersGreen: bool
    bColorByExecutionTime: bool
    ExecutionTimeDivisor: float



class LightmassPrimitiveSettings:
    bUseTwoSidedLighting: bool
    bShadowIndirectOnly: bool
    bUseEmissiveForStaticLighting: bool
    bUseVertexNormalForHemisphereGather: bool
    EmissiveLightFalloffExponent: float
    EmissiveLightExplicitInfluenceRadius: float
    EmissiveBoost: float
    DiffuseBoost: float
    FullyOccludedSamplesFraction: float



class LightmassLightSettings:
    IndirectLightingSaturation: float
    ShadowExponent: float
    bUseAreaShadowsForStationaryLight: bool



class LightmassDirectionalLightSettings(LightmassLightSettings):
    LightSourceAngle: float



class LightmassPointLightSettings(LightmassLightSettings): ...


class LocalizedSubtitle:
    LanguageExt: str
    Subtitles: unreal.WrappedArray[SubtitleCue]
    bMature: bool
    bManualWordWrap: bool
    bSingleLine: bool



class BasedPosition:
    Base: Actor
    Position: core_uobject.Vector
    CachedBaseLocation: core_uobject.Vector
    CachedBaseRotation: core_uobject.Rotator
    CachedTransPosition: core_uobject.Vector



class FractureEffect:
    ParticleSystem: ParticleSystem
    Sound: SoundBase



class CollisionImpactData:
    ContactInfos: unreal.WrappedArray[RigidBodyContactInfo]
    TotalNormalImpulse: core_uobject.Vector
    TotalFrictionImpulse: core_uobject.Vector



class RigidBodyContactInfo:
    ContactPosition: core_uobject.Vector
    ContactNormal: core_uobject.Vector
    ContactPenetration: float
    PhysMaterial: PhysicalMaterial
    RelativeVelocity: core_uobject.Vector



class RigidBodyErrorCorrection:
    PingExtrapolation: float
    ErrorPerLinearDifference: float
    ErrorPerAngularDifference: float
    MaxRestoredStateError: float
    MaxLinearHardSnapDistance: float
    PositionLerp: float
    AngleLerp: float
    LinearVelocityCoefficient: float
    AngularVelocityCoefficient: float
    ErrorAccumulationSeconds: float
    ErrorAccumulationDistanceSq: float
    ErrorAccumulationSimilarity: float



class RigidBodyState:
    Quaternion: core_uobject.Quat
    Flags: int



class FontCharacter:
    StartU: int
    StartV: int
    USize: int
    VSize: int
    TextureIndex: int
    VerticalOffset: int



class FontImportOptionsData:
    FontName: str
    Height: float
    bEnableAntialiasing: bool
    bEnableBold: bool
    bEnableItalic: bool
    bEnableUnderline: bool
    bAlphaOnly: bool
    CharacterSet: int
    Chars: str
    UnicodeRange: str
    CharsFilePath: str
    CharsFileWildcard: str
    bCreatePrintableOnly: bool
    bIncludeASCIIRange: bool
    ForegroundColor: core_uobject.LinearColor
    bEnableDropShadow: bool
    TexturePageWidth: int
    TexturePageMaxHeight: int
    XPadding: int
    YPadding: int
    ExtendBoxTop: int
    ExtendBoxBottom: int
    ExtendBoxRight: int
    ExtendBoxLeft: int
    bEnableLegacyMode: bool
    Kerning: int
    bUseDistanceFieldAlpha: bool
    DistanceFieldScaleFactor: int
    DistanceFieldScanRadiusScale: float



class ForceFeedbackAttenuationSettings(BaseAttenuationSettings): ...


class GaitScalingSettings:
    GaitScalingAlpha: float
    GaitScalingInterpSpeed: float
    GaitScalingHips: BoneReference
    GaitScalingLimbs: unreal.WrappedArray[GaitLimb]
    AppliedLimbLength: float
    HipRaiseRatio: float



class GaitLimb:
    EffectorLimb: BoneReference
    MaxLength: float



class CalculateGaitLimbMaxLengthButton: ...


class GameObjectPoolManager: ...


class PredictProjectilePathParams:
    StartLocation: core_uobject.Vector
    LaunchVelocity: core_uobject.Vector
    bTraceWithCollision: bool
    ProjectileRadius: float
    MaxSimTime: float
    bTraceWithChannel: bool
    TraceChannel: int
    ObjectTypes: unreal.WrappedArray[int]
    ActorsToIgnore: unreal.WrappedArray[Actor]
    SimFrequency: float
    OverrideGravityZ: float
    DrawDebugType: int
    DrawDebugTime: float
    bTraceComplex: bool



class GbxAnimManagerData:
    OccasionalTickRate: int
    MaxEvalRateForInterpolation: int
    UpdateRateThresholds: unreal.WrappedArray[float]



class GbxAnimSetPair:
    bActive: bool
    AnimSet: GbxAnimSet



class GbxStateManagerRuntime: ...


class GbxStateManagerId: ...


class CurveWeightOverride:
    StartBoneName: str
    OptionalEndBoneName: str
    WeightModifierType: ECurveOverrideType
    BlendDepth: int
    OverrideCurveName: str
    NormalizeCurvesOverride: NormalizeCurvesOverride
    Weight: float



class NormalizeCurvesOverride:
    CurveNames: unreal.WrappedArray[str]
    RangeMin: float
    RangeMax: float



class GbxBoneSetEntry:
    Bone: BoneReference
    BlendDepth: int
    Weight: float
    bAdditive: bool
    bMeshSpaceRotation: bool



class AutoLightMapResEntry:
    ScaleDeviation: float
    PowerOfTwoExponent: int



class GbxSpawnActorAsyncRequest:
    Class: unreal.UClass
    Transform: core_uobject.Transform
    TransformActor: Actor
    TransformComponent: SceneComponent
    TransformSocketName: str
    TransformSocketNames: unreal.WrappedArray[str]
    bTransformIgnorePitch: bool
    bComputeTransformWhenSpawned: bool
    Owner: Actor
    Instigator: Actor
    Template: Actor
    Delay: float
    ForceSpawnTimer: float
    InstanceCount: int
    InstanceDelay: float
    bStopOnInstigatorDeath: bool
    bSkipOnClients: bool
    SnapToGroundSearchExtent: float
    bCancelIfGroundNotFound: bool
    bAlignToGroundNormal: bool
    CollisionHandling: ESpawnActorCollisionHandlingMethod
    Name: str
    bDeferConstruction: bool
    ExposeOnSpawnCache: GbxExposeOnSpawnValueCache



class GbxExposeOnSpawnValueCache: ...


class GbxSpawnActorAsyncRequestEntry(GbxSpawnActorAsyncRequest): ...


class GbxTraceAsyncRequest:
    Mode: EGbxTraceAsyncMode
    Channel: int
    ObjectType: int
    ObjectTypes: unreal.WrappedArray[int]
    Type: EGbxTraceAsyncType
    Start: core_uobject.Vector
    End: core_uobject.Vector
    Radius: float
    CapsuleHalfHeight: float
    BoxHalfSize: core_uobject.Vector
    bTraceComplex: bool
    bIgnoreSelf: bool
    ActorsToIgnore: unreal.WrappedArray[Actor]
    Name: str
    DebugDrawType: int
    DebugTraceColor: core_uobject.LinearColor
    DebugTraceHitColor: core_uobject.LinearColor
    DebugDrawTime: float



class GbxViewFlagSettings:
    Flag: EGbxViewFlag
    Name: str
    bOwner: bool
    bOnlyOwner: bool
    bOnlyViewportOwner: bool



class GbxZoneMapFODSavedLevelData:
    LevelName: str
    DiscoveryPercentage: float
    DataState: int
    FODData: unreal.WrappedArray[int]



class GestaltSocketMapping:
    PartName: str
    OriginalSocketName: str
    MappedName: str



class GestaltInfo:
    Parts: unreal.WrappedArray[GestaltPart]



class GestaltPart:
    SkeletalMeshFragmentName: str
    MaterialIndex: int
    FirstIndex: int
    NumPrimitives: int
    SupportedClothAsset: core_uobject.Guid



class GestaltPartBoundsEntry:
    PartName: str
    ReferencePoseBounds: core_uobject.BoxSphereBounds



class ActiveHapticFeedbackEffect:
    HapticEffect: HapticFeedbackEffect_Base



class HapticFeedbackDetails_Curve:
    Frequency: RuntimeFloatCurve
    Amplitude: RuntimeFloatCurve



class ClusterNode:
    BoundMin: core_uobject.Vector
    FirstChild: int
    BoundMax: core_uobject.Vector
    LastChild: int
    FirstInstance: int
    LastInstance: int
    MinInstanceScale: core_uobject.Vector
    MaxInstanceScale: core_uobject.Vector



class ClusterNode_DEPRECATED:
    BoundMin: core_uobject.Vector
    FirstChild: int
    BoundMax: core_uobject.Vector
    LastChild: int
    FirstInstance: int
    LastInstance: int



class HLODProxyMesh:
    StaticMesh: StaticMesh
    Key: str



class ImportanceTexture:
    Size: core_uobject.IntPoint
    NumMips: int
    MarginalCDF: unreal.WrappedArray[float]
    ConditionalCDF: unreal.WrappedArray[float]
    TextureData: unreal.WrappedArray[core_uobject.Color]
    Texture: Texture2D
    Weighting: int



class ComponentOverrideRecord:
    ComponentClass: unreal.UClass
    ComponentTemplate: ActorComponent
    ComponentKey: ComponentKey
    CookedComponentInstancingData: BlueprintCookedComponentInstancingData



class ComponentKey:
    OwnerClass: unreal.UClass
    SCSVariableName: str
    AssociatedGuid: core_uobject.Guid



class BlueprintInputDelegateBinding:
    bConsumeInput: bool
    bExecuteWhenPaused: bool
    bOverrideParentBinding: bool



class BlueprintInputActionDelegateBinding(BlueprintInputDelegateBinding):
    InputActionName: str
    InputKeyEvent: int
    FunctionNameToBind: str



class BlueprintInputAxisDelegateBinding(BlueprintInputDelegateBinding):
    InputAxisName: str
    FunctionNameToBind: str



class BlueprintInputAxisKeyDelegateBinding(BlueprintInputDelegateBinding):
    AxisKey: input_core.Key
    FunctionNameToBind: str



class CachedKeyToActionInfo:
    PlayerInput: PlayerInput



class BlueprintInputKeyDelegateBinding(BlueprintInputDelegateBinding):
    InputChord: slate.InputChord
    InputKeyEvent: int
    FunctionNameToBind: str



class BlueprintInputTouchDelegateBinding(BlueprintInputDelegateBinding):
    InputKeyEvent: int
    FunctionNameToBind: str



class InstancedStaticMeshMappingInfo: ...


class InstancedStaticMeshInstanceData:
    Transform: core_uobject.Transform



class IntegralCurve(IndexedCurve):
    Keys: unreal.WrappedArray[IntegralKey]
    DefaultValue: int
    bUseDefaultValueBeforeFirstKey: bool



class IntegralKey:
    Time: float
    Value: int



class CurveEdTab:
    TabName: str
    Curves: unreal.WrappedArray[CurveEdEntry]
    ViewStartInput: float
    ViewEndInput: float
    ViewStartOutput: float
    ViewEndOutput: float



class CurveEdEntry:
    CurveObject: unreal.UObject
    CurveColor: core_uobject.Color
    CurveName: str
    bHideCurve: int
    bColorCurve: int
    bFloatingPointColorCurve: int
    bClamp: int
    ClampLow: float
    ClampHigh: float



class InterpEdSelKey:
    Group: InterpGroup
    Track: InterpTrack
    KeyIndex: int
    UnsnappedPosition: float



class CameraPreviewInfo:
    PawnClass: unreal.UClass
    AnimSeq: AnimSequence
    Location: core_uobject.Vector
    Rotation: core_uobject.Rotator
    PawnInst: Pawn



class SubTrackGroup:
    GroupName: str
    TrackIndices: unreal.WrappedArray[int]
    bIsCollapsed: bool
    bIsSelected: bool



class SupportedSubTrackInfo:
    SupportedClass: unreal.UClass
    SubTrackName: str
    GroupIndex: int



class AnimControlTrackKey:
    StartTime: float
    AnimSeq: AnimSequence
    AnimStartOffset: float
    AnimEndOffset: float
    AnimPlayRate: float
    bLooping: bool
    bReverse: bool



class BoolTrackKey:
    Time: float
    Value: bool



class DirectorTrackCut:
    Time: float
    TransitionTime: float
    TargetCamGroup: str
    ShotNumber: int



class EventTrackKey:
    Time: float
    EventName: str



class InterpLookupTrack:
    Points: unreal.WrappedArray[InterpLookupPoint]



class InterpLookupPoint:
    GroupName: str
    Time: float



class ParticleReplayTrackKey:
    Time: float
    Duration: float
    ClipIDNumber: int



class SoundTrackKey:
    Time: float
    Volume: float
    Pitch: float
    Sound: SoundBase



class ToggleTrackKey:
    Time: float
    ToggleAction: int



class VisibilityTrackKey:
    Time: float
    Action: int
    ActiveCondition: int



class VectorSpringState: ...


class FloatSpringState: ...


class DrawToRenderTargetContext:
    RenderTarget: TextureRenderTarget2D



class LatentActionManager: ...


class LayerActorStats:
    Type: unreal.UClass
    Total: int



class ReplicatedStaticActorDestructionInfo:
    ObjClass: unreal.UClass



class LevelSimplificationDetails:
    bCreatePackagePerAsset: bool
    DetailsPercentage: float
    StaticMeshMaterialSettings: MaterialProxySettings
    bOverrideLandscapeExportLOD: bool
    LandscapeExportLOD: int
    LandscapeMaterialSettings: MaterialProxySettings
    bBakeFoliageToLandscape: bool
    bBakeGrassToLandscape: bool
    bGenerateMeshNormalMap: bool
    bGenerateMeshMetallicMap: bool
    bGenerateMeshRoughnessMap: bool
    bGenerateMeshSpecularMap: bool
    bGenerateLandscapeNormalMap: bool
    bGenerateLandscapeMetallicMap: bool
    bGenerateLandscapeRoughnessMap: bool
    bGenerateLandscapeSpecularMap: bool
    bUseLandscapeCulling: bool
    LandscapeCullingPrecision: ELevelLandscapeCullingPrecision



class MaterialProxySettings:
    TextureSize: core_uobject.IntPoint
    TextureSizingType: int
    GutterSpace: float
    SamplingQuality: EMaterialProxySmaplingQuality
    UVStrech: EUVStrech
    bSplitProxyMaterialBasedOnType: bool
    bUseTangentSpace: bool
    bNormalMap: bool
    bMetallicMap: bool
    MetallicConstant: float
    bRoughnessMap: bool
    RoughnessConstant: float
    bSpecularMap: bool
    SpecularConstant: float
    bEmissiveMap: bool
    bOpacityMap: bool
    OpacityConstant: float
    AOConstant: float
    bOpacityMaskMap: bool
    OpacityMaskConstant: float
    bAmbientOcclusionMap: bool
    AmbientOcclusionConstant: float
    DiffuseTextureSize: core_uobject.IntPoint
    NormalTextureSize: core_uobject.IntPoint
    MetallicTextureSize: core_uobject.IntPoint
    RoughnessTextureSize: core_uobject.IntPoint
    SpecularTextureSize: core_uobject.IntPoint
    EmissiveTextureSize: core_uobject.IntPoint
    OpacityTextureSize: core_uobject.IntPoint
    OpacityMaskTextureSize: core_uobject.IntPoint
    AmbientOcclusionTextureSize: core_uobject.IntPoint
    MaterialMergeType: int
    BlendMode: int



class StreamableTextureInstance: ...


class DynamicTextureInstance(StreamableTextureInstance):
    Texture: Texture2D
    bAttached: bool
    OriginalRadius: float



class BatchedPoint:
    Position: core_uobject.Vector
    Color: core_uobject.LinearColor
    PointSize: float
    RemainingLifetime: float
    DepthPriority: int



class BatchedLine:
    Start: core_uobject.Vector
    End: core_uobject.Vector
    Color: core_uobject.LinearColor
    Thickness: float
    RemainingLifetime: float
    DepthPriority: int



class ClientReceiveData:
    LocalPC: PlayerController
    MessageType: str
    MessageIndex: int
    MessageString: str
    RelatedPlayerState_1: PlayerState
    RelatedPlayerState_2: PlayerState
    OptionalObject: unreal.UObject



class StaticLightingLevelInfo:
    StaticLightingBuildDateTime: core_uobject.DateTime
    StaticLightingBuildGuid: core_uobject.Guid
    NumLightmaps: int
    NumShadowmaps: int
    NumTexturesTotal: int
    LightMapSizeActualMB: float
    ShadowMapSizeActualMB: float
    LightMapSizeEstMB: float
    ShadowMapSizeEstMB: float
    TotalSizeEstMB: float
    TotalSizeActualMB: float
    LightMapUnusedSizeMB: float
    ShadowMapUnusedSizeMB: float
    TotalUnusedSizeMB: float



class ParameterGroupData:
    GroupName: str
    GroupSortPriority: int



class MaterialParameterCollectionInfo:
    StateId: core_uobject.Guid
    ParameterCollection: MaterialParameterCollection



class MaterialFunctionInfo:
    StateId: core_uobject.Guid
    Function: MaterialFunctionInterface



class MaterialSpriteElement:
    Material: MaterialInterface
    DistanceToOpacityCurve: CurveFloat
    bSizeIsInScreenSpace: bool
    BaseSizeX: float
    BaseSizeY: float
    DistanceToSizeCurve: CurveFloat



class CustomInput:
    InputName: str
    Input: ExpressionInput



class FunctionExpressionOutput:
    ExpressionOutput: MaterialExpressionFunctionOutput
    ExpressionOutputId: core_uobject.Guid
    Output: ExpressionOutput



class FunctionExpressionInput:
    ExpressionInput: MaterialExpressionFunctionInput
    ExpressionInputId: core_uobject.Guid
    Input: ExpressionInput



class FontParameterValue:
    ParameterInfo: MaterialParameterInfo
    FontValue: Font
    FontPage: int
    ExpressionGUID: core_uobject.Guid



class MaterialParameterInfo:
    Name: str
    Association: int
    Index: int



class TextureParameterValue:
    ParameterInfo: MaterialParameterInfo
    ParameterValue: Texture
    ExpressionGUID: core_uobject.Guid



class VectorParameterValue:
    ParameterInfo: MaterialParameterInfo
    ParameterValue: core_uobject.LinearColor
    ExpressionGUID: core_uobject.Guid



class ScalarParameterValue:
    ParameterInfo: MaterialParameterInfo
    ParameterValue: float
    ExpressionGUID: core_uobject.Guid



class ScalarParameterAtlasInstanceData:
    bIsUsedAsAtlasPosition: bool



class MaterialInstanceBasePropertyOverrides:
    bOverride_OpacityMaskClipValue: bool
    bOverride_BlendMode: bool
    bOverride_ShadingModel: bool
    bOverride_DitheredLODTransition: bool
    bOverride_CastDynamicShadowAsMasked: bool
    bOverride_TwoSided: bool
    bOverride_DisableEdgeDetection: bool
    bOverride_ShouldDoOuterEdge: bool
    bOverride_IgnoreCustomMask: bool
    bOverride_IgnoreCustomGlow: bool
    bOverride_EnableWorldPositionOffset: bool
    bOverride_EnablePixelDepthOffset: bool
    bOverride_EnableRefraction: bool
    OpacityMaskClipValue: float
    BlendMode: int
    ShadingModel: int
    TwoSided: bool
    DitheredLODTransition: bool
    bCastDynamicShadowAsMasked: bool
    DisableEdgeDetection: bool
    bShouldDoOuterEdge: bool
    bIgnoreCustomMask: bool
    bIgnoreCustomGlow: bool
    bEnableWorldPositionOffset: bool
    bEnablePixelDepthOffset: bool
    bEnableRefraction: bool



class MaterialTextureInfo:
    SamplingScale: float
    UVChannelIndex: int
    TextureName: str



class LightmassMaterialInterfaceSettings:
    bCastShadowAsMasked: bool
    EmissiveBoost: float
    DiffuseBoost: float
    ExportResolutionScale: float
    bOverrideCastShadowAsMasked: bool
    bOverrideEmissiveBoost: bool
    bOverrideDiffuseBoost: bool
    bOverrideExportResolutionScale: bool



class MaterialLayersFunctions:
    Layers: unreal.WrappedArray[MaterialFunctionInterface]
    Blends: unreal.WrappedArray[MaterialFunctionInterface]
    LayerStates: unreal.WrappedArray[bool]
    KeyString: str



class SimplygonMaterialLODSettings:
    bActive: bool
    MaterialLODType: int
    bUseAutomaticSizes: bool
    TextureWidth: int
    TextureHeight: int
    SamplingQuality: int
    GutterSpace: int
    TextureStrech: int
    bReuseExistingCharts: bool
    ChannelsToCast: unreal.WrappedArray[SimplygonChannelCastingSettings]
    bBakeVertexData: bool
    bBakeActorData: bool
    bAllowMultiMaterial: bool
    bPreferTwoSideMaterials: bool
    bUseVertexWeights: bool
    OutputMaterialInfo: OutputMaterialInfo



class OutputMaterialInfo: ...


class SimplygonChannelCastingSettings:
    MaterialChannel: int
    Caster: int
    bActive: bool
    ColorChannels: int
    BitsPerChannel: int
    bUseSRGB: bool
    bBakeVertexColors: bool
    bFlipBackfacingNormals: bool
    bUseTangentSpaceNormals: bool
    bFlipGreenChannel: bool



class CollectionVectorParameter(CollectionParameterBase):
    DefaultValue: core_uobject.LinearColor



class CollectionScalarParameter(CollectionParameterBase):
    DefaultValue: float



class InterpGroupActorInfo:
    ObjectName: str
    Actors: unreal.WrappedArray[Actor]



class CameraCutInfo:
    Location: core_uobject.Vector
    Timestamp: float



class SimplygonRemeshingSettings:
    bActive: bool
    ScreenSize: int
    bRecalculateNormals: bool
    HardAngleThreshold: float
    MergeDistance: int
    bUseClippingPlane: bool
    ClippingLevel: float
    AxisIndex: int
    bPlaneNegativeHalfspace: bool
    bUseMassiveLOD: bool
    bUseAggregateLOD: bool
    MaterialLODSettings: SimplygonMaterialLODSettings



class MeshInstancingSettings:
    ActorClassToUse: unreal.UClass
    InstanceReplacementThreshold: int
    MeshReplacementMethod: EMeshInstancingReplacementMethod
    bSkipMeshesWithVertexColors: bool
    bUseHLODVolumes: bool



class MeshMergingSettings:
    bGenerateLightMapUV: bool
    TargetLightMapResolution: int
    bComputedLightMapResolution: bool
    bImportVertexColors: bool
    bPivotPointAtZero: bool
    bMergePhysicsData: bool
    bAssignLODGroup: bool
    LODGroupIndex: int
    bMergeMaterials: bool
    MaterialSettings: MaterialProxySettings
    bBakeVertexDataToMesh: bool
    bUseVertexDataForBakingMaterial: bool
    bUseTextureBinning: bool
    bReuseMeshLightmapUVs: bool
    bMergeEquivalentMaterials: bool
    OutputUVs: EUVOutput
    GutterSize: int
    bCalculateCorrectLODModel: bool
    LODSelectionType: EMeshLODSelectionType
    ExportSpecificLOD: int
    SpecificLOD: int
    bUseLandscapeCulling: bool
    bIncludeImposters: bool
    bAllowDistanceField: bool
    bExportNormalMap: bool
    bExportMetallicMap: bool
    bExportRoughnessMap: bool
    bExportSpecularMap: bool
    MergedMaterialAtlasResolution: int
    LODGroup: str



class MeshProxySettings:
    ScreenSize: int
    bOverrideVoxelSize: bool
    VoxelSize: float
    MaterialSettings: MaterialProxySettings
    TextureWidth: int
    TextureHeight: int
    bExportNormalMap: bool
    bExportMetallicMap: bool
    bExportRoughnessMap: bool
    bExportSpecularMap: bool
    bCalculateCorrectLODModel: bool
    MergeDistance: float
    UnresolvedGeometryColor: core_uobject.Color
    bOverrideTransferDistance: bool
    MaxRayCastDist: float
    bUseHardAngleThreshold: bool
    HardAngleThreshold: float
    NormalCalculationMethod: int
    LightMapResolution: int
    bComputeLightMapResolution: bool
    bRecalculateNormals: bool
    bBakeVertexData: bool
    bUseLandscapeCulling: bool
    LandscapeCullingPrecision: int
    bAllowAdjacency: bool
    bAllowDistanceField: bool
    bReuseMeshLightmapUVs: bool
    bCreateCollision: bool
    bAllowVertexColors: bool
    bGenerateLightmapUVs: bool
    bAssignLODGroup: bool
    LODGroupIndex: int
    bAggregateMeshes: bool
    AggregatorMode: EChartAggregationMode
    bUseCustomHemisphere: bool
    LODGroup: str



class MeshReductionSettings:
    BaseLODModel: int
    MetricToUse: EOptimizationMetric
    PercentTriangles: float
    ScreenSize: float
    MaxDeviation: float
    PixelError: float
    WeldingThreshold: float
    SilhouetteImportance: int
    TextureImportance: int
    ShadingImportance: int
    VertexColorImportance: int
    bRecalculateNormals: bool
    HardAngleThreshold: float
    bActive: bool
    bGenerateUniqueLightmapUVs: bool
    bKeepSymmetry: bool
    bVisibilityAided: bool
    bCullOccluded: bool
    VisibilityAggressiveness: int
    bUseVertexWeights: bool
    bSimplifyMaterials: bool
    MaterialLODSettings: SimplygonMaterialLODSettings
    MaterialProxySettings: MaterialProxySettings
    VertexWeightColorChannel: int



class PurchaseInfo:
    Identifier: str
    DisplayName: str
    DisplayDescription: str
    DisplayPrice: str



class NameCurve(IndexedCurve):
    Keys: unreal.WrappedArray[NameCurveKey]



class NameCurveKey:
    Time: float
    Value: str



class NavDataConfig(NavAgentProperties):
    Name: str
    Color: core_uobject.Color
    DefaultQueryExtent: core_uobject.Vector
    NavigationDataClass: unreal.UClass
    NavigationDataClassName: core_uobject.SoftClassPath



class NavAgentSelector:
    bSupportsAgent1: bool
    bSupportsAgent2: bool
    bSupportsAgent3: bool
    bSupportsAgent4: bool
    bSupportsAgent5: bool
    bSupportsAgent6: bool
    bSupportsAgent7: bool
    bSupportsAgent8: bool
    bSupportsAgent9: bool
    bSupportsAgent11: bool
    bSupportsAgent12: bool
    bSupportsAgent13: bool
    bSupportsAgent14: bool
    bSupportsAgent15: bool



class NavigationLinkBase:
    LeftProjectHeight: float
    MaxFallDownLength: float
    Direction: int
    SnapRadius: float
    SnapHeight: float
    SupportedAgents: NavAgentSelector
    bSupportsAgent1: bool
    bSupportsAgent2: bool
    bSupportsAgent3: bool
    bSupportsAgent4: bool
    bSupportsAgent5: bool
    bSupportsAgent6: bool
    bSupportsAgent7: bool
    bSupportsAgent8: bool
    bSupportsAgent9: bool
    bSupportsAgent11: bool
    bSupportsAgent12: bool
    bSupportsAgent13: bool
    bSupportsAgent14: bool
    bSupportsAgent15: bool
    bUseSnapHeight: bool
    bSnapToCheapestArea: bool
    bCustomFlag1: bool
    bCustomFlag2: bool
    bCustomFlag3: bool
    bCustomFlag4: bool
    bCustomFlag5: bool
    bCustomFlag6: bool
    bCustomFlag7: bool
    AreaClass: unreal.UClass



class NavigationSegmentLink(NavigationLinkBase):
    LeftStart: core_uobject.Vector
    LeftEnd: core_uobject.Vector
    RightStart: core_uobject.Vector
    RightEnd: core_uobject.Vector



class NavigationLink(NavigationLinkBase):
    Left: core_uobject.Vector
    Right: core_uobject.Vector



class PacketSimulationSettings:
    PktLoss: int
    PktOrder: int
    PktDup: int
    PktLag: int
    PktLagVariance: int



class NodeItem:
    ParentName: str
    Transform: core_uobject.Transform



class ObjectTag:
    Category: str
    Name: str



class ParticleBurst:
    Count: int
    CountLow: int
    Time: float



class ParticleRandomSeedInfo:
    ParameterName: str
    bGetSeedFromInstance: bool
    bInstanceSeedIsIndex: bool
    bResetSeedOnEmitterLooping: bool
    bRandomlySelectSeedArray: bool
    RandomSeeds: unreal.WrappedArray[int]



class ParticleCurvePair:
    CurveName: str
    CurveObject: unreal.UObject



class BeamModifierOptions:
    bModify: bool
    bScale: bool
    bLock: bool



class ParticleEvent_GenerateInfo:
    Type: int
    Frequency: int
    ParticleFrequency: int
    FirstTimeOnly: bool
    LastTimeOnly: bool
    UseReflectedImpactVector: bool
    bUseOrbitOffset: bool
    CustomName: str
    ParticleModuleEventsToSendToGame: unreal.WrappedArray[ParticleModuleEventSendToGame]



class LocationBoneSocketInfo:
    BoneSocketName: str
    Offset: core_uobject.Vector
    OffsetDistribution: RawDistributionVector



class OrbitOptions:
    bProcessDuringSpawn: bool
    bProcessDuringUpdate: bool
    bUseEmitterTime: bool



class EmitterDynamicParameter:
    ParamName: str
    bUseEmitterTime: bool
    bSpawnTimeOnly: bool
    ValueMethod: int
    bScaleVelocityByParamValue: bool
    ParamValue: RawDistributionFloat



class BeamTargetData:
    TargetName: str
    TargetPercentage: float



class GPUSpriteResourceData:
    QuantizedColorSamples: unreal.WrappedArray[core_uobject.Color]
    QuantizedMiscSamples: unreal.WrappedArray[core_uobject.Color]
    QuantizedSimulationAttrSamples: unreal.WrappedArray[core_uobject.Color]
    ColorScale: core_uobject.Vector4
    ColorBias: core_uobject.Vector4
    MiscScale: core_uobject.Vector4
    MiscBias: core_uobject.Vector4
    SimulationAttrCurveScale: core_uobject.Vector4
    SimulationAttrCurveBias: core_uobject.Vector4
    SubImageSize: core_uobject.Vector4
    SizeBySpeed: core_uobject.Vector4
    ConstantAcceleration: core_uobject.Vector
    OrbitOffsetBase: core_uobject.Vector
    OrbitOffsetRange: core_uobject.Vector
    OrbitFrequencyBase: core_uobject.Vector
    OrbitFrequencyRange: core_uobject.Vector
    OrbitPhaseBase: core_uobject.Vector
    OrbitPhaseRange: core_uobject.Vector
    GlobalVectorFieldScale: float
    GlobalVectorFieldTightness: float
    PerParticleVectorFieldScale: float
    PerParticleVectorFieldBias: float
    DragCoefficientScale: float
    DragCoefficientBias: float
    ResilienceScale: float
    ResilienceBias: float
    CollisionRadiusScale: float
    CollisionRadiusBias: float
    CollisionTimeBias: float
    CollisionRandomSpread: float
    CollisionRandomDistribution: float
    OneMinusFriction: float
    RotationRateScale: float
    CameraMotionBlurAmount: float
    ScreenAlignment: int
    LockAxisFlag: int
    PivotOffset: core_uobject.Vector2D
    bRemoveHMDRoll: bool
    MinFacingCameraBlendDistance: float
    MaxFacingCameraBlendDistance: float



class GPUSpriteEmitterInfo:
    RequiredModule: ParticleModuleRequired
    SpawnModule: ParticleModuleSpawn
    SpawnPerUnitModule: ParticleModuleSpawnPerUnit
    SpawnModules: unreal.WrappedArray[ParticleModule]
    LocalVectorField: GPUSpriteLocalVectorFieldInfo
    VectorFieldScale: FloatDistribution
    DragCoefficient: FloatDistribution
    PointAttractorStrength: FloatDistribution
    Resilience: FloatDistribution
    ConstantAcceleration: core_uobject.Vector
    PointAttractorPosition: core_uobject.Vector
    PointAttractorRadiusSq: float
    OrbitOffsetBase: core_uobject.Vector
    OrbitOffsetRange: core_uobject.Vector
    InvMaxSize: core_uobject.Vector2D
    InvRotationRateScale: float
    MaxLifetime: float
    MaxParticleCount: int
    ScreenAlignment: int
    LockAxisFlag: int
    bEnableCollision: bool
    CollisionMode: int
    bRemoveHMDRoll: bool
    MinFacingCameraBlendDistance: float
    MaxFacingCameraBlendDistance: float
    DynamicColor: RawDistributionVector
    DynamicAlpha: RawDistributionFloat
    DynamicColorScale: RawDistributionVector
    DynamicAlphaScale: RawDistributionFloat



class GPUSpriteLocalVectorFieldInfo:
    Field: VectorField
    Transform: core_uobject.Transform
    MinInitialRotation: core_uobject.Rotator
    MaxInitialRotation: core_uobject.Rotator
    RotationRate: core_uobject.Rotator
    Intensity: float
    Tightness: float
    bIgnoreComponentTransform: bool
    bTileX: bool
    bTileY: bool
    bTileZ: bool
    bUseFixDT: bool



class NoiseModifier:
    Values: RawDistributionVector
    bUniformSeed: bool
    TimeSource: NoiseTimeSource



class NamedEmitterMaterial:
    Name: str
    Material: MaterialInterface



class LODSoloTrack:
    SoloEnableSetting: unreal.WrappedArray[int]



class ParticleSystemLOD: ...


class ParticleSystemReplayFrame: ...


class ParticleEmitterReplayFrame: ...


class PhysicalAnimationData:
    BodyName: str
    bIsLocalSimulation: bool
    OrientationStrength: float
    AngularVelocityStrength: float
    PositionStrength: float
    VelocityStrength: float
    MaxLinearForce: float
    MaxAngularForce: float



class TireFrictionScalePair:
    TireType: TireType
    FrictionScale: float



class PhysicalAnimationProfile:
    ProfileName: str
    PhysicalAnimationData: PhysicalAnimationData



class PhysicsConstraintProfileHandle:
    ProfileProperties: ConstraintProfileProperties
    ProfileName: str



class PhysicalSurfaceName:
    Type: int
    Name: str



class DelegateArray: ...


class TViewTarget:
    Target: Actor
    POV: MinimalViewInfo
    PlayerState: PlayerState



class CameraCacheEntry:
    Timestamp: float
    POV: MinimalViewInfo



class InputAxisKeyMapping:
    AxisName: str
    Scale: float
    Key: input_core.Key



class InputActionKeyMapping:
    ActionName: str
    bShift: bool
    bCtrl: bool
    bAlt: bool
    bCmd: bool
    Key: input_core.Key



class InputAxisConfigEntry:
    AxisKeyName: str
    AxisProperties: InputAxisProperties



class InputAxisProperties:
    DeadZone: float
    Sensitivity: float
    Exponent: float
    bInvert: bool



class KeyBind:
    Key: input_core.Key
    Command: str
    Control: bool
    SHiFT: bool
    Alt: bool
    Cmd: bool
    bIgnoreCtrl: bool
    bIgnoreShift: bool
    bIgnoreAlt: bool
    bIgnoreCmd: bool
    bEditorOnly: bool
    bDisabled: bool



class PlayerMuteList:
    bHasVoiceHandshakeCompleted: bool
    VoiceChannelIdx: int



class PoseDataContainer:
    PoseNames: unreal.WrappedArray[SmartName]
    Poses: unreal.WrappedArray[PoseData]
    Tracks: unreal.WrappedArray[str]
    Curves: unreal.WrappedArray[AnimCurveBase]



class PoseData:
    LocalSpacePose: unreal.WrappedArray[core_uobject.Transform]
    LocalSpacePoseMask: unreal.WrappedArray[bool]
    CurveData: unreal.WrappedArray[float]



class PostProcessSettingsWithInheritance(PostProcessSettings):
    OverridePostProcessSettings: unreal.UClass
    bInheritanceWhiteBalance: bool
    bInheritanceColorGrading: bool
    bInheritanceColorGradingSMH: bool
    bInheritanceFilm: bool
    bInheritanceSceneColor: bool
    bInheritanceBloom: bool
    bInheritanceDirtMask: bool
    bInheritanceLightPropagationVolume: bool
    bInheritanceAmbientCubemap: bool
    bInheritanceAutoExposure: bool
    bInheritanceLensFlares: bool
    bInheritanceAmbientOcclusion: bool
    bInheritanceGlobalIllumination: bool
    bInheritanceDepthOfField: bool
    bInheritanceMotionBlur: bool
    bInheritanceScreenSpaceReflections: bool
    bInheritanceEdgeDetection: bool
    bInheritanceFWeightedBlendable: bool
    bInheritanceMisc: bool
    bInheritanceSkyEnvMap: bool
    bInheritanceAmbientOcclusionGBX: bool
    bInheritanceExponentialHeightFog: bool
    bInheritanceAtmosphericFog: bool



class PostProcessSettingsWithBlocker(PostProcessSettings):
    bBlockWhiteBalance: bool
    bBlockColorGrading: bool
    bBlockColorGradingSMH: bool
    bBlockFilm: bool
    bBlockSceneColor: bool
    bBlockBloom: bool
    bBlockDirtMask: bool
    bBlockLightPropagationVolume: bool
    bBlockAmbientCubemap: bool
    bBlockAutoExposure: bool
    bBlockLensFlares: bool
    bBlockAmbientOcclusion: bool
    bBlockGlobalIllumination: bool
    bBlockDepthOfField: bool
    bBlockMotionBlur: bool
    bBlockScreenSpaceReflections: bool
    bBlockEdgeDetection: bool
    bBlockFWeightedBlendable: bool
    bBlockMisc: bool
    bBlockSkyEnvMap: bool
    bBlockAmbientOcclusionGBX: bool
    bBlockExponentialHeightFog: bool
    bBlockAtmosphericFog: bool



class PreviewAssetAttachContainer:
    AttachedObjects: unreal.WrappedArray[PreviewAttachedObjectPair]



class PreviewAttachedObjectPair:
    Object: unreal.UObject
    AttachedTo: str



class PreviewMeshCollectionEntry: ...


class SpriteCategoryInfo:
    Category: str
    DisplayName: str
    Description: str



class ParsedProperty:
    ParsedPath: ParsedPropertyPathElement



class ParsedPropertyPathElement:
    PropertyName: str
    bUsesArrayIndex: bool
    ArrayIndex: int



class TransformBase:
    Node: str
    Constraints: TransformBaseConstraint



class TransformBaseConstraint:
    TransformConstraints: unreal.WrappedArray[RigTransformConstraint]



class RigTransformConstraint:
    TranformType: int
    ParentSpace: str
    Weight: float



class Node:
    Name: str
    ParentName: str
    Transform: core_uobject.Transform
    DisplayName: str
    bAdvanced: bool



class RootMotionSource:
    AccumulateMode: ERootMotionAccumulateMode
    InstanceName: str
    StartTime: float
    CurrentTime: float
    PreviousTime: float
    Duration: float
    Status: RootMotionSourceStatus
    Settings: RootMotionSourceSettings
    bInLocalSpace: bool
    RootMotionParams: RootMotionMovementParams
    FinishVelocityParams: RootMotionFinishVelocitySettings



class RootMotionFinishVelocitySettings:
    Mode: ERootMotionFinishVelocityMode
    SetVelocity: core_uobject.Vector
    ClampVelocity: float



class RootMotionSourceStatus:
    Flags: int



class RootMotionSource_JumpForce(RootMotionSource):
    Rotation: core_uobject.Rotator
    Distance: float
    Height: float
    bDisableTimeout: bool
    PathOffsetCurve: CurveVector
    TimeMappingCurve: CurveFloat



class RootMotionSource_MoveToDynamicForce(RootMotionSource):
    StartLocation: core_uobject.Vector
    InitialTargetLocation: core_uobject.Vector
    TargetLocation: core_uobject.Vector
    bRestrictSpeedToExpected: bool
    PathOffsetCurve: CurveVector
    TimeMappingCurve: CurveFloat



class RootMotionSource_MoveToForce(RootMotionSource):
    StartLocation: core_uobject.Vector
    TargetLocation: core_uobject.Vector
    bRestrictSpeedToExpected: bool
    PathOffsetCurve: CurveVector



class RootMotionSource_RadialForce(RootMotionSource):
    Location: core_uobject.Vector
    LocationActor: Actor
    Radius: float
    Strength: float
    bIsPush: bool
    bNoZForce: bool
    StrengthDistanceFalloff: CurveFloat
    StrengthOverTime: CurveFloat
    bUseFixedWorldDirection: bool
    FixedWorldDirection: core_uobject.Rotator



class RootMotionSource_ConstantForce(RootMotionSource):
    Force: core_uobject.Vector
    StrengthOverTime: CurveFloat



class CameraExposureSettings:
    Method: int
    LowPercent: float
    HighPercent: float
    MinBrightness: float
    MaxBrightness: float
    MinBrightnessHDR: float
    MaxBrightnessHDR: float
    SpeedUp: float
    SpeedDown: float
    Bias: float
    BiasHDR: float
    HistogramLogMin: float
    HistogramLogMax: float
    CalibrationConstant: float



class LensSettings:
    Bloom: LensBloomSettings
    Imperfections: LensImperfectionSettings
    ChromaticAberration: float



class LensImperfectionSettings:
    DirtMask: Texture
    DirtMaskIntensity: float
    DirtMaskTint: core_uobject.LinearColor



class LensBloomSettings:
    GaussianSum: GaussianSumBloomSettings
    Convolution: ConvolutionBloomSettings
    Method: int



class ConvolutionBloomSettings:
    Texture: Texture2D
    Size: float
    CenterUV: core_uobject.Vector2D
    PreFilterMin: float
    PreFilterMax: float
    PreFilterMult: float
    BufferScale: float



class GaussianSumBloomSettings:
    Intensity: float
    Threshold: float
    SizeScale: float
    Filter1Size: float
    Filter2Size: float
    Filter3Size: float
    Filter4Size: float
    Filter5Size: float
    Filter6Size: float
    Filter1Tint: core_uobject.LinearColor
    Filter2Tint: core_uobject.LinearColor
    Filter3Tint: core_uobject.LinearColor
    Filter4Tint: core_uobject.LinearColor
    Filter5Tint: core_uobject.LinearColor
    Filter6Tint: core_uobject.LinearColor



class FilmStockSettings:
    Slope: float
    Toe: float
    Shoulder: float
    BlackClip: float
    WhiteClip: float



class ColorGradingSettings:
    Global: ColorGradePerRangeSettings
    Shadows: ColorGradePerRangeSettings
    Midtones: ColorGradePerRangeSettings
    Highlights: ColorGradePerRangeSettings
    ShadowsMax: float
    HighlightsMin: float



class ColorGradePerRangeSettings:
    Saturation: core_uobject.Vector4
    Contrast: core_uobject.Vector4
    Gamma: core_uobject.Vector4
    Gain: core_uobject.Vector4
    Offset: core_uobject.Vector4



class EngineShowFlagsSetting:
    ShowFlagName: str
    Enabled: bool



class SingleAnimationPlayData:
    AnimToPlay: AnimationAsset
    bSavedLooping: bool
    bSavedPlaying: bool
    SavedPosition: float
    SavedPlayRate: float



class SkeletalMaterial:
    MaterialInterface: MaterialInterface
    bEnableShadowCasting: bool
    bRecomputeTangent: bool
    MaterialSlotName: str
    UVChannelData: MeshUVChannelInfo



class ClothingAssetData_Legacy:
    AssetName: str
    ApexFileName: str
    bClothPropertiesChanged: bool
    PhysicsProperties: ClothPhysicsProperties_Legacy



class ClothPhysicsProperties_Legacy:
    VerticalResistance: float
    HorizontalResistance: float
    BendResistance: float
    ShearResistance: float
    Friction: float
    Damping: float
    TetherStiffness: float
    TetherLimit: float
    Drag: float
    StiffnessFrequency: float
    GravityScale: float
    MassScale: float
    InertiaBlend: float
    SelfCollisionThickness: float
    SelfCollisionSquashScale: float
    SelfCollisionStiffness: float
    SolverFrequency: float
    FiberCompression: float
    FiberExpansion: float
    FiberResistance: float



class SkeletalMeshLODInfo:
    ScreenSize: PerPlatformFloat
    LODHysteresis: float
    LODMaterialMap: unreal.WrappedArray[int]
    bEnableShadowCasting: unreal.WrappedArray[bool]
    bAllowCPUAccess: bool
    bSupportUniformlyDistributedSampling: bool



class GroupedSkeletalOptimizationSettings:
    bAutoComputeLODDistance: bool
    LevelOfDetailType: ESkeletalMeshLODType
    ReductionSettings: SkeletalMeshOptimizationSettings
    ProxySettings: MeshProxySettings
    bForceLODRebuild: bool



class SkeletalMeshOptimizationSettings:
    ReductionMethod: int
    NumOfTrianglesPercentage: float
    MaxDeviationPercentage: float
    ScreenSize: int
    bRemapMorphTargets: bool
    SilhouetteImportance: int
    TextureImportance: int
    ShadingImportance: int
    SkinningImportance: int
    WeldingThreshold: float
    bRecalcNormals: bool
    BoneReductionRatio: float
    NormalsThreshold: float
    MaxBonesPerVertex: int
    BonesToRemove: unreal.WrappedArray[BoneReference]
    BaseLOD: int
    BakePose: AnimSequence
    LODChainLastIndex: int
    bUseVertexWeights: bool
    bUseVertexWeightsForMaterial: bool
    bSimplifyMaterials: bool
    MaterialLODSettings: SimplygonMaterialLODSettings
    MaterialSettings: MaterialProxySettings
    bForceRebuild: bool



class SkeletalMeshClothBuildParams:
    TargetAsset: clothing_system_runtime_interface.ClothingAssetBase
    TargetLod: int
    bRemapParameters: bool
    AssetName: str
    LODIndex: int
    SourceSection: int
    bRemoveFromMesh: bool



class BoneMirrorExport:
    BoneName: str
    SourceBoneName: str
    BoneFlipAxis: int



class BoneMirrorInfo:
    SourceIndex: int
    BoneFlipAxis: int



class SkeletalMeshComponentClothTickFunction(TickFunction): ...


class SkeletalMeshComponentEndPhysicsTickFunction(TickFunction): ...


class SkeletalMeshLODGroupSettings:
    ScreenSize: PerPlatformFloat
    LODHysteresis: float
    BoneFilterActionOption: EBoneFilterActionOption
    BoneList: unreal.WrappedArray[BoneFilter]
    ReductionSettings: SkeletalMeshOptimizationSettings



class BoneFilter:
    bExcludeSelf: bool
    BoneName: str



class SkeletalMeshSamplingInfo:
    Regions: unreal.WrappedArray[SkeletalMeshSamplingRegion]
    BuiltData: SkeletalMeshSamplingBuiltData



class SkeletalMeshSamplingBuiltData:
    WholeMeshBuiltData: unreal.WrappedArray[SkeletalMeshSamplingLODBuiltData]
    RegionBuiltData: unreal.WrappedArray[SkeletalMeshSamplingRegionBuiltData]



class SkeletalMeshSamplingRegionBuiltData: ...


class SkeletalMeshSamplingLODBuiltData: ...


class SkeletalMeshSamplingRegion:
    Name: str
    LODIndex: int
    bSupportUniformlyDistributedSampling: bool
    MaterialFilters: unreal.WrappedArray[SkeletalMeshSamplingRegionMaterialFilter]
    BoneFilters: unreal.WrappedArray[SkeletalMeshSamplingRegionBoneFilter]



class SkeletalMeshSamplingRegionBoneFilter:
    BoneName: str
    bIncludeOrExclude: bool
    bApplyToChildren: bool



class SkeletalMeshSamplingRegionMaterialFilter:
    MaterialName: str



class VirtualBone:
    SourceBoneName: str
    TargetBoneName: str
    VirtualBoneName: str



class AnimSlotGroup:
    GroupName: str
    SlotNames: unreal.WrappedArray[str]



class RigConfiguration:
    Rig: Rig
    BoneMappingTable: unreal.WrappedArray[NameMapping]



class NameMapping:
    NodeName: str
    BoneName: str



class BoneReductionSetting:
    BonesToRemove: unreal.WrappedArray[str]



class ReferencePose:
    PoseName: str
    ReferencePose: unreal.WrappedArray[core_uobject.Transform]



class BoneNode:
    Name: str
    ParentIndex: int
    TranslationRetargetingMode: int



class SkeletonToMeshLinkup:
    SkeletonToMeshTable: unreal.WrappedArray[int]
    MeshToSkeletonTable: unreal.WrappedArray[int]



class GestaltDataContainer:
    SkeletalMesh: SkeletalMesh
    LODModelData: unreal.WrappedArray[GestaltLODModel]
    SocketMappings: unreal.WrappedArray[SocketRemapEntry]
    PartNames: unreal.WrappedArray[str]
    SupportedClothAssets: unreal.WrappedArray[core_uobject.Guid]
    ReferencePoseBounds: core_uobject.BoxSphereBounds
    bUsingDefaultParts: bool



class SocketRemapEntry:
    MappedName: str
    UniqueSocketName: str



class GestaltLODModel:
    GestaltFragments: unreal.WrappedArray[GestaltLODModelFragment]



class GestaltLODModelFragment:
    MaterialIndex: int
    FirstIndex: int
    NumPrimitives: int



class SkelMeshComponentLODInfo:
    HiddenMaterials: unreal.WrappedArray[bool]



class SkelMeshSkinWeightInfo:
    Bones: int
    Weights: int



class SlotNodeBlendSpaceData: ...


class SlotNodeCameraData: ...


class SmartNameContainer: ...


class SmartNameMapping: ...


class CurveMetaData: ...


class AnimCurveType: ...


class SoundAttenuationSettings(BaseAttenuationSettings):
    bAttenuate: bool
    bSpatialize: bool
    bAttenuateWithLPF: bool
    bEnableListenerFocus: bool
    bEnableFocusInterpolation: bool
    bEnableOcclusion: bool
    bUseComplexCollisionForOcclusion: bool
    bEnableReverbSend: bool
    bApplyNormalizationToStereoSounds: bool
    bEnableLogFrequencyScaling: bool
    SpatializationAlgorithm: int
    AbsorptionMethod: EAirAbsorptionMethod
    OcclusionTraceChannel: int
    ReverbSendMethod: EReverbSendMethod
    OmniRadius: float
    StereoSpread: float
    LPFRadiusMin: float
    LPFRadiusMax: float
    CustomLowpassAirAbsorptionCurve: RuntimeFloatCurve
    CustomHighpassAirAbsorptionCurve: RuntimeFloatCurve
    LPFFrequencyAtMin: float
    LPFFrequencyAtMax: float
    HPFFrequencyAtMin: float
    HPFFrequencyAtMax: float
    FocusAzimuth: float
    NonFocusAzimuth: float
    FocusDistanceScale: float
    NonFocusDistanceScale: float
    FocusPriorityScale: float
    NonFocusPriorityScale: float
    FocusVolumeAttenuation: float
    NonFocusVolumeAttenuation: float
    FocusAttackInterpSpeed: float
    FocusReleaseInterpSpeed: float
    OcclusionLowPassFilterFrequency: float
    OcclusionVolumeAttenuation: float
    OcclusionInterpolationTime: float
    ReverbWetLevelMin: float
    ReverbWetLevelMax: float
    ReverbDistanceMin: float
    ReverbDistanceMax: float
    ManualReverbSendLevel: float
    CustomReverbSendCurve: RuntimeFloatCurve
    PluginSettings: SoundAttenuationPluginSettings



class SoundAttenuationPluginSettings:
    SpatializationPluginSettingsArray: unreal.WrappedArray[SpatializationPluginSourceSettingsBase]
    OcclusionPluginSettingsArray: unreal.WrappedArray[OcclusionPluginSourceSettingsBase]
    ReverbPluginSettingsArray: unreal.WrappedArray[ReverbPluginSourceSettingsBase]



class PassiveSoundMixModifier:
    SoundMix: SoundMix
    MinVolumeThreshold: float
    MaxVolumeThreshold: float



class SoundClassProperties:
    Volume: float
    Pitch: float
    StereoBleed: float
    LFEBleed: float
    VoiceCenterChannelVolume: float
    RadioFilterVolume: float
    RadioFilterVolumeThreshold: float
    bApplyEffects: bool
    bAlwaysPlay: bool
    bIsUISound: bool
    bIsMusic: bool
    bReverb: bool
    Default2DReverbSendAmount: float
    bCenterChannelOnly: bool
    bApplyAmbientVolumes: bool
    OutputTarget: int



class SoundClassEditorData: ...


class SoundConcurrencySettings:
    MaxCount: int
    bLimitToOwner: bool
    ResolutionRule: int
    VolumeScale: float



class SoundNodeEditorData: ...


class SourceEffectChainEntry:
    Preset: SoundEffectSourcePreset
    bBypass: bool



class SoundGroup:
    SoundGroup: int
    DisplayName: str
    bAlwaysDecompressOnLoad: bool
    DecompressedDuration: float



class SoundClassAdjuster:
    SoundClassObject: SoundClass
    VolumeAdjuster: float
    PitchAdjuster: float
    bApplyToChildren: bool
    VoiceCenterChannelVolumeAdjuster: float



class AudioEQEffect:
    FrequencyCenter1: float
    Gain1: float
    Bandwidth1: float
    FrequencyCenter2: float
    Gain2: float
    Bandwidth2: float
    FrequencyCenter3: float
    Gain3: float
    Bandwidth3: float



class DistanceDatum:
    FadeInDistanceStart: float
    FadeInDistanceEnd: float
    FadeOutDistanceStart: float
    FadeOutDistanceEnd: float
    Volume: float



class ModulatorContinuousParams:
    ParameterName: str
    Default: float
    MinInput: float
    MaxInput: float
    MinOutput: float
    MaxOutput: float
    ParamMode: int



class SoundSourceBusSendInfo:
    SendLevel: float
    SoundSourceBus: SoundSourceBus



class SoundSubmixSendInfo:
    SendLevel: float
    SoundSubmix: SoundSubmix



class StreamedAudioPlatformData: ...


class EditorMarker:
    Distance: float
    Label: str
    Color: core_uobject.Color



class SplinePoint:
    InputKey: float
    Position: core_uobject.Vector
    ArriveTangent: core_uobject.Vector
    LeaveTangent: core_uobject.Vector
    Rotation: core_uobject.Rotator
    Scale: core_uobject.Vector
    Type: int



class SplineMeshParams:
    StartPos: core_uobject.Vector
    StartTangent: core_uobject.Vector
    StartScale: core_uobject.Vector2D
    StartRoll: float
    StartOffset: core_uobject.Vector2D
    EndPos: core_uobject.Vector
    EndTangent: core_uobject.Vector
    EndScale: core_uobject.Vector2D
    EndRoll: float
    EndOffset: core_uobject.Vector2D



class MaterialRemapIndex:
    MaterialRemap: unreal.WrappedArray[int]



class StaticMaterial:
    MaterialInterface: MaterialInterface
    MaterialSlotName: str
    ImportedMaterialSlotName: str
    UVChannelData: MeshUVChannelInfo



class AssetEditorOrbitCameraPosition:
    bIsSet: bool
    CamOrbitPoint: core_uobject.Vector
    CamOrbitZoom: core_uobject.Vector
    CamOrbitRotation: core_uobject.Rotator



class MeshSectionInfoMap: ...


class MeshSectionInfo:
    MaterialIndex: int
    bEnableCollision: bool
    bCastShadow: bool



class StaticMeshSourceModel:
    BuildSettings: MeshBuildSettings
    ReductionSettings: MeshReductionSettings
    RemeshingSettings: SimplygonRemeshingSettings
    bHasBeenSimplified: bool
    OptimizationSettings: GroupedStaticMeshOptimizationSettings
    LODDistance: float
    ScreenSize: PerPlatformFloat
    SourceImportFilename: str
    PerLODPlatformSettings: PerLODPlatformSettings



class PerLODPlatformSettings:
    bEnableOnXbox: bool
    bEnableOnPS4: bool
    bEnableOnPC_HighDetail: bool
    bEnableOnPC_LowDetail: bool



class GroupedStaticMeshOptimizationSettings:
    LevelOfDetailType: EStaticMeshLODType
    ReductionSettings: MeshReductionSettings
    ProxySettings: MeshProxySettings



class StaticMeshOptimizationSettings:
    ReductionMethod: int
    NumOfTrianglesPercentage: float
    MaxDeviationPercentage: float
    WeldingThreshold: float
    bRecalcNormals: bool
    NormalsThreshold: float
    SilhouetteImportance: int
    TextureImportance: int
    ShadingImportance: int



class StaticMeshComponentLODInfo:
    PaintedVertices: unreal.WrappedArray[PaintedVertex]



class PaintedVertex:
    Position: core_uobject.Vector
    Normal: core_uobject.Vector4
    Color: core_uobject.Color



class StaticParameterSet:
    StaticSwitchParameters: unreal.WrappedArray[StaticSwitchParameter]
    StaticComponentMaskParameters: unreal.WrappedArray[StaticComponentMaskParameter]
    TerrainLayerWeightParameters: unreal.WrappedArray[StaticTerrainLayerWeightParameter]
    MaterialLayersParameters: unreal.WrappedArray[StaticMaterialLayersParameter]



class StaticMaterialLayersParameter:
    ParameterInfo: MaterialParameterInfo
    Value: MaterialLayersFunctions
    bOverride: bool
    ExpressionGUID: core_uobject.Guid



class StaticTerrainLayerWeightParameter:
    ParameterInfo: MaterialParameterInfo
    bOverride: bool
    ExpressionGUID: core_uobject.Guid
    WeightmapIndex: int
    bWeightBasedBlend: bool



class StaticComponentMaskParameter:
    ParameterInfo: MaterialParameterInfo
    R: bool
    G: bool
    B: bool
    A: bool
    bOverride: bool
    ExpressionGUID: core_uobject.Guid



class StaticSwitchParameter:
    ParameterInfo: MaterialParameterInfo
    Value: bool
    bOverride: bool
    ExpressionGUID: core_uobject.Guid



class StreamingLevelRemapData:
    OldLevelPath: str
    NewLevelPath: str



class StringCurve(IndexedCurve):
    DefaultValue: str
    Keys: unreal.WrappedArray[StringCurveKey]



class StringCurveKey:
    Time: float
    Value: str



class SubsurfaceProfileStruct:
    ScatterRadius: float
    SubsurfaceColor: core_uobject.LinearColor
    FalloffColor: core_uobject.LinearColor
    BoundaryColorBleed: core_uobject.LinearColor
    ExtinctionScale: float
    NormalScale: float
    ScatteringDistribution: float
    IOR: float
    Roughness1: float
    LobeMix: float



class TexturePlatformData: ...


class TextureSource: ...


class TextureLODGroup:
    Group: int
    LODBias: int
    LODBias_Smaller: int
    LODBias_Smallest: int
    NumStreamedMips: int
    MipGenSettings: int
    MinLODSize: int
    MaxLODSize: int
    MaxLODSize_Smaller: int
    MaxLODSize_Smallest: int
    OptionalLODBias: int
    OptionalMaxLODSize: int
    MinMagFilter: str
    MipFilter: str



class TextureLODStreamingSettings:
    BoostFactor: float
    FOVBoostFactor: float
    RetentionPriority: int
    LoadOrderPriority: int
    IsCharacterTexture: int



class StreamingTextureBuildInfo:
    TextureLevelIndex: int
    TexelFactor: float



class StreamingTexturePrimitiveInfo:
    Texture: TextureStreaming
    Bounds: core_uobject.BoxSphereBounds
    TexelFactor: float



class Timeline:
    LengthMode: int
    bLooping: bool
    bReversePlayback: bool
    bPlaying: bool
    Length: float
    PlayRate: float
    Position: float
    Events: unreal.WrappedArray[TimelineEventEntry]
    InterpVectors: unreal.WrappedArray[TimelineVectorTrack]
    InterpFloats: unreal.WrappedArray[TimelineFloatTrack]
    InterpLinearColors: unreal.WrappedArray[TimelineLinearColorTrack]
    PropertySetObject: unreal.UObject
    DirectionPropertyName: str
    DirectionProperty: core_uobject.Property



class TimelineLinearColorTrack:
    LinearColorCurve: CurveLinearColor
    TrackName: str
    LinearColorPropertyName: str
    LinearColorProperty: core_uobject.StructProperty



class TimelineFloatTrack:
    FloatCurve: CurveFloat
    TrackName: str
    FloatPropertyName: str
    FloatProperty: core_uobject.FloatProperty



class TimelineVectorTrack:
    VectorCurve: CurveVector
    TrackName: str
    VectorPropertyName: str
    VectorProperty: core_uobject.StructProperty



class TimelineEventEntry:
    Time: float



class TTTrackBase:
    TrackName: str
    bIsExternalCurve: bool



class TTLinearColorTrack(TTTrackBase):
    CurveLinearColor: CurveLinearColor



class TTVectorTrack(TTTrackBase):
    CurveVector: CurveVector



class TTFloatTrack(TTTrackBase):
    CurveFloat: CurveFloat



class TTEventTrack(TTTrackBase):
    CurveKeys: CurveFloat



class TimeStretchCurveInstance:
    bHasValidData: bool



class TimeStretchCurve:
    SamplingRate: float
    CurveValueMinPrecision: float
    Markers: unreal.WrappedArray[TimeStretchCurveMarker]
    Sum_dT_i_by_C_i: float



class TimeStretchCurveMarker:
    Time: float
    Alpha: float



class TouchInputControl:
    Image1: Texture2D
    Image2: Texture2D
    Center: core_uobject.Vector2D
    VisualSize: core_uobject.Vector2D
    ThumbSize: core_uobject.Vector2D
    InteractionSize: core_uobject.Vector2D
    InputScale: core_uobject.Vector2D
    MainInputKey: input_core.Key
    AltInputKey: input_core.Key



class TrajectoryParams:
    Speed: float
    Error: float
    TargetOffset: core_uobject.Vector
    PredictDistMax: float
    Angle: float



class Trajectory:
    StartLoc: core_uobject.Vector
    Velocity: core_uobject.Vector
    GravityZ: float
    Time: float



class HardwareCursorReference:
    CursorPath: str
    HotSpot: core_uobject.Vector2D



class VoiceSettings:
    ComponentToAttachTo: SceneComponent
    AttenuationSettings: SoundAttenuation
    SourceEffectChain: SoundEffectSourcePresetChain



class LevelCollection:
    GameState: GameStateBase
    NetDriver: NetDriver
    DemoNetDriver: DemoNetDriver
    PersistentLevel: Level



class StartAsyncSimulationFunction(TickFunction): ...


class EndPhysicsTickFunction(TickFunction): ...


class StartPhysicsTickFunction(TickFunction): ...


class LevelViewportInfo:
    CamPosition: core_uobject.Vector
    CamRotation: core_uobject.Rotator
    CamOrthoZoom: float
    CamUpdated: bool



class WorldPSCPool: ...


class PSCPool:
    FreeElements: unreal.WrappedArray[PSCPoolElem]
    InUseComponents_Auto: unreal.WrappedArray[ParticleSystemComponent]
    InUseComponents_Manual: unreal.WrappedArray[ParticleSystemComponent]



class PSCPoolElem:
    PSC: ParticleSystemComponent



class BroadphaseSettings:
    bUseMBPOnClient: bool
    bUseMBPOnServer: bool
    MBPBounds: core_uobject.Box



class HierarchicalSimplification:
    TransitionScreenSize: float
    OverrideDrawDistance: float
    bUseOverrideDrawDistance: bool
    bAllowSpecificExclusion: bool
    bSimplifyMesh: bool
    bFarShadowCastersOnly: bool
    ProxySetting: MeshProxySettings
    MergeSetting: MeshMergingSettings
    DesiredBoundRadius: float
    DesiredFillingPercentage: float
    MinNumberOfActorsToBuild: int
    bOnlyGenerateClustersForVolumes: bool
    bReusePreviousLevelClusters: bool



class NetViewer:
    Connection: NetConnection
    InViewer: Actor
    ViewTarget: Actor
    ViewLocation: core_uobject.Vector
    ViewDir: core_uobject.Vector



class LightmassWorldInfoSettings:
    StaticLightingLevelScale: float
    NumIndirectLightingBounces: int
    NumSkyLightingBounces: int
    IndirectLightingQuality: float
    IndirectLightingSmoothness: float
    EnvironmentColor: core_uobject.Color
    EnvironmentIntensity: float
    EmissiveBoost: float
    DiffuseBoost: float
    VolumeLightingMethod: int
    VolumetricLightmapDetailCellSize: float
    VolumetricLightmapMaximumBrickMemoryMb: float
    VolumetricLightmapMaximumIndirectionMemoryMb: float
    VolumetricLightmapSphericalHarmonicSmoothing: float
    VolumeLightSamplePlacementScale: float
    bUseAmbientOcclusion: bool
    bGenerateAmbientOcclusionMaterialMask: bool
    DirectIlluminationOcclusionFraction: float
    IndirectIlluminationOcclusionFraction: float
    OcclusionExponent: float
    FullyOccludedSamplesFraction: float
    MaxOcclusionDistance: float
    bVisualizeMaterialDiffuse: bool
    bVisualizeAmbientOcclusion: bool
    bCompressLightmaps: bool



class Default__BlueprintGeneratedClass: ...


class Default__AnimBlueprintGeneratedClass: ...


class Default__UserDefinedStruct: ...


class ETextGender(enum.Enum):
    Neuter = 0
    Feminine = 1


class EFormatArgumentType(enum.Enum):
    Text = 0
    UInt = 1
    Float = 2


class EEndPlayReason(enum.Enum):
    LevelTransition = 0
    Quit = 1
    EndPlayInEditor = 2


class ENetRole(enum.Enum):
    ROLE_MAX = 0
    ROLE_SimulatedProxy = 1
    ROLE_AutonomousProxy = 2


class EAttachLocation(enum.Enum):
    EAttachLocation_MAX = 0
    KeepWorldPosition = 1
    SnapToTarget = 2


class EAttachmentRule(enum.Enum):
    KeepWorld = 0
    SnapToTarget = 1


class EDetachmentRule(enum.Enum):
    EDetachmentRule_MAX = 0
    KeepWorld = 1


class ENetDormancy(enum.Enum):
    DORM_Awake = 0
    DORM_DormantAll = 1
    DORM_Initial = 2


class ETickingGroup(enum.Enum):
    TG_StartPhysics = 0
    TG_PostPhysics = 1
    TG_DuringPhysics = 2
    TG_MAX = 3


class EAutoReceiveInput(enum.Enum):
    Player0 = 0
    Player1 = 1
    Player3 = 2
    Player7 = 3


class ESpawnActorCollisionHandlingMethod(enum.Enum):
    DontSpawnIfColliding = 0
    AdjustIfPossibleButAlwaysSpawn = 1
    AlwaysSpawn = 2


class ERotatorQuantization(enum.Enum):
    ShortComponents = 0
    ERotatorQuantization_MAX = 1


class EVectorQuantization(enum.Enum):
    RoundTwoDecimals = 0
    RoundOneDecimal = 1


class EComponentCreationMethod(enum.Enum):
    EComponentCreationMethod_MAX = 0
    SimpleConstructionScript = 1
    UserConstructionScript = 2


class ETemperatureSeverityType(enum.Enum):
    Critical = 0
    Bad = 1
    Good = 2


class EPlaneConstraintAxisSetting(enum.Enum):
    X = 0
    UseGlobalPhysicsSetting = 1
    Y = 2


class EInterpToBehaviourType(enum.Enum):
    OneShot_Reverse = 0
    EInterpToBehaviourType_MAX = 1
    Loop_Reset = 2


class EPlatformInterfaceDataType(enum.Enum):
    PIDT_Int = 0
    PIDT_Float = 1
    PIDT_Object = 2


class EMovementMode(enum.Enum):
    MOVE_Swimming = 0
    MOVE_Walking = 1
    MOVE_NavWalking = 2


class ENetworkFailure(enum.Enum):
    NetDriverCreateFailure = 0
    NetDriverListenFailure = 1
    ConnectionTimeout = 2
    PendingConnectionFailure = 3


class ETravelFailure(enum.Enum):
    InvalidURL = 0
    LoadMapFailure = 1
    PackageVersion = 2
    PendingNetGameCreateFailure = 3


class EScreenOrientation(enum.Enum):
    Portrait = 0
    LandscapeRight = 1
    PortraitUpsideDown = 2


class EApplicationState(enum.Enum):
    Inactive = 0
    Background = 1
    EApplicationState_MAX = 2


class EObjectTypeQuery(enum.Enum):
    ObjectTypeQuery2 = 0
    ObjectTypeQuery3 = 1
    ObjectTypeQuery5 = 2
    ObjectTypeQuery9 = 3
    ObjectTypeQuery_MAX = 4
    ObjectTypeQuery17 = 5


class EDrawDebugTrace(enum.Enum):
    EDrawDebugTrace_MAX = 0
    ForOneFrame = 1
    ForDuration = 2


class ETraceTypeQuery(enum.Enum):
    TraceTypeQuery2 = 0
    TraceTypeQuery3 = 1
    TraceTypeQuery5 = 2
    TraceTypeQuery9 = 3
    TraceTypeQuery17 = 4
    TraceTypeQuery_MAX = 5


class EMoveComponentAction(enum.Enum):
    Stop = 0
    Return = 1


class EQuitPreference(enum.Enum):
    Background = 0
    EQuitPreference_MAX = 1


class ENetworkSmoothingMode(enum.Enum):
    Exponential = 0
    Linear = 1
    ENetworkSmoothingMode_MAX = 2


class EEasingFunc(enum.Enum):
    SinusoidalInOut = 0
    Step = 1
    SinusoidalIn = 2
    ExpoIn = 3


class ERichCurveTangentWeightMode(enum.Enum):
    RCTWM_WeightedArrive = 0
    RCTWM_WeightedLeave = 1
    RCTWM_MAX = 2


class ERichCurveTangentMode(enum.Enum):
    RCTM_User = 0
    RCTM_Break = 1
    RCTM_MAX = 2


class ERichCurveInterpMode(enum.Enum):
    RCIM_Cubic = 0
    RCIM_Constant = 1
    RCIM_MAX = 2


class ERichCurveExtrapolation(enum.Enum):
    RCCE_Oscillate = 0
    RCCE_CycleWithOffset = 1
    RCCE_Constant = 2


class ECameraAnimPlaySpace(enum.Enum):
    UserDefined = 0
    World = 1


class ERadialBlurPreset(enum.Enum):
    RadialBlur_Large = 0
    RadialBlur_Medium = 1
    RadialBlur_None = 2


class EViewTargetBlendFunction(enum.Enum):
    VTBlend_EaseInOut = 0
    VTBlend_Cubic = 1
    VTBlend_EaseIn = 2


class ETravelType(enum.Enum):
    TRAVEL_Partial = 0
    TRAVEL_Relative = 1


class ECollisionChannel(enum.Enum):
    ECC_WorldDynamic = 0
    ECC_Pawn = 1
    ECC_Camera = 2
    ECC_EngineTraceChannel1 = 3
    ECC_GameTraceChannel3 = 4
    ECC_OverlapAll_Deprecated = 5


class EControllerAnalogStick(enum.Enum):
    CAS_RightStick = 0
    CAS_MAX = 1


class EDynamicForceFeedbackAction(enum.Enum):
    Update = 0
    Stop = 1


class EDepthOfFieldMethod(enum.Enum):
    DOFM_Gaussian = 0
    DOFM_CircleDOF = 1


class EAutoExposureMethod(enum.Enum):
    AEM_Basic = 0
    AEM_Manual = 1


class EBloomMethod(enum.Enum):
    BM_FFT = 0
    BM_MAX = 1


class EParticleSysParamType(enum.Enum):
    PSPT_Scalar = 0
    PSPT_ScalarRand = 1
    PSPT_VectorRand = 2
    PSPT_MAX = 3


class EAutoPossessAI(enum.Enum):
    PlacedInWorld = 0
    Spawned = 1
    EAutoPossessAI_MAX = 2


class ECollisionResponse(enum.Enum):
    ECR_Overlap = 0
    ECR_Block = 1


class EBlendMode(enum.Enum):
    BLEND_Modulate = 0
    BLEND_Masked = 1
    BLEND_Translucent = 2


class EMouseLockMode(enum.Enum):
    LockOnCapture = 0
    LockAlways = 1


class EWindowTitleBarMode(enum.Enum):
    VerticalBox = 0
    EWindowTitleBarMode_MAX = 1


class EInputEvent(enum.Enum):
    IE_Released = 0
    IE_Repeat = 1
    IE_Axis = 2


class ERelativeTransformSpace(enum.Enum):
    RTS_Actor = 0
    RTS_Component = 1
    RTS_MAX = 2


class EDetailMode(enum.Enum):
    DM_Medium = 0
    DM_High = 1


class EComponentMobility(enum.Enum):
    Stationary = 0
    Movable = 1


class ERadialImpulseFalloff(enum.Enum):
    RIF_Linear = 0
    RIF_MAX = 1


class ECollisionEnabled(enum.Enum):
    QueryOnly = 0
    ECollisionEnabled_MAX = 1
    PhysicsOnly = 2


class EWalkableSlopeBehavior(enum.Enum):
    WalkableSlope_Increase = 0
    WalkableSlope_Decrease = 1
    WalkableSlope_Max = 2


class EDOFMode(enum.Enum):
    SixDOF = 0
    XYPlane = 1
    YZPlane = 2


class ERendererStencilMask(enum.Enum):
    ERSM_255 = 0
    ERSM_4 = 1
    ERSM_1 = 2
    ERSM_64 = 3


class EGbxViewFlagAction(enum.Enum):
    Add = 0
    Remove = 1


class EHavokNavMobility(enum.Enum):
    Static = 0
    Movable = 1


class EHavokNavGeometryUsage(enum.Enum):
    None_ = 0
    WalkableSurface = 1
    StaticPaintingVolume = 2


class EHavokNavGeometrySource(enum.Enum):
    SingleConvex = 0
    BoundingBox = 1


class EHavokNavPresets(enum.Enum):
    Block = 0
    Ignore = 1
    EHavokNavPresets_MAX = 2


class ESleepFamily(enum.Enum):
    Sensitive = 0
    Custom = 1


class ECanBeCharacterBase(enum.Enum):
    ECB_Owner = 0
    ECB_Yes = 1


class EHasCustomNavigableGeometry(enum.Enum):
    Yes = 0
    EvenIfNotCollidable = 1
    EHasCustomNavigableGeometry_MAX = 2


class ELightmapType(enum.Enum):
    ForceSurface = 0
    ForceVolumetric = 1


class EIndirectLightingCacheQuality(enum.Enum):
    ILCQ_Point = 0
    ILCQ_Volume = 1


class ESceneDepthPriorityGroup(enum.Enum):
    SDPG_Foreground = 0
    SDPG_MAX = 1


class EAngularDriveMode(enum.Enum):
    TwistAndSwing = 0
    EAngularDriveMode_MAX = 1


class EAngularConstraintMotion(enum.Enum):
    ACM_Locked = 0
    ACM_Limited = 1


class EConstraintFrame(enum.Enum):
    EConstraintFrame_MAX = 0
    Frame2 = 1


class ELinearConstraintMotion(enum.Enum):
    LCM_Locked = 0
    LCM_Limited = 1


class EAlphaBlendOption(enum.Enum):
    Cubic = 0
    HermiteCubic = 1
    QuadraticInOut = 2
    CircularIn = 3


class EAnimGroupRole(enum.Enum):
    AlwaysFollower = 0
    AlwaysLeader = 1
    TransitionFollower = 2


class ERawCurveTrackTypes(enum.Enum):
    RCT_Vector = 0
    RCT_Transform = 1
    RCT_MAX = 2


class EAnimAssetCurveFlags(enum.Enum):
    AACF_DriveTrack = 0
    AACF_DriveMaterial_DEPRECATED = 1
    AACF_DriveMorphTarget_DEPRECATED = 2
    AACF_DriveAttribute_DEPRECATED = 3
    AACF_Disabled = 4
    AACF_Editable = 5
    AACF_Metadata = 6


class AnimationCompressionFormat(enum.Enum):
    ACF_Fixed48NoW = 0
    ACF_Float96NoW = 1
    ACF_Fixed32NoW = 2


class EAdditiveBasePoseType(enum.Enum):
    ABPT_RefPose = 0
    ABPT_AnimScaled = 1
    ABPT_MAX = 2


class ERootMotionMode(enum.Enum):
    IgnoreRootMotion = 0
    RootMotionFromEverything = 1
    ERootMotionMode_MAX = 2


class ERootMotionRootLock(enum.Enum):
    AnimFirstFrame = 0
    Zero = 1


class EMontagePlayReturnType(enum.Enum):
    Duration = 0
    EMontagePlayReturnType_MAX = 1


class EAnimCurveType(enum.Enum):
    MorphTargetCurve = 0
    MaterialCurve = 1
    EAnimCurveType_MAX = 2


class EDrawDebugItemType(enum.Enum):
    Sphere = 0
    Line = 1
    CoordinateSystem = 2


class EAnimLinkMethod(enum.Enum):
    Relative = 0
    Proportional = 1


class EMontageSubStepResult(enum.Enum):
    NotMoved = 0
    InvalidSection = 1
    EMontageSubStepResult_MAX = 2


class EAnimNotifyEventType(enum.Enum):
    End = 0
    EAnimNotifyEventType_MAX = 1


class EEvaluatorMode(enum.Enum):
    EM_DelayedFreeze = 0
    EM_Freeze = 1


class EEvaluatorDataSource(enum.Enum):
    EDS_DestinationPose = 0
    EDS_MAX = 1


class ECopyType(enum.Enum):
    BoolProperty = 0
    StructProperty = 1
    BoolPropertyToBoolArray = 2


class EPostCopyOperation(enum.Enum):
    LogicalNegateBool = 0
    AbsoluteValueFloat = 1


class EPinHidingMode(enum.Enum):
    PinHiddenByDefault = 0
    PinShownByDefault = 1
    EPinHidingMode_MAX = 2


class EAnimNotifyEndReason(enum.Enum):
    Aborted = 0
    MontageInterrupted = 1
    LowBlendWeight = 2


class AnimPhysCollisionType(enum.Enum):
    CustomSphere = 0
    InnerSphere = 1
    AnimPhysCollisionType_MAX = 2


class AnimPhysTwistAxis(enum.Enum):
    AxisY = 0
    AxisZ = 1


class AnimationKeyFormat(enum.Enum):
    AKF_VariableKeyLerp = 0
    AKF_PerTrackCompression = 1


class ETypeAdvanceAnim(enum.Enum):
    ETAA_Finished = 0
    ETAA_Looped = 1


class ERootMotionBlendType(enum.Enum):
    Target = 0
    Source = 1


class EBlendStartTime(enum.Enum):
    BST_End = 0
    BST_AnimMarker = 1


class ETransitionLogicType(enum.Enum):
    TLT_Custom = 0
    TLT_MAX = 1


class ETransitionBlendMode(enum.Enum):
    TBM_MAX = 0
    TBM_Cubic = 1


class EComponentType(enum.Enum):
    TranslationX = 0
    TranslationY = 1
    RotationX = 2
    ScaleX = 3


class EAxisOption(enum.Enum):
    Y = 0
    Y_Neg = 1
    Z = 2


class EAnimInterpolationType(enum.Enum):
    EAnimInterpolationType_MAX = 0
    Step = 1


class ECurveBlendOption(enum.Enum):
    NormalizeByWeight = 0
    BlendByWeight = 1


class EAdditiveAnimationType(enum.Enum):
    AAT_RotationOffsetMeshSpace = 0
    AAT_LocalSpaceBase = 1


class FAnimNotifyTrackLockState(enum.Enum):
    Unlocked = 0
    GeneratedOnly = 1


class ENotifyFilterType(enum.Enum):
    LOD = 0
    ENotifyFilterType_MAX = 1


class EMontageNotifyTickType(enum.Enum):
    EMontageNotifyTickType_MAX = 0
    BranchingPoint = 1


class EBoneRotationSource(enum.Enum):
    BRS_KeepLocalSpaceRotation = 0
    BRS_CopyFromTarget = 1


class EBoneControlSpace(enum.Enum):
    BCS_ComponentSpace = 0
    BCS_ParentBoneSpace = 1
    BCS_MAX = 2


class EBoneAxis(enum.Enum):
    BA_Y = 0
    BA_Z = 1


class EPrimaryAssetCookRule(enum.Enum):
    NeverCook = 0
    DevelopmentCook = 1
    AlwaysCook = 2


class EAttenuationShape(enum.Enum):
    EAttenuationShape_MAX = 0
    Capsule = 1
    Box = 2


class EAttenuationDistanceModel(enum.Enum):
    Logarithmic = 0
    Inverse = 1
    NaturalSound = 2


class EMonoChannelUpmixMethod(enum.Enum):
    EqualPower = 0
    FullVolume = 1


class EPanningMethod(enum.Enum):
    EqualPower = 0
    EPanningMethod_MAX = 1


class EVoiceSampleRate(enum.Enum): ...


class ReverbPreset(enum.Enum):
    REVERB_StoneRoom = 0
    REVERB_Bathroom = 1
    REVERB_ConcertHall = 2
    REVERB_Alley = 3
    REVERB_Underwater = 4


class EBlendableLocation(enum.Enum):
    BL_BeforeTonemapping = 0
    BL_BeforeTranslucency = 1
    BL_BeforeFog = 2


class ENotifyTriggerMode(enum.Enum):
    None_ = 0
    HighestWeightedAnimation = 1


class EBlendSpaceAxis(enum.Enum):
    BSA_X = 0
    BSA_Y = 1


class EBlueprintNativizationFlag(enum.Enum):
    Dependency = 0
    ExplicitlyEnabled = 1


class EBlueprintCompileMode(enum.Enum):
    Development = 0
    FinalRelease = 1


class EBlueprintType(enum.Enum):
    BPTYPE_Const = 0
    BPTYPE_MacroLibrary = 1
    BPTYPE_LevelScript = 2


class EBlueprintStatus(enum.Enum):
    BS_Error = 0
    BS_Dirty = 1
    BS_BeingCreated = 2


class EDynamicActorScene(enum.Enum):
    UseSyncScene = 0
    UseAsyncScene = 1


class EBodyCollisionResponse(enum.Enum):
    BodyCollision_Disabled = 0
    BodyCollision_MAX = 1


class EPhysicsType(enum.Enum):
    PhysType_Kinematic = 0
    PhysType_Simulated = 1


class ECollisionTraceFlag(enum.Enum):
    CTF_MAX = 0
    CTF_UseSimpleAndComplex = 1
    CTF_UseSimpleAsComplex = 2


class EBrushType(enum.Enum):
    Brush_Add = 0
    Brush_Subtract = 1


class ECsgOper(enum.Enum):
    CSG_Add = 0
    CSG_Subtract = 1
    CSG_Deintersect = 2


class EInitialOscillatorOffset(enum.Enum):
    EOO_OffsetSpecified = 0
    EOO_OffsetZero = 1


class ECameraAlphaBlendMode(enum.Enum):
    CABM_Cubic = 0
    CABM_MAX = 1


class ECameraProjectionMode(enum.Enum):
    Orthographic = 0
    ECameraProjectionMode_MAX = 1


class EChannelType(enum.Enum):
    CHTYPE_Control = 0
    CHTYPE_Actor = 1
    CHTYPE_Voice = 2
    CHTYPE_MAX = 3


class ECloudStorageDelegate(enum.Enum):
    CSD_KeyValueWriteComplete = 0
    CSD_ValueChanged = 1
    CSD_DocumentReadComplete = 2


class EDefaultVertexColor(enum.Enum):
    OpaqueGrey = 0
    OpaqueBlack = 1
    TranslucentGrey = 2
    TransparentBlack = 3


class ECullMethod(enum.Enum):
    INTERPOLATE = 0
    ROUND = 1


class EEvaluateCurveTableResult(enum.Enum):
    RowNotFound = 0
    EEvaluateCurveTableResult_MAX = 1


class EGrammaticalNumber(enum.Enum):
    Plural = 0
    EGrammaticalNumber_MAX = 1


class EGrammaticalGender(enum.Enum):
    EGrammaticalGender_MAX = 0
    Feminine = 1
    Masculine = 2


class DistributionParamMode(enum.Enum):
    DPM_Abs = 0
    DPM_Direct = 1


class EDistributionVectorMirrorFlags(enum.Enum):
    EDVMF_Different = 0
    EDVMF_Mirror = 1


class EDistributionVectorLockFlags(enum.Enum):
    EDVLF_XY = 0
    EDVLF_XZ = 1
    EDVLF_XYZ = 2


class ENodeEnabledState(enum.Enum):
    Disabled = 0
    DevelopmentOnly = 1
    ConstructionScriptOnly = 2


class ENodeAdvancedPins(enum.Enum):
    Shown = 0
    Hidden = 1


class ENodeTitleType(enum.Enum):
    ListView = 0
    MAX_TitleTypes = 1
    EditableTitle = 2


class EPinContainerType(enum.Enum):
    Set = 0
    Array = 1
    EPinContainerType_MAX = 2


class EEdGraphPinDirection(enum.Enum):
    EGPD_Output = 0
    EGPD_MAX = 1


class EBlueprintPinStyleType(enum.Enum):
    BPST_VariantA = 0
    BPST_MAX = 1


class ECanCreateConnectionResponse(enum.Enum):
    CONNECT_RESPONSE_DISALLOW = 0
    CONNECT_RESPONSE_BREAK_OTHERS_AB = 1
    CONNECT_RESPONSE_BREAK_OTHERS_A = 2


class EGraphType(enum.Enum):
    GT_Ubergraph = 0
    GT_StateMachine = 1
    GT_Macro = 2


class EGbxViewFlag(enum.Enum):
    GameFlag8 = 0
    ThirdPerson = 1
    HideViewTarget = 2
    EngineFlag2 = 3
    EngineFlag6 = 4


class EConsoleType(enum.Enum):
    CONSOLE_MAX = 0
    CONSOLE_Mobile = 1


class ETransitionType(enum.Enum):
    Paused = 0
    Connecting = 1
    Loading = 2


class EFullyLoadPackageType(enum.Enum):
    FULLYLOAD_Game_PreLoadClass = 0
    FULLYLOAD_Game_PostLoadClass = 1
    FULLYLOAD_Mutator = 2


class EViewModeIndex(enum.Enum):
    VMI_Wireframe = 0
    VMI_Unlit = 1
    VMI_Lit_DetailLighting = 2
    VMI_CollisionVisibility = 3
    VMI_ShaderComplexity = 4
    VMI_VertexShaderComplexity = 5


class EDemoPlayFailure(enum.Enum):
    Corrupt = 0
    DemoNotFound = 1
    EDemoPlayFailure_MAX = 2


class ENetworkLagState(enum.Enum):
    Lagging = 0
    ENetworkLagState_MAX = 1


class EMouseCaptureMode(enum.Enum):
    CapturePermanently = 0
    CapturePermanently_IncludingInitialMouseDown = 1
    CaptureDuringRightMouseDown = 2


class ECustomTimeStepSynchronizationState(enum.Enum):
    Error = 0
    Synchronized = 1
    ECustomTimeStepSynchronizationState_MAX = 2


class ELODDetailSetting(enum.Enum):
    Medium = 0
    High = 1
    Off = 2


class EMeshBufferAccess(enum.Enum):
    ForceCPUAndGPU = 0
    EMeshBufferAccess_MAX = 1


class EComponentSocketType(enum.Enum):
    Bone = 0
    Socket = 1


class EPhysicalSurface(enum.Enum):
    SurfaceType2 = 0
    SurfaceType1 = 1
    SurfaceType4 = 2
    SurfaceType8 = 3
    SurfaceType16 = 4
    SurfaceType32 = 5
    EPhysicalSurface_MAX = 6


class EUpdateRateShiftBucket(enum.Enum):
    ShiftBucket1 = 0
    ShiftBucket2 = 1
    ShiftBucket4 = 2


class ETeleportType(enum.Enum):
    TeleportPhysics = 0
    ResetPhysics = 1


class EShadowMapFlags(enum.Enum):
    SMF_Streamed = 0
    SMF_RGBA = 1


class ELightMapPaddingType(enum.Enum):
    LMPT_PrePadding = 0
    LMPT_NoPadding = 1


class ETimelineSigType(enum.Enum):
    ETS_FloatSignature = 0
    ETS_InvalidSignature = 1
    ETS_VectorSignature = 2


class EInputConsumeOptions(enum.Enum):
    ICO_ConsumeBoundKeys = 0
    ICO_ConsumeNone = 1


class EFilterInterpolationType(enum.Enum):
    BSIT_Linear = 0
    BSIT_Cubic = 1


class EPhysicsSceneType(enum.Enum):
    PST_Cloth = 0
    PST_Async = 1


class EExtraCollisionChannel(enum.Enum):
    ExtraCollisionChannel_MAX = 0


class EOverlapFilterOption(enum.Enum):
    OverlapFilter_DynamicOnly = 0
    OverlapFilter_StaticOnly = 1


class ELightingBuildQuality(enum.Enum):
    Quality_Medium = 0
    Quality_High = 1
    Quality_MAX = 2


class EMaterialSamplerType(enum.Enum):
    SAMPLERTYPE_Grayscale = 0
    SAMPLERTYPE_Alpha = 1
    SAMPLERTYPE_Masks = 2
    SAMPLERTYPE_External = 3


class EMaterialTessellationMode(enum.Enum):
    MTM_FlatTessellation = 0
    MTM_PNTriangles = 1


class EMaterialShadingModel(enum.Enum):
    MSM_Cloth = 0
    MSM_DefaultLit = 1
    MSM_Subsurface = 2
    MSM_ClearCoat = 3


class EParticleCollisionMode(enum.Enum):
    EParticleCollisionMode_MAX = 0
    DistanceField = 1


class ETrailWidthMode(enum.Enum):
    ETrailWidthMode_FromFirst = 0
    ETrailWidthMode_FromSecond = 1


class EGBufferFormat(enum.Enum):
    Default = 0


class EGbxColorRemapLUTCategory(enum.Enum):
    DCRC_MAX = 0
    DCRC_FX = 1


class ESceneCaptureCompositeMode(enum.Enum):
    SCCM_Additive = 0
    SCCM_Composite = 1


class ESceneCaptureSource(enum.Enum):
    SCS_SceneDepth = 0
    SCS_FinalColorLDR = 1
    SCS_SceneColorHDRNoAlpha = 2
    SCS_MAX = 3


class ETranslucentSortPolicy(enum.Enum):
    SortAlongAxis = 0
    SortByProjectedZ = 1


class ERefractionMode(enum.Enum):
    RM_PixelNormalOffset = 0
    RM_MAX = 1


class ETranslucencyLightingMode(enum.Enum):
    TLM_Surface = 0
    TLM_VolumetricPerVertexNonDirectional = 1
    TLM_VolumetricDirectional = 2


class ESamplerSourceMode(enum.Enum):
    SSM_Wrap_WorldGroupSettings = 0
    SSM_Clamp_WorldGroupSettings = 1


class EOcclusionCombineMode(enum.Enum):
    OCM_MAX = 0
    OCM_Multiply = 1


class EActorMetricsType(enum.Enum):
    METRICS_TRIS = 0
    METRICS_SECTIONS = 1


class EAspectRatioAxisConstraint(enum.Enum):
    AspectRatio_MajorAxisFOV = 0
    AspectRatio_MaintainXFOV = 1


class EPrimitiveSpecificDataFlags(enum.Enum):
    PSDF_CustomLit = 0
    PSDF_MaskPrimitiveInStencil = 1
    PSDF_DebugFlagY = 2


class EFontCacheType(enum.Enum):
    EFontCacheType_MAX = 0
    Runtime = 1


class EFontImportCharacterSet(enum.Enum):
    FontICS_Ansi = 0
    FontICS_Symbol = 1


class EStandbyType(enum.Enum):
    STDBY_Tx = 0
    STDBY_BadPing = 1


class ESuggestProjVelocityTraceOption(enum.Enum):
    TraceFullPath = 0
    OnlyTraceWhileAscending = 1


class EWindowMode(enum.Enum):
    WindowedFullscreen = 0
    Windowed = 1


class EAnimSetFindReplaceDLC(enum.Enum):
    Geranium = 0
    Game = 1
    Dandelion = 2


class EAnimDebugChannel(enum.Enum):
    LookAt = 0
    TickingPhysics = 1
    StretchBones = 2
    ForwardDynamics = 3


class EGbxAttributeModifierType(enum.Enum):
    OverrideBaseValue = 0
    PreAdd = 1
    PostAdd = 2


class EBoneSetTransitionBlendType(enum.Enum):
    ResetToZero_BlendToOne = 0
    None_ = 1
    BlendToOne = 2
    EBoneSetTransitionBlendType_MAX = 3


class ECurveOverrideType(enum.Enum):
    SingleCurve = 0
    NormalizeCurves = 1


class EGbxColorRemapLUTSource(enum.Enum):
    DCRS_NegativeIdentity = 0
    DCRS_FlattenedTexture2D = 1
    DCRS_MAX = 2


class GbxSignificance(enum.Enum):
    Insignificant = 0
    DistantAndInvisible = 1
    Significant = 2


class EGbxTraceAsyncType(enum.Enum):
    Sphere = 0
    Count = 1
    Capsule = 2


class EGbxTraceAsyncMode(enum.Enum):
    EGbxTraceAsyncMode_MAX = 0
    ObjectType = 1
    ObjectTypes = 2


class EGbxZoneMapFODDataState(enum.Enum):
    ZMDS_NoValidTexels = 0
    ZMDS_NoDiscovery = 1
    ZMDS_FullDiscovery = 2


class EHavokNavDataType(enum.Enum):
    VOLUME = 0
    EHavokNavDataType_MAX = 1


class EImportanceWeight(enum.Enum):
    Green = 0
    Red = 1
    Alpha = 2


class EAdManagerDelegate(enum.Enum):
    AMD_UserClosedAd = 0
    AMD_MAX = 1


class EAnimAlphaInputType(enum.Enum):
    Bool = 0
    Curve = 1


class ETrackActiveCondition(enum.Enum):
    ETAC_GoreEnabled = 0
    ETAC_GoreDisabled = 1


class EInterpTrackMoveRotMode(enum.Enum):
    IMR_LookAtGroup = 0
    IMR_Ignore = 1


class EInterpMoveAxis(enum.Enum):
    AXIS_TranslationY = 0
    AXIS_RotationY = 1
    AXIS_TranslationZ = 2


class ETrackToggleAction(enum.Enum):
    ETTA_On = 0
    ETTA_Toggle = 1
    ETTA_MAX = 2


class EVisibilityTrackCondition(enum.Enum):
    EVTC_GoreEnabled = 0
    EVTC_GoreDisabled = 1


class EVisibilityTrackAction(enum.Enum):
    EVTA_Toggle = 0
    EVTA_Show = 1


class ESlateGesture(enum.Enum):
    Scroll = 0
    Magnify = 1
    Rotate = 2


class ELerpInterpolationMode(enum.Enum):
    EulerInterp = 0
    DualQuatInterp = 1


class ERoundingMode(enum.Enum):
    ToZero = 0
    HalfFromZero = 1
    HalfToZero = 2


class ELevelLandscapeCullingPrecision(enum.Enum):
    Medium = 0
    Low = 1


class EStreamingVolumeUsage(enum.Enum):
    SVB_VisibilityBlockingOnLoad = 0
    SVB_LoadingAndVisibility = 1
    SVB_LoadingNotVisible = 2


class EMaterialDecalResponse(enum.Enum):
    MDR_ColorNormalRoughness = 0
    MDR_Color = 1
    MDR_ColorRoughness = 2
    MDR_MAX = 3


class EDecalBlendMode(enum.Enum):
    DBM_Normal = 0
    DBM_Stain = 1
    DBM_DBuffer_ColorNormalRoughness = 2
    DBM_DBuffer_Normal = 3


class ETextureColorChannel(enum.Enum):
    TCC_Green = 0
    TCC_Blue = 1
    TCC_MAX = 2


class EMaterialAttributeBlend(enum.Enum):
    UseA = 0
    UseB = 1


class EChannelMaskParameterColor(enum.Enum):
    EChannelMaskParameterColor_MAX = 0
    Green = 1
    Blue = 2


class EClampMode(enum.Enum):
    CMODE_ClampMin = 0
    CMODE_ClampMax = 1


class ECustomMaterialOutputType(enum.Enum):
    CMOT_Float2 = 0
    CMOT_Float3 = 1
    CMOT_MAX = 2


class EDepthOfFieldFunctionValue(enum.Enum):
    TDOF_NearMask = 0
    TDOF_FarMask = 1
    TDOF_MAX = 2


class EFunctionInputType(enum.Enum):
    FunctionInput_Vector3 = 0
    FunctionInput_Vector2 = 1
    FunctionInput_Texture2D = 2
    FunctionInput_StaticBool = 3


class ENoiseFunction(enum.Enum):
    NOISEFUNCTION_ValueALU = 0
    NOISEFUNCTION_GradientTex = 1
    NOISEFUNCTION_GradientTex3D = 2


class EMaterialSceneAttributeInputMode(enum.Enum):
    OffsetFraction = 0
    EMaterialSceneAttributeInputMode_MAX = 1


class ESceneTextureId(enum.Enum):
    PPI_SceneDepth = 0
    PPI_DiffuseColor = 1
    PPI_SubsurfaceColor = 2
    PPI_WorldNormal = 3
    PPI_PostProcessInput2 = 4


class ESpeedTreeLODType(enum.Enum):
    STLOD_MAX = 0
    STLOD_Smooth = 1


class ESpeedTreeWindType(enum.Enum):
    STW_Best = 0
    STW_Fast = 1
    STW_Fastest = 2


class ESpeedTreeGeometryType(enum.Enum):
    STG_Leaf = 0
    STG_Frond = 1
    STG_Billboard = 2


class EMaterialExposedTextureProperty(enum.Enum):
    TMTM_MAX = 0
    TMTM_TexelSize = 1


class ETextureMipValueMode(enum.Enum):
    TMVM_MipLevel = 0
    TMVM_MipBias = 1
    TMVM_MAX = 2


class ETimeOrigin(enum.Enum):
    Primitive = 0
    Material = 1


class ETimeSource(enum.Enum):
    ETimeSource_MAX = 0
    Real = 1


class EMaterialVectorCoordTransform(enum.Enum):
    TRANSFORM_Local = 0
    TRANSFORM_World = 1
    TRANSFORM_Camera = 2


class EMaterialVectorCoordTransformSource(enum.Enum):
    TRANSFORMSOURCE_Local = 0
    TRANSFORMSOURCE_World = 1
    TRANSFORMSOURCE_Camera = 2


class EMaterialPositionTransformSource(enum.Enum):
    TRANSFORMPOSSOURCE_World = 0
    TRANSFORMPOSSOURCE_TranslatedWorld = 1
    TRANSFORMPOSSOURCE_Camera = 2


class EVectorNoiseFunction(enum.Enum):
    VNF_GradientALU = 0
    VNF_VectorALU = 1
    VNF_VoronoiALU = 2


class EMaterialExposedViewProperty(enum.Enum):
    MEVP_FieldOfView = 0
    MEVP_TanHalfFieldOfView = 1
    MEVP_WorldSpaceViewPosition = 2


class EWorldPositionIncludedOffsets(enum.Enum):
    WPT_CameraRelative = 0
    WPT_ExcludeAllShaderOffsets = 1
    WPT_MAX = 2


class EMaterialFunctionUsage(enum.Enum):
    MaterialLayer = 0
    MaterialLayerBlend = 1


class EMaterialParameterCopyMethod(enum.Enum):
    CopyAll = 0
    CopyAllButSelfInstanced = 1


class EMaterialUsage(enum.Enum):
    MATUSAGE_BeamTrails = 0
    MATUSAGE_ParticleSprites = 1
    MATUSAGE_StaticLighting = 2
    MATUSAGE_Clothing = 3
    MATUSAGE_GPUSprites = 4


class EMaterialParameterAssociation(enum.Enum):
    GlobalParameter = 0
    BlendParameter = 1


class ESimplygonMaterialChannel(enum.Enum):
    SG_MATERIAL_CHANNEL_ROUGHNESS = 0
    SG_MATERIAL_CHANNEL_DIFFUSE = 1
    SG_MATERIAL_CHANNEL_SPECULAR = 2
    SG_MATERIAL_CHANNEL_EMISSIVE = 3


class ESimplygonTextureResolution(enum.Enum):
    TextureResolution_128 = 0
    TextureResolution_256 = 1
    TextureResolution_1024 = 2
    TextureResolution_MAX = 3


class ESimplygonColorChannels(enum.Enum):
    RGB = 0
    L = 1


class ESimplygonTextureSamplingQuality(enum.Enum):
    Low = 0
    Medium = 1
    ESimplygonTextureSamplingQuality_MAX = 2


class ESimplygonCasterType(enum.Enum):
    ESimplygonCasterType_MAX = 0
    Normals = 1
    Color = 2


class ESimplygonTextureStrech(enum.Enum):
    VerySmall = 0
    Large = 1
    Small = 2


class EMaterialLODType(enum.Enum):
    BakeTexture = 0
    BakeVertexColor = 1
    EMaterialLODType_MAX = 2


class ESimplygonLODType(enum.Enum):
    Remeshing = 0
    ESimplygonLODType_MAX = 1


class EOptimizationMetric(enum.Enum):
    OnScreenSize = 0
    MaxDeviation = 1


class EMaterialProxySmaplingQuality(enum.Enum):
    Low = 0
    Medium = 1
    EMaterialProxySmaplingQuality_MAX = 2


class EUVStrech(enum.Enum):
    Large = 0
    Medium = 1
    EUVStrech_MAX = 2


class EMaterialMergeType(enum.Enum):
    MaterialMergeType_Simplygon = 0
    MaterialMergeType_MAX = 1


class ETextureSizingType(enum.Enum):
    TextureSizingType_UseAutomaticBiasedSizes = 0
    TextureSizingType_UseManualOverrideTextureSize = 1
    TextureSizingType_MAX = 2


class EMaterialDomain(enum.Enum):
    MD_PostProcess = 0
    MD_LightFunction = 1
    MD_DeferredDecal = 2


class EMaterialPowerFunction(enum.Enum):
    UnClampedPow = 0
    PositiveClampedPow = 1
    EMaterialPowerFunction_MAX = 2


class EMeshInstancingReplacementMethod(enum.Enum):
    KeepOriginalActorsAsEditorOnly = 0
    EMeshInstancingReplacementMethod_MAX = 1


class EUVOutput(enum.Enum):
    OutputChannel = 0
    EUVOutput_MAX = 1


class EMeshMergeType(enum.Enum):
    MeshMergeType_MergeActor = 0
    MeshMergeType_MAX = 1


class EMeshLODSelectionType(enum.Enum):
    SpecificLOD = 0
    CalculateLOD = 1
    EMeshLODSelectionType_MAX = 2


class EProxyNormalComputationMethod(enum.Enum):
    AreaWeighted = 0
    EqualWeighted = 1


class ELandscapeCullingPrecision(enum.Enum):
    Medium = 0
    Low = 1


class EChartAggregationMode(enum.Enum):
    SurfaceArea = 0
    PixelDensity = 1
    EChartAggregationMode_MAX = 2


class EMeshFeatureImportance(enum.Enum):
    Lowest = 0
    Low = 1
    High = 2


class EVertexPaintAxis(enum.Enum):
    Y = 0
    Z = 1


class EMicroTransactionResult(enum.Enum):
    MTR_Failed = 0
    MTR_Canceled = 1
    MTR_MAX = 2


class EMicroTransactionDelegate(enum.Enum):
    MTD_MAX = 0
    MTD_PurchaseComplete = 1


class FNavigationSystemRunMode(enum.Enum):
    EditorMode = 0
    GameMode = 1
    PIEMode = 2


class ENavigationQueryResult(enum.Enum):
    Error = 0
    Fail = 1
    ENavigationQueryResult_MAX = 2


class ENavPathEvent(enum.Enum):
    UpdatedDueToGoalMoved = 0
    NewPath = 1
    ENavPathEvent_MAX = 2
    Invalidated = 3


class ENavDataGatheringModeConfig(enum.Enum):
    Instant = 0
    Lazy = 1


class ENavDataGatheringMode(enum.Enum):
    Instant = 0
    Lazy = 1


class ENavigationOptionFlag(enum.Enum):
    Enable = 0
    Disable = 1


class ENavLinkDirection(enum.Enum):
    LeftToRight = 0
    RightToLeft = 1


class EmitterPlatform(enum.Enum):
    XBoxOne = 0
    PS4 = 1
    None_ = 2


class EmitterPerformanceCategory(enum.Enum):
    Disabled = 0
    NonCritical = 1


class EEmitterRenderMode(enum.Enum):
    ERM_Point = 0
    ERM_Cross = 1
    ERM_None = 2


class EParticleSubUVInterpMethod(enum.Enum):
    PSUVIM_Linear = 0
    PSUVIM_Linear_Blend = 1
    PSUVIM_Random_Blend = 2


class EParticleBurstMethod(enum.Enum):
    EPBM_Interpolated = 0
    EPBM_MAX = 1


class EBeamAttachmentType(enum.Enum):
    Location = 0
    Actor = 1
    Component = 2


class EParticleSystemInsignificanceReaction(enum.Enum):
    DisableTick = 0
    Complete = 1
    Num = 2


class EParticleSignificanceLevel(enum.Enum):
    Medium = 0
    High = 1
    Num = 2


class EParticleDetailMode(enum.Enum):
    PDM_Medium = 0
    PDM_High = 1


class EParticleSourceSelectionMethod(enum.Enum):
    EPSSM_Sequential = 0
    EPSSM_MAX = 1


class EModuleType(enum.Enum):
    EPMT_TypeData = 0
    EPMT_Beam = 1
    EPMT_Spawn = 2
    EPMT_SubUV = 3


class EAttractorParticleSelectionMethod(enum.Enum):
    EAPSM_Sequential = 0
    EAPSM_MAX = 1


class EBeamModuleTaperMethod(enum.Enum):
    Full = 0
    Partial = 1


class EBeamInterpolation(enum.Enum):
    Cubic = 0
    Spline = 1


class EBeamMethod(enum.Enum):
    Target = 0
    EBeamMethod_MAX = 1


class Beam2SourceTargetTangentMethod(enum.Enum):
    PEB2STTM_UserSet = 0
    PEB2STTM_Distribution = 1
    PEB2STTM_MAX = 2


class Beam2SourceTargetMethod(enum.Enum):
    PEB2STM_Actor = 0
    PEB2STM_UserSet = 1
    PEB2STM_Emitter = 2


class BeamModifierType(enum.Enum):
    PEB2MT_Target = 0
    PEB2MT_MAX = 1


class EParticleCameraOffsetUpdateMethod(enum.Enum):
    EPCOUM_Scalar = 0
    EPCOUM_Additive = 1


class EParticleCollisionComplete(enum.Enum):
    EPCC_Freeze = 0
    EPCC_HaltCollisions = 1
    EPCC_FreezeRotation = 2


class EParticleCollisionResponse(enum.Enum):
    Stop = 0
    Kill = 1


class ELocationBoneSocketSelectionMethod(enum.Enum):
    BONESOCKETSEL_Random = 0
    BONESOCKETSEL_Manual = 1


class ELocationBoneSocketSource(enum.Enum):
    BONESOCKETSOURCE_MAX = 0
    BONESOCKETSOURCE_Sockets = 1


class ELocationEmitterSelectionMethod(enum.Enum):
    ELESM_Sequential = 0
    ELESM_ManualAlpha = 1


class EmitterLocationMode(enum.Enum):
    EvenDistribution = 0
    ManualAlpha = 1


class CylinderHeightAxis(enum.Enum):
    PMLPC_HEIGHTAXIS_Y = 0
    PMLPC_HEIGHTAXIS_Z = 1


class ELocationSkelVertSurfaceSource(enum.Enum):
    VERTSURFACESOURCE_Surface = 0
    VERTSURFACESOURCE_MAX = 1


class EOrbitChainMode(enum.Enum):
    EOChainMode_Scale = 0
    EOChainMode_Link = 1


class EParticleAxisLock(enum.Enum):
    EPAL_X = 0
    EPAL_Y = 1
    EPAL_NEGATIVE_X = 2
    EPAL_ROTATE_Y = 3


class EEmitterDynamicParameterValue(enum.Enum):
    EDPV_AutoSet = 0
    EDPV_VelocityX = 1
    EDPV_VelocityZ = 2


class StartTimeSelectionMethod(enum.Enum):
    StartTimeSelectionMethod_MAX = 0
    Absolute = 1


class AnimationSelectionMethod(enum.Enum):
    Sequential = 0
    AnimationSelectionMethod_MAX = 1


class EEmitterNormalsMode(enum.Enum):
    ENM_Spherical = 0
    ENM_Cylindrical = 1


class EParticleSortMode(enum.Enum):
    PSORTMODE_Age_NewestFirst = 0
    PSORTMODE_ViewProjDepth = 1
    PSORTMODE_DistanceToView = 2


class EParticleUVFlipMode(enum.Enum):
    FlipUOnly = 0
    FlipUV = 1
    RandomFlipUV = 2
    EParticleUVFlipMode_MAX = 3


class ETrail2SourceMethod(enum.Enum):
    PET2SRCM_Particle = 0
    PET2SRCM_Actor = 1


class EBeamTaperMethod(enum.Enum):
    PEBTM_Full = 0
    PEBTM_Partial = 1


class EBeam2Method(enum.Enum):
    PEB2M_Target = 0
    PEB2M_Branch = 1


class MeshSelectionMethod(enum.Enum):
    MeshSelectionMethod_MAX = 0
    Sequential = 1


class EMeshCameraFacingOptions(enum.Enum):
    XAxisFacing_ZUp = 0
    XAxisFacing_NegativeZUp = 1
    XAxisFacing_NegativeYUp = 2
    LockedAxis_NegativeYAxisFacing = 3


class EMeshCameraFacingUpAxis(enum.Enum):
    CameraFacing_ZUp = 0
    CameraFacing_NegativeZUp = 1
    CameraFacing_NegativeYUp = 2


class EMeshScreenAlignment(enum.Enum):
    PSMA_MeshFaceCameraWithLockedAxis = 0
    PSMA_MeshFaceCameraWithSpin = 1


class ETrailsRenderAxisOption(enum.Enum):
    Trails_SourceUp = 0
    Trails_WorldUp = 1


class EVortexAxisAlignment(enum.Enum):
    VAA_Y = 0
    VAA_Z = 1


class NoiseTimeSource(enum.Enum):
    ParticleLifetime = 0
    Length = 1


class ParticleWaveNoiseType(enum.Enum):
    Square = 0
    Triangle = 1
    ParticleWaveNoiseType_MAX = 2


class EParticleScreenAlignment(enum.Enum):
    PSA_Square = 0
    PSA_Rectangle = 1
    PSA_AwayFromCenter = 2


class EForceKillParticlesThreshold(enum.Enum):
    Near = 0
    Mid = 1
    VeryFar = 2


class EParticleSystemOcclusionBoundsMethod(enum.Enum):
    EPSOBM_ParticleBounds = 0
    EPSOBM_CustomBounds = 1


class ParticleSystemLODMethod(enum.Enum):
    PARTICLESYSTEMLODMETHOD_DirectSet = 0
    PARTICLESYSTEMLODMETHOD_ActivateAutomatic = 1


class EParticleSystemUpdateMode(enum.Enum):
    EPSUM_FrozenTime = 0
    EPSUM_FixedTime = 1


class EParticleEventType(enum.Enum):
    EPET_Spawn = 0
    EPET_Burst = 1
    EPET_Death = 2


class ParticleReplayState(enum.Enum):
    PRS_Capturing = 0
    PRS_Replaying = 1


class EStaticPruningStructure(enum.Enum):
    eNONE = 0
    eSTATIC_AABB_TREE = 1


class EBroadPhaseType(enum.Enum):
    eMBP = 0
    EBroadPhaseType_MAX = 1


class ESettingsLockedAxis(enum.Enum):
    X = 0
    Y = 1
    Invalid = 2


class ESettingsDOF(enum.Enum):
    ESettingsDOF_MAX = 0
    YZPlane = 1
    XZPlane = 2


class EFrictionCombineMode(enum.Enum):
    Min = 0
    Multiply = 1


class EReflectionSourceType(enum.Enum):
    SpecifiedCubemap = 0
    EReflectionSourceType_MAX = 1


class EDefaultBackBufferPixelFormat(enum.Enum):
    DBBPF_A16B16G16R16 = 0
    DBBPF_A2B10G10R10 = 1
    DBBPF_FloatRGB = 2


class EAutoExposureMethodUI(enum.Enum):
    AEM_Basic = 0
    AEM_Manual = 1


class EAlphaChannelMode(enum.Enum):
    LinearColorSpaceOnly = 0
    AllowThroughTonemapper = 1


class EEarlyZPass(enum.Enum):
    OpaqueOnly = 0
    OpaqueAndMasked = 1
    EEarlyZPass_MAX = 2


class ECustomDepthStencil(enum.Enum):
    Enabled = 0
    EnabledOnDemand = 1
    ECustomDepthStencil_MAX = 2


class EMobileMSAASampleCount(enum.Enum):
    One = 0
    Two = 1
    Four = 2
    Eight = 3


class ECompositingSampleCount(enum.Enum):
    One = 0
    Two = 1
    Four = 2
    Eight = 3


class EClearSceneOptions(enum.Enum):
    QuadAtMaxZ = 0
    HardwareClear = 1


class EReporterLineStyle(enum.Enum):
    Dash = 0
    EReporterLineStyle_MAX = 1


class ELegendPosition(enum.Enum):
    Inside = 0
    ELegendPosition_MAX = 1


class EGraphDataStyle(enum.Enum):
    EGraphDataStyle_MAX = 0
    Filled = 1


class EGraphAxisStyle(enum.Enum):
    Notches = 0
    Grid = 1


class EConstraintTransform(enum.Enum):
    EConstraintTransform_MAX = 0
    Relative = 1


class EControlConstraint(enum.Enum):
    MAX = 0
    Translation = 1


class ERootMotionFinishVelocityMode(enum.Enum):
    SetVelocity = 0
    ClampVelocity = 1


class ERootMotionSourceSettingsFlags(enum.Enum):
    UseSensitiveLiftoffCheck = 0
    DisablePartialEndTick = 1


class ERootMotionSourceStatusFlags(enum.Enum):
    Prepared = 0
    Finished = 1
    MarkedForRemoval = 2


class ERootMotionAccumulateMode(enum.Enum):
    Additive = 0
    ERootMotionAccumulateMode_MAX = 1


class ELightUnits(enum.Enum):
    Candelas = 0
    Lumens = 1


class EAntiAliasingMethod(enum.Enum):
    AAM_FXAA = 0
    AAM_MAX = 1
    AAM_TemporalAA = 2


class ESceneCapturePrimitiveRenderMode(enum.Enum):
    PRM_RenderScenePrimitives = 0
    PRM_UseShowOnlyList = 1


class EPrimitiveSceneCaptureFlags(enum.Enum):
    PSCF_ForceDrawRelevance_True = 0
    PSCF_TempTestB = 1
    PSCF_ForceDrawRelevance_False = 2


class EMaterialProperty(enum.Enum):
    MP_OpacityMask = 0
    MP_Opacity = 1
    MP_SpecularColor = 2
    MP_Roughness = 3
    MP_AmbientOcclusion = 4
    MP_MaterialAttributes = 5


class EShaderCompareType(enum.Enum):
    GreaterEqual = 0
    Less = 1
    Equal = 2


class EBoundsGenerationType(enum.Enum):
    Tight = 0
    EBoundsGenerationType_MAX = 1


class ESkeletalMeshLODType(enum.Enum):
    Proxy = 0
    ESkeletalMeshLODType_MAX = 1


class EPhysicsTransformUpdateMode(enum.Enum):
    ComponentTransformIsKinematic = 0
    EPhysicsTransformUpdateMode_MAX = 1


class EAnimationMode(enum.Enum):
    EAnimationMode_MAX = 0
    AnimationSingleNode = 1
    AnimationCustomMode = 2


class EKinematicBonesUpdateToPhysics(enum.Enum):
    EKinematicBonesUpdateToPhysics_MAX = 0
    SkipAllBones = 1


class EBoneFilterActionOption(enum.Enum):
    Invalid = 0
    Keep = 1


class SkeletalMeshOptimizationImportance(enum.Enum):
    SMOI_Low = 0
    SMOI_Lowest = 1
    SMOI_High = 2


class SkeletalMeshOptimizationType(enum.Enum):
    SMOT_TriangleOrDeviation = 0
    SMOT_MaxDeviation = 1
    SMOT_MAX = 2


class EBoneTranslationRetargetingMode(enum.Enum):
    Skeleton = 0
    AnimationScaled = 1
    OrientAndScale = 2


class EBoneSpaces(enum.Enum):
    ComponentSpace = 0
    EBoneSpaces_MAX = 1


class EMeshComponentUpdateFlag(enum.Enum):
    AlwaysTickPose = 0
    OccasionallyTickPoseAndRefreshBones = 1
    OnlyTickPoseWhenRendered = 2


class EPhysBodyOp(enum.Enum):
    PBO_Term = 0
    PBO_MAX = 1


class EBoneVisibilityStatus(enum.Enum):
    BVS_Visible = 0
    BVS_ExplicitlyHidden = 1
    BVS_MAX = 2


class ESkyLightSourceType(enum.Enum):
    SLS_SpecifiedCubemap = 0
    SLS_MAX = 1


class EReverbSendMethod(enum.Enum):
    CustomCurve = 0
    Manual = 1


class EAirAbsorptionMethod(enum.Enum):
    EAirAbsorptionMethod_MAX = 0
    CustomCurve = 1


class ESoundSpatializationAlgorithm(enum.Enum):
    SPATIALIZATION_HRTF = 0
    SPATIALIZATION_MAX = 1


class ESoundDistanceCalc(enum.Enum):
    SOUNDDISTANCE_InfiniteXYPlane = 0
    SOUNDDISTANCE_InfiniteXZPlane = 1
    SOUNDDISTANCE_MAX = 2


class EAudioOutputTarget(enum.Enum):
    Controller = 0
    ControllerFallbackToSpeaker = 1


class EMaxConcurrentResolutionRule(enum.Enum):
    StopOldest = 0
    StopFarthestThenPreventNew = 1
    StopLowestPriority = 2


class ESoundGroup(enum.Enum):
    SOUNDGROUP_Effects = 0
    SOUNDGROUP_Voice = 1
    SOUNDGROUP_UI = 2
    SOUNDGROUP_GameSoundGroup4 = 3
    SOUNDGROUP_GameSoundGroup12 = 4


class ModulationParamMode(enum.Enum):
    MPM_Abs = 0
    MPM_Direct = 1


class ESourceBusChannels(enum.Enum):
    Stereo = 0
    ESourceBusChannels_MAX = 1


class EAudioRecordingExportType(enum.Enum):
    WavFile = 0
    EAudioRecordingExportType_MAX = 1


class ESubmixChannelFormat(enum.Enum):
    Stereo = 0
    Quad = 1
    SevenDotOne = 2


class EDecompressionType(enum.Enum):
    DTYPE_RealTime = 0
    DTYPE_Invalid = 1
    DTYPE_Preview = 2
    DTYPE_MAX = 3


class ESplineCoordinateSpace(enum.Enum):
    World = 0
    ESplineCoordinateSpace_MAX = 1


class ESplinePointType(enum.Enum):
    CurveCustomTangent = 0
    Curve = 1
    Constant = 2


class ESplineMeshAxis(enum.Enum):
    Y = 0
    Z = 1


class EStaticMeshLODType(enum.Enum):
    Proxy = 0
    EStaticMeshLODType_MAX = 1


class EOptimizationType(enum.Enum):
    OT_MaxDeviation = 0
    OT_MAX = 1


class EImportanceLevel(enum.Enum):
    IL_Lowest = 0
    IL_Low = 1
    IL_High = 2


class ENormalMode(enum.Enum):
    NM_RecalculateNormals = 0
    NM_RecalculateNormalsSmooth = 1
    TEMP_BROKEN = 2


class EStereoLayerShape(enum.Enum):
    SLSH_CylinderLayer = 0
    SLSH_CubemapLayer = 1


class EStereoLayerType(enum.Enum):
    SLT_TrackerLocked = 0
    SLT_FaceLocked = 1


class EOpacitySourceMode(enum.Enum):
    OSM_RedChannel = 0
    OSM_ColorBrightness = 1
    OSM_BlueChannel = 2


class ESubUVBoundingVertexCount(enum.Enum):
    BVC_EightVertices = 0
    BVC_MAX = 1


class EVerticalTextAligment(enum.Enum):
    EVRTA_MAX = 0
    EVRTA_TextCenter = 1
    EVRTA_TextBottom = 2


class EHorizTextAligment(enum.Enum):
    EHTA_Center = 0
    EHTA_Right = 1


class ETextureCompressionQuality(enum.Enum):
    TCQ_Low = 0
    TCQ_Lowest = 1
    TCQ_High = 2


class ETextureSourceFormat(enum.Enum):
    TSF_RGBA16 = 0
    TSF_G8 = 1
    TSF_BGRA8 = 2
    TSF_MAX = 3


class ETextureSourceArtType(enum.Enum):
    TSAT_PNGCompressed = 0
    TSAT_DDSFile = 1


class ETextureMipCount(enum.Enum):
    TMC_AllMips = 0
    TMC_AllMipsBiased = 1


class ECompositeTextureMode(enum.Enum):
    CTM_NormalRoughnessToRed = 0
    CTM_NormalRoughnessToGreen = 1
    CTM_NormalRoughnessToAlpha = 2


class TextureAddress(enum.Enum):
    TA_Clamp = 0
    TA_Mirror = 1


class TextureFilter(enum.Enum):
    TF_Bilinear = 0
    TF_Trilinear = 1
    TF_MAX = 2


class TextureCompressionSettings(enum.Enum):
    TC_Masks = 0
    TC_Normalmap = 1
    TC_Displacementmap = 2
    TC_Alpha = 3


class ETextureArchetype(enum.Enum):
    Texture3D = 0
    Texture2DArray = 1
    TextureCube = 2


class ETextureSamplerFilter(enum.Enum):
    Bilinear = 0
    Trilinear = 1
    AnisotropicLinear = 2


class ETexturePowerOfTwoSetting(enum.Enum):
    PadToPowerOfTwo = 0
    PadToSquarePowerOfTwo = 1


class TextureMipGenSettings(enum.Enum):
    TMGS_Sharpen6 = 0
    TMGS_SimpleAverage = 1
    TMGS_Sharpen0 = 2
    TMGS_Sharpen2 = 3
    TMGS_Blur2 = 4


class TextureGroup(enum.Enum):
    TEXTUREGROUP_CharacterNormalMap = 0
    TEXTUREGROUP_WorldNormalMap = 1
    TEXTUREGROUP_WorldSpecular = 2
    TEXTUREGROUP_WeaponSpecular = 3
    TEXTUREGROUP_UI = 4
    TEXTUREGROUP_Default = 5


class ETextureRenderTargetFormat(enum.Enum):
    RTF_RG16f = 0
    RTF_RGBA8 = 1
    RTF_RG8 = 2
    RTF_RGBA32f = 3


class ETimecodeProviderSynchronizationState(enum.Enum):
    ETimecodeProviderSynchronizationState_MAX = 0
    Error = 1
    Synchronized = 2


class ETimelineDirection(enum.Enum):
    Backward = 0
    ETimelineDirection_MAX = 1


class ETimelineLengthMode(enum.Enum):
    TL_LastKeyFrame = 0
    TL_MAX = 1


class ETimeStretchCurveMapping(enum.Enum):
    T_TargetMin = 0
    T_TargetMax = 1


class ETwitterIntegrationDelegate(enum.Enum):
    TID_TweetUIComplete = 0
    TID_RequestComplete = 1


class ETwitterRequestMethod(enum.Enum):
    TRM_Post = 0
    TRM_Delete = 1


class EUserDefinedStructureStatus(enum.Enum):
    UDSS_Dirty = 0
    UDSS_MAX = 1
    UDSS_Error = 2


class EUIScalingRule(enum.Enum):
    Custom = 0
    LongestSide = 1
    Horizontal = 2


class ERenderFocusRule(enum.Enum):
    NavigationOnly = 0
    NonPointer = 1
    ERenderFocusRule_MAX = 2


class EVectorFieldConstructionOp(enum.Enum):
    VFCO_Revolve = 0
    VFCO_MAX = 1


class EWindSourceType(enum.Enum):
    Point = 0
    EWindSourceType_MAX = 1


class EPSCPoolMethod(enum.Enum):
    AutoRelease = 0
    EPSCPoolMethod_MAX = 1
    ManualRelease = 2


class EVolumeLightingMethod(enum.Enum):
    VLM_SparseVolumeLightingSamples = 0
    VLM_MAX = 1


class EVisibilityAggressiveness(enum.Enum):
    VIS_ModeratelyAggressive = 0
    VIS_MostAggressive = 1


class Default__UserDefinedEnum(enum.Enum): ...

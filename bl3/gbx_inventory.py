from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import umg
from . import online_subsystem_utils
from . import gbx_runtime
from . import wwise_audio
from . import gbx_dialog
from . import gbx_game_system_core
from . import gbx_ui
from . import gameplay_tags


class InventoryAspectData(gbx_runtime.GbxDataAsset):
    Priority: EInventoryAspectUsagePriority

    def K2_OnBeginPlay(
        self,
        InventoryActor: engine.Actor,
        InventoryBalanceState: InventoryBalanceStateComponent,
    ): ...
    def K2_OnApplyAspect(
        self,
        InventoryActor: engine.Actor,
        InventoryBalanceState: InventoryBalanceStateComponent,
    ): ...
    def K2_GetFriendlyDescription(self) -> str: ...
    def K2_CloneAppearance(
        self,
        CloneActor: engine.Actor,
        InventoryActor: engine.Actor,
        InventoryBalanceState: InventoryBalanceStateComponent,
    ): ...


class InventoryBalanceData(gbx_game_system_core.ActorPartSelectionData):
    InventoryBalanceStateClass: unreal.UClass
    BaseBalanceData: InventoryBalanceData
    InventoryData: InventoryData
    RarityData: InventoryRarityData
    Manufacturers: unreal.WrappedArray[InventoryManufacturerBalanceData]
    RuntimeGenericPartList: RuntimeGenericPartListData
    bIsGearBuildable: bool
    GearBuilderCategory: GearBuilderCategoryData
    MaxNumPrefixes: int
    DlcInventorySetData: DownloadableInventorySetData
    bMigratedToActorPartSelectionData: bool
    AssetGuid: core_uobject.Guid
    bDisableVisibilityAndCollision: bool


class InventoryData(gbx_runtime.GbxDataAsset):
    bInventoryNameIsFullName: bool
    InventoryName: str
    PrefixPartList: unreal.WrappedArray[InventoryNamePartData]
    TitlePartList: unreal.WrappedArray[InventoryNamePartData]
    SuffixPartList: unreal.WrappedArray[InventoryNamePartData]
    NamingStrategy: InventoryNamingStrategyData
    InventoryActorClass: unreal.UClass
    InventoryAttributeEffects: unreal.WrappedArray[
        gbx_game_system_core.AttributeEffectData
    ]
    InstigatorAttributeEffects: unreal.WrappedArray[
        gbx_game_system_core.InstigatorAttributeEffectData
    ]
    AspectList: unreal.WrappedArray[InventoryAspectData]
    StandaloneAspectList: unreal.WrappedArray[InventoryAspectData]
    bDisplayNameInInteractionHeader: bool
    bUsesItemCard: bool
    ItemCardTypeFrameName: str
    OnUseConstraints: unreal.WrappedArray[gbx_runtime.GbxCondition]
    bUsesPlayerLevelRequirement: bool
    UIStats: unreal.WrappedArray[gbx_game_system_core.UIStatPriorityData]
    AssetGuid: core_uobject.Guid
    PickupSound: wwise_audio.WwiseEvent
    PickupEquipSound: wwise_audio.WwiseEvent
    SpottedCalloutCondition: gbx_runtime.GbxCondition
    SpottedCallout: gbx_dialog.DialogEvent
    PickupImpact: gbx_game_system_core.ImpactData
    EquipUISound: wwise_audio.WwiseEvent
    DropUISound: wwise_audio.WwiseEvent
    InventoryItemPickupClass: unreal.UClass
    bReplicateActorInPickup: bool
    bSharedByPickups: bool
    bMustMatchGameStageToShare: bool
    PickupFlyToTarget: str
    PickupHiddenBones: unreal.WrappedArray[str]
    bOverrideRotationInShop: bool
    RotationInShop: core_uobject.Rotator
    bOverrideTranslationInShop: bool
    TranslationInShop: core_uobject.Vector
    bOverrideScaleInShop: bool
    ScaleInShop: core_uobject.Vector
    bOverrideRotationInContainer: bool
    RotationInContainer: core_uobject.Rotator
    bCanBeHolsteredOnBody: bool
    bCanShowHolsteredInFirstPerson: bool
    DefaultHolsterSocketName: str
    InventoryCategory: InventoryCategoryData
    PlayerDroppability: EPlayerDroppability
    SizeInInventory: int
    MonetaryValue: gbx_game_system_core.AttributeInitializationData
    bIgnoreShopPriceMarkup: bool
    bCalculatePriceInShopUsingPlayerAsContext: bool
    BaseMonetaryValueModifier: float
    bUsesInventoryScore: bool
    AssociatedCustomizationData: unreal.UObject
    ThumbnailTransform: core_uobject.Transform
    ItemInspectInitialTransform: core_uobject.Transform
    ItemInspectInitialTransform_Vertical: core_uobject.Transform
    ItemInspectInitialTransform_4way: core_uobject.Transform

    def EnumeratePickupFlyToTargets(self, Targets: unreal.WrappedArray[str]): ...


class InventoryData_Simple(InventoryData):
    InventoryBalanceStateClass: unreal.UClass
    ManufacturerData: ManufacturerData
    RarityData: InventoryRarityData
    BalanceData: InventoryBalanceData


class InventoryListComponent(engine.ActorComponent):
    InventoryList: InventoryListContainer
    InventoryCapacityUsed: int
    SelectedIndexs: Any
    DroppedPickupClass: unreal.UClass
    bCanPickupOnTouch: bool
    MaxInventoryItems: engine.GbxAttributeInteger
    OnInventoryItemAdded: Any
    OnInventoryItemRemoved: Any
    OnInventoryItemUpdated: Any
    OnInventoryItemActorReplaced: Any
    OnInventoryItemQuantityUpdated: Any
    OnInventoryItemPickedUp: Any
    OnAddedToInventory_Internal: Any
    OnPreAddToFullInventory_Internal: Any
    OnRemovingFromInventory_Internal: Any

    def SizeInInventory(self, PickupToTest: InventoryItemPickup) -> int: ...
    def ServerTransferItem(
        self,
        InventoryItemHandle: InventoryListEntryHandle,
        DestinationActor: engine.Actor,
        Quantity: int,
    ): ...
    def ServerSetItemUIFlags(
        self, Handle: InventoryListEntryHandle, Flags: int, FlagsMask: int
    ): ...
    def ServerSetItemsUIFlags(
        self, Category: InventoryCategoryData, Flags: int, FlagsMask: int
    ): ...
    def ServerRemoveItem(self, InventoryItemHandle: InventoryListEntryHandle): ...
    def ServerRemoveCustomizationPartFromInventoryActor(
        self,
        InventoryItemHandle: InventoryListEntryHandle,
        Part: InventoryCustomizationPartData,
    ): ...
    def ServerDropItem(
        self,
        InventoryItemHandle: InventoryListEntryHandle,
        InitialLocation: core_uobject.Vector,
        InitialRotation: core_uobject.Rotator,
    ): ...
    def ServerConsumeItem(
        self, InventoryItemHandle: InventoryListEntryHandle, Quantity: int
    ): ...
    def ServerAddCustomizationPartToInventoryActor(
        self,
        InventoryItemHandle: InventoryListEntryHandle,
        Part: InventoryCustomizationPartData,
    ): ...
    def IsInventoryFull(self) -> bool: ...
    def HasActorInList(self, ItemActor: engine.Actor) -> bool: ...
    def GetStoredInventoryActor(
        self, InventoryItemHandle: InventoryListEntryHandle
    ) -> engine.Actor: ...
    def GetSelectedItemQuantity(
        self, ChildTypeToGet: InventoryCategoryData, Quantity: int, MaxQuantity: int
    ): ...
    def GetMaxInventoryItems(self) -> int: ...
    def GetItem(
        self,
        InventoryItemHandle: InventoryListEntryHandle,
        ListEntry: InventoryListEntry,
    ) -> bool: ...
    def GetInventoryListEntryDisplayName(
        self, ListEntry: InventoryListEntry
    ) -> str: ...
    def GetInventoryListEntryDisplayDescription(
        self, ListEntry: InventoryListEntry
    ) -> str: ...
    def GetInventoryItemCount(self) -> int: ...
    def GetInventoryHandlesOfType(
        self,
        ChildTypeToGet: InventoryCategoryData,
        ItemHandleList: unreal.WrappedArray[InventoryListEntryHandle],
    ): ...
    def GetInventoryDisplayName(self, InventoryActor: engine.Actor) -> str: ...
    def GetInventoryDisplayDescription(self, InventoryActor: engine.Actor) -> str: ...
    def GetCategoryOnlyInventoryHandles(
        self,
        ChildTypeToGet: InventoryCategoryData,
        ItemHandleList: unreal.WrappedArray[InventoryListEntryHandle],
    ): ...
    def GetCategoryItemQuantity(self, ItemCategory: InventoryCategoryData) -> int: ...
    def GetAndConsumeSelected(
        self, TypeToConsume: InventoryCategoryData, Quantity: int
    ) -> engine.Actor: ...
    def GetAndConsumeItem(
        self, InventoryItemHandle: InventoryListEntryHandle, Quantity: int
    ) -> engine.Actor: ...
    def ClearInventory(self, DestroyInventory: bool): ...
    def CanUseSelected(
        self, ChildTypeToUse: InventoryCategoryData, Quantity: int
    ) -> bool: ...
    def CanSwapItemForPickup(
        self, Item: engine.Actor, Pickup: InventoryItemPickup
    ) -> bool: ...
    def AddOrUpdateCategoryOnly(
        self, ItemCategory: InventoryCategoryData, Quantity: int
    ): ...
    def AddItemFromPickup(
        self, PickupActor: InventoryItemPickup
    ) -> InventoryListEntryHandle: ...
    def AddExternalItemEx(
        self,
        ItemCategory: InventoryCategoryData,
        ActorToAdd: engine.Actor,
        Quantity: int,
        Flags: int,
        bConditionalDestroyActor: bool,
        DesiredSlot: int,
        bBypassInventoryFull: bool,
    ) -> InventoryListEntryHandle: ...
    def AddExternalItem(
        self,
        ItemCategory: InventoryCategoryData,
        ActorToAdd: engine.Actor,
        Quantity: int,
        AddedByPickup: bool,
        bAutoEquip: bool,
        bConditionalDestroyActor: bool,
        DesiredSlot: int,
        bBypassInventoryFull: bool,
    ) -> InventoryListEntryHandle: ...
    def AddCategory(
        self, ItemCategory: InventoryCategoryData, TrackQuantity: bool
    ) -> bool: ...


class InventoryBalanceStateComponent(gbx_game_system_core.BalanceStateComponent):
    PackedReplicationData: InventoryReplicationData
    NamePartList: unreal.WrappedArray[InventoryNamePartData]
    MonetaryValueModifierTotal: float
    MonetaryValue: int
    InventoryScoreModifierTotal: float
    InventoryScoreValue: int
    InventoryData: InventoryData
    InventoryBalanceData: InventoryBalanceData
    ManufacturerData: ManufacturerData
    PartList: unreal.WrappedArray[InventoryPartData]
    GenericPartList: unreal.WrappedArray[InventoryGenericPartData]
    AdditionalData: unreal.WrappedArray[int]
    CustomizationPartList: unreal.WrappedArray[InventoryCustomizationPartData]
    ReRollCount: int
    DisplayName: str
    GenericAspects: unreal.WrappedArray[InventoryAspectData]
    GestaltData: engine.GestaltData
    GestaltMeshPartNames: unreal.WrappedArray[str]
    InstigatorAttributeModifiers: unreal.WrappedArray[
        gbx_game_system_core.GbxAttributeModifierHandle
    ]
    PrimitiveAspectSetList: unreal.WrappedArray[InventoryPrimitiveAspectSetData]
    ConditionalDamageAspectList: unreal.WrappedArray[
        InventoryConditionalDamageAspectData
    ]
    AttributeEffectsAspectList: unreal.WrappedArray[InventoryAttributeEffectsAspectData]
    ParticleAspects: unreal.WrappedArray[InventoryParticleAspectData]
    UIStats: gbx_game_system_core.CachedUIStatCollectionData
    ReplicatedUIStats: gbx_game_system_core.ReplicatedUIStatCollectionData
    InventoryMaterialAspectTextureAssetStreamers: unreal.WrappedArray[
        InventoryMaterialAspectTextureAssetStreamer
    ]

    def PostBeginPlay(self): ...
    def OnRep_ReplicatedUIStats(self): ...
    def NotifyUnequipped(self, OldInstigator: engine.Pawn): ...
    def NotifyEquipped(self, NewInstigator: engine.Pawn): ...
    def NotifyAttached(self, Instigator: engine.Pawn): ...
    def K2_GetDamageType(self) -> unreal.UClass: ...
    def IsManufactureredBy(self, Manufacturer: ManufacturerData) -> bool: ...
    def GetReRollCount(self) -> int: ...
    def GetPartList(self) -> unreal.WrappedArray[InventoryPartData]: ...
    def GetMonetaryValue(self) -> int: ...
    def GetManufacturer(self) -> ManufacturerData: ...
    def GetInventoryScoreValue(self) -> int: ...
    def GetInventoryRarityLootBeamOverride(self) -> engine.ParticleSystem: ...
    def GetInventoryRarityLootBeamHeight(self) -> float: ...
    def GetInventoryRarityLootAudioStinger(self) -> wwise_audio.WwiseEvent: ...
    def GetInventoryRarityLifeSpanType(self) -> EDropLifeSpanType: ...
    def GetInventoryRarityLifeSpan(self) -> float: ...
    def GetInventoryRarityFrameName(self) -> str: ...
    def GetInventoryRarityDisplayName(self) -> str: ...
    def GetInventoryRarityData(self) -> InventoryRarityData: ...
    def GetInventoryRarityColorOutline(self) -> core_uobject.LinearColor: ...
    def GetInventoryRarityColorFX(self) -> core_uobject.LinearColor: ...
    def GetInventoryDisplayRarityOutline(self) -> bool: ...
    def GetInventoryData(self) -> InventoryData: ...
    def GetInventoryBalanceData(self) -> InventoryBalanceData: ...
    def GetGenericPartList(self) -> unreal.WrappedArray[InventoryGenericPartData]: ...
    def GetDisplayName(self) -> str: ...
    def GetDamageType(self) -> unreal.UClass: ...
    def GetCustomizationPartList(
        self,
    ) -> unreal.WrappedArray[InventoryCustomizationPartData]: ...
    def CloneAppearance(
        self,
        DestActor: engine.Actor,
        ParentComp: engine.SceneComponent,
        bAbsoluteScale: bool,
    ): ...


class InventoryItemPickup(engine.Actor):
    PickupAudioEvent: wwise_audio.WwiseEvent
    CompletePickupAudioEvent: wwise_audio.WwiseEvent
    DestroyOnPickup: bool
    UseFailBumpUpVelocity: float
    UseFailBumpBaseRotation: float
    PickedUpBy: engine.Actor
    PickupMesh: engine.StaticMeshComponent
    PickupSkelMesh: engine.SkeletalMeshComponent
    PickupActorParticles: unreal.WrappedArray[engine.ParticleSystemComponent]
    Quantity: int
    bCanOnlyBePickedUpByOwnerController: bool
    bHighDetail: bool
    bSharedWithAllPlayers: bool
    bSharedPlayersMustBeOnFriendlyTeam: bool
    bReplicatePickupActor: bool
    StaticPickup: bool
    bUseInventoryDataPickupActionType: bool
    DefaultPickupActorClass: unreal.UClass
    MaxDrawDistance: float
    DefaultPickupActionType: EPickupActionType
    StaticPickupActionType: EPickupActionType
    CanBeTouchedCondition: gbx_runtime.GbxCondition
    PickupCategory: InventoryCategoryData
    OnPickupSpawnUnpaused: Any
    OnPickupSpawnActive: Any
    OnPickupIsActive: Any
    OnPickedUp: Any
    StaticLocation: core_uobject.Vector
    StaticRotation: core_uobject.Rotator
    NotAddedToInventory: bool
    PickupSphereRadius: float
    PickupSphereRadiusHideScale: float
    PickupSphereComponent: engine.SphereComponent
    AssociatedInventoryData: InventoryData
    OverrideErrorText: str
    PlacedPickup: bool
    CachedInventoryBalanceComponent: InventoryBalanceStateComponent
    PickupActor: engine.Actor
    ReplicatedPickupActor: engine.Actor
    PickupActorClientSpawnData: InventoryItemPickupClientSpawnData
    bPickupSpawnPaused: bool
    bIsActive: bool
    BumpAngularDir: engine.Vector_NetQuantizeNormal
    LootSpawnAction: unreal.UClass
    RepLootSpawnAction: unreal.UClass

    def WaitForBalanceState(self): ...
    def SetCanOnlyBePickedUpByOwner(
        self,
        bNewCanOnlyBePickedUpByOwnerController: bool,
        OwnerController: engine.Controller,
    ): ...
    def ResetBumpOnPickupFail(self): ...
    def OnUsedBy(self, UseEvent: gbx_game_system_core.UseEvent): ...
    def OnRespawnEvent(self): ...
    def OnRep_RepLootSpawnAction(self): ...
    def OnRep_PickupActorClientSpawnData(self): ...
    def OnRep_PickupActor(self): ...
    def OnRep_PickedUpBy(self): ...
    def OnRep_IsActive(self): ...
    def OnRep_BumpAngularDir(self): ...
    def OnPickedUpEvent(self, WasPickedUpBy: engine.Actor): ...
    def OnLookedAtByPlayer(
        self,
        InstigatingPlayer: engine.PlayerController,
        bCanInteractWith: bool,
        NewUsableComponentImpactPoint: core_uobject.Vector,
        NewUsableDistanceAway: float,
    ): ...
    def IsPickupInitialized(self) -> bool: ...
    def GiveInventoryToUser(self, Other: engine.Actor, bAutoEquip: bool): ...
    def GetMeshComponent(self) -> engine.MeshComponent: ...
    def GetInventoryRarityLootBeamOverride(self) -> engine.ParticleSystem: ...
    def GetInventoryRarityLootAudioStinger(self) -> wwise_audio.WwiseEvent: ...
    def GetInventoryRarityLifeSpanType(self) -> EDropLifeSpanType: ...
    def GetInventoryRarityColorOutline(self) -> core_uobject.LinearColor: ...
    def GetInventoryRarityColorFX(self) -> core_uobject.LinearColor: ...
    def GetInventoryDisplayRarityOutline(self) -> bool: ...
    def GetInventoryBalanceStateComponent(self) -> InventoryBalanceStateComponent: ...
    def DeactivatePickup(self): ...
    def CanBePickedUp(
        self,
        Other: engine.Actor,
        UsedByOther: bool,
        bUseHeld: bool,
        bForMassPickup: bool,
    ) -> bool: ...
    def ActivatePickup(self): ...
    def ActivateAfterSpawnDelay(self): ...


class DroppedInventoryItemPickup(InventoryItemPickup):
    LinearDamping: float
    NextImpactDistanceThreshold: float
    NextImpactTimeThreshold: float
    ImpactVelocityThreshold: float
    DefaultVelocity: float
    InitialMassScale: float
    DroppedQuantity: int
    ShrinkLifeSpan: float
    bDroppedFromPlayerInventory: bool

    def OnRep_ShrinkLifeSpan(self): ...
    def OnRep_InitialMassScale(self): ...
    def OnRep_DroppedQuantity(self): ...
    def OnPickupHit(
        self,
        HitComponent: engine.PrimitiveComponent,
        OtherActor: engine.Actor,
        OtherComp: engine.PrimitiveComponent,
        NormalImpulse: core_uobject.Vector,
        Hit: engine.HitResult,
    ): ...
    def OnPhysicsWake(
        self, WakingComponent: engine.PrimitiveComponent, BoneName: str
    ): ...
    def OnPhysicsSleep(
        self, WakingComponent: engine.PrimitiveComponent, BoneName: str
    ): ...


class DownloadableInventorySetData(online_subsystem_utils.DownloadableContentData): ...


class InventoryCustomizationPartData(gbx_game_system_core.GbxCustomizationData):
    AssetGuid: core_uobject.Guid
    bShouldRemovePartWhenDropped: bool


class InventoryPartData(gbx_game_system_core.ActorPartData):
    MonetaryValueModifier: gbx_game_system_core.AttributeInitializationData
    InventoryScoreModifier: gbx_game_system_core.AttributeInitializationData
    PrefixPartList: unreal.WrappedArray[InventoryNamePartData]
    TitlePartList: unreal.WrappedArray[InventoryNamePartData]
    SuffixPartList: unreal.WrappedArray[InventoryNamePartData]
    InventoryNamingTag: str
    InventoryAttributeEffects: unreal.WrappedArray[
        gbx_game_system_core.AttributeEffectData
    ]
    InstigatorAttributeEffects: unreal.WrappedArray[
        gbx_game_system_core.InstigatorAttributeEffectData
    ]
    UIStats: unreal.WrappedArray[gbx_game_system_core.UIStatPriorityData]
    bAvailableForPartInspection: bool
    PartInspectionTitleOverride: unreal.WrappedArray[
        gbx_game_system_core.UIStatData_Text
    ]
    PartInspectionDescription: gbx_game_system_core.UIStatData_Text
    bHideStatsForPartInspection: bool
    AspectList: unreal.WrappedArray[InventoryAspectData]
    GearBuilderDescription: str
    bShouldIgnorePartBoundsForPickupAttachment: bool
    ExcludedGestaltMeshPartNamesForItemInspectionAndThumbnailBounds: (
        unreal.WrappedArray[str]
    )
    AssetGuid: core_uobject.Guid

    def GetMonetaryValueModifier(
        self,
    ) -> gbx_game_system_core.AttributeInitializationData: ...


class InventoryGenericPartData(InventoryPartData):
    bOverridePartSelection: bool
    Tags: gameplay_tags.GameplayTagContainer


class InventoryNamingStrategyData(gbx_runtime.GbxDataAsset): ...


class InventoryRarityData(gbx_runtime.GbxDataAsset):
    RarityColorFX: core_uobject.LinearColor
    RarityColorOutline: core_uobject.LinearColor
    RarityOutlineDepthStencilValue: int
    DisplayRarityOutline: bool
    RarityFrameName: str
    RarityLifeSpanType: EDropLifeSpanType
    RarityDisplayname: str
    RaritySortValue: int
    RarityLootBeamOverride: engine.ParticleSystem
    RarityLootBeamForInventoryWithFoilParts: engine.ParticleSystem
    RarityLootBeamHeight: float
    ItemScoreRarityModifier: gbx_game_system_core.AttributeInitializationData
    RarityLootAudioStinger: wwise_audio.WwiseEvent
    MonetaryValueModifier: gbx_game_system_core.AttributeInitializationData
    OnPickedUpStat: Any

    def GetRaritySortValue(self) -> int: ...
    def GetRarityOutlineDepthStencilValue(self) -> int: ...
    def GetRarityLootBeamOverride(
        self, bInventoryHasAFoilPart: bool
    ) -> engine.ParticleSystem: ...
    def GetRarityLootBeamHeight(self) -> float: ...
    def GetRarityLootAudioStinger(self) -> wwise_audio.WwiseEvent: ...
    def GetRarityLifeSpanType(self) -> EDropLifeSpanType: ...
    def GetRarityLifeSpan(self) -> float: ...
    def GetRarityDisplayName(self) -> str: ...
    def GetRarityColorOutline(self) -> core_uobject.LinearColor: ...
    def GetRarityColorFX(self) -> core_uobject.LinearColor: ...
    def GetItemScoreRarityModifier(
        self,
    ) -> gbx_game_system_core.AttributeInitializationData: ...
    def GetDisplayRarityOutline(self) -> bool: ...


class LootableComponent(engine.ActorComponent):
    OnPickupAttached: Any
    OnPickupDetached: Any
    OnAllPickupsDetached: Any
    BalanceData: LootableBalanceData
    InitialDropLootMassScale: float
    LootAttachmentMode: EPickupLootAttachmentMode
    LootSpawnActions: unreal.WrappedArray[unreal.UClass]
    bForceSpawnedLootToHaveInfiniteLifespan: bool
    UseOverrideBoxExtents: core_uobject.Vector
    bOverrideUseWithBox: bool
    LootConfigurations: unreal.WrappedArray[LootConfigurationInfo]
    AttachedLoot: unreal.WrappedArray[DroppedInventoryItemPickup]
    LootableBalanceDataOverride: LootableBalanceData
    BalanceContextOverride: engine.Actor

    def SpawnAndDropLoot(self, SelectedConfigurationName: str): ...
    def SpawnAndAttachLoot(self, SelectedConfigurationName: str): ...
    def SetBalanceContextOverride(
        self, NewOverrideContext: engine.Actor, bOnlyUseForGameStage: bool
    ): ...
    def InitializeLootConfigurations(
        self, LootableBalanceData: LootableBalanceData
    ): ...
    def GetAttachedPickups(self) -> unreal.WrappedArray[DroppedInventoryItemPickup]: ...
    def ActivateAttachedLoot(self): ...


class ManufacturerData(gbx_runtime.GbxDataAsset):
    MinGameStage: gbx_game_system_core.AttributeInitializationData
    MaxGameStage: gbx_game_system_core.AttributeInitializationData
    ManufacturerName: str
    Blurb: str
    UIStats: unreal.WrappedArray[gbx_game_system_core.UIStatData]
    AssetGuid: core_uobject.Guid
    ManufacturerLogoFrameName: str
    ManufacturerDialogEnumValue: gbx_dialog.DialogEnumValue


class ItemPoolListInterface(gbx_runtime.GbxDataAsset):
    PartSelectionOverrides: unreal.WrappedArray[ItemPoolPartSelectionOverrideData]


class ItemPoolData(ItemPoolListInterface):
    BalancedItems: unreal.WrappedArray[BalancedInventoryInfo]
    bSupportsGameStageVariance: bool
    Quantity: gbx_game_system_core.AttributeInitializationData
    MinGameStageRequirement: gbx_game_system_core.GbxAttributeData
    MaxGameStageRequirement: gbx_game_system_core.GbxAttributeData
    Expansions: unreal.WrappedArray[ItemPoolExpansionData]
    AssetGuid: core_uobject.Guid


class InventoryMaterialAspectData(InventoryAspectData):
    PrimitiveComponentName: str
    PrimitiveComponentTag: str
    SectionIndex: int
    Material: engine.MaterialInterface
    RaritySpecificMaterials: unreal.WrappedArray[RarityMaterialData]
    VectorParameters: unreal.WrappedArray[MaterialVectorParameterData]
    ScalarParameters: unreal.WrappedArray[MaterialScalarParameterData]
    TextureParameters: unreal.WrappedArray[MaterialTextureParameterData]
    TextureAssetParameters: unreal.WrappedArray[MaterialTextureAssetParameterData]
    FontParameters: unreal.WrappedArray[MaterialFontParameterData]


class InventoryPartSetData(gbx_game_system_core.ActorPartSetData):
    GenericParts: InventoryGenericPartListData


class InventoryAttributeEffectsAspectData(InventoryAspectData):
    ComparisonTags: gameplay_tags.GameplayTagContainer
    bResetAttributes: bool
    InventoryAttributeEffects: unreal.WrappedArray[
        gbx_game_system_core.AttributeEffectData
    ]


class GbxCondition_InventoryRarityComparison(gbx_runtime.GbxCondition):
    Operator: gbx_game_system_core.EConditionComparisonOperatorType
    ReferenceRarity: InventoryRarityData


class GearBuilderCategoryData(gbx_runtime.GbxDataAsset):
    CategoryName: str


class GearBuilderWidget(umg.Widget):
    OwnerMenu: GearBuilderDebugMenu
    GearData: InventoryBalanceStateInitializationData
    SelectedItem: unreal.UObject


class GearBuilderDebugMenu(gbx_ui.GbxDebugMenuSubmenu):
    GearBuilder: GearBuilderWidget


class InventoryBalanceCollectionData(gbx_runtime.GbxDataAsset):
    ParentCollection: InventoryBalanceCollectionData
    InventoryBalanceList: unreal.WrappedArray[Any]
    RuntimeInventoryBalanceList: unreal.WrappedArray[InventoryBalanceData]


class InventoryBalanceData_Generated(InventoryBalanceData): ...


class InventoryBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def GetPossibleGenericParts(
        self,
        InventoryBalanceState: InventoryBalanceStateComponent,
        Tags: gameplay_tags.GameplayTagContainer,
        bMustHaveAllTags: bool,
        bExcludeCurrentlySelectedParts: bool,
    ) -> unreal.WrappedArray[InventoryGenericPartData]: ...
    def GetInventoryBalanceState(
        self, Inventory: engine.Actor
    ) -> InventoryBalanceStateComponent: ...
    def CreateInventory(
        self,
        WorldContextObject: unreal.UObject,
        bCreatePickup: bool,
        SpawnLocation: core_uobject.Vector,
        InitData: InventoryBalanceStateInitializationData,
    ) -> engine.Actor: ...
    def CloneInventory(self, SourceInventory: engine.Actor) -> engine.Actor: ...
    def BuildInventory(
        self,
        WorldContextObject: unreal.UObject,
        bCreatePickup: bool,
        SpawnLocation: core_uobject.Vector,
        InitData: InventoryBalanceStateInitializationData,
    ) -> engine.Actor: ...


class InventoryCategoryData(gbx_game_system_core.GbxInventoryCategoryData):
    NotAddedToInventory: bool
    PickupActionType: EPickupActionType
    SharedWithAllPlayers: bool
    bSharedPlayersMustBeOnFriendlyTeam: bool
    bLevelSyncPickupCurrency: bool
    ManualActivation: bool
    CategoryDisplayName: str
    bCanInspectItem: bool
    bCanInspectManufacturer: bool
    bCanInspectElementalEffects: bool
    bCanInspectParts: bool
    bCanChangeSkins: bool
    bUseEquipAudioFromWeaponType: bool
    bDoNotUseCosmeticLabelInBackpackCells: bool
    EquipAudioEventName: str
    bEnableSaveGameQuantityChangeThrottling: bool


class InventoryConditionalDamageAspectData(InventoryAspectData):
    DamageConditionals: unreal.WrappedArray[InventoryConditionalDamageAspectInfo]


class InventoryGenericPartExpansionData(gbx_runtime.GbxDataAsset):
    ExpansionCondition: gbx_runtime.GbxCondition
    InventoryBalanceCollection: InventoryBalanceCollectionData
    GenericParts: InventoryGenericPartExpansionListData

    def EnumeratePartListForPartType(
        self,
        PartType: int,
        OutPartList: unreal.WrappedArray[gbx_game_system_core.ActorPartData],
    ): ...


class InventoryMaterialAspectTextureAssetStreamer(unreal.UObject): ...


class InventoryModuleSettings(unreal.UObject):
    DefaultDroppedPickupBlueprint: unreal.UClass
    VeryShortLivedDropLifeSpan: float
    ShortLivedDropLifeSpan: float
    LongLivedDropLifeSpan: float
    PickupShrinkDuration: float
    ResetBumpOnPickupFailDelay: float
    PickupFlyToTargets: unreal.WrappedArray[str]


class InventoryNamePartData(gbx_runtime.GbxDataAsset):
    PartName: str
    Priority: float
    Condition: gbx_runtime.GbxCondition
    MinExperienceLevel: int
    MaxExperienceLevel: int


class InventoryOwnerInterface(core_uobject.Interface):

    def AttachedItemPickedUp(
        self, InventoryItemPickedUp: InventoryItemPickup, PickedUpBy: engine.Actor
    ): ...


class InventoryParticleAspectData(InventoryAspectData):
    ParticleSystem: engine.ParticleSystem
    ComponentName: str
    SocketName: str
    RelativeTranslation: core_uobject.Vector
    RelativeRotation: core_uobject.Rotator
    ConditionalEmitters: unreal.WrappedArray[ConditionalInventoryParticleEmitter]


class InventorySerialNumberAssetInterface(core_uobject.Interface): ...


class InventorySerialNumberDatabase(unreal.UObject):
    AssetClasses: unreal.WrappedArray[unreal.UClass]


class ItemPoolExpansionData(gbx_runtime.GbxDataAsset):
    ItemPoolToExpand: ItemPoolData
    BalancedItems: unreal.WrappedArray[BalancedInventoryInfo]


class ItemPoolListData(ItemPoolListInterface):
    ItemPoolIncludedLists: unreal.WrappedArray[ItemPoolListData]
    ItemPools: unreal.WrappedArray[ItemPoolInfo]


class ItemPoolPartSelectionOverrideData(gbx_runtime.GbxDataAsset):
    PartSetClass: unreal.UClass
    PartTypeEnum: unreal.UEnum
    PartTypeOverrides: unreal.WrappedArray[ItemPoolPartSelectionPartTypeOverrideData]

    def EnumerateInventoryParts(
        self,
        PartType: int,
        OutPartList: unreal.WrappedArray[gbx_game_system_core.ActorPartData],
    ): ...


class LootableBalanceData(gbx_runtime.GbxDataAsset):
    DefaultLoot: unreal.WrappedArray[LootConfigurationInfo]
    DefaultIncludedLootLists: unreal.WrappedArray[LootListData]
    DefaultLootGameStageVarianceFormula: unreal.UClass


class LootFunctionLibrary(engine.BlueprintFunctionLibrary):

    def SpawnItemsRaw(
        self,
        WorldContextObject: unreal.UObject,
        ItemPoolLists: unreal.WrappedArray[ItemPoolListData],
        ExtraItemPools: unreal.WrappedArray[ItemPoolInfo],
        GameStage: int,
        Location: core_uobject.Vector,
        Rotation: core_uobject.Rotator,
        InitialVelocity: float,
    ): ...


class LootListData(gbx_runtime.GbxDataAsset):
    LootData: unreal.WrappedArray[LootConfigurationInfo]


class PickupableMeshActor(engine.Actor):
    ActionComponent: gbx_game_system_core.GbxActionComponent


class PickupFlyToAbleInterface(core_uobject.Interface): ...


class PickupFlyToData(gbx_runtime.GbxDataAsset):
    MaxLifetime: float
    TargetThreshold: float
    bEnableSpinSpeedRange: bool
    bEnableLinearSpeedRange: bool
    bEnableTargetRotationSpeedRange: bool
    SpinSpeed: core_uobject.Rotator
    MaxSpinSpeed: core_uobject.Rotator
    LinearSpeed: float
    MaxLinearSpeed: float
    LinearAcceleration: float
    TerminalLinearSpeed: float
    TargetRotationSpeed: float
    MaxTargetRotationSpeed: float
    TargetScaleByDistanceCurve: engine.CurveFloat
    TargetScaleByDistanceBlendInSpeed: float
    ArcCurve: engine.CurveFloat
    ArcCompletePercent: float


class PickupFlyToTargetInterface(core_uobject.Interface): ...


class InventoryListEntryHandle:
    Handle: int


class ItemPoolInfo:
    ItemPool: ItemPoolData
    PoolProbability: gbx_game_system_core.AttributeInitializationData
    NumberOfTimesToSelectFromThisPool: gbx_game_system_core.AttributeInitializationData
    PartSelectionOverrides: unreal.WrappedArray[ItemPoolPartSelectionOverrideData]


class SelectedInventoryInfo:
    InventoryData: InventoryData
    InventoryBalanceData: InventoryBalanceData
    ManufacturerData: ManufacturerData
    GameStage: int
    PartSelectionOverrideData: gbx_game_system_core.ActorPartSelectionOverrideData
    GenericPartSelectionOverrideData: gbx_game_system_core.ActorPartList
    GenericPartsToInject: unreal.WrappedArray[InventoryGenericPartData]
    bCompileUIStats: bool
    bDroppedFromAI: bool


class InventoryReplicationData: ...


class InventorySaveGameData:
    EncryptedSerialNumber: unreal.WrappedArray[int]
    DevelopmentSaveData: InventoryBalanceStateInitializationData


class InventoryBalanceStateInitializationData:
    GameStage: int
    InventoryData: InventoryData
    InventoryBalanceData: InventoryBalanceData
    ManufacturerData: ManufacturerData
    PartList: unreal.WrappedArray[InventoryPartData]
    GenericPartList: unreal.WrappedArray[InventoryGenericPartData]
    AdditionalData: unreal.WrappedArray[int]
    CustomizationPartList: unreal.WrappedArray[InventoryCustomizationPartData]
    ReRollCount: int
    bDroppedFromAI: bool


class InventoryListEntry(engine.FastArraySerializerItem):
    Handle: InventoryListEntryHandle
    BaseCategoryDefinition: InventoryCategoryData
    Quantity: int
    StoredActor: engine.Actor
    PlayerDroppability: EPlayerDroppability


class ItemPoolCollection:
    ItemPools: unreal.WrappedArray[ItemPoolInfo]
    ItemPoolLists: unreal.WrappedArray[ItemPoolListData]


class MaterialParameterData:
    Name: str


class RuntimeGenericPartListData:
    bEnabled: bool
    PartList: unreal.WrappedArray[gbx_game_system_core.WeightedActorPartData]


class InventoryManufacturerBalanceData:
    ManufacturerData: ManufacturerData
    GameStageWeight: gbx_game_system_core.GameStageGradeWeightData
    PartSelectionOverrideData: ItemPoolPartSelectionOverrideData


class InventoryPrimitiveAspectSetData:
    PrimitiveComponentName: str
    PrimitiveComponentTag: str
    SectionAspectSetList: unreal.WrappedArray[InventoryPrimitiveSectionAspectSetData]


class InventoryPrimitiveSectionAspectSetData:
    PrimaryMaterialAspect: InventoryMaterialAspectData
    MaterialAspects: unreal.WrappedArray[InventoryMaterialAspectData]


class InventoryConditionalDamageAspectInfo:
    ConditionalModifier: gbx_game_system_core.ConditionalDamageModifier
    bUseInventoryForDamageValueContext: bool
    ApplicationTarget: EInventoryConditionalDamageApplicationTarget


class InventoryGenericPartExpansionListData(gbx_game_system_core.ActorPartListData): ...


class InventoryItemPickupClientSpawnData:
    bSpawnDefaultPickupActor: bool
    BalanceData: InventoryReplicationData
    UIStats: gbx_game_system_core.ReplicatedUIStatCollectionData
    MonetaryValue: int
    InventoryScoreValue: int


class InventorySelectionTracker:
    SelectedIndex: int
    TrackQuantity: bool
    SelectedHandle: InventoryListEntryHandle


class InventoryListContainer(engine.FastArraySerializer):
    Items: unreal.WrappedArray[InventoryListEntry]


class InventoryListEntryUIData: ...


class InventoryCategorySaveData:
    BaseCategoryDefinition: InventoryCategoryData
    Quantity: int


class RarityMaterialData:
    Rarity: InventoryRarityData
    Material: engine.MaterialInterface


class MaterialFontParameterData(MaterialParameterData):
    Font: engine.Font
    FontPage: int


class MaterialTextureAssetParameterData(MaterialParameterData):
    Texture: Any


class MaterialTextureParameterData(MaterialParameterData):
    Texture: engine.Texture


class MaterialScalarParameterData(MaterialParameterData):
    Scalar: float


class MaterialVectorParameterData(MaterialParameterData):
    Vector: core_uobject.LinearColor


class ConditionalInventoryParticleEmitter:
    EnableCondition: gbx_runtime.GbxCondition
    EmitterNames: unreal.WrappedArray[str]


class InventoryGenericPartListData(gbx_game_system_core.ActorPartListData): ...


class InventorySerialNumber:
    State: EInventorySerialNumberState
    Buffer: unreal.WrappedArray[int]
    RunningCounter: int


class BalancedInventoryInfo:
    ItemPoolData: ItemPoolData
    InventoryBalanceData: Any
    ResolvedInventoryBalanceData: InventoryBalanceData
    Weight: gbx_game_system_core.AttributeInitializationData


class ItemPoolPartSelectionPartTypeOverrideData:
    PartType: int
    PreferredParts: unreal.WrappedArray[gbx_game_system_core.ActorPartData]


class LootConfigurationInfo:
    ConfigurationName: str
    LootGameStageVarianceFormula: unreal.UClass
    Weight: gbx_game_system_core.AttributeInitializationData
    ItemAttachments: unreal.WrappedArray[LootAttachmentInfo]


class LootAttachmentInfo:
    ItemPool: ItemPoolData
    AttachmentPointName: str
    Probability: gbx_game_system_core.AttributeInitializationData
    OverrideAttachmentList: unreal.WrappedArray[PoolSocketAttachmentInfo]


class PoolSocketAttachmentInfo:
    ItemPool: ItemPoolData
    AttachmentPointName: str
    Weight: gbx_game_system_core.AttributeInitializationData


class ManufacturerGradeData:
    DisplayName: str


class EPickupLootAttachmentMode(enum.Enum):
    Center = 0
    ScaleDown = 1
    CenterAndScale = 2


class EPlayerDroppability(enum.Enum):
    EPD_NoDrop = 0
    EPD_NoDropOrSell = 1


class EPickupActionType(enum.Enum):
    OnUseOnly = 0
    OnTouchOnly = 1


class EInventoryAspectUsagePriority(enum.Enum):
    Medium = 0
    Low = 1
    Ultra = 2


class EInventoryConditionalDamageApplicationTarget(enum.Enum):
    InstigatorDamageCaused = 0
    InstigatorDamageReceived = 1


class EAddInventoryItemFlags(enum.Enum):
    AddedByPickup = 0
    AddedBySave = 1
    EAddInventoryItemFlags_MAX = 2


class EDropLifeSpanType(enum.Enum):
    DROP_LiveAsLongAsLevel = 0
    DROP_ShortLived = 1
    DROP_LongLived = 2


class EInventorySerialNumberState(enum.Enum):
    Writing = 0
    Full = 1
    Encrypted = 2


class EPickupFlyToAlignmentType(enum.Enum):
    TargetFacing = 0
    EPickupFlyToAlignmentType_MAX = 1

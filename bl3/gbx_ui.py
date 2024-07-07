from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine
from . import umg
from . import gbx_runtime
from . import wwise_audio
from . import gbx_dialog
from . import gbx_game_system_core
from . import media_assets
from . import scaleform_ui
from . import input_core
from . import slate_core



class GbxGFxMovie(scaleform_ui.GFxMoviePlayer):
    MovieData: scaleform_ui.SwfMovie
    ScaleModeType: int
    AlignmentType: int
    bAnchorToViewport: bool
    AnchorData: GbxGFxAnchor
    AudioDataTable: engine.DataTable
    GetChildAppendix: GbxGFxMovieClipAppendix
    GetChildStrategy: scaleform_ui.EGbxGFxMovieGetChildStrategy
    CachedStage: GbxGFxObject
    GbxRoot: GbxGFxObject
    GetChildRoot: GbxGFxObject
    CachedGbxRootPosition: core_uobject.Vector2D
    bIsTransitioning: bool
    TransitionTimeout: float
    OwningGPC: gbx_game_system_core.GbxPlayerController
    Tickables: unreal.WrappedArray[GbxGFxObject]
    bGbxMovieStarted: bool
    def TranslateWorldToLocal(self, LocationWorldSpace: core_uobject.Vector, OutPositionLocal: core_uobject.Vector2D, bPlayerViewportRelative: bool, bUseMovieDimensions: bool, ReturnValue: bool) -> bool: ...
    def TranslateToScreen(self, Point: core_uobject.Vector2D, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def TranslateScreenToLocal(self, Point: core_uobject.Vector2D, bUseMovieDimensions: bool, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def TranslateRectToScreen(self, Rect: core_uobject.Box2D, ReturnValue: core_uobject.Box2D) -> core_uobject.Box2D: ...
    def SpawnMovie(self, NewGPCOwner: gbx_game_system_core.GbxPlayerController, RenderTarget: engine.TextureRenderTarget2D): ...
    def SpawnGbxGFxMovie(self, GbxPlayerController: gbx_game_system_core.GbxPlayerController, MovieClass: unreal.UClass, ReturnValue: GbxGFxMovie) -> GbxGFxMovie: ...
    def SetViewportToPlayerScreen(self, pc: gbx_game_system_core.GbxPlayerController): ...
    def SetOffsetDisplayTransform(self, Transform: core_uobject.Transform): ...
    def SetBaseDisplayTransform(self, Transform: core_uobject.Transform): ...
    def SetAudioEnabled(self, bEnabled: bool): ...
    def SetAnchor(self, Anchor: GbxGFxAnchor): ...
    def RunUIEventAudio(self, EventName: str, ProviderHistory: str, ReturnValue: bool) -> bool: ...
    def GetViewportOffset(self, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def GetViewportDimensions(self, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def GetStageDimensions(self, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def GetOwningPlayerPawn(self, ReturnValue: engine.Pawn) -> engine.Pawn: ...
    def GetOwningPlayerController(self, ReturnValue: gbx_game_system_core.GbxPlayerController) -> gbx_game_system_core.GbxPlayerController: ...
    def GetOffsetDisplayTransform(self, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def GetMovieDimensions(self, ReturnValue: core_uobject.Vector2D) -> core_uobject.Vector2D: ...
    def GetBaseDisplayTransform(self, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def extTransitionComplete(self): ...
    def extAnimationFinished(self, TargetName: str): ...
    def ApplyNewAudioSettings(self, NewDataTable: engine.DataTable, MergeOperation: EUIAudioSettingOperation): ...


class GbxGFxMenu(GbxGFxMovie):
    DefaultMouseFocusBehavior: EGbxFocusableWidgetMouseBehavior
    MenuData: GbxGFxMenuData
    ButtonFocusedAudioEventName: str
    ButtonClickedAudioEventName: str
    SliderAudioEventName: str
    SpinnerAudioEventName: str
    NavigateBackAudioEventName: str
    OpenMenuAudioEventName: str
    CloseMenuAudioEventName: str
    HintBarAlignment: EGbxGFxListAlignment
    bCallMenuTickOnlyIfMenuIsStarted: bool
    SplitscreenRootOffset: float
    OwnedContextualMenu: GbxGFxContextualMenu
    ActiveDialog: GbxGFxMenu
    PCOwner: gbx_game_system_core.GbxPlayerController
    PrimaryCharacterOwner: gbx_game_system_core.GbxCharacter
    MenuStackOwner: GbxMenuStack
    DrawPriority: int
    FocusManager: GbxWidgetFocusManager
    HintBar: GbxHintBar
    HintBarContainer: GbxGFxHintBarContainer
    MouseBlockerClip: GbxGFxMouseBlocker
    bWantsDismiss: bool
    GameInstanceRef: gbx_game_system_core.GbxGameInstance
    UIGlobalsRef: GbxUIGlobals
    bCachedLastInputFromMouse: bool
    bReceiveMouseEvenIfNotActive: bool
    bIsInitedFromStash: bool
    bMouseHitsAllowedYet: bool
    bGotFirstMouseMove: bool
    MenuContentClip: GbxGFxObject
    MenuLayoutsClip: GbxGFxObject
    MenuLayoutClip: GbxGFxObject
    bIsSplitScreenLayout: bool
    bBlockPauseMenu: bool
    bGFxMenuWasStarted: bool
    LastFocusedButton: GbxGFxButton
    def MenuStack_Clear(self): ...
    def IsWidgetFocused(self, WidgetInQuestion: unreal.UObject, ReturnValue: bool) -> bool: ...
    def GetFocusedWidget(self, ReturnValue: unreal.UObject) -> unreal.UObject: ...


class GbxGFxHUDWidget(GbxGFxMovie):
    AnchorType: EGFxHUDWidgetAnchorType
    LayoutInstanceStringOverride: str
    AnchorBoneName: str
    MaxContextSensitivePromptTime: float
    MaxTimeUntilStopAdvancing: float
    ShowFrameName: str
    HideFrameName: str
    OnFrameName: str
    OffFrameName: str
    ContextSensitivePrompt: GbxGFxHintWidget
    InstanceString: str
    OwningHUD: GbxHUD
    OwningHUDContainer: GbxGFxHUDContainer
    OwningPC: gbx_game_system_core.GbxPlayerController
    OwningPawn: engine.Pawn
    IconTransitionWrapper: GbxGFxObject
    InitializationClip: GbxGFxObject
    GameInstanceRef: engine.GameInstance
    UIGlobalsRef: GbxUIGlobals
    bDynamicallyLoaded: bool
    def extInitAnimationFinished(self): ...
    def extHideAnimationFinished(self): ...


class GbxUserWidget(umg.UserWidget):
    LabelTextBlock: umg.TextBlock
    ValueTextBlock: umg.TextBlock
    SelectedImage: umg.Image
    bRegisterAsFocusableWidget: bool
    MouseFocusBehavior: EGbxFocusableWidgetMouseBehavior
    FocusableWidgetStyleData: GbxFocusableWidgetStyleData
    OnFocusedAudioEventName: str
    OnClickedAudioEventName: str
    bNeverCreateMouseFocusButton: bool
    MouseFocusButton: umg.BUTTON
    FocusableWidgetNavUp: str
    FocusableWidgetNavDown: str
    FocusableWidgetNavLeft: str
    FocusableWidgetNavRight: str
    bFocusOnMenuCreation: bool
    MenuThatOwnsFocus: GbxUmgMenu
    AudioDataTable: engine.DataTable
    def SetLabelText(self, LabelText: str): ...
    def OnFocusableWidgetUnhovered(self): ...
    def OnFocusableWidgetReleased(self): ...
    def OnFocusableWidgetPressed(self): ...
    def OnFocusableWidgetHovered(self): ...
    def OnFocusableWidgetClicked(self): ...
    def IsRegisteredAsFocusableWidget(self, ReturnValue: bool) -> bool: ...
    def IsFocusableWidgetStateHovered(self, State: EGbxFocusableWidgetState, ReturnValue: bool) -> bool: ...
    def IsFocusableWidgetStateFocused(self, State: EGbxFocusableWidgetState, ReturnValue: bool) -> bool: ...
    def HandleFocusableWidgetStateChanged(self, NewState: EGbxFocusableWidgetState, bBecameFocused: bool, bLostFocus: bool): ...
    def GotoAndStop(self, StopTime: core_uobject.FrameTime, InAnimation: umg.WidgetAnimation): ...
    def GetAllChildWidgetsOfClass(self, TargetClass: unreal.UClass, OutputArray: unreal.WrappedArray[umg.Widget]): ...


class GbxUmgMenu(GbxUserWidget):
    MenuData: GbxUmgMenuData
    PCOwner: gbx_game_system_core.GbxPlayerController
    MenuStackOwner: GbxMenuStack
    FocusManager: GbxWidgetFocusManager
    HintBar: GbxHintBar
    DefaultMouseFocusBehavior: EGbxFocusableWidgetMouseBehavior
    def SetWidgetAdjacency(self, Widget: unreal.UObject, AdjacencyInfo: GbxFocusableWidgetAdjacencyInfo): ...
    def SetSlateFocusedWidget(self, Widget: umg.Widget): ...
    def SetFocusedWidget(self, Widget: unreal.UObject, bFromMouse: bool): ...
    def SetFocusableWidgetAdjancency(self, Widget: unreal.UObject, AdjacentUp: unreal.UObject, AdjacentDown: unreal.UObject, AdjacentLeft: unreal.UObject, AdjacentRight: unreal.UObject): ...
    def RegisterFocusableWidgetWithAdjacency(self, Widget: unreal.UObject, AdjacentUp: unreal.UObject, AdjacentDown: unreal.UObject, AdjacentLeft: unreal.UObject, AdjacentRight: unreal.UObject): ...
    def RegisterFocusableWidget(self, Widget: unreal.UObject, AdjacencyInfo: GbxFocusableWidgetAdjacencyInfo): ...
    def PopulateHintBar(self): ...
    def NavigateBack(self): ...
    def MenuStack_SwitchTo(self, MenuDataIn: GbxMenuData, ReturnValue: unreal.UObject) -> unreal.UObject: ...
    def MenuStack_Push(self, MenuDataIn: GbxMenuData, ReturnValue: unreal.UObject) -> unreal.UObject: ...
    def MenuStack_PopToSwitchTo(self, Menu: unreal.UObject, MenuDataIn: GbxMenuData, ReturnValue: unreal.UObject) -> unreal.UObject: ...
    def MenuStack_PopTo(self, Menu: unreal.UObject): ...
    def MenuStack_Pop(self): ...
    def MenuStack_Clear(self): ...
    def IsWidgetFocused(self, WidgetInQuestion: unreal.UObject, ReturnValue: bool) -> bool: ...
    def IsActiveMenuOnStack(self, ReturnValue: bool) -> bool: ...
    def HandleMenuInputDeviceChanged(self, NewInputDevice: EGbxMenuInputDevice): ...
    def HandleMenuInputAction(self, InputAction: str, ControllerId: int): ...
    def HandleMenuInit(self): ...
    def HandleMenuDeinit(self): ...
    def HandleMenuDeactivate(self): ...
    def HandleMenuAspectRatioChanged(self, NewAspectRatio: float): ...
    def HandleMenuActivate(self): ...
    def GetListItemFactory(self, ReturnValue: GbxListItemFactory) -> GbxListItemFactory: ...
    def GetFocusedWidget(self, ReturnValue: unreal.UObject) -> unreal.UObject: ...
    def GetCurrentInputDevice(self, ReturnValue: EGbxMenuInputDevice) -> EGbxMenuInputDevice: ...


class GbxMenuSwitcherSubmenu(GbxUmgMenu):
    OwnerMenuSwitcher: GbxMenuSwitcher



class GbxDebugMenuSubmenu(GbxMenuSwitcherSubmenu): ...


class GbxMenuData(gbx_runtime.GbxDataAsset):
    bHideMenusBeneath: bool
    bShowsMouse: bool
    InputMode: EGbxMenuInputMode
    ParentType: EGbxMenuParentType
    bAutoAttemptPop: bool
    bUseMenuStashing: bool
    bActivateIfPoppedTo: bool
    IdleDialogEvent: gbx_dialog.DialogEvent
    IdleDialogTargetParamater: gbx_dialog.DialogParameter



class GbxGFxMenuData(GbxMenuData):
    TransitionMovieClipTarget: str
    TransitionOutAnimation: str
    TransitionOutTimeout: float
    OverrideHUDState: GbxHUDStateData
    GFxMenuDrawPriorityBoost: int
    CreatedMenus: unreal.WrappedArray[unreal.UObject]



class GbxGFxObject(scaleform_ui.GFxObject):
    OwningMovie: GbxGFxMovie
    def SetOffsetDisplayTransform(self, Transform: core_uobject.Transform): ...
    def SetBaseDisplayTransform(self, Transform: core_uobject.Transform): ...
    def RotateAboutPoint(self, Degrees: float, Point: core_uobject.Vector2D): ...
    def GetOffsetDisplayTransform(self, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def GetBaseDisplayTransform(self, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...


class GbxGFxButton(GbxGFxObject):
    MouseFocusBehavior: EGbxFocusableWidgetMouseBehavior
    OnFocusedAudioEventName: str
    OnClickedAudioEventName: str
    OwningMenu: GbxGFxMenu
    Label: GbxTextField
    AppearanceFrameClip: GbxGFxObject
    TimeButtonHeld: float
    bHasSentHeldEvent: bool
    bWantsHeld: bool
    bIgnoreNextClick: bool
    bNewIndicatorUsesLabels: bool
    def SetLockedState(self, InLockedState: EGbxGFxButtonLockedState, bShouldRefresh: bool): ...
    def SetLabelText(self, Text: str, bForceUpdate: bool): ...
    def SetCheckedState(self, InCheckedState: EGbxGFxButtonCheckedState, bShouldRefresh: bool): ...
    def SetButtonType(self, InButtonType: EGbxGFxButtonType): ...
    def RefreshView(self, PrevState: EGbxFocusableWidgetState): ...
    def K2_HandleFocusableWidgetStateChanged(self, NewState: EGbxFocusableWidgetState, bBecameFocused: bool, bLostFocus: bool): ...
    def IsRegisteredAsFocusableWidget(self, ReturnValue: bool) -> bool: ...
    def IsLocked(self, ReturnValue: bool) -> bool: ...
    def IsFocusableWidgetStateUp(self, State: EGbxFocusableWidgetState, ReturnValue: bool) -> bool: ...
    def IsFocusableWidgetStateHovered(self, State: EGbxFocusableWidgetState, ReturnValue: bool) -> bool: ...
    def IsFocusableWidgetStateFocused(self, State: EGbxFocusableWidgetState, ReturnValue: bool) -> bool: ...
    def IsFocusableWidgetStateDown(self, State: EGbxFocusableWidgetState, ReturnValue: bool) -> bool: ...
    def IsFocusableWidgetStateDisabled(self, State: EGbxFocusableWidgetState, ReturnValue: bool) -> bool: ...
    def IsChecked(self, ReturnValue: bool) -> bool: ...
    def GetLockedState(self, ReturnValue: EGbxGFxButtonLockedState) -> EGbxGFxButtonLockedState: ...
    def GetCheckedState(self, ReturnValue: EGbxGFxButtonCheckedState) -> EGbxGFxButtonCheckedState: ...
    def GetButtonType(self, ReturnValue: EGbxGFxButtonType) -> EGbxGFxButtonType: ...
    def GbxGFxButtonEvent__DelegateSignature(self, BUTTON: GbxGFxButton, InputInfo: GbxMenuInputEvent): ...


class GbxGFxListCell(GbxGFxButton):
    OwningList: GbxGFxGridScrollingList
    CellBounds: GbxGFxObject
    ListIndex: int
    PositionInContainer: core_uobject.Vector2D
    TopOffsetPosition: float
    BottomOffsetPosition: float
    LeftOffsetPosition: float
    RightOffsetPosition: float
    bIsReadjustingFocus: bool



class GbxGFxListCellWithData(GbxGFxListCell):
    TextID: str
    DataAsset: engine.DataAsset



class GbxGFxListItemSpinner(GbxGFxListCellWithData):
    SpinnerItem: GbxSpinner
    def OnSpinnerValueUpdated(self): ...


class GbxGFxMenuSwitcherSubmenu(GbxGFxMenu):
    OwnerMenuSwitcher: GbxGFxMenuSwitcher



class GbxGFxMenuSwitcher(GbxGFxMenu):
    CurrentSubmenu: GbxGFxMenuSwitcherSubmenu
    CurrentSubmenuId: str
    PreviousSubmenuId: str
    NumSubMenus: int



class GbxGFxMovieLoader(GbxGFxObject):
    LoadedMovie: GbxGFxObject
    QueuedLoadMovie: scaleform_ui.SwfMovie
    CurrentMovie: scaleform_ui.SwfMovie



class GbxGFxProgressBar(GbxGFxObject):
    Percent: float
    NumFillFrames: int
    NumDeltaBarFrames: int
    NumBackgroundBarFrames: int
    DefaultInterpolator: GbxProgressBarInterpolator
    Ranges: unreal.WrappedArray[GbxProgressBarRange]
    EdgeFlashID: str
    EdgeFlashInnerID: str
    FillBarId: str
    DeltaBarId: str
    BackgroundBarId: str
    CurrentValueLabelId: str
    MaxValueLabelId: str
    Interpolator: GbxProgressBarInterpolator
    def SetPercent(self, InPercent: float): ...
    def SetMaxValueText(self, Text: str): ...
    def SetFillColorAndOpacity(self, InColor: core_uobject.LinearColor): ...
    def SetCurrentValueText(self, Text: str): ...
    def PassedPercentThreshold(self, Threshold: float, OldValue: float, CurrentValue: float, bIncreasing: bool, bDecreasing: bool, ReturnValue: bool) -> bool: ...
    def InterpolateToPercentWithInterpolator(self, InPercent: float, Interpolator: GbxProgressBarInterpolator): ...
    def InterpolateToPercent(self, InPercent: float): ...
    def HandlePercentChanged(self, OldValue: float, CurrentValue: float, bIsInterpolating: bool, ActiveInterpolator: GbxProgressBarInterpolator): ...
    def HandleEnterPercentRange(self, RangeName: str): ...
    def GetPercent(self, ReturnValue: float) -> float: ...
    def EnteredPercentRange(self, RangeMin: float, RangeMax: float, OldValue: float, CurrentValue: float, bIncreasing: bool, bDecreasing: bool, ReturnValue: bool) -> bool: ...


class GbxGFxGridScrollingList(GbxGFxObject):
    Config: GbxGFxListConfig
    SelectedIndex: int
    SelectedIndexWhenFocusWasLost: int
    AllCells: unreal.WrappedArray[GbxScrollingListCellInfo]
    UnusedCellPool: unreal.WrappedArray[GbxScrollingListCellInfo]
    GridArea: GbxGFxObject
    GridMask: GbxGFxObject
    PositionOfFirstItem: core_uobject.Vector2D
    NextUniqueId: int
    ViewWindowSize: float
    UiScroller: GbxUIScroller
    bIsContentDirty: bool
    AverageItemDims: core_uobject.Vector2D
    ScrollBar: GbxGFxSlider
    bScrollbarIsChildOfThis: bool
    def OnScrollBarPositionUpdated(self, SliderPercentage: float): ...


class GbxGFxPooledGridList(GbxGFxGridScrollingList):
    PooledConfig: GbxGFxPooledGridListConfig
    HelperDataDirDim: float
    HelperDataItemsInDir: int
    HelperDataItemsPerDir: int
    HelperDataFirstItemIndex: int
    HelperDataNumVisibleItems: int
    HelperDataScrollOffset: float
    MasterCellPool: unreal.WrappedArray[GbxGFxPooledGridPoolInfo]



class GbxGFxRadioButtonList(GbxGFxGridScrollingList): ...


class GbxGFxListItemNumber(GbxGFxListCellWithData):
    SliderRepeatsToAccelerate: int
    SliderMaxIncreases: int
    SliderFastestSteps: int
    SliderItem: GbxGFxSlider
    ValueItem: GbxTextField
    def OnSliderUpdated(self, SliderPct: float): ...


class GbxGFxEditableTextField(GbxGFxListCell):
    bConfirmOnFocusOut: bool
    EditText: str
    bMultiline: bool
    KeyboardType: GFxVirtualKeyboardType
    bLoseFocusOnConfirm: bool
    OnTextSubmittedAudioEventName: str
    OnTextEditAbortedAudioEventName: str
    OnTextInputAudioEventName: str



class GbxGFxGridScrollingListPaged(GbxGFxGridScrollingList): ...


class GbxGFxMenuSwitcherMenuData(GbxGFxMenuData):
    CurrentSubmenus: unreal.WrappedArray[GbxGFxMenuSwitcherSubmenuInfo]
    Submenus: unreal.WrappedArray[GbxGFxMenuSwitcherSubmenuInfo]



class GbxHUDContainer(GbxUserWidget):
    RootPanel: umg.CanvasPanel
    OwningPlayerController: gbx_game_system_core.GbxPlayerController
    OwningHUD: GbxHUD
    ProjectedContainerZOrder: int
    DebugPanel: umg.CanvasPanel
    def HandleInit(self): ...
    def HandleDeinit(self): ...
    def HandleDeactivate(self): ...
    def HandleActivate(self): ...


class GbxHUDWidget(GbxUserWidget):
    CachedGeometry: slate_core.Geometry
    OwningHUDContainer: GbxHUDContainer
    OwningHUD: GbxHUD
    OwningPlayerController: gbx_game_system_core.GbxPlayerController
    def HandleInit(self): ...
    def HandleDeinit(self): ...
    def HandleDeactivate(self): ...
    def HandleActivate(self): ...


class GbxListItem(GbxUserWidget):
    ChangedAudioEventName: str
    def GetItemIndex(self, ReturnValue: int) -> int: ...


class GbxListItemText(GbxListItem): ...


class GbxGFxHUDContainer(GbxGFxMovie):
    Widgets: unreal.WrappedArray[GbxGFxHUDWidget]
    HUDData: GbxHUDData
    FeedbackManager: GbxHUDFeedbackManager
    OwningPC: gbx_game_system_core.GbxPlayerController
    OwningHUD: GbxHUD
    OwningPawn: engine.Pawn
    bViewportNeedsRefresh: bool
    bFinishedInitializing: bool



class GbxHUD(engine.HUD):
    HudStateManager: GbxHUDStateManager
    bDisplayScaleformHUD: bool
    ChangedFromPawn: engine.Pawn
    GFxHUDContainer: GbxGFxHUDContainer
    OverrideContainerDefinition: GbxHUDData
    CurrentInputDevice: EGbxMenuInputDevice
    OwningPC: gbx_game_system_core.GbxPlayerController
    OwningPrimaryCharacter: gbx_game_system_core.GbxCharacter
    OwningPawn: engine.Pawn
    def SwitchToHUDState(self, PlayerController: gbx_game_system_core.GbxPlayerController, State: GbxHUDStateData): ...
    def SetHUDContainer(self, PlayerController: gbx_game_system_core.GbxPlayerController, ContainerDefinition: GbxHUDData): ...
    def PushHUDState(self, PlayerController: gbx_game_system_core.GbxPlayerController, State: GbxHUDStateData, bAllowDuplicatePush: bool): ...
    def PopToSwitchToHUDState(self, PlayerController: gbx_game_system_core.GbxPlayerController, PopToState: GbxHUDStateData, SwitchToState: GbxHUDStateData): ...
    def PopToHUDState(self, PlayerController: gbx_game_system_core.GbxPlayerController, State: GbxHUDStateData): ...
    def PopSpecifiedHUDState(self, PlayerController: gbx_game_system_core.GbxPlayerController, State: GbxHUDStateData): ...
    def PopHUDState(self, PlayerController: gbx_game_system_core.GbxPlayerController): ...
    def OnPrimaryCharacterChanged(self, Character: gbx_game_system_core.GbxCharacter): ...
    def OnPawnChanged(self, Pawn: engine.Pawn, OldPawn: engine.Pawn): ...
    def GotoPreviousHUDState(self, PlayerController: gbx_game_system_core.GbxPlayerController): ...
    def GotoHUDState(self, PlayerController: gbx_game_system_core.GbxPlayerController, State: GbxHUDStateData): ...
    def GetCurrentHUDState(self, PlayerController: gbx_game_system_core.GbxPlayerController, ReturnValue: GbxHUDStateData) -> GbxHUDStateData: ...
    def ClearToDefaultHUDState(self, PlayerController: gbx_game_system_core.GbxPlayerController): ...
    def ClearHUDStates(self, PlayerController: gbx_game_system_core.GbxPlayerController): ...


class GbxUILibrary(engine.BlueprintFunctionLibrary):

    def SendTextToDebugHUD(self, WorldContextObject: unreal.UObject, Text: str, Color: core_uobject.LinearColor, TextSize: int, Duration: float): ...
    def PlayFullScreenMovie(self, GbxPC: gbx_game_system_core.GbxPlayerController, MediaSource: media_assets.MediaSource, bPlayOnceAndDestroy: bool, ReturnValue: GbxFullScreenMovie) -> GbxFullScreenMovie: ...
    def AbbreviateNumberText(self, ValueToFormat: float, ReturnValue: str) -> str: ...


class GbxUIGlobals(gbx_runtime.GbxDataAsset):
    InputToGlyphMap: GbxInputToGlyphMap
    PlatformToGlyphMap: GbxPlatformToGlyphMap
    DefaultPlatformGlyphHeight: float
    DialogBoxTemplates: GbxDialogBoxData
    DefaultListItemFactory: GbxListItemFactory
    FullScreenMovieWidget: unreal.UClass
    FullScreenMediaPlayer: media_assets.MediaPlayer
    PersistentWidgetGroups: unreal.WrappedArray[GbxHUDData]
    MaxWidgetLoadTimePerFrameInMs: float
    GFxContextualMenuTemplate: GbxGFxContextualMenuData
    MarkupStartCharacter: str
    MarkupEndCharacter: str
    DefaultGlyphSize: core_uobject.Vector2D
    GlyphMarkupStartCharacter: str
    GlyphMarkupEndCharacter: str
    AlwaysLoadedGFxMenus: unreal.WrappedArray[GbxMenuData]
    HintGlyphVSpace: int



class GbxUmgMenuData(GbxMenuData):
    MenuClass: unreal.UClass
    ListItemFactory: GbxListItemFactory



class GbxCascadingList(GbxUserWidget):
    DefaultListItemClass: unreal.UClass
    ListViews: unreal.WrappedArray[GbxGridListWidget]
    ActiveList: GbxGridListWidget
    NavigationStack: unreal.WrappedArray[GbxCascadingListItemData]
    def SetActiveList(self, List: GbxGridListWidget): ...
    def PushItems(self, Items: unreal.WrappedArray[GbxCascadingListItemData]): ...
    def Pop(self): ...
    def OnShiftListsForward(self): ...
    def OnShiftListsBack(self): ...
    def OnItemSelected_Internal(self, Item: GbxListItem): ...
    def OnItemClicked_Internal(self, Item: GbxListItem): ...
    def HasItems(self, ReturnValue: bool) -> bool: ...
    def GetStackDepth(self, ReturnValue: int) -> int: ...
    def Clear(self): ...


class GbxComboBoxDropdownMenu(GbxUmgMenu):
    ChoiceListArray: unreal.WrappedArray[GbxComboBoxItemInfo]
    ChoiceListContainer: umg.Widget
    ChoiceList: GbxGridListWidget
    ComboBoxOwner: GbxComboBox
    def OnChoiceClicked(self, ListItem: GbxListItem): ...
    def DismissWithoutChanging(self): ...


class GbxComboBox(GbxListItem):
    DropdownMenuClass: unreal.UClass
    DropdownMenuOffset: core_uobject.Vector2D
    ChoiceListArray: unreal.WrappedArray[GbxComboBoxItemInfo]
    CurrentChoiceReferenceIndex: int
    LastKnownGeometry: slate_core.Geometry
    def OnComboBoxClicked(self, Widget: GbxUserWidget, InputInfo: GbxMenuInputEvent): ...
    def GetCurentChoiceReferenceIndex(self, ReturnValue: int) -> int: ...


class GbxCoreDialogBoxHelpers(engine.BlueprintFunctionLibrary):

    def ShowYesNoDialog(self, pc: gbx_game_system_core.GbxPlayerController, HeaderText: str, MessageText: str, bAnyUserCanInteract: bool, ReturnValue: GbxDialogBox) -> GbxDialogBox: ...
    def ShowOkayDialog(self, pc: gbx_game_system_core.GbxPlayerController, HeaderText: str, MessageText: str, bAnyUserCanInteract: bool, Template: EGbxDialogBoxHelpersDialogTemplate, ReturnValue: GbxDialogBox) -> GbxDialogBox: ...
    def ShowDialog(self, pc: gbx_game_system_core.GbxPlayerController, DialogBoxInfo: GbxDialogBoxInfo, ReturnValue: GbxDialogBox) -> GbxDialogBox: ...
    def ShowConfirmCancelDialog(self, pc: gbx_game_system_core.GbxPlayerController, HeaderText: str, MessageText: str, bAnyUserCanInteract: bool, ReturnValue: GbxDialogBox) -> GbxDialogBox: ...
    def ShowBlockingDialog(self, pc: gbx_game_system_core.GbxPlayerController, HeaderText: str, MessageText: str, bBlocksAllUsers: bool, ReturnValue: GbxDialogBox) -> GbxDialogBox: ...


class GbxCrosshairDataAsset(gbx_runtime.GbxDataAsset):
    CrosshairFrameName: str
    CrosshairActorClass: unreal.UClass
    bHideMinSpreadReticle: bool
    bHideAccuracyReticle: bool
    ChargeClipState: EChargeClipState



class GbxMenuSwitcherMenuData(GbxUmgMenuData):
    Submenus: unreal.WrappedArray[GbxMenuSwitcherSubmenuInfo]



class GbxDebugMenuData(GbxMenuSwitcherMenuData): ...


class GbxMenuSwitcher(GbxUmgMenu):

    def SwitchToPage(self, SubMenuId: str): ...
    def PrevPage(self): ...
    def NextPage(self): ...
    def GetCurrentSubmenuId(self, ReturnValue: str) -> str: ...


class GbxDebugMenu(GbxMenuSwitcher):
    CategoryList: GbxGridListWidget
    CloseButton: umg.BUTTON
    SubmenuContainer: umg.PanelWidget
    HiddenSubmenus: unreal.WrappedArray[str]
    def OnCloseClicked(self): ...
    def OnCategorySelected(self, Widget: GbxUserWidget, InputInfo: GbxMenuInputEvent): ...


class GbxDebugRumbleMenu(GbxDebugMenuSubmenu):
    SliderStepSize: float
    ContentPanel: GbxScrollBoxList
    LeftLargeSlider: GbxListItemNumber
    LeftSmallSlider: GbxListItemNumber
    RightLargeSlider: GbxListItemNumber
    RightSmallSlider: GbxListItemNumber
    def OnSliderValueChanged(self, Item: GbxListItem): ...


class GbxDialogBoxData(GbxUmgMenuData):
    DialogInfo: GbxDialogBoxInfo
    Templates: unreal.WrappedArray[GbxDialogBoxTemplateMapItem]



class GbxDialogBox(GbxUmgMenu):
    bWantsToDismiss: bool
    HeaderText: str
    BodyText: str
    ChoiceList: GbxScrollBoxList
    def UpdateText(self, NewHeaderText: str, NewBodyText: str): ...
    def SetupDialog(self, DialogBoxInfo: GbxDialogBoxInfo): ...
    def SetHeaderTextFormatArg(self, ArgName: str, ReplacementText: str): ...
    def SetHeaderText(self, NewText: str, bClearFormatArgs: bool): ...
    def SetBodyTextFormatArg(self, ArgName: str, ReplacementText: str): ...
    def SetBodyText(self, NewText: str, bClearFormatArgs: bool): ...
    def OnChoiceClicked(self, ClickedItem: GbxListItem): ...
    def Dismiss(self): ...


class GbxDialogBoxChoiceWidget(GbxListItem):
    ChoiceNameId: str



class GbxDragDropContainerInterface(core_uobject.Interface): ...


class GbxFocusableWidgetStyleData(gbx_runtime.GbxDataAsset):
    Styles: unreal.WrappedArray[GbxFocusableWidgetItemStyle]
    DefaultFocusedStyle: GbxFocusableWidgetItemStyle
    DefaultNotFocusedStyle: GbxFocusableWidgetItemStyle



class GbxFocusableWidget(core_uobject.Interface):

    def SetFocusableWidgetEnabled(self, bEnabled: bool): ...
    def IsFocusableWidgetFocused(self, ReturnValue: bool) -> bool: ...
    def IsFocusableWidgetEnabled(self, ReturnValue: bool) -> bool: ...
    def GetFocusableWidgetState(self, ReturnValue: EGbxFocusableWidgetState) -> EGbxFocusableWidgetState: ...


class GbxFullScreenMovie(GbxUserWidget):
    CurrentPlayer: media_assets.MediaPlayer
    def OnMovieFinishedPlaying(self): ...


class GbxGFxContextualMenuData(GbxGFxMenuData):
    ContextualMenuInfo: ContextualMenuInfo



class GbxGFxContextualMenu(GbxGFxMenu):
    LocTable: unreal.WrappedArray[GbxGFxContextualMenuLocTableData]
    ContextualMenu: scaleform_ui.GFxObject
    ContentPanel: GbxGFxGridScrollingList
    ToolTipsTextField: GbxTextField
    RemoveFriendText: str
    AddShiftFriendText: str
    RemoveShiftFriendText: str
    BlockShiftUserText: str
    UnblockShiftUserText: str
    ReportShiftPlayerText: str
    def OnSelectionChanged(self, Item: GbxGFxListCell): ...
    def OnContextualMenuItemClicked(self, PressedButton: GbxGFxButton, InputInfo: GbxMenuInputEvent): ...


class GbxGFxContextualMenuHelpers(unreal.UObject): ...


class GbxGFxDragDropManager(unreal.UObject):

    def OnDropButtonUnhovered(self, UnhoveredButton: GbxGFxButton, InputInfo: GbxMenuInputEvent): ...
    def OnDropButtonHovered(self, HoveredButton: GbxGFxButton, InputInfo: GbxMenuInputEvent): ...


class GbxGFxDropDownList(GbxGFxObject):
    CurrentSelectionText: GbxTextField
    ListScrollBar: GbxGFxSlider
    DropDownButton: GbxGFxButton
    TopButton: GbxGFxButton
    DropDownListContainer: GbxGFxObject
    DropDownList: GbxGFxComboBoxScrollingList
    EntriesList: unreal.WrappedArray[str]
    CurrentlySelectedEntry: str
    def OnEntryClicked(self, BUTTON: GbxGFxButton, InputInfo: GbxMenuInputEvent): ...
    def OnDropDownButtonClicked(self, BUTTON: GbxGFxButton, InputInfo: GbxMenuInputEvent): ...


class GbxGFxComboBoxScrollingList(GbxGFxGridScrollingList): ...


class GbxGFxHintBarContainer(GbxGFxGridScrollingList):
    HintBarOwningBar: GbxHintBar
    HintBarOwnerPC: gbx_game_system_core.GbxPlayerController



class GbxGFxHintWidget(GbxGFxListCell):
    HintBarOwnerBar: GbxHintBar
    HintBarOwnerPC: gbx_game_system_core.GbxPlayerController
    HintBarHintInfo: GbxHintInfo
    HintText: GbxTextField
    HoldToPressBar: GbxGFxObject
    HoldToPressGamepad: GbxGFxProgressBar
    HoldToPressKeyboard: GbxGFxProgressBar
    HoldToPressKeyboardWide: GbxGFxProgressBar
    HoldToPressKeyboardXWide: GbxGFxProgressBar
    HintCaret: GbxGFxObject
    bHasInitialHintTextWidth: bool
    InitialHintTextWidth: float
    HoldToPressType: EHoldToPressGlyphType
    ManualPressToHoldProgress: float
    bHasBroadcastPressToHoldEvent: bool
    bIsHintVisible: bool
    bIsAvailable: bool
    bInputNeedsResetBeforeShowingProgress: bool
    ExternalHintHeldProgress: float
    def OnThisHintClicked(self, BUTTON: GbxGFxButton, InputInfo: GbxMenuInputEvent): ...


class GbxGFxListItemComboBox(GbxGFxListCellWithData):
    DropDownListItem: GbxGFxDropDownList
    def OnSelectionUpdated(self, Item: GbxGFxListCell): ...
    def OnOwningListSelectionChanged(self, Item: GbxGFxListCell): ...
    def OnDropDownButtonClicked(self): ...


class GbxGFxListItemControls(GbxGFxListCellWithData):
    TitleItem: GbxTextField
    BadBindingIcon: GbxGFxObject
    RebindButton: GbxGFxObject
    LinkedRebindButton: GbxGFxObject



class GbxGFxMediaPlayer(unreal.UObject):
    PlayerConfig: GbxGFxMediaPlayerConfig
    MaterialRenderer: GbxGFxMaterialRenderer
    MediaPlayer: media_assets.MediaPlayer
    def OnMovieTracksChanged(self): ...
    def OnMovieSeekCompleted(self): ...
    def OnMoviePlaybackSuspended(self): ...
    def OnMoviePlaybackResumed(self): ...
    def OnMovieMediaOpenFailed(self, FailedUrl: str): ...
    def OnMovieMediaOpened(self, OpenedUrl: str): ...
    def OnMovieMediaClosed(self): ...
    def OnMovieEndReached(self): ...
    def GbxGFxMediaPlayerEvent__DelegateSignature(self): ...


class GbxGFxMenuSwitcherNavCell(GbxGFxListCell):
    bOuterFocusedState: bool



class GbxGFxMenuSwitcherNavWidget(GbxGFxObject):
    PrevTabHintClip: GbxGFxHintWidget
    NextTabHintClip: GbxGFxHintWidget
    NavListClip: GbxGFxGridScrollingList
    NavType: EGbxGFxMenuSwitchNavWidgetType
    NavListSubmenuDatas: unreal.WrappedArray[GbxGFxMenuSwitcherSubmenuInfo]
    NavListItemDatas: unreal.WrappedArray[GbxGFxMenuSwitcherNavWidgetCustomItem]
    def OnTabClicked(self, BUTTON: GbxGFxButton, InputInfo: GbxMenuInputEvent): ...


class GbxGFxSprite(GbxGFxObject):
    Graphics: GbxGFxObject



class GbxGFxMouseBlocker(GbxGFxSprite):
    bIsBlocking: bool



class GbxGFxMouseCapturePanel(GbxGFxObject): ...


class GbxGFxRechargeableProgressBar(GbxGFxProgressBar): ...


class GbxGFxSlider(GbxGFxButton):
    SliderAcceleration: GbxGFxSliderAcceleration
    UpOrLeftButton: GbxGFxButton
    DownOrRightButton: GbxGFxButton
    SliderThumb: GbxGFxButton
    SliderTrack: GbxGFxButton
    SliderTrackButton: GbxGFxObject
    MaskFill: GbxGFxObject
    SliderDefaultThumb: GbxGFxObject
    def GbxGFxSliderUpdateEvent__DelegateSignature(self, SliderPercent: float): ...
    def EndSlide(self, BUTTON: GbxGFxButton, InputInfo: GbxMenuInputEvent): ...
    def BeginRightSlide(self, BUTTON: GbxGFxButton, InputInfo: GbxMenuInputEvent): ...
    def BeginLeftSlide(self, BUTTON: GbxGFxButton, InputInfo: GbxMenuInputEvent): ...


class GbxGridListWidget(umg.GridPanel):
    SelectedColumn: int
    SelectedRow: int
    SelectedIndexWhenFocusWasLost: int
    MenuThatOwnsFocus: GbxUmgMenu
    GridColumns: int
    GridRows: int
    GridFill: EGbxGridWidgetFill
    RowWrapMode: EGbxListWrapMode
    ColumnWrapMode: EGbxListWrapMode
    DefaultItemSelectionBehavior: EGbxFocusableWidgetMouseBehavior
    ListItemFactory: GbxListItemFactory
    DefaultListItemClass: unreal.UClass
    FocusChangeAction: EGbxListFocusChangedAction
    bRegisterAsFocusableWidget: bool
    FocusableWidgetNavUp: str
    FocusableWidgetNavDown: str
    FocusableWidgetNavLeft: str
    FocusableWidgetNavRight: str
    bFocusOnMenuCreation: bool



class GbxGuidePanel(umg.CanvasPanel): ...


class GbxHintBarWidgetContainer(core_uobject.Interface):

    def HintBarSetVisible(self, bVisible: bool): ...
    def HintBarInitOwnerInfo(self, HintBarOwner: GbxHintBar, PlayerControllerContext: gbx_game_system_core.GbxPlayerController): ...
    def HintBarClearAllHints(self): ...
    def HintBarAppendHint(self, HintInfo: GbxHintInfo): ...


class GbxHintBar(unreal.UObject):
    Container: unreal.UObject
    HintInfos: unreal.WrappedArray[GbxHintInfo]
    StagePlacedHints: unreal.WrappedArray[GbxHintWidgetMapItem]
    bAreHintsVisible: bool
    bIsInputBlocked: bool
    bHideOnOwnerMenuDeactivate: bool
    bSendInputActionEvenIfOwnerIsDeactivated: bool
    def OnHintClicked(self, InputAction: str, bHeld: bool): ...


class GbxHintWidget(core_uobject.Interface):

    def HintWidgetSetVisible(self, bVisible: bool): ...
    def HintWidgetSetInfo(self, HintInfo: GbxHintInfo): ...
    def HintWidgetInitOwnerInfo(self, HintBarOwner: GbxHintBar, PlayerControllerContext: gbx_game_system_core.GbxPlayerController): ...


class GbxHUDData(gbx_runtime.GbxDataAsset):
    ContainerClass: unreal.UClass
    Widgets: unreal.WrappedArray[GbxGFxHUDWidgetInfo]
    StandardLayout: GbxHUDLayoutData
    TwoPlayerHorizontalLayout: GbxHUDLayoutData
    TwoPlayerVerticalLayout: GbxHUDLayoutData
    FourPlayerLayout: GbxHUDLayoutData
    StandardLayoutGearUpMode: GbxHUDLayoutData
    TwoPlayerHorizontalLayoutGearUpMode: GbxHUDLayoutData
    TwoPlayerVerticalLayoutGearUpMode: GbxHUDLayoutData
    FourPlayerLayoutGearUpMode: GbxHUDLayoutData
    FeedbackData: GbxGFxHUDFeedbackData
    StartState: GbxHUDStateData



class HUDDataProviderInterface(core_uobject.Interface): ...


class GbxGFxHUDFeedbackData(gbx_game_system_core.GbxHUDFeedbackData): ...


class GbxHUDStateData(gbx_runtime.GbxDataAsset):
    StateName: str
    InitializationAnimSet: EHUDInitializationAnimationSet
    ListType: EGbxHUDStateListType
    StayOnTopOfStack: bool



class GbxList(core_uobject.Interface):

    def TryToAcquireMenuFocus(self, bFromMouse: bool): ...
    def SetSelectedItem(self, Item: GbxListItem, bScrollIntoView: bool, bAnimateScroll: bool): ...
    def SetSelectedIndex(self, NewSelection: int, bScrollIntoView: bool, bAnimateScroll: bool): ...
    def RemoveListItem(self, Item: GbxListItem): ...
    def RemoveAllListItems(self): ...
    def OnItemClicked(self, Item: GbxListItem): ...
    def MoveSelectionUp(self, ReturnValue: bool) -> bool: ...
    def MoveSelectionRight(self, ReturnValue: bool) -> bool: ...
    def MoveSelectionLeft(self, ReturnValue: bool) -> bool: ...
    def MoveSelectionDown(self, ReturnValue: bool) -> bool: ...
    def IsListFocused(self, ReturnValue: bool) -> bool: ...
    def IsListEnabled(self, ReturnValue: bool) -> bool: ...
    def InsertListItem(self, Item: GbxListItem): ...
    def GetSelectedItem(self, ReturnValue: GbxListItem) -> GbxListItem: ...
    def GetSelectedIndex(self, ReturnValue: int) -> int: ...
    def GetNumItemsInList(self, ReturnValue: int) -> int: ...
    def GetListItemFactory(self, ReturnValue: GbxListItemFactory) -> GbxListItemFactory: ...
    def GetItemAtIndex(self, Index: int, ReturnValue: GbxListItem) -> GbxListItem: ...
    def GetDefaultItemClass(self, ReturnValue: unreal.UClass) -> unreal.UClass: ...


class GbxListItemBoolean(GbxListItem):
    ValueCheckBox: umg.CheckBox
    def SetChecked(self, bChecked: bool): ...
    def IsChecked(self, ReturnValue: bool) -> bool: ...
    def HandleFocusableWidgetPressed(self, InputInfo: GbxMenuInputEvent): ...


class GbxListItemComboBox(GbxListItem):
    ValueComboBox: umg.ComboBoxString
    def SetSelectedOptionIndex(self, Index: int): ...
    def SelectPreviousOption(self): ...
    def SelectNextOption(self): ...
    def OnValueComboBoxChanged(self, SelectedItem: str, SelectionType: int): ...
    def ListItemComboBoxSelectionChangedDelegate__DelegateSignature(self, NewSelectedIndex: int): ...
    def InitializeComboBox(self, Items: unreal.WrappedArray[str], InitialValue: int): ...
    def GetSelectedOptionIndex(self, ReturnValue: int) -> int: ...


class GbxListItemFactory(engine.DataAsset):
    DefaultListItem: unreal.UClass
    BasicTextListItem: unreal.UClass
    BooleanListItem: unreal.UClass
    NumberListItem: unreal.UClass
    ComboBoxListItem: unreal.UClass



class GbxListItemNumber(GbxListItem):
    ValueSlider: umg.Slider
    def OnSliderValueChanged(self, NewPosition: float): ...
    def IncrementSlider(self): ...
    def GetCurrentValue(self, ReturnValue: float) -> float: ...
    def DecrementSlider(self): ...


class GbxMenu(core_uobject.Interface): ...


class GbxMenuInputSettings(unreal.UObject):
    KeyRepeatConfig: GbxMenuKeyRepeatInfo
    AxisAsButtonThreshold: float
    AxisThreshold: float
    ActionMappings: unreal.WrappedArray[GbxMenuInputAction]
    AxisMappings: unreal.WrappedArray[GbxMenuInputAxisAction]



class GbxMenuInput(unreal.UObject):
    bShowDebugKeyStates: bool
    FramesToIgnoreMouseMoves: int
    KeyRepeatConfig: GbxMenuKeyRepeatInfo
    AxisAsButtonThreshold: float
    AxisThreshold: float
    ActionMappings: unreal.WrappedArray[GbxMenuInputAction]
    AxisMappings: unreal.WrappedArray[GbxMenuInputAxisAction]
    MousePoses: unreal.WrappedArray[GbxMenuInputRawMousePos]



class GbxMenuInputListener(core_uobject.Interface): ...


class GbxMenuStackMenuInfo(gbx_game_system_core.BaseMenuStackMenuInfo):
    MenuData: GbxMenuData



class GbxMenuStack(unreal.UObject):
    PCOwner: gbx_game_system_core.GbxPlayerController
    MenuInput: GbxMenuInput
    MenuStack: unreal.WrappedArray[GbxMenuStackMenuInfo]
    MenuDeleteList: unreal.WrappedArray[GbxMenuStackMenuInfo]
    QueuedInputActions: unreal.WrappedArray[GbxMenuInputEvent]
    UnpairedInputCache: unreal.WrappedArray[GbxMenuInputEvent]
    QueuedAxisInputActions: unreal.WrappedArray[GbxMenuAxisInputEvent]
    PopupMenus: unreal.WrappedArray[GbxMenuStackMenuInfo]
    PriorityBase: int
    PriorityDelta: int
    PopupMenuPriorityBase: int
    bStackHasChanged: bool
    bIsTicking: bool
    bIsDoingMenuInit: bool
    bIsDoingMenuDeinit: bool
    bIsDoingMenuDeactivate: bool
    AxisAsButtonThreshold: float
    CurrentInputDevice: EGbxMenuInputDevice
    bLastInputFromMouse: bool
    BlockAllRawInput: int
    bIsProcessingInput: bool
    bProcessingInputCancelled: bool
    bStackHidden: bool
    PassiveMenuLoadQueue: unreal.WrappedArray[GbxMenuData]
    PassiveLoadingMenu: GbxMenuStackMenuInfo
    CachedGameInstance: gbx_game_system_core.GbxGameInstance
    def Tick(self, DeltaTime: float): ...
    def SwitchTo(self, MenuData: GbxMenuData, ReturnValue: unreal.UObject) -> unreal.UObject: ...
    def SetBlockingMode(self, bShouldBlock: bool): ...
    def SetBlockAllRawInput(self, bShouldBlock: bool): ...
    def Push(self, MenuData: GbxMenuData, ReturnValue: unreal.UObject) -> unreal.UObject: ...
    def PopToSwitchTo(self, Menu: unreal.UObject, MenuData: GbxMenuData, ReturnValue: unreal.UObject) -> unreal.UObject: ...
    def PopTo(self, Menu: unreal.UObject): ...
    def Pop(self): ...
    def Num(self, ReturnValue: int) -> int: ...
    def HandleRawInput(self, Key: input_core.Key, EVENTTYPE: int, ControllerId: int): ...
    def GetTopMenu(self, ReturnValue: unreal.UObject) -> unreal.UObject: ...
    def GetMenuAtIndex(self, Index: int, ReturnValue: unreal.UObject) -> unreal.UObject: ...
    def GetIndexOfMenu(self, Menu: unreal.UObject, ReturnValue: int) -> int: ...
    def GetCurrentInputDevice(self, ReturnValue: EGbxMenuInputDevice) -> EGbxMenuInputDevice: ...
    def Draw(self): ...
    def Clear(self): ...


class GbxMeshWidget(umg.Widget):
    MeshData: umg.SlateVectorArtData
    MaxNumUnits: int



class GbxNoClipCanvasPanel(umg.CanvasPanel):
    ClipZoneAdjustmentMin: core_uobject.Vector2D
    ClipZoneAdjustmentMax: core_uobject.Vector2D



class GbxProgressBar(GbxUserWidget):
    FillTexture: engine.Texture2D
    bShowDeltaBar: bool
    DeltaTexture: engine.Texture2D
    DeltaEffectTexture: engine.Texture2D
    BackgroundTexture: engine.Texture2D
    FillDirection: EGbxProgressBarFillDirection
    Percent: float
    Shear: float
    DefaultInterpolator: GbxProgressBarInterpolator
    Ranges: unreal.WrappedArray[GbxProgressBarRange]
    Fill: umg.Image
    DeltaEffect: umg.Image
    Background: umg.Image
    CurrentValueText: umg.TextBlock
    MaxValueText: umg.TextBlock
    PercentAnimationOwner: GbxUserWidget
    PercentAnimation: umg.WidgetAnimation
    def SetShear(self, InShear: float): ...
    def SetPercent(self, InPercent: float): ...
    def SetMaxValueText(self, Text: str): ...
    def SetFillColorAndOpacity(self, InColor: core_uobject.LinearColor): ...
    def SetCurrentValueText(self, Text: str): ...
    def PassedPercentThreshold(self, Threshold: float, OldValue: float, CurrentValue: float, bIncreasing: bool, bDecreasing: bool, ReturnValue: bool) -> bool: ...
    def IsInterpolating(self, ReturnValue: bool) -> bool: ...
    def InterpolateToPercentWithInterpolator(self, InPercent: float, Interpolator: GbxProgressBarInterpolator): ...
    def InterpolateToPercent(self, InPercent: float): ...
    def HandleShowDeltaEffect(self, Effect: umg.Widget, OldValue: float, CurrentValue: float): ...
    def HandlePercentChanged(self, OldValue: float, CurrentValue: float, bIsInterpolating: bool, ActiveInterpolator: GbxProgressBarInterpolator): ...
    def HandleEnterPercentRange(self, RangeName: str): ...
    def GetShear(self, ReturnValue: float) -> float: ...
    def GetPercent(self, ReturnValue: float) -> float: ...
    def GbxProgressBarRangeEvent__DelegateSignature(self, RangeName: str): ...
    def GbxProgressBarEvent__DelegateSignature(self): ...
    def EnteredPercentRange(self, RangeMin: float, RangeMax: float, OldValue: float, CurrentValue: float, bIncreasing: bool, bDecreasing: bool, ReturnValue: bool) -> bool: ...


class GbxRetainerBox(umg.RetainerBox): ...


class GbxRichTextBlock(umg.RichTextBlock):
    Baseline: int
    ShadowOffset: core_uobject.Vector2D
    ShadowColorAndOpacity: core_uobject.LinearColor



class GbxScrollBoxList(umg.ScrollBox):
    SelectedIndex: int
    SelectedIndexWhenFocusWasLost: int
    MenuThatOwnsFocus: GbxUmgMenu
    WrapMode: EGbxScrollBoxListWrapMode
    DefaultItemSelectionBehavior: EGbxFocusableWidgetMouseBehavior
    ListItemFactory: GbxListItemFactory
    DefaultListItemClass: unreal.UClass
    FocusChangeAction: EGbxScrollBoxListFocusChangedAction
    bRegisterAsFocusableWidget: bool
    FocusableWidgetNavUp: str
    FocusableWidgetNavDown: str
    FocusableWidgetNavLeft: str
    FocusableWidgetNavRight: str
    bFocusOnMenuCreation: bool



class GbxSpinner(GbxGFxButton):
    LeftButton: GbxGFxButton
    RightButton: GbxGFxButton
    ChoiceText: GbxTextField
    def SpinRight(self, PressedButton: GbxGFxButton, InputInfo: GbxMenuInputEvent): ...
    def SpinnerValueUpdatedEvent__DelegateSignature(self): ...
    def SpinLeft(self, PressedButton: GbxGFxButton, InputInfo: GbxMenuInputEvent): ...


class GbxTextField(GbxGFxObject):
    ScrollBar: GbxGFxSlider
    def OnScrollBarPositionUpdated(self, SliderPercentage: float): ...


class UIAccessors(core_uobject.Interface): ...


class GbxUILocalization(engine.BlueprintFunctionLibrary):

    def PlatformToText(self, Platform: str, pc: gbx_game_system_core.GbxPlayerController, ReturnValue: str) -> str: ...
    def PlatformToRichText(self, Platform: str, pc: gbx_game_system_core.GbxPlayerController, GlyphSize: core_uobject.Vector2D, ReturnValue: str) -> str: ...
    def PlatformToGlyph(self, Platform: str, pc: gbx_game_system_core.GbxPlayerController, ReturnValue: slate_core.SlateBrush) -> slate_core.SlateBrush: ...
    def PlatformToGFxHTMLText(self, Platform: str, pc: gbx_game_system_core.GbxPlayerController, GlyphHeight: float, VSpace: int, ReturnValue: str) -> str: ...
    def IsPlatformGlyphAvailable(self, Platform: str, pc: gbx_game_system_core.GbxPlayerController, ReturnValue: bool) -> bool: ...
    def IsInputActionGlyphAvailable(self, ActionName: str, pc: gbx_game_system_core.GbxPlayerController, GlyphType: EGbxActionToTextType, ReturnValue: bool) -> bool: ...
    def InputActionToText(self, ActionName: str, pc: gbx_game_system_core.GbxPlayerController, GlyphType: EGbxActionToTextType, ReturnValue: str) -> str: ...
    def InputActionToRichText(self, ActionName: str, pc: gbx_game_system_core.GbxPlayerController, GlyphType: EGbxActionToTextType, GlyphSize: core_uobject.Vector2D, ReturnValue: str) -> str: ...
    def InputActionToGlyph(self, ActionName: str, pc: gbx_game_system_core.GbxPlayerController, GlyphType: EGbxActionToTextType, ReturnValue: slate_core.SlateBrush) -> slate_core.SlateBrush: ...
    def InputActionToGFxHTMLText(self, ActionName: str, pc: gbx_game_system_core.GbxPlayerController, GlyphType: EGbxActionToTextType, GlyphHeight: float, VSpace: int, ReturnValue: str) -> str: ...
    def FKeyToGFxHTMLText(self, Key: input_core.Key, pc: gbx_game_system_core.GbxPlayerController, GlyphType: EGbxActionToTextType, GlyphHeight: float, ReturnValue: str) -> str: ...


class GbxInputToGlyphMap(gbx_runtime.GbxDataAsset):
    InputMap: unreal.WrappedArray[GbxInputToGlyphMapItem]
    SpecialInputActionMap: unreal.WrappedArray[GbxInputToGlyphSpecialActionItem]



class GbxPlatformToGlyphMap(gbx_runtime.GbxDataAsset): ...


class GbxUISpinnerWidget(GbxUserWidget):
    SpinnerDisplayStrip: umg.CanvasPanel
    TotalDigitsDisplayed: int
    AnimationTime: float
    CurrentValue: int
    bTransitionUpwards: bool
    CurrentDistanceRemaining: float
    CurrentAnimSpeed: float
    NewValueToGoTo: int
    AnimationType: EGbxSpinnerWidgetGoToMethod
    def MoveToNumber(self, NewNumber: int, GoToMethod: EGbxSpinnerWidgetGoToMethod, ReturnValue: float) -> float: ...


class GbxWidgetComponent(umg.WidgetComponent):
    DistanceScaleCurve: engine.CurveFloat
    DistanceAlphaCurve: engine.CurveFloat
    DistanceAlphaBorder: umg.Border
    TrackedPlayerController: gbx_game_system_core.GbxPlayerController
    GbxWidget: GbxUserWidget
    def Setup(self, NewWidgetClass: unreal.UClass, NewTrackedPlayer: gbx_game_system_core.GbxPlayerController, ParentComponent: engine.SceneComponent, WidgetSpace: umg.EWidgetSpace, NewLayerZOrder: int, CollisionProfile: str): ...
    def SetDistanceScaleCurve(self, NewDistanceScaleCurve: engine.CurveFloat): ...
    def SetDistanceAlphaCurve(self, NewDistanceAlphaCurve: engine.CurveFloat): ...
    def SetDistanceAlphaBorder(self, NewDistanceAlphaBorder: umg.Border): ...


class GbxWidgetFocusManager(unreal.UObject):
    OwnerMenu: unreal.UObject
    FocusedWidget: unreal.UObject
    RegisteredWidgets: unreal.WrappedArray[GbxFocusableWidgetInfo]



class GbxWorldSpaceProxyWidget(GbxUserWidget):
    Depth: float
    Alignment: core_uobject.Vector2D
    def GetWorldLocation(self, ReturnValue: core_uobject.Vector) -> core_uobject.Vector: ...


class InWorldDamageNumber(GbxUserWidget):
    DisplayField: GbxRichTextBlock
    DisplayPanel: umg.CanvasPanel
    DamageAnimationPairings: unreal.WrappedArray[DamageAnimationPairing]
    InstigatingPlayer: gbx_game_system_core.GbxPlayerController
    DamageNumberContainer: umg.WidgetComponent
    def OnWentOffscreen(self): ...
    def ImpulseAnimationCompleted(self, AssociatedWidget: umg.UserWidget): ...


class GbxMenuInputEvent: ...


class GbxCascadingListItemData:
    ItemId: str
    Label: str
    bHasChildren: bool



class GbxGFxMaterialRenderer:
    Material: engine.MaterialInterface
    RenderTarget: engine.TextureRenderTarget2D
    OwningMovie: GbxGFxMovie



class GbxGFxMediaPlayerConfig:
    MediaPlayer: media_assets.MediaPlayer
    MediaData: gbx_game_system_core.GbxMediaData
    MediaMaterial: engine.MaterialInterface
    MediaDimensions: core_uobject.Vector2D
    ExternalTextureName: str



class GbxGFxMouseCapturePanelMouseButtonInfo: ...


class GbxGFxListCellUpdateInfo:
    Cell: GbxGFxListCell
    ListIndex: int
    bIsSelected: bool
    bIsNewSelection: bool
    bIsNewInView: bool



class GbxGFxSliderAcceleration:
    RepeatsNeededToAcclerate: int
    RepeatAdder: int
    MaxIncreases: int
    TimeToResetMouseWheelRepeat: float



class GbxProgressBarInterpolator:
    Delay: float
    Duration: float
    EasingFunc: gbx_game_system_core.GbxEasingFunc
    StartValue: float
    CurrentValue: float
    EndValue: float
    ElapsedTime: float
    DeltaEndOverride: float



class GbxProgressBarRange:
    Name: str
    Min: float
    Max: float
    bIncreasing: bool
    bDecreasing: bool



class GbxHUDStateManager:
    StateStack: unreal.WrappedArray[GbxHUDStateData]
    Widgets: unreal.WrappedArray[GbxGFxHUDWidget]



class GbxGFxAnchor:
    NormalizedPosition: core_uobject.Vector2D
    Offset: core_uobject.Vector2D
    Scale: core_uobject.Vector2D



class GbxGFxMovieClipAppendix:
    DefaultRetVal: GbxGFxmovieClipAppendixItem



class GbxGFxmovieClipAppendixItem:
    ClipPaths: unreal.WrappedArray[str]



class GbxFocusableWidgetAdjacencyInfo:
    WidgetUp: unreal.UObject
    WidgetDown: unreal.UObject
    WidgetLeft: unreal.UObject
    WidgetRight: unreal.UObject



class GbxGFxListConfig:
    ConfigType: EGbxGFxListConfigType
    ListOrientation: EGbxGFxListOrientation
    ListAlignment: EGbxGFxListAlignment
    FillSize: int
    VertCellSpacing: float
    HorzCellSpacing: float
    bAutoHideScrollBar: bool
    ScrollBarName: str
    WrapMode: EGbxGFxScrollListWrapMode
    DefaultItemSelectionBehavior: EGbxFocusableWidgetMouseBehavior
    FocusChangeAction: EGbxGFxScrollListFocusChangedAction
    bMustHaveOneFocusableCellToReceiveFocus: bool
    EntryPrefix: str
    GridAreaName: str
    GridMaskName: str
    FocusOrderPriority: EGbxGFxScrollListFocusOrderPriority
    AddedItemPriority: EGbxGFxScrollListAddedItemPriority
    bUseFixedCellBounds: bool
    FixedCellBoundsDemensions: core_uobject.Vector2D
    bMoveSelectionScrollIntoView: bool
    bMoveSelectionAnimateScroll: bool
    bKeepScrollbarOnTop: bool
    bAlwaysConsumeDirectionInput: bool
    bAllowScrolling: bool
    bReverseScrollDirection: bool
    DefaultItemSelectedAudioEventName: str
    DefaultItemClickedAudioEventName: str
    bCanBeNavigatedIfMouseDisabled: bool
    bFocusListIfCellGetsFocused: bool



class GbxGFxPooledGridListFullConfig:
    BaseListConfig: GbxGFxListConfig
    PoolListConfig: GbxGFxPooledGridListConfig



class GbxGFxPooledGridListConfig:
    ItemNativeClass: unreal.UClass
    ItemASClass: str
    ItemSize: core_uobject.Vector2D
    ItemRootOffset: core_uobject.Vector2D
    VisibleRows: int
    VisibleCols: int



class GbxFocusableWidgetAdjacencyNames:
    WidgetUpName: str
    WidgetDownName: str
    WidgetLeftName: str
    WidgetRightName: str



class GbxComboBoxItemInfo:
    DisplayName: str
    ReferenceIndex: int



class GbxDialogBoxTemplateMapItem:
    NameId: str
    DialogClass: unreal.UClass



class GbxDialogBoxInfo:
    HeaderText: str
    BodyText: str
    Choices: unreal.WrappedArray[GbxDialogBoxChoiceInfo]
    bCanCancel: bool
    bAnyUserCanInteract: bool
    TemplateNameId: str



class GbxDialogBoxChoiceInfo:
    LabelText: str
    ChoiceNameId: str
    bCloseDialogOnSelection: bool



class GbxFocusableWidgetItemStyle:
    State: EGbxFocusableWidgetState
    bUseTextColor: bool
    bUseTextSize: bool
    bUseIndicatorBrush: bool
    TextColor: slate_core.SlateColor
    TextSize: int
    IndicatorBrush: slate_core.SlateBrush



class GbxGFxContextualMenuLocTableData:
    Type: EContextualMenuEntryType
    ItemText: str
    FrameString: str



class ContextualMenuInfo: ...


class ContextualMenuEntryInfo: ...


class GbxScrollingListCellInfo:
    LibraryName: str
    CellClass: unreal.UClass
    Cell: GbxGFxListCell



class GbxGFxMenuSwitcherSubmenuInfo:
    MenuID: str
    MenuName: str
    MenuDescription: str
    MenuData: GbxGFxMenuData
    MenuData_NoCrossplay: GbxGFxMenuData
    MenuClass: unreal.UClass
    bAddToNav: bool



class GbxGFxMenuSwitcherNavWidgetCustomItem:
    ItemId: str
    IconFrameName: str
    TitleText: str
    bDisabled: bool



class UIEventAudioPairRow(engine.TableRowBase):
    WwiseSound: wwise_audio.WwiseEvent



class GbxGFxPooledGridPoolInfo:
    CellInfo: GbxScrollingListCellInfo
    OwningList: GbxGFxPooledGridList
    ListIndex: int
    VisibleIndexOffset: int



class GbxHintWidgetMapItem:
    InputActions: unreal.WrappedArray[str]
    bIsEnabled: bool
    HintWidget: unreal.UObject



class GbxHintInfo:
    InputActions: unreal.WrappedArray[str]
    HelpText: str
    bStagePlaced: bool
    StagePlacedWidget: unreal.UObject
    bClickable: bool
    bForceRefreshText: bool



class GbxHUDLayoutData:
    Layout: engine.DataTable
    Scale: float



class GbxHUDLayoutTableRow(engine.TableRowBase):
    AnchorPosition: core_uobject.Vector2D
    Offset: core_uobject.Vector2D
    Scale: core_uobject.Vector2D
    LibraryMovieString: str



class GbxGFxHUDWidgetInfo:
    WidgetClass: unreal.UClass
    InstanceString: str
    Priority: int



class GbxHUDFeedbackManager:
    FeedbackData: GbxGFxHUDFeedbackData
    Widgets: unreal.WrappedArray[GbxGFxMovie]
    OwningPlayer: gbx_game_system_core.GbxPlayerController
    OwningPawn: engine.Pawn
    OwningPlayerCameraManager: engine.PlayerCameraManager



class GbxMenuInputRawMousePos:
    PrevMousePos: core_uobject.Vector2D
    NewMousePos: core_uobject.Vector2D
    ControllerId: int
    IgnoreMouseMoveFrames: int



class GbxMenuInputAxisAction:
    ActionName: str
    Binds: unreal.WrappedArray[GbxMenuInputAxisBind]
    bTreatAsButtonPress: bool
    PositiveAxisAction: str
    NegativeAxisAction: str
    bWantsRepeat: bool



class GbxMenuInputAxisBind:
    Key: input_core.Key
    Scale: float



class GbxMenuInputAction:
    ActionName: str
    Keys: unreal.WrappedArray[input_core.Key]
    ActionTrigger: EGbxMenuInputActionTrigger
    bWantsRepeat: bool



class GbxMenuInputActionInfo:
    bIsHeld: bool
    bIsPressToHold: bool
    PressToHoldDuration: float
    PressToHoldProgress: float



class GbxMenuKeyRepeatInfo:
    InitialButtonRepeatDelay: float
    RepeatDelayStart: float
    RepeatDelayEnd: float
    RepeatDelayDelta: float
    HoldToPressDuration: float
    HoldToPressDurationLong: float



class GbxMenuAxisInputEvent: ...


class GbxDLCMenuSplitscreenLayouts:
    SoftVerticalLayout: core_uobject.SoftObjectPath
    SoftQuarterLayout: core_uobject.SoftObjectPath



class GbxMenuSplitscreenLayouts:
    QuarterLayoutPath: core_uobject.SoftObjectPath



class GbxMenuSwitcherSubmenuInfo:
    MenuID: str
    MenuName: str
    MenuData: GbxMenuData
    MenuClass: unreal.UClass



class TextMarkupDictionaryEntry:
    OutputText: str
    bRequiresEndSection: bool



class TextDebugData:
    DisplayText: str
    DisplayTime: float
    DisplaySize: int
    DisplayColor: core_uobject.LinearColor



class GbxInputToGlyphSpecialActionItem:
    InputAction: str
    KeyboardMouseGlyph: str
    PS4Glyph: str
    XboxOneGlyph: str
    DPXGlyph: str
    MPXGlyph: str
    GenericGamepadGlyph: str
    SwitchProGlyph: str
    StadiaGlyph: str
    KeyboardMouseGlyphBrush: slate_core.SlateBrush
    PS4GlyphBrush: slate_core.SlateBrush
    XboxOneGlyphBrush: slate_core.SlateBrush
    DPXGlyphBrush: slate_core.SlateBrush
    MPXGlyphBrush: slate_core.SlateBrush
    GenericGamepadGlyphBrush: slate_core.SlateBrush
    SwitchProGlyphBrush: slate_core.SlateBrush
    StadiaGlyphBrush: slate_core.SlateBrush



class GbxInputToGlyphMapItem:
    Key: input_core.Key
    KeyboardMouseGlyph: str
    PS4Glyph: str
    XboxOneGlyph: str
    DPXGlyph: str
    MPXGlyph: str
    GenericGamepadGlyph: str
    SwitchProGlyph: str
    StadiaGlyph: str
    KeyboardMouseGlyphBrush: slate_core.SlateBrush
    PS4GlyphBrush: slate_core.SlateBrush
    XboxOneGlyphBrush: slate_core.SlateBrush
    DPXGlyphBrush: slate_core.SlateBrush
    MPXGlyphBrush: slate_core.SlateBrush
    GenericGamepadGlyphBrush: slate_core.SlateBrush
    SwitchProGlyphBrush: slate_core.SlateBrush
    StadiaGlyphBrush: slate_core.SlateBrush



class GbxUIScroller:
    Acceleration: float
    ItemSize: float
    MaxVelocity: float
    MinVelocity: float
    bUseFixedVelocity: bool
    FixedVelocity: float
    ScrollPosition: float
    DesiredPosition: float
    WindowSize: float
    FullSize: float
    CurVelocity: float
    DesiredVelocity: float
    bHasMoved: bool
    bIsMoving: bool
    bHasSlowedDown: bool



class GbxFocusableWidgetInfo:
    Widget: unreal.UObject
    AdjacencyInfo: GbxFocusableWidgetAdjacencyInfo



class DamageAnimationPairing:
    DamageTypeFlag: gbx_game_system_core.ERecentDamageFlags
    LeftAnimations: unreal.WrappedArray[umg.WidgetAnimation]
    RightAnimations: unreal.WrappedArray[umg.WidgetAnimation]



class EGbxFocusableWidgetState(enum.Enum):
    Disabled = 0
    NotFocused_MouseDown = 1
    NotFocused = 2
    EGbxFocusableWidgetState_MAX = 3


class EGbxFocusableWidgetMouseBehavior(enum.Enum):
    SelectOnHover = 0
    SelectOnClick = 1
    EGbxFocusableWidgetMouseBehavior_MAX = 2


class EGbxGFxButtonType(enum.Enum):
    Checkbox = 0
    Radio = 1
    EGbxGFxButtonType_MAX = 2


class EGbxGFxButtonCheckedState(enum.Enum):
    Checked = 0
    EGbxGFxButtonCheckedState_MAX = 1


class EGbxGFxButtonLockedState(enum.Enum):
    Locked = 0
    EGbxGFxButtonLockedState_MAX = 1


class EMenuTransition(enum.Enum):
    MainMenu_OptionMenu = 0
    LoadCharacterMenu_MainMenu = 1
    MainMenu_LoadCharacterMenu = 2
    TitleScreen_FirstBoot = 3


class EGbxMenuInputDevice(enum.Enum):
    Gamepad = 0
    KeyboardMouse = 1


class EBindingType(enum.Enum):
    Driving = 0
    Common = 1


class EGbxProgressBarFillDirection(enum.Enum):
    RightToLeft = 0
    EGbxProgressBarFillDirection_MAX = 1


class EHUDInitializationAnimationSet(enum.Enum):
    InitialSet = 0
    AmmoBar = 1
    MissionTracker = 2


class EUIAudioSettingOperation(enum.Enum):
    Replace = 0
    Preserve = 1


class EGbxGFxListAlignment(enum.Enum):
    Right = 0
    Center = 1


class EGFxHUDWidgetAnchorType(enum.Enum):
    Crosshair = 0
    EGFxHUDWidgetAnchorType_MAX = 1


class EGbxDialogBoxHelpersDialogTemplate(enum.Enum):
    Warning = 0
    Error = 1


class EChargeClipState(enum.Enum):
    ACCURACYCLIP = 0
    SPREADCLIP = 1


class EContextualMenuEntryType(enum.Enum):
    SendItem = 0
    Join = 1
    Unfavorite = 2
    LootMode_Classic = 3
    KickOut = 4


class EContextualMenuExpandDirection(enum.Enum):
    Down = 0
    Up = 1


class EContextualMenuLayout(enum.Enum):
    MailMenuRecieved = 0
    MailMenuSendTo = 1


class GFxVirtualKeyboardType(enum.Enum):
    Password = 0
    Number = 1
    Web = 2


class EGbxGFxListConfigType(enum.Enum):
    PreserveLayout = 0
    EGbxGFxListConfigType_MAX = 1


class EGbxGFxScrollListAddedItemPriority(enum.Enum):
    OldestOnTop = 0
    EGbxGFxScrollListAddedItemPriority_MAX = 1


class EGbxGFxScrollListFocusOrderPriority(enum.Enum):
    LeaveUnchanged = 0
    EGbxGFxScrollListFocusOrderPriority_MAX = 1
    BringToFrontWithEverythingElseInOrder = 2


class EGFxHUDWidgetTransitionType(enum.Enum):
    Instant = 0
    EGFxHUDWidgetTransitionType_MAX = 1


class EGbxGFxListOrientation(enum.Enum):
    Horizontal = 0
    EGbxGFxListOrientation_MAX = 1


class EGbxGFxScrollListFocusChangedAction(enum.Enum):
    SelectNoneOnLossSelectFirstOnGain = 0
    SelectNoneOnLossRestorePreviousOnGain = 1


class EGbxGFxScrollListWrapMode(enum.Enum):
    Wrap = 0
    EGbxGFxScrollListWrapMode_MAX = 1


class EGbxGFxMenuSwitcherSubmenuInitReason(enum.Enum):
    Pushed = 0
    NextPage = 1
    Switched = 2


class EGbxGFxMenuSwitchNavWidgetType(enum.Enum):
    CustomSwitcher = 0
    MenuSwitcher = 1


class EEdgeFlashType(enum.Enum):
    InterpolatedDecreaseOnly = 0
    All = 1


class EGbxGFxSliderState(enum.Enum):
    ScrollingLeft = 0
    ScrollingRight = 1


class EGbxGFxSliderDirection(enum.Enum):
    Vertical = 0
    EGbxGFxSliderDirection_MAX = 1


class EGbxGridWidgetFill(enum.Enum):
    FillColumn = 0
    EGbxGridWidgetFill_MAX = 1


class EGbxHUDStateListType(enum.Enum):
    BlackList = 0
    EGbxHUDStateListType_MAX = 1


class EHUDStateManagerVisibility(enum.Enum):
    Visible = 0
    NotVisible = 1


class EGbxListFocusChangedAction(enum.Enum):
    SelectNoneOnLossSelectFirstOnGain = 0
    SelectNoneOnLossRestorePreviousOnGain = 1


class EGbxListWrapMode(enum.Enum):
    Wrap = 0
    EGbxListWrapMode_MAX = 1


class EGbxMenuInputMode(enum.Enum):
    AnyController = 0
    OwnerPlayer = 1
    OwnerPlayer_DontConsumeInput = 2


class EGbxMenuParentType(enum.Enum):
    PlayerScreen = 0
    Inherit = 1


class EGbxMenuInputActionTrigger(enum.Enum):
    Held = 0
    HeldLong = 1
    EGbxMenuInputActionTrigger_MAX = 2


class EGbxMenuSwitcherSubmenuInitReason(enum.Enum):
    Pushed = 0
    NextPage = 1
    Switched = 2


class EMenuTransitionOperation(enum.Enum):
    Invalid = 0
    Pop = 1
    EMenuTransitionOperation_MAX = 2


class EGbxScrollBoxListFocusChangedAction(enum.Enum):
    SelectNoneOnLossSelectFirstOnGain = 0
    SelectNoneOnLossRestorePreviousOnGain = 1


class EGbxScrollBoxListWrapMode(enum.Enum):
    EGbxScrollBoxListWrapMode_MAX = 0
    Wrap = 1


class EVerticalTextAutoSizeType(enum.Enum):
    center = 0
    top = 1
    EVerticalTextAutoSizeType_MAX = 2


class EHoldToPressGlyphType(enum.Enum):
    KeyboardXWide = 0
    Gamepad = 1
    Keyboard = 2


class EGbxInputGlyphType(enum.Enum):
    PS4 = 0
    SwitchPro = 1
    XboxOne = 2
    EGbxInputGlyphType_MAX = 3


class EGbxActionToTextType(enum.Enum):
    Gamepad = 0
    KeyboardMouse = 1


class EGbxSpinnerWidgetGoToMethod(enum.Enum):
    Immediately = 0
    EGbxSpinnerWidgetGoToMethod_MAX = 1

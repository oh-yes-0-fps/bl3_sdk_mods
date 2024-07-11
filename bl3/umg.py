from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import movie_scene
from . import input_core
from . import slate_core
from . import slate
from . import movie_scene_tracks
from . import property_path


class Visual(unreal.UObject): ...


class Widget(Visual):
    Slot: PanelSlot
    bIsEnabledDelegate: Any
    ToolTipText: str
    ToolTipTextDelegate: Any
    ToolTipWidget: Widget
    ToolTipWidgetDelegate: Any
    VisibilityDelegate: Any
    RenderTransform: WidgetTransform
    RenderTransformPivot: core_uobject.Vector2D
    bIsVariable: bool
    bCreatedByConstructionScript: bool
    bIsEnabled: bool
    bOverride_Cursor: bool
    bIsVolatile: bool
    Cursor: int
    Clipping: slate_core.EWidgetClipping
    Visibility: ESlateVisibility
    RenderOpacity: float
    Navigation: WidgetNavigation
    NativeBindings: unreal.WrappedArray[PropertyBinding]

    def SetVisibility(self, InVisibility: ESlateVisibility): ...
    def SetUserFocus(self, PlayerController: engine.PlayerController): ...
    def SetToolTipText(self, InToolTipText: str): ...
    def SetToolTip(self, Widget: Widget): ...
    def SetRenderTranslation(self, Translation: core_uobject.Vector2D): ...
    def SetRenderTransformPivot(self, Pivot: core_uobject.Vector2D): ...
    def SetRenderTransform(self, InTransform: WidgetTransform): ...
    def SetRenderShear(self, Shear: core_uobject.Vector2D): ...
    def SetRenderScale(self, Scale: core_uobject.Vector2D): ...
    def SetRenderOpacity(self, InOpacity: float): ...
    def SetRenderAngle(self, Angle: float): ...
    def SetNavigationRule(
        self,
        Direction: slate_core.EUINavigation,
        Rule: slate_core.EUINavigationRule,
        WidgetToFocus: str,
    ): ...
    def SetKeyboardFocus(self): ...
    def SetIsEnabled(self, bInIsEnabled: bool): ...
    def SetCursor(self, InCursor: int): ...
    def SetClipping(self, InClipping: slate_core.EWidgetClipping): ...
    def SetAllNavigationRules(
        self, Rule: slate_core.EUINavigationRule, WidgetToFocus: str
    ): ...
    def ResetCursor(self): ...
    def RemoveFromParent(self): ...
    def OnReply__DelegateSignature(self) -> EventReply: ...
    def OnPointerEvent__DelegateSignature(
        self, MyGeometry: slate_core.Geometry, MouseEvent: slate_core.PointerEvent
    ) -> EventReply: ...
    def IsVisible(self) -> bool: ...
    def IsHovered(self) -> bool: ...
    def InvalidateLayoutAndVolatility(self): ...
    def HasUserFocusedDescendants(
        self, PlayerController: engine.PlayerController
    ) -> bool: ...
    def HasUserFocus(self, PlayerController: engine.PlayerController) -> bool: ...
    def HasMouseCaptureByUser(self, UserIndex: int, PointerIndex: int) -> bool: ...
    def HasMouseCapture(self) -> bool: ...
    def HasKeyboardFocus(self) -> bool: ...
    def HasFocusedDescendants(self) -> bool: ...
    def HasAnyUserFocus(self) -> bool: ...
    def GetWidget__DelegateSignature(self) -> Widget: ...
    def GetVisibility(self) -> ESlateVisibility: ...
    def GetText__DelegateSignature(self) -> str: ...
    def GetSlateVisibility__DelegateSignature(self) -> ESlateVisibility: ...
    def GetSlateColor__DelegateSignature(self) -> slate_core.SlateColor: ...
    def GetSlateBrush__DelegateSignature(self) -> slate_core.SlateBrush: ...
    def GetRenderOpacity(self) -> float: ...
    def GetParent(self) -> PanelWidget: ...
    def GetOwningPlayer(self) -> engine.PlayerController: ...
    def GetOwningLocalPlayer(self) -> engine.LocalPlayer: ...
    def GetMouseCursor__DelegateSignature(self) -> int: ...
    def GetLinearColor__DelegateSignature(self) -> core_uobject.LinearColor: ...
    def GetIsEnabled(self) -> bool: ...
    def GetInt32__DelegateSignature(self) -> int: ...
    def GetFloat__DelegateSignature(self) -> float: ...
    def GetDesiredSize(self) -> core_uobject.Vector2D: ...
    def GetClipping(self) -> slate_core.EWidgetClipping: ...
    def GetCheckBoxState__DelegateSignature(self) -> slate_core.ECheckBoxState: ...
    def GetCachedGeometry(self) -> slate_core.Geometry: ...
    def GetBool__DelegateSignature(self) -> bool: ...
    def GenerateWidgetForString__DelegateSignature(self, Item: str) -> Widget: ...
    def GenerateWidgetForObject__DelegateSignature(
        self, Item: unreal.UObject
    ) -> Widget: ...
    def ForceVolatile(self, bForce: bool): ...
    def ForceLayoutPrepass(self): ...


class UserWidget(Widget):
    ColorAndOpacity: core_uobject.LinearColor
    ColorAndOpacityDelegate: Any
    ForegroundColor: slate_core.SlateColor
    ForegroundColorDelegate: Any
    Padding: slate_core.Margin
    ActiveSequencePlayers: unreal.WrappedArray[UMGSequencePlayer]
    StoppedSequencePlayers: unreal.WrappedArray[UMGSequencePlayer]
    NamedSlotBindings: unreal.WrappedArray[NamedSlotBinding]
    WidgetTree: WidgetTree
    Priority: int
    bSupportsKeyboardFocus: bool
    bIsFocusable: bool
    bStopAction: bool
    bHasScriptImplementedTick: bool
    bHasScriptImplementedPaint: bool
    bCookedWidgetTree: bool
    TickFrequency: EWidgetTickFrequency
    InputComponent: engine.InputComponent

    def UnregisterInputComponent(self): ...
    def Tick(self, MyGeometry: slate_core.Geometry, InDeltaTime: float): ...
    def StopListeningForInputAction(self, ActionName: str, EVENTTYPE: int): ...
    def StopListeningForAllInputActions(self): ...
    def StopAnimationsAndLatentActions(self): ...
    def StopAnimation(self, InAnimation: WidgetAnimation): ...
    def StopAllAnimations(self): ...
    def SetPositionInViewport(
        self, Position: core_uobject.Vector2D, bRemoveDPIScale: bool
    ): ...
    def SetPlaybackSpeed(self, InAnimation: WidgetAnimation, PlaybackSpeed: float): ...
    def SetPadding(self, InPadding: slate_core.Margin): ...
    def SetOwningPlayer(self, LocalPlayerController: engine.PlayerController): ...
    def SetNumLoopsToPlay(self, InAnimation: WidgetAnimation, NumLoopsToPlay: int): ...
    def SetInputActionPriority(self, NewPriority: int): ...
    def SetInputActionBlocking(self, bShouldBlock: bool): ...
    def SetForegroundColor(self, InForegroundColor: slate_core.SlateColor): ...
    def SetDesiredSizeInViewport(self, Size: core_uobject.Vector2D): ...
    def SetColorAndOpacity(self, InColorAndOpacity: core_uobject.LinearColor): ...
    def SetAnchorsInViewport(self, Anchors: slate.Anchors): ...
    def SetAlignmentInViewport(self, Alignment: core_uobject.Vector2D): ...
    def ReverseAnimation(self, InAnimation: WidgetAnimation): ...
    def RemoveFromViewport(self): ...
    def RegisterInputComponent(self): ...
    def PreConstruct(self, IsDesignTime: bool): ...
    def PlaySound(self, SoundToPlay: engine.SoundBase): ...
    def PlayAnimationTo(
        self,
        InAnimation: WidgetAnimation,
        StartAtTime: float,
        EndAtTime: float,
        NumLoopsToPlay: int,
        PlayMode: int,
        PlaybackSpeed: float,
    ): ...
    def PlayAnimation(
        self,
        InAnimation: WidgetAnimation,
        StartAtTime: float,
        NumLoopsToPlay: int,
        PlayMode: int,
        PlaybackSpeed: float,
    ): ...
    def PauseAnimation(self, InAnimation: WidgetAnimation) -> float: ...
    def OnTouchStarted(
        self, MyGeometry: slate_core.Geometry, InTouchEvent: slate_core.PointerEvent
    ) -> EventReply: ...
    def OnTouchMoved(
        self, MyGeometry: slate_core.Geometry, InTouchEvent: slate_core.PointerEvent
    ) -> EventReply: ...
    def OnTouchGesture(
        self, MyGeometry: slate_core.Geometry, GestureEvent: slate_core.PointerEvent
    ) -> EventReply: ...
    def OnTouchEnded(
        self, MyGeometry: slate_core.Geometry, InTouchEvent: slate_core.PointerEvent
    ) -> EventReply: ...
    def OnRemovedFromFocusPath(self, InFocusEvent: slate_core.FocusEvent): ...
    def OnPreviewMouseButtonDown(
        self, MyGeometry: slate_core.Geometry, MouseEvent: slate_core.PointerEvent
    ) -> EventReply: ...
    def OnPreviewKeyDown(
        self, MyGeometry: slate_core.Geometry, InKeyEvent: slate_core.KeyEvent
    ) -> EventReply: ...
    def OnPaint(self, Context: PaintContext): ...
    def OnMouseWheel(
        self, MyGeometry: slate_core.Geometry, MouseEvent: slate_core.PointerEvent
    ) -> EventReply: ...
    def OnMouseMove(
        self, MyGeometry: slate_core.Geometry, MouseEvent: slate_core.PointerEvent
    ) -> EventReply: ...
    def OnMouseLeave(self, MouseEvent: slate_core.PointerEvent): ...
    def OnMouseEnter(
        self, MyGeometry: slate_core.Geometry, MouseEvent: slate_core.PointerEvent
    ): ...
    def OnMouseCaptureLost(self): ...
    def OnMouseButtonUp(
        self, MyGeometry: slate_core.Geometry, MouseEvent: slate_core.PointerEvent
    ) -> EventReply: ...
    def OnMouseButtonDown(
        self, MyGeometry: slate_core.Geometry, MouseEvent: slate_core.PointerEvent
    ) -> EventReply: ...
    def OnMouseButtonDoubleClick(
        self, InMyGeometry: slate_core.Geometry, InMouseEvent: slate_core.PointerEvent
    ) -> EventReply: ...
    def OnMotionDetected(
        self, MyGeometry: slate_core.Geometry, InMotionEvent: slate_core.MotionEvent
    ) -> EventReply: ...
    def OnKeyUp(
        self, MyGeometry: slate_core.Geometry, InKeyEvent: slate_core.KeyEvent
    ) -> EventReply: ...
    def OnKeyDown(
        self, MyGeometry: slate_core.Geometry, InKeyEvent: slate_core.KeyEvent
    ) -> EventReply: ...
    def OnKeyChar(
        self,
        MyGeometry: slate_core.Geometry,
        InCharacterEvent: slate_core.CharacterEvent,
    ) -> EventReply: ...
    def OnFocusReceived(
        self, MyGeometry: slate_core.Geometry, InFocusEvent: slate_core.FocusEvent
    ) -> EventReply: ...
    def OnFocusLost(self, InFocusEvent: slate_core.FocusEvent): ...
    def OnDrop(
        self,
        MyGeometry: slate_core.Geometry,
        PointerEvent: slate_core.PointerEvent,
        Operation: DragDropOperation,
    ) -> bool: ...
    def OnDragOver(
        self,
        MyGeometry: slate_core.Geometry,
        PointerEvent: slate_core.PointerEvent,
        Operation: DragDropOperation,
    ) -> bool: ...
    def OnDragLeave(
        self, PointerEvent: slate_core.PointerEvent, Operation: DragDropOperation
    ): ...
    def OnDragEnter(
        self,
        MyGeometry: slate_core.Geometry,
        PointerEvent: slate_core.PointerEvent,
        Operation: DragDropOperation,
    ): ...
    def OnDragDetected(
        self,
        MyGeometry: slate_core.Geometry,
        PointerEvent: slate_core.PointerEvent,
        Operation: DragDropOperation,
    ): ...
    def OnDragCancelled(
        self, PointerEvent: slate_core.PointerEvent, Operation: DragDropOperation
    ): ...
    def OnAnimationStarted(self, Animation: WidgetAnimation): ...
    def OnAnimationFinished(self, Animation: WidgetAnimation): ...
    def OnAnalogValueChanged(
        self,
        MyGeometry: slate_core.Geometry,
        InAnalogInputEvent: slate_core.AnalogInputEvent,
    ) -> EventReply: ...
    def OnAddedToFocusPath(self, InFocusEvent: slate_core.FocusEvent): ...
    def ListenForInputAction(
        self, ActionName: str, EVENTTYPE: int, bConsume: bool, Callback: Any
    ): ...
    def IsPlayingAnimation(self) -> bool: ...
    def IsListeningForInputAction(self, ActionName: str) -> bool: ...
    def IsInViewport(self) -> bool: ...
    def IsInteractable(self) -> bool: ...
    def IsAnyAnimationPlaying(self) -> bool: ...
    def IsAnimationPlayingForward(self, InAnimation: WidgetAnimation) -> bool: ...
    def IsAnimationPlaying(self, InAnimation: WidgetAnimation) -> bool: ...
    def GetOwningPlayerPawn(self) -> engine.Pawn: ...
    def GetIsVisible(self) -> bool: ...
    def GetAnimationCurrentTime(self, InAnimation: WidgetAnimation) -> float: ...
    def GetAnchorsInViewport(self) -> slate.Anchors: ...
    def GetAlignmentInViewport(self) -> core_uobject.Vector2D: ...
    def Destruct(self): ...
    def Construct(self): ...
    def CancelLatentActions(self): ...
    def AddToViewport(self, ZOrder: int): ...
    def AddToPlayerScreen(self, ZOrder: int) -> bool: ...


class AsyncTaskDownloadImage(engine.BlueprintAsyncActionBase):
    OnSuccess: Any
    OnFail: Any

    def DownloadImage(self, URL: str) -> AsyncTaskDownloadImage: ...


class PanelWidget(Widget):
    Slots: unreal.WrappedArray[PanelSlot]

    def RemoveChildAt(self, Index: int) -> bool: ...
    def RemoveChild(self, Content: Widget) -> bool: ...
    def HasChild(self, Content: Widget) -> bool: ...
    def HasAnyChildren(self) -> bool: ...
    def GetChildrenCount(self) -> int: ...
    def GetChildIndex(self, Content: Widget) -> int: ...
    def GetChildAt(self, Index: int) -> Widget: ...
    def ClearChildren(self): ...
    def AddChild(self, Content: Widget) -> PanelSlot: ...


class ContentWidget(PanelWidget):

    def SetContent(self, Content: Widget) -> PanelSlot: ...
    def GetContentSlot(self) -> PanelSlot: ...
    def GetContent(self) -> Widget: ...


class BackgroundBlur(ContentWidget):
    Padding: slate_core.Margin
    HorizontalAlignment: int
    VerticalAlignment: int
    bApplyAlphaToBlur: bool
    BlurStrength: float
    bOverrideAutoRadiusCalculation: bool
    BlurRadius: int
    LowQualityFallbackBrush: slate_core.SlateBrush

    def SetVerticalAlignment(self, InVerticalAlignment: int): ...
    def SetPadding(self, InPadding: slate_core.Margin): ...
    def SetLowQualityFallbackBrush(self, InBrush: slate_core.SlateBrush): ...
    def SetHorizontalAlignment(self, InHorizontalAlignment: int): ...
    def SetBlurStrength(self, InStrength: float): ...
    def SetBlurRadius(self, InBlurRadius: int): ...
    def SetApplyAlphaToBlur(self, bInApplyAlphaToBlur: bool): ...


class PanelSlot(Visual):
    Parent: PanelWidget
    Content: Widget


class BackgroundBlurSlot(PanelSlot):
    Padding: slate_core.Margin
    HorizontalAlignment: int
    VerticalAlignment: int

    def SetVerticalAlignment(self, InVerticalAlignment: int): ...
    def SetPadding(self, InPadding: slate_core.Margin): ...
    def SetHorizontalAlignment(self, InHorizontalAlignment: int): ...


class PropertyBinding(unreal.UObject):
    SourceObject: unreal.UObject
    SourcePath: DynamicPropertyPath
    DestinationProperty: str


class BoolBinding(PropertyBinding):

    def GetValue(self) -> bool: ...


class Border(ContentWidget):
    HorizontalAlignment: int
    VerticalAlignment: int
    bShowEffectWhenDisabled: bool
    ContentColorAndOpacity: core_uobject.LinearColor
    ContentColorAndOpacityDelegate: Any
    Padding: slate_core.Margin
    Background: slate_core.SlateBrush
    BackgroundDelegate: Any
    BrushColor: core_uobject.LinearColor
    BrushColorDelegate: Any
    DesiredSizeScale: core_uobject.Vector2D
    OnMouseButtonDownEvent: Any
    OnMouseButtonUpEvent: Any
    OnMouseMoveEvent: Any
    OnMouseDoubleClickEvent: Any

    def SetVerticalAlignment(self, InVerticalAlignment: int): ...
    def SetPadding(self, InPadding: slate_core.Margin): ...
    def SetHorizontalAlignment(self, InHorizontalAlignment: int): ...
    def SetDesiredSizeScale(self, InScale: core_uobject.Vector2D): ...
    def SetContentColorAndOpacity(
        self, InContentColorAndOpacity: core_uobject.LinearColor
    ): ...
    def SetBrushFromTexture(self, Texture: engine.Texture2D): ...
    def SetBrushFromMaterial(self, Material: engine.MaterialInterface): ...
    def SetBrushFromAsset(self, Asset: engine.SlateBrushAsset): ...
    def SetBrushColor(self, InBrushColor: core_uobject.LinearColor): ...
    def SetBrush(self, InBrush: slate_core.SlateBrush): ...
    def GetDynamicMaterial(self) -> engine.MaterialInstanceDynamic: ...


class BorderSlot(PanelSlot):
    Padding: slate_core.Margin
    HorizontalAlignment: int
    VerticalAlignment: int

    def SetVerticalAlignment(self, InVerticalAlignment: int): ...
    def SetPadding(self, InPadding: slate_core.Margin): ...
    def SetHorizontalAlignment(self, InHorizontalAlignment: int): ...


class BrushBinding(PropertyBinding):

    def GetValue(self) -> slate_core.SlateBrush: ...


class BUTTON(ContentWidget):
    Style: slate_core.SlateWidgetStyleAsset
    WidgetStyle: slate_core.ButtonStyle
    ColorAndOpacity: core_uobject.LinearColor
    BackgroundColor: core_uobject.LinearColor
    ClickMethod: int
    TouchMethod: int
    PressMethod: int
    IsFocusable: bool
    OnClicked: Any
    OnPressed: Any
    OnReleased: Any
    OnHovered: Any
    OnUnhovered: Any

    def SetTouchMethod(self, InTouchMethod: int): ...
    def SetStyle(self, InStyle: slate_core.ButtonStyle): ...
    def SetPressMethod(self, InPressMethod: int): ...
    def SetColorAndOpacity(self, InColorAndOpacity: core_uobject.LinearColor): ...
    def SetClickMethod(self, InClickMethod: int): ...
    def SetBackgroundColor(self, InBackgroundColor: core_uobject.LinearColor): ...
    def IsPressed(self) -> bool: ...


class ButtonSlot(PanelSlot):
    Padding: slate_core.Margin
    HorizontalAlignment: int
    VerticalAlignment: int

    def SetVerticalAlignment(self, InVerticalAlignment: int): ...
    def SetPadding(self, InPadding: slate_core.Margin): ...
    def SetHorizontalAlignment(self, InHorizontalAlignment: int): ...


class CanvasPanel(PanelWidget):

    def AddChildToCanvas(self, Content: Widget) -> CanvasPanelSlot: ...


class CanvasPanelSlot(PanelSlot):
    LayoutData: AnchorData
    bAutoSize: bool
    ZOrder: int

    def SetZOrder(self, InZOrder: int): ...
    def SetSize(self, InSize: core_uobject.Vector2D): ...
    def SetPosition(self, InPosition: core_uobject.Vector2D): ...
    def SetOffsets(self, InOffset: slate_core.Margin): ...
    def SetMinimum(self, InMinimumAnchors: core_uobject.Vector2D): ...
    def SetMaximum(self, InMaximumAnchors: core_uobject.Vector2D): ...
    def SetLayout(self, InLayoutData: AnchorData): ...
    def SetAutoSize(self, InbAutoSize: bool): ...
    def SetAnchors(self, InAnchors: slate.Anchors): ...
    def SetAlignment(self, InAlignment: core_uobject.Vector2D): ...
    def GetZOrder(self) -> int: ...
    def GetSize(self) -> core_uobject.Vector2D: ...
    def GetPosition(self) -> core_uobject.Vector2D: ...
    def GetOffsets(self) -> slate_core.Margin: ...
    def GetLayout(self) -> AnchorData: ...
    def GetAutoSize(self) -> bool: ...
    def GetAnchors(self) -> slate.Anchors: ...
    def GetAlignment(self) -> core_uobject.Vector2D: ...


class CheckBox(ContentWidget):
    CheckedState: slate_core.ECheckBoxState
    CheckedStateDelegate: Any
    WidgetStyle: slate_core.CheckBoxStyle
    Style: slate_core.SlateWidgetStyleAsset
    UncheckedImage: engine.SlateBrushAsset
    UncheckedHoveredImage: engine.SlateBrushAsset
    UncheckedPressedImage: engine.SlateBrushAsset
    CheckedImage: engine.SlateBrushAsset
    CheckedHoveredImage: engine.SlateBrushAsset
    CheckedPressedImage: engine.SlateBrushAsset
    UndeterminedImage: engine.SlateBrushAsset
    UndeterminedHoveredImage: engine.SlateBrushAsset
    UndeterminedPressedImage: engine.SlateBrushAsset
    HorizontalAlignment: int
    Padding: slate_core.Margin
    BorderBackgroundColor: slate_core.SlateColor
    IsFocusable: bool
    OnCheckStateChanged: Any

    def SetIsChecked(self, InIsChecked: bool): ...
    def SetCheckedState(self, InCheckedState: slate_core.ECheckBoxState): ...
    def IsPressed(self) -> bool: ...
    def IsChecked(self) -> bool: ...
    def GetCheckedState(self) -> slate_core.ECheckBoxState: ...


class CheckedStateBinding(PropertyBinding):

    def GetValue(self) -> slate_core.ECheckBoxState: ...


class CircularThrobber(Widget):
    NumberOfPieces: int
    Period: float
    Radius: float
    PieceImage: engine.SlateBrushAsset
    Image: slate_core.SlateBrush
    bEnableRadius: bool

    def SetRadius(self, InRadius: float): ...
    def SetPeriod(self, InPeriod: float): ...
    def SetNumberOfPieces(self, InNumberOfPieces: int): ...


class ColorBinding(PropertyBinding):

    def GetSlateValue(self) -> slate_core.SlateColor: ...
    def GetLinearValue(self) -> core_uobject.LinearColor: ...


class ComboBox(Widget):
    Items: unreal.WrappedArray[unreal.UObject]
    OnGenerateWidgetEvent: Any
    bIsFocusable: bool


class ComboBoxString(Widget):
    DefaultOptions: unreal.WrappedArray[str]
    SelectedOption: str
    WidgetStyle: slate_core.ComboBoxStyle
    ItemStyle: slate_core.TableRowStyle
    ContentPadding: slate_core.Margin
    MaxListHeight: float
    HasDownArrow: bool
    EnableGamepadNavigationMode: bool
    Font: slate_core.SlateFontInfo
    ForegroundColor: slate_core.SlateColor
    bIsFocusable: bool
    OnGenerateWidgetEvent: Any
    OnSelectionChanged: Any
    OnOpening: Any

    def SetSelectedOptionByIndex(self, Index: int): ...
    def SetSelectedOption(self, Option: str): ...
    def RemoveOption(self, Option: str) -> bool: ...
    def RefreshOptions(self): ...
    def OnSelectionChangedEvent__DelegateSignature(
        self, SelectedItem: str, SelectionType: int
    ): ...
    def OnOpeningEvent__DelegateSignature(self): ...
    def GetSelectedOptionIndex(self) -> int: ...
    def GetSelectedOption(self) -> str: ...
    def GetOptionCount(self) -> int: ...
    def GetOptionAtIndex(self, Index: int) -> str: ...
    def FindOptionIndex(self, Option: str) -> int: ...
    def ClearSelection(self): ...
    def ClearOptions(self): ...
    def AddOption(self, Option: str): ...


class DragDropOperation(unreal.UObject):
    Tag: str
    Payload: unreal.UObject
    DefaultDragVisual: Widget
    Pivot: EDragPivot
    Offset: core_uobject.Vector2D
    OnDrop: Any
    OnDragCancelled: Any
    OnDragged: Any

    def Drop(self, PointerEvent: slate_core.PointerEvent): ...
    def Dragged(self, PointerEvent: slate_core.PointerEvent): ...
    def DragCancelled(self, PointerEvent: slate_core.PointerEvent): ...


class DynamicEntryBox(Widget):
    EntryBoxType: EDynamicBoxType
    EntrySpacing: core_uobject.Vector2D
    SpacingPattern: unreal.WrappedArray[core_uobject.Vector2D]
    EntrySizeRule: SlateChildSize
    EntryHorizontalAlignment: int
    EntryVerticalAlignment: int
    MaxElementSize: int
    EntryWidgetClass: unreal.UClass

    def SetEntrySpacing(self, InEntrySpacing: core_uobject.Vector2D): ...
    def Reset(self, bDeleteWidgets: bool): ...
    def RemoveEntry(self, EntryWidget: UserWidget): ...
    def GetNumEntries(self) -> int: ...
    def GetAllEntries(self) -> unreal.WrappedArray[UserWidget]: ...
    def BP_CreateEntry(self) -> UserWidget: ...


class EditableText(Widget):
    Text: str
    TextDelegate: Any
    HintText: str
    HintTextDelegate: Any
    WidgetStyle: slate_core.EditableTextStyle
    Style: slate_core.SlateWidgetStyleAsset
    BackgroundImageSelected: engine.SlateBrushAsset
    BackgroundImageComposing: engine.SlateBrushAsset
    CaretImage: engine.SlateBrushAsset
    Font: slate_core.SlateFontInfo
    ColorAndOpacity: slate_core.SlateColor
    IsReadOnly: bool
    IsPassword: bool
    MinimumDesiredWidth: float
    IsCaretMovedWhenGainFocus: bool
    SelectAllTextWhenFocused: bool
    RevertTextOnEscape: bool
    ClearKeyboardFocusOnCommit: bool
    SelectAllTextOnCommit: bool
    AllowContextMenu: bool
    KeyboardType: int
    VirtualKeyboardOptions: slate.VirtualKeyboardOptions
    VirtualKeyboardDismissAction: slate.EVirtualKeyboardDismissAction
    Justification: int
    ShapedTextOptions: ShapedTextOptions
    OnTextChanged: Any
    OnTextCommitted: Any

    def SetText(self, InText: str): ...
    def SetIsReadOnly(self, InbIsReadyOnly: bool): ...
    def SetIsPassword(self, InbIsPassword: bool): ...
    def SetHintText(self, InHintText: str): ...
    def OnEditableTextCommittedEvent__DelegateSignature(
        self, Text: str, CommitMethod: int
    ): ...
    def OnEditableTextChangedEvent__DelegateSignature(self, Text: str): ...
    def GetText(self) -> str: ...


class EditableTextBox(Widget):
    Text: str
    TextDelegate: Any
    WidgetStyle: slate_core.EditableTextBoxStyle
    Style: slate_core.SlateWidgetStyleAsset
    HintText: str
    HintTextDelegate: Any
    Font: slate_core.SlateFontInfo
    ForegroundColor: core_uobject.LinearColor
    BackgroundColor: core_uobject.LinearColor
    ReadOnlyForegroundColor: core_uobject.LinearColor
    IsReadOnly: bool
    IsPassword: bool
    MinimumDesiredWidth: float
    Padding: slate_core.Margin
    IsCaretMovedWhenGainFocus: bool
    SelectAllTextWhenFocused: bool
    RevertTextOnEscape: bool
    ClearKeyboardFocusOnCommit: bool
    SelectAllTextOnCommit: bool
    AllowContextMenu: bool
    KeyboardType: int
    VirtualKeyboardOptions: slate.VirtualKeyboardOptions
    VirtualKeyboardDismissAction: slate.EVirtualKeyboardDismissAction
    Justification: int
    ShapedTextOptions: ShapedTextOptions
    OnTextChanged: Any
    OnTextCommitted: Any

    def SetText(self, InText: str): ...
    def SetIsReadOnly(self, bReadOnly: bool): ...
    def SetIsPassword(self, bIsPassword: bool): ...
    def SetHintText(self, InText: str): ...
    def SetError(self, InError: str): ...
    def OnEditableTextBoxCommittedEvent__DelegateSignature(
        self, Text: str, CommitMethod: int
    ): ...
    def OnEditableTextBoxChangedEvent__DelegateSignature(self, Text: str): ...
    def HasError(self) -> bool: ...
    def GetText(self) -> str: ...
    def ClearError(self): ...


class ExpandableArea(Widget):
    Style: slate_core.ExpandableAreaStyle
    BorderBrush: slate_core.SlateBrush
    BorderColor: slate_core.SlateColor
    bIsExpanded: bool
    MaxHeight: float
    HeaderPadding: slate_core.Margin
    AreaPadding: slate_core.Margin
    OnExpansionChanged: Any
    HeaderContent: Widget
    BodyContent: Widget

    def SetIsExpanded_Animated(self, IsExpanded: bool): ...
    def SetIsExpanded(self, IsExpanded: bool): ...
    def GetIsExpanded(self) -> bool: ...


class FloatBinding(PropertyBinding):

    def GetValue(self) -> float: ...


class GridPanel(PanelWidget):
    ColumnFill: unreal.WrappedArray[float]
    RowFill: unreal.WrappedArray[float]

    def SetRowFill(self, ColumnIndex: int, Coefficient: float): ...
    def SetColumnFill(self, ColumnIndex: int, Coefficient: float): ...
    def AddChildToGrid(self, Content: Widget) -> GridSlot: ...


class GridSlot(PanelSlot):
    Padding: slate_core.Margin
    HorizontalAlignment: int
    VerticalAlignment: int
    Row: int
    RowSpan: int
    Column: int
    ColumnSpan: int
    Layer: int
    Nudge: core_uobject.Vector2D

    def SetVerticalAlignment(self, InVerticalAlignment: int): ...
    def SetRowSpan(self, InRowSpan: int): ...
    def SetRow(self, InRow: int): ...
    def SetPadding(self, InPadding: slate_core.Margin): ...
    def SetLayer(self, InLayer: int): ...
    def SetHorizontalAlignment(self, InHorizontalAlignment: int): ...
    def SetColumnSpan(self, InColumnSpan: int): ...
    def SetColumn(self, InColumn: int): ...


class HorizontalBox(PanelWidget):

    def AddChildToHorizontalBox(self, Content: Widget) -> HorizontalBoxSlot: ...


class HorizontalBoxSlot(PanelSlot):
    Padding: slate_core.Margin
    Size: SlateChildSize
    HorizontalAlignment: int
    VerticalAlignment: int

    def SetVerticalAlignment(self, InVerticalAlignment: int): ...
    def SetSize(self, InSize: SlateChildSize): ...
    def SetPadding(self, InPadding: slate_core.Margin): ...
    def SetHorizontalAlignment(self, InHorizontalAlignment: int): ...


class Image(Widget):
    Brush: slate_core.SlateBrush
    BrushDelegate: Any
    ColorAndOpacity: core_uobject.LinearColor
    ColorAndOpacityDelegate: Any
    OnMouseButtonDownEvent: Any

    def SetOpacity(self, InOpacity: float): ...
    def SetColorAndOpacity(self, InColorAndOpacity: core_uobject.LinearColor): ...
    def SetBrushTintColor(self, TintColor: slate_core.SlateColor): ...
    def SetBrushSize(self, DesiredSize: core_uobject.Vector2D): ...
    def SetBrushFromTextureDynamic(
        self, Texture: engine.Texture2DDynamic, bMatchSize: bool
    ): ...
    def SetBrushFromTexture(self, Texture: engine.Texture2D, bMatchSize: bool): ...
    def SetBrushFromMaterial(self, Material: engine.MaterialInterface): ...
    def SetBrushFromAtlasInterface(self, AtlasRegion: Any, bMatchSize: bool): ...
    def SetBrushFromAsset(self, Asset: engine.SlateBrushAsset): ...
    def SetBrush(self, InBrush: slate_core.SlateBrush): ...
    def GetDynamicMaterial(self) -> engine.MaterialInstanceDynamic: ...


class InputKeySelector(Widget):
    WidgetStyle: slate_core.ButtonStyle
    TextStyle: slate_core.TextBlockStyle
    SelectedKey: slate.InputChord
    Font: slate_core.SlateFontInfo
    Margin: slate_core.Margin
    ColorAndOpacity: core_uobject.LinearColor
    KeySelectionText: str
    NoKeySpecifiedText: str
    bAllowModifierKeys: bool
    bAllowGamepadKeys: bool
    EscapeKeys: unreal.WrappedArray[input_core.Key]
    OnKeySelected: Any
    OnIsSelectingKeyChanged: Any

    def SetTextBlockVisibility(self, InVisibility: ESlateVisibility): ...
    def SetSelectedKey(self, InSelectedKey: slate.InputChord): ...
    def SetNoKeySpecifiedText(self, InNoKeySpecifiedText: str): ...
    def SetKeySelectionText(self, InKeySelectionText: str): ...
    def SetEscapeKeys(self, InKeys: unreal.WrappedArray[input_core.Key]): ...
    def SetAllowModifierKeys(self, bInAllowModifierKeys: bool): ...
    def SetAllowGamepadKeys(self, bInAllowGamepadKeys: bool): ...
    def OnKeySelected__DelegateSignature(self, SelectedKey: slate.InputChord): ...
    def OnIsSelectingKeyChanged__DelegateSignature(self): ...
    def GetIsSelectingKey(self) -> bool: ...


class Int32Binding(PropertyBinding):

    def GetValue(self) -> int: ...


class InvalidationBox(ContentWidget):
    bCanCache: bool
    CacheRelativeTransforms: bool

    def SetCanCache(self, CanCache: bool): ...
    def InvalidateCache(self): ...
    def GetCanCache(self) -> bool: ...


class NativeUserListEntry(core_uobject.Interface):

    def IsListItemSelected(self) -> bool: ...
    def IsListItemExpanded(self) -> bool: ...


class UserListEntry(NativeUserListEntry):

    def BP_OnItemSelectionChanged(self, bIsSelected: bool): ...
    def BP_OnItemExpansionChanged(self, bIsExpanded: bool): ...
    def BP_OnEntryReleased(self): ...


class UserObjectListEntry(UserListEntry):

    def OnListItemObjectSet(self, ListItemObject: unreal.UObject): ...
    def GetListItemObject(self) -> unreal.UObject: ...


class ListViewBase(Widget):
    EntryWidgetClass: unreal.UClass
    BP_OnEntryGenerated: Any
    BP_OnEntryReleased: Any

    def ScrollToTop(self): ...
    def ScrollToBottom(self): ...
    def RegenerateAllEntries(self): ...
    def GetDisplayedEntryWidgets(self) -> unreal.WrappedArray[UserWidget]: ...


class ListView(ListViewBase):
    SelectionMode: int
    ConsumeMouseWheel: slate_core.EConsumeMouseWheel
    bClearSelectionOnClick: bool
    EntrySpacing: float
    ListItems: unreal.WrappedArray[unreal.UObject]
    BP_OnItemClicked: Any
    BP_OnItemDoubleClicked: Any
    BP_OnItemIsHoveredChanged: Any
    BP_OnItemSelectionChanged: Any
    BP_OnItemScrolledIntoView: Any

    def SetSelectionMode(self, SelectionMode: int): ...
    def SetSelectedIndex(self, Index: int): ...
    def ScrollIndexIntoView(self, Index: int): ...
    def NavigateToIndex(self, Index: int): ...
    def IsRefreshPending(self) -> bool: ...
    def GetNumItems(self) -> int: ...
    def GetListItems(self) -> unreal.WrappedArray[unreal.UObject]: ...
    def GetItemAt(self, Index: int) -> unreal.UObject: ...
    def GetIndexForItem(self, Item: unreal.UObject) -> int: ...
    def ClearListItems(self): ...
    def BP_SetSelectedItem(self, Item: unreal.UObject): ...
    def BP_SetListItems(self, InListItems: unreal.WrappedArray[unreal.UObject]): ...
    def BP_SetItemSelection(self, Item: unreal.UObject, bSelected: bool): ...
    def BP_ScrollItemIntoView(self, Item: unreal.UObject): ...
    def BP_NavigateToItem(self, Item: unreal.UObject): ...
    def BP_IsItemVisible(self, Item: unreal.UObject) -> bool: ...
    def BP_GetSelectedItems(
        self, Items: unreal.WrappedArray[unreal.UObject]
    ) -> bool: ...
    def BP_GetSelectedItem(self) -> unreal.UObject: ...
    def BP_GetNumItemsSelected(self) -> int: ...
    def BP_ClearSelection(self): ...
    def BP_CancelScrollIntoView(self): ...
    def AddItem(self, Item: unreal.UObject): ...


class ListViewDesignerPreviewItem(unreal.UObject): ...


class MenuAnchor(ContentWidget):
    MenuClass: unreal.UClass
    OnGetMenuContentEvent: Any
    Placement: int
    ShouldDeferPaintingAfterWindowContent: bool
    UseApplicationMenuStack: bool
    OnMenuOpenChanged: Any

    def ToggleOpen(self, bFocusOnOpen: bool): ...
    def ShouldOpenDueToClick(self) -> bool: ...
    def Open(self, bFocusMenu: bool): ...
    def IsOpen(self) -> bool: ...
    def HasOpenSubMenus(self) -> bool: ...
    def GetMenuPosition(self) -> core_uobject.Vector2D: ...
    def Close(self): ...


class MouseCursorBinding(PropertyBinding):

    def GetValue(self) -> int: ...


class MovieScene2DTransformSection(movie_scene.MovieSceneSection):
    TransformMask: MovieScene2DTransformMask
    Translation: movie_scene.MovieSceneFloatChannel
    Rotation: movie_scene.MovieSceneFloatChannel
    Scale: movie_scene.MovieSceneFloatChannel
    Shear: movie_scene.MovieSceneFloatChannel


class MovieScene2DTransformTrack(movie_scene_tracks.MovieScenePropertyTrack): ...


class MovieSceneMarginSection(movie_scene.MovieSceneSection):
    TopCurve: movie_scene.MovieSceneFloatChannel
    LeftCurve: movie_scene.MovieSceneFloatChannel
    RightCurve: movie_scene.MovieSceneFloatChannel
    BottomCurve: movie_scene.MovieSceneFloatChannel


class MovieSceneMarginTrack(movie_scene_tracks.MovieScenePropertyTrack): ...


class MovieSceneWidgetMaterialTrack(movie_scene_tracks.MovieSceneMaterialTrack):
    BrushPropertyNamePath: unreal.WrappedArray[str]
    TrackName: str


class TextLayoutWidget(Widget):
    ShapedTextOptions: ShapedTextOptions
    Justification: int
    WrappingPolicy: slate.ETextWrappingPolicy
    AutoWrapText: bool
    WrapTextAt: float
    Margin: slate_core.Margin
    LineHeightPercentage: float


class MultiLineEditableText(TextLayoutWidget):
    Text: str
    HintText: str
    HintTextDelegate: Any
    WidgetStyle: slate_core.TextBlockStyle
    bIsReadOnly: bool
    Font: slate_core.SlateFontInfo
    SelectAllTextWhenFocused: bool
    ClearTextSelectionOnFocusLoss: bool
    RevertTextOnEscape: bool
    ClearKeyboardFocusOnCommit: bool
    AllowContextMenu: bool
    VirtualKeyboardOptions: slate.VirtualKeyboardOptions
    VirtualKeyboardDismissAction: slate.EVirtualKeyboardDismissAction
    OnTextChanged: Any
    OnTextCommitted: Any

    def SetText(self, InText: str): ...
    def SetIsReadOnly(self, bReadOnly: bool): ...
    def OnMultiLineEditableTextCommittedEvent__DelegateSignature(
        self, Text: str, CommitMethod: int
    ): ...
    def OnMultiLineEditableTextChangedEvent__DelegateSignature(self, Text: str): ...
    def GetText(self) -> str: ...


class MultiLineEditableTextBox(TextLayoutWidget):
    Text: str
    HintText: str
    HintTextDelegate: Any
    WidgetStyle: slate_core.EditableTextBoxStyle
    TextStyle: slate_core.TextBlockStyle
    bIsReadOnly: bool
    AllowContextMenu: bool
    VirtualKeyboardOptions: slate.VirtualKeyboardOptions
    VirtualKeyboardDismissAction: slate.EVirtualKeyboardDismissAction
    Style: slate_core.SlateWidgetStyleAsset
    Font: slate_core.SlateFontInfo
    ForegroundColor: core_uobject.LinearColor
    BackgroundColor: core_uobject.LinearColor
    ReadOnlyForegroundColor: core_uobject.LinearColor
    OnTextChanged: Any
    OnTextCommitted: Any

    def SetText(self, InText: str): ...
    def SetIsReadOnly(self, bReadOnly: bool): ...
    def SetError(self, InError: str): ...
    def OnMultiLineEditableTextBoxCommittedEvent__DelegateSignature(
        self, Text: str, CommitMethod: int
    ): ...
    def OnMultiLineEditableTextBoxChangedEvent__DelegateSignature(self, Text: str): ...
    def GetText(self) -> str: ...


class NamedSlot(ContentWidget): ...


class NamedSlotInterface(core_uobject.Interface): ...


class NativeWidgetHost(Widget): ...


class Overlay(PanelWidget):

    def AddChildToOverlay(self, Content: Widget) -> OverlaySlot: ...


class OverlaySlot(PanelSlot):
    Padding: slate_core.Margin
    HorizontalAlignment: int
    VerticalAlignment: int

    def SetVerticalAlignment(self, InVerticalAlignment: int): ...
    def SetPadding(self, InPadding: slate_core.Margin): ...
    def SetHorizontalAlignment(self, InHorizontalAlignment: int): ...


class ProgressBar(Widget):
    WidgetStyle: slate_core.ProgressBarStyle
    Style: slate_core.SlateWidgetStyleAsset
    BackgroundImage: engine.SlateBrushAsset
    FillImage: engine.SlateBrushAsset
    MarqueeImage: engine.SlateBrushAsset
    Percent: float
    BarFillType: int
    bIsMarquee: bool
    BorderPadding: core_uobject.Vector2D
    PercentDelegate: Any
    FillColorAndOpacity: core_uobject.LinearColor
    FillColorAndOpacityDelegate: Any

    def SetPercent(self, InPercent: float): ...
    def SetIsMarquee(self, InbIsMarquee: bool): ...
    def SetFillColorAndOpacity(self, InColor: core_uobject.LinearColor): ...


class RetainerBox(ContentWidget):
    RenderOnInvalidation: bool
    RenderOnPhase: bool
    Phase: int
    PhaseCount: int
    EffectMaterial: engine.MaterialInterface
    TextureParameter: str

    def SetTextureParameter(self, TextureParameter: str): ...
    def SetRenderingPhase(self, RenderPhase: int, TotalPhases: int): ...
    def SetEffectMaterial(self, EffectMaterial: engine.MaterialInterface): ...
    def RequestRender(self): ...
    def GetEffectMaterial(self) -> engine.MaterialInstanceDynamic: ...


class RichTextBlock(TextLayoutWidget):
    Text: str
    TextStyleSet: engine.DataTable
    DecoratorClasses: unreal.WrappedArray[unreal.UClass]
    InstanceDecorators: unreal.WrappedArray[RichTextBlockDecorator]

    def SetText(self, InText: str): ...
    def SetColorAndOpacity(self, InColorAndOpacity: slate_core.SlateColor): ...
    def GetText(self) -> str: ...
    def GetDecoratorByClass(
        self, DecoratorClass: unreal.UClass
    ) -> RichTextBlockDecorator: ...


class RichTextBlockDecorator(unreal.UObject): ...


class RichTextBlockImageDecorator(RichTextBlockDecorator):
    ImageSet: engine.DataTable


class SafeZone(ContentWidget):
    PadLeft: bool
    PadRight: bool
    PadTop: bool
    PadBottom: bool

    def SetSidesToPad(
        self, InPadLeft: bool, InPadRight: bool, InPadTop: bool, InPadBottom: bool
    ): ...


class SafeZoneSlot(PanelSlot):
    bIsTitleSafe: bool
    SafeAreaScale: slate_core.Margin
    HAlign: int
    VAlign: int
    Padding: slate_core.Margin


class ScaleBox(ContentWidget):
    Stretch: int
    StretchDirection: int
    UserSpecifiedScale: float
    IgnoreInheritedScale: bool
    bSingleLayoutPass: bool

    def SetUserSpecifiedScale(self, InUserSpecifiedScale: float): ...
    def SetStretchDirection(self, InStretchDirection: int): ...
    def SetStretch(self, InStretch: int): ...
    def SetIgnoreInheritedScale(self, bInIgnoreInheritedScale: bool): ...


class ScaleBoxSlot(PanelSlot):
    Padding: slate_core.Margin
    HorizontalAlignment: int
    VerticalAlignment: int

    def SetVerticalAlignment(self, InVerticalAlignment: int): ...
    def SetPadding(self, InPadding: slate_core.Margin): ...
    def SetHorizontalAlignment(self, InHorizontalAlignment: int): ...


class ScrollBar(Widget):
    WidgetStyle: slate_core.ScrollBarStyle
    Style: slate_core.SlateWidgetStyleAsset
    bAlwaysShowScrollbar: bool
    Orientation: int
    Thickness: core_uobject.Vector2D

    def SetState(self, InOffsetFraction: float, InThumbSizeFraction: float): ...


class ScrollBox(PanelWidget):
    WidgetStyle: slate_core.ScrollBoxStyle
    WidgetBarStyle: slate_core.ScrollBarStyle
    Style: slate_core.SlateWidgetStyleAsset
    BarStyle: slate_core.SlateWidgetStyleAsset
    Orientation: int
    ScrollBarVisibility: ESlateVisibility
    ConsumeMouseWheel: slate_core.EConsumeMouseWheel
    ScrollbarThickness: core_uobject.Vector2D
    AlwaysShowScrollbar: bool
    AllowOverscroll: bool
    NavigationDestination: slate.EDescendantScrollDestination
    NavigationScrollPadding: float
    bAllowRightClickDragScrolling: bool
    OnUserScrolled: Any

    def SetScrollOffset(self, NewScrollOffset: float): ...
    def SetScrollBarVisibility(self, NewScrollBarVisibility: ESlateVisibility): ...
    def SetScrollbarThickness(self, NewScrollbarThickness: core_uobject.Vector2D): ...
    def SetOrientation(self, NewOrientation: int): ...
    def SetAlwaysShowScrollbar(self, NewAlwaysShowScrollbar: bool): ...
    def SetAllowOverscroll(self, NewAllowOverscroll: bool): ...
    def ScrollWidgetIntoView(
        self,
        WidgetToFind: Widget,
        AnimateScroll: bool,
        ScrollDestination: slate.EDescendantScrollDestination,
    ): ...
    def ScrollToStart(self): ...
    def ScrollToEnd(self): ...
    def GetViewOffsetFraction(self) -> float: ...
    def GetScrollOffset(self) -> float: ...
    def GetPhysicalScrollOffset(self) -> float: ...


class ScrollBoxSlot(PanelSlot):
    Padding: slate_core.Margin
    HorizontalAlignment: int
    VerticalAlignment: int

    def SetVerticalAlignment(self, InVerticalAlignment: int): ...
    def SetPadding(self, InPadding: slate_core.Margin): ...
    def SetHorizontalAlignment(self, InHorizontalAlignment: int): ...


class SizeBox(ContentWidget):
    bOverride_WidthOverride: bool
    bOverride_HeightOverride: bool
    bOverride_MinDesiredWidth: bool
    bOverride_MinDesiredHeight: bool
    bOverride_MaxDesiredWidth: bool
    bOverride_MaxDesiredHeight: bool
    bOverride_MaxAspectRatio: bool
    WidthOverride: float
    HeightOverride: float
    MinDesiredWidth: float
    MinDesiredHeight: float
    MaxDesiredWidth: float
    MaxDesiredHeight: float
    MaxAspectRatio: float

    def SetWidthOverride(self, InWidthOverride: float): ...
    def SetMinDesiredWidth(self, InMinDesiredWidth: float): ...
    def SetMinDesiredHeight(self, InMinDesiredHeight: float): ...
    def SetMaxDesiredWidth(self, InMaxDesiredWidth: float): ...
    def SetMaxDesiredHeight(self, InMaxDesiredHeight: float): ...
    def SetMaxAspectRatio(self, InMaxAspectRatio: float): ...
    def SetHeightOverride(self, InHeightOverride: float): ...
    def ClearWidthOverride(self): ...
    def ClearMinDesiredWidth(self): ...
    def ClearMinDesiredHeight(self): ...
    def ClearMaxDesiredWidth(self): ...
    def ClearMaxDesiredHeight(self): ...
    def ClearMaxAspectRatio(self): ...
    def ClearHeightOverride(self): ...


class SizeBoxSlot(PanelSlot):
    Padding: slate_core.Margin
    HorizontalAlignment: int
    VerticalAlignment: int

    def SetVerticalAlignment(self, InVerticalAlignment: int): ...
    def SetPadding(self, InPadding: slate_core.Margin): ...
    def SetHorizontalAlignment(self, InHorizontalAlignment: int): ...


class SlateBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def ScreenToWidgetLocal(
        self,
        WorldContextObject: unreal.UObject,
        Geometry: slate_core.Geometry,
        ScreenPosition: core_uobject.Vector2D,
        LocalCoordinate: core_uobject.Vector2D,
    ): ...
    def ScreenToWidgetAbsolute(
        self,
        WorldContextObject: unreal.UObject,
        ScreenPosition: core_uobject.Vector2D,
        AbsoluteCoordinate: core_uobject.Vector2D,
    ): ...
    def ScreenToViewport(
        self,
        WorldContextObject: unreal.UObject,
        ScreenPosition: core_uobject.Vector2D,
        ViewportPosition: core_uobject.Vector2D,
    ): ...
    def LocalToViewport(
        self,
        WorldContextObject: unreal.UObject,
        Geometry: slate_core.Geometry,
        LocalCoordinate: core_uobject.Vector2D,
        PixelPosition: core_uobject.Vector2D,
        ViewportPosition: core_uobject.Vector2D,
    ): ...
    def LocalToAbsolute(
        self, Geometry: slate_core.Geometry, LocalCoordinate: core_uobject.Vector2D
    ) -> core_uobject.Vector2D: ...
    def IsUnderLocation(
        self, Geometry: slate_core.Geometry, AbsoluteCoordinate: core_uobject.Vector2D
    ) -> bool: ...
    def GetLocalSize(self, Geometry: slate_core.Geometry) -> core_uobject.Vector2D: ...
    def GetAbsoluteSize(
        self, Geometry: slate_core.Geometry
    ) -> core_uobject.Vector2D: ...
    def EqualEqual_SlateBrush(
        self, A: slate_core.SlateBrush, B: slate_core.SlateBrush
    ) -> bool: ...
    def AbsoluteToViewport(
        self,
        WorldContextObject: unreal.UObject,
        AbsoluteDesktopCoordinate: core_uobject.Vector2D,
        PixelPosition: core_uobject.Vector2D,
        ViewportPosition: core_uobject.Vector2D,
    ): ...
    def AbsoluteToLocal(
        self, Geometry: slate_core.Geometry, AbsoluteCoordinate: core_uobject.Vector2D
    ) -> core_uobject.Vector2D: ...


class SlateVectorArtData(unreal.UObject):
    VertexData: unreal.WrappedArray[SlateMeshVertex]
    IndexData: unreal.WrappedArray[int]
    Material: engine.MaterialInterface
    ExtentMin: core_uobject.Vector2D
    ExtentMax: core_uobject.Vector2D


class Slider(Widget):
    Value: float
    ValueDelegate: Any
    WidgetStyle: slate_core.SliderStyle
    Orientation: int
    SliderBarColor: core_uobject.LinearColor
    SliderHandleColor: core_uobject.LinearColor
    IndentHandle: bool
    Locked: bool
    StepSize: float
    IsFocusable: bool
    OnMouseCaptureBegin: Any
    OnMouseCaptureEnd: Any
    OnControllerCaptureBegin: Any
    OnControllerCaptureEnd: Any
    OnValueChanged: Any

    def SetValue(self, InValue: float): ...
    def SetStepSize(self, InValue: float): ...
    def SetSliderHandleColor(self, InValue: core_uobject.LinearColor): ...
    def SetSliderBarColor(self, InValue: core_uobject.LinearColor): ...
    def SetLocked(self, InValue: bool): ...
    def SetIndentHandle(self, InValue: bool): ...
    def GetValue(self) -> float: ...


class Spacer(Widget):
    Size: core_uobject.Vector2D

    def SetSize(self, InSize: core_uobject.Vector2D): ...


class SpinBox(Widget):
    Value: float
    ValueDelegate: Any
    WidgetStyle: slate_core.SpinBoxStyle
    Style: slate_core.SlateWidgetStyleAsset
    Delta: float
    SliderExponent: float
    Font: slate_core.SlateFontInfo
    Justification: int
    MinDesiredWidth: float
    ClearKeyboardFocusOnCommit: bool
    SelectAllTextOnCommit: bool
    ForegroundColor: slate_core.SlateColor
    OnValueChanged: Any
    OnValueCommitted: Any
    OnBeginSliderMovement: Any
    OnEndSliderMovement: Any
    bOverride_MinValue: bool
    bOverride_MaxValue: bool
    bOverride_MinSliderValue: bool
    bOverride_MaxSliderValue: bool
    MinValue: float
    MaxValue: float
    MinSliderValue: float
    MaxSliderValue: float

    def SetValue(self, NewValue: float): ...
    def SetMinValue(self, NewValue: float): ...
    def SetMinSliderValue(self, NewValue: float): ...
    def SetMaxValue(self, NewValue: float): ...
    def SetMaxSliderValue(self, NewValue: float): ...
    def SetForegroundColor(self, InForegroundColor: slate_core.SlateColor): ...
    def OnSpinBoxValueCommittedEvent__DelegateSignature(
        self, InValue: float, CommitMethod: int
    ): ...
    def OnSpinBoxValueChangedEvent__DelegateSignature(self, InValue: float): ...
    def OnSpinBoxBeginSliderMovement__DelegateSignature(self): ...
    def GetValue(self) -> float: ...
    def GetMinValue(self) -> float: ...
    def GetMinSliderValue(self) -> float: ...
    def GetMaxValue(self) -> float: ...
    def GetMaxSliderValue(self) -> float: ...
    def ClearMinValue(self): ...
    def ClearMinSliderValue(self): ...
    def ClearMaxValue(self): ...
    def ClearMaxSliderValue(self): ...


class TextBinding(PropertyBinding):

    def GetTextValue(self) -> str: ...
    def GetStringValue(self) -> str: ...


class TextBlock(TextLayoutWidget):
    Text: str
    TextDelegate: Any
    ColorAndOpacity: slate_core.SlateColor
    ColorAndOpacityDelegate: Any
    Font: slate_core.SlateFontInfo
    ShadowOffset: core_uobject.Vector2D
    ShadowColorAndOpacity: core_uobject.LinearColor
    ShadowColorAndOpacityDelegate: Any
    MinDesiredWidth: float
    bWrapWithInvalidationPanel: bool
    bAutoWrapText: bool

    def SetText(self, InText: str): ...
    def SetShadowOffset(self, InShadowOffset: core_uobject.Vector2D): ...
    def SetShadowColorAndOpacity(
        self, InShadowColorAndOpacity: core_uobject.LinearColor
    ): ...
    def SetOpacity(self, InOpacity: float): ...
    def SetMinDesiredWidth(self, InMinDesiredWidth: float): ...
    def SetJustification(self, InJustification: int): ...
    def SetFont(self, InFontInfo: slate_core.SlateFontInfo): ...
    def SetColorAndOpacity(self, InColorAndOpacity: slate_core.SlateColor): ...
    def SetAutoWrapText(self, InAutoTextWrap: bool): ...
    def GetText(self) -> str: ...
    def GetDynamicOutlineMaterial(self) -> engine.MaterialInstanceDynamic: ...
    def GetDynamicFontMaterial(self) -> engine.MaterialInstanceDynamic: ...


class Throbber(Widget):
    NumberOfPieces: int
    bAnimateHorizontally: bool
    bAnimateVertically: bool
    bAnimateOpacity: bool
    PieceImage: engine.SlateBrushAsset
    Image: slate_core.SlateBrush

    def SetNumberOfPieces(self, InNumberOfPieces: int): ...
    def SetAnimateVertically(self, bInAnimateVertically: bool): ...
    def SetAnimateOpacity(self, bInAnimateOpacity: bool): ...
    def SetAnimateHorizontally(self, bInAnimateHorizontally: bool): ...


class TileView(ListView):
    EntryHeight: float
    EntryWidth: float
    TileAlignment: slate.EListItemAlignment
    bWrapHorizontalNavigation: bool

    def SetEntryWidth(self, NewWidth: float): ...
    def SetEntryHeight(self, NewHeight: float): ...


class TreeView(ListView):
    BP_OnGetItemChildren: Any
    BP_OnItemExpansionChanged: Any

    def SetItemExpansion(self, Item: unreal.UObject, bExpandItem: bool): ...
    def ExpandAll(self): ...
    def CollapseAll(self): ...


class UMGSequencePlayer(unreal.UObject):
    Animation: WidgetAnimation


class UniformGridPanel(PanelWidget):
    SlotPadding: slate_core.Margin
    MinDesiredSlotWidth: float
    MinDesiredSlotHeight: float

    def SetSlotPadding(self, InSlotPadding: slate_core.Margin): ...
    def SetMinDesiredSlotWidth(self, InMinDesiredSlotWidth: float): ...
    def SetMinDesiredSlotHeight(self, InMinDesiredSlotHeight: float): ...
    def AddChildToUniformGrid(self, Content: Widget) -> UniformGridSlot: ...


class UniformGridSlot(PanelSlot):
    HorizontalAlignment: int
    VerticalAlignment: int
    Row: int
    Column: int

    def SetVerticalAlignment(self, InVerticalAlignment: int): ...
    def SetRow(self, InRow: int): ...
    def SetHorizontalAlignment(self, InHorizontalAlignment: int): ...
    def SetColumn(self, InColumn: int): ...


class VerticalBox(PanelWidget):

    def AddChildToVerticalBox(self, Content: Widget) -> VerticalBoxSlot: ...


class VerticalBoxSlot(PanelSlot):
    Padding: slate_core.Margin
    Size: SlateChildSize
    HorizontalAlignment: int
    VerticalAlignment: int

    def SetVerticalAlignment(self, InVerticalAlignment: int): ...
    def SetSize(self, InSize: SlateChildSize): ...
    def SetPadding(self, InPadding: slate_core.Margin): ...
    def SetHorizontalAlignment(self, InHorizontalAlignment: int): ...


class Viewport(ContentWidget):
    BackgroundColor: core_uobject.LinearColor

    def Spawn(self, ActorClass: unreal.UClass) -> engine.Actor: ...
    def SetViewRotation(self, Rotation: core_uobject.Rotator): ...
    def SetViewLocation(self, Location: core_uobject.Vector): ...
    def GetViewRotation(self) -> core_uobject.Rotator: ...
    def GetViewportWorld(self) -> engine.World: ...
    def GetViewLocation(self) -> core_uobject.Vector: ...


class VisibilityBinding(PropertyBinding):

    def GetValue(self) -> ESlateVisibility: ...


class WidgetAnimation(movie_scene.MovieSceneSequence):
    OnAnimationStarted: Any
    OnAnimationFinished: Any
    MovieScene: movie_scene.MovieScene
    AnimationBindings: unreal.WrappedArray[WidgetAnimationBinding]
    bLegacyFinishOnStop: bool

    def GetStartTime(self) -> float: ...
    def GetEndTime(self) -> float: ...


class WidgetBinding(PropertyBinding):

    def GetValue(self) -> Widget: ...


class WidgetBlueprintGeneratedClass(engine.BlueprintGeneratedClass):
    WidgetTree: WidgetTree
    bAllowTemplate: bool
    bAllowDynamicCreation: bool
    bValidTemplate: bool
    bTemplateInitialized: bool
    bCookedTemplate: bool
    bClassRequiresNativeTick: bool
    Bindings: unreal.WrappedArray[DelegateRuntimeBinding]
    Animations: unreal.WrappedArray[WidgetAnimation]
    NamedSlots: unreal.WrappedArray[str]
    TemplateAsset: Any
    Template: UserWidget


class WidgetBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def UnlockMouse(self, Reply: EventReply) -> EventReply: ...
    def Unhandled(self) -> EventReply: ...
    def SetWindowTitleBarState(
        self,
        TitleBarContent: Widget,
        Mode: engine.EWindowTitleBarMode,
        bTitleBarDragEnabled: bool,
        bWindowButtonsVisible: bool,
        bTitleBarVisible: bool,
    ): ...
    def SetWindowTitleBarOnCloseClickedDelegate(self, Delegate: Any): ...
    def SetWindowTitleBarCloseButtonActive(self, bActive: bool): ...
    def SetUserFocus(
        self, Reply: EventReply, FocusWidget: Widget, bInAllUsers: bool
    ) -> EventReply: ...
    def SetMousePosition(
        self, Reply: EventReply, NewMousePosition: core_uobject.Vector2D
    ) -> EventReply: ...
    def SetInputMode_UIOnlyEx(
        self,
        PlayerController: engine.PlayerController,
        InWidgetToFocus: Widget,
        InMouseLockMode: engine.EMouseLockMode,
    ): ...
    def SetInputMode_UIOnly(
        self,
        Target: engine.PlayerController,
        InWidgetToFocus: Widget,
        bLockMouseToViewport: bool,
    ): ...
    def SetInputMode_GameOnly(self, PlayerController: engine.PlayerController): ...
    def SetInputMode_GameAndUIEx(
        self,
        PlayerController: engine.PlayerController,
        InWidgetToFocus: Widget,
        InMouseLockMode: engine.EMouseLockMode,
        bHideCursorDuringCapture: bool,
    ): ...
    def SetInputMode_GameAndUI(
        self,
        Target: engine.PlayerController,
        InWidgetToFocus: Widget,
        bLockMouseToViewport: bool,
        bHideCursorDuringCapture: bool,
    ): ...
    def SetHardwareCursor(
        self,
        WorldContextObject: unreal.UObject,
        CursorShape: int,
        CursorName: str,
        HotSpot: core_uobject.Vector2D,
    ) -> bool: ...
    def SetFocusToGameViewport(self): ...
    def SetBrushResourceToTexture(
        self, Brush: slate_core.SlateBrush, Texture: engine.Texture2D
    ): ...
    def SetBrushResourceToMaterial(
        self, Brush: slate_core.SlateBrush, Material: engine.MaterialInterface
    ): ...
    def RestorePreviousWindowTitleBarState(self): ...
    def ReleaseMouseCapture(self, Reply: EventReply) -> EventReply: ...
    def ReleaseJoystickCapture(
        self, Reply: EventReply, bInAllJoysticks: bool
    ) -> EventReply: ...
    def OnGameWindowCloseButtonClickedDelegate__DelegateSignature(self): ...
    def NoResourceBrush(self) -> slate_core.SlateBrush: ...
    def MakeBrushFromTexture(
        self, Texture: engine.Texture2D, Width: int, Height: int
    ) -> slate_core.SlateBrush: ...
    def MakeBrushFromMaterial(
        self, Material: engine.MaterialInterface, Width: int, Height: int
    ) -> slate_core.SlateBrush: ...
    def MakeBrushFromAsset(
        self, BrushAsset: engine.SlateBrushAsset
    ) -> slate_core.SlateBrush: ...
    def LockMouse(self, Reply: EventReply, CapturingWidget: Widget) -> EventReply: ...
    def IsDragDropping(self) -> bool: ...
    def Handled(self) -> EventReply: ...
    def GetSafeZonePadding(
        self,
        WorldContextObject: unreal.UObject,
        SafePadding: core_uobject.Vector4,
        SafePaddingScale: core_uobject.Vector2D,
        SpillOverPadding: core_uobject.Vector4,
    ): ...
    def GetKeyEventFromAnalogInputEvent(
        self, Event: slate_core.AnalogInputEvent
    ) -> slate_core.KeyEvent: ...
    def GetInputEventFromPointerEvent(
        self, Event: slate_core.PointerEvent
    ) -> slate_core.InputEvent: ...
    def GetInputEventFromNavigationEvent(
        self, Event: slate_core.NavigationEvent
    ) -> slate_core.InputEvent: ...
    def GetInputEventFromKeyEvent(
        self, Event: slate_core.KeyEvent
    ) -> slate_core.InputEvent: ...
    def GetInputEventFromCharacterEvent(
        self, Event: slate_core.CharacterEvent
    ) -> slate_core.InputEvent: ...
    def GetDynamicMaterial(
        self, Brush: slate_core.SlateBrush
    ) -> engine.MaterialInstanceDynamic: ...
    def GetDragDroppingContent(self) -> DragDropOperation: ...
    def GetBrushResourceAsTexture2D(
        self, Brush: slate_core.SlateBrush
    ) -> engine.Texture2D: ...
    def GetBrushResourceAsMaterial(
        self, Brush: slate_core.SlateBrush
    ) -> engine.MaterialInterface: ...
    def GetBrushResource(self, Brush: slate_core.SlateBrush) -> unreal.UObject: ...
    def GetAllWidgetsWithInterface(
        self,
        WorldContextObject: unreal.UObject,
        Interface: unreal.UClass,
        FoundWidgets: unreal.WrappedArray[UserWidget],
        TopLevelOnly: bool,
    ): ...
    def GetAllWidgetsOfClass(
        self,
        WorldContextObject: unreal.UObject,
        FoundWidgets: unreal.WrappedArray[UserWidget],
        WidgetClass: unreal.UClass,
        TopLevelOnly: bool,
    ): ...
    def EndDragDrop(self, Reply: EventReply) -> EventReply: ...
    def DrawTextFormatted(
        self,
        Context: PaintContext,
        Text: str,
        Position: core_uobject.Vector2D,
        Font: engine.Font,
        FontSize: int,
        FontTypeFace: str,
        Tint: core_uobject.LinearColor,
    ): ...
    def DrawText(
        self,
        Context: PaintContext,
        inString: str,
        Position: core_uobject.Vector2D,
        Tint: core_uobject.LinearColor,
    ): ...
    def DrawLines(
        self,
        Context: PaintContext,
        Points: unreal.WrappedArray[core_uobject.Vector2D],
        Tint: core_uobject.LinearColor,
        bAntiAlias: bool,
    ): ...
    def DrawLine(
        self,
        Context: PaintContext,
        PositionA: core_uobject.Vector2D,
        PositionB: core_uobject.Vector2D,
        Tint: core_uobject.LinearColor,
        bAntiAlias: bool,
    ): ...
    def DrawBox(
        self,
        Context: PaintContext,
        Position: core_uobject.Vector2D,
        Size: core_uobject.Vector2D,
        Brush: engine.SlateBrushAsset,
        Tint: core_uobject.LinearColor,
    ): ...
    def DismissAllMenus(self): ...
    def DetectDragIfPressed(
        self,
        PointerEvent: slate_core.PointerEvent,
        WidgetDetectingDrag: Widget,
        DragKey: input_core.Key,
    ) -> EventReply: ...
    def DetectDrag(
        self, Reply: EventReply, WidgetDetectingDrag: Widget, DragKey: input_core.Key
    ) -> EventReply: ...
    def CreateDragDropOperation(
        self, OperationClass: unreal.UClass
    ) -> DragDropOperation: ...
    def Create(
        self,
        WorldContextObject: unreal.UObject,
        WidgetType: unreal.UClass,
        OwningPlayer: engine.PlayerController,
    ) -> UserWidget: ...
    def ClearUserFocus(self, Reply: EventReply, bInAllUsers: bool) -> EventReply: ...
    def CaptureMouse(
        self, Reply: EventReply, CapturingWidget: Widget
    ) -> EventReply: ...
    def CaptureJoystick(
        self, Reply: EventReply, CapturingWidget: Widget, bInAllJoysticks: bool
    ) -> EventReply: ...
    def CancelDragDrop(self): ...


class WidgetComponent(engine.MeshComponent):
    Space: EWidgetSpace
    TimingPolicy: EWidgetTimingPolicy
    WidgetClass: unreal.UClass
    DrawSize: core_uobject.IntPoint
    bManuallyRedraw: bool
    bRedrawRequested: bool
    RedrawTime: float
    CurrentDrawSize: core_uobject.IntPoint
    bDrawAtDesiredSize: bool
    Pivot: core_uobject.Vector2D
    bReceiveHardwareInput: bool
    bWindowFocusable: bool
    bApplyGammaCorrection: bool
    OwnerPlayer: engine.LocalPlayer
    BackgroundColor: core_uobject.LinearColor
    TintColorAndOpacity: core_uobject.LinearColor
    OpacityFromTexture: float
    BlendMode: EWidgetBlendMode
    bIsTwoSided: bool
    TickWhenOffscreen: bool
    Widget: UserWidget
    BodySetup: engine.BodySetup
    TranslucentMaterial: engine.MaterialInterface
    TranslucentMaterial_OneSided: engine.MaterialInterface
    OpaqueMaterial: engine.MaterialInterface
    OpaqueMaterial_OneSided: engine.MaterialInterface
    MaskedMaterial: engine.MaterialInterface
    MaskedMaterial_OneSided: engine.MaterialInterface
    RenderTarget: engine.TextureRenderTarget2D
    MaterialInstance: engine.MaterialInstanceDynamic
    bAddedToScreen: bool
    bEditTimeUsable: bool
    SharedLayerName: str
    LayerZOrder: int
    GeometryMode: EWidgetGeometryMode
    CylinderArcAngle: float

    def SetWidget(self, Widget: UserWidget): ...
    def SetTintColorAndOpacity(
        self, NewTintColorAndOpacity: core_uobject.LinearColor
    ): ...
    def SetOwnerPlayer(self, LocalPlayer: engine.LocalPlayer): ...
    def SetManuallyRedraw(self, bUseManualRedraw: bool): ...
    def SetDrawSize(self, Size: core_uobject.Vector2D): ...
    def SetBackgroundColor(self, NewBackgroundColor: core_uobject.LinearColor): ...
    def RequestRedraw(self): ...
    def GetUserWidgetObject(self) -> UserWidget: ...
    def GetRenderTarget(self) -> engine.TextureRenderTarget2D: ...
    def GetOwnerPlayer(self) -> engine.LocalPlayer: ...
    def GetMaterialInstance(self) -> engine.MaterialInstanceDynamic: ...
    def GetDrawSize(self) -> core_uobject.Vector2D: ...


class WidgetInteractionComponent(engine.SceneComponent):
    OnHoveredWidgetChanged: Any
    VirtualUserIndex: int
    PointerIndex: float
    TraceChannel: int
    InteractionDistance: float
    InteractionSource: EWidgetInteractionSource
    bEnableHitTesting: bool
    bShowDebug: bool
    DebugColor: core_uobject.LinearColor
    CustomHitResult: engine.HitResult
    LocalHitLocation: core_uobject.Vector2D
    LastLocalHitLocation: core_uobject.Vector2D
    HoveredWidgetComponent: WidgetComponent
    LastHitResult: engine.HitResult
    bIsHoveredWidgetInteractable: bool
    bIsHoveredWidgetFocusable: bool
    bIsHoveredWidgetHitTestVisible: bool

    def SetCustomHitResult(self, HitResult: engine.HitResult): ...
    def SendKeyChar(self, Characters: str, bRepeat: bool) -> bool: ...
    def ScrollWheel(self, ScrollDelta: float): ...
    def ReleasePointerKey(self, Key: input_core.Key): ...
    def ReleaseKey(self, Key: input_core.Key) -> bool: ...
    def PressPointerKey(self, Key: input_core.Key): ...
    def PressKey(self, Key: input_core.Key, bRepeat: bool) -> bool: ...
    def PressAndReleaseKey(self, Key: input_core.Key) -> bool: ...
    def IsOverInteractableWidget(self) -> bool: ...
    def IsOverHitTestVisibleWidget(self) -> bool: ...
    def IsOverFocusableWidget(self) -> bool: ...
    def GetLastHitResult(self) -> engine.HitResult: ...
    def GetHoveredWidgetComponent(self) -> WidgetComponent: ...
    def Get2DHitLocation(self) -> core_uobject.Vector2D: ...


class WidgetLayoutLibrary(engine.BlueprintFunctionLibrary):

    def SlotAsVerticalBoxSlot(self, Widget: Widget) -> VerticalBoxSlot: ...
    def SlotAsUniformGridSlot(self, Widget: Widget) -> UniformGridSlot: ...
    def SlotAsOverlaySlot(self, Widget: Widget) -> OverlaySlot: ...
    def SlotAsHorizontalBoxSlot(self, Widget: Widget) -> HorizontalBoxSlot: ...
    def SlotAsGridSlot(self, Widget: Widget) -> GridSlot: ...
    def SlotAsCanvasSlot(self, Widget: Widget) -> CanvasPanelSlot: ...
    def SlotAsBorderSlot(self, Widget: Widget) -> BorderSlot: ...
    def RemoveAllWidgets(self, WorldContextObject: unreal.UObject): ...
    def ProjectWorldLocationToWidgetPosition(
        self,
        PlayerController: engine.PlayerController,
        WorldLocation: core_uobject.Vector,
        ScreenPosition: core_uobject.Vector2D,
    ) -> bool: ...
    def GetViewportWidgetGeometry(
        self, WorldContextObject: unreal.UObject
    ) -> slate_core.Geometry: ...
    def GetViewportSize(
        self, WorldContextObject: unreal.UObject
    ) -> core_uobject.Vector2D: ...
    def GetViewportScale(self, WorldContextObject: unreal.UObject) -> float: ...
    def GetPlayerScreenWidgetGeometry(
        self, PlayerController: engine.PlayerController
    ) -> slate_core.Geometry: ...
    def GetMousePositionScaledByDPI(
        self, Player: engine.PlayerController, LocationX: float, LocationY: float
    ) -> bool: ...
    def GetMousePositionOnViewport(
        self, WorldContextObject: unreal.UObject
    ) -> core_uobject.Vector2D: ...
    def GetMousePositionOnPlatform(self) -> core_uobject.Vector2D: ...


class WidgetNavigation(unreal.UObject):
    Up: WidgetNavigationData
    Down: WidgetNavigationData
    Left: WidgetNavigationData
    Right: WidgetNavigationData
    Next: WidgetNavigationData
    Previous: WidgetNavigationData


class WidgetSwitcher(PanelWidget):
    ActiveWidgetIndex: int

    def SetActiveWidgetIndex(self, Index: int): ...
    def SetActiveWidget(self, Widget: Widget): ...
    def GetWidgetAtIndex(self, Index: int) -> Widget: ...
    def GetNumWidgets(self) -> int: ...
    def GetActiveWidgetIndex(self) -> int: ...
    def GetActiveWidget(self) -> Widget: ...


class WidgetSwitcherSlot(PanelSlot):
    Padding: slate_core.Margin
    HorizontalAlignment: int
    VerticalAlignment: int

    def SetVerticalAlignment(self, InVerticalAlignment: int): ...
    def SetPadding(self, InPadding: slate_core.Margin): ...
    def SetHorizontalAlignment(self, InHorizontalAlignment: int): ...


class WidgetTree(unreal.UObject):
    RootWidget: Widget


class WindowTitleBarArea(ContentWidget):
    bWindowButtonsEnabled: bool
    bDoubleClickTogglesFullscreen: bool

    def SetVerticalAlignment(self, InVerticalAlignment: int): ...
    def SetPadding(self, InPadding: slate_core.Margin): ...
    def SetHorizontalAlignment(self, InHorizontalAlignment: int): ...


class WindowTitleBarAreaSlot(PanelSlot):
    Padding: slate_core.Margin
    HorizontalAlignment: int
    VerticalAlignment: int

    def SetVerticalAlignment(self, InVerticalAlignment: int): ...
    def SetPadding(self, InPadding: slate_core.Margin): ...
    def SetHorizontalAlignment(self, InHorizontalAlignment: int): ...


class WrapBox(PanelWidget):
    InnerSlotPadding: core_uobject.Vector2D
    WrapWidth: float
    bExplicitWrapWidth: bool

    def SetInnerSlotPadding(self, InPadding: core_uobject.Vector2D): ...
    def AddChildWrapBox(self, Content: Widget) -> WrapBoxSlot: ...


class WrapBoxSlot(PanelSlot):
    Padding: slate_core.Margin
    bFillEmptySpace: bool
    FillSpanWhenLessThan: float
    HorizontalAlignment: int
    VerticalAlignment: int

    def SetVerticalAlignment(self, InVerticalAlignment: int): ...
    def SetPadding(self, InPadding: slate_core.Margin): ...
    def SetHorizontalAlignment(self, InHorizontalAlignment: int): ...
    def SetFillSpanWhenLessThan(self, InFillSpanWhenLessThan: float): ...
    def SetFillEmptySpace(self, InbFillEmptySpace: bool): ...


class EventReply: ...


class WidgetTransform:
    Translation: core_uobject.Vector2D
    Scale: core_uobject.Vector2D
    Shear: core_uobject.Vector2D
    Angle: float


class PaintContext: ...


class ShapedTextOptions:
    bOverride_TextShapingMethod: bool
    bOverride_TextFlowDirection: bool
    TextShapingMethod: slate_core.ETextShapingMethod
    TextFlowDirection: slate.ETextFlowDirection


class NamedSlotBinding:
    Name: str
    Content: Widget


class AnchorData:
    Offsets: slate_core.Margin
    Anchors: slate.Anchors
    Alignment: core_uobject.Vector2D


class DynamicPropertyPath(property_path.CachedPropertyPath): ...


class MovieScene2DTransformMask:
    Mask: int


class MovieScene2DTransformSectionTemplate(
    movie_scene.MovieScenePropertySectionTemplate
):
    Translation: movie_scene.MovieSceneFloatChannel
    Rotation: movie_scene.MovieSceneFloatChannel
    Scale: movie_scene.MovieSceneFloatChannel
    Shear: movie_scene.MovieSceneFloatChannel
    BlendType: movie_scene.EMovieSceneBlendType
    Mask: MovieScene2DTransformMask


class MovieSceneMarginSectionTemplate(movie_scene.MovieScenePropertySectionTemplate):
    TopCurve: movie_scene.MovieSceneFloatChannel
    LeftCurve: movie_scene.MovieSceneFloatChannel
    RightCurve: movie_scene.MovieSceneFloatChannel
    BottomCurve: movie_scene.MovieSceneFloatChannel
    BlendType: movie_scene.EMovieSceneBlendType


class MovieSceneWidgetMaterialSectionTemplate(
    movie_scene_tracks.MovieSceneParameterSectionTemplate
):
    BrushPropertyNamePath: unreal.WrappedArray[str]


class RichTextStyleRow(engine.TableRowBase):
    TextStyle: slate_core.TextBlockStyle


class RichImageRow(engine.TableRowBase):
    Brush: slate_core.SlateBrush


class SlateMeshVertex:
    Position: core_uobject.Vector2D
    Color: core_uobject.Color
    UV1: core_uobject.Vector2D
    UV2: core_uobject.Vector2D
    UV3: core_uobject.Vector2D
    UV4: core_uobject.Vector2D
    UV5: core_uobject.Vector2D


class SlateChildSize:
    Value: float
    SizeRule: int


class WidgetAnimationBinding:
    WidgetName: str
    SlotWidgetName: str
    AnimationGuid: core_uobject.Guid
    bIsRootWidget: bool


class DelegateRuntimeBinding:
    ObjectName: str
    PropertyName: str
    FunctionName: str
    SourcePath: DynamicPropertyPath
    Kind: EBindingKind


class WidgetNavigationData:
    Rule: slate_core.EUINavigationRule
    WidgetToFocus: str
    Widget: Widget
    CustomDelegate: Any


class Default__WidgetBlueprintGeneratedClass: ...


class ESlateVisibility(enum.Enum):
    Hidden = 0
    Collapsed = 1
    SelfHitTestInvisible = 2


class EVirtualKeyboardType(enum.Enum):
    Password = 0
    Number = 1
    Web = 2


class EUMGSequencePlayMode(enum.Enum):
    Reverse = 0
    PingPong = 1


class EWidgetTickFrequency(enum.Enum):
    Auto = 0
    EWidgetTickFrequency_MAX = 1


class EDragPivot(enum.Enum):
    TopLeft = 0
    CenterLeft = 1
    TopCenter = 2
    BottomCenter = 3


class EDynamicBoxType(enum.Enum):
    EDynamicBoxType_MAX = 0
    Vertical = 1
    Wrap = 2


class ESlateSizeRule(enum.Enum):
    Fill = 0
    ESlateSizeRule_MAX = 1


class EWidgetDesignFlags(enum.Enum):
    Designing = 0
    ShowOutline = 1
    ExecutePreConstruct = 2


class EBindingKind(enum.Enum):
    Property = 0
    EBindingKind_MAX = 1


class EWidgetGeometryMode(enum.Enum):
    Cylinder = 0
    EWidgetGeometryMode_MAX = 1


class EWidgetBlendMode(enum.Enum):
    Masked = 0
    Transparent = 1


class EWidgetTimingPolicy(enum.Enum):
    GameTime = 0
    EWidgetTimingPolicy_MAX = 1


class EWidgetSpace(enum.Enum):
    Screen = 0
    EWidgetSpace_MAX = 1


class EWidgetInteractionSource(enum.Enum):
    EWidgetInteractionSource_MAX = 0
    Mouse = 1
    CenterScreen = 2

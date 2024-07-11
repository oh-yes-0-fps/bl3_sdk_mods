from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject


class FontBulkData(unreal.UObject): ...


class FontFaceInterface(core_uobject.Interface): ...


class FontProviderInterface(core_uobject.Interface): ...


class SlateTypes(unreal.UObject): ...


class SlateWidgetStyleAsset(unreal.UObject):
    CustomStyle: SlateWidgetStyleContainerBase


class SlateWidgetStyleContainerBase(unreal.UObject): ...


class SlateWidgetStyleContainerInterface(core_uobject.Interface): ...


class Geometry: ...


class SlateBrush:
    ImageSize: core_uobject.Vector2D
    Margin: Margin
    TintColor: SlateColor
    ResourceObject: unreal.UObject
    ResourceName: str
    UVRegion: core_uobject.Box2D
    DrawAs: int
    Tiling: int
    Mirroring: int
    ImageType: int
    bIsDynamicallyLoaded: bool
    bHasUObject: bool


class SlateColor:
    SpecifiedColor: core_uobject.LinearColor
    ColorUseRule: int


class Margin:
    Left: float
    Top: float
    Right: float
    Bottom: float


class InputEvent: ...


class PointerEvent(InputEvent): ...


class CharacterEvent(InputEvent): ...


class KeyEvent(InputEvent): ...


class NavigationEvent(InputEvent): ...


class AnalogInputEvent(KeyEvent): ...


class SlateFontInfo:
    FontObject: unreal.UObject
    FontMaterial: unreal.UObject
    OutlineSettings: FontOutlineSettings
    TypefaceFontName: str
    Size: int


class FontOutlineSettings:
    OutlineSize: int
    bSeparateFillAlpha: bool
    OutlineMaterial: unreal.UObject
    OutlineColor: core_uobject.LinearColor


class SlateWidgetStyle: ...


class TableRowStyle(SlateWidgetStyle):
    SelectorFocusedBrush: SlateBrush
    ActiveHoveredBrush: SlateBrush
    ActiveBrush: SlateBrush
    InactiveHoveredBrush: SlateBrush
    InactiveBrush: SlateBrush
    EvenRowBackgroundHoveredBrush: SlateBrush
    EvenRowBackgroundBrush: SlateBrush
    OddRowBackgroundHoveredBrush: SlateBrush
    OddRowBackgroundBrush: SlateBrush
    TextColor: SlateColor
    SelectedTextColor: SlateColor
    DropIndicator_Above: SlateBrush
    DropIndicator_Onto: SlateBrush
    DropIndicator_Below: SlateBrush


class ComboBoxStyle(SlateWidgetStyle):
    ComboButtonStyle: ComboButtonStyle
    PressedSlateSound: SlateSound
    SelectionChangeSlateSound: SlateSound


class SlateSound:
    ResourceObject: unreal.UObject


class ComboButtonStyle(SlateWidgetStyle):
    ButtonStyle: ButtonStyle
    DownArrowImage: SlateBrush
    MenuBorderBrush: SlateBrush
    MenuBorderPadding: Margin


class ButtonStyle(SlateWidgetStyle):
    Normal: SlateBrush
    Hovered: SlateBrush
    Pressed: SlateBrush
    Disabled: SlateBrush
    NormalPadding: Margin
    PressedPadding: Margin
    PressedSlateSound: SlateSound
    HoveredSlateSound: SlateSound


class EditableTextStyle(SlateWidgetStyle):
    Font: SlateFontInfo
    ColorAndOpacity: SlateColor
    BackgroundImageSelected: SlateBrush
    BackgroundImageComposing: SlateBrush
    CaretImage: SlateBrush


class EditableTextBoxStyle(SlateWidgetStyle):
    BackgroundImageNormal: SlateBrush
    BackgroundImageHovered: SlateBrush
    BackgroundImageFocused: SlateBrush
    BackgroundImageReadOnly: SlateBrush
    Padding: Margin
    Font: SlateFontInfo
    ForegroundColor: SlateColor
    BackgroundColor: SlateColor
    ReadOnlyForegroundColor: SlateColor
    HScrollBarPadding: Margin
    VScrollBarPadding: Margin
    ScrollBarStyle: ScrollBarStyle


class ScrollBarStyle(SlateWidgetStyle):
    HorizontalBackgroundImage: SlateBrush
    VerticalBackgroundImage: SlateBrush
    VerticalTopSlotImage: SlateBrush
    HorizontalTopSlotImage: SlateBrush
    VerticalBottomSlotImage: SlateBrush
    HorizontalBottomSlotImage: SlateBrush
    NormalThumbImage: SlateBrush
    HoveredThumbImage: SlateBrush
    DraggedThumbImage: SlateBrush


class TextBlockStyle(SlateWidgetStyle):
    Font: SlateFontInfo
    ColorAndOpacity: SlateColor
    ShadowOffset: core_uobject.Vector2D
    ShadowColorAndOpacity: core_uobject.LinearColor
    SelectedBackgroundColor: SlateColor
    HighlightColor: core_uobject.LinearColor
    HighlightShape: SlateBrush
    UnderlineBrush: SlateBrush


class SpinBoxStyle(SlateWidgetStyle):
    BackgroundBrush: SlateBrush
    HoveredBackgroundBrush: SlateBrush
    ActiveFillBrush: SlateBrush
    InactiveFillBrush: SlateBrush
    ArrowsImage: SlateBrush
    ForegroundColor: SlateColor
    TextPadding: Margin


class FocusEvent: ...


class MotionEvent(InputEvent): ...


class CompositeFont:
    DefaultTypeface: Typeface
    FallbackTypeface: CompositeFallbackFont
    SubTypefaces: unreal.WrappedArray[CompositeSubFont]


class CompositeFallbackFont:
    Typeface: Typeface
    ScalingFactor: float


class Typeface:
    Fonts: unreal.WrappedArray[TypefaceEntry]


class TypefaceEntry:
    Name: str
    Font: FontData


class FontData:
    FontFilename: str
    Hinting: EFontHinting
    LoadingPolicy: EFontLoadingPolicy
    SubFaceIndex: int
    FontFaceAsset: unreal.UObject


class CompositeSubFont(CompositeFallbackFont):
    CharacterRanges: unreal.WrappedArray[core_uobject.Int32Range]
    Cultures: str


class CaptureLostEvent: ...


class WindowStyle(SlateWidgetStyle):
    MinimizeButtonStyle: ButtonStyle
    MaximizeButtonStyle: ButtonStyle
    RestoreButtonStyle: ButtonStyle
    CloseButtonStyle: ButtonStyle
    TitleTextStyle: TextBlockStyle
    ActiveTitleBrush: SlateBrush
    InactiveTitleBrush: SlateBrush
    FlashTitleBrush: SlateBrush
    BackgroundColor: SlateColor
    OutlineBrush: SlateBrush
    OutlineColor: SlateColor
    BorderBrush: SlateBrush
    BackgroundBrush: SlateBrush
    ChildBackgroundBrush: SlateBrush


class ScrollBorderStyle(SlateWidgetStyle):
    TopShadowBrush: SlateBrush
    BottomShadowBrush: SlateBrush


class ScrollBoxStyle(SlateWidgetStyle):
    TopShadowBrush: SlateBrush
    BottomShadowBrush: SlateBrush
    LeftShadowBrush: SlateBrush
    RightShadowBrush: SlateBrush


class DockTabStyle(SlateWidgetStyle):
    CloseButtonStyle: ButtonStyle
    NormalBrush: SlateBrush
    ActiveBrush: SlateBrush
    ColorOverlayTabBrush: SlateBrush
    ColorOverlayIconBrush: SlateBrush
    ForegroundBrush: SlateBrush
    HoveredBrush: SlateBrush
    ContentAreaBrush: SlateBrush
    TabWellBrush: SlateBrush
    TabPadding: Margin
    OverlapWidth: float
    FlashColor: SlateColor


class HeaderRowStyle(SlateWidgetStyle):
    ColumnStyle: TableColumnHeaderStyle
    LastColumnStyle: TableColumnHeaderStyle
    ColumnSplitterStyle: SplitterStyle
    BackgroundBrush: SlateBrush
    ForegroundColor: SlateColor


class SplitterStyle(SlateWidgetStyle):
    HandleNormalBrush: SlateBrush
    HandleHighlightBrush: SlateBrush


class TableColumnHeaderStyle(SlateWidgetStyle):
    SortPrimaryAscendingImage: SlateBrush
    SortPrimaryDescendingImage: SlateBrush
    SortSecondaryAscendingImage: SlateBrush
    SortSecondaryDescendingImage: SlateBrush
    NormalBrush: SlateBrush
    HoveredBrush: SlateBrush
    MenuDropdownImage: SlateBrush
    MenuDropdownNormalBorderBrush: SlateBrush
    MenuDropdownHoveredBorderBrush: SlateBrush


class InlineTextImageStyle(SlateWidgetStyle):
    Image: SlateBrush
    Baseline: int


class VolumeControlStyle(SlateWidgetStyle):
    SliderStyle: SliderStyle
    HighVolumeImage: SlateBrush
    MidVolumeImage: SlateBrush
    LowVolumeImage: SlateBrush
    NoVolumeImage: SlateBrush
    MutedImage: SlateBrush


class SliderStyle(SlateWidgetStyle):
    NormalBarImage: SlateBrush
    DisabledBarImage: SlateBrush
    NormalThumbImage: SlateBrush
    DisabledThumbImage: SlateBrush
    BarThickness: float


class SearchBoxStyle(SlateWidgetStyle):
    TextBoxStyle: EditableTextBoxStyle
    ActiveFontInfo: SlateFontInfo
    UpArrowImage: SlateBrush
    DownArrowImage: SlateBrush
    GlassImage: SlateBrush
    ClearImage: SlateBrush
    ImagePadding: Margin
    bLeftAlignButtons: bool


class ExpandableAreaStyle(SlateWidgetStyle):
    CollapsedImage: SlateBrush
    ExpandedImage: SlateBrush
    RolloutAnimationSeconds: float


class ProgressBarStyle(SlateWidgetStyle):
    BackgroundImage: SlateBrush
    FillImage: SlateBrush
    MarqueeImage: SlateBrush


class InlineEditableTextBlockStyle(SlateWidgetStyle):
    EditableTextBoxStyle: EditableTextBoxStyle
    TextStyle: TextBlockStyle


class HyperlinkStyle(SlateWidgetStyle):
    UnderlineStyle: ButtonStyle
    TextStyle: TextBlockStyle
    Padding: Margin


class CheckBoxStyle(SlateWidgetStyle):
    CheckBoxType: int
    UncheckedImage: SlateBrush
    UncheckedHoveredImage: SlateBrush
    UncheckedPressedImage: SlateBrush
    CheckedImage: SlateBrush
    CheckedHoveredImage: SlateBrush
    CheckedPressedImage: SlateBrush
    UndeterminedImage: SlateBrush
    UndeterminedHoveredImage: SlateBrush
    UndeterminedPressedImage: SlateBrush
    Padding: Margin
    ForegroundColor: SlateColor
    BorderBackgroundColor: SlateColor
    CheckedSlateSound: SlateSound
    UncheckedSlateSound: SlateSound
    HoveredSlateSound: SlateSound


class ECheckBoxState(enum.Enum):
    Checked = 0
    Undetermined = 1


class EWidgetClipping(enum.Enum):
    ClipToBounds = 0
    ClipToBoundsWithoutIntersecting = 1
    OnDemand = 2


class ESlateBrushImageType(enum.Enum):
    FullColor = 0
    Linear = 1


class ESlateBrushMirrorType(enum.Enum):
    ESlateBrushMirrorType_MAX = 0
    Horizontal = 1
    Vertical = 2


class ESlateBrushTileType(enum.Enum):
    ESlateBrushTileType_MAX = 0
    Horizontal = 1
    Vertical = 2


class ESlateBrushDrawType(enum.Enum):
    ESlateBrushDrawType_MAX = 0
    Box = 1
    Border = 2


class ESlateColorStylingMode(enum.Enum):
    UseColor_Specified_Link = 0
    UseColor_Foreground = 1
    UseColor_MAX = 2


class EUINavigationRule(enum.Enum):
    Custom = 0
    Explicit = 1
    Wrap = 2


class EUINavigation(enum.Enum):
    Next = 0
    Up = 1
    Right = 2
    EUINavigation_MAX = 3


class ESelectInfo(enum.Enum):
    OnNavigation = 0
    ESelectInfo_MAX = 1
    OnMouseClick = 2


class ETextCommit(enum.Enum):
    OnUserMovedFocus = 0
    OnEnter = 1
    ETextCommit_MAX = 2


class ETextShapingMethod(enum.Enum):
    KerningOnly = 0
    FullShaping = 1


class EFontLayoutMethod(enum.Enum):
    BoundingBox = 0
    EFontLayoutMethod_MAX = 1


class EFontLoadingPolicy(enum.Enum):
    Stream = 0
    Inline = 1


class EFontHinting(enum.Enum):
    Auto = 0
    AutoLight = 1
    None_ = 2


class EFocusCause(enum.Enum):
    Navigation = 0
    SetDirectly = 1
    OtherWidgetLostFocus = 2


class EColorVisionDeficiency(enum.Enum):
    Deuteranope = 0
    EColorVisionDeficiency_MAX = 1
    Protanope = 2


class EScrollDirection(enum.Enum):
    Scroll_Up = 0
    Scroll_MAX = 1


class EOrientation(enum.Enum):
    Orient_MAX = 0
    Orient_Vertical = 1


class EMenuPlacement(enum.Enum):
    MenuPlacement_BelowRightAnchor = 0
    MenuPlacement_CenteredBelowAnchor = 1
    MenuPlacement_ComboBoxRight = 2
    MenuPlacement_AboveRightAnchor = 3


class EVerticalAlignment(enum.Enum):
    VAlign_Top = 0
    VAlign_Center = 1
    VAlign_MAX = 2


class EHorizontalAlignment(enum.Enum):
    HAlign_Left = 0
    HAlign_Center = 1
    HAlign_MAX = 2


class ENavigationGenesis(enum.Enum):
    Controller = 0
    User = 1


class ENavigationSource(enum.Enum):
    ENavigationSource_MAX = 0
    WidgetUnderCursor = 1


class EButtonPressMethod(enum.Enum):
    ButtonPress = 0
    ButtonRelease = 1


class EButtonTouchMethod(enum.Enum):
    PreciseTap = 0
    EButtonTouchMethod_MAX = 1


class EButtonClickMethod(enum.Enum):
    EButtonClickMethod_MAX = 0
    MouseDown = 1
    MouseUp = 2


class EFontFallback(enum.Enum):
    FF_LocalizedFallback = 0
    FF_LastResortFallback = 1


class ESlateCheckBoxType(enum.Enum):
    ESlateCheckBoxType_MAX = 0
    ToggleButton = 1


class ESlateParentWindowSearchMethod(enum.Enum):
    MainWindow = 0
    ESlateParentWindowSearchMethod_MAX = 1


class EConsumeMouseWheel(enum.Enum):
    Always = 0
    Never = 1

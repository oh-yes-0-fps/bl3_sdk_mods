from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import input_core
from . import slate_core



class ButtonWidgetStyle(slate_core.SlateWidgetStyleContainerBase):
    ButtonStyle: slate_core.ButtonStyle



class CheckBoxWidgetStyle(slate_core.SlateWidgetStyleContainerBase):
    CheckBoxStyle: slate_core.CheckBoxStyle



class ComboBoxWidgetStyle(slate_core.SlateWidgetStyleContainerBase):
    ComboBoxStyle: slate_core.ComboBoxStyle



class ComboButtonWidgetStyle(slate_core.SlateWidgetStyleContainerBase):
    ComboButtonStyle: slate_core.ComboButtonStyle



class EditableTextBoxWidgetStyle(slate_core.SlateWidgetStyleContainerBase):
    EditableTextBoxStyle: slate_core.EditableTextBoxStyle



class EditableTextWidgetStyle(slate_core.SlateWidgetStyleContainerBase):
    EditableTextStyle: slate_core.EditableTextStyle



class ProgressWidgetStyle(slate_core.SlateWidgetStyleContainerBase):
    ProgressBarStyle: slate_core.ProgressBarStyle



class ScrollBarWidgetStyle(slate_core.SlateWidgetStyleContainerBase):
    ScrollBarStyle: slate_core.ScrollBarStyle



class ScrollBoxWidgetStyle(slate_core.SlateWidgetStyleContainerBase):
    ScrollBoxStyle: slate_core.ScrollBoxStyle



class SlateSettings(unreal.UObject):
    bExplicitCanvasChildZOrder: bool



class SpinBoxWidgetStyle(slate_core.SlateWidgetStyleContainerBase):
    SpinBoxStyle: slate_core.SpinBoxStyle



class TextBlockWidgetStyle(slate_core.SlateWidgetStyleContainerBase):
    TextBlockStyle: slate_core.TextBlockStyle



class VirtualKeyboardOptions:
    bEnableAutocorrect: bool



class InputChord:
    Key: input_core.Key
    bShift: bool
    bCtrl: bool
    bAlt: bool
    bCmd: bool



class Anchors:
    Minimum: core_uobject.Vector2D
    Maximum: core_uobject.Vector2D



class ETextFlowDirection(enum.Enum):
    LeftToRight = 0
    RightToLeft = 1


class ETextJustify(enum.Enum):
    Center = 0
    Right = 1


class EVirtualKeyboardDismissAction(enum.Enum):
    TextCommitOnAccept = 0
    TextCommitOnDismiss = 1


class ETextWrappingPolicy(enum.Enum):
    ETextWrappingPolicy_MAX = 0
    AllowPerCharacterWrapping = 1


class ETableViewMode(enum.Enum):
    Tile = 0
    Tree = 1


class ESelectionMode(enum.Enum):
    SingleToggle = 0
    Single = 1
    ESelectionMode_MAX = 2


class EProgressBarFillType(enum.Enum):
    FillFromCenter = 0
    RightToLeft = 1
    BottomToTop = 2


class EStretch(enum.Enum):
    Fill = 0
    ScaleToFit = 1
    ScaleToFitY = 2
    EStretch_MAX = 3


class EStretchDirection(enum.Enum):
    UpOnly = 0
    DownOnly = 1


class EDescendantScrollDestination(enum.Enum):
    Center = 0
    TopOrLeft = 1


class EListItemAlignment(enum.Enum):
    RightAligned = 0
    EvenlySize = 1
    EvenlyWide = 2


class EMultipleKeyBindingIndex(enum.Enum):
    Secondary = 0
    NumChords = 1

from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum





class InputCoreTypes(unreal.UObject): ...


class Key:
    KeyName: str



class ETouchIndex(enum.Enum):
    Touch2 = 0
    Touch3 = 1
    Touch5 = 2
    Touch9 = 3


class EControllerHand(enum.Enum):
    AnyHand = 0
    Right = 1
    Special_3 = 2
    ExternalCamera = 3
    Special_11 = 4


class ETouchType(enum.Enum):
    NumTypes = 0
    Moved = 1
    Stationary = 2


class EConsoleForGamepadLabels(enum.Enum):
    XBoxOne = 0
    PS4 = 1

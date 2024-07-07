from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum





class NamedInterfaces(unreal.UObject):
    NamedInterfaces: unreal.WrappedArray[NamedInterface]
    NamedInterfaceDefs: unreal.WrappedArray[NamedInterfaceDef]



class NamedInterfaceDef:
    InterfaceName: str
    InterfaceClassName: str



class NamedInterface:
    InterfaceName: str
    InterfaceObject: unreal.UObject



class EOnlineActivityOutcome(enum.Enum):
    Cancelled = 0
    Failed = 1

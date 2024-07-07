from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject



class SessionServiceLogUnsubscribe: ...


class SessionServiceLogSubscribe: ...


class SessionServiceLog:
    Category: str
    Data: str
    InstanceId: core_uobject.Guid
    TimeSeconds: float
    Verbosity: int



class SessionServicePong:
    Authorized: bool
    BuildDate: str
    DeviceName: str
    InstanceId: core_uobject.Guid
    InstanceName: str
    IsConsoleBuild: bool
    PlatformName: str
    SessionId: core_uobject.Guid
    SessionName: str
    SessionOwner: str
    Standalone: bool



class SessionServicePing:
    UserName: str


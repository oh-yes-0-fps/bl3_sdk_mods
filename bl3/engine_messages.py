from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject


class EngineServiceNotification:
    Text: str
    TimeSeconds: float


class EngineServiceTerminate:
    UserName: str


class EngineServiceExecuteCommand:
    Command: str
    UserName: str


class EngineServiceAuthGrant:
    UserName: str
    UserToGrant: str


class EngineServiceAuthDeny:
    UserName: str
    UserToDeny: str


class EngineServicePong:
    CurrentLevel: str
    EngineVersion: int
    HasBegunPlay: bool
    InstanceId: core_uobject.Guid
    InstanceType: str
    SessionId: core_uobject.Guid
    WorldTimeSeconds: float


class EngineServicePing: ...

from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


class TcpMessagingSettings(unreal.UObject):
    EnableTransport: bool
    ListenEndpoint: str
    ConnectToEndpoints: unreal.WrappedArray[str]
    ConnectionRetryDelay: int

from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


class UdpMessagingSettings(unreal.UObject):
    EnableTransport: bool
    UnicastEndpoint: str
    MulticastEndpoint: str
    MulticastTimeToLive: int
    StaticEndpoints: unreal.WrappedArray[str]
    EnableTunnel: bool
    TunnelUnicastEndpoint: str
    TunnelMulticastEndpoint: str
    RemoteTunnelEndpoints: unreal.WrappedArray[str]


class UdpMockMessage:
    Data: unreal.WrappedArray[int]

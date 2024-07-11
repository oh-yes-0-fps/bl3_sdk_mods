from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import online_subsystem_utils


class EpicNetConnection(online_subsystem_utils.IpConnection): ...


class EpicBeaconNetConnection(EpicNetConnection): ...


class EpicNetDriver(online_subsystem_utils.IpNetDriver):
    bIsPassthrough: bool


class EpicBeaconNetDriver(EpicNetDriver): ...

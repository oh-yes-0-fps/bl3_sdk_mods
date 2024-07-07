from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import online_subsystem_utils



class SparkNetConnection(online_subsystem_utils.IpConnection): ...


class SparkBeaconNetConnection(SparkNetConnection): ...


class SparkNetDriver(online_subsystem_utils.IpNetDriver):
    bIsPassthrough: bool



class SparkBeaconNetDriver(SparkNetDriver): ...

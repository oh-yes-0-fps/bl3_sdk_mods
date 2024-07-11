from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


class LogitechARXConfig(unreal.UObject):
    BasePathToAssets: str
    IndexFile: str
    AppletTitle: str
    AppletFriendlyName: str

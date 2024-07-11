from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


class GbxJiraSettings(unreal.UObject):
    bDisplayInLevelEditor: bool
    BugIconSize: int

from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import engine


class CoherentRenderingSettings(unreal.UObject):
    RenderingLogSeverity: ECoherentRenderingSettingsSeverity
    ShowWarningsOnScreen: bool
    DeveloperOptions: str


class CohTextureUserWrapData(unreal.UObject):
    Texture: engine.Texture


class ECoherentRenderingSettingsSeverity(enum.Enum):
    Debug = 0
    Info = 1
    AssertFailure = 2

from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


class MaterialShaderQualitySettings(unreal.UObject):
    ForwardSettingMap: Any


class ShaderPlatformQualitySettings(unreal.UObject):
    QualityOverrides: MaterialQualityOverrides


class MaterialQualityOverrides:
    bEnableOverride: bool
    bForceFullyRough: bool
    bForceNonMetal: bool
    bForceDisableLMDirectionality: bool
    bForceLQReflections: bool
    bDisableMaterialNormalCalculation: bool
    MobileCSMQuality: EMobileCSMQuality


class EMobileCSMQuality(enum.Enum):
    PCF_2x2 = 0
    PCF_1x1 = 1

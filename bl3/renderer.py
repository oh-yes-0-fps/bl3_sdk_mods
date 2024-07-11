from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


class LightPropagationVolumeSettings:
    bOverride_LPVIntensity: bool
    bOverride_LPVDirectionalOcclusionIntensity: bool
    bOverride_LPVDirectionalOcclusionRadius: bool
    bOverride_LPVDiffuseOcclusionExponent: bool
    bOverride_LPVSpecularOcclusionExponent: bool
    bOverride_LPVDiffuseOcclusionIntensity: bool
    bOverride_LPVSpecularOcclusionIntensity: bool
    bOverride_LPVSize: bool
    bOverride_LPVSecondaryOcclusionIntensity: bool
    bOverride_LPVSecondaryBounceIntensity: bool
    bOverride_LPVGeometryVolumeBias: bool
    bOverride_LPVVplInjectionBias: bool
    bOverride_LPVEmissiveInjectionIntensity: bool
    LPVIntensity: float
    LPVVplInjectionBias: float
    LPVSize: float
    LPVSecondaryOcclusionIntensity: float
    LPVSecondaryBounceIntensity: float
    LPVGeometryVolumeBias: float
    LPVEmissiveInjectionIntensity: float
    LPVDirectionalOcclusionIntensity: float
    LPVDirectionalOcclusionRadius: float
    LPVDiffuseOcclusionExponent: float
    LPVSpecularOcclusionExponent: float
    LPVDiffuseOcclusionIntensity: float
    LPVSpecularOcclusionIntensity: float
    LPVFadeRange: float
    LPVDirectionalOcclusionFadeRange: float

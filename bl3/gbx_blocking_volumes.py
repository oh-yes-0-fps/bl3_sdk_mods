from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import engine



class GbxBlockingVolume(engine.Volume):
    bAlwaysRender: bool
    bBlockRockets: bool
    bBlockProjectiles: bool
    bBlockTossed: bool
    bBlockEnemyPawns: bool
    bBlockEnemyVehicles: bool
    bBlockFriendlyPawns: bool
    bBlockPlayerVehicles: bool
    bBlockUsingThings: bool
    bAllowStandingOn: bool
    bBlockCamera: bool
    bEnemyPawnsPropEnabled: bool
    bEnemyVehiclesPropEnabled: bool
    bFriendlyPawnsPropEnabled: bool
    bPlayerVehiclesPropEnabled: bool



class GbxBlockingVolumeUserSettings(unreal.UObject):
    bAlwaysRenderVolumes: bool
    bNeverRenderVolumes: bool
    BlockingVolumeOpacity: float
    bInvertColors: bool


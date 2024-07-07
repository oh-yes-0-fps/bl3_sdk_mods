from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject



class ImgMediaSettings(unreal.UObject):
    DefaultFrameRate: core_uobject.FrameRate
    CacheBehindPercentage: float
    CacheSizeGB: float
    CacheThreads: int
    CacheThreadStackSizeKB: int
    DefaultProxy: str
    UseDefaultProxy: bool


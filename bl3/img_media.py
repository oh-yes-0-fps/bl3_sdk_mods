from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine
from . import media_assets



class ImgMediaSource(media_assets.BaseMediaSource):
    FrameRateOverride: core_uobject.FrameRate
    ProxyOverride: str
    SequencePath: engine.DirectoryPath
    def SetSequencePath(self, Path: str): ...
    def GetSequencePath(self, ReturnValue: str) -> str: ...
    def GetProxies(self, OutProxies: unreal.WrappedArray[str]): ...

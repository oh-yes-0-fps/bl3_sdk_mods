from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum





class GbxMixerSettings(unreal.UObject):
    AppClientID: str
    RequiredAuthScope: str
    MixplayProjectVersionID: str
    BackendServiceURL: str


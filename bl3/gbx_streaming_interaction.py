from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum





class InteractiveStreamingServiceViewer:
    ID: str
    Name: str



class EStreamingService(enum.Enum):
    Mixer = 0
    Twitch = 1

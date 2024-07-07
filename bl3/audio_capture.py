from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import audio_mixer



class AudioCaptureComponent(audio_mixer.SynthComponent):
    JitterLatencyFrames: int


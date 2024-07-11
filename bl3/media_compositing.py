from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import movie_scene
from . import media_assets


class MovieSceneMediaSection(movie_scene.MovieSceneSection):
    Proxy: str
    MediaSoundComponent: media_assets.MediaSoundComponent
    MediaTexture: media_assets.MediaTexture
    MediaSource: media_assets.MediaSource


class MovieSceneMediaTrack(movie_scene.MovieSceneNameableTrack):
    MediaSections: unreal.WrappedArray[movie_scene.MovieSceneSection]


class MovieSceneMediaSectionTemplate(movie_scene.MovieSceneEvalTemplate):
    Params: MovieSceneMediaSectionParams


class MovieSceneMediaSectionParams:
    MediaSoundComponent: media_assets.MediaSoundComponent
    MediaSource: media_assets.MediaSource
    MediaTexture: media_assets.MediaTexture
    Proxy: str
    SectionStartFrame: core_uobject.FrameNumber
    SectionEndFrame: core_uobject.FrameNumber

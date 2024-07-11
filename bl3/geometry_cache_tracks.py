from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import movie_scene


class MovieSceneGeometryCacheSection(movie_scene.MovieSceneSection):
    Params: MovieSceneGeometryCacheParams


class MovieSceneGeometryCacheTrack(movie_scene.MovieSceneNameableTrack):
    AnimationSections: unreal.WrappedArray[movie_scene.MovieSceneSection]


class MovieSceneGeometryCacheParams:
    GeometryCache: core_uobject.SoftObjectPath
    StartOffset: float
    EndOffset: float
    PlayRate: float
    bReverse: bool


class MovieSceneGeometryCacheSectionTemplate(movie_scene.MovieSceneEvalTemplate):
    Params: MovieSceneGeometryCacheSectionTemplateParameters


class MovieSceneGeometryCacheSectionTemplateParameters(MovieSceneGeometryCacheParams):
    SectionStartTime: core_uobject.FrameNumber
    SectionEndTime: core_uobject.FrameNumber

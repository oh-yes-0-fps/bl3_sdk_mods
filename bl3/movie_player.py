from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum





class MoviePlayerSettings(unreal.UObject):
    bWaitForMoviesToComplete: bool
    bMoviesAreSkippable: bool
    StartupMovies: unreal.WrappedArray[str]
    bLoopLastStartupMovie: bool



class EMoviePlaybackType(enum.Enum):
    MT_Looped = 0
    MT_LoadingLoop = 1

from dataclasses import dataclass
from typing import Callable, List, Tuple
import mods_base
from unrealsdk import logging, find_class, hooks
from mods_base import ENGINE, Library, build_mod, hook

__version_info__: tuple[int, int] = (1, 2)
__version__: str = f"{__version_info__[0]}.{__version_info__[1]}"

__all__: tuple[str, ...] = (
    "__version__",
    "__version_info__",
    "delayed",
    "periodic",
    "get_game_time",
    "get_real_time",
    "dilate_time",
    "DelayedCallback",
    "PeriodicCallback",
)

__GAMEPLAY_STATICS = find_class("GameplayStatics").ClassDefaultObject

@dataclass
class DelayedCallback:
    time: float
    callback: Callable[[], None]
    real_time: bool

@dataclass
class PeriodicCallback:
    interval: float
    callback: Callable[[float], None]
    real_time: bool
    enabled: bool

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

__TIMED_CALLBACKS: List[DelayedCallback] = []
__PERIODIC_CALLBACKS: List[Tuple[PeriodicCallback, float]] = []

def get_game_time() -> float:
    """
    Get the current game time in seconds.
    """
    return __GAMEPLAY_STATICS.GetTimeSeconds(ENGINE.GameViewport.World)

def get_real_time() -> float:
    """
    Get the current real time in seconds since game launch.
    """
    return __GAMEPLAY_STATICS.GetRealTimeSeconds(ENGINE.GameViewport.World)

def dilate_time(dilation: float) -> None:
    """
    Set the games time dilation.
    """
    __GAMEPLAY_STATICS.SetGlobalTimeDilation(ENGINE.GameViewport.World, dilation)

@hook("/Script/Engine.HUD:ReceiveDrawHUD", auto_enable=True, hook_type=hooks.Type.POST_UNCONDITIONAL)
def tick(_1, _2, _3, _4):
    game_time = get_game_time()
    real_time = get_real_time()
    to_remove = []
    for callback in __TIMED_CALLBACKS:
        if (callback.real_time and real_time >= callback.time) or (not callback.real_time and game_time >= callback.time):
            callback.callback()
            to_remove.append(callback)
    for callback in to_remove:
        __TIMED_CALLBACKS.remove(callback)
    for i, (callback, last_time) in enumerate(__PERIODIC_CALLBACKS):
        if not callback.enabled:
            continue
        now = game_time if not callback.real_time else real_time
        if (callback.real_time and real_time - last_time >= callback.interval) \
            or (not callback.real_time and game_time - last_time >= callback.interval):
                callback.callback(now - last_time)
                __PERIODIC_CALLBACKS[i] = (callback, now)

def delayed(
        callback: Callable[[], None],
        delay: float,
        real_time: bool = False) -> None:
    """
    Schedule a callback to be called after a delay.

    Args:
        callback: The callback to call.
        delay: The delay in seconds.
        real_time: Whether to use real time or game time.
    """
    now = get_game_time() if not real_time else get_real_time()
    __TIMED_CALLBACKS.append(DelayedCallback(now + delay, callback, real_time))

def periodic(
        interval: float,
        real_time: bool = False,
        auto_enabled: bool = False) -> Callable[[Callable[[float], None]], PeriodicCallback]:

    """
    A decorator to schedule a callback to be called periodically.
    Periodics are checked every frame, if you want finer resolution it's reccomended to use threading.
    If the interval is less than the frame time, the callback will be called every frame.

    Args:
        interval: The interval in seconds.
        real_time: Whether to use real time or game time.
        auto_enabled: Whether the callback should be enabled automatically.
    """

    def decorator(callback: Callable[[float], None]):
        now = get_game_time() if not real_time else get_real_time()
        __PERIODIC_CALLBACKS.append((PeriodicCallback(interval, callback, real_time, auto_enabled), now))
        if auto_enabled:
            __PERIODIC_CALLBACKS[-1][0].enable()
        return __PERIODIC_CALLBACKS[-1][0]

    return decorator

build_mod(
    mod_type=mods_base.ModType.Library,
    cls=Library,
    auto_enable=True,
)
from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine



class EyeTrackerFunctionLibrary(engine.BlueprintFunctionLibrary):

    def SetEyeTrackedPlayer(self, PlayerController: engine.PlayerController): ...
    def IsStereoGazeDataAvailable(self, ReturnValue: bool) -> bool: ...
    def IsEyeTrackerConnected(self, ReturnValue: bool) -> bool: ...
    def GetStereoGazeData(self, OutGazeData: EyeTrackerStereoGazeData, ReturnValue: bool) -> bool: ...
    def GetGazeData(self, OutGazeData: EyeTrackerGazeData, ReturnValue: bool) -> bool: ...


class EyeTrackerStereoGazeData:
    LeftEyeOrigin: core_uobject.Vector
    LeftEyeDirection: core_uobject.Vector
    RightEyeOrigin: core_uobject.Vector
    RightEyeDirection: core_uobject.Vector
    FixationPoint: core_uobject.Vector
    ConfidenceValue: float



class EyeTrackerGazeData:
    GazeOrigin: core_uobject.Vector
    GazeDirection: core_uobject.Vector
    FixationPoint: core_uobject.Vector
    ConfidenceValue: float



class EEyeTrackerStatus(enum.Enum):
    NotTracking = 0
    Tracking = 1

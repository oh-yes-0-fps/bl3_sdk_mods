from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine



class GbxTelemetryBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def SetNamedTelemetryVector(self, StatArray: K2TelemetryValues, Key: str, Value: core_uobject.Vector, Opt: ESetTelemetryValue, ReturnValue: K2TelemetryValues) -> K2TelemetryValues: ...
    def SetNamedTelemetryString(self, StatArray: K2TelemetryValues, Key: str, Value: str, Opt: ESetTelemetryValue, ReturnValue: K2TelemetryValues) -> K2TelemetryValues: ...
    def SetNamedTelemetryRotator(self, StatArray: K2TelemetryValues, Key: str, Value: core_uobject.Rotator, Opt: ESetTelemetryValue, ReturnValue: K2TelemetryValues) -> K2TelemetryValues: ...
    def SetNamedTelemetryInt(self, StatArray: K2TelemetryValues, Key: str, Value: int, Opt: ESetTelemetryValue, ReturnValue: K2TelemetryValues) -> K2TelemetryValues: ...
    def SetNamedTelemetryFloat(self, StatArray: K2TelemetryValues, Key: str, Value: float, Opt: ESetTelemetryValue, ReturnValue: K2TelemetryValues) -> K2TelemetryValues: ...
    def SetNamedTelemetryByte(self, StatArray: K2TelemetryValues, Key: str, Value: int, Opt: ESetTelemetryValue, ReturnValue: K2TelemetryValues) -> K2TelemetryValues: ...
    def SetNamedTelemetryBool(self, StatArray: K2TelemetryValues, Key: str, Value: bool, Opt: ESetTelemetryValue, ReturnValue: K2TelemetryValues) -> K2TelemetryValues: ...
    def MakeTelemetryEventRef(self, EventName: str, ReturnValue: K2EventRef) -> K2EventRef: ...
    def IsValid(self, EventRef: K2EventRef, ReturnValue: bool) -> bool: ...
    def EmitTelemetryValues(self, EventContext: str, Values: K2TelemetryValues, WorldContextObject: unreal.UObject, Guid: core_uobject.Guid, bRunOnClient: bool, ReturnValue: bool) -> bool: ...
    def EmitTelemetryEvent(self, Event: K2EventRef, EventContext: str, EventContextObject: unreal.UObject, EventInstigatorObject: unreal.UObject, WorldContextObject: unreal.UObject, Guid: core_uobject.Guid, bRunOnClient: bool, ReturnValue: bool) -> bool: ...
    def DefineTelemetryEventRef(self, EventName: str, TableDesc: str, ReturnValue: K2EventRef) -> K2EventRef: ...


class K2TelemetryValues:
    Event: K2EventRef



class K2EventRef:
    EventName: str



class ESetTelemetryValue(enum.Enum):
    IfNew = 0
    ESetTelemetryValue_MAX = 1

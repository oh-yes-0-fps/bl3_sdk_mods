from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine
from . import wwise_audio



class MaterialExpressionTimeOfDay(engine.MaterialExpression): ...


class TimeOfDayActor(engine.Actor):
    TimeOfDayComponent: TimeOfDayComponent
    DirectionalLightComponent: engine.DirectionalLightComponent
    SkyLightComponent: engine.SkyLightComponent
    AtmosphericFogComponent: engine.AtmosphericFogComponent
    ExponentialHeightFogComponent: engine.ExponentialHeightFogComponent
    StaticMeshComponent: engine.StaticMeshComponent
    PostProcessComponent: engine.PostProcessComponent
    ControlledLightActors: unreal.WrappedArray[engine.Light]
    ControlledLights: unreal.WrappedArray[ControlledLight]
    StartTime: float
    StartLayer: str
    EventListeners: unreal.WrappedArray[unreal.UObject]
    def GetDirectionalLightComponent(self, ReturnValue: engine.DirectionalLightComponent) -> engine.DirectionalLightComponent: ...
    def EnumerateLayerNames(self, OutLayerNames: unreal.WrappedArray[str]): ...
    def AddEventListener(self, InListener: unreal.UObject): ...


class TimeOfDayBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def TransitionUpOneLayer(self, WorldContextObject: unreal.UObject, TransitionDuration: float): ...
    def TransitionToLayer(self, WorldContextObject: unreal.UObject, ToLayer: str, TransitionDuration: float): ...
    def TransitionDownOneLayer(self, WorldContextObject: unreal.UObject, TransitionDuration: float): ...
    def StartTimeOfDay(self, WorldContextObject: unreal.UObject): ...
    def SetTimeOfDay(self, WorldContextObject: unreal.UObject, NewTimeOfDay: float): ...
    def PauseTimeOfDay(self, WorldContextObject: unreal.UObject): ...
    def GetTimeOfDayState(self, WorldContextObject: unreal.UObject, ReturnValue: ETimeOfDayState) -> ETimeOfDayState: ...
    def GetTimeOfDay(self, WorldContextObject: unreal.UObject, ReturnValue: float) -> float: ...
    def AddTimeOfDayListener(self, WorldContextObject: unreal.UObject, InListener: unreal.UObject): ...


class TimeOfDayComponent(engine.SceneComponent):
    TimeOfDayCycleInstanceData: TimeOfDayCycleInstanceData
    TimeOfDayCycleInstance: TimeOfDayCycleInstance
    TimeOfDay: float
    CurrentLayerName: str
    TransitionTimeLeft: float
    LastEvaluatedTime: float
    CinematicTimeOfDay: float
    bUseCinematicTimeOfDay: bool
    bShouldTick: bool
    def SetUseCinematicTimeOfDay(self, InUseCinematicTimeOfDay: bool): ...
    def SetCinematicTimeOfDay(self, InCinematicTimeOfDay: float): ...


class TimeOfDayCycle(unreal.UObject):
    ParameterCollection: engine.MaterialParameterCollection
    TimeOfDayAudioParameter: wwise_audio.WwiseRtpc
    CycleLength: float



class TimeOfDayCycleInstance(unreal.UObject):
    ParentCycle: TimeOfDayCycle
    bOverrideCycleLength: bool
    OverrideCycleLength: float
    ParameterLayerCurves: unreal.WrappedArray[LayerParameterCurves]
    PropertyLayerCurves: unreal.WrappedArray[LayerPropertyCurves]



class TimeOfDayKeyBase(unreal.UObject):
    ParentLayer: TimeOfDayLayer
    KeyTime: float
    bEnabled: bool
    KeyType: ETimeOfDayKeyType



class TimeOfDayEventKey(TimeOfDayKeyBase):
    EventName: str
    State: ETimeOfDayState



class TimeOfDayLayer(unreal.UObject):
    ParentCycle: TimeOfDayCycle
    LayerOverrideName: str
    Keys: unreal.WrappedArray[TimeOfDayKeyBase]
    OverrideScalarParameters: unreal.WrappedArray[engine.CollectionScalarParameter]
    OverrideVectorParameters: unreal.WrappedArray[engine.CollectionVectorParameter]
    OverrideScalarProperties: unreal.WrappedArray[engine.CollectionScalarParameter]
    OverrideVectorProperties: unreal.WrappedArray[engine.CollectionVectorParameter]
    OverrideVector4Properties: unreal.WrappedArray[TODCollectionVector4Parameter]



class TimeOfDayPropertyKey(TimeOfDayKeyBase):
    OverrideScalarParameters: unreal.WrappedArray[engine.CollectionScalarParameter]
    OverrideVectorParameters: unreal.WrappedArray[engine.CollectionVectorParameter]
    OverrideScalarProperties: unreal.WrappedArray[engine.CollectionScalarParameter]
    OverrideVectorProperties: unreal.WrappedArray[engine.CollectionVectorParameter]
    OverrideVector4Properties: unreal.WrappedArray[TODCollectionVector4Parameter]



class ControlledLight:
    IntensityMultiplier: float
    LightActor: engine.Light



class TimeOfDayCycleInstanceData:
    ParentCycle: TimeOfDayCycle
    bOverrideCycleLength: bool
    OverrideCycleLength: float
    LayerCurveData: unreal.WrappedArray[LayerCurveData]



class LayerCurveData:
    LayerName: str
    ParameterLayerCurves: LayerParameterCurves
    PropertyLayerCurves: LayerPropertyCurves
    LayerEvents: unreal.WrappedArray[TimeOfDayEvent]



class TimeOfDayEvent:
    EventTime: float
    EventName: str
    State: ETimeOfDayState



class LayerPropertyCurves:
    FloatProps: unreal.WrappedArray[FloatPropertyLayerCurve]
    VectorProps: unreal.WrappedArray[VectorPropertyLayerCurve]
    ColorProps: unreal.WrappedArray[ColorPropertyLayerCurve]
    Vector4Props: unreal.WrappedArray[Vector4PropertyLayerCurve]



class PropertyLayerCurveBase:
    ClassName: str
    PropertyName: str



class Vector4PropertyLayerCurve(PropertyLayerCurveBase):
    ValueCurve: engine.RichCurve



class ColorPropertyLayerCurve(PropertyLayerCurveBase):
    ValueCurve: engine.RichCurve



class VectorPropertyLayerCurve(PropertyLayerCurveBase):
    ValueCurve: engine.RichCurve



class FloatPropertyLayerCurve(PropertyLayerCurveBase):
    ValueCurve: engine.RichCurve



class LayerParameterCurves:
    FloatParams: unreal.WrappedArray[FloatParamLayerCurve]
    VectorParams: unreal.WrappedArray[VectorParamLayerCurve]



class VectorParamLayerCurve:
    ParamName: str
    ValueCurve: engine.RichCurve



class FloatParamLayerCurve:
    ParamName: str
    ValueCurve: engine.RichCurve



class TODCollectionParam:
    ParameterName: str
    ID: core_uobject.Guid



class TODVectorCollectionParam(TODCollectionParam): ...


class TODScalarCollectionParam(TODCollectionParam): ...


class TODCollectionVector4Parameter(engine.CollectionParameterBase):
    DefaultValue: core_uobject.Vector4



class TimeOfDaySaveGameData:
    PlanetCycleInfo: unreal.WrappedArray[PlanetCycleInfo]
    PlanetCycle: str



class PlanetCycleInfo:
    PlanetName: str
    CycleLength: float
    LastCachedTime: float



class ETimeOfDayState(enum.Enum):
    Morning = 0
    Day = 1
    Night = 2


class ETimeOfDayKeyType(enum.Enum):
    PropertyKey = 0
    EventKey = 1
    ETimeOfDayKeyType_MAX = 2

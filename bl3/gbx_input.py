from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine
from . import gbx_runtime
from . import input_core



class GbxInputAction(gbx_runtime.GbxDataAsset): ...


class GbxInputAction_ConsoleCommand(GbxInputAction): ...


class GbxInputActionCollection(gbx_runtime.GbxDataAsset): ...


class GbxInputActionData(gbx_runtime.GbxDataAsset):
    ActionName: str



class GbxInputActionData_Continuous_Vector(GbxInputActionData): ...


class GbxInputActionData_Discrete(GbxInputActionData): ...


class GbxInputActionEventInterpreter(unreal.UObject): ...


class GbxInputActionReceiverDelegateBinding(engine.DynamicBlueprintBinding): ...


class GbxInputActionReceiverDelegateBinding_Continuous_Vector(GbxInputActionReceiverDelegateBinding):
    InputActionReceiverDelegateBindings: unreal.WrappedArray[BlueprintGbxInputActionReceiverDelegateBinding_Continuous_Vector]



class GbxInputActionReceiverDelegateBinding_Discrete(GbxInputActionReceiverDelegateBinding):
    InputActionReceiverDelegateBindings: unreal.WrappedArray[BlueprintGbxInputActionReceiverDelegateBinding_Discrete]



class GbxInputActionReceiverInterface(core_uobject.Interface): ...


class GbxInputComponent(engine.InputComponent):
    RebindCategory: GbxInputRebindCategory
    DefaultRebindContext: GbxInputRebindContext
    InputActionEventLookupList: GbxInputActionEventLookupList
    RebindContext: GbxInputRebindContext
    def StartInputConsumeKeyImpl(self): ...
    def StartInputAction_Discrete_Impl(self, DiscreteAction: GbxInputActionData_Discrete, bConsumeEvent: bool): ...
    def InputAction_Continuous_Vector_Impl(self, AxisAction: GbxInputActionData_Continuous_Vector, Value: core_uobject.Vector): ...


class GbxInputDevice(gbx_runtime.GbxDataAsset):
    DeviceName: str



class GbxInputEventHelpers(unreal.UObject):

    def SigFunc_Button_PressPulse(self, NextPulseDelay: float): ...
    def SigFunc_Axis(self, Val: core_uobject.Vector): ...


class GbxInputKeyRebindData(engine.DataAsset):
    RebindName: str
    PlatformSupportType: EGbxInputRebindPlatformSupportType



class GbxInputKeyRebindData_Button(GbxInputKeyRebindData): ...


class GbxInputKeyRebindData_Axis(GbxInputKeyRebindData): ...


class GbxInputRebindCategory(engine.DataAsset):
    CategoryName: str
    CategoryDescription: str
    ParentCategory: GbxInputRebindCategory
    DefaultContext: GbxInputRebindContext



class GbxInputRebindContext(engine.DataAsset):
    ParentContext: GbxInputRebindContext
    ButtonBindings: unreal.WrappedArray[GbxInputRebind_Button]
    AxisBindings: unreal.WrappedArray[GbxInputRebind_Axis]
    DefaultContext: GbxInputRebindContext



class GbxPlayerInput(engine.PlayerInput):
    Categories: unreal.WrappedArray[GbxInputRebindCategory]



class BlueprintGbxInputActionReceiverDelegateBinding_Continuous_Vector:
    Action: GbxInputActionData_Continuous_Vector
    FunctionNameToBind: str
    BindingID: core_uobject.Guid



class BlueprintGbxInputActionReceiverDelegateBinding_Discrete:
    Action: GbxInputActionData_Discrete
    InputEvent: int
    FunctionNameToBind: str
    BindingID: core_uobject.Guid



class GbxInputKey:
    KeyName: str



class GbxInputAxis(GbxInputKey):
    Keys: unreal.WrappedArray[GbxInputAxisKey]



class GbxInputAxisKey:
    Key: input_core.Key
    Scale3D: core_uobject.Vector



class GbxInputButton(GbxInputKey):
    Keys: unreal.WrappedArray[input_core.Key]



class GbxInputActionEventLookupList:
    InputActionMaps: unreal.WrappedArray[GbxInputActionMap]



class GbxInputActionMap:
    InputActionData: GbxInputActionData
    Events: unreal.WrappedArray[GbxInputActionMappedEventData]



class GbxInputActionMappedEventData:
    Buttons: unreal.WrappedArray[GbxInputButton]
    Axes: unreal.WrappedArray[GbxInputAxis]
    Bindings: unreal.WrappedArray[GbxInputKeyRebindData]
    StringParams: unreal.WrappedArray[GbxInputActionMappedEventParam_String]
    NameParams: unreal.WrappedArray[GbxInputActionMappedEventParam_Name]
    IntParams: unreal.WrappedArray[GbxInputActionMappedEventParam_Int]
    FloatParams: unreal.WrappedArray[GbxInputActionMappedEventParam_Float]



class GbxInputActionMappedEventParam:
    ParamName: str



class GbxInputActionMappedEventParam_Float(GbxInputActionMappedEventParam):
    Value: float



class GbxInputActionMappedEventParam_Int(GbxInputActionMappedEventParam):
    Value: int



class GbxInputActionMappedEventParam_Name(GbxInputActionMappedEventParam):
    Value: str



class GbxInputActionMappedEventParam_String(GbxInputActionMappedEventParam):
    Value: str



class GbxInputEvent:
    ExecOutputs: unreal.WrappedArray[GbxInputEventExecOutput]
    SelfClass: engine.BlueprintGeneratedClass
    Component: GbxInputComponent
    PendingDiscreteActions: unreal.WrappedArray[GbxInputActionData_Discrete]
    bBlockParentClassEvent: bool



class GbxInputEventExecOutput:
    EventName: str
    ExecFunctionName: str
    bIsBound: bool
    FastPathData: GbxInputEventExecOutput_FastPath
    ExecFunction: core_uobject.Function



class GbxInputEventExecOutput_FastPath:
    bUsesFastpath: bool
    DirectActionData: GbxInputActionData
    bConsumeEvent: bool



class GbxInputEvent_Axis_Core(GbxInputEvent):
    AXIS: GbxInputAxis
    RebindData: GbxInputKeyRebindData_Axis



class GbxInputEvent_Axis_Basic(GbxInputEvent_Axis_Core): ...


class GbxInputEvent_Button_Core(GbxInputEvent):
    BUTTON: GbxInputButton
    RebindData: GbxInputKeyRebindData_Button



class GbxInputEvent_Button_PressHoldRelease(GbxInputEvent_Button_Core):
    HoldTime: float



class GbxInputEvent_Button_PressPulse(GbxInputEvent_Button_Core):
    DelayBeforeInitialPulse: float
    BaseDelayBetweenPulses: float
    PulseDelayAcceleration: float
    FinalDelayBetweenPulses: float



class GbxInputEvent_Button_PressRelease(GbxInputEvent_Button_Core): ...


class GbxInputEventHelper_SigFunc_Button_PressPulse_Data:
    NextPulseDelay: float



class GbxInputEventHelper_SigFunc_Axis_Data:
    Val: core_uobject.Vector



class GbxInputRebind_Axis:
    Binding: GbxInputKeyRebindData_Axis
    AXIS: GbxInputAxis



class GbxInputRebind_Button:
    Binding: GbxInputKeyRebindData_Button
    BUTTON: GbxInputButton



class EGbxButtonEvent(enum.Enum):
    Released = 0
    EGbxButtonEvent_MAX = 1


class EGbxInputEvent_Button_PressHoldRelease_Events(enum.Enum):
    Released = 0
    Held = 1


class EGbxInputEvent_Button_PressPulse_Events(enum.Enum):
    EGbxInputEvent_Button_PressPulse_MAX = 0
    InitialPulse = 1
    Pulse = 2


class EGbxInputEvent_Button_PressRelease_Events(enum.Enum):
    Released = 0
    EGbxInputEvent_Button_PressRelease_MAX = 1


class EGbxInputRebindPlatformSupportType(enum.Enum):
    Console_Only = 0
    PC_And_Console = 1

from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine
from . import umg



class CohtmlAssetReferencer(unreal.UObject): ...


class CohtmlAtlasContainedTextures(unreal.UObject): ...


class CohtmlTextureAtlasDetails(unreal.UObject):
    AtlasPath: str
    Width: int
    Height: int
    PixelFormat: str
    MaxAtlasWidth: int
    MaxAtlasHeight: int
    MaxTextureWidth: int
    MaxTextureHeight: int



class CohtmlAudioWrapper(unreal.UObject):
    Owner: unreal.UObject



class CohtmlBaseComponent(engine.ActorComponent):
    bEnableComplexCSSSupport: bool
    Texture: engine.TextureRenderTarget2D
    Filter: int
    bReceiveInput: bool
    bDelayedUpdate: bool
    AudioWrapper: CohtmlAudioWrapper
    def UpdateWholeDataModelFromStruct(self, Struct: core_uobject.StructProperty): ...
    def UpdateWholeDataModelFromObject(self, Model: unreal.UObject): ...
    def TriggerJSEvent(self, Name: str, EventData: CohtmlJSEvent): ...
    def SynchronizeModels(self): ...
    def ShowPaintRects(self, show: bool): ...
    def SetSoundAttenuation(self, Settings: engine.SoundAttenuationSettings): ...
    def Resize(self, Width: int, Height: int): ...
    def Reload(self): ...
    def Load(self, Path: str): ...
    def IsReadyToCreateView(self, ReturnValue: bool) -> bool: ...
    def IsReadyForBindings(self, ReturnValue: bool) -> bool: ...
    def HasRequestedView(self, ReturnValue: bool) -> bool: ...
    def EndDebugFrameSave(self): ...
    def EnableRendering(self, bEnabled: bool): ...
    def EnableDelayedUpdate(self, bEnabled: bool): ...
    def DebugSaveNextFrame(self): ...
    def CreateJSEvent(self, ReturnValue: CohtmlJSEvent) -> CohtmlJSEvent: ...
    def CreateDataModelFromStruct(self, Name: str, Arg: core_uobject.StructProperty): ...
    def CreateDataModelFromObject(self, Name: str, Model: unreal.UObject): ...
    def BeginDebugFrameSave(self): ...


class CohtmlBlueprintFunctionLibrary(engine.BlueprintFunctionLibrary):

    def TriggerJSEvent(self, Component: CohtmlBaseComponent, EventName: str, JSEvent: CohtmlJSEvent): ...
    def CreateJSEvent(self, WorldContextObject: unreal.UObject, ReturnValue: CohtmlJSEvent) -> CohtmlJSEvent: ...
    def AddStructArg(self, JSEvent: CohtmlJSEvent, Arg: core_uobject.StructProperty): ...
    def AddString(self, JSEvent: CohtmlJSEvent, Arg: str): ...
    def AddObject(self, JSEvent: CohtmlJSEvent, Arg: unreal.UObject): ...
    def AddInt32(self, JSEvent: CohtmlJSEvent, Arg: int): ...
    def AddFloat(self, JSEvent: CohtmlJSEvent, Arg: float): ...
    def AddByte(self, JSEvent: CohtmlJSEvent, Arg: int): ...
    def AddBool(self, JSEvent: CohtmlJSEvent, Arg: bool): ...
    def AddArrayOfStructs(self, JSEvent: CohtmlJSEvent, Arg: unreal.WrappedArray[int]): ...
    def AddArray(self, JSEvent: CohtmlJSEvent, Arg: unreal.WrappedArray[int], ArrayType: int): ...


class CohtmlComponent(CohtmlBaseComponent):
    URL: str
    Width: int
    Height: int
    ManualTexture: bool
    PrimitiveName: str



class CohtmlEventHelpers(unreal.UObject): ...


class CohtmlGameHUD(engine.HUD):
    CohtmlHUD: CohtmlHUD
    CohtmlHUDInternal: CohtmlHUD
    def SetupView(self, PageUrl: str, bEnableComplexCSSSupport: bool, bDelayedUpdate: bool): ...


class CohtmlHUD(CohtmlBaseComponent):
    HUDMaterialName: core_uobject.SoftObjectPath
    HUDMaterial: engine.Material
    HUDMaterialInstance: engine.MaterialInstanceDynamic



class CohtmlInputActor(engine.Actor):

    def ToggleCohtmlInputFocus(self): ...
    def SetLineTraceMode(self, Mode: int): ...
    def SetInputPropagationBehaviour(self, Propagation: int): ...
    def SetCohtmlViewFocus(self, NewFocusedView: CohtmlBaseComponent): ...
    def SetCohtmlInputFocus(self, FocusUI: bool): ...
    def IsCohtmlFocused(self, ReturnValue: bool) -> bool: ...
    def Initialize(self, CollisionChannel: int, AddressMode: int, RaycastQuality: int, UVChannel: int): ...
    def GetInputPropagationBehaviour(self, ReturnValue: int) -> int: ...
    def AlwaysAcceptMouseInput(self, bAccept: bool): ...


class CohtmlJSEvent(unreal.UObject):
    StructTypes: unreal.WrappedArray[unreal.UStruct]
    def AddText(self, Text: str): ...
    def AddStructArg(self, Arg: core_uobject.StructProperty): ...
    def AddString(self, str: str): ...
    def AddObject(self, Object: unreal.UObject): ...
    def AddName(self, Name: str): ...
    def AddInt32(self, integer: int): ...
    def AddFloat(self, fl: float): ...
    def AddByte(self, byte: int): ...
    def AddBool(self, B: bool): ...
    def AddArray(self, Array: unreal.WrappedArray[int]): ...


class CohtmlSettings(unreal.UObject):
    EnableLiveReload: bool
    DevToolsPort: int
    EnableLocalization: bool
    EnableBreakIterator: bool
    HandleInputOnHTMLBody: bool
    InputTransparentCssClasses: unreal.WrappedArray[str]
    ScrollDelta: float
    ShowWarningsOnScreen: bool
    LogSeverity: ECohtmlSettingsSeverity
    bRespectTitleSafeZone: bool
    bRespectLetterboxing: bool
    TickWhileGameIsPaused: bool
    bUseLowerCaseNamesForAutoExposedProperties: bool
    MSAA: ECohtmlMSAA
    FallbacksForAllFormats: unreal.WrappedArray[SingleFormatFallbacks]
    bUseInputPreprocessor: bool
    ProtocolPathDefs: unreal.WrappedArray[ProtocolPathDef]



class CohtmlSystem(engine.Actor): ...


class CohtmlWidget(umg.Widget):
    Owner: engine.Actor
    bEnableComplexCSSSupport: bool
    Filter: int
    bReceiveInput: bool
    InputPropagationBehaviour: int
    bGammaCorrectedMaterial: bool
    TickPeriodInMinimizedGame: float
    AudioWrapper: CohtmlAudioWrapper
    URL: str
    def UpdateWholeDataModelFromStruct(self, Struct: core_uobject.StructProperty): ...
    def UpdateWholeDataModelFromObject(self, Model: unreal.UObject): ...
    def TriggerJSEvent(self, Name: str, EventData: CohtmlJSEvent): ...
    def SynchronizeModels(self): ...
    def ShowPaintRects(self, show: bool): ...
    def SetSoundAttenuation(self, Settings: engine.SoundAttenuationSettings): ...
    def SetInputPropagationBehaviour(self, Propagation: int): ...
    def Reload(self): ...
    def Load(self, Path: str): ...
    def IsReadyToCreateView(self, ReturnValue: bool) -> bool: ...
    def IsReadyForBindings(self, ReturnValue: bool) -> bool: ...
    def HasRequestedView(self, ReturnValue: bool) -> bool: ...
    def GetRenderTexture(self, ReturnValue: engine.TextureRenderTarget2D) -> engine.TextureRenderTarget2D: ...
    def GetInputPropagationBehaviour(self, ReturnValue: int) -> int: ...
    def CreateJSEvent(self, ReturnValue: CohtmlJSEvent) -> CohtmlJSEvent: ...
    def CreateDataModelFromStruct(self, Name: str, Struct: core_uobject.StructProperty): ...
    def CreateDataModelFromObject(self, Name: str, Model: unreal.UObject): ...


class HummingbirdBaseComponent(CohtmlBaseComponent): ...


class HummingbirdComponent(CohtmlComponent): ...


class HummingbirdGameHUD(CohtmlGameHUD): ...


class HummingbirdHUD(CohtmlHUD): ...


class HummingbirdInputActor(CohtmlInputActor): ...


class HummingbirdSystem(CohtmlSystem): ...


class TextureAtlasMetaData: ...


class TextureAtlasMappingInfo:
    AtlasPath: str
    Width: int
    Height: int
    OriginX: int
    OriginY: int



class CohtmlSound:
    Component: engine.AudioComponent
    Stream: engine.SoundWaveProcedural



class ProtocolPathDef:
    Protocol: str
    RootPath: str
    RelativePrefix: str
    WatcherPrefix: str



class SingleFormatFallbacks:
    BaseFormat: ECohtmlImageFormat
    PossibleFallbacks: unreal.WrappedArray[ECohtmlImageFormat]



class CohtmlViewSettings:
    Width: int
    Height: int
    IsTransparent: bool
    AnimationFrameDefer: float



class ECohtmlKeys(enum.Enum):
    MiddleMouseButton = 0
    RightMouseButton = 1
    A = 2
    ThumbMouseButton2 = 3
    Pause = 4
    Left = 5
    NumPadSix = 6


class ECohtmlImageFormat(enum.Enum):
    TGA = 0
    JPEG = 1
    SVG = 2
    PKM = 3


class ECohtmlMSAA(enum.Enum):
    MSAA_2x = 0
    MSAA_4x = 1


class ECohtmlSettingsSeverity(enum.Enum):
    Debug = 0
    Info = 1
    AssertFailure = 2


class ECohtmlInputPropagationBehaviour(enum.Enum):
    Keyboard = 0
    Joystick = 1
    ECohtmlInputPropagationBehaviour_MAX = 2


class ECohtmlGamepadBehaviourOnFocusLost(enum.Enum):
    CohtmlUseCurrentState = 0
    CohtmlUseStateBeforeReset = 1


class ECohtmlInputWidgetLineTraceMode(enum.Enum):
    CohtmlInputLineTrace_Multi = 0
    CohtmlInputLineTrace_MAX = 1


class ECohtmlInputWidgetRaycastQuality(enum.Enum):
    CohtmlRaycastQuality_Balanced = 0
    CohtmlRaycastQuality_Accurate = 1

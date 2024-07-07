from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine
from . import input_core



class GFxMoviePlayer(unreal.UObject):
    SwfAssetName: str
    Root: GFxObject
    bDisplayWithHudOff: bool
    bEnableGammaCorrection: bool
    bAllowInput: bool
    bAllowFocus: bool
    bCloseOnLevelChange: bool
    bOnlyOwnerFocusable: bool
    bDiscardNonOwnerInput: bool
    bCaptureKeyboardInput: bool
    bCaptureMouseInput: bool
    bCaptureGamepadInput: bool
    bCaptureTouchInput: bool
    bIsSplitscreenLayoutModified: bool
    bShowDefaultMouseCursor: bool
    bBlurLesserMovies: bool
    bHideLesserMovies: bool
    bIsPriorityBlurred: bool
    bIsPriorityHidden: bool
    bIgnoreVisibilityEffect: bool
    bIgnoreBlurEffect: bool
    bRefreshed: bool
    bPerformHitTest: bool
    bCacheThisDefinition: bool
    bSkipUnnamedObjectsDuringPopulation: bool
    HitTestType: int
    RenderTexture: engine.TextureRenderTarget2D
    ExternalInterface: unreal.UObject
    CaptureKeys: unreal.WrappedArray[input_core.Key]
    FocusIgnoreKeys: unreal.WrappedArray[input_core.Key]
    ExternalTextures: unreal.WrappedArray[ExternalTexture]
    RenderTextureMode: int
    Priority: int
    WidgetBindings: unreal.WrappedArray[GFxWidgetBinding]
    SplitscreenLayoutYAdjust: int
    bIgnoresSafeFrameScaling: bool
    bIgnoresHDRCalibration: bool
    CachedMovieClipsArray: unreal.WrappedArray[GFxObject]
    def Start(self, bRefresh: bool, ReturnValue: bool) -> bool: ...
    def SetVisible(self, bVisible: bool): ...
    def SetVisibility(self, MovieClipName: str, bVisible: bool): ...
    def SetViewScaleMode(self, ScaleMode: int): ...
    def SetViewport(self, X: int, Y: int, Width: int, Height: int): ...
    def SetView3D(self, ViewTransform: core_uobject.Transform): ...
    def SetVariableValueArray(self, MovieClipName: str, MemberName: str, Value: unreal.WrappedArray[ASValue]): ...
    def SetVariableValue(self, MovieClipName: str, MemberName: str, Value: ASValue): ...
    def SetTimingMode(self, TimingMode: int): ...
    def SetScale(self, MovieClipName: str, XScale: float, YScale: float): ...
    def SetPosition(self, MovieClipName: str, X: float, Y: float): ...
    def SetPerspective3D(self, PerspectiveTransform: ASPerspectiveTransform): ...
    def SetPause(self, bPausePlayback: bool): ...
    def SetMovieCanReceiveInput(self, bCanReceiveInput: bool): ...
    def SetMovieCanReceiveFocus(self, bCanReceiveFocus: bool): ...
    def SetFocusIgnoreKeys(self, Keys: unreal.WrappedArray[input_core.Key]): ...
    def SetExternalTexture(self, Resource: str, Texture: engine.Texture): ...
    def SetDisplayTransform(self, MovieClipName: str, DisplayTransform: core_uobject.Transform): ...
    def SetDisplayInfo(self, MovieClipName: str, Info: ASDisplayInfo): ...
    def SetColorTransform(self, MovieClipName: str, UnrealColorTransform: ASColorTransform): ...
    def SetCaptureKeys(self, Keys: unreal.WrappedArray[input_core.Key]): ...
    def SetAlignment(self, Align: int): ...
    def ReceiveGFxCommand(self, Command: str, Arguments: str): ...
    def OpenMovie(self, SwfMovie: SwfMovie, ExternalScriptInterface: unreal.UObject, RenderToTexture: engine.TextureRenderTarget2D, MoviePlayer: GFxMoviePlayer, DisplayWithHudOff: bool, bRefresh: bool, ReturnValue: GFxMoviePlayer) -> GFxMoviePlayer: ...
    def OnTick(self, DeltaTime: float): ...
    def OnStart(self): ...
    def OnGameTick(self, DeltaTime: float): ...
    def OnFocusLost(self, LocalPlayerIndex: int): ...
    def OnFocusGained(self, LocalPlayerIndex: int): ...
    def OnClose(self): ...
    def IsVisible(self, ReturnValue: bool) -> bool: ...
    def IsPaused(self, ReturnValue: bool) -> bool: ...
    def Invoke(self, MovieClipName: str, FunctionName: str, Params: unreal.WrappedArray[ASValue], ReturnValue: ASValue) -> ASValue: ...
    def GotoAndStopI(self, MovieClipName: str, Frame: int): ...
    def GotoAndStop(self, MovieClipName: str, Frame: str): ...
    def GotoAndPlayI(self, MovieClipName: str, Frame: int): ...
    def GotoAndPlay(self, MovieClipName: str, Frame: str): ...
    def GetVisibility(self, MovieClipName: str, ReturnValue: bool) -> bool: ...
    def GetView3D(self, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def GetVariableValueArray(self, MovieClipName: str, MemberName: str, ReturnValue: unreal.WrappedArray[ASValue]) -> unreal.WrappedArray[ASValue]: ...
    def GetVariableValue(self, MovieClipName: str, MemberName: str, ReturnValue: ASValue) -> ASValue: ...
    def GetScale(self, MovieClipName: str, XScale: float, YScale: float, ReturnValue: bool) -> bool: ...
    def GetPosition(self, MovieClipName: str, X: float, Y: float, ReturnValue: bool) -> bool: ...
    def GetPerspective3D(self, ReturnValue: ASPerspectiveTransform) -> ASPerspectiveTransform: ...
    def GetMovieClip(self, MovieClipName: str, ReturnValue: GFxObject) -> GFxObject: ...
    def GetDisplayTransform(self, MovieClipName: str, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def GetDisplayInfo(self, MovieClipName: str, ReturnValue: ASDisplayInfo) -> ASDisplayInfo: ...
    def GetColorTransform(self, MovieClipName: str, ReturnValue: ASColorTransform) -> ASColorTransform: ...
    def Close(self): ...


class GFxObject(unreal.UObject):

    def SetVisible(self, bVisible: bool): ...
    def SetScale(self, XScale: float, YScale: float): ...
    def SetPosition(self, X: float, Y: float): ...
    def SetMemberValueArray(self, MoviePlayer: GFxMoviePlayer, MemberName: str, Input: unreal.WrappedArray[ASValue]): ...
    def SetMemberValue(self, MemberName: str, Input: ASValue): ...
    def SetDisplayTransform(self, DisplayTransform: core_uobject.Transform): ...
    def SetDisplayInfo(self, UnrealDisplayInfo: ASDisplayInfo): ...
    def SetColorTransform(self, UnrealColorTransform: ASColorTransform): ...
    def Invoke(self, FunctionName: str, Params: unreal.WrappedArray[ASValue], ReturnValue: ASValue) -> ASValue: ...
    def GotoAndStopI(self, FrameNumber: int): ...
    def GotoAndStop(self, FrameString: str): ...
    def GotoAndPlayI(self, FrameNumber: int): ...
    def GotoAndPlay(self, FrameString: str): ...
    def GetVisible(self, ReturnValue: bool) -> bool: ...
    def GetScale(self, XScale: float, YScale: float, ReturnValue: bool) -> bool: ...
    def GetPosition(self, X: float, Y: float, ReturnValue: bool) -> bool: ...
    def GetMemberValueArray(self, MemberName: str, ReturnValue: unreal.WrappedArray[ASValue]) -> unreal.WrappedArray[ASValue]: ...
    def GetMemberValue(self, MemberName: str, ReturnValue: ASValue) -> ASValue: ...
    def GetDisplayTransform(self, ReturnValue: core_uobject.Transform) -> core_uobject.Transform: ...
    def GetDisplayInfo(self, ReturnValue: ASDisplayInfo) -> ASDisplayInfo: ...
    def GetColorTransform(self, ReturnValue: ASColorTransform) -> ASColorTransform: ...


class ScaleformBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def OpenMovie(self, Movie: SwfMovie, ExternalInterface: unreal.UObject, RenderTexture: engine.TextureRenderTarget2D, MoviePlayer: GFxMoviePlayer, DisplayWithHudOff: bool, StartPaused: bool, ReturnValue: GFxMoviePlayer) -> GFxMoviePlayer: ...
    def InvokeNoParams(self, MoviePlayer: GFxMoviePlayer, FunctionName: str, ReturnValue: ASValue) -> ASValue: ...
    def Invoke(self, MoviePlayer: GFxMoviePlayer, FunctionName: str, Params: unreal.WrappedArray[ASValue], ReturnValue: ASValue) -> ASValue: ...
    def GetVariable(self, MoviePlayer: GFxMoviePlayer, VariablePath: str, ReturnValue: GFxObject) -> GFxObject: ...
    def GetMovieClip(self, MoviePlayer: GFxMoviePlayer, MovieClipName: str, ReturnValue: GFxObject) -> GFxObject: ...
    def GetMember(self, MoviePlayer: GFxMoviePlayer, MemberName: str, ReturnValue: GFxObject) -> GFxObject: ...
    def GetAllGFxMoviePlayerOfClass(self, WorldContextObject: unreal.UObject, FoundGFxMoviePlayer: unreal.WrappedArray[GFxMoviePlayer], GFxMoviePlayerClass: unreal.UClass, VisibleOnly: bool): ...
    def CloseMovie(self, MoviePlayer: GFxMoviePlayer): ...


class SwfMovie(unreal.UObject):
    bUseGFxExport: bool
    bOptimizeForMobiles: bool
    bSetSRGBOnImportedTextures: bool
    bPackTextures: bool
    PackTextureSize: int
    bArePackedTextures4k: bool
    bForceSquarePacking: bool
    TextureRescale: int
    TextureFormat: str
    bReplaceImages: bool
    SourceFile: str
    bUseOrderedLoading: bool
    bLoadImageFiles: bool
    TextureLoadPriority: int
    FontMappings: unreal.WrappedArray[str]
    SourceFileTimestamp: str
    RawData: unreal.WrappedArray[int]
    ReferencedAssets: unreal.WrappedArray[unreal.UObject]
    SoftReferencedTextures: unreal.WrappedArray[ScaleformTextureReference]
    InstanceNameAndPathBindings: unreal.WrappedArray[FlashNativeBindingInfo]
    TransientInstanceNameAndPathBindings: unreal.WrappedArray[FlashNativeBindingInfo]



class ASColorTransform:
    Multiply: core_uobject.LinearColor
    Add: core_uobject.LinearColor



class ASDisplayInfo:
    Position: core_uobject.Vector
    Scale: core_uobject.Vector
    Rotation: float
    XRotation: float
    YRotation: float
    Alpha: float
    Visible: bool



class ASValue:
    ASType: int
    ASBoolean: bool
    ASInt: int
    AsNumber: float
    AsString: str
    AsObject: GFxObject



class ASPerspectiveTransform:
    Row1: core_uobject.Vector4
    Row2: core_uobject.Vector4
    Row3: core_uobject.Vector4



class GFxWidgetBinding:
    WidgetName: str
    WidgetClass: unreal.UClass



class ExternalTexture:
    Resource: str
    Texture: engine.Texture



class ScaleformTextureReference: ...


class ScaleformAssetReference: ...


class FlashNativeBindingInfo:
    InstanceName: str
    FullPath: str
    ClosestParentInstanceName: str



class GbxGFxBounds:
    Top: float
    Left: float
    Bottom: float
    Right: float



class EASType(enum.Enum):
    Null = 0
    Boolean = 1
    Number = 2
    DisplayObject = 3


class EGFxAlign(enum.Enum):
    TopCenter = 0
    BottomCenter = 1
    CenterRight = 2
    BottomRight = 3


class EGFxTimingMode(enum.Enum):
    EGFxTimingMode_MAX = 0
    Real = 1


class EGFxScaleMode(enum.Enum):
    ShowAll = 0
    ExactFit = 1
    EGFxScaleMode_MAX = 2


class EGFxRenderTextureMode(enum.Enum):
    AlphaComposite = 0
    Alpha = 1


class GFxHitTestType(enum.Enum):
    HitTest_ButtonEvents = 0
    HitTest_Shapes = 1
    HitTest_MAX = 2


class EGbxGFxMovieGetChildStrategy(enum.Enum):
    ByTable = 0
    ByTableThenPath = 1
    ByPathThenTable = 2
    EGbxGFxMovieGetChildStrategy_MAX = 3


class FlashTextureRescale(enum.Enum):
    FlashTextureScale_Low = 0
    FlashTextureScale_NextLow = 1
    FlashTextureScale_None = 2

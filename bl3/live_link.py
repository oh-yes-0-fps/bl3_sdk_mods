from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import engine
from . import live_link_interface



class LiveLinkBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def TransformNames(self, SubjectFrameHandle: SubjectFrameHandle, TransformNames: unreal.WrappedArray[str]): ...
    def TransformName(self, LiveLinkTransform: LiveLinkTransform, Name: str): ...
    def RequestShutdown(self, SourceHandle: LiveLinkSourceHandle, ReturnValue: bool) -> bool: ...
    def ParentBoneSpaceTransform(self, LiveLinkTransform: LiveLinkTransform, Transform: core_uobject.Transform): ...
    def NumberOfTransforms(self, SubjectFrameHandle: SubjectFrameHandle, ReturnValue: int) -> int: ...
    def IsSourceStillValid(self, SourceHandle: LiveLinkSourceHandle, ReturnValue: bool) -> bool: ...
    def HasParent(self, LiveLinkTransform: LiveLinkTransform, ReturnValue: bool) -> bool: ...
    def GetTransformByName(self, SubjectFrameHandle: SubjectFrameHandle, TransformName: str, LiveLinkTransform: LiveLinkTransform): ...
    def GetTransformByIndex(self, SubjectFrameHandle: SubjectFrameHandle, TransformIndex: int, LiveLinkTransform: LiveLinkTransform): ...
    def GetSourceType(self, SourceHandle: LiveLinkSourceHandle, ReturnValue: str) -> str: ...
    def GetSourceStatus(self, SourceHandle: LiveLinkSourceHandle, ReturnValue: str) -> str: ...
    def GetSourceMachineName(self, SourceHandle: LiveLinkSourceHandle, ReturnValue: str) -> str: ...
    def GetRootTransform(self, SubjectFrameHandle: SubjectFrameHandle, LiveLinkTransform: LiveLinkTransform): ...
    def GetParent(self, LiveLinkTransform: LiveLinkTransform, Parent: LiveLinkTransform): ...
    def GetMetadata(self, SubjectFrameHandle: SubjectFrameHandle, MetaData: SubjectMetadata): ...
    def GetChildren(self, LiveLinkTransform: LiveLinkTransform, Children: unreal.WrappedArray[LiveLinkTransform]): ...
    def ComponentSpaceTransform(self, LiveLinkTransform: LiveLinkTransform, Transform: core_uobject.Transform): ...
    def ChildCount(self, LiveLinkTransform: LiveLinkTransform, ReturnValue: int) -> int: ...


class LiveLinkComponent(engine.ActorComponent):

    def GetSubjectData(self, SubjectName: str, bSuccess: bool, SubjectFrameHandle: SubjectFrameHandle): ...
    def GetAvailableSubjectNames(self, SubjectNames: unreal.WrappedArray[str]): ...


class LiveLinkDrivenComponent(engine.ActorComponent):
    SubjectName: live_link_interface.LiveLinkSubjectName
    ActorTransformBone: str
    bModifyActorTransform: bool
    bSetRelativeLocation: bool



class LiveLinkInstance(engine.AnimInstance): ...


class LiveLinkMessageBusFinder(unreal.UObject):

    def GetAvailableProviders(self, WorldContextObject: unreal.UObject, LatentInfo: engine.LatentActionInfo, Duration: float, AvailableProviders: unreal.WrappedArray[ProviderPollResult]): ...
    def ConstructMessageBusFinder(self, ReturnValue: LiveLinkMessageBusFinder) -> LiveLinkMessageBusFinder: ...
    def ConnectToProvider(self, Provider: ProviderPollResult, SourceHandle: LiveLinkSourceHandle): ...


class LiveLinkRetargetAsset(unreal.UObject): ...


class LiveLinkRemapAsset(LiveLinkRetargetAsset):

    def GetRemappedCurveName(self, CurveName: str, ReturnValue: str) -> str: ...
    def GetRemappedBoneName(self, BoneName: str, ReturnValue: str) -> str: ...


class AnimNode_LiveLinkPose(engine.AnimNode_Base):
    SubjectName: str
    RetargetAsset: unreal.UClass
    CurrentRetargetAsset: LiveLinkRetargetAsset



class LiveLinkSourceHandle: ...


class SubjectFrameHandle: ...


class LiveLinkTransform: ...


class CachedSubjectFrame: ...


class SubjectMetadata:
    SceneTimecode: core_uobject.Timecode
    SceneFramerate: core_uobject.FrameRate



class LiveLinkInstanceProxy(engine.AnimInstanceProxy): ...


class ProviderPollResult:
    Name: str
    MachineName: str



class LiveLinkRetargetAssetReference:
    CurrentRetargetAsset: LiveLinkRetargetAsset



class LiveLinkVirtualSubject:
    Subjects: unreal.WrappedArray[str]
    Source: core_uobject.Guid


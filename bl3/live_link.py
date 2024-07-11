from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject
from . import engine
from . import live_link_interface


class LiveLinkBlueprintLibrary(engine.BlueprintFunctionLibrary):

    def TransformNames(
        self,
        SubjectFrameHandle: SubjectFrameHandle,
        TransformNames: unreal.WrappedArray[str],
    ): ...
    def TransformName(self, LiveLinkTransform: LiveLinkTransform, Name: str): ...
    def RequestShutdown(self, SourceHandle: LiveLinkSourceHandle) -> bool: ...
    def ParentBoneSpaceTransform(
        self, LiveLinkTransform: LiveLinkTransform, Transform: core_uobject.Transform
    ): ...
    def NumberOfTransforms(self, SubjectFrameHandle: SubjectFrameHandle) -> int: ...
    def IsSourceStillValid(self, SourceHandle: LiveLinkSourceHandle) -> bool: ...
    def HasParent(self, LiveLinkTransform: LiveLinkTransform) -> bool: ...
    def GetTransformByName(
        self,
        SubjectFrameHandle: SubjectFrameHandle,
        TransformName: str,
        LiveLinkTransform: LiveLinkTransform,
    ): ...
    def GetTransformByIndex(
        self,
        SubjectFrameHandle: SubjectFrameHandle,
        TransformIndex: int,
        LiveLinkTransform: LiveLinkTransform,
    ): ...
    def GetSourceType(self, SourceHandle: LiveLinkSourceHandle) -> str: ...
    def GetSourceStatus(self, SourceHandle: LiveLinkSourceHandle) -> str: ...
    def GetSourceMachineName(self, SourceHandle: LiveLinkSourceHandle) -> str: ...
    def GetRootTransform(
        self,
        SubjectFrameHandle: SubjectFrameHandle,
        LiveLinkTransform: LiveLinkTransform,
    ): ...
    def GetParent(
        self, LiveLinkTransform: LiveLinkTransform, Parent: LiveLinkTransform
    ): ...
    def GetMetadata(
        self, SubjectFrameHandle: SubjectFrameHandle, MetaData: SubjectMetadata
    ): ...
    def GetCurves(self, SubjectFrameHandle: SubjectFrameHandle, Curves: Any): ...
    def GetChildren(
        self,
        LiveLinkTransform: LiveLinkTransform,
        Children: unreal.WrappedArray[LiveLinkTransform],
    ): ...
    def ComponentSpaceTransform(
        self, LiveLinkTransform: LiveLinkTransform, Transform: core_uobject.Transform
    ): ...
    def ChildCount(self, LiveLinkTransform: LiveLinkTransform) -> int: ...


class LiveLinkComponent(engine.ActorComponent):
    OnLiveLinkUpdated: Any

    def GetSubjectData(
        self, SubjectName: str, bSuccess: bool, SubjectFrameHandle: SubjectFrameHandle
    ): ...
    def GetAvailableSubjectNames(self, SubjectNames: unreal.WrappedArray[str]): ...


class LiveLinkDrivenComponent(engine.ActorComponent):
    SubjectName: live_link_interface.LiveLinkSubjectName
    ActorTransformBone: str
    bModifyActorTransform: bool
    bSetRelativeLocation: bool


class LiveLinkInstance(engine.AnimInstance): ...


class LiveLinkMessageBusFinder(unreal.UObject):

    def GetAvailableProviders(
        self,
        WorldContextObject: unreal.UObject,
        LatentInfo: engine.LatentActionInfo,
        Duration: float,
        AvailableProviders: unreal.WrappedArray[ProviderPollResult],
    ): ...
    def ConstructMessageBusFinder(self) -> LiveLinkMessageBusFinder: ...
    def ConnectToProvider(
        self, Provider: ProviderPollResult, SourceHandle: LiveLinkSourceHandle
    ): ...


class LiveLinkRetargetAsset(unreal.UObject): ...


class LiveLinkRemapAsset(LiveLinkRetargetAsset):

    def RemapCurveElements(self, CurveItems: Any): ...
    def GetRemappedCurveName(self, CurveName: str) -> str: ...
    def GetRemappedBoneName(self, BoneName: str) -> str: ...


class AnimNode_LiveLinkPose(engine.AnimNode_Base):
    SubjectName: str
    RetargetAsset: unreal.UClass
    CurrentRetargetAsset: LiveLinkRetargetAsset


class LiveLinkSourceHandle: ...


class SubjectFrameHandle: ...


class LiveLinkTransform: ...


class CachedSubjectFrame: ...


class SubjectMetadata:
    StringMetadata: Any
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

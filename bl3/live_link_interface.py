from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject



class LiveLinkSourceFactory(unreal.UObject): ...


class LiveLinkSourceSettings(unreal.UObject):
    InterpolationSettings: LiveLinkInterpolationSettings



class LiveLinkRefSkeleton:
    BoneNames: unreal.WrappedArray[str]
    BoneParents: unreal.WrappedArray[int]



class LiveLinkInterpolationSettings:
    bUseInterpolation: bool
    InterpolationOffset: float



class LiveLinkFrameData:
    Transforms: unreal.WrappedArray[core_uobject.Transform]
    CurveElements: unreal.WrappedArray[LiveLinkCurveElement]
    WorldTime: LiveLinkWorldTime
    MetaData: LiveLinkMetaData



class LiveLinkMetaData:
    SceneTime: LiveLinkTimeCode



class LiveLinkTimeCode_Base_DEPRECATED:
    Seconds: int
    Frames: int
    FrameRate: LiveLinkFrameRate



class LiveLinkFrameRate(core_uobject.FrameRate): ...


class LiveLinkTimeCode(LiveLinkTimeCode_Base_DEPRECATED): ...


class LiveLinkWorldTime:
    Time: float
    Offset: float



class LiveLinkCurveElement:
    CurveName: str
    CurveValue: float



class LiveLinkSubjectName:
    Name: str


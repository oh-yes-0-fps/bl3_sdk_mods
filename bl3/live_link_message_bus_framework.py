from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject
from . import live_link_interface



class LiveLinkClearSubject:
    SubjectName: str



class LiveLinkHeartbeatMessage: ...


class LiveLinkConnectMessage: ...


class LiveLinkPongMessage:
    ProviderName: str
    MachineName: str
    PollRequest: core_uobject.Guid



class LiveLinkPingMessage:
    PollRequest: core_uobject.Guid



class LiveLinkSubjectFrameMessage:
    SubjectName: str
    Transforms: unreal.WrappedArray[core_uobject.Transform]
    Curves: unreal.WrappedArray[live_link_interface.LiveLinkCurveElement]
    MetaData: live_link_interface.LiveLinkMetaData
    Time: float



class LiveLinkSubjectDataMessage:
    RefSkeleton: live_link_interface.LiveLinkRefSkeleton
    SubjectName: str


from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum


from . import core_uobject



class GbxTwitchSettings(unreal.UObject):
    AppClientID: str
    AppClientID_Stable: str
    AppClientID_Cert: str
    ExtensionID: str
    GameID: str



class TwitchAPI(unreal.UObject): ...


class TwitchIRCClient(unreal.UObject):
    PendingChannels: unreal.WrappedArray[TwitchChannel]
    ConnectedChannels: unreal.WrappedArray[TwitchChannel]
    IRCCommandsMessages: unreal.WrappedArray[str]
    def SendChatMessage(self, ChannelName: str, MESSAGE: str): ...
    def QuitChannel(self, ChannelName: str): ...
    def InitChatBot(self): ...
    def ExitChatBot(self): ...


class TwitchStreamInfo:
    StreamID: str
    UserID: str
    UserDisplayName: str
    UserLogin: str
    GameID: str
    GameName: str
    bIsLive: bool
    Title: str
    ViewerCount: int
    StartedAt: str
    Language: str



class TwitchChannelMessage:
    Channel: str
    UserName: str
    UserMessage: str



class TwitchStreamsRequest:
    RequestGuid: core_uobject.Guid
    StreamsFound: unreal.WrappedArray[TwitchStreamInfo]
    bResponseReceived: bool
    bGameNameResolved: bool
    bUserNameResolved: bool
    MaxNbStreams: int
    GameName: str
    UserLogin: str
    Language: str



class TwitchActiveExtensionsInfo:
    PanelExtensions: unreal.WrappedArray[TwitchExtensionInfo]
    OverlayExtensions: unreal.WrappedArray[TwitchExtensionInfo]
    ComponentExtensions: unreal.WrappedArray[TwitchExtensionInfo]



class TwitchExtensionInfo:
    ID: str
    Version: str
    Name: str
    bCanActivate: bool
    Type: unreal.WrappedArray[str]
    bActive: bool



class TwitchUserInfo:
    ID: str
    Login: str
    DisplayName: str
    Type: str
    Description: str
    ViewCount: int



class TwitchChannel:
    ChannelName: str
    ChannelDescription: str
    ChannelActiveUsers: unreal.WrappedArray[str]
    IncomingChannelMessage: unreal.WrappedArray[TwitchChannelMessage]


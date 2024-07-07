from __future__ import annotations # type: ignore
from unrealsdk import unreal
import typing
import enum





class DeviceType(enum.Enum):
    SpecificDevice = 0
    DefaultSystemDevice = 1
    DeviceType_MAX = 2


class EAudioFadeModel(enum.Enum):
    ExponentialByDistance = 0
    LinearByDistance = 1


class ChannelType(enum.Enum):
    Positional = 0
    Echo = 1


class ConnectionState(enum.Enum):
    ConnectionState_MAX = 0
    Connecting = 1
    Connected = 2


class ParticipantSpeakingUpdateRate(enum.Enum):
    Never = 0
    Update1Hz = 1
    Update10Hz = 2


class TransmissionMode(enum.Enum):
    Single = 0
    All = 1


class SubscriptionReply(enum.Enum):
    Block = 0
    SubscriptionReply_MAX = 1


class SubscriptionMode(enum.Enum):
    Block = 0
    Defer = 1


class LoginState(enum.Enum):
    LoggingIn = 0
    LoggedIn = 1
    LoginState_MAX = 2


class TTSMessageState(enum.Enum):
    Enqueued = 0
    TTSMessageState_MAX = 1


class TTSDestination(enum.Enum):
    LocalPlayback = 0
    RemoteTransmissionWithLocalPlayback = 1
    QueuedLocalPlayback = 2


class PresenceStatus(enum.Enum):
    Available = 0
    Away = 1
    Chat = 2

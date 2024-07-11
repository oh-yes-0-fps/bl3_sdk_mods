from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import engine
from . import gbx_runtime
from . import audio_mixer


class BeaconChannel(engine.Channel): ...


class DownloadableContentData(gbx_runtime.GbxDataAsset):
    PackageData: DownloadablePackageData
    LicenseData: DownloadableContentLicenseData
    ContentId: int
    ContentDisplayName: str
    NewDLCDisplayName: str


class DownloadableContentLicenseData(gbx_runtime.GbxDataAsset):
    PackageData: DownloadablePackageData
    LicenseName: str
    DisplayName: str
    LicenseId: int


class DownloadablePackageData(engine.PrimaryDataAsset):
    PackageId: int
    PackageDisplayName: str
    DLCName: str
    Licenses: unreal.WrappedArray[DownloadableContentLicenseData]


class DownloadablePackageLicenseItem(engine.DataAsset):
    LicenseMask: int


class IpNetDriver(engine.NetDriver):
    LogPortUnreach: bool
    AllowPlayerPortUnreach: bool
    MaxPortCountToTry: int


class IpBeaconNetDriver(IpNetDriver): ...


class IpConnection(engine.NetConnection):
    TravelTimeout: float


class OnlineBeacon(unreal.UObject):
    BeaconConnectionInitialTimeout: float
    BeaconConnectionTimeout: float
    NetDriverName: str
    NetDriver: engine.NetDriver


class OnlineBeaconClient(OnlineBeacon):
    BeaconConnection: engine.NetConnection
    ConnectionState: EBeaconConnectionState


class OnlineBeaconHost(OnlineBeacon):
    ListenPort: int
    MaxAllowedRemotePlayers: int


class OnlineEngineInterfaceImpl(engine.OnlineEngineInterface): ...


class OnlinePIESettings(engine.DeveloperSettings):
    bOnlinePIEEnabled: bool
    Logins: unreal.WrappedArray[PIELoginSettingsInternal]


class OnlineSessionClient(engine.OnlineSession):
    bIsFromInvite: bool
    bHandlingDisconnect: bool


class VoipListenerSynthComponent(audio_mixer.SynthComponent):

    def IsIdling(self) -> bool: ...


class PIELoginSettingsInternal:
    ID: str
    Token: str
    Type: str
    TokenBytes: unreal.WrappedArray[int]


class EBeaconConnectionState(enum.Enum):
    Closed = 0
    EBeaconConnectionState_MAX = 1
    Pending = 2

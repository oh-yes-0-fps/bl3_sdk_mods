from __future__ import annotations  # type: ignore
from unrealsdk import unreal
from typing import Any
import enum


from . import core_uobject


class ConsoleSettings(unreal.UObject):
    MaxScrollbackSize: int
    ManualAutoCompleteList: unreal.WrappedArray[AutoCompleteCommand]
    AutoCompleteMapPaths: unreal.WrappedArray[str]
    BackgroundOpacityPercentage: float
    bOrderTopToBottom: bool
    InputColor: core_uobject.Color
    HistoryColor: core_uobject.Color
    AutoCompleteCommandColor: core_uobject.Color
    AutoCompleteCVarColor: core_uobject.Color
    AutoCompleteFadedColor: core_uobject.Color


class GameMapsSettings(unreal.UObject):
    EditorStartupMap: core_uobject.SoftObjectPath
    LocalMapOptions: str
    TransitionMap: core_uobject.SoftObjectPath
    bUseSplitscreen: bool
    TwoPlayerSplitscreenLayout: int
    ThreePlayerSplitscreenLayout: int
    bOffsetPlayerGamepadIds: bool
    GameInstanceClass: core_uobject.SoftClassPath
    GameDefaultMap: core_uobject.SoftObjectPath
    ServerDefaultMap: core_uobject.SoftObjectPath
    GlobalDefaultGameMode: core_uobject.SoftClassPath
    GlobalDefaultServerGameMode: core_uobject.SoftClassPath
    GameModeMapPrefixes: unreal.WrappedArray[GameModeName]
    GameModeClassAliases: unreal.WrappedArray[GameModeName]


class GameNetworkManagerSettings(unreal.UObject):
    MinDynamicBandwidth: int
    MaxDynamicBandwidth: int
    TotalNetBandwidth: int
    BadPingThreshold: int
    bIsStandbyCheckingEnabled: bool
    StandbyRxCheatTime: float
    StandbyTxCheatTime: float
    PercentMissingForRxStandby: float
    PercentMissingForTxStandby: float
    PercentForBadPing: float
    JoinInProgressStandbyWaitTime: float


class GameSessionSettings(unreal.UObject):
    MaxSpectators: int
    MaxPlayers: int
    bRequiresPushToTalk: bool


class GeneralEngineSettings(unreal.UObject): ...


class GeneralProjectSettings(unreal.UObject):
    CompanyName: str
    CompanyDistinguishedName: str
    CopyrightNotice: str
    Description: str
    Homepage: str
    LicensingTerms: str
    PrivacyPolicy: str
    ProjectID: core_uobject.Guid
    ProjectName: str
    ProjectVersion: str
    SupportContact: str
    ProjectDisplayedTitle: str
    ProjectDebugTitleInfo: str
    bShouldWindowPreserveAspectRatio: bool
    bUseBorderlessWindow: bool
    bStartInVR: bool
    bStartInAR: bool
    bSupportAR: bool
    bAllowWindowResize: bool
    bAllowClose: bool
    bAllowMaximize: bool
    bAllowMinimize: bool


class HudSettings(unreal.UObject):
    bShowHUD: bool
    DebugDisplay: unreal.WrappedArray[str]


class AutoCompleteCommand:
    Command: str
    Desc: str


class GameModeName:
    Name: str
    GameMode: core_uobject.SoftClassPath


class EThreePlayerSplitScreenType(enum.Enum):
    FavorBottom = 0
    RespectTwoPlayerSplit_FavorTopLeft = 1
    RespectTwoPlayerSplit_FavorBottomLeft = 2


class ETwoPlayerSplitScreenType(enum.Enum):
    Vertical = 0
    ETwoPlayerSplitScreenType_MAX = 1

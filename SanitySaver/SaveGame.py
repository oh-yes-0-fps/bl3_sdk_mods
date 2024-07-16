from os import getlogin, mkdir
from os.path import exists
from typing import Any, Callable, Optional, cast, reveal_type
from bl3 import get_pc
from bl3.oak_game import GFxPauseMenu, OakSaveGame
from bl3.scaleform_ui import GFxMoviePlayer
from unrealsdk import logging
from unrealsdk.hooks import Type
from unrealsdk.unreal import BoundFunction, UObject, WrappedStruct
from mods_base import hook
import json
import bl3 as game

SAVE_PROPERTIES = set(
    [
        'SaveGameId',
        'bLevelledSaveNeedsFixup',
        'LastSaveTimestamp',
        'TimePlayedSeconds',
        'AccumulatedLevelPersistenceResetTimerSeconds',
        'LevelPersistenceData',
        'PlayerClassData',
        'ResourcePools',
        'SavedRegions',
        'ExperiencePoints',
        'GameStatsData',
        'InventoryCategoryList',
        'InventoryItems',
        'EquippedInventoryList',
        'ActiveWeaponList',
        'AbilityData',
        'LastPlayThroughIndex',
        'PlaythroughsCompleted',
        'bShowNewPlaythroughNotification',
        'MissionPlaythroughsData',
        'ActiveTravelStationsForPlaythrough',
        'DiscoveryData',
        'LastActiveTravelStationForPlaythrough',
        'VehiclesUnlockedData',
        'VehiclePartsUnlocked',
        'VehicleLoadouts',
        'VehicleLastLoadoutIndex',
        'OakChallengeData',
        'SDUList',
        'SelectedCustomizations',
        'EquippedEmoteCustomizations',
        'SelectedColorCustomizations',
        'CrewQuartersRoom',
        'CrewQuartersGunRack',
        'UnlockedEchoLogs',
        'bHasPlayedSpecialEchoLogInsertAlready',
        'NicknameMappings',
        'GameStateSaveDataForPlaythrough',
        'ChallengeCategoryCompletionPcts',
        'CharacterSlotSaveGameData',
        'UITrackingSaveGameData',
        'PreferredGroupMode',
        'TimeOfDayData',
        'ZoneMapFODSavedData',
        'bIsNetReplicating',
        'CharacterGuardianRank',
        'ProfileChallengeDataForSerialization',
        'bOptionalObjectiveRewardFixupApplied',
        'bVehiclePartRewardsFixupApplied',
        'bLevelledSaveVehiclePartRewardsFixupApplied',
        'LastActiveLeague',
        'LastActiveLeagueInstance',
        'ActiveLeagueInstanceForEvent',
        'CurrentVaultCardDaySeed',
        'CurrentVaultCardWeekSeed',
        'PreferredCharacterName',
        'NameCharacterLimit',
        'GuardianRank',
        'LastActiveTravelStation',
        'GameStateSaveData',
        'ActiveTravelStations'
    ]
)

class PySaveGame:
    """
    A Pyhton Accessible Save Game

    Structured as a dictionary, with the keys being the names of the save game properties.

    Extends the save game object and stores that data in a json file

    Gets current save game so will change what save its interfacing with upon changing characters
    """
    def __init__(self):
        self.savegame: Optional[OakSaveGame] = get_pc().CurrentSavegame
        self.savegame_properties = SAVE_PROPERTIES
        self.json_properties = set([])
        self.jdata = {}
        self.json_path = f'C:\\Users\\{getlogin()}\\Documents\\My Games\\Borderlands 3\\Saved\\SaveGames\\JSON'
        if not exists(self.json_path):
            mkdir(self.json_path)
        if self.savegame:
            self.read_json()
        self.savegame_functions = []
        self.save_open_callbakcs: list[Callable] = []
        self.save_close_callbacks: list[Callable] = []

    
    @property
    def SaveName(self) -> str:
        if self.savegame:
            return hex(self.savegame.SaveGameId)[2:].upper()
        else:
            return "Unknown"

    def refresh(self) -> None:
        self.__init__()

    def on_save_open(self, callback: Callable) -> None:
        self.save_open_callbakcs.append(callback)

    def on_save_close(self, callback: Callable) -> None:
        self.save_close_callbacks.append(callback)

    def read_json(self):
        try:
            with open(f'{self.json_path}\\{self.SaveName}.json', 'r') as f:
                data = dict(json.load(f))
            self.json_properties = set(data.keys())
            self.jdata = data
        except FileNotFoundError:
            with open(f'{self.json_path}\\{self.SaveName}.json', 'w') as f:
                json.dump({}, f)
            self.json_properties = set([])
            self.jdata = {}

    def write_json(self) -> None:
        with open(f'{self.json_path}\\{self.SaveName}.json', 'w') as f:
            json.dump(self.jdata, f)
        return None

    def __getitem__(self, __key: str) -> Any:
        if __key in self.json_properties:
            return self.jdata[__key]
        elif __key in self.savegame_properties:
            return getattr(self.savegame, __key)
        else:
            raise KeyError(f'{__key} is not a valid key')
    
    def __setitem__(self, __key: str, __value: Any) -> None:
        if __key in self.savegame_properties:
            setattr(self.savegame, __key, __value)
        else :
            self.jdata[__key] = __value
            self.json_properties.add(__key)
            self.write_json()

    def __delitem__(self, __key: str) -> None:
        if __key in self.json_properties:
            del self.jdata[__key]
            self.json_properties.remove(__key)
            self.write_json()
        elif __key in self.savegame_properties:
            raise KeyError(f'{__key} is a save game property and cannot be deleted')
        else:
            raise KeyError(f'{__key} is not a valid key')

    def __contains__(self, __key: str) -> bool:
        return __key in self.json_properties or __key in self.savegame_properties

    def __iter__(self) -> Callable:
        raise NotImplementedError('Iterating over a PySaveGame is not supported')

    def __len__(self) -> int:
        return len(self.json_properties) + len(self.savegame_properties)

    def __repr__(self) -> str:
        return f'<PySaveGame: {hex(getattr(self.savegame, "SaveGameId", -1))}>'

    def __str__(self) -> str:
        return f'<PySaveGame: {hex(getattr(self.savegame, "SaveGameId", -1))}>'

    def __dir__(self) -> list:
        return list(self.json_properties) + list(self.savegame_properties)

SAVE_GAME = PySaveGame()
  
@hook("/Game/Common/_Design/BPCont_Player.BPCont_Player_C:UserConstructionScript", auto_enable=True, hook_type=Type.PRE)
def refresh_map_load(_1: UObject, _2: WrappedStruct, _3: Any, _4: BoundFunction):
    SAVE_GAME.savegame = list(game.find_all(OakSaveGame))[-1]
    SAVE_GAME.read_json()
    for callback in SAVE_GAME.save_open_callbakcs:
        callback()

@hook(GFxPauseMenu.OnQuitChoiceMade._path_name(), auto_enable=True, hook_type=Type.PRE)
def save_quit(_1, _2, _3, _4):
    for callback in SAVE_GAME.save_close_callbacks:
        callback()
    SAVE_GAME.write_json()
    SAVE_GAME.savegame = None
    SAVE_GAME.jdata = {}
    SAVE_GAME.json_properties = set([])
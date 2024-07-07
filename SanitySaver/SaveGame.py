from os import getlogin, mkdir
from os.path import exists
from typing import Any, Callable
from unrealsdk import logging
from unrealsdk.hooks import Type
from unrealsdk.unreal import BoundFunction, UObject, WrappedStruct
from mods_base import hook, get_pc
import json

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
    'ActiveTravelStations',
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
        self.savegame = get_pc().CurrentSavegame
        self.savegame_properties = SAVE_PROPERTIES
        self.json_properties = set([])
        self.jdata = {}
        self.json_path = f'C:\\Users\\{getlogin()}\\Documents\\My Games\\Borderlands 3\\Saved\\SaveGames\\JSON'
        if not exists(self.json_path):
            mkdir(self.json_path)
        if self.savegame:
            self.read_json()
        self.savegame_functions = []

    
    @property
    def SaveName(self) -> str:
        if self.savegame:
            return hex(self.savegame.SaveGameId)[2:].upper()
        else:
            return "Unknown"

    def refresh(self) -> None:
        self.__init__()

    def read_json(self) -> None:
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
        return None

    def __write_json(self) -> None:
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
            self.__write_json()

    def __delitem__(self, __key: str) -> None:
        if __key in self.json_properties:
            del self.jdata[__key]
            self.json_properties.remove(__key)
            self.__write_json()
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
        return f'<PySaveGame: {hex(self.savegame.SaveGameId)}>'

    def __str__(self) -> str:
        return f'<PySaveGame: {hex(self.savegame.SaveGameId)}>'

    def __dir__(self) -> list:
        return list(self.json_properties) + list(self.savegame_properties)

SAVE_GAME = PySaveGame()

@hook("/Script/OakGame.DiscoveryComponent.ClientDiscoverLevel", auto_enable=True, hook_type=Type.PRE)
def refresh_map_load(caller: UObject, _2: WrappedStruct, _3: Any, _4: BoundFunction):
    if caller.GetOwner().Class.Name == 'BPCont_Player_C':
        if get_pc().PlayerController.CurrentSavegame != None:
            SAVE_GAME.savegame = get_pc().CurrentSavegame
            SAVE_GAME.read_json()

@hook("/Script/OakGame.GFxPauseMenu.OnQuitChoiceMade", auto_enable=True, hook_type=Type.PRE)
def save_quit(_1: UObject, _2: WrappedStruct, _3: Any, _4: BoundFunction):
    SAVE_GAME.savegame = None
    SAVE_GAME.jdata = {}
    SAVE_GAME.json_properties = set([])
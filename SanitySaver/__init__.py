from bl3 import get_pc
import bl3 as game
from bl3.bp import BPChar_Player_C
from bl3.core_uobject import Vector
from bl3.engine import Actor, Pawn
from bl3.gbx_inventory import InventoryBalanceStateComponent, InventoryBalanceStateInitializationData, InventoryCategoryData
from bl3.oak_game import OakCharacter
import mods_base
from oak_libs import INVENTORY
import thoth
from unrealsdk.unreal import UObject
import unrealsdk
from mods_base import ENGINE, Game as GameVariant, hook
import json
from os.path import exists
import sys
from typing import Callable, List, Optional, cast
from .SaveGame import SAVE_GAME, refresh_map_load, save_quit

DEBUG = True

BASE_PARTS = set([
    f'{obj.Class.Name}|{getattr(obj.Outer, "Name", "None")}.{obj.Name}' \
        for obj in unrealsdk.find_all("InventoryPartData", False)
])


class ParentSaveManager:

    def __init__(self):
        self.character: BPChar_Player_C = cast(BPChar_Player_C, get_pc().Pawn)

    def GetWorld(self) -> UObject:
        return ENGINE.GameViewport.World

    def GetLocation(self) -> Vector:
        """
        Returns the location of the player.
        """
        loc = self.character.CapsuleComponent.RelativeLocation
        return cast(Vector, unrealsdk.make_struct("Vector", X = loc.X, Y = loc.Y, Z = loc.Z))

    def ObjectToStr(self,obj: UObject) -> str:
        """Converts an object to a string"""
        return f'{obj.Class.Name}|{getattr(obj.Outer, "Name", "None")}.{obj.Name}'

    def StrToObject(self, obj_str: str) -> UObject:
        """Converts a string to an object"""
        obj = obj_str.split('|')
        return unrealsdk.find_object(obj[0], obj[1])

    def ActorToData(self, item: Actor) -> Optional[dict[str, UObject]]:
        """Converts an actor to a list, returns None if the game can serialize the item on its own"""
        try:
            item_data: InventoryBalanceStateComponent = item.BalanceStateComponent
        except:
            item_data: InventoryBalanceStateComponent = item.InventoryBalanceState

        save_data = {
            "GameStage": int(item_data.GameStage),
            "InventoryData": self.ObjectToStr(item_data.InventoryData),
            "InventoryBalanceData": self.ObjectToStr(item_data.InventoryBalanceData),
            "ManufacturerData": self.ObjectToStr(item_data.ManufacturerData),
            "PartList": [self.ObjectToStr(obj) for obj in item_data.PartList],
            "GenericPartList": [self.ObjectToStr(obj) for obj in item_data.GenericPartList],
            "AdditionalData": list(item_data.AdditionalData),
            "CustomizationPartList": [self.ObjectToStr(obj) for obj in item_data.CustomizationPartList],
            "ReRollCount": int(item_data.ReRollCount)
        }

        if GameVariant.get_current() == GameVariant.WL:
            save_data["OverpowerLevel"] = int(item_data.OverpowerLevel)

        part_classes = set()
        if len(save_data["PartList"]) == 0 and len(save_data["GenericPartList"]) == 0:
            return None
        for i in save_data["PartList"]:
            part_classes.add(i.split('|')[0])
            if i not in BASE_PARTS:
                return save_data
        if len(list(part_classes)) != 1:
            return save_data
        for i in save_data["GenericPartList"]:
            if i not in BASE_PARTS:
                return save_data
        return None

    def DataToActor(self, item_data: dict) -> Actor:
        """Converts a saved item data into an actor"""

        save_dict = {
            "GameStage": item_data["GameStage"],
            "InventoryData": self.StrToObject(item_data["InventoryData"]),
            "InventoryBalanceData": self.StrToObject(item_data["InventoryBalanceData"]),
            "ManufacturerData": self.StrToObject(item_data["ManufacturerData"]),
            "PartList": [self.StrToObject(obj) for obj in item_data["PartList"]],
            "GenericPartList": [self.StrToObject(obj) for obj in item_data["GenericPartList"]],
            "AdditionalData": item_data["AdditionalData"],
            "CustomizationPartList": [self.StrToObject(obj) for obj in item_data["CustomizationPartList"]],
            "ReRollCount": item_data["ReRollCount"],
        }
        if GameVariant.get_current() == GameVariant.WL:
            save_dict["OverpowerLevel"] = item_data["OverpowerLevel"]
        else:
            save_dict["bDroppedFromAI"] = False
        save_struct = cast(
            InventoryBalanceStateInitializationData,
            unrealsdk.make_struct("InventoryBalanceStateInitializationData", **save_dict)
        )
        return INVENTORY.BuildInventory(self.GetWorld(), False, self.GetLocation(), save_struct)


class PlayerSaveManager(ParentSaveManager):
    def __init__(self):
        super().__init__()

    def EquippedItemList(self) -> list[Actor]:
        """Returns a list of all items equipped on the player"""
        slot_list = self.character.EquipmentSlots
        item_lst = []
        for i in slot_list:
            equipped_actor = self.character.GetEquippedInventoryForSlot(i)
            if equipped_actor:
                item_lst.append(equipped_actor)
        return item_lst

    def AllItemList(self) -> list[UObject]:
        """Returns a list of all items in the players inventory"""
        inv_list = self.character.InventoryList.InventoryList.Items
        item_lst = []
        for i in range(len(list(inv_list))):
            if inv_list[i].StoredActor != None:
                item_lst.append(inv_list[i].StoredActor)
        return item_lst

    def DupelessItemList(self) -> list[Actor]:
        """Returns a list of all items in the players inventory without duplicates"""
        fixed_inv_lst = []
        for i in self.AllItemList():
            if i not in self.EquippedItemList():
                fixed_inv_lst.append(i)
        return fixed_inv_lst

    # def ReadCurrencyData(self) -> dict[str, int]:
    #     inv_list = self.character.InventoryList.InventoryList.Items
    #     currency_dct = {}
    #     for i in inv_list:
    #         if i.StoredActor == None:
    #             currency_dct[i.BaseCategoryDefinition._path_name()] = i.Quantity
    #     return currency_dct

    # def WriteCurrencyData(self, dct: dict[str, int]):
    #     pawn = self.character
    #     inv_list = pawn.InventoryList
    #     for path, quantity in dct.items():
    #         obj = game.ty_find_object(InventoryCategoryData, path)
    #         inv_list.AddExternalItem(obj, None, quantity, False, False, False, 0, True) # type: ignore

    def ExtractSave(self) -> None:
        AllItemList_var = []
        for item in self.DupelessItemList():
            inv_data = self.ActorToData(item)
            if inv_data != None:
                AllItemList_var.append(inv_data)
        EquippedItemList_var = []
        for item in self.EquippedItemList():
            eqp_data = self.ActorToData(item)
            if eqp_data != None:
                EquippedItemList_var.append(eqp_data)
        save_data = {'Equipped': EquippedItemList_var,'Inventory': AllItemList_var},
        SAVE_GAME['Items'] = save_data

    def ApplySave(self) -> None:

        def add_item(item_data: Actor) -> None:
            """Adds an item to the player's inventory"""
            if DEBUG:
                print('DEBUG: Adding item')
            try:
                InvCategory = item_data.BalanceStateComponent.InventoryData.InventoryCategory
            except AttributeError:
                InvCategory = item_data.InventoryBalanceState.InventoryData.InventoryCategory
            self.character.InventoryList.AddExternalItem(InvCategory, item, 1, False, False, False, 0, True)

        if 'Items' in SAVE_GAME:
            if DEBUG: print('DEBUG: found save data')
            save_data = SAVE_GAME['Items']
            for item in save_data['Equipped']:
                item = self.DataToActor(item)
                add_item(item)
            for item in save_data['Inventory']:
                item = self.DataToActor(item)
                add_item(item)
        else:
            print('No save data found')
            self.ExtractSave()
            return

#############################################################################

@hook("/Script/OakGame.OakCharacter_Player:ShowConnectEffect")
def ApplySave(_1, _2, _3, _4):
    def run():
        print('Applying Save')
        PlayerSaveManager().ApplySave()
        drop_item.enable()
        add_item.enable()
        extract_save_wrapper_quit.enable()
    thoth.delayed(run, 0.5)

def extract_save_wrapper_item():
    print('Extracting Save; Reason: Item')
    PlayerSaveManager().ExtractSave()

@hook("/Script/OakGame.OakCharacter:RemovingFromInventory")
def drop_item(_1, _2, _3, _4) -> None:
    thoth.delayed(extract_save_wrapper_item, 0.1)

@hook("/Script/OakGame.OakCharacter:AddedToInventory")
def add_item(_1, _2, _3, _4) -> None:
    thoth.delayed(extract_save_wrapper_item, 0.1)

def extract_save_wrapper_quit():
    print('Extracting Save; Reason: Quit')
    PlayerSaveManager().ExtractSave()
    drop_item.disable()
    add_item.disable()


SAVE_GAME.on_save_close(extract_save_wrapper_quit)


mods_base.build_mod(
    name="Sanity Saver",
    hooks=[
        refresh_map_load,
        save_quit,
        drop_item,
        add_item
    ]
)


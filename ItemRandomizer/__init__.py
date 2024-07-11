from bl3.bp import BPInv_ClassModData2_C
from bl3.core_uobject import Int32Interval
from bl3.gbx_game_system_core import ActorPartListData, AttributeInitializationData, RuntimeActorPartListData, RuntimeActorPartListPartTypeData, UIStatData, WeightedActorPartData
from bl3.gbx_inventory import GearBuilderCategoryData, InventoryBalanceData, InventoryPartData, RuntimeGenericPartListData
from unrealsdk import find_all, make_struct, unreal
import json
from typing import cast
from functools import lru_cache
import threading
from mods_base import build_mod, hook, BoolOption, command
import bl3 as game

DEBUG = True

PART_ENUMS: dict[str, dict[str, str]] = {
    "BPInvPart_AR_DAL_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Accessory",
        "5": "Foregrip",
        "6": "Grip",
        "7": "Magazine",
        "8": "Trash",
        "9": "Scope",
        "10": "AltMod",
        "11": "Elemental",
        "12": "Material"
    },
    "BPInvPart_AR_TOR_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Stock",
        "5": "Foregrip",
        "6": "Scope",
        "7": "Magazine",
        "8": "Elemental",
        "9": "Accessory",
        "10": "Material"
    },
    "BPInvPart_ATL_AR_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "AltMod",
        "5": "Magazine",
        "6": "Grip",
        "7": "Foregrip",
        "8": "Scope",
        "9": "Material"
    },
    "BPInvPart_ATL_HW_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "AltMod",
        "5": "Foregrip",
        "6": "Grip",
        "7": "Accessory",
        "8": "Scope",
        "9": "Magazine",
        "10": "Material"
    },
    "BPInvPart_AR_COV_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Magazine",
        "5": "Grip",
        "6": "Foregrip",
        "7": "Trash",
        "8": "Scope",
        "9": "Elemental",
        "10": "Material"
    },
    "BPInvPart_Dahl_SMG_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Accessory",
        "5": "Trash",
        "6": "Scope",
        "7": "Magazine",
        "8": "Foregrip",
        "9": "Grip",
        "10": "Stock",
        "11": "Elemental",
        "12": "Material",
        "13": "AltMod",
        "14": "Trash"
    },
    "BPInvPart_HW_COV_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Grip",
        "5": "Magazine",
        "6": "Stock",
        "7": "Foregrip",
        "8": "Scope",
        "9": "Elemental",
        "10": "Material"
    },
    "BPInvPart_HW_TOR_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Grip",
        "5": "Magazine",
        "6": "Stock",
        "7": "Accessory",
        "8": "Scope",
        "9": "Elemental",
        "10": "Material"
    },
    "BPInvPart_HW_VLA_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Grip",
        "5": "Stock",
        "6": "Foregrip",
        "7": "Scope",
        "8": "AltMod",
        "9": "Magazine",
        "10": "Elemental",
        "11": "Material"
    },
    "BPInvPart_Hyperion_Shotgun_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Foregrip",
        "5": "Grip",
        "6": "Magazine",
        "7": "Scope",
        "8": "Elemental",
        "9": "Accessory",
        "10": "Material"
    },
    "BPInvPart_Jakobs_Pistol_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Grip",
        "5": "Foregrip",
        "6": "Magazine",
        "7": "Trash",
        "8": "Scope",
        "9": "Material"
    },
    "BPInvPart_SG_JAK_C": {
        "0": "Body",
        "1": "Grip",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Trash",
        "5": "Elemental",
        "6": "Foregrip",
        "7": "Stock",
        "8": "Accessory",
        "9": "Magazine",
        "10": "Scope",
        "11": "Material"
    },
    "BPInvPart_JAK_AR_C": {
        "0": "Body",
        "1": "Grip",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Elemental",
        "5": "Magazine",
        "6": "Foregrip",
        "7": "Stock",
        "8": "Accessory",
        "9": "Scope",
        "10": "Material"
    },
    "BPInvPart_SG_MAL_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Grip",
        "5": "Stock",
        "6": "Magazine",
        "7": "Scope",
        "8": "Elemental",
        "9": "AltMod",
        "10": "Material"
    },
    "BPInvPart_Maliwan_SMG_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Scope",
        "5": "Magazine",
        "6": "Grip",
        "7": "Accessory",
        "8": "Stock",
        "9": "Elemental",
        "10": "AltMod",
        "11": "Material"
    },
    "BPInvPart_MAL_SR_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Grip",
        "5": "Accessory",
        "6": "Foregrip",
        "7": "Magazine",
        "8": "Scope",
        "9": "Accessory",
        "10": "Elemental",
        "11": "AltMod",
        "12": "Material"
    },
    "BPInvPart_PS_ATL_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Grip",
        "5": "AltMod",
        "6": "Foregrip",
        "7": "Magazine",
        "8": "Material"
    },
    "BPInvPart_PS_COV_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Magazine",
        "5": "Accessory",
        "6": "Grip",
        "7": "Stock",
        "8": "Scope",
        "9": "Elemental",
        "10": "Material"
    },
    "BPInvPart_PS_DAL_C": {
        "0": "Body",
        "1": "Barrel",
        "2": "Barrel_Mod",
        "3": "Grip",
        "4": "Stock",
        "5": "Scope",
        "6": "Magazine",
        "7": "Accessory",
        "8": "Accessory",
        "9": "Elemental",
        "10": "AltMod",
        "11": "Material"
    },
    "BPInvPart_PS_MAL_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Grip",
        "5": "Foregrip",
        "6": "Magazine",
        "7": "Accessory",
        "8": "Scope",
        "9": "Elemental",
        "10": "AltMod",
        "11": "Material"
    },
    "BPInvPart_PS_TOR_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Grip",
        "5": "Stock",
        "6": "Foregrip",
        "7": "Magazine",
        "8": "Scope",
        "9": "Elemental",
        "10": "Accessory",
        "11": "Material"
    },
    "BPInvPart_PS_VLA_C": {
        "0": "Body",
        "1": "Scope",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Foregrip",
        "5": "Foregrip",
        "6": "Magazine",
        "7": "Grip",
        "8": "Trash",
        "9": "Trash",
        "10": "Scope",
        "11": "AltMod",
        "12": "Accessory",
        "13": "Accessory",
        "14": "Elemental",
        "15": "Material"
    },
    "BPInvPart_SG_TED_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Grip",
        "5": "Foregrip",
        "6": "Scope",
        "7": "Foregrip",
        "8": "Elemental",
        "9": "Material"
    },
    "BPInvPart_SG_Torgue_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Grip",
        "5": "Foregrip",
        "6": "Magazine",
        "7": "Scope",
        "8": "Elemental",
        "9": "Material",
        "10": "Accessory"
    },
    "BPInvPart_SM_Hyperion_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Grip",
        "5": "Stock",
        "6": "Trash",
        "7": "Scope",
        "8": "Magazine",
        "9": "Foregrip",
        "10": "Accessory",
        "11": "Elemental",
        "12": "Material"
    },
    "BPInvPart_SR_DAL_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Magazine",
        "5": "Grip",
        "6": "Accessory",
        "7": "Foregrip",
        "8": "Trash",
        "9": "Trash",
        "10": "Scope",
        "11": "Accessory",
        "12": "AltMod",
        "13": "Elemental",
        "14": "Material"
    },
    "BPInvPart_SR_HYP_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Magazine",
        "5": "Grip",
        "6": "Trash",
        "7": "Scope",
        "8": "Accessory",
        "9": "Scope",
        "10": "Accessory",
        "11": "Elemental",
        "12": "Material",
        "13": "Stock"
    },
    "BPInvPart_SR_JAK_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Magazine",
        "5": "Elemental",
        "6": "Scope",
        "7": "Accessory",
        "8": "Stock",
        "9": "Accessory",
        "10": "Foregrip",
        "11": "Material"
    },
    "BPInvPart_Tediore_Pistol_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Magazine",
        "5": "Grip",
        "6": "Scope",
        "7": "Elemental",
        "8": "Material"
    },
    "BPInvPart_SM_TED_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Scope",
        "5": "AltMod",
        "6": "Foregrip",
        "7": "Grip",
        "8": "Elemental",
        "9": "Material"
    },
    "BPInvPart_VLA_AR_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "AltMod",
        "5": "Accessory",
        "6": "Grip",
        "7": "Accessory",
        "8": "Foregrip",
        "9": "Magazine",
        "10": "Trash",
        "11": "Scope",
        "12": "Elemental",
        "13": "Material",
        "14": "Scope",
        "15": "Trash",
        "16": "Trash"
    },
    "BPInvPart_VLA_SR_C": {
        "0": "Body",
        "1": "Body_Mod",
        "2": "Barrel",
        "3": "Barrel_Mod",
        "4": "Grip",
        "5": "Foregrip",
        "6": "Magazine",
        "7": "Scope",
        "8": "Accessory",
        "9": "AltMod",
        "10": "AltMod",
        "11": "Accessory",
        "12": "Elemental",
        "13": "Material"
    }
}

RARITY_PART_COUNT = { #this is so rarity matters alot more than just pure random
    'Common': {'normal': (0,0), 'special': (1,1), 'single': (1,1)},
    'Uncommon': {'normal': (0,1), 'special': (1,1), 'single': (1,1)},
    'Rare': {'normal': (1,1), 'special': (1,1), 'single': (1,1)},
    'VeryRare': {'normal': (1,2), 'special': (1,2), 'single': (1,1)},
    'Legendary': {'normal': (2,2), 'special': (2,2), 'single': (1,1)}
}
PART_TYPE_DICT = {
    0: 'single', #body
    1: 'normal', #body mod
    2: 'special',#barrel
    3: 'normal', #barrel mod
    4: 'normal', #grip
    5: 'normal', #foregrip
    6: 'normal', #stock
    7: 'normal', #accessory
    8: 'special',#alt mode
    9: 'single', #magazine
    10: 'single',#scope
    11: 'single',#elemental
    12: 'single' #material
}
PART_CAT_TYPE = {
    'Body' : 0,
    'Body_Mod' : 1,
    'Barrel' : 2,
    'Barrel_Mod' : 3,
    'Grip' : 4,
    'Foregrip' : 5,
    'Stock' : 6,
    'Accessory' : 7,
    'AltMod' : 8,
    'Magazine' : 9,
    'Scope' : 10,
    'Elemental' : 11,
    'Material' : 12,
}

# WEAIGHT_STRUCT = cast(
#     AttributeInitializationData,
#     make_struct(
#         "AttributeInitializationData",
#         BaseValueConstant=1.5,
#         DataTableValue=make_struct(
#             "DataTableValueHandle",
#             DataTable=None,
#             RowName='None',
#             ValueName='None'
#         ),
#         BaseValueAttribute=None,
#         AttributeInitializer=None,
#         BaseValueScale=1.5
# ))

def weight_struct() -> AttributeInitializationData:
    return cast(
        AttributeInitializationData,
        make_struct(
            "AttributeInitializationData",
            BaseValueConstant=1.5,
            DataTableValue=make_struct(
                "DataTableValueHandle",
                DataTable=None,
                RowName='None',
                ValueName='None'
            ),
            BaseValueAttribute=None,
            AttributeInitializer=None,
            BaseValueScale=1.5
        )
    )

class Randomizer:
    """
    Give this class a list of categories to whitelist.
    Extreme will make things more random, but will also make it more likely to crash.
    """
    def __init__(self, whitelist: list[str] = []) -> None:
        self.whitelist = whitelist
        self.parts: list[InventoryPartData] = []
        self.gen_parts: list[InventoryPartData] = []
        self.weap_parts: list[InventoryPartData] = []
        if DEBUG: print(f'Randomizer made: {whitelist}')

    @property
    def categories(self) -> set[GearBuilderCategoryData]:
        whitelist = self.whitelist
        """
        Gets category objects for filtering.
        
        Options: Artifacts, Assault Rifles, Class Mods, Grenade Mods, \n
        Heavy Weapons, Pistols, Shields, Shotguns,SMGs, Sniper Rifles.
        """
        avail_categories = game.ty_find_all(GearBuilderCategoryData)
        final_list = set()
        for cat in avail_categories:
            if cat.CategoryName in whitelist:
                final_list.add(cat)
        return final_list

    @property
    def rand_item_type(self):
        weapons = ['Assault Rifles', 'Pistols', 'SMGs', 'Shotguns', 'Sniper Rifles', 'Heavy Weapons']
        gear = ['Artifacts', 'Shields', 'Class Mods', 'Grenade Mods']
        whitelist = self.whitelist
        if len(whitelist) == 0:
            raise ValueError('No categories were given to the randomizer.')
        #if item in whitelist is in weapons and an item in whitelist is in gear, raise error
        if any(i in whitelist for i in weapons) and any(i in whitelist for i in gear):
            raise ValueError('Cannot randomize both weapons and gear.')
        if any(i in whitelist for i in weapons):
            return 'Weapon'
        else:
            return 'Gear'

    def __get_balances(self) -> list[InventoryBalanceData]:
        """
        Finds all balances within the parameters of the whitelist.
        """
        all_bal = game.ty_find_all(InventoryBalanceData)
        out_bal = []
        for bal in all_bal:
            if bal.GearBuilderCategory is None:
                continue
            if bal.GearBuilderCategory in self.categories:
                out_bal.append(bal)
        print(f"found {len(out_bal)} balances")
        return out_bal

    def __get_parts(self) -> tuple[list[InventoryPartData], list[InventoryPartData]]:
        """
        Finds all parts within the parameters of the whitelist.
        """
        name_to_class = {
            'Artifacts' : ['BPInvPart_Artifact_C'],
            'Shields' : ['BPInvPart_Shield_C'],
            'Class Mods' : ['BPInvPart_ClassMod_C'],
            'Grenade Mods' : ['BPInvPart_GrenadeMod_C'],
            'Assault Rifles' : ['BPInvPart_AR_COV_C', 'BPInvPart_JAK_AR_C', 'BPInvPart_AR_DAL_C', 'BPInvPart_VLA_AR_C', 'BPInvPart_AR_TOR_C', 'BPInvPart_ATL_AR_C','BPInvPart_PS_DAL_C'],
            'Pistols' : ['BPInvPart_PS_COV_C', 'BPInvPart_Jakobs_Pistol_C', 'BPInvPart_PS_DAL_C', 'BPInvPart_PS_VLA_C', 'BPInvPart_PS_TOR_C','BPInvPart_PS_ATL_C','BPInvPart_PS_MAL_C','BPInvPart_Tediore_Pistol_C'],
            'SMGs' : ['BPInvPart_SM_TED_C', 'BPInvPart_Maliwan_SMG_C', 'BPInvPart_SM_Hyperion_C', 'BPInvPart_Dahl_SMG_C'],
            'Shotguns' : ['BPInvPart_SG_Torgue_C','BPInvPart_SG_JAK_C','BPInvPart_SG_TED_C','BPInvPart_SG_MAL_C','BPInvPart_Hyperion_Shotgun_C'],
            'Sniper Rifles' : ['BPInvPart_VLA_SR_C', 'BPInvPart_MAL_SR_C', 'BPInvPart_SR_JAK_C', 'BPInvPart_SR_HYP_C','BPInvPart_SR_DAL_C'],
            'Heavy Weapons' : ['BPInvPart_HW_VLA_C', 'BPInvPart_HW_TOR_C', 'BPInvPart_ATL_HW_C','BPInvPart_HW_COV_C']
        }
        wanted_part_classes = set()
        for cat in self.categories:
            wanted_part_classes = wanted_part_classes.union(name_to_class[cat.CategoryName])
        all_parts = find_all("InventoryPartData", False)
        selected_parts = []
        generic_parts = []
        part_class_blacklist = set(['VehiclePartData','OakVehiclePartData','BPVehiclePart_C','OakWeaponMayhemPartData'])
        for part in all_parts:
            if part.Class.Name in part_class_blacklist:
                continue
            if 'Default__' in part.Name:
                continue
            if part.Class.Name == 'InventoryGenericPartData':
                generic_parts.append(part)
            elif part.Class.Name in wanted_part_classes:
                selected_parts.append(part)
        if DEBUG: print(f"found {len(selected_parts)} parts and {len(generic_parts)} generic parts")
        return selected_parts, generic_parts

    def __weap_part_sorter(self):
        """
        Sorts weapon parts into having better part typing.
        """
        for part in self.parts:
            cls = part.Class.Name
            if cls in set(['VehiclePartData','OakVehiclePartData','BPVehiclePart_C','OakWeaponMayhemPartData']):
                continue
            try:
                part_type_name = PART_ENUMS[cls][str(part.PartType)]
            except Exception as e:
                print(f"Error: {e}, Class: {cls},Part: {part.Name}, PartType: {part.PartType}")
                continue
            if part_type_name == 'Trash':
                continue
            part.PartType = PART_CAT_TYPE[part_type_name]
            self.weap_parts.append(part)
        print(f"sorted {len(self.weap_parts)} weapon parts")

    def __part_fixer(self):
        for part in self.parts:
            part.Dependencies.clear()
            part.Excluders.clear()
        if "Class Mods" in self.whitelist:
            uistats = game.ty_find_all(UIStatData)
            for stat in uistats:
                if stat.SectionName == "LegendaryClassModInfo":
                    stat.SectionName = "Secondary"
        for part in self.gen_parts:
            part.InventoryAttributeEffects.clear()
        print("Fixed parts")

    def gear_balance_constructor(self) -> RuntimeActorPartListData:
        parts_sorted = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        for part in self.parts:
            part_type = part.PartType
            if part_type > 15:
                part.PartType = 15
                part_type = 15
            parts_sorted[part_type].append(part)
        start_idx = 0
        PartTypeTOC_lst = []
        for lst in parts_sorted:
            num_of_parts = len(lst)
            PartTypeTOC_lst.append(cast(
                RuntimeActorPartListPartTypeData,
                make_struct(
                    "RuntimeActorPartListPartTypeData",
                    StartIndex=start_idx,
                    NumParts=num_of_parts
                )
            ))
            start_idx += num_of_parts
        AllParts_lst = []
        for lst in parts_sorted:
            for part in lst:
                AllParts_lst.append(cast(
                    WeightedActorPartData,
                    make_struct(
                        "WeightedActorPartData",
                        PartData=part,
                        Weight=weight_struct()
                    )
                ))
        return cast(
            RuntimeActorPartListData,
            make_struct(
                "RuntimeActorPartListData",
                bIsInitialized=True,
                PartTypeTOC=PartTypeTOC_lst,
                AllParts=AllParts_lst
            ))

    def weap_balance_constructor(self) -> RuntimeActorPartListData:
        parts = self.weap_parts
        parts_sorted = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
        bHasBodyPart = False
        for part in parts:
            part_type = part.PartType
            if part_type == 0 and not bHasBodyPart:
                bHasBodyPart = True
            elif part_type == 0 and bHasBodyPart:
                continue
            parts_sorted[part_type].append(part)
        start_idx = 0
        PartTypeTOC_lst: list[RuntimeActorPartListPartTypeData] = []
        for lst in parts_sorted:
            num_of_parts = len(lst)
            PartTypeTOC_lst.append(cast(
                RuntimeActorPartListPartTypeData,
                make_struct(
                    "RuntimeActorPartListPartTypeData",
                    StartIndex=start_idx,
                    NumParts=num_of_parts
                )
            ))
            start_idx += num_of_parts
        AllParts_lst: list[WeightedActorPartData] = []
        for lst in parts_sorted:
            for part in lst:
                AllParts_lst.append(cast(
                    WeightedActorPartData,
                    make_struct(
                        "WeightedActorPartData",
                        PartData=part,
                        Weight=weight_struct()
                    )
                ))
        return cast(
            RuntimeActorPartListData,
            make_struct(
                "RuntimeActorPartListData",
                bIsInitialized=True,
                PartTypeTOC=PartTypeTOC_lst,
                AllParts=AllParts_lst
            ))

    def generic_part_list(self) -> RuntimeGenericPartListData:
        """Returns a list of generic parts"""
        if DEBUG: print(f"Starting to create generic part list")
        gen_part_out_lst: list[WeightedActorPartData] = []
        for part in self.gen_parts:
            gen_part_out_lst.append(cast(
                WeightedActorPartData,
                make_struct(
                    "WeightedActorPartData",
                    PartData=part,
                    Weight=weight_struct()
                )
            ))
        return cast(
            RuntimeGenericPartListData,
            make_struct(
                "RuntimeGenericPartListData",
                bEnabled=True,
                PartList=gen_part_out_lst
            )
        )

    def weap_part_count_modifier(self, balance: InventoryBalanceData) -> None:
        """Modifies the number of parts that can be generated for a weapon based on rarity"""
        def __part_range(part_type: int, raity: str) -> Int32Interval:
            part_type_name = PART_TYPE_DICT[part_type]
            part_range = RARITY_PART_COUNT[raity][part_type_name]
            return cast(
                Int32Interval,
                make_struct(
                    "Int32Interval",
                    Min=part_range[0],
                    Max=part_range[1]
                )
            )
        def __get_bal_parts(part_type: int, bal_partlist: RuntimeActorPartListData) -> list[WeightedActorPartData]:
            toc = bal_partlist.PartTypeTOC
            all_parts = bal_partlist.AllParts
            start_idx = toc[part_type].StartIndex
            end_idx = start_idx + toc[part_type].NumParts
            parts = all_parts[start_idx:end_idx]
            return parts
        balance.MaxNumPrefixes = 3 #more text means more things... right?
        bodypart = None
        try:
            bodypart = balance.RuntimePartList.AllParts[0].PartData
        except IndexError:
            pass
        bal_parts = self.weap_balance_constructor()
        if DEBUG: print(f"Weapon balance constructed for {balance.Name}")
        bal_parts.AllParts[0] = cast(
            WeightedActorPartData,
            make_struct(
                "WeightedActorPartData",
                PartData=bodypart,
                Weight=weight_struct()
            ))
        balance.RuntimePartList = bal_parts
        partset = balance.PartSetData
        part_enum = partset.PartTypeEnum
        rarity_name = str(balance.RarityData.Name).split('_')[-1]
        if DEBUG: print(f"Starting to create ActorPartLists for {balance.Name}")
        actor_part_list = []
        for part_idx in range(13):
            actor_part_list.append(cast(
                ActorPartListData,
                make_struct(
                    "ActorPartListData",
                    PartTypeEnum=part_enum,
                    PartType=part_idx,
                    bCanSelectMultipleParts=True,
                    bUseWeightWithMultiplePartSelection=False,
                    MultiplePartSelectionRange=__part_range(part_idx, rarity_name),
                    bEnabled=True,
                    Parts=__get_bal_parts(part_idx, bal_parts)
            )))
        if DEBUG: print(f"ActorPartLists for {balance.Name} created")
        partset.ActorPartLists = actor_part_list # type: ignore
        if DEBUG: print(f"ActorPartLists for {balance.Name} set")

    def randomize(self) -> None:
        self.parts, self.gen_parts = self.__get_parts()
        if self.rand_item_type == 'Weapon': self.__weap_part_sorter()
        # loaded_com = cast(BPInv_ClassModData2_C, game.ty_find_class(BPInv_ClassModData2_C).ClassDefaultObject)
        self.__part_fixer()
        balances = self.__get_balances()
        for bal in balances:
            if DEBUG: print("Randomizing balance: ", bal.Name)
            # if self.rand_item_type == 'Weapon':
            #     self.weap_part_count_modifier(bal)
            #     if DEBUG: print(f"Part count modification of {bal.Name} is complete.")
            # else:
            #     if self.whitelist == ['Class Mods']: bal.InventoryData = loaded_com
            #     bal.RuntimePartList = self.gear_balance_constructor()
            bal.RuntimeGenericPartList = self.generic_part_list()
            print(f"Generic part modification of {bal.Name} is complete.")
            bal.DlcInventorySetData = None # type: ignore
            if DEBUG: print(f'Randomization of {bal.Name} is complete.')
        for i in self.whitelist:
            print(f'Randomization of {i} is complete.')

class RandHelper:
    def __init__(self, extreme: bool):
        self.extreme = True
    def all_wep_rand(self):
        print('Randomizing all weapons...')
        if not self.extreme:
            Randomizer(whitelist=['Shotguns']).randomize()
            Randomizer(whitelist=['Assault Rifles']).randomize()
            Randomizer(whitelist=['Sniper Rifles']).randomize()
            Randomizer(whitelist=['SMGs']).randomize()
            Randomizer(whitelist=['Pistols']).randomize()
            Randomizer(whitelist=['Heavy Weapons']).randomize()
        else:
            Randomizer(whitelist=['Shotguns', 'Assault Rifles', 'Sniper Rifles', 'SMGs', 'Pistols', 'Heavy Weapons']).randomize()
    def all_gear_rand(self):
        print('Randomizing all gear...')
        Randomizer(whitelist=['Artifacts']).randomize()
        Randomizer(whitelist=['Shields']).randomize()
        Randomizer(whitelist=['Class Mods']).randomize()
        Randomizer(whitelist=['Grenade Mods']).randomize()

extreme_option = BoolOption(
    "Extreme",
    False,
    true_text="Weapons can have the parts of any weapon type",
    false_text="Weapons can only have parts of their own type"
)

def rand_all():
    RandHelper(extreme_option.value).all_wep_rand()

# `@hook("/Script/OakGame.MenuMapMenuFlow:OnPlayerControllerLogIn")
# def rand_hook(_1, _2, _3, _4):
#     rand_all()

@command
def rand_items(_):
    rand_all()


build_mod(
    auto_enable=True
)


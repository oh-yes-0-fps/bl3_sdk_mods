from mods_base import build_mod
from unrealsdk import unreal, find_object


PATTERN = find_object("LootSpawnPatternData", "/Game/GameData/Loot/SpawnPatterns/LootSpawnPattern_Default.LootSpawnPattern_Default")



build_mod(
    auto_enable=True,
)
from __future__ import annotations

from dataclasses import dataclass
import os
import pathlib
from threading import Thread
from time import sleep
import uuid
import json
import csv

import mods_base
import unrealsdk
from mods_base import SETTINGS_DIR, build_mod, hook, get_pc, keybind
from typing import Any
from unrealsdk.hooks import Type
from unrealsdk.unreal import BoundFunction, UObject, WrappedStruct, WrappedArray

from .settings import *

def get_output_path() -> pathlib.Path:
    path = None
    my_games = os.path.join(os.path.expanduser("~"), "Documents", "My Games")
    game = mods_base.Game.get_current()
    if game == mods_base.Game.BL3:
        path = pathlib.Path(os.path.join(my_games, "Borderlands 3", "CombatLogs"))
    else:
        path = pathlib.Path(
            os.path.join(my_games, "Tiny Tina's Wonderlands", "CombatLogs")
        )
    if not path.exists():
        path = SETTINGS_DIR / "CombatLogs"
    return path


def create_path_if_not_exists(path: pathlib.Path):
    if not path.exists():
        path.mkdir(parents=True)


@dataclass(slots=True, frozen=True)
class HealthTypeDamageSummary:
    health_type: str
    damage: float


@dataclass(slots=True, frozen=True)
class CombatLogEntry:
    enemy: str
    damage: float
    damage_source: str
    damage_type: str
    critical: bool
    radius: float
    damage_per_health_type: list[HealthTypeDamageSummary]

    def to_dict(self):
        return {
            "enemy": self.enemy,
            "damage": self.damage,
            "damage_source": self.damage_source,
            "damage_type": self.damage_type,
            "critical": self.critical,
            "radius": self.radius,
            "damage_per_health_type": [
                {"health_type": h.health_type, "damage": h.damage}
                for h in self.damage_per_health_type
            ],
        }


@dataclass(slots=True, frozen=True)
class CombatLogConfig:
    minimum_damage: float
    only_crits: bool
    allow_self_damage: bool

    @staticmethod
    def from_settings():
        return CombatLogConfig(
            minimum_damage=minimum_damage.value,
            only_crits=only_crits.value,
            allow_self_damage=allow_self_damage.value,
        )

@dataclass
class CombatLogger:
    config: CombatLogConfig
    memory: list[CombatLogEntry]
    player: UObject
    id: uuid.UUID
    flusher: Thread
    enabled = False

    def __init__(self, config: CombatLogConfig):
        self.config = config
        self.memory = []
        self.player = get_pc()
        self.id = uuid.uuid4()
        self.flusher = Thread(target=self.flush_runner)

    def flush_json(self, id: uuid.UUID):
        path = get_output_path()
        create_path_if_not_exists(path)
        path = path / f"combat_log_{id}.json"
        with open(path, "w") as f:
            json.dump([entry.to_dict() for entry in self.memory], f, indent=4)

    def flush_csv(self, id: uuid.UUID):
        path = get_output_path()
        create_path_if_not_exists(path)
        path = path / f"combat_log_{id}.csv"
        with open(path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(
                [
                    "Enemy",
                    "Damage",
                    "Damage Source",
                    "Damage Type",
                    "Critical",
                    "Radius",
                ]
            )
            for entry in self.memory:
                writer.writerow(
                    [
                        entry.enemy,
                        entry.damage,
                        entry.damage_source,
                        entry.damage_type,
                        entry.critical,
                        entry.radius,
                    ]
                )

    def flush(self):
        self.flush_json(self.id)
        self.flush_csv(self.id)

    def flush_runner(self):
        last_mem_len = len(self.memory)
        while self.enabled:
            mem_len = len(self.memory)
            if mem_len < last_mem_len:
                break
            if mem_len - last_mem_len > 0:
                self.flush()
                last_mem_len = len(self.memory)
            sleep(1)

    def add_entry(self, entry: CombatLogEntry):
        self.memory.append(entry)

    def start(self):
        self.config = CombatLogConfig.from_settings()
        self.enabled = True
        self.player = get_pc()
        self.id = uuid.uuid4()
        self.flusher = Thread(target=self.flush_runner)
        self.flusher.start()
        OnDamage.enable()
        unrealsdk.logging.info("Combat Logger Started")

    def end(self):
        if self.enabled: self.flush()
        self.enabled = False
        self.memory = []
        OnDamage.disable()
        unrealsdk.logging.info("Combat Logger Ended")

COMBAT_LOGGER: CombatLogger = CombatLogger(CombatLogConfig.from_settings())

@keybind("Toggle Combat Logger")
def toggle_combat_logger():
    if COMBAT_LOGGER.enabled:
        COMBAT_LOGGER.end()
    else:
        COMBAT_LOGGER.start()


@hook(
    "/Script/GbxGameSystemCore.DamageComponent:ReceiveAnyDamage",
    Type.POST_UNCONDITIONAL
)
def OnDamage(
    caller: UObject, params: WrappedStruct, _3: Any, _4: BoundFunction
) -> None:
    if COMBAT_LOGGER.enabled:
        cl: CombatLogger = COMBAT_LOGGER  # type: ignore
        if (
            bool(caller == cl.player.Pawn.OakDamageComponent)
            and cl.config.allow_self_damage == False
        ):
            return
        if params.InstigatedBy != cl.player:
            return
        if params.Damage < cl.config.minimum_damage:
            return

        # TODO add dot and damagetype checks

        # damage_per_health_type = []
        # for i in params.Details.DamagePerHealthType:
        #     damage_per_health_type.append(
        #         HealthTypeDamageSummary(i.HealthType.Name, i.Damage)
        #     )
        entry = CombatLogEntry(
            enemy=caller.GetOwner().Name,
            damage=params.Damage,
            damage_source=str(params.DamageSource.Name)
                .removesuffix("_C")
                .removeprefix("Default__"),
            damage_type=str(params.DamageType.Name)
                .removesuffix("_C")
                .removeprefix("Default__"),
            critical=params.Details.bWasCrit,
            radius=params.Details.DamageRadius,
            damage_per_health_type=[],
        )
        cl.add_entry(entry)


@hook("/Script/OakGame.GFxPauseMenu:OnQuitChoiceMade", Type.POST_UNCONDITIONAL, auto_enable=True)
def close_logger_on_quit(_1: UObject, _2: Any, _3: Any, _4: BoundFunction) -> None:
    if COMBAT_LOGGER.enabled:
        COMBAT_LOGGER.end()


build_mod(
    auto_enable=True,
    name="Combat Logger",
    keybinds=[toggle_combat_logger],
    options=[
        only_crits,
        allow_self_damage,
        minimum_damage
    ],
)
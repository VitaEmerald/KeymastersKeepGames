from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


# Option Dataclass
@dataclass
class ArchipelagoOptions:
    pass

# Main Class
class MetroidPrimeGame(Game):
    name = "Metroid Prime"
    platform = KeymastersKeepGamePlatforms.GC

    platforms_other = [
        KeymastersKeepGamePlatforms.WII,
        KeymastersKeepGamePlatforms.WIIU,
        KeymastersKeepGamePlatforms.SW,
    ]

    is_adult_only_or_unrated = False

    options_cls = ArchipelagoOptions

    # Optional Game Constraints
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
            ),
        ]

    # Main Objectives
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Obtain the following item: MAJORITEMS",
                data={
                    "MAJORITEMS": (self.majoritems, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Scan and Defeat ENEMY",
                data={
                    "ENEMY": (self.enemies, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Defeat COUNT enemies in LEVEL",
                data={
                    "COUNT": (self.enemy_count, 1),
                    "LEVEL": (self.levels, 1),
                    },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
        ]

    # Datasets
    @staticmethod
    def majoritems() -> List[str]:
        return [
            "Morph Ball",
            "Charge Beam",
            "Morph Ball Bombs",
            "Varia Suit",
            "Boost Ball",
            "Space Jump Boots",
            "Wave Beam",
            "Super Missiles",
            "Thermal Visor",
            "Spider Ball",
            "Ice Beam",
            "Gravity Suit",
            "Power Bombs",
            "X-Ray Visor",
            "Grapple Beam",
            "Plasma Beam",
            "Phazon Suit",
            "Wavebuster",
            "Ice Spreader",
            "Flamethrower",
        ]
    
    @staticmethod
    def levels(self) -> List[str]:
        return [
            "Tallon Overworld",
            "Chozo Ruins",
            "Magmoor Caverns"
            "Phendrana Drifts"
            "Phazon Mines",
        ]
    
    @staticmethod
    def enemies() -> List[str]:
        return [
            "Auto Turret",
            "Zoomer",
            "Geemer",
            "Sap Sac",
            "Bloodflower",
            "Seedling",
            "Scarab",
            "Beetle",
            "Plated Beetle",
            "War Wasp",
            "Plazmite",
            "Shriekbat",
            "Stone Toad",
            "Plated Parasite",
            "Chozo Ghost",
            "Grizby",
            "Burrower",
            "Puffer",
            "Triclops",
            "Magmoor",
            "Crystallite",
            "Pulse Bombu",
            "Scatter Bombu",
            "Ice Beetle",
            "Flickerbat",
            "Jelzap",
            "Baby Sheegoth",
            "Sheegoth",
            "Sentry Drone",
            "Space Pirate",
            "Shadow Pirate",
            "Flying Pirate",
            "Aqua Sac",
            "Tallon Crab",
            "Mega Turret",
            "Power Trooper",
            "Wave Trooper",
            "Ice Trooper",
            "Plasma Trooper",
            "Metroid",
            "Hunter Metroid",
        ]

    # picks a random number from 5-10
    @staticmethod
    def enemy_count() -> range:
        return range(5, 10)
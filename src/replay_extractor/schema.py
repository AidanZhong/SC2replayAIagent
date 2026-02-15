# -*- coding: utf-8 -*-
"""
Created on 15/02/2026 22:21

@author: Aidan
@project: SC2replayAIagent
@filename: schema
"""
from dataclasses import dataclass, asdict
from typing import Literal, Optional, List, Dict, Any

EventType = Literal[
    "building_started",
    "building_finished",
    "unit_started",
    "unit_finished",
    "upgrade_started",
    "upgrade_finished",
    "ability_used"
]


@dataclass
class PlayerMeta:
    id: int
    name: str
    race: str


@dataclass
class ReplayMeta:
    game_duration: float
    map_name: Optional[str]
    game_version: Optional[str]
    winner_id: Optional[int]
    players: List[PlayerMeta]


@dataclass
class TimelineEvent:
    t: float
    player_id: int
    event_type: EventType
    name: str
    tags: Dict[str, Any] = None  # {"location":[x,y]}

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        if d["tags"] is None:
            d["tags"] = {}
        return d


@dataclass
class Snapshot:
    t: float
    player_id: int
    minerals: int
    vespene: int
    supply_used: int
    supply_cap: int
    workers: int


@dataclass
class TimelineJSON:
    metadata: ReplayMeta
    events: List[TimelineEvent]
    snapshots: List[Snapshot]
    derived: Dict[str, Any]  # computed later

    def to_dict(self) -> Dict[str, Any]:
        return {
            "metadata": asdict(self.metadata),
            "events": [e.to_dict() for e in self.events],
            "snapshots": [asdict(s) for s in self.snapshots],
            "derived": self.derived
        }

# -*- coding: utf-8 -*-
"""
Created on 15/02/2026 22:32

@author: Aidan
@project: SC2replayAIagent
@filename: extractor
"""
import argparse
import json
from pathlib import Path

from src.replay_extractor.schema import ReplayMeta, PlayerMeta, TimelineJSON


def extract_replay():
    ap = argparse.ArgumentParser()
    ap.add_argument("replay", type=str)
    ap.add_argument("--output", type=str, required=True)
    args = ap.parse_args()
    meta = ReplayMeta(
        game_duration=0.0,
        map_name="",
        game_version="",
        winner_id=1,
        players=[
            PlayerMeta(id=1, name="P1", race="Random"),
            PlayerMeta(id=2, name="P2", race="Random")
        ],
    )

    timeline = TimelineJSON(metadata=meta, events=[], snapshots=[], derived={})
    Path(args.output).write_text(json.dumps(timeline.to_dict(), indent=4), encoding="utf-8")
    print(f"Replay extracted to {args.output}")


if __name__ == "__main__":
    extract_replay()

# -*- coding: utf-8 -*-
"""
Created on 15/02/2026 22:48

@author: Aidan
@project: SC2replayAIagent
@filename: sc2extractor_compare
"""
from __future__ import annotations

import sc2reader
# s2protocol needs an MPQ reader to unpack sections:
# pip install s2protocol mpyq
from mpyq import MPQArchive  # type: ignore
from s2protocol import versions  # type: ignore

if __name__ == '__main__':
    REPLAY_PATH = "../data/1. Oceanborn.SC2Replay"

    # -------------------------
    # A) sc2reader: load replay
    # -------------------------
    r1 = sc2reader.load_replay(REPLAY_PATH, load_level=4)

    # r1 is the sc2reader replay object
    # you can explore: r1.players, r1.events, r1.tracker_events, etc.

    # -----------------------------------------
    # B) s2protocol: unpack + decode raw sections
    # -----------------------------------------
    archive = MPQArchive(REPLAY_PATH)

    # raw bytes for each replay section
    header_bytes = archive.read_file("replay.header")
    details_bytes = archive.read_file("replay.details")
    init_bytes = archive.read_file("replay.initData")
    game_events_bytes = archive.read_file("replay.game.events")
    tracker_events_bytes = archive.read_file("replay.tracker.events")

    # pick correct protocol version from header
    proto_latest = versions.latest()
    header = proto_latest.decode_replay_header(header_bytes)
    base_build = header["m_version"]["m_baseBuild"]
    protocol = versions.build(base_build)

    # decoded (still “raw” structured dict/list outputs)
    details = protocol.decode_replay_details(details_bytes)
    initdata = protocol.decode_replay_initdata(init_bytes)
    game_events = protocol.decode_replay_game_events(game_events_bytes)
    tracker_events = protocol.decode_replay_tracker_events(tracker_events_bytes)

    print(details)

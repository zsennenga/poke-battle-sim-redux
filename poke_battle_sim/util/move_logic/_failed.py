from __future__ import annotations
import poke_battle_sim.core.battle as bt


def _failed(battle: bt.Battle) -> None:
    battle.add_text("But, it failed!")

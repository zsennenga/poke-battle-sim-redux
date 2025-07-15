from __future__ import annotations
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt


def _missed(attacker: pk.Pokemon, battle: bt.Battle):
    battle.add_text(f"{attacker.nickname}'s attack missed!")

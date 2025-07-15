from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._failed import _failed


def _effect_spikes(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    enemy = defender.trainer
    if enemy.spikes < 3:
        enemy.spikes += 1
        battle.add_text(
            f"Spikes were scattered all around the feet of {enemy.name}'s team!"
        )
    else:
        _failed(battle)

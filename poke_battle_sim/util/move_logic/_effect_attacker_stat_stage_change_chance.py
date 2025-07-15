from __future__ import annotations
from random import randrange
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_attacker_stat_stage_change_chance(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    dmg = _calculate_damage(attacker, defender, battlefield, battle, move_data)
    if attacker.is_alive and dmg and randrange(1, 101) < move_data.ef_chance:
        give_stat_change(
            attacker, battle, move_data.ef_stat, move_data.ef_amount, bypass=True
        )
    return True

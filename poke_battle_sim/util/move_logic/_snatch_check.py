from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_data as gd


def _snatch_check(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
) -> bool:
    if defender.is_alive and defender.snatch and move_data.name in gd.SNATCH_CHECK:
        battle.add_text(
            defender.nickname + " snatched " + attacker.nickname + "'s move!"
        )
        _process_effect(defender, attacker, battlefield, battle, move_data, is_first)
        return True
    return False

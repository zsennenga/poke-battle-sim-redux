from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_knock_off(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    dmg = _calculate_damage(attacker, defender, battlefield, battle, move_data)
    if defender.is_alive and dmg and defender.item and defender.h_item:
        battle.add_text(
            attacker.nickname
            + " knocked off "
            + defender.nickname
            + "'s "
            + cap_name(defender.item)
            + "!"
        )
        defender.item = None
    return True

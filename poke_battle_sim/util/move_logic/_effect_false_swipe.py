from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._calculate_damage import _calculate_damage


def _effect_false_swipe(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    dmg = _calculate_damage(
        attacker, defender, battlefield, battle, move_data, skip_dmg=True
    )
    if not dmg:
        return True
    if not defender.substitute and dmg >= defender.cur_hp:
        dmg = defender.cur_hp - 1
    defender.take_damage(dmg, move_data)
    return True

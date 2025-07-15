from __future__ import annotations
from random import randrange
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._calculate_damage import _calculate_damage
from poke_battle_sim.util.move_logic._flinch import _flinch


def _effect_twister(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if defender.in_air:
        cc_ib[1] = True
        move_data.power *= 2
    dmg = _calculate_damage(
        attacker, defender, battlefield, battle, move_data, cc_ib[0], cc_ib[1]
    )
    if dmg and randrange(5) < 1:
        _flinch(defender, battle, is_first)
    return True

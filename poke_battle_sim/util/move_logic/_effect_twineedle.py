from __future__ import annotations
from random import randrange
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._calculate_damage import _calculate_damage
from poke_battle_sim.util.move_logic.poison import poison


def _effect_twineedle(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    dmg = _calculate_damage(attacker, defender, battlefield, battle, move_data)
    if not defender.is_alive or not dmg:
        return True
    if randrange(1, 6) < 2:
        poison(defender, battle)
    dmg = _calculate_damage(attacker, defender, battlefield, battle, move_data)
    if dmg and randrange(5) < 1:
        poison(defender, battle)
    return True

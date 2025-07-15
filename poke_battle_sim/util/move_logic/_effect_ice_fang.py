from __future__ import annotations
from random import randrange
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._calculate_damage import _calculate_damage
from poke_battle_sim.util.move_logic._flinch import _flinch
from poke_battle_sim.util.move_logic.freeze import freeze


def _effect_ice_fang(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    dmg = _calculate_damage(attacker, defender, battlefield, battle, move_data)
    if defender.is_alive and dmg:
        if randrange(1, 101) < move_data.ef_chance:
            freeze(defender, battle)
        if randrange(1, 101) < move_data.ef_chance:
            _flinch(defender, battle, is_first)
    return True

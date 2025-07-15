from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._calculate_type_ef import _calculate_type_ef
from poke_battle_sim.util.move_logic._missed import _missed


def _effect_sonic_boom(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if defender.is_alive and _calculate_type_ef(defender, move_data) != 0:
        defender.take_damage(move_data.ef_amount, move_data)
    else:
        _missed(attacker, battle)
    return True

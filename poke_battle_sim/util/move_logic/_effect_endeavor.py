from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_endeavor(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if (
        defender.is_alive
        and attacker.cur_hp < defender.cur_hp
        and _calculate_type_ef(defender, move_data)
    ):
        defender.take_damage(defender.cur_hp - attacker.cur_hp)
    else:
        _failed(battle)
    return True

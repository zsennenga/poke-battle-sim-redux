from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs


def _effect_counter(
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
        and attacker.last_move_hit_by
        and defender.last_move
        and attacker.last_move_hit_by.name == defender.last_move.name
        and attacker.last_move_hit_by.category == gs.PHYSICAL
        and _calculate_type_ef(defender, move_data)
    ):
        defender.take_damage(attacker.last_damage_taken * 2, move_data)
    else:
        _failed(battle)
    return True

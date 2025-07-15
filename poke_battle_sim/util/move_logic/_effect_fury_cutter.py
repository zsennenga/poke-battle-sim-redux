from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_fury_cutter(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if (
        attacker.last_move
        and attacker.last_move is attacker.last_successful_move
        and attacker.last_move.name == move_data.name
    ):
        move_data.ef_stat = min(5, int(attacker.last_move.ef_stat) + 1)
        move_data.power = move_data.o_power * 2 ** (move_data.ef_stat - 1)
    else:
        move_data.ef_stat = 1

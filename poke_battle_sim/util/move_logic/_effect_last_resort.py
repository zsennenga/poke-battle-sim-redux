from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_last_resort(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if len(attacker.moves) < 2 or not all(
        [
            (
                attacker.moves[i].cur_pp < attacker.old_pp[i]
                or attacker.moves[i] == "last-resort"
            )
            for i in range(len(attacker.moves))
        ]
    ):
        _failed(battle)
        return True

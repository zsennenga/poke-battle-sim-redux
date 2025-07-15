from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_spite(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if defender.is_alive and defender.last_move and defender.last_move.cur_pp:
        if defender.last_move.cur_pp < 4:
            amt_reduced = defender.last_move.cur_pp
        else:
            amt_reduced = 4
        defender.last_move.cur_pp -= amt_reduced
        battle.add_text(
            "It reduced the pp of "
            + defender.nickname
            + "'s "
            + cap_name(defender.last_move.name)
            + " by "
            + str(amt_reduced)
            + "!"
        )
    else:
        _failed(battle)

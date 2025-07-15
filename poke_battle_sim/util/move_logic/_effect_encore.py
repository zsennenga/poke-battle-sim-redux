from __future__ import annotations
from random import randrange
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_data as gd
from poke_battle_sim.util.move_logic._failed import _failed


def _effect_encore(
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
        and not defender.encore_count
        and defender.last_move
        and defender.last_move.cur_pp
        and defender.last_move not in gd.ENCORE_CHECK
        and any([(move.name == defender.last_move.name) for move in defender.moves])
    ):
        defender.next_moves.clear()
        defender.encore_count = min(randrange(2, 7), defender.last_move.pp)
        for move in defender.moves:
            if move.name != defender.last_move.name:
                move.encore_blocked = True
            else:
                defender.encore_move = move
        battle.add_text(defender.nickname + " received an encore!")
    else:
        _failed(battle)

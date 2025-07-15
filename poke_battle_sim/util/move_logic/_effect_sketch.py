from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._failed import _failed


def _effect_sketch(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if (
        attacker.transformed
        or not move_data in attacker.original_moves
        or not defender.is_alive
        or not defender.last_move
        or attacker.is_move(defender.last_move.name)
    ):
        _failed(battle)
        return True
    attacker.moves[move_data.pos] = Move(defender.last_move.md)

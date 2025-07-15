from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_copycat(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if battle.last_move and battle.last_move.name != move_data.name:
        _process_effect(
            attacker, defender, battlefield, battle, Move(battle.last_move.md), is_first
        )
        return True
    else:
        _failed(battle)

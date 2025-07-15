from __future__ import annotations
from random import randrange
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._failed import _failed


def _effect_disable(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    has_disabled = not all([(not move.disabled) for move in defender.moves])
    if not defender.last_move or not defender.last_move.cur_pp or has_disabled:
        _failed(battle)
    else:
        disabled_move = defender.last_move
        disabled_move.disabled = randrange(4, 8)
        battle.add_text(
            defender.trainer.name
            + "'s "
            + defender.nickname
            + "'s "
            + disabled_move.name
            + " was disabled!"
        )

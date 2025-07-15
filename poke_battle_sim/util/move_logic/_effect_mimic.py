from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._failed import _failed
from poke_battle_sim.util.move_logic.cap_name import cap_name


def _effect_mimic(
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
        and defender.last_move
        and not attacker.copied
        and not attacker.is_move(defender.last_move.md)
    ):
        attacker.copied = Move(defender.last_move.md)
        attacker.copied.max_pp = min(5, attacker.copied.max_pp)
        attacker.copied.cur_pp = attacker.copied.max_pp
        battle.add_text(
            attacker.nickname + " learned " + cap_name(attacker.copied.name)
        )
    else:
        _failed(battle)

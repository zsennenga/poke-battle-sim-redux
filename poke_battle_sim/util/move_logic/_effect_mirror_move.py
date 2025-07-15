from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._failed import _failed
from poke_battle_sim.util.move_logic._process_effect import _process_effect
from poke_battle_sim.util.move_logic.cap_name import cap_name


def _effect_mirror_move(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if defender.is_alive and defender.last_move:
        battle.add_text(
            attacker.nickname + " used " + cap_name(defender.last_move.name) + "!"
        )
        _process_effect(
            attacker, defender, battlefield, battle, defender.last_move, is_first
        )
    else:
        _failed(battle)
    return True

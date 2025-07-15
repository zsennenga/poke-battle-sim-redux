from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._failed import _failed
from poke_battle_sim.util.move_logic._process_effect import _process_effect
from poke_battle_sim.util.move_logic.cap_name import cap_name


def _effect_me_first(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if attacker.mf_move:
        if attacker.mf_move.power:
            attacker.mf_move.power = int(1.5 * attacker.mf_move.power)
        battle.add_text(
            attacker.nickname + " used " + cap_name(attacker.mf_move.name) + "!"
        )
        _process_effect(
            attacker, defender, battlefield, battle, attacker.mf_move, is_first
        )
        attacker.mf_move = None
    else:
        _failed(battle)
    return True

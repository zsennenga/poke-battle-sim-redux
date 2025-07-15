from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._failed import _failed


def _effect_focus_punch(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if not defender.is_alive:
        _failed(battle)
        return True
    if attacker.turn_damage:
        battle._pop_text()
        battle.add_text(attacker.nickname + " lost its focus and couldn't move!")
        return True

from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_pain_split(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if defender.is_alive:
        new_hp = (attacker.cur_hp + defender.cur_hp) // 2
        battle.add_text("The battlers shared their pain!")
        attacker.cur_hp = min(new_hp, attacker.max_hp)
        defender.cur_hp = min(new_hp, defender.max_hp)
    else:
        _failed(battle)
    return True

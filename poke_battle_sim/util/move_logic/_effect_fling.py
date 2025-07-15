from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_fling(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if attacker.item:
        battle.add_text(attacker.nickname + " flung its " + attacker.item + "!")
        move_data.power = 20
        _calculate_damage(attacker, defender, battlefield, battle, move_data)
        if attacker.is_alive:
            attacker.give_item(None)
    else:
        _failed(battle)

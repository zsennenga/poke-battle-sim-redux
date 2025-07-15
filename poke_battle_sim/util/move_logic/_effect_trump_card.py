from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_trump_card(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if move_data.cur_pp >= 4:
        move_data.power = 40
    elif move_data.cur_pp == 3:
        move_data.power = 50
    elif move_data.cur_pp == 2:
        move_data.power = 60
    elif move_data.cur_pp == 1:
        move_data.power = 80
    else:
        move_data.power = 200

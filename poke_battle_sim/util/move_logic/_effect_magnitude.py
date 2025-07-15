from __future__ import annotations
from random import randrange
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_magnitude(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    res = randrange(20)
    if res < 1:
        mag = 4
        move_data.power = 10
    elif res < 3:
        mag = 5
        move_data.power = 30
    elif res < 7:
        mag = 6
        move_data.power = 50
    elif res < 13:
        mag = 7
        move_data.power = 70
    elif res < 17:
        mag = 8
        move_data.power = 90
    elif res < 19:
        mag = 9
        move_data.power = 110
    else:
        mag = 10
        move_data.power = 150
    if defender.in_ground:
        cc_ib[1] = True
        move_data.power *= 2
    battle.add_text(f"Magnitude {str(mag)}!")

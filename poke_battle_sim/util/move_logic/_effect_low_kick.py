from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_low_kick(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if defender.weight < 100:
        move_data.power = 20
    elif defender.weight < 250:
        move_data.power = 40
    elif defender.weight < 500:
        move_data.power = 60
    elif defender.weight < 1000:
        move_data.power = 80
    elif defender.weight < 2000:
        move_data.power = 100
    else:
        move_data.power = 120

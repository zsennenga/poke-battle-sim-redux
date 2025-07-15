from __future__ import annotations
from random import randrange
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_hidden_power(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    hp_stats = attacker.hidden_power_stats()
    if hp_stats:
        move_data.type, move_data.power = hp_stats
    else:
        move_data.power = randrange(30, 71)
        move_data.type = attacker.types[0]

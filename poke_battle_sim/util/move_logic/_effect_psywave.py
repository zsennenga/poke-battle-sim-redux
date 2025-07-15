from __future__ import annotations
from random import randrange
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_psywave(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    dmg = attacker.level * (randrange(0, 11) * 10 + 50) // 100
    if defender.is_alive:
        defender.take_damage(dmg if dmg != 0 else 1, move_data)
    else:
        _missed(attacker, battle)
    return True

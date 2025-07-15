from __future__ import annotations
from random import randrange
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_protect(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if attacker.substitute:
        _failed(battle)
    p_chance = min(8, 2**attacker.protect_count)
    if randrange(p_chance) < 1:
        attacker.invulnerable = True
        attacker.protect = True
        attacker.protect_count += 1
    else:
        _failed(battle)

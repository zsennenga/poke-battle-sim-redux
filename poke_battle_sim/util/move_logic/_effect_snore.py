from __future__ import annotations
from random import randrange
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs


def _effect_snore(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if defender.is_alive and attacker.nv_status == gs.ASLEEP:
        dmg = _calculate_damage(attacker, defender, battlefield, battle, move_data)
        if dmg and randrange(10) < 3:
            _flinch(defender, battle, is_first)
    else:
        _failed(battle)
    return True

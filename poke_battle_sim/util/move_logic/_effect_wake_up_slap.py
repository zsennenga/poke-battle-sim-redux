from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs


def _effect_wake_up_slap(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if defender.nv_status == gs.ASLEEP:
        move_data.power *= 2
    dmg = _calculate_damage(attacker, defender, battlefield, battle, move_data)
    if defender.is_alive and dmg:
        cure_nv_status(gs.ASLEEP, defender, battle)
    return True

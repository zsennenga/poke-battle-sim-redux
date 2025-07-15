from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_flail(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    hp_ratio = int(float(attacker.cur_hp) / attacker.max_hp * 10000)
    if hp_ratio >= 6719:
        move_data.power = 20
    elif hp_ratio >= 3438:
        move_data.power = 40
    elif hp_ratio >= 2031:
        move_data.power = 80
    elif hp_ratio >= 938:
        move_data.power = 100
    elif hp_ratio >= 313:
        move_data.power = 150
    else:
        move_data.power = 200

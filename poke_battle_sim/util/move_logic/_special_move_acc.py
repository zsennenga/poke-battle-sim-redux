from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs


def _special_move_acc(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
) -> bool:
    if move_data.name == "thunder":
        if battlefield.weather == gs.RAIN and not defender.in_ground:
            return True
        if battlefield.weather == gs.HARSH_SUNLIGHT:
            move_data.acc = 50
    return False

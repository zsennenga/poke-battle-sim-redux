from __future__ import annotations
from random import randrange
from poke_battle_sim.poke_sim import PokeSim
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.util.process_ability as pa
import poke_battle_sim.util.process_item as pi
import poke_battle_sim.conf.global_settings as gs
import poke_battle_sim.conf.global_data as gd

def _ef_035(
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

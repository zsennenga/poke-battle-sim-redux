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

def _grounded_check(attacker: pk.Pokemon, battle: bt.Battle, move_data: Move) -> bool:
    if attacker.grounded and move_data.name in gd.GROUNDED_CHECK:
        _failed(battle)
        return True
    return False

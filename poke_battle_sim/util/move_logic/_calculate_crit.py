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

def _calculate_crit(crit_chance: int = None) -> bool:
    if not crit_chance:
        return randrange(16) < 1
    elif crit_chance == 1:
        return randrange(9) < 1
    elif crit_chance == 2:
        return randrange(5) < 1
    elif crit_chance == 3:
        return randrange(4) < 1
    elif crit_chance == 4:
        return randrange(3) < 1
    else:
        return randrange(1000) < crit_chance

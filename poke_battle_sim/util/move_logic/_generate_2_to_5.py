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

def _generate_2_to_5() -> int:
    n = randrange(8)
    if n < 3:
        num_hits = 2
    elif n < 6:
        num_hits = 3
    elif n < 7:
        num_hits = 4
    else:
        num_hits = 5
    return num_hits

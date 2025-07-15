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

def _truant_check(attacker: pk.Pokemon, battle: bt.Battle, move_data: Move) -> bool:
    if (
        attacker.has_ability("truant")
        and attacker.last_move
        and move_data.name == attacker.last_move.name
    ):
        battle.add_text(attacker.nickname + " loafed around!")
        return True
    return False

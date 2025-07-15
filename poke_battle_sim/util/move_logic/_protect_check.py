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

def _protect_check(defender: pk.Pokemon, battle: bt.Battle, move_data: Move) -> bool:
    if (
        defender.is_alive
        and defender.protect
        and not move_data.name in ["feint", "shadow-force"]
        and move_data.target in gd.PROTECT_TARGETS
    ):
        battle.add_text(defender.nickname + " protected itself!")
        return True
    return False

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

def _soundproof_check(defender: pk.Pokemon, battle: bt.Battle, move_data: Move) -> bool:
    if (
        defender.is_alive
        and defender.has_ability("soundproof")
        and move_data in gd.SOUNDPROOF_CHECK
    ):
        battle.add_text("It doesn't affect " + defender.nickname)
        return True
    return False

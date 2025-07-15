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

def _safeguard_check(poke: pk.Pokemon, battle: bt.Battle) -> bool:
    if poke.trainer.safeguard:
        battle.add_text(poke.nickname + " is protected by Safeguard!")
        return True
    return False

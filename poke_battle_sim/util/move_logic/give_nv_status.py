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

def give_nv_status(
    status: int, recipient: pk.Pokemon, battle: bt.Battle, forced: bool = False
):
    if status == gs.BURNED:
        burn(recipient, battle, forced)
    elif status == gs.FROZEN:
        freeze(recipient, battle, forced)
    elif status == gs.PARALYZED:
        paralyze(recipient, battle, forced)
    elif status == gs.POISONED:
        poison(recipient, battle, forced)
    elif status == gs.ASLEEP:
        sleep(recipient, battle, forced)
    elif status == gs.BADLY_POISONED:
        badly_poison(recipient, battle, forced)

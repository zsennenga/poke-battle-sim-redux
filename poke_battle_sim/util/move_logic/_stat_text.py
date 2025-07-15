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

def _stat_text(recipient: pk.Pokemon, stat: int, amount: int) -> str:
    if stat == gs.ACC:
        cur_stage = recipient.accuracy_stage
    elif stat == gs.EVA:
        cur_stage = recipient.evasion_stage
    else:
        cur_stage = recipient.stat_stages[stat]
    if not amount:
        return
    base = recipient.nickname + "'s " + gs.STAT_TO_NAME[stat]
    if amount > 0:
        dif = min(6 - cur_stage, amount)
        if dif <= 0:
            base += " won't go any higher!"
        elif dif == 1:
            base += " rose!"
        elif dif == 2:
            base += " rose sharply!"
        else:
            base += " rose drastically!"
    else:
        dif = max(-6 - cur_stage, amount)
        if dif >= 0:
            base += " won't go any lower!"
        elif dif == -1:
            base += " fell!"
        elif dif == -2:
            base += " fell harshly!"
        else:
            base += " fell severely!"
    return base

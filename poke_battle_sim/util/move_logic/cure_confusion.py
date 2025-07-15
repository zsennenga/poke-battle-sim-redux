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

def cure_confusion(recipient: pk.Pokemon, battle: bt.Battle):
    if recipient.is_alive and recipient.v_status[gs.CONFUSED]:
        recipient.v_status[gs.CONFUSED] = 0
        battle.add_text(recipient.nickname + " snapped out of its confusion!")

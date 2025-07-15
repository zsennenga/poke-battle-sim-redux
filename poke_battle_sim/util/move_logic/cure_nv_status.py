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

def cure_nv_status(status: int, recipient: pk.Pokemon, battle: bt.Battle):
    if not recipient.is_alive or not status:
        return
    if recipient.nv_status != status and not (
        status == gs.POISONED and recipient.nv_status == gs.BADLY_POISONED
    ):
        return
    if status == gs.BURNED:
        text = "'s burn was healed!"
    elif status == gs.FROZEN:
        text = " thawed out!"
    elif status == gs.PARALYZED:
        text = " was cured of paralysis!"
    elif status == gs.ASLEEP:
        text = " woke up!"
    else:
        text = " was cured of poison!"

    recipient.nv_status = 0
    battle.add_text(recipient.nickname + text)

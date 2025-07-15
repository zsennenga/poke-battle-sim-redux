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

def _flinch(
    recipient: pk.Pokemon, battle: bt.Battle, is_first: bool, forced: bool = False
):
    if (
        not recipient.is_alive
        or recipient.substitute
        or recipient.has_ability("shield-dust")
    ):
        return
    if is_first and recipient.is_alive and not recipient.v_status[gs.FLINCHED]:
        if not recipient.has_ability("inner-focus"):
            recipient.v_status[gs.FLINCHED] = 1
        elif forced:
            battle.add_text(
                recipient.nickname + " won't flinch because of its Inner Focus!"
            )

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

def confuse(
    recipient: pk.Pokemon, battle: bt.Battle, forced: bool = False, bypass: bool = False
):
    if (
        not recipient.is_alive
        or recipient.substitute
        or recipient.has_ability("own-tempo")
    ):
        if forced:
            _failed(battle)
        return
    if _safeguard_check(recipient, battle):
        return
    if not forced and not bypass and recipient.has_ability("shield-dust"):
        return
    if forced and recipient.v_status[gs.CONFUSED]:
        battle.add_text(recipient.nickname + " is already confused!")
        return
    recipient.v_status[gs.CONFUSED] = _generate_2_to_5()
    battle.add_text(recipient.nickname + " became confused!")
    pi.status_items(recipient, battle)

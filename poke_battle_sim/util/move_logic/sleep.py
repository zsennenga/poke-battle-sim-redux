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

def sleep(recipient: pk.Pokemon, battle: bt.Battle, forced: bool = False):
    if (
        not recipient.is_alive
        or recipient.substitute
        or recipient.has_ability("insomnia")
        or recipient.has_ability("vital-spirit")
        or (
            recipient.has_ability("leaf-guard")
            and battle.battlefield.weather == gs.HARSH_SUNLIGHT
        )
    ):
        if forced:
            _failed(battle)
        return
    if _safeguard_check(recipient, battle):
        return
    if not forced and recipient.has_ability("shield-dust"):
        return
    if forced and recipient.nv_status == gs.ASLEEP:
        battle.add_text(recipient.nickname + " is already asleep!")
    elif not recipient.nv_status:
        recipient.nv_status = gs.ASLEEP
        recipient.nv_counter = randrange(2, 6)
        battle.add_text(recipient.nickname + " fell asleep!")
        if recipient.has_ability("synchronize"):
            sleep(recipient.enemy.current_poke, battle)
        pi.status_items(recipient, battle)

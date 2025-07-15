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

def infatuate(
    attacker: pk.Pokemon, defender: pk.Pokemon, battle: bt.Battle, forced: bool = False
):
    if (
        not defender.is_alive
        or defender.infatuation
        or defender.has_ability("oblivious")
    ):
        if forced:
            _failed(battle)
        return
    if (attacker.gender == "male" and defender.gender == "female") or (
        attacker.gender == "female" and defender.gender == "male"
    ):
        defender.infatuation = attacker
        battle.add_text(
            defender.nickname + " fell in love with " + attacker.nickname + "!"
        )
        pi.status_items(defender, battle)

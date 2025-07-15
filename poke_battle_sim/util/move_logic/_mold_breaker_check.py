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

def _mold_breaker_check(
    attacker: pk.Pokemon, defender: pk.Pokemon, end_turn: bool = True
):
    if not attacker.has_ability("mold-breaker"):
        return
    if not end_turn and not defender.ability_suppressed:
        defender.ability_suppressed = True
        attacker.ability_count = 1
    elif end_turn and attacker.ability_count:
        defender.ability_suppressed = False
        attacker.ability_count = 0

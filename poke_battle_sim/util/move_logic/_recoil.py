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

def _recoil(attacker: pk.Pokemon, battle: bt.Battle, damage: int, move_data: Move):
    if not attacker.is_alive or not damage:
        return
    if attacker.has_ability("rock-head") and move_data.name in gd.RECOIL_CHECK:
        return
    attacker.take_damage(damage)
    battle.add_text(attacker.nickname + " is hit with recoil!")

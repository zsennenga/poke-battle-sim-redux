from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
from poke_battle_sim.const.ability_enum import Ability
import poke_battle_sim.conf.global_data as gd


def _recoil(attacker: pk.Pokemon, battle: bt.Battle, damage: int, move_data: Move):
    if not attacker.is_alive or not damage:
        return
    if attacker.has_ability(Ability.ROCK_HEAD) and move_data.name in gd.RECOIL_CHECK:
        return
    attacker.take_damage(damage)
    battle.add_text(f"{attacker.nickname} is hit with recoil!")

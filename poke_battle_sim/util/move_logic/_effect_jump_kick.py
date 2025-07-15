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


def _effect_jump_kick(attacker: pk.Pokemon, defender: pk.Pokemon,
    battlefield: bf.Battlefield, battle: bt.Battle, move_data: Move,
    is_first: bool, cc_ib: list) ->bool:
    if not defender.is_alive:
        return True
    dmg = _calculate_damage(attacker, defender, battlefield, battle, move_data)
    if dmg:
        dmg //= 2
    elif dmg == 0 and attacker.enemy and _calculate_type_ef(defender, move_data
        ) == 0:
        dmg = defender.max_hp // 2
    if not dmg:
        return True
    battle.add_text(attacker.nickname + ' kept going and crashed!')
    attacker.take_damage(dmg)
    return True

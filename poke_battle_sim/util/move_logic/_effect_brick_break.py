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


def _effect_brick_break(attacker: pk.Pokemon, defender: pk.Pokemon,
    battlefield: bf.Battlefield, battle: bt.Battle, move_data: Move,
    is_first: bool, cc_ib: list) ->bool:
    if (defender.is_alive and not defender.invulnerable and not defender.
        protect):
        t = defender.trainer
        if t.light_screen or t.reflect:
            t.light_screen = 0
            t.reflect = 0
            battle.add_text('It shattered the barrier!')
        _calculate_damage(attacker, defender, battlefield, battle, move_data)
    else:
        _failed(battle)
    return True

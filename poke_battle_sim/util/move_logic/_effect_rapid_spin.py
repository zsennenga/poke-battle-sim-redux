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


def _effect_rapid_spin(attacker: pk.Pokemon, defender: pk.Pokemon,
    battlefield: bf.Battlefield, battle: bt.Battle, move_data: Move,
    is_first: bool, cc_ib: list) ->bool:
    _calculate_damage(attacker, defender, battlefield, battle, move_data)
    if attacker.is_alive:
        attacker.v_status[gs.BINDING_COUNT] = 0
        attacker.binding_type = None
        attacker.binding_poke = None
        attacker.v_status[gs.LEECH_SEED] = 0
        t = attacker.trainer
        t.spikes = 0
        t.toxic_spikes = 0
        t.steal_rock = 0
    return True

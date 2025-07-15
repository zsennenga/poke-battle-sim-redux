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


def _effect_me_first(attacker: pk.Pokemon, defender: pk.Pokemon,
    battlefield: bf.Battlefield, battle: bt.Battle, move_data: Move,
    is_first: bool, cc_ib: list) ->bool:
    if attacker.mf_move:
        if attacker.mf_move.power:
            attacker.mf_move.power = int(1.5 * attacker.mf_move.power)
        battle.add_text(attacker.nickname + ' used ' + cap_name(attacker.
            mf_move.name) + '!')
        _process_effect(attacker, defender, battlefield, battle, attacker.
            mf_move, is_first)
        attacker.mf_move = None
    else:
        _failed(battle)
    return True

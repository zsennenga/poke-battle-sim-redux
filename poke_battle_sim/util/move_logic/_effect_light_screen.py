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


def _effect_light_screen(attacker: pk.Pokemon, defender: pk.Pokemon,
    battlefield: bf.Battlefield, battle: bt.Battle, move_data: Move,
    is_first: bool, cc_ib: list) ->bool:
    t = attacker.trainer
    num_turns = 5 if attacker.item != 'light-clay' else 8
    if move_data.ef_stat == 1:
        if t.light_screen:
            _failed(battle)
            return True
        t.light_screen = num_turns
        battle.add_text('Light Screen raised ' + t.name +
            "'s team's Special Defense!")
    elif move_data.ef_stat == 2:
        if t.reflect:
            _failed(battle)
            return True
        t.reflect = num_turns
        battle.add_text('Light Screen raised ' + t.name + "'s team's Defense!")

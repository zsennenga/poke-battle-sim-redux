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


def _effect_rest(attacker: pk.Pokemon, defender: pk.Pokemon, battlefield:
    bf.Battlefield, battle: bt.Battle, move_data: Move, is_first: bool,
    cc_ib: list) ->bool:
    if not attacker.has_ability('insomnia') and not attacker.has_ability(
        'vital-spirit'):
        attacker.nv_status = gs.ASLEEP
        attacker.nv_counter = 3
        battle.add_text(attacker.nickname + ' went to sleep!')
        attacker.heal(attacker.max_hp)
    else:
        _failed(battle)

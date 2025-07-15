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


def _effect_roost(attacker: pk.Pokemon, defender: pk.Pokemon, battlefield:
    bf.Battlefield, battle: bt.Battle, move_data: Move, is_first: bool,
    cc_ib: list) ->bool:
    attacker.heal(max(1, attacker.max_hp // 2))
    if not is_first or not 'flying' in attacker.types:
        return True
    attacker.r_types = attacker.types
    other_type = [type for type in attacker.types if type != 'flying']
    if len(other_type) > 0:
        attacker.types = other_type[0], None
    else:
        attacker.types = 'normal', None

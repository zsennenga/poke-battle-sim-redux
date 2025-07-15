from __future__ import annotations
from random import randrange
from poke_battle_sim.poke_sim import PokeSim
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_conversion_2(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if not attacker.last_move_hit_by or not PokeSim.is_valid_type(
        attacker.last_move_hit_by.type
    ):
        _failed(battle)
        return True
    last_move_type = attacker.last_move_hit_by.type
    types = PokeSim.get_all_types()
    poss_types = []
    for type in types:
        if type and PokeSim.get_type_ef(last_move_type, type) < 1:
            poss_types.append(type)
    poss_types = [type for type in poss_types if type not in attacker.types]
    poss_types = PokeSim.filter_valid_types(poss_types)
    if len(poss_types):
        new_type = poss_types[randrange(len(poss_types))]
        attacker.types = new_type, None
        battle.add_text(
            attacker.nickname + " transformed into the " + new_type.upper() + " type!"
        )
    else:
        _failed(battle)

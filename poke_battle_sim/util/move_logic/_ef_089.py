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

def _ef_089(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if not move_data.ef_stat:
        if attacker.df_curl and move_data.power == move_data.o_power:
            move_data.power *= 2
        move_data.ef_stat = 1
    else:
        move_data.ef_stat += 1
    _calculate_damage(
        attacker, defender, battlefield, battle, move_data, cc_ib[0], cc_ib[1]
    )
    move_data.power *= 2
    if move_data.ef_stat < 5:
        attacker.next_moves.put(move_data)
    return True

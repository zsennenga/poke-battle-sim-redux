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


def _effect_beat_up(attacker: pk.Pokemon, defender: pk.Pokemon, battlefield:
    bf.Battlefield, battle: bt.Battle, move_data: Move, is_first: bool,
    cc_ib: list) ->bool:
    if not defender.is_alive:
        _failed(battle)
        return True
    poke_hits = [poke for poke in attacker.trainer.poke_list if not poke.
        nv_status]
    num_hits = 0
    move_data.power = 10
    while defender.is_alive and num_hits < len(poke_hits):
        _calculate_damage(attacker, defender, battlefield, battle, move_data)
        battle.add_text(poke_hits[num_hits].nickname + "'s attack!")
        num_hits += 1
    return True

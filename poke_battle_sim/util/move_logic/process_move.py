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

def process_move(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
):
    if _pre_process_status(attacker, defender, battlefield, battle, move_data):
        return
    battle.add_text(attacker.nickname + " used " + cap_name(move_data.name) + "!")
    battle.last_move_next = attacker.last_move_next = move_data
    if not _calculate_hit_or_miss(
        attacker, defender, battlefield, battle, move_data, is_first
    ):
        return
    attacker.last_successful_move_next = move_data
    if _meta_effect_check(attacker, defender, battlefield, battle, move_data, is_first):
        return
    _process_effect(attacker, defender, battlefield, battle, move_data, is_first)
    _post_process_status(attacker, defender, battlefield, battle, move_data)
    battle._faint_check()

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


def _effect_lunar_dance(attacker: pk.Pokemon, defender: pk.Pokemon,
    battlefield: bf.Battlefield, battle: bt.Battle, move_data: Move,
    is_first: bool, cc_ib: list) ->bool:
    t = attacker.trainer
    if t.num_fainted >= len(t.poke_list) - 1:
        _failed(battle)
    attacker.faint()
    battle._process_selection(t)
    battle.add_text(t.current_poke.nickname +
        'became cloaked in mystical moonlight!')
    t.current_poke.heal(t.current_poke.max_hp)
    t.current_poke.nv_status = 0
    for move in t.current_poke.moves:
        move.cur_pp = move.max_pp

from __future__ import annotations

import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.core.pokemon as pk
from poke_battle_sim.const.ability_enum import Ability
from poke_battle_sim.core.move import Move
from poke_battle_sim.util.move_logic._failed import _failed


def _effect_baton_pass(attacker: pk.Pokemon, defender: pk.Pokemon,
                       battlefield: bf.Battlefield, battle: bt.Battle, move_data: Move,
                       is_first: bool, cc_ib: list) -> bool:
    t = attacker.trainer
    old_poke = attacker
    if t.num_fainted >= len(t.poke_list) - 1 or battle._process_selection(t):
        _failed(battle)
    t.current_poke.v_status = attacker.v_status.copy()
    t.current_poke.stat_stages = attacker.stat_stages.copy()
    t.current_poke.perish_count = attacker.perish_count
    t.current_poke.trapped = attacker.trapped
    t.current_poke.perma_trapped = attacker.perma_trapped
    t.current_poke.embargo_count = attacker.embargo_count
    t.current_poke.magnetic_rise = attacker.magnet_rise
    t.current_poke.substitute = attacker.substitute
    t.current_poke.hb_count = attacker.hb_count
    t.current_poke.power_trick = attacker.power_trick
    if not attacker.has_ability(Ability.MULTITYPE):
        t.current_poke.ability_supressed = attacker.ability_suppressed

from __future__ import annotations
from random import randrange

from poke_battle_sim.const.ability_enum import Ability
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.util.process_ability as pa
import poke_battle_sim.util.process_item as pi
from poke_battle_sim.util.move_logic._missed import _missed
from poke_battle_sim.util.move_logic._special_move_acc import _special_move_acc


def _calculate_hit_or_miss(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
):
    d_eva_stage = defender.evasion_stage
    a_acc_stage = attacker.accuracy_stage
    if defender.foresight_target or defender.me_target:
        if defender.evasion_stage > 0:
            d_eva_stage = 0
    if attacker.has_ability(Ability.UNAWARE):
        d_eva_stage = 0
    if defender.has_ability(Ability.UNAWARE):
        a_acc_stage = 0
    stage = a_acc_stage - d_eva_stage
    stage_mult = max(3, 3 + stage) / max(3, 3 - stage)
    ability_mult = pa.homc_abilities(attacker, defender, battlefield, battle, move_data)
    item_mult = pi.homc_items(
        attacker, defender, battlefield, battle, move_data, is_first
    )

    ma = move_data.acc
    if _special_move_acc(attacker, defender, battlefield, battle, move_data):
        return True
    if not ma:
        return True
    if defender.mr_count and defender.mr_target and attacker is defender.mr_target:
        return True
    if attacker.has_ability(Ability.NO_GUARD) or defender.has_ability(Ability.NO_GUARD):
        return True
    if attacker.next_will_hit:
        attacker.next_will_hit = False
        return True

    if ma == -1:
        res = randrange(1, 101) <= attacker.level - defender.level + 30
    else:
        hit_threshold = (
            ma * stage_mult * battlefield.acc_modifier * item_mult * ability_mult
        )
        res = randrange(1, 101) <= hit_threshold
    if not res:
        if defender.evasion_stage > 0:
            battle.add_text(f"{defender.nickname} avoided the attack!")
        else:
            _missed(attacker, battle)
    return res

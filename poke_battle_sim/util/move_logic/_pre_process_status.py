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

def _pre_process_status(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
) -> bool:
    _mold_breaker_check(attacker, defender, end_turn=False)
    if attacker.inv_count:
        attacker.inv_count -= 1
        if not attacker.inv_count:
            attacker.invulnerable = False
            attacker.in_ground = False
            attacker.in_air = False
            attacker.in_water = False
    if attacker.prio_boost:
        attacker.prio_boost = False
    if attacker.nv_status == gs.FROZEN:
        if move_data.name in gd.FREEZE_CHECK or randrange(5) < 1:
            cure_nv_status(gs.FROZEN, attacker, battle)
        else:
            battle.add_text(attacker.nickname + " is frozen solid!")
            return True
    if attacker.nv_status == gs.ASLEEP:
        if not attacker.nv_counter:
            attacker.nv_status = 0
        else:
            attacker.nv_counter -= 1
        if attacker.nv_counter and attacker.has_ability(Ability.EARLY_BIRD):
            attacker.nv_counter -= 1
        if attacker.nv_counter > 0:
            battle.add_text(attacker.nickname + " is fast asleep!")
            if move_data.name != "snore" and move_data.name != "sleep-talk":
                return True
        battle.add_text(attacker.nickname + " woke up!")
    if attacker.v_status[gs.FLINCHED]:
        attacker.v_status[gs.FLINCHED] = 0
        battle.add_text(attacker.nickname + " flinched and couldn't move")
        if attacker.has_ability(Ability.STEADFAST):
            give_stat_change(attacker, battle, gs.ATK, 1)
        return True
    if attacker.nv_status == gs.PARALYZED:
        if randrange(4) < 1:
            battle.add_text(attacker.nickname + " is paralyzed! It can't move!")
            return True
    if attacker.infatuation:
        if not attacker.infatuation is defender:
            attacker.infatuation = None
            battle.add_text(attacker.nickname + " got over its infatuation!")
        elif randrange(2) < 1:
            battle.add_text(attacker.nickname + " is immobilized by love!")
            return True
    if attacker.v_status[gs.CONFUSED]:
        attacker.v_status[gs.CONFUSED] -= 1
        if attacker.v_status[gs.CONFUSED]:
            battle.add_text(attacker.nickname + " is confused!")
            if randrange(2) < 1:
                battle.add_text("It hurt itself in its confusion!")
                self_attack = Move(
                    [0, "self-attack", 1, "typeless", 40, 1, 999, 0, 10, 2, 1, "", "", ""]
                )
                _calculate_damage(
                    attacker, attacker, battlefield, battle, self_attack, crit_chance=0
                )
                return True
        else:
            battle.add_text(attacker.nickname + " snapped out of its confusion!")
    return False

from __future__ import annotations
from random import randrange

from poke_battle_sim.poke_sim import PokeSim
from poke_battle_sim.core.move import Move
from poke_battle_sim.const.ability_enum import Ability

import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf

import poke_battle_sim.conf.global_settings as gs
import poke_battle_sim.conf.global_data as gd
from poke_battle_sim.util.move_logic._calculate_type_ef import _calculate_type_ef
from poke_battle_sim.util.move_logic.burn import burn
from poke_battle_sim.util.move_logic.cure_nv_status import cure_nv_status
from poke_battle_sim.util.move_logic.give_nv_status import give_nv_status
from poke_battle_sim.util.move_logic.give_stat_change import give_stat_change
from poke_battle_sim.util.move_logic.infatuate import infatuate
from poke_battle_sim.util.move_logic.paralyze import paralyze
from poke_battle_sim.util.move_logic.poison import poison


def selection_abilities(
    poke: pk.Pokemon, battlefield: bf.Battlefield, battle: bt.Battle
):
    if poke.has_ability(Ability.DRIZZLE) and battlefield.weather != gs.RAIN:
        battlefield.change_weather(gs.RAIN)
        battlefield.weather_count = 999
        battle.add_text("It started to rain!")
    elif poke.has_ability(Ability.DROUGHT) and battlefield.weather != gs.HARSH_SUNLIGHT:
        battlefield.change_weather(gs.HARSH_SUNLIGHT)
        battlefield.weather_count = 999
        battle.add_text("The sunlight turned harsh!")
    elif poke.has_ability(Ability.SNOW_WARNING) and battlefield.weather != gs.HAIL:
        battlefield.change_weather(gs.HAIL)
        battlefield.weather_count = 999
        battle.add_text("It started to hail!")
    elif poke.has_ability(Ability.SAND_STREAM) and battlefield.weather != gs.SANDSTORM:
        battlefield.change_weather(gs.SANDSTORM)
        battlefield.weather_count = 999
        battle.add_text("A sandstorm brewed")
    elif poke.has_ability(Ability.WATER_VEIL) and poke.nv_status == gs.BURNED:
        cure_nv_status(gs.BURNED, poke, battle)
    elif poke.has_ability(Ability.MAGMA_ARMOR) and poke.nv_status == gs.FROZEN:
        cure_nv_status(gs.FROZEN, poke, battle)
    elif poke.has_ability(Ability.LIMBER) and poke.nv_status == gs.PARALYZED:
        cure_nv_status(gs.PARALYZED, poke, battle)
    elif poke.has_ability(Ability.INSOMNIA) and poke.nv_status == gs.ASLEEP:
        cure_nv_status(gs.ASLEEP, poke, battle)
    elif poke.has_ability(Ability.IMMUNITY):
        if poke.nv_status == gs.POISONED or poke.nv_status == gs.BADLY_POISONED:
            cure_nv_status(gs.POISONED, poke, battle)
    elif (
        poke.has_ability(Ability.CLOUD_NINE) or poke.has_ability(Ability.AIR_LOCK)
    ) and battlefield.weather != gs.CLEAR:
        battle.add_text("The effects of weather disappeared.")
        battlefield.change_weather(gs.CLEAR)
    elif poke.has_ability(Ability.OWN_TEMPO) and poke.v_status[gs.CONFUSED]:
        battle.add_text(f"{poke.nickname} snapped out of its confusion!")
        poke.v_status[gs.CONFUSED] = 0
    elif (
        poke.has_ability(Ability.TRACE)
        and poke.enemy.current_poke.is_alive
        and poke.enemy.current_poke.ability
        and not poke.enemy.current_poke.has_ability(Ability.TRACE)
    ):
        battle.add_text(
            f"{poke.nickname} copied {poke.enemy.current_poke.nickname}'s {str(poke.enemy.current_poke.ability)}!"
        )
        poke.give_ability(poke.enemy.current_poke.ability)
    elif poke.has_ability(Ability.FORECAST):
        _forecast_check(poke, battle, battlefield)
    elif (
        poke.has_ability(Ability.DOWNLOAD)
        and not poke.ability_activated
        and poke.enemy.current_poke.is_alive
    ):
        poke.enemy.current_poke.calculate_stats_effective()
        if (
            poke.enemy.current_poke.stats_effective[gs.DEF]
            < poke.enemy.current_poke.stats_effective[gs.SP_DEF]
        ):
            give_stat_change(poke, battle, gs.ATK, 1)
        else:
            give_stat_change(poke, battle, gs.SP_ATK, 1)
        poke.ability_activated = True
    elif poke.has_ability(Ability.ANTICIPATION) and poke.enemy.current_poke.is_alive:
        if any(
            [
                _calculate_type_ef(poke, move) > 1 or move.id in [20, 55, 62]
                for move in poke.enemy.current_poke.moves
            ]
        ):
            battle.add_text(f"{poke.nickname} shuddered!")
    elif poke.has_ability(Ability.FOREWARN) and poke.enemy.current_poke.is_alive:
        alert = _rand_max_power(poke.enemy.current_poke)
        battle.add_text(f"{poke.nickname}'s Forewarn alerted it to {alert.name}")
    elif (
        poke.has_ability(Ability.FRISK)
        and poke.enemy.current_poke.ability
        and poke.enemy.current_poke.item
    ):
        battle.add_text(
            poke.nickname
            + " frisked "
            + poke.enemy.current_poke.nickname
            + " and found its "
            + poke.enemy.current_poke.item
            + "!"
        )
    elif poke.has_ability(Ability.MULTITYPE) and poke.item in gd.PLATE_DATA:
        poke.types = (gd.PLATE_DATA[poke.item], None)
        battle.add_text(
            f"{poke.nickname} transformed into the {poke.types[0].value.upper()} type!"
        )


def enemy_selection_abilities(
    enemy_poke: pk.Pokemon, battlefield: bf.Battlefield, battle: bt.Battle
):
    poke = enemy_poke.enemy.current_poke
    if not poke.is_alive:
        return
    if poke.has_ability(Ability.INTIMIDATE):
        give_stat_change(enemy_poke, battle, gs.ATK, -1, forced=True)
    elif poke.has_ability(Ability.TRACE) and enemy_poke.ability:
        battle.add_text(
            f"{poke.nickname} copied {enemy_poke.nickname}'s {str(enemy_poke.ability)}!"
        )
        poke.give_ability(enemy_poke.ability)
    elif poke.has_ability(Ability.DOWNLOAD) and not poke.ability_activated:
        enemy_poke.calculate_stats_effective()
        if enemy_poke.stats_effective[gs.DEF] < enemy_poke.stats_effective[gs.SP_DEF]:
            give_stat_change(poke, battle, gs.ATK, 1)
        else:
            give_stat_change(poke, battle, gs.SP_ATK, 1)
        poke.ability_activated = True
    elif poke.has_ability(Ability.ANTICIPATION) and poke.enemy.current_poke.is_alive:
        if any(
            [
                _calculate_type_ef(poke, move) > 1 or move.id in [20, 55, 62]
                for move in poke.enemy.current_poke.moves
            ]
        ):
            battle.add_text(f"{poke.nickname} shuddered!")
    elif poke.has_ability(Ability.FOREWARN):
        alert = _rand_max_power(enemy_poke)
        battle.add_text(f"{poke.nickname}'s Forewarn alerted it to {alert.name}")
    elif (
        poke.has_ability(Ability.FRISK)
        and poke.enemy.current_poke.ability
        and poke.enemy.current_poke.item
    ):
        battle.add_text(
            poke.nickname
            + " frisked "
            + poke.enemy.current_poke.nickname
            + " and found its "
            + poke.enemy.current_poke.item
            + "!"
        )


def end_turn_abilities(poke: pk.Pokemon, battle: bt.Battle):
    if poke.has_ability(Ability.SPEED_BOOST):
        give_stat_change(poke, battle, gs.SPD, 1)
    elif poke.has_ability(Ability.SLOW_START):
        poke.ability_count += 1
    elif (
        poke.has_ability(Ability.BAD_DREAMS)
        and poke.enemy.current_poke.is_alive
        and poke.enemy.current_poke.nv_status == gs.ASLEEP
    ):
        battle.add_text(f"{poke.enemy.current_poke.nickname} is tormented!")
        poke.enemy.current_poke.take_damage(max(1, poke.enemy.current_poke.max_hp // 8))


def type_protection_abilities(
    defender: pk.Pokemon, move_data: Move, battle: bt.Battle
) -> bool:
    if defender.has_ability(Ability.VOLT_ABSORB) and move_data.type == "electric":
        battle.add_text(
            f"{defender.nickname} absorbed {move_data.name} with Volt Absorb!"
        )
        if not defender.cur_hp == defender.max_hp:
            defender.heal(defender.max_hp // 4)
        return True
    elif defender.has_ability(Ability.WATER_ABSORB) and move_data.type == "water":
        battle.add_text(
            f"{defender.nickname} absorbed {move_data.name} with Water Absorb!"
        )
        if not defender.cur_hp == defender.max_hp:
            defender.heal(defender.max_hp // 4)
        return True
    elif defender.has_ability(Ability.FLASH_FIRE) and move_data.type == "fire":
        battle.add_text(f"It doesn't affect {defender.nickname}")
        defender.ability_activated = True
        return True
    return False


def on_hit_abilities(
    attacker: pk.Pokemon, defender: pk.Pokemon, battle: bt.Battle, move_data: Move
) -> bool:
    made_contact = move_data.name in gd.CONTACT_CHECK
    if defender.has_ability(Ability.STATIC) and made_contact and randrange(10) < 3:
        paralyze(attacker, battle)
    elif defender.has_ability(Ability.ROUGH_SKIN) and made_contact:
        attacker.take_damage(max(1, attacker.max_hp // 16))
        battle.add_text(f"{attacker.nickname} was hurt!")
    elif (
        defender.has_ability(Ability.EFFECT_SPORE)
        and made_contact
        and randrange(10) < 3
    ):
        give_nv_status(randrange(3, 6), attacker, battle)
    elif (
        defender.has_ability(Ability.COLOR_CHANGE)
        and move_data.type not in defender.types
        and PokeSim.is_valid_type(move_data.type)
    ):
        defender.types = (move_data.type, None)
        battle.add_text(
            defender.nickname
            + " transformed into the "
            + move_data.type.value.upper()
            + " type!"
        )
    elif (
        defender.has_ability(Ability.WONDER_GUARD)
        and _calculate_type_ef(defender, move_data) < 2
    ):
        battle.add_text(f"It doesn't affect {defender.nickname}")
        return True
    elif (
        defender.has_ability(Ability.FLAME_BODY) and made_contact and randrange(10) < 3
    ):
         burn(attacker, battle)
    elif (
        defender.has_ability(Ability.POISON_POINT)
        and made_contact
        and not "steel" in attacker.types
        and not "poison" in attacker.types
        and randrange(10) < 3
    ):
        poison(attacker, battle)
    elif (
        defender.has_ability(Ability.CUTE_CHARM) and made_contact and randrange(10) < 3
    ):
        infatuate(defender, attacker, battle)
    elif defender.has_ability(Ability.MOTOR_DRIVE) and move_data.type == "electric":
        give_stat_change(defender, battle, gs.SPD, 1)
        return True
    return False


def stat_calc_abilities(poke: pk.Pokemon):
    if (
        poke.has_ability(Ability.SWIFT_SWIM)
        and poke.cur_battle.battlefield.weather == gs.RAIN
    ):
        poke.stats_effective[gs.SPD] *= 2
    elif (
        poke.has_ability(Ability.CHLOROPHYLL)
        and poke.cur_battle.battlefield.weather == gs.HARSH_SUNLIGHT
    ):
        poke.stats_effective[gs.SPD] *= 2
    elif poke.has_ability(Ability.HUGE_POWER) or poke.has_ability(Ability.PURE_POWER):
        poke.stats_effective[gs.ATK] *= 2
    elif poke.has_ability(Ability.HUSTLE) or (
        poke.has_ability(Ability.GUTS) and poke.nv_status
    ):
        poke.stats_effective[gs.ATK] = int(poke.stats_effective[gs.ATK] * 1.5)
    elif poke.has_ability(Ability.MARVEL_SCALE) and poke.nv_status:
        poke.stats_effective[gs.DEF] = int(poke.stats_effective[gs.DEF] * 1.5)
    elif (
        poke.has_ability(Ability.SOLAR_POWER)
        and poke.cur_battle.battlefield.weather == gs.HARSH_SUNLIGHT
    ):
        poke.stats_effective[gs.SP_ATK] = int(poke.stats_effective[gs.SP_ATK] * 1.5)
    elif poke.has_ability(Ability.QUICK_FEET) and poke.nv_status:
        poke.stats_effective[gs.SPD] = int(poke.stats_effective[gs.SPD] * 1.5)
    elif poke.has_ability(Ability.SLOW_START) and poke.ability_count < 5:
        poke.stats_effective[gs.ATK] //= 2
        poke.stats_effective[gs.SPD] //= 2
    elif (
        poke.has_ability(Ability.FLOWER_GIFT)
        and poke.cur_battle.battlefield.weather == gs.HARSH_SUNLIGHT
    ):
        poke.stats_effective[gs.ATK] = int(poke.stats_effective[gs.ATK] * 1.5)
        poke.stats_effective[gs.SP_DEF] = int(poke.stats_effective[gs.SP_DEF] * 1.5)
    elif poke.has_ability(Ability.UNBURDEN) and poke.unburden:
        poke.stats_effective[gs.SPD] *= 2


def damage_calc_abilities(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battle: bt.Battle,
    move_data: Move,
    t_mult: int,
):
    if (
        attacker.has_ability(Ability.FLASH_FIRE)
        and attacker.ability_activated
        and move_data.type == "fire"
    ):
        move_data.power = int(move_data.power * 1.5)
    elif (
        attacker.has_ability(Ability.OVERGROW)
        and move_data.type == "grass"
        and attacker.cur_hp <= attacker.max_hp // 3
    ):
        move_data.power = int(move_data.power * 1.5)
    elif (
        attacker.has_ability(Ability.BLAZE)
        and move_data.type == "fire"
        and attacker.cur_hp <= attacker.max_hp // 3
    ):
        move_data.power = int(move_data.power * 1.5)
    elif (
        attacker.has_ability(Ability.TORRENT)
        and move_data.type == "water"
        and attacker.cur_hp <= attacker.max_hp // 3
    ):
        move_data.power = int(move_data.power * 1.5)
    elif (
        attacker.has_ability(Ability.SWARM)
        and move_data.type == "bug"
        and attacker.cur_hp <= attacker.max_hp // 3
    ):
        move_data.power = int(move_data.power * 1.5)
    elif attacker.has_ability(Ability.RIVALRY):
        if attacker.gender == defender.gender and (
            attacker.gender == "male" or attacker.gender == "female"
        ):
            move_data.power = int(move_data.power * 1.25)
        elif (attacker.gender == "female" and defender.gender == "male") or (
            attacker.gender == "male" and defender.gender == "female"
        ):
            move_data.power = int(move_data.power * 0.75)
    elif attacker.has_ability(Ability.IRON_FIST) and move_data.name in gd.PUNCH_CHECK:
        move_data.power *= int(move_data.power * 1.2)
    elif attacker.has_ability(Ability.NORMALIZE):
        move_data.type = "normal"
    elif attacker.has_ability(Ability.TECHNICIAN) and move_data.power <= 60:
        move_data.power = int(move_data.power * 1.5)
    elif attacker.has_ability(Ability.TINTED_LENS) and t_mult < 1:
        move_data.power *= 2
    elif attacker.has_ability(Ability.RECKLESS) and move_data.name in gd.RECOIL_CHECK:
        move_data.power = int(move_data.power * 1.2)

    if defender.has_ability(Ability.HEATPROOF) and move_data.type == "fire":
        move_data.power //= 2
    elif (
        defender.has_ability(Ability.FILTER) or defender.has_ability(Ability.SOLID_ROCK)
    ) and t_mult > 1:
        move_data.power *= 0.75


def homc_abilities(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
) -> float:
    ability_mult = 1
    if defender.has_ability(Ability.SAND_VEIL) and battlefield.weather == gs.SANDSTORM:
        ability_mult *= 0.8
    elif defender.has_ability(Ability.SNOW_CLOAK) and battlefield.weather == gs.HAIL:
        ability_mult *= 0.8
    elif defender.has_ability(Ability.COMPOUND_EYES):
        ability_mult *= 1.3
    elif defender.has_ability(Ability.HUSTLE) and move_data.category == gs.PHYSICAL:
        ability_mult *= 0.8
    elif defender.has_ability(Ability.TANGLED_FEET) and defender.v_status[gs.CONFUSED]:
        ability_mult *= 0.5
    elif defender.has_ability(Ability.THICK_FAT) and (
        move_data.type == "fire" or move_data.type == "ice"
    ):
        ability_mult *= 0.5
    return ability_mult


def pre_move_abilities(
    attacker: pk.Pokemon, defender: pk.Pokemon, battle: bt.Battle, move_data: Move
):
    if attacker.has_ability(Ability.SERENE_GRACE) and move_data.ef_chance:
        move_data.ef_chance *= 2


def weather_change_abilities(battle: bt.Battle, battlefield: bf.Battlefield):
    _forecast_check(battle.t1.current_poke, battle, battlefield)
    _forecast_check(battle.t2.current_poke, battle, battlefield)


def _forecast_check(poke: pk.Pokemon, battle: bt.Battle, battlefield: bf.Battlefield):
    if poke.is_alive and poke.has_ability(Ability.FORECAST):
        if battlefield.weather == gs.HARSH_SUNLIGHT:
            poke.types = ("fire", None)
        elif battlefield.weather == gs.RAIN:
            poke.types = ("water", None)
        elif battlefield.weather == gs.HAIL:
            poke.types = ("ice", None)
        else:
            poke.types = ("normal", None)
        battle.add_text(
            f"{poke.nickname} transformed into the {poke.types[0].value.upper()} type!"
        )


def _rand_max_power(poke: pk.Pokemon) -> Move:
    p_max, p_moves = None, []
    for move in poke.moves:
        if not move.power and not p_max:
            p_moves.append(move)
        elif not move.power and p_max:
            continue
        elif (move.power and not p_max) or move.power > p_max:
            p_max = move.power
            p_moves = [move]
        elif move.power == p_max:
            p_moves.append(move)
    return p_moves[randrange(len(p_moves))]

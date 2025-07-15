from __future__ import annotations
from random import randrange
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.util.process_ability as pa
import poke_battle_sim.util.process_item as pi
from poke_battle_sim.const.ability_enum import Ability
import poke_battle_sim.conf.global_settings as gs
from poke_battle_sim.util.move_logic._calculate_crit import _calculate_crit
from poke_battle_sim.util.move_logic._calculate_type_ef import _calculate_type_ef
from poke_battle_sim.util.move_logic._invulnerability_check import (
    _invulnerability_check,
)
from poke_battle_sim.util.move_logic._missed import _missed
from poke_battle_sim.const.type_enum import PokemonType


def _calculate_damage(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    crit_chance: int = None,
    inv_bypass: bool = False,
    skip_fc: bool = False,
    skip_dmg: bool = False,
    skip_txt: bool = False,
) -> int:
    if battle.winner or move_data.category == gs.STATUS:
        return
    if not defender.is_alive:
        _missed(attacker, battle)
        return
    if not inv_bypass and _invulnerability_check(
        attacker, defender, battlefield, battle, move_data
    ):
        return
    if not move_data.power:
        return
    t_mult = _calculate_type_ef(defender, move_data)
    if (
        not skip_txt
        and not t_mult
        or (t_mult < 2 and defender.has_ability(Ability.WONDER_GUARD))
    ):
        battle.add_text(f"It doesn't affect {defender.nickname}")
        return
    if pa.type_protection_abilities(defender, move_data, battle):
        return

    cc = crit_chance + attacker.crit_stage if crit_chance else attacker.crit_stage
    if attacker.has_ability(Ability.SUPER_LUCK):
        cc += 1
    if attacker.item == "scope-lens" or attacker.item == "razor-claw":
        cc += 1
    elif attacker.item == "lucky-punch" and attacker.name == "chansey":
        cc += 2
    if (
        not defender.trainer.lucky_chant
        and not defender.has_ability(Ability.BATTLE_ARMOR)
        and not defender.has_ability(Ability.SHELL_ARMOR)
        and _calculate_crit(cc)
    ):
        crit_mult = 2 if not attacker.has_ability(Ability.SNIPER) else 3
        battle.add_text("A critical hit!")
    else:
        crit_mult = 1

    if not skip_txt and t_mult < 1:
        battle.add_text("It's not very effective...")
    elif not skip_txt and t_mult > 1:
        battle.add_text("It's super effective!")

    attacker.calculate_stats_effective(
        ignore_stats=defender.has_ability(Ability.UNAWARE)
    )
    defender.calculate_stats_effective(
        ignore_stats=attacker.has_ability(Ability.UNAWARE)
    )

    a_stat = gs.ATK if move_data.category == gs.PHYSICAL else gs.SP_ATK
    d_stat = gs.DEF if move_data.category == gs.PHYSICAL else gs.SP_DEF

    if crit_mult == 1:
        atk_ig = attacker.stats_effective[a_stat]
        def_ig = defender.stats_effective[d_stat]
    else:
        def_ig = min(defender.stats_actual[d_stat], defender.stats_effective[d_stat])
        atk_ig = max(attacker.stats_actual[a_stat], attacker.stats_effective[a_stat])
    ad_ratio = atk_ig / def_ig

    if attacker.nv_status == gs.BURNED and not attacker.has_ability(Ability.GUTS):
        burn = 0.5
    else:
        burn = 1
    if attacker.charged and move_data.type == PokemonType.ELECTRIC:
        move_data.power *= 2
    if move_data.type == PokemonType.ELECTRIC and (attacker.mud_sport or defender.mud_sport):
        move_data.power //= 2
    if move_data.type == PokemonType.FIRE and (attacker.water_sport or defender.water_sport):
        move_data.power //= 2
    pa.damage_calc_abilities(attacker, defender, battle, move_data, t_mult)
    pi.damage_calc_items(attacker, defender, battle, move_data)

    if (
        t_mult <= 1
        and (move_data.category == gs.PHYSICAL and defender.trainer.reflect)
        or (move_data.category == gs.SPECIAL and defender.trainer.light_screen)
    ):
        screen = 0.5
    else:
        screen = 1
    weather_mult = 1
    if battlefield.weather == gs.HARSH_SUNLIGHT:
        if move_data.type == PokemonType.FIRE:
            weather_mult = 1.5
        elif move_data.type == PokemonType.WATER:
            weather_mult = 0.5
    elif battlefield.weather == gs.RAIN:
        if move_data.type == PokemonType.FIRE:
            weather_mult = 0.5
        elif move_data.type == PokemonType.WATER:
            weather_mult = 1.5

    if move_data.type == attacker.types[0] or move_data.type == attacker.types[1]:
        stab = 1.5 if not attacker.has_ability(Ability.ADAPTABILITY) else 2
    else:
        stab = 1
    random_mult = randrange(85, 101) / 100

    berry_mult = pi.pre_hit_berries(attacker, defender, battle, move_data, t_mult)
    item_mult = pi.damage_mult_items(attacker, defender, battle, move_data, t_mult)

    damage = (
        (2 * attacker.level / 5 + 2) * move_data.power * ad_ratio
    ) / 50 * burn * screen * weather_mult + 2
    damage *= crit_mult * item_mult * random_mult * stab * t_mult * berry_mult
    damage = int(damage)
    if skip_dmg:
        return damage
    damage_done = defender.take_damage(damage, move_data)
    if not skip_fc:
        battle._faint_check()
    if (
        crit_mult > 1
        and defender.is_alive
        and defender.has_ability(Ability.ANGER_POINT)
        and defender.stat_stages[gs.ATK] < 6
    ):
        battle.add_text(f"{defender.nickname} maxed it's Attack!")
        defender.stat_stages[gs.ATK] = 6
    pi.post_damage_items(attacker, battle, damage_done)
    return damage_done

from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.const.ability_enum import Ability


def _effect_skill_swap(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if (
        defender.is_alive
        and not defender.has_ability(Ability.WONDER_GUARD)
        and not defender.has_ability(Ability.MULTITYPE)
        and not attacker.has_ability(Ability.WONDER_GUARD)
        and not attacker.has_ability(Ability.MULTITYPE)
    ):
        a_ability = attacker.ability
        attacker.give_ability(defender.ability)
        defender.give_ability(a_ability)
        battle.add_text(attacker.nickname + " swapped abilities with its target!")
    else:
        _failed(battle)

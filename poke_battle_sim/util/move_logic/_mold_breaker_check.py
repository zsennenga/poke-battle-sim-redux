from __future__ import annotations

from poke_battle_sim.const.ability_enum import Ability
import poke_battle_sim.core.pokemon as pk


def _mold_breaker_check(
    attacker: pk.Pokemon, defender: pk.Pokemon, end_turn: bool = True
) -> bool:
    if not attacker.has_ability(Ability.MOLD_BREAKER):
        return False
    if not end_turn and not defender.ability_suppressed:
        defender.ability_suppressed = True
        attacker.ability_count = 1
    elif end_turn and attacker.ability_count:
        defender.ability_suppressed = False
        attacker.ability_count = 0

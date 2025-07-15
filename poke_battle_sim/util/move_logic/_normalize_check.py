from __future__ import annotations

import poke_battle_sim.core.pokemon as pk
from poke_battle_sim.const.ability_enum import Ability
from poke_battle_sim.core.move import Move
from poke_battle_sim.const.type_enum import PokemonType


def _normalize_check(attacker: pk.Pokemon, move_data: Move):
    if attacker.has_ability(Ability.NORMALIZE):
        move_data.type = PokemonType.NORMAL

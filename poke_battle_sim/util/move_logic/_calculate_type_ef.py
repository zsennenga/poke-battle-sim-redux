from __future__ import annotations
from poke_battle_sim.core.move import Move
from poke_battle_sim.const.ability_enum import Ability
from poke_battle_sim.const.type_enum import PokemonType
from poke_battle_sim.core.pokemon import Pokemon
from poke_battle_sim.poke_sim import PokeSim


def _calculate_type_ef(defender: Pokemon, move_data: Move) -> float:
    if move_data.type == "typeless":
        return 1
    if (
        move_data.type == PokemonType.GROUND
        and not defender.grounded
        and (defender.magnet_rise or defender.has_ability(Ability.LEVITATE))
    ):
        return 0

    vulnerable_types = []
    if (
        move_data.type == PokemonType.GROUND
        and PokemonType.FLYING in defender.types
        and defender.grounded
    ):
        vulnerable_types.append(PokemonType.FLYING)
    if (
        (
            defender.foresight_target
            or defender.enemy.current_poke.has_ability(Ability.SCRAPPY)
        )
        and move_data.type in (PokemonType.NORMAL, PokemonType.FIGHTING)
        and PokemonType.GHOST in defender.types
    ):
        vulnerable_types.append(PokemonType.GHOST)
    if (
        defender.me_target
        and move_data.type == PokemonType.PSYCHIC
        and PokemonType.DARK in defender.types
    ):
        vulnerable_types.append(PokemonType.DARK)

    if defender.types[0] in vulnerable_types:
        t_mult = 1
    else:
        t_mult = PokeSim.get_type_ef(move_data.type, defender.types[0])
    if defender.types[1]:
        if defender.types[1] not in vulnerable_types:
            t_mult *= PokeSim.get_type_ef(move_data.type, defender.types[1])
    return t_mult

from __future__ import annotations
from poke_battle_sim.poke_sim import PokeSim
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
from poke_battle_sim.const.ability_enum import Ability


def _calculate_type_ef(defender: pk.Pokemon, move_data: Move) -> float:
    if move_data.type == "typeless":
        return 1
    if (
        move_data.type == "ground"
        and not defender.grounded
        and (defender.magnet_rise or defender.has_ability(Ability.LEVITATE))
    ):
        return 0

    vulnerable_types = []
    if move_data.type == "ground" and "flying" in defender.types and defender.grounded:
        vulnerable_types.append("flying")
    if (
        (
            defender.foresight_target
            or defender.enemy.current_poke.has_ability(Ability.SCRAPPY)
        )
        and move_data.type in ("normal", "fighting")
        and "ghost" in defender.types
    ):
        vulnerable_types.append("ghost")
    if defender.me_target and move_data.type == "psychic" and "dark" in defender.types:
        vulnerable_types.append("dark")

    if defender.types[0] in vulnerable_types:
        t_mult = 1
    else:
        t_mult = PokeSim.get_type_ef(move_data.type, defender.types[0])
    if defender.types[1]:
        if defender.types[1] not in vulnerable_types:
            t_mult *= PokeSim.get_type_ef(move_data.type, defender.types[1])
    return t_mult

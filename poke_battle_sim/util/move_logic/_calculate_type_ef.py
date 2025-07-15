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

def _calculate_type_ef(defender: pk.Pokemon, move_data: Move) -> float:
    if move_data.type == "typeless":
        return 1
    if (
        move_data.type == "ground"
        and not defender.grounded
        and (defender.magnet_rise or defender.has_ability("levitate"))
    ):
        return 0

    vulnerable_types = []
    if move_data.type == "ground" and "flying" in defender.types and defender.grounded:
        vulnerable_types.append("flying")
    if (
        (
            defender.foresight_target
            or defender.enemy.current_poke.has_ability("scrappy")
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

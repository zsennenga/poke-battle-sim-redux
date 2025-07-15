from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs
from poke_battle_sim.const.type_enum import PokemonType


def _effect_weather_ball(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if battlefield.weather == gs.HARSH_SUNLIGHT:
        move_data.type = PokemonType.FIRE
    elif battlefield.weather == gs.RAIN:
        move_data.type = PokemonType.WATER
    elif battlefield.weather == gs.HAIL:
        move_data.type = PokemonType.ICE
    elif battlefield.weather == gs.SANDSTORM:
        move_data.type = PokemonType.ROCK
    else:
        move_data.type = PokemonType.NORMAL
    if battlefield.weather != gs.CLEAR:
        move_data.power *= 2

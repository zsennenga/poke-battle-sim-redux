from __future__ import annotations

from poke_battle_sim.const.ability_enum import Ability
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs
import poke_battle_sim.conf.global_data as gd


def _effect_natural_gift(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if (
        attacker.item
        and attacker.item in gd.BERRY_DATA
        and not battlefield.weather in [gs.HARSH_SUNLIGHT, gs.RAIN]
        and not attacker.has_ability(Ability.KLUTZ)
        and not attacker.embargo_count
    ):
        move_data.type, move_data.power = gd.BERRY_DATA[attacker.item]
        attacker.give_item(None)
    else:
        _failed(battle)
        return True

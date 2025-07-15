from __future__ import annotations

from random import randrange

import poke_battle_sim.conf.global_data as gd
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.util.process_item as pi
from poke_battle_sim.const.ability_enum import Ability
from poke_battle_sim.core.move import Move
from poke_battle_sim.util.move_logic._calculate_damage import _calculate_damage


def _effect_pluck(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    dmg = _calculate_damage(attacker, defender, battlefield, battle, move_data)
    if (
        defender.is_alive
        and dmg
        and defender.item
        and defender.item in gd.BERRY_DATA
        and not defender.has_ability(Ability.STICKY_HOLD)
        and not defender.substitute
    ):
        battle.add_text(
            attacker.nickname
            + " stole and ate "
            + defender.nickname
            + "'s "
            + defender.item
            + "!"
        )
        if not attacker.has_ability(Ability.KLUTZ) and not attacker.embargo_count:
            pi.use_item(
                attacker.trainer,
                battle,
                defender.item,
                attacker,
                randrange(len(attacker.moves)),
                text_skip=True,
                can_skip=True,
            )
        defender.give_item(None)
    return True

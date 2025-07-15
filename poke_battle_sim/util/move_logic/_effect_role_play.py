from __future__ import annotations

import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.core.pokemon as pk
from poke_battle_sim.const.ability_enum import Ability
from poke_battle_sim.core.move import Move
from poke_battle_sim.util.move_logic._failed import _failed


def _effect_role_play(attacker: pk.Pokemon, defender: pk.Pokemon,
                      battlefield: bf.Battlefield, battle: bt.Battle, move_data: Move,
                      is_first: bool, cc_ib: list) -> bool:
    if defender.is_alive and defender.ability and not defender.has_ability(
            Ability.WONDER_GUARD) and not defender.has_ability(Ability.MULTITYPE):
        attacker.give_ability(defender.ability)
        battle.add_text(attacker.nickname + ' copied ' + defender.nickname +
                        "'s " + defender.ability + "'!")
    else:
        _failed(battle)

from __future__ import annotations

import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.core.pokemon as pk
from poke_battle_sim.const.ability_enum import Ability
from poke_battle_sim.core.move import Move
from poke_battle_sim.util.move_logic._calculate_damage import _calculate_damage


def _effect_absorb(attacker: pk.Pokemon, defender: pk.Pokemon, battlefield:
bf.Battlefield, battle: bt.Battle, move_data: Move, is_first: bool,
                   cc_ib: list) -> bool:
    dmg = _calculate_damage(attacker, defender, battlefield, battle, move_data)
    if dmg:
        heal_amt = max(1, dmg // 2)
        if attacker.item == 'big-root':
            heal_amt = int(heal_amt * 1.3)
        if not defender.has_ability(Ability.LIQUID_OOZE):
            attacker.heal(heal_amt, text_skip=True)
            battle.add_text(defender.nickname + " had it's energy drained!")
        else:
            attacker.take_damage(heal_amt)
            battle.add_text(attacker.nickname + ' sucked up the liquid ooze!')
    return True

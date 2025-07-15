from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.const.ability_enum import Ability
from poke_battle_sim.util.move_logic._calculate_type_ef import _calculate_type_ef
from poke_battle_sim.util.move_logic._missed import _missed


def _effect_ohko(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if not defender.is_alive:
        _missed(attacker, battle)
    if defender.has_ability(Ability.STURDY):
        battle.add_text(defender.nickname + " endured the hit!")
        return True
    if _calculate_type_ef(defender, move_data) != 0:
        defender.take_damage(65535, move_data)
        if not defender.is_alive:
            battle.add_text("It's a one-hit KO!")
    else:
        battle.add_text("It doesn't affect " + defender.nickname)
    return True

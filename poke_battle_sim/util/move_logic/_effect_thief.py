from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.const.ability_enum import Ability
from poke_battle_sim.util.move_logic._calculate_damage import _calculate_damage
from poke_battle_sim.util.move_logic.cap_name import cap_name


def _effect_thief(
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
        defender.item
        and dmg
        and not attacker.item
        and not defender.substitute
        and not defender.has_ability(Ability.STICKY_HOLD)
        and not defender.has_ability(Ability.MULTITYPE)
    ):
        battle.add_text(
            attacker.nickname
            + " stole "
            + defender.nickname
            + "'s "
            + cap_name(defender.item)
            + "!"
        )
        attacker.give_item(defender.item)
        defender.give_item(None)
    return True

from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.const.ability_enum import Ability
from poke_battle_sim.util.move_logic._failed import _failed
from poke_battle_sim.util.move_logic.cap_name import cap_name


def _effect_trick(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if (
        defender.is_alive
        and not defender.substitute
        and (attacker.item or defender.item)
        and attacker.item != "griseous-orb"
        and defender.item != "griseous-orb"
        and not defender.has_ability(Ability.STICKY_HOLD)
        and not defender.has_ability(Ability.MULTITYPE)
        and not attacker.has_ability(Ability.MULTITYPE)
    ):
        a_item = attacker.item
        attacker.give_item(defender.item)
        defender.give_item(a_item)
        battle.add_text(attacker.nickname + " switched items with its target!")
        if attacker.item:
            battle.add_text(
                attacker.nickname + " obtained one " + cap_name(attacker.item) + "."
            )
        if defender.item:
            battle.add_text(
                defender.nickname + " obtained one " + cap_name(defender.item) + "."
            )
    else:
        _failed(battle)

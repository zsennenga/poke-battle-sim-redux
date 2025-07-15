from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.const.ability_enum import Ability


def _truant_check(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
) -> bool:
    if (
        attacker.has_ability(Ability.TRUANT)
        and attacker.last_move
        and attacker.last_move.name not in ["bide", "struggle"]
    ):
        battle.add_text(attacker.nickname + " is loafing around!")
        return True
    return False

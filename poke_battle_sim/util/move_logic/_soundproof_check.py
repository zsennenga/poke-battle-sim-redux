from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.const.ability_enum import Ability
import poke_battle_sim.conf.global_data as gd


def _soundproof_check(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
) -> bool:
    if (
        move_data.name in gd.SOUND_CHECK
        and defender.has_ability(Ability.SOUNDPROOF)
        and not attacker.has_ability(Ability.MOLD_BREAKER)
    ):
        battle.add_text("It doesn't affect " + defender.nickname)
        return True
    return False

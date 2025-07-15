from __future__ import annotations

import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.core.pokemon as pk
from poke_battle_sim.const.ability_enum import Ability
from poke_battle_sim.core.move import Move
from poke_battle_sim.util.move_logic._failed import _failed


def _effect_gastro_acid(
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
        and not defender.has_ability(Ability.MULTITYPE)
        and not defender.ability_suppressed
    ):
        defender.ability_suppressed = True
        battle.add_text(defender.nickname + "'s ability was suppressed!")
    else:
        _failed(battle)

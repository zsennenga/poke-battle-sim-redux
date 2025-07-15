from __future__ import annotations

import poke_battle_sim.conf.global_settings as gs
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.pokemon as pk
from poke_battle_sim.const.ability_enum import Ability


def _flinch(
    recipient: pk.Pokemon, battle: bt.Battle, is_first: bool, forced: bool = False
):
    if (
        not recipient.is_alive
        or recipient.substitute
        or recipient.has_ability(Ability.SHIELD_DUST)
    ):
        return
    if is_first and recipient.is_alive and not recipient.v_status[gs.FLINCHED]:
        if not recipient.has_ability(Ability.INNER_FOCUS):
            recipient.v_status[gs.FLINCHED] = 1
        elif forced:
            battle.add_text(
                recipient.nickname + " won't flinch because of its Inner Focus!"
            )

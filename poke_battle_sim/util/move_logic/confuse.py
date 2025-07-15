from __future__ import annotations

from poke_battle_sim.const.ability_enum import Ability
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.util.process_item as pi
import poke_battle_sim.conf.global_settings as gs
from poke_battle_sim.util.move_logic._failed import _failed
from poke_battle_sim.util.move_logic._generate_2_to_5 import _generate_2_to_5
from poke_battle_sim.util.move_logic._safeguard_check import _safeguard_check


def confuse(
    recipient: pk.Pokemon, battle: bt.Battle, forced: bool = False, bypass: bool = False
):
    if (
        not recipient.is_alive
        or recipient.substitute
        or recipient.has_ability(Ability.OWN_TEMPO)
    ):
        if forced:
            _failed(battle)
        return
    if _safeguard_check(recipient, battle):
        return
    if not forced and not bypass and recipient.has_ability(Ability.SHIELD_DUST):
        return
    if forced and recipient.v_status[gs.CONFUSED]:
        battle.add_text(recipient.nickname + " is already confused!")
        return
    recipient.v_status[gs.CONFUSED] = _generate_2_to_5()
    battle.add_text(recipient.nickname + " became confused!")
    pi.status_items(recipient, battle)

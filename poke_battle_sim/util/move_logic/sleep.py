from __future__ import annotations

from random import randrange

import poke_battle_sim.conf.global_settings as gs
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.util.process_item as pi
from poke_battle_sim.const.ability_enum import Ability
from poke_battle_sim.util.move_logic._failed import _failed
from poke_battle_sim.util.move_logic._safeguard_check import _safeguard_check


def sleep(recipient: pk.Pokemon, battle: bt.Battle, forced: bool = False) -> None:
    if (
        not recipient.is_alive
        or recipient.substitute
        or recipient.has_ability(Ability.INSOMNIA)
        or recipient.has_ability(Ability.VITAL_SPIRIT)
        or (
            recipient.has_ability(Ability.LEAF_GUARD)
            and battle.battlefield.weather == gs.HARSH_SUNLIGHT
        )
    ):
        if forced:
            _failed(battle)
        return
    if _safeguard_check(recipient, battle):
        return
    if not forced and recipient.has_ability(Ability.SHIELD_DUST):
        return
    if forced and recipient.nv_status == gs.ASLEEP:
        battle.add_text(recipient.nickname + " is already asleep!")
    elif not recipient.nv_status:
        recipient.nv_status = gs.ASLEEP
        recipient.nv_counter = randrange(2, 6)
        battle.add_text(recipient.nickname + " fell asleep!")
        if recipient.has_ability(Ability.SYNCHRONIZE):
            sleep(recipient.enemy.current_poke, battle)
        pi.status_items(recipient, battle)

from __future__ import annotations
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.util.process_item as pi
from poke_battle_sim.const.ability_enum import Ability
import poke_battle_sim.conf.global_settings as gs
from poke_battle_sim.util.move_logic._failed import _failed
from poke_battle_sim.util.move_logic._safeguard_check import _safeguard_check


def burn(recipient: pk.Pokemon, battle: bt.Battle, forced: bool = False):
    if (
        not recipient.is_alive
        or recipient.substitute
        or recipient.has_ability(Ability.WATER_VEIL)
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
    if "fire" in recipient.types:
        if forced:
            _failed(battle)
        return
    if not forced and recipient.has_ability(Ability.SHIELD_DUST):
        return
    if forced and recipient.nv_status == gs.BURNED:
        battle.add_text(recipient.nickname + " is already burned!")
    elif not recipient.nv_status:
        recipient.nv_status = gs.BURNED
        recipient.nv_counter = 0
        battle.add_text(recipient.nickname + " was burned!")
        if recipient.has_ability(Ability.SYNCHRONIZE):
            burn(recipient.enemy.current_poke, battle)
        pi.status_items(recipient, battle)

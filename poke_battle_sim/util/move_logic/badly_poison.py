from __future__ import annotations
from random import randrange
from poke_battle_sim.poke_sim import PokeSim
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.util.process_ability as pa
import poke_battle_sim.util.process_item as pi
from poke_battle_sim.const.ability_enum import Ability
import poke_battle_sim.conf.global_settings as gs
import poke_battle_sim.conf.global_data as gd
from poke_battle_sim.util.move_logic._failed import _failed
from poke_battle_sim.util.move_logic._safeguard_check import _safeguard_check
from poke_battle_sim.util.move_logic.poison import poison


def badly_poison(recipient: pk.Pokemon, battle: bt.Battle, forced: bool = False):
    if (
        not recipient.is_alive
        or recipient.substitute
        or recipient.has_ability(Ability.IMMUNITY)
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
    if forced and recipient.nv_status == gs.BADLY_POISONED:
        battle.add_text(recipient.nickname + " is already badly poisoned!")
    elif not recipient.nv_status:
        recipient.nv_status = gs.BADLY_POISONED
        recipient.nv_counter = 1
        battle.add_text(recipient.nickname + " was badly poisoned!")
        if recipient.has_ability(Ability.SYNCHRONIZE):
            poison(recipient.enemy.current_poke, battle)
        pi.status_items(recipient, battle)

from __future__ import annotations
from random import randrange
from poke_battle_sim.poke_sim import PokeSim
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.util.process_ability as pa
import poke_battle_sim.util.process_item as pi
import poke_battle_sim.conf.global_settings as gs
import poke_battle_sim.conf.global_data as gd


def _effect_pluck(attacker: pk.Pokemon, defender: pk.Pokemon, battlefield:
    bf.Battlefield, battle: bt.Battle, move_data: Move, is_first: bool,
    cc_ib: list) ->bool:
    dmg = _calculate_damage(attacker, defender, battlefield, battle, move_data)
    if (defender.is_alive and dmg and defender.item and defender.item in gd
        .BERRY_DATA and not defender.has_ability('sticky-hold') and not
        defender.substitute):
        battle.add_text(attacker.nickname + ' stole and ate ' + defender.
            nickname + "'s " + defender.item + '!')
        if not attacker.has_ability('klutz') and not attacker.embargo_count:
            pi.use_item(attacker.trainer, battle, defender.item, attacker,
                randrange(len(attacker.moves)), text_skip=True, can_skip=True)
        defender.give_item(None)
    return True

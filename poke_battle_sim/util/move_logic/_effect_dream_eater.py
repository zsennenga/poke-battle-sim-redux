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


def _effect_dream_eater(attacker: pk.Pokemon, defender: pk.Pokemon,
    battlefield: bf.Battlefield, battle: bt.Battle, move_data: Move,
    is_first: bool, cc_ib: list) ->bool:
    if not defender.is_alive:
        _missed(attacker, battle)
    elif defender.nv_status == gs.ASLEEP:
        dmg = _calculate_damage(attacker, defender, battlefield, battle,
            move_data)
        if dmg:
            heal_amt = max(1, dmg // 2)
            if attacker.item == 'big-root':
                heal_amt = int(heal_amt * 1.3)
            attacker.heal(heal_amt)
        battle.add_text(defender.nickname + "'s dream was eaten!")
    else:
        _failed(battle)
    return True

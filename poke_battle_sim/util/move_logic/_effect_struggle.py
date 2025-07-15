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


def _effect_struggle(attacker: pk.Pokemon, defender: pk.Pokemon,
    battlefield: bf.Battlefield, battle: bt.Battle, move_data: Move,
    is_first: bool, cc_ib: list) ->bool:
    battle._pop_text()
    battle.add_text(attacker.nickname + ' has no moves left!')
    battle.add_text(attacker.nickname + ' used Struggle!')
    _calculate_damage(attacker, defender, battlefield, battle, move_data)
    struggle_dmg = max(1, attacker.max_hp // 4)
    _recoil(attacker, battle, struggle_dmg, move_data)

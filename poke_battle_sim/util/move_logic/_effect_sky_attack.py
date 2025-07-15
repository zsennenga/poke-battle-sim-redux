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


def _effect_sky_attack(attacker: pk.Pokemon, defender: pk.Pokemon,
    battlefield: bf.Battlefield, battle: bt.Battle, move_data: Move,
    is_first: bool, cc_ib: list) ->bool:
    if not move_data.ef_stat and not _power_herb_check(attacker, battle):
        move_data.ef_stat = 1
        defender.next_moves.put(move_data)
        battle._pop_text()
        battle.add_text(attacker.nickname + ' became clocked in a harsh light!'
            )
    else:
        dmg = _calculate_damage(attacker, defender, battlefield, battle,
            move_data, crit_chance=1)
        if dmg and randrange(10) < 3:
            _flinch(defender, battle, is_first)
    return True

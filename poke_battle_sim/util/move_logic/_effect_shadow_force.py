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


def _effect_shadow_force(attacker: pk.Pokemon, defender: pk.Pokemon,
    battlefield: bf.Battlefield, battle: bt.Battle, move_data: Move,
    is_first: bool, cc_ib: list) ->bool:
    if not move_data.ef_stat and not _power_herb_check(attacker, battle):
        move_data.ef_stat = 1
        attacker.next_moves.put(move_data)
        attacker.invulnerable = True
        attacker.inv_count = 1
        battle.add_text(attacker.nickname + ' vanished instantly!')
    attacker.invulnerable = False

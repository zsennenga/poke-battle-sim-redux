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

def _ef_052(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if not move_data.ef_stat:
        attacker.trapped = True
        move_data.ef_stat = 1
        attacker.bide_count = 2 if is_first else 3
        attacker.next_moves.put(move_data)
        attacker.bide_dmg = 0
        battle.add_text(attacker.nickname + " is storing energy!")
    else:
        battle._pop_text()
        battle.add_text(attacker.nickname + " unleashed energy!")
        if defender.is_alive:
            defender.take_damage(2 * attacker.bide_dmg, move_data)
        else:
            _missed(attacker, battle)
        attacker.bide_dmg = 0
    return True

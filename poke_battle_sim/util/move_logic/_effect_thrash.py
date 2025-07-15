from __future__ import annotations
from random import randrange
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._calculate_damage import _calculate_damage
from poke_battle_sim.util.move_logic.confuse import confuse


def _effect_thrash(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if not move_data.ef_stat:
        num_turns = randrange(1, 3)
        move_data.ef_stat = num_turns
        attacker.next_moves.put(move_data)
    else:
        move_data.ef_stat -= 1
        if move_data.ef_stat == 0:
            dmg = _calculate_damage(attacker, defender, battlefield, battle, move_data)
            if dmg:
                confuse(attacker, battle, bypass=True)
            return True
        else:
            attacker.next_moves.put(move_data)

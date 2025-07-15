from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._missed import _missed


def _effect_bide(
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

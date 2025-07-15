from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_dive(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if not move_data.ef_stat and not _power_herb_check(attacker, battle):
        move_data.ef_stat = 1
        attacker.next_moves.put(move_data)
        attacker.in_water = True
        attacker.invulnerable = True
        attacker.inv_count = 1
        battle._pop_text()
        battle.add_text(attacker.nickname + " hid underwater!")
        return True

from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._calculate_damage import _calculate_damage
from poke_battle_sim.util.move_logic._missed import _missed


def _effect_triple_kick(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if not defender.is_alive:
        _missed(attacker, battle)
    num_hits = 0
    while num_hits < 3 and defender.is_alive:
        _calculate_damage(
            attacker, defender, battlefield, battle, move_data, skip_fc=True
        )
        move_data.power += 10
        num_hits += 1
    battle.add_text("Hit" + str(num_hits) + "time(s)!")
    return True

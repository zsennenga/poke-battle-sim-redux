from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._calculate_damage import _calculate_damage
from poke_battle_sim.util.move_logic._failed import _failed
from poke_battle_sim.util.move_logic._flinch import _flinch


def _effect_guaranteed_flinch(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if attacker.has_moved:
        _failed(battle)
        return True
    dmg = _calculate_damage(attacker, defender, battlefield, battle, move_data)
    if defender.is_alive and dmg:
        _flinch(defender, battle, is_first, forced=True)
    return True

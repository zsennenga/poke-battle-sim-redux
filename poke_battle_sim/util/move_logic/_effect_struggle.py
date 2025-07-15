from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._calculate_damage import _calculate_damage
from poke_battle_sim.util.move_logic._recoil import _recoil


def _effect_struggle(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    battle._pop_text()
    battle.add_text(f"{attacker.nickname} has no moves left!")
    battle.add_text(f"{attacker.nickname} used Struggle!")
    _calculate_damage(attacker, defender, battlefield, battle, move_data)
    struggle_dmg = max(1, attacker.max_hp // 4)
    _recoil(attacker, battle, struggle_dmg, move_data)

from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._calculate_damage import _calculate_damage
from poke_battle_sim.util.move_logic._calculate_type_ef import _calculate_type_ef


def _effect_jump_kick(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if not defender.is_alive:
        return True
    dmg = _calculate_damage(attacker, defender, battlefield, battle, move_data)
    if dmg:
        dmg //= 2
    elif dmg == 0 and attacker.enemy and _calculate_type_ef(defender, move_data) == 0:
        dmg = defender.max_hp // 2
    if not dmg:
        return True
    battle.add_text(attacker.nickname + " kept going and crashed!")
    attacker.take_damage(dmg)
    return True

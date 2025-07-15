from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_super_fang(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if not defender.is_alive or _calculate_type_ef(defender, move_data) == 0:
        _failed(battle)
        return True
    else:
        dmg = defender.max_hp // 2
        defender.take_damage(dmg if dmg > 0 else 1, move_data)
    return True

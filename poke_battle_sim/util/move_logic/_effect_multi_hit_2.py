from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._calculate_damage import _calculate_damage


def _effect_multi_hit_2(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    dmg = _calculate_damage(
        attacker, defender, battlefield, battle, move_data, skip_fc=True
    )
    if not dmg:
        return True
    elif defender.is_alive:
        _calculate_damage(
            attacker,
            defender,
            battlefield,
            battle,
            move_data,
            skip_fc=True,
            skip_txt=True,
        )
    else:
        battle.add_text("Hit 1 time(s)!")
        return True
    battle.add_text("Hit 2 time(s)!")
    return True

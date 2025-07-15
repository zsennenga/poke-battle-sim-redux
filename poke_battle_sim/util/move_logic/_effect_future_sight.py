from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_future_sight(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    t = defender.trainer
    if defender.is_alive and not t.fs_count:
        move_data.type = "typeless"
        t.fs_dmg = _calculate_damage(
            attacker,
            defender,
            battlefield,
            battle,
            move_data,
            crit_chance=-4,
            skip_dmg=True,
        )
        t.fs_count = 3
        battle.add_text(attacker.nickname + " foresaw an attack!")
    else:
        _failed(battle)
    return True

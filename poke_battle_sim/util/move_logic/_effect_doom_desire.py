from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._calculate_damage import _calculate_damage
from poke_battle_sim.util.move_logic._failed import _failed


def _effect_doom_desire(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    t = defender.trainer
    if defender.is_alive and not t.dd_count:
        move_data.type = "typeless"
        t.dd_dmg = _calculate_damage(
            attacker,
            defender,
            battlefield,
            battle,
            move_data,
            crit_chance=0,
            skip_dmg=True,
        )
        t.dd_count = 3
        battle.add_text(f"{attacker.nickname} chose Doom Desire as its destiny!")
    else:
        _failed(battle)
    return True

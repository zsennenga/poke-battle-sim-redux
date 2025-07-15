from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._calculate_damage import _calculate_damage
from poke_battle_sim.util.move_logic._failed import _failed


def _effect_brick_break(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if defender.is_alive and not defender.invulnerable and not defender.protect:
        t = defender.trainer
        if t.light_screen or t.reflect:
            t.light_screen = 0
            t.reflect = 0
            battle.add_text("It shattered the barrier!")
        _calculate_damage(attacker, defender, battlefield, battle, move_data)
    else:
        _failed(battle)
    return True

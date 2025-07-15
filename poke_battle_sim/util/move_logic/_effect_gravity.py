from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_gravity(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if not battlefield.gravity_count:
        battlefield.gravity_count = 5
        battlefield.acc_modifier = 5 / 3
        attacker.grounded = True
        defender.grounded = True
        battle.add_text("Gravity intensified!")
    else:
        _failed(battle)

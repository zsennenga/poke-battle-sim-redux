from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_stealth_rock(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if not defender.trainer.stealth_rock:
        defender.trainer.steal_rock = 1
        battle.add_text(
            "Pointed stones float in the air around "
            + defender.trainer.name
            + "'s team!"
        )
    else:
        _failed(battle)

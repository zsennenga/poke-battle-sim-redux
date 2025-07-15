from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_lucky_chant(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if not attacker.trainer.lucky_chant:
        attacker.trainer.lucky_chant = 5
        battle.add_text(
            "The Lucky Chant shielded"
            + attacker.trainer.name
            + "'s team from critical hits!"
        )
    else:
        _failed(battle)

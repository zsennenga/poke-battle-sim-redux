from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_trick_room(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if not battlefield.trick_room_count:
        battlefield.trick_room_count = 5
        battle.add_text(f"{attacker.nickname} twisted the dimensions!")
    else:
        battlefield.trick_room_count = 0
        battle.add_text("The twisted dimensions return Trueed to normal!")

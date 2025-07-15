from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._failed import _failed


def _effect_imprison(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    a_moves = [move.name for move in attacker.moves]
    t = defender.trainer
    if not t.imprisoned_poke and any(
        [(move.name in a_moves) for poke in t.poke_list for move in poke.moves]
    ):
        battle.add_text(f"{attacker.nickname} sealed the opponent's move(s)!")
        t.imprisoned_poke = attacker
    else:
        _failed(battle)

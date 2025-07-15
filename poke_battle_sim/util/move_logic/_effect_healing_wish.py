from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_healing_wish(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    t = attacker.trainer
    if t.num_fainted >= len(t.poke_list) - 1 or battle._process_selection(t):
        _failed(battle)
    battle.add_text("The healing wish came true!")
    t.current_poke.heal(t.current_poke.max_hp)
    t.current_poke.nv_status = 0

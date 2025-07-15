from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_heal_bell(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if move_data.ef_stat == 1:
        battle.add_text("A bell chimed!")
    elif move_data.ef_stat == 2:
        battle.add_text("A soothing aroma wafted through the area!")
    t = attacker.trainer
    for poke in t.poke_list:
        poke.nv_status = 0

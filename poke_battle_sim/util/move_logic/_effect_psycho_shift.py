from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._failed import _failed
from poke_battle_sim.util.move_logic.give_nv_status import give_nv_status


def _effect_psycho_shift(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if attacker.nv_status:
        give_nv_status(attacker.nv_status, defender, battle)
        attacker.nv_status = 0
    else:
        _failed(battle)

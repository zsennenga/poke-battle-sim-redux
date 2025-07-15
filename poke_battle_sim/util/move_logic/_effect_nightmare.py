from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs
from poke_battle_sim.util.move_logic._failed import _failed


def _effect_nightmare(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if (
        defender.is_alive
        and defender.nv_status == gs.ASLEEP
        and not defender.substitute
    ):
        defender.v_status[gs.NIGHTMARE] = 1
        battle.add_text(defender.nickname + " began having a nightmare!")
    else:
        _failed(battle)

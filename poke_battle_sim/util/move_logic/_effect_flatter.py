from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs


def _effect_flatter(
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
        and not defender.substitute
        and (not defender.v_status[gs.CONFUSED] or defender.stat_stages[gs.SP_ATK] < 6)
    ):
        give_stat_change(defender, battle, gs.SP_ATK, 1)
        confuse(defender, battle)
    else:
        _failed(battle)

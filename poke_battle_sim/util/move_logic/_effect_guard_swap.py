from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs


def _effect_guard_swap(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if defender.is_alive:
        attacker.stat_stages[gs.DEF], defender.stat_stages[gs.DEF] = (
            defender.stat_stages[gs.DEF],
            attacker.stat_stages[gs.DEF],
        )
        attacker.stat_stages[gs.SP_DEF], defender.stat_stages[gs.SP_DEF] = (
            defender.stat_stages[gs.SP_DEF],
            attacker.stat_stages[gs.SP_DEF],
        )
        battle.add_text(
            attacker.nickname
            + " switched all changes to its Defense and Sp. Def with "
            + defender.nickname
            + "!"
        )
    else:
        _failed(battle)

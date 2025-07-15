from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic.give_stat_change import give_stat_change


def _effect_defender_stat_stage_change(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if defender.is_alive and defender.trainer.mist:
        battle.add_text(defender.nickname + "'s protected by mist.")
        return True
    give_stat_change(defender, battle, move_data.ef_stat, move_data.ef_amount)

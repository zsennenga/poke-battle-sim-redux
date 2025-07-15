from __future__ import annotations
from random import randrange
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_acupressure(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    ef_stats = attacker.stat_stages + [attacker.accuracy_stage, attacker.evasion_stage]
    ef_stats = [stat_i for stat_i in range(len(ef_stats)) if ef_stats[stat_i] < 6]
    if len(ef_stats):
        give_stat_change(attacker, battle, randrange(len(ef_stats)), 2)
    else:
        _failed(battle)

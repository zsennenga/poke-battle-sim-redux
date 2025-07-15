from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs


def _effect_gyro_ball(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    attacker.calculate_stats_effective()
    defender.calculate_stats_effective()
    move_data.power = min(
        150,
        attacker.stats_effective[gs.SPD] * 25 / max(1, defender.stats_effective[gs.SPD])
        + 1,
    )

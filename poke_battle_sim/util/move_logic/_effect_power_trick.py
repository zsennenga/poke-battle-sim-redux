from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs


def _effect_power_trick(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    attacker.stats_actual[gs.ATK], attacker.stats_actual[gs.DEF] = (
        attacker.stats_actual[gs.DEF],
        attacker.stats_actual[gs.ATK],
    )
    battle.add_text(attacker.nickname + " switched its Attack and Defense!")
    attacker.power_trick = True

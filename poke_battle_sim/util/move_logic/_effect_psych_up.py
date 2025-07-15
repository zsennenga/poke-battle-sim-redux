from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._failed import _failed


def _effect_psych_up(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if defender.is_alive:
        attacker.stat_stages = [stat for stat in defender.stat_stages]
        attacker.accuracy_stage = defender.accuracy_stage
        attacker.evasion_stage = defender.evasion_stage
        attacker.crit_stage = defender.crit_stage
        battle.add_text(
            attacker.nickname + " copied " + defender.nickname + "'s stat changes!"
        )
    else:
        _failed(battle)

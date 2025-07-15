from __future__ import annotations
from random import randrange
from poke_battle_sim.poke_sim import PokeSim
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.util.process_ability as pa
import poke_battle_sim.util.process_item as pi
import poke_battle_sim.conf.global_settings as gs
import poke_battle_sim.conf.global_data as gd

def _ef_111(
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

from __future__ import annotations
from random import randrange
from poke_battle_sim.poke_sim import PokeSim
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.util.process_ability as pa
import poke_battle_sim.util.process_item as pi
from poke_battle_sim.const.ability_enum import Ability
import poke_battle_sim.conf.global_settings as gs
import poke_battle_sim.conf.global_data as gd

def _truant_check(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
) -> bool:
    if (
        attacker.has_ability(Ability.TRUANT)
        and attacker.last_move
        and attacker.last_move.name not in ["bide", "struggle"]
    ):
        battle.add_text(attacker.nickname + " is loafing around!")
        return True
    return False

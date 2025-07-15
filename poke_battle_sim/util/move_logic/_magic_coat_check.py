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

def _magic_coat_check(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
) -> bool:
    if (
        defender.is_alive
        and defender.magic_coat
        and move_data.name in gd.MAGIC_COAT_CHECK
    ):
        battle.add_text(
            attacker.nickname
            + "'s "
            + move_data.name
            + " was bounced back by Magic Coat!"
        )
        _process_effect(defender, attacker, battlefield, battle, move_data, is_first)
        return True
    return False

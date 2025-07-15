from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_data as gd
from poke_battle_sim.util.move_logic._process_effect import _process_effect


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
            f"{attacker.nickname}'s {move_data.name} was bounced back by Magic Coat!"
        )
        _process_effect(defender, attacker, battlefield, battle, move_data, is_first)
        return True
    return False

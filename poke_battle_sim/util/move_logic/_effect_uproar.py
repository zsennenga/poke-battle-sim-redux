from __future__ import annotations
from random import randrange
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._calculate_damage import _calculate_damage


def _effect_uproar(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    dmg = _calculate_damage(attacker, defender, battlefield, battle, move_data)
    if dmg and not attacker.uproar:
        attacker.uproar = randrange(1, 5)
        battle.add_text(attacker.nickname + " caused an uproar!")
    return True

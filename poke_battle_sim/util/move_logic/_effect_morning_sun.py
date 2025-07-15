from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs


def _effect_morning_sun(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if battlefield.weather == gs.CLEAR:
        heal_amount = 2
    elif battlefield.weather == gs.HARSH_SUNLIGHT:
        heal_amount = 1.5
    else:
        heal_amount = 4
    attacker.heal(int(attacker.max_hp / heal_amount))

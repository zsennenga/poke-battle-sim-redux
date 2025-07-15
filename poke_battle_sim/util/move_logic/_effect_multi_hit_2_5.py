from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.const.ability_enum import Ability
from poke_battle_sim.util.move_logic._calculate_damage import _calculate_damage
from poke_battle_sim.util.move_logic._generate_2_to_5 import _generate_2_to_5
from poke_battle_sim.util.move_logic._missed import _missed


def _effect_multi_hit_2_5(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if not defender.is_alive:
        _missed(attacker, battle)
    if not attacker.has_ability(Ability.SKILL_LINK):
        num_hits = _generate_2_to_5()
    else:
        num_hits = 5
    nh = num_hits
    dmg = _calculate_damage(
        attacker, defender, battlefield, battle, move_data, skip_fc=True
    )
    if not dmg:
        nh = 0
    else:
        nh -= 1
    while nh and defender.is_alive:
        _calculate_damage(
            attacker,
            defender,
            battlefield,
            battle,
            move_data,
            skip_fc=True,
            skip_txt=True,
        )
        nh -= 1
    battle.add_text(f"Hit {str(num_hits)} time(s)!")
    return True

from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.const.ability_enum import Ability
import poke_battle_sim.conf.global_settings as gs
from poke_battle_sim.util.move_logic._calculate_damage import _calculate_damage
from poke_battle_sim.util.move_logic._failed import _failed


def _effect_explosion(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if not defender.is_alive:
        _failed(battle)
        return True
    if attacker.has_ability(Ability.DAMP) or defender.has_ability(Ability.DAMP):
        battle.add_text(attacker.nickname + " cannot use Explosion!")
        return True
    attacker.faint()
    old_def = defender.stats_actual[gs.DEF]
    defender.stats_actual[gs.DEF] //= 2
    _calculate_damage(attacker, defender, battlefield, battle, move_data)
    defender.stats_actual[gs.DEF] = old_def
    return True

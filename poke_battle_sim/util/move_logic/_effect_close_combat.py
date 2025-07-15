from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs
from poke_battle_sim.util.move_logic._calculate_damage import _calculate_damage
from poke_battle_sim.util.move_logic.give_stat_change import give_stat_change


def _effect_close_combat(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    dmg = _calculate_damage(attacker, defender, battlefield, battle, move_data)
    if attacker.is_alive and dmg:
        give_stat_change(attacker, battle, gs.DEF, -1, bypass=True)
        give_stat_change(attacker, battle, gs.SP_DEF, -1, bypass=True)
    return True

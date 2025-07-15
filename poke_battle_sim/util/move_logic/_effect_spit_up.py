from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs


def _effect_spit_up(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if attacker.stockpile:
        _calculate_damage(attacker, defender, battlefield, battle, move_data)
        move_data.power = 100 * attacker.stockpile
        attacker.stockpile = 0
        attacker.stat_stages[gs.DEF] -= attacker.stockpile
        attacker.stat_stages[gs.SP_DEF] -= attacker.stockpile
        battle.add_text(attacker.nickname + "'s stockpile effect wore off!")
    else:
        _failed(battle)

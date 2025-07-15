from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs
from poke_battle_sim.util.move_logic._power_herb_check import _power_herb_check
from poke_battle_sim.util.move_logic.give_stat_change import give_stat_change


def _effect_skull_bash(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if not move_data.ef_stat and not _power_herb_check(attacker, battle):
        battle._pop_text()
        battle.add_text(attacker.nickname + " tucked in its head!")
        give_stat_change(attacker, battle, gs.DEF, 1)
        move_data.ef_stat = 1
        attacker.next_moves.put(move_data)
        return True

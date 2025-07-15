from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs
from poke_battle_sim.util.move_logic._power_herb_check import _power_herb_check


def _effect_solar_beam(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if (
        not move_data.ef_stat
        and battlefield.weather != gs.HARSH_SUNLIGHT
        and not _power_herb_check(attacker, battle)
    ):
        battle._pop_text()
        battle.add_text(f"{attacker.nickname} absorbed light!")
        move_data.ef_stat = 1
        attacker.next_moves.put(move_data)
        return True
    if battlefield.weather != gs.HARSH_SUNLIGHT and battlefield.weather != gs.CLEAR:
        move_data.power //= 2

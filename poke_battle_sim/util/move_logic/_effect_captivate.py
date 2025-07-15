from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs
from poke_battle_sim.util.move_logic._failed import _failed
from poke_battle_sim.util.move_logic.give_stat_change import give_stat_change


def _effect_captivate(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if (
        defender.is_alive
        and (attacker.gender == "male" and defender.gender == "female")
        or attacker.gender == "female"
        and defender.gender == "male"
    ):
        give_stat_change(defender, battle, gs.SP_ATK, -2, forced=True)
    else:
        _failed(battle)

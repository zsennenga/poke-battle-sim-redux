from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.util.process_ability as pa
from poke_battle_sim.util.move_logic._calculate_damage import _calculate_damage


def _process_effect(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
):
    pa.pre_move_abilities(attacker, defender, battle, move_data)
    ef_id = move_data.ef_id

    crit_chance = None
    inv_bypass = False
    cc_ib = [crit_chance, inv_bypass]

    if _MOVE_EFFECTS[ef_id](
        attacker, defender, battlefield, battle, move_data, is_first, cc_ib
    ):
        _calculate_damage(
            attacker,
            defender,
            battlefield,
            battle,
            move_data,
            crit_chance=cc_ib[0],
            inv_bypass=cc_ib[1],
        )

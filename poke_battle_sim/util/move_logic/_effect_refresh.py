from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs
from poke_battle_sim.util.move_logic._failed import _failed


def _effect_refresh(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if (
        attacker.nv_status == gs.BURNED
        or attacker.nv_status == gs.PARALYZED
        or attacker.nv_status == gs.POISONED
    ):
        attacker.nv_status = 0
        battle.add_text(f"{attacker.nickname}'s status return Trueed to normal!")
    else:
        _failed(battle)

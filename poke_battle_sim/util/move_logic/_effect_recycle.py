from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._failed import _failed
from poke_battle_sim.util.move_logic.cap_name import cap_name


def _effect_recycle(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if not attacker.item and not attacker.h_item and attacker.last_consumed_item:
        attacker.give_item(attacker.last_consumed_item)
        attacker.last_consumed_item = None
        battle.add_text(
            attacker.nickname + " found one " + cap_name(attacker.item) + "!"
        )
    else:
        _failed(battle)

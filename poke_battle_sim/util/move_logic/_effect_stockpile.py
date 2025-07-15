from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs
from poke_battle_sim.util.move_logic._failed import _failed
from poke_battle_sim.util.move_logic.give_stat_change import give_stat_change


def _effect_stockpile(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if attacker.stockpile < 3:
        attacker.stockpile += 1
        battle.add_text(
            f"{attacker.nickname} stockpiled {str(attacker.stockpile)}!"
        )
        give_stat_change(attacker, battle, gs.DEF, 1)
        give_stat_change(attacker, battle, gs.SP_DEF, 1)
    else:
        _failed(battle)

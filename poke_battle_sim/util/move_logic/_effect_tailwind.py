from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs


def _effect_tailwind(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if not attacker.trainer.tailwind_count:
        battle.add_text(
            "The tailwind blew from being " + attacker.trainer.name + "'s team!"
        )
        attacker.trainer.tailwind_count = 3
        for poke in attacker.trainer.poke_list:
            poke.stats_actual[gs.SPD] *= 2
    else:
        _failed(battle)

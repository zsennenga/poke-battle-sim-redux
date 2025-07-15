from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs
from poke_battle_sim.util.move_logic._failed import _failed


def _effect_belly_drum(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if attacker.max_hp // 2 > attacker.cur_hp or attacker.stat_stages[gs.ATK] == 6:
        _failed(battle)
        return True
    battle.add_text(f"{attacker.nickname} cut its own HP and maximized its Attack!")
    attacker.stat_stages[gs.ATK] = 6

from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._failed import _failed


def _effect_substitute(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if attacker.substitute:
        _failed(battle)
        return True
    if attacker.cur_hp - attacker.max_hp // 4 < 0:
        battle.add_text("But it does not have enough HP left to make a substitute!")
        return True
    attacker.substitute = attacker.take_damage(attacker.max_hp // 4) + 1
    battle.add_text(f"{attacker.nickname} made a substitute!")

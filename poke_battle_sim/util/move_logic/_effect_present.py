from __future__ import annotations
from random import randrange
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._missed import _missed


def _effect_present(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    res = randrange(10)
    if res < 2:
        if not defender.is_alive:
            _missed(attacker, battle)
            return True
        if defender.cur_hp == defender.max_hp:
            battle.add_text(f"{defender.nickname} can't receive the gift!")
            return True
        defender.heal(defender.max_hp // 4)
        return True
    elif res < 6:
        move_data.power = 40
    elif res < 9:
        move_data.power = 80
    elif res < 10:
        move_data.power = 120

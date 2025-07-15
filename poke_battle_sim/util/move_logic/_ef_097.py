from __future__ import annotations
from random import randrange
from poke_battle_sim.poke_sim import PokeSim
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.util.process_ability as pa
import poke_battle_sim.util.process_item as pi
import poke_battle_sim.conf.global_settings as gs
import poke_battle_sim.conf.global_data as gd

def _ef_097(
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
            battle.add_text(defender.nickname + " can't receive the gift!")
            return True
        defender.heal(defender.max_hp // 4)
        return True
    elif res < 6:
        move_data.power = 40
    elif res < 9:
        move_data.power = 80
    elif res < 10:
        move_data.power = 120

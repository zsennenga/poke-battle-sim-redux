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

def _ef_044(
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
        and defender.last_move
        and not attacker.copied
        and not attacker.is_move(defender.last_move.md)
    ):
        attacker.copied = Move(defender.last_move.md)
        attacker.copied.max_pp = min(5, attacker.copied.max_pp)
        attacker.copied.cur_pp = attacker.copied.max_pp
        battle.add_text(
            attacker.nickname + " learned " + cap_name(attacker.copied.name)
        )
    else:
        _failed(battle)

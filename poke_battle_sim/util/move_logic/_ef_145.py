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

def _ef_145(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    a_moves = [move.name for move in attacker.moves]
    t = defender.trainer
    if not t.imprisoned_poke and any(
        [move.name in a_moves for poke in t.poke_list for move in poke.moves]
    ):
        battle.add_text(attacker.nickname + " sealed the opponent's move(s)!")
        t.imprisoned_poke = attacker
    else:
        _failed(battle)

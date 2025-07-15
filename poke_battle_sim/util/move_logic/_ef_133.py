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

def _ef_133(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    possible_moves = [
        move
        for poke in attacker.trainer.poke_list
        for move in poke.moves
        if move.name not in gd.ASSIST_CHECK
    ]
    if len(possible_moves):
        _process_effect(
            attacker,
            defender,
            battlefield,
            battle,
            Move(possible_moves[randrange(len(possible_moves))].md),
            is_first,
        )
    else:
        _failed(battle)
    return True

from __future__ import annotations
from random import randrange
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs


def _effect_sleep_talk(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if attacker.nv_status != gs.ASLEEP:
        _failed(battle)
        return True
    pos_moves = [move for move in attacker.moves if move.name != "sleep-talk"]
    sel_move = Move(pos_moves[randrange(len(pos_moves))].md)
    battle.add_text(attacker.nickname + " used " + cap_name(sel_move.name) + "!")
    _process_effect(attacker, defender, battlefield, battle, sel_move, is_first)
    return True

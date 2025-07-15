from __future__ import annotations
from poke_battle_sim.poke_sim import PokeSim
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs
import poke_battle_sim.conf.global_data as gd
from poke_battle_sim.util.move_logic._process_effect import _process_effect
from poke_battle_sim.util.move_logic.cap_name import cap_name


def _effect_metronome(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    move_names = [move.name for move in attacker.moves]
    rand_move = PokeSim.get_rand_move()
    attempts = 0
    while attempts < 50 and (
        rand_move[gs.MOVE_NAME] in move_names
        or rand_move[gs.MOVE_NAME] in gd.METRONOME_CHECK
    ):
        rand_move = PokeSim.get_rand_move()
        attempts += 1
    rand_move = Move(rand_move)
    battle.add_text(attacker.nickname + " used " + cap_name(rand_move.name) + "!")
    _process_effect(attacker, defender, battlefield, battle, rand_move, is_first)
    return True

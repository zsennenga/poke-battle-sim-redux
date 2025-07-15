from __future__ import annotations
from random import randrange
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.conf.global_settings as gs
import poke_battle_sim.conf.global_data as gd


def _extra_flinch_check(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
):
    if attacker.item == "king's-rock" or attacker.item == "razor-fang":
        if (
            move_data in gd.EXTRA_FLINCH_CHECK
            and not defender.v_status[gs.FLINCHED]
            and is_first
            and randrange(10) < 1
        ):
            _flinch(defender, battle, is_first)

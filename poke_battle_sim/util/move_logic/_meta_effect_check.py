from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._extra_flinch_check import _extra_flinch_check
from poke_battle_sim.util.move_logic._grounded_check import _grounded_check
from poke_battle_sim.util.move_logic._magic_coat_check import _magic_coat_check
from poke_battle_sim.util.move_logic._normalize_check import _normalize_check
from poke_battle_sim.util.move_logic._protect_check import _protect_check
from poke_battle_sim.util.move_logic._snatch_check import _snatch_check
from poke_battle_sim.util.move_logic._soundproof_check import _soundproof_check
from poke_battle_sim.util.move_logic._truant_check import _truant_check


def _meta_effect_check(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
) -> bool:
    if _magic_coat_check(attacker, defender, battlefield, battle, move_data, is_first):
        return True
    if _snatch_check(attacker, defender, battlefield, battle, move_data, is_first):
        return True
    if _protect_check(defender, battle, move_data):
        return True
    if _soundproof_check(defender, battle, move_data):
        return True
    if _grounded_check(attacker, battle, move_data):
        return True
    if _truant_check(attacker, battle, move_data):
        return True
    _normalize_check(attacker, move_data)
    _extra_flinch_check(attacker, defender, battle, move_data, is_first)
    return False

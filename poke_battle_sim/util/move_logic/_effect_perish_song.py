from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf


def _effect_perish_song(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if not attacker.perish_count:
        attacker.perish_count = 4
    if defender.is_alive and not defender.perish_count:
        defender.perish_count = 4
    battle.add_text("All pokemon hearing the song will faint in three turns!")

from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs


def _effect_hail(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if battlefield.weather != gs.HAIL:
        battlefield.change_weather(gs.HAIL)
        battlefield.weather_count = 5 if attacker.item != "icy-rock" else 8
        battle.add_text("It started to hail!")
    else:
        _failed(battle)

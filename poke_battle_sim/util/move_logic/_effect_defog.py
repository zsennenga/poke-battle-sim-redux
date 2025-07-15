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


def _effect_defog(attacker: pk.Pokemon, defender: pk.Pokemon, battlefield:
    bf.Battlefield, battle: bt.Battle, move_data: Move, is_first: bool,
    cc_ib: list) ->bool:
    if defender.is_alive:
        battle.add_text(_stat_text(defender, gs.EVA, -1))
        if defender.evasion_stage > -6:
            defender.evasion_stage -= 1
    defender.trainer.spikes = 0
    defender.trainer.toxic_spikes = 0
    defender.stealth_rock = 0
    defender.trainer.safeguard = 0
    defender.trainer.light_screen = 0
    defender.trainer.reflect = 0
    defender.trainer.mist = 0

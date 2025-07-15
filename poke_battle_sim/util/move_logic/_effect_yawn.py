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


def _effect_yawn(attacker: pk.Pokemon, defender: pk.Pokemon, battlefield:
    bf.Battlefield, battle: bt.Battle, move_data: Move, is_first: bool,
    cc_ib: list) ->bool:
    if (defender.is_alive and not defender.v_status[gs.DROWSY] and not
        defender.substitute and not defender.nv_status == gs.FROZEN and not
        defender.nv_status == gs.ASLEEP and not defender.has_ability(
        'insomnia') and not defender.has_ability('vital-spirit') and not
        defender.trainer.safeguard and not (defender.has_ability(
        'leaf-guard') and battlefield.weather == gs.HARSH_SUNLIGHT) and not
        (defender.uproar and not defender.has_ability('soundproof'))):
        defender.v_status[gs.DROWSY] = 2
        battle.add_text(attacker.nickname + ' made ' + defender.nickname +
            ' drowsy!')
    else:
        _failed(battle)

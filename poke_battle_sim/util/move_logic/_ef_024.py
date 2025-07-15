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

def _ef_024(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    dmg = _calculate_damage(attacker, defender, battlefield, battle, move_data)
    if (
        defender.is_alive
        and dmg
        and not defender.substitute
        and not defender.v_status[gs.BINDING_COUNT]
    ):
        defender.v_status[gs.BINDING_COUNT] = (
            _generate_2_to_5() if attacker.item != "grip-claw" else 5
        )
        defender.binding_poke = attacker
        if move_data.ef_stat == gs.BIND:
            defender.binding_type = "Bind"
            battle.add_text(
                defender.nickname + " was squeezed by " + attacker.nickname + "!"
            )
        elif move_data.ef_stat == gs.WRAP:
            defender.binding_type = "Wrap"
            battle.add_text(
                defender.nickname + " was wrapped by " + attacker.nickname + "!"
            )
        elif move_data.ef_stat == gs.FIRE_SPIN:
            defender.binding_type = "Fire Spin"
            battle.add_text(defender.nickname + " was trapped in the vortex!")
        elif move_data.ef_stat == gs.CLAMP:
            defender.binding_type = "Clamp"
            battle.add_text(attacker.nickname + " clamped " + defender.nickname + "!")
        elif move_data.ef_stat == gs.WHIRLPOOL:
            defender.binding_type = "Whirlpool"
            battle.add_text(defender.nickname + " was trapped in the vortex!")
        elif move_data.ef_stat == gs.SAND_TOMB:
            defender.binding_type = "Sand Tomb"
            battle.add_text(defender.nickname + " was trapped by Sand Tomb!")
        elif move_data.ef_stat == gs.MAGMA_STORM:
            defender.binding_type = "Magma Storm"
            battle.add_text(defender.nickname + " became trapped by swirling magma!")
    return True

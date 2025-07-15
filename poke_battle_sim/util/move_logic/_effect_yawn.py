from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.const.ability_enum import Ability
import poke_battle_sim.conf.global_settings as gs
from poke_battle_sim.util.move_logic._failed import _failed


def _effect_yawn(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if (
        defender.is_alive
        and not defender.v_status[gs.DROWSY]
        and not defender.substitute
        and not defender.nv_status == gs.FROZEN
        and not defender.nv_status == gs.ASLEEP
        and not defender.has_ability(Ability.INSOMNIA)
        and not defender.has_ability(Ability.VITAL_SPIRIT)
        and not defender.trainer.safeguard
        and not (
            defender.has_ability(Ability.LEAF_GUARD)
            and battlefield.weather == gs.HARSH_SUNLIGHT
        )
        and not (defender.uproar and not defender.has_ability(Ability.SOUNDPROOF))
    ):
        defender.v_status[gs.DROWSY] = 2
        battle.add_text(attacker.nickname + " made " + defender.nickname + " drowsy!")
    else:
        _failed(battle)

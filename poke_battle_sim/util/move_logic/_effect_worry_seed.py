from __future__ import annotations

from poke_battle_sim.const.ability_enum import Ability
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
from poke_battle_sim.util.move_logic._failed import _failed


def _effect_worry_seed(
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
        and not defender.has_ability(Ability.MULTITYPE)
        and not defender.has_ability(Ability.TRUANT)
    ):
        battle.add_text(defender.nickname + " acquired insomnia!")
        defender.give_ability(Ability.INSOMNIA)
    else:
        _failed(battle)

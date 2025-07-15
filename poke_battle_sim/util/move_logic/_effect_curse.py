from __future__ import annotations
from poke_battle_sim.core.move import Move
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.core.battlefield as bf
import poke_battle_sim.conf.global_settings as gs
from poke_battle_sim.util.move_logic._failed import _failed
from poke_battle_sim.util.move_logic.give_stat_change import give_stat_change
from poke_battle_sim.const.type_enum import PokemonType


def _effect_curse(
    attacker: pk.Pokemon,
    defender: pk.Pokemon,
    battlefield: bf.Battlefield,
    battle: bt.Battle,
    move_data: Move,
    is_first: bool,
    cc_ib: list,
) -> bool:
    if PokemonType.GHOST not in attacker.types:
        if (
            attacker.stat_stages[gs.ATK] == 6
            and attacker.stat_stages[gs.DEF] == 6
            and attacker.stat_stages[gs.SPD] == -6
        ):
            _failed(battle)
            return True
        if attacker.stat_stages[gs.ATK] < 6:
            give_stat_change(attacker, battle, gs.ATK, 1)
        if attacker.stat_stages[gs.DEF] < 6:
            give_stat_change(attacker, battle, gs.DEF, 1)
        if attacker.stat_stages[gs.SPD] > -6:
            give_stat_change(attacker, battle, gs.SPD, -1, bypass=True)
    else:
        if not defender.is_alive or defender.v_status[gs.CURSE] or defender.substitute:
            _failed(battle)
            return True
        attacker.take_damage(attacker.max_hp // 2)
        defender.v_status[gs.CURSE] = 1
        battle.add_text(
            f"{attacker.nickname} cut its own HP and laid a curse on {defender.nickname}!"
        )

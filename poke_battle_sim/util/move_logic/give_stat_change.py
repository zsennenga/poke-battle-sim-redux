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

def give_stat_change(
    recipient: pk.Pokemon,
    battle: bt.Battle,
    stat: int,
    amount: int,
    forced: bool = False,
    bypass: bool = False,
):
    if not recipient.is_alive:
        if forced:
            _failed(battle)
        return
    if (
        amount < 0
        and not bypass
        and (
            recipient.substitute
            or recipient.has_ability("clear-body")
            or recipient.has_ability("white-smoke")
        )
    ):
        if forced:
            _failed(battle)
        return
    if (
        amount < 0
        and not forced
        and not bypass
        and recipient.has_ability("shield-dust")
    ):
        return
    if recipient.has_ability("simple"):
        amount *= 2
    if stat == 6:
        r_stat = recipient.accuracy_stage
        if amount < 0 and recipient.has_ability("keen-eye"):
            if forced:
                _failed(battle)
            return
        recipient.accuracy_stage = _fit_stat_bounds(recipient.accuracy_stage + amount)
    elif stat == 7:
        r_stat = recipient.evasion_stage
        recipient.evasion_stage = _fit_stat_bounds(recipient.evasion_stage + amount)
    else:
        r_stat = recipient.stat_stages[stat]
        if stat == gs.ATK and amount < 0 and recipient.has_ability("hyper-cutter"):
            if forced:
                _failed(battle)
            return
        recipient.stat_stages[stat] = _fit_stat_bounds(
            recipient.stat_stages[stat] + amount
        )
    if -6 < r_stat < 6 or forced:
        battle.add_text(_stat_text(recipient, stat, amount))
    return

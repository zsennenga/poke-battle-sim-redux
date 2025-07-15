from __future__ import annotations
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.conf.global_settings as gs


def _stat_text(recipient: pk.Pokemon, stat: int, amount: int) -> str:
    if stat == gs.ACC:
        cur_stage = recipient.accuracy_stage
    elif stat == gs.EVA:
        cur_stage = recipient.evasion_stage
    else:
        cur_stage = recipient.stat_stages[stat]
    if not amount:
        return ""
    base = recipient.get_name() + "'s " + gs.STAT_TO_NAME[stat]
    if amount > 0:
        dif = min(6 - cur_stage, amount)
        if dif <= 0:
            base += " won't go any higher!"
        elif dif == 1:
            base += " rose!"
        elif dif == 2:
            base += " rose sharply!"
        else:
            base += " rose drastically!"
    else:
        dif = max(-6 - cur_stage, amount)
        if dif >= 0:
            base += " won't go any lower!"
        elif dif == -1:
            base += " fell!"
        elif dif == -2:
            base += " fell harshly!"
        else:
            base += " fell severely!"
    return base

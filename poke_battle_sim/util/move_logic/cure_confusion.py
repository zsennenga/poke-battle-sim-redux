from __future__ import annotations
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt
import poke_battle_sim.conf.global_settings as gs


def cure_confusion(recipient: pk.Pokemon, battle: bt.Battle) -> None:
    if recipient.is_alive and recipient.v_status[gs.CONFUSED]:
        recipient.v_status[gs.CONFUSED] = 0
        battle.add_text(recipient.nickname + " snapped out of its confusion!")

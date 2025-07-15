from __future__ import annotations
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt


def cure_infatuation(recipient: pk.Pokemon, battle: bt.Battle):
    if recipient.is_alive and recipient.infatuation:
        recipient.infatuation = None
        battle.add_text(recipient.nickname + " got over its infatuation!")

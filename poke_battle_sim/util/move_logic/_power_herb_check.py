from __future__ import annotations
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt


def _power_herb_check(attacker: pk.Pokemon, battle: bt.Battle) -> bool:
    if attacker.item == "power-herb":
        battle.add_text(
            attacker.nickname + " became fully charged due to its Power Herb!"
        )
        attacker.give_item(None)
        return True
    return False

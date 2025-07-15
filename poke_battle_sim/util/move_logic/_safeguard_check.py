from __future__ import annotations
import poke_battle_sim.core.pokemon as pk
import poke_battle_sim.core.battle as bt


def _safeguard_check(poke: pk.Pokemon, battle: bt.Battle) -> bool:
    if poke.trainer and poke.trainer.safeguard:
        battle.add_text(f"{poke.nickname} is protected by Safeguard!")
        return True
    return False

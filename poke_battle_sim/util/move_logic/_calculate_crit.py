from __future__ import annotations
from random import randrange


def _calculate_crit(crit_chance: int | None = None) -> bool:
    if not crit_chance:
        return randrange(16) < 1
    elif crit_chance == 1:
        return randrange(9) < 1
    elif crit_chance == 2:
        return randrange(5) < 1
    elif crit_chance == 3:
        return randrange(4) < 1
    elif crit_chance == 4:
        return randrange(3) < 1
    else:
        return randrange(1000) < crit_chance

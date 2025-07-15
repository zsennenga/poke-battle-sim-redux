from __future__ import annotations
from random import randrange


def _generate_2_to_5() -> int:
    n = randrange(8)
    if n < 3:
        num_hits = 2
    elif n < 6:
        num_hits = 3
    elif n < 7:
        num_hits = 4
    else:
        num_hits = 5
    return num_hits

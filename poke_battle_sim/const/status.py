from enum import Enum


class NonVolatileStatus(Enum):
    BURN = 1
    FREEZE = 2
    PARALYSIS = 3
    POISON = 4
    SLEEP = 5
    BADLY_POISONED = 6


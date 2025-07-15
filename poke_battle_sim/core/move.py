from __future__ import annotations

import poke_battle_sim.conf.global_settings as gs
from pydantic import BaseModel
from typing import Optional, List

from poke_battle_sim.const.move_effects import MoveEffect
from poke_battle_sim.const.stat import Stat
from poke_battle_sim.const.type_enum import PokemonType


class Move(BaseModel):
    name: str
    type: PokemonType
    o_power: int
    power: int
    max_pp: int
    acc: int
    prio: int
    target: str
    category: str
    ef_id: Optional[MoveEffect] = None
    ef_chance: Optional[int] = None
    ef_amount: Optional[int] = None
    ef_stat: Optional[Stat] = None
    cur_pp: int
    pos: Optional[int] = None
    disabled: int = 0
    encore_blocked: bool = False

    @classmethod
    def from_move_data(cls, move_data: list) -> 'Move':
        effect_id = move_data[gs.MOVE_EFFECT_ID]
        return cls(
            name=move_data[gs.MOVE_NAME],
            type=PokemonType(move_data[gs.MOVE_TYPE]),
            o_power=move_data[gs.MOVE_POWER],
            power=move_data[gs.MOVE_POWER],
            max_pp=move_data[gs.MOVE_PP],
            acc=move_data[gs.MOVE_ACC],
            prio=move_data[gs.MOVE_PRIORITY],
            target=move_data[gs.MOVE_TARGET],
            category=move_data[gs.MOVE_CATEGORY],
            ef_id=MoveEffect(effect_id) if effect_id is not None else None,
            ef_chance=move_data[gs.MOVE_EFFECT_CHANCE],
            ef_amount=move_data[gs.MOVE_EFFECT_AMT],
            ef_stat=Stat(move_data[gs.MOVE_EFFECT_STAT]) if move_data[gs.MOVE_EFFECT_STAT] is not None else None,
            cur_pp=move_data[gs.MOVE_PP],
        )

    def reset(self):
        self.cur_pp = self.max_pp
        self.pos = None
        self.disabled = 0
        self.encore_blocked = False
        self.power = self.o_power
        self.max_pp = self.max_pp
        self.acc = self.acc

    def get_tcopy(self) -> 'Move':
        copy = self.model_copy(deep=True)
        return copy

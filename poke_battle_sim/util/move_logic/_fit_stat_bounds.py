from __future__ import annotations


def _fit_stat_bounds(stage: int) -> int:
    if stage >= 0:
        return min(6, stage)
    else:
        return max(-6, stage)

from __future__ import annotations


def cap_name(move_name: str) -> str:
    move_name = move_name.replace("-", " ")
    words = move_name.split()
    words = [word.capitalize() for word in words]
    return " ".join(words)

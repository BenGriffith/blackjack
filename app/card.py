from dataclasses import dataclass


@dataclass(frozen=True)
class Card:
    suit: str
    rank: str
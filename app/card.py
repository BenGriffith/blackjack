from dataclasses import dataclass


@dataclass(frozen=True)
class Card:
    suit: str
    rank: str

    def __repr__(self):
        return f"({self.suit}, {self.rank})"
from dataclasses import dataclass, field
from random import shuffle


@dataclass(frozen=True)
class Card:
    suit: str
    rank: str

    def card_value(self):
        if self.rank in "J Q K".split():
            return 10
        elif self.rank == "A":
            return (1, 11)
        else:
            return int(self.rank)

    def __str__(self):
        return f"{self.__class__.__name__}({self.suit}, {self.rank})"


@dataclass
class Deck:

    cards: list = field(default_factory=list)   

    def __post_init__(self):
        suits = "clubs diamonds hearts spades".split()
        _cards = "2 3 4 5 6 7 8 9 10 J Q K A".split()
        deck = []
        for suit in suits:
            for card in _cards:
                deck.append(Card(suit, card))
        shuffle(deck)
        self.cards = deck

    def __str__(self):        
        return f"{self.__class__.__name__}({', '.join(card.__str__() for card in self.cards)})"
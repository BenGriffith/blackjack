from dataclasses import dataclass, field
from typing import List

from card import Card


@dataclass(frozen=True)
class Deck:

    def create_deck():
        suits = "clubs diamonds hearts spades".split()
        cards = "2 3 4 5 6 7 8 9 10 J Q K A".split()
        deck = []
        for suit in suits:
            for card in cards:
                deck.append(Card(suit, card))

        return deck

    cards: List[Card] = field(default_factory=create_deck)

# sole use is for testing - will eventually remove
if __name__ == "__main__":
    a = Deck()
    a.cards[0].rank = "Test"
    print(a.cards)
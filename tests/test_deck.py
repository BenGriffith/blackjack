from dataclasses import FrozenInstanceError

import pytest

from app.deck import Card, Deck

DECK = (
    "Deck(Card(clubs, 2), Card(clubs, 3), Card(clubs, 4), Card(clubs, 5), Card(clubs, 6), " 
        "Card(clubs, 7), Card(clubs, 8), Card(clubs, 9), Card(clubs, 10), Card(clubs, J), "
        "Card(clubs, Q), Card(clubs, K), Card(clubs, A), Card(diamonds, 2), Card(diamonds, 3), "
        "Card(diamonds, 4), Card(diamonds, 5), Card(diamonds, 6), Card(diamonds, 7), Card(diamonds, 8), "
        "Card(diamonds, 9), Card(diamonds, 10), Card(diamonds, J), Card(diamonds, Q), Card(diamonds, K), "
        "Card(diamonds, A), Card(hearts, 2), Card(hearts, 3), Card(hearts, 4), Card(hearts, 5), Card(hearts, 6), "
        "Card(hearts, 7), Card(hearts, 8), Card(hearts, 9), Card(hearts, 10), Card(hearts, J), Card(hearts, Q), "
        "Card(hearts, K), Card(hearts, A), Card(spades, 2), Card(spades, 3), Card(spades, 4), Card(spades, 5), "
        "Card(spades, 6), Card(spades, 7), Card(spades, 8), Card(spades, 9), Card(spades, 10), Card(spades, J), "
        "Card(spades, Q), Card(spades, K), Card(spades, A))"
)

@pytest.fixture
def card():
    return Card("hearts", "5")


@pytest.fixture
def deck():
    return Deck()


def test_card(card):
    assert card.suit == "hearts"
    assert card.rank == "5"
    assert card.__repr__() == "Card(hearts, 5)"


def test_card_mutability_error():
    with pytest.raises(FrozenInstanceError):
        card = Card("clubs", "2")
        card.rank = "3"


def test_deck_length(deck):
    assert len(deck.cards) == 52
    deck.cards.pop()
    assert len(deck.cards) == 51


def test_deck_repr(deck):
    assert deck.__repr__() == DECK


def test_deck_card_mutability_error(deck):
    with pytest.raises(FrozenInstanceError):
        first_card = deck.cards[0]
        first_card.rank = "20"
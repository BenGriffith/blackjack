from dataclasses import FrozenInstanceError

import pytest

from app.card import Card
from app.deck import Deck

DECK = (
    "Deck((clubs, 2), (clubs, 3), (clubs, 4), (clubs, 5), (clubs, 6), " 
        "(clubs, 7), (clubs, 8), (clubs, 9), (clubs, 10), (clubs, J), "
        "(clubs, Q), (clubs, K), (clubs, A), (diamonds, 2), (diamonds, 3), "
        "(diamonds, 4), (diamonds, 5), (diamonds, 6), (diamonds, 7), (diamonds, 8), "
        "(diamonds, 9), (diamonds, 10), (diamonds, J), (diamonds, Q), (diamonds, K), "
        "(diamonds, A), (hearts, 2), (hearts, 3), (hearts, 4), (hearts, 5), (hearts, 6), "
        "(hearts, 7), (hearts, 8), (hearts, 9), (hearts, 10), (hearts, J), (hearts, Q), "
        "(hearts, K), (hearts, A), (spades, 2), (spades, 3), (spades, 4), (spades, 5), "
        "(spades, 6), (spades, 7), (spades, 8), (spades, 9), (spades, 10), (spades, J), "
        "(spades, Q), (spades, K), (spades, A))"
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
    assert card.__repr__() == "(hearts, 5)"


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
from dataclasses import FrozenInstanceError

import pytest

from .context import blackjack


@pytest.fixture
def card():
    return blackjack.Card("hearts", "5")

@pytest.fixture
def number_cards():
    return range(2, 11)

@pytest.fixture
def deck():
    return blackjack.Deck()


def test_card(card):
    assert card.suit == "hearts"
    assert card.rank == "5"
    assert card.__str__() == "Card(hearts, 5)"


def test_card_value(number_cards):
    face_card = blackjack.Card("hearts", "J")
    assert face_card.card_value() == 10

    ace = blackjack.Card("hearts", "A")
    assert ace.card_value() == (1, 11)

    assert list(range(2, 11)) == [blackjack.Card("hearts", num).card_value() for num in number_cards]


def test_card_mutability_error():
    with pytest.raises(FrozenInstanceError):
        card = blackjack.Card("clubs", "2")
        card.rank = "3"


def test_deck_length(deck):
    assert len(deck.cards) == 52
    last_card = deck.cards[-1]
    assert last_card == deck.cards.pop()
    assert len(deck.cards) == 51


def test_deck_card_mutability_error(deck):
    with pytest.raises(FrozenInstanceError):
        first_card = deck.cards[0]
        first_card.rank = "20"
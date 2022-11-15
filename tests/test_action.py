import pytest

from .context import blackjack


@pytest.fixture
def deck():
    return blackjack.Deck()

@pytest.fixture
def player():
    _player = blackjack.Player()
    _player.bet = 10
    return _player

@pytest.fixture
def hit(deck, player):
    return blackjack.Action(deck, player)

@pytest.fixture
def deck_with_ace_eleven(deck):
    cards = [
        blackjack.Card("spades", "A"),
        blackjack.Card("clubs", "9"),
        blackjack.Card("diamonds", "4"),
    ]
    deck.cards.clear()
    deck.cards = cards
    return deck   

@pytest.fixture
def deck_with_ace_one(deck):
    cards = [
        blackjack.Card("hearts", "A"),
        blackjack.Card("clubs", "8"),
        blackjack.Card("diamonds", "10"),
    ]
    deck.cards.clear()
    deck.cards = cards
    return deck


def test_valid_hit(hit, deck, player):
    player_action = hit
    assert player_action.deck == deck
    assert player_action.person == player
    assert player_action.person.bet == 10
    assert player_action.person.score == 0
    assert player_action.person.hand == []
    
    player_action.hit()
    assert player_action.person.hand == player.hand
    assert len(player.hand) == 1


def test_set_ace_eleven(deck_with_ace_eleven, player):
    player_action = blackjack.Action(deck_with_ace_eleven, player)
    player_action.hit()
    assert player.score == 4
    assert player.hand == [blackjack.Card("diamonds", "4")]
    player_action.hit()
    assert player.score == 13
    assert player.hand == [blackjack.Card("diamonds", "4"), blackjack.Card("clubs", "9")]
    player_action.hit()
    assert player.score == 14
    assert player.hand == [blackjack.Card("diamonds", "4"), blackjack.Card("clubs", "9"), blackjack.Card("spades", "A")]


def test_set_ace_one(deck_with_ace_one, player):
    player_action = blackjack.Action(deck_with_ace_one, player)
    player_action.hit()
    assert player.score == 10
    assert player.hand == [blackjack.Card("diamonds", "10")]
    player_action.hit()
    assert player.score == 18
    assert player.hand == [blackjack.Card("diamonds", "10"), blackjack.Card("clubs", "8")]
    player_action.hit()
    assert player.score == 19
    assert player.hand == [blackjack.Card("diamonds", "10"), blackjack.Card("clubs", "8"), blackjack.Card("hearts", "A")]
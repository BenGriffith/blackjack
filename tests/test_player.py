import pytest

from .context import blackjack


@pytest.fixture
def deck():
    return blackjack.Deck()

@pytest.fixture
def dealer():
    return blackjack.Dealer()

@pytest.fixture
def dealer_one(dealer):
    _dealer = dealer
    _dealer.score = 5
    return _dealer

@pytest.fixture
def player():
    return blackjack.Player()

@pytest.fixture
def player_one(player):
    _player = player
    _player.score = 10
    _player.bet = 10
    return _player


def test_dealer(dealer):
    assert dealer.score == 0
    assert dealer.hand == []


def test_dealer_valid_update(dealer_one, deck):
    last_card = deck.cards[-1]
    assert len(deck.cards) == 52
    assert dealer_one.score == 5
    dealer_one.deal_card(deck, blackjack.Action)
    assert dealer_one.hand[0] == last_card
    assert len(dealer_one.hand) == 1
    assert isinstance(dealer_one.hand[0], blackjack.Card) == True


def test_dealer_invalid_score(dealer):
    with pytest.raises(ValueError):
        dealer.score = -10


def test_dealer_bet(dealer):
    with pytest.raises(AttributeError):
        dealer.bet = 10


def test_player(player):
    assert player.score == 0
    assert player.bet == 0
    assert player.hand == []


def test_player_valid_update(player_one, deck):
    last_card = deck.cards[-1]
    assert len(deck.cards) == 52
    assert player_one.score == 10
    assert player_one.bet == 10
    player_one.deal_card(deck, blackjack.Action)
    assert player_one.hand[0] == last_card
    assert len(player_one.hand) == 1
    assert isinstance(player_one.hand[0], blackjack.Card) == True


def test_player_invalid_score(player):
    with pytest.raises(ValueError):
        player.score = -10


def test_player_invalid_bet(player):
    with pytest.raises(ValueError):
        player.bet = "ten"

    with pytest.raises(ValueError):
        player.bet = -10
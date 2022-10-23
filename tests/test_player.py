import pytest

from app.player import Dealer, Player


@pytest.fixture
def dealer():
    return Dealer()

@pytest.fixture
def dealer_one(dealer):
    _dealer = dealer
    _dealer.score = 5
    _dealer.hand = "5"
    return _dealer

@pytest.fixture
def player():
    return Player()

@pytest.fixture
def player_one(player):
    _player = player
    _player.score = 10
    _player.bet = 10
    _player.hand = "K"
    return _player


def test_dealer(dealer):
    assert dealer.score == 0
    assert dealer.hand == []


def test_dealer_valid_update(dealer_one):
    assert dealer_one.score == 5
    assert dealer_one.hand == ["5"]


def test_dealer_invalid_score(dealer, capsys):
    dealer.score = -10
    captured = capsys.readouterr()
    assert captured.out == "Value should be greater than 0\n"


def test_player(player):
    assert player.score == 0
    assert player.bet == 0
    assert player.hand == []


def test_player_valid_update(player_one):
    assert player_one.score == 10
    assert player_one.bet == 10
    assert player_one.hand == ["K"]


def test_player_invalid_score(player, capsys):
    player.score = -10
    captured = capsys.readouterr()
    assert captured.out == "Value should be greater than 0\n"


def test_player_invalid_bet(player, capsys):
    player.bet = "1"
    captured = capsys.readouterr()
    assert captured.out == "Please provide an integer value\n"

    player.bet = -10
    captured = capsys.readouterr()
    assert captured.out == "Please provide a positive integer value\n"
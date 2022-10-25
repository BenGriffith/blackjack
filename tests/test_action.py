import pytest

from app.deck import Deck
from app.player import Player
from app.action import Action

@pytest.fixture
def deck():
    return Deck()

@pytest.fixture
def player():
    _player = Player()
    _player.bet = 10
    return _player

@pytest.fixture
def hit(deck, player):
    return Action("hit", deck, player)

@pytest.fixture
def double_down(deck, player):
    return Action("double down", deck, player)


def test_valid_hit(hit, deck, player):
    player_action = hit
    assert player_action.deck == deck
    assert player_action.player == player
    assert player_action.player.bet == 10
    assert player_action.player.score == 0
    assert player_action.player.hand == []
    
    player_action.hit()
    assert player_action.player.hand == player.hand
    assert len(player.hand) == 1


def test_valid_double_down(double_down, deck, player):
    player_action = double_down
    assert player_action.deck == deck
    assert player_action.player == player
    assert player_action.player.bet == 10
    assert player_action.player.hand == []

    player_action.double_down()
    assert player_action.player.bet == player.bet
    assert player.bet == 100
    assert player_action.player.hand == player.hand
    assert len(player.hand) == 1


def test_invalid_action(deck, player, capsys):
    player_action = Action("stay", deck, player)
    captured = capsys.readouterr()
    assert captured.out == "Please choose either hit, stand or double down\n"
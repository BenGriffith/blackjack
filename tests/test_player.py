import pytest

from app.player import Player


@pytest.fixture
def player():
    return Player()

@pytest.fixture
def player_one(player):
    player_one = player
    player_one.score = 1
    player_one.bet = 10
    player_one.hand = "K"
    return player_one


def test_player(player):
    assert player.score == 0
    assert player.bet == 0
    assert player.hand == []


def test_player_valid_update(player_one):
    assert player_one.score == 1
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
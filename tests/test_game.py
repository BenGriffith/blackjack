import pytest

from blackjack.deck import Deck, Card
from blackjack.player import Player, Dealer
from blackjack.action import Action
from blackjack.game import Game
from blackjack.game_setup import *


@pytest.fixture
def deck():
    return Deck()

@pytest.fixture
def dealer():
    return Dealer()

@pytest.fixture
def dealer_one_card(deck, dealer):
    dealer.deal_card(deck, Action)
    return dealer

@pytest.fixture
def player():
    return Player()

@pytest.fixture
def player_one_card(deck, player):
    player.deal_card(deck, Action)
    return player

@pytest.fixture
def game(deck, dealer, player):
    return Game(deck, dealer, player)

@pytest.fixture()
def first_round(player_one_card, dealer_one_card):
    message = (
        f"\nResult after Round 1\n"
        "---------------\n"
        f"{player_one_card}\n"
        f"{dealer_one_card.__str__()}\n\n"
    )
    return message

@pytest.fixture
def final_round(player_one_card, dealer_one_card):
    message = (
        "\nFinal Result\n"
        "---------------\n"
        f"{player_one_card}\n"
        f"{dealer_one_card}\n\n"
    )
    return message


def test_place_invalid_bet(monkeypatch, game):
    # invalid bet
    with pytest.raises(ValueError):
        monkeypatch.setattr("builtins.input", lambda _: "ten")
        bet = input("How much would you like to bet? ")
        game.player.bet = bet


def test_place_valid_bet(monkeypatch, game):
    # valid bet
    monkeypatch.setattr("builtins.input", lambda _: 10)
    bet = input("How much money would you like to bet? ")
    game.player.bet = bet
    assert game.player.bet == 10


def test_deal_card_message(capsys, game, player, dealer):
    game._deal_card_message(player, 0)
    captured = capsys.readouterr()
    assert captured.out == "Dealing Player Card...\n"
    game._deal_card_message(dealer, 0)
    captured = capsys.readouterr()
    assert captured.out == "Dealing Dealer Card...\n"


def test_result_message(capsys, game, dealer_one_card, first_round, final_round):
    game._result_message(True, dealer_one_card.__str__())
    captured = capsys.readouterr()
    assert captured.out == first_round

    game._result_message()
    captured = capsys.readouterr()
    assert captured.out == final_round


def test_player_action_hit(capsys, game):
    game._player_action_hit()
    captured = capsys.readouterr()
    assert captured.out == f"Dealing Player Card...\n{game.player}\n"


def test_player_action_stay_first_check(game):
    game.dealer.score = 10
    game.player.score = 9
    assert game._player_action_stay() == None


def test_player_action_stay_second_check(capsys, game):
    dealer_card_one = Card("hearts", "10")
    dealer_card_two = Card("hearts", "5")
    game.dealer.hand.append(dealer_card_one)
    game.dealer.hand.append(dealer_card_two)
    game.dealer.score = 15
    game.player.score = 17
    assert len(game.dealer.hand) == 2
    assert game.dealer.score < DEALER_SCORE_MIN
    game._player_action_stay()
    captured = capsys.readouterr()
    assert captured.out == f"Dealing Dealer Card...\n{game.dealer}\n"
    assert len(game.dealer.hand) == 3
    assert game.dealer.score > DEALER_SCORE_MIN


def test_process_blackjack_player(capsys, game):
    # blackjack
    game.player.bet = 10
    game.player.score = 21
    game._process_blackjack(game.player)
    captured = capsys.readouterr()

    result_message = (
        "\nFinal Result\n"
        "---------------\n"
        f"{game.player}\n"
        f"{game.dealer}\n\n"
    )

    assert captured.out == f"{result_message}Congratulations! You scored Blackjack and win ${game.player.bet * PRIZE}!\n"
    
    # bust
    game.player.score = 1
    game._process_blackjack(game.player)
    captured = capsys.readouterr()

    result_message = (
        "\nFinal Result\n"
        "---------------\n"
        f"{game.player}\n"
        f"{game.dealer}\n\n"
    )

    assert captured.out == f"{result_message}BUST! House wins!\n"


def test_process_blackjack_dealer(capsys, game):
    # blackjack
    game.dealer.score = 21
    game._process_blackjack(game.dealer)
    captured = capsys.readouterr()

    result_message = (
        "\nFinal Result\n"
        "---------------\n"
        f"{game.player}\n"
        f"{game.dealer}\n\n"
    )

    assert captured.out == f"{result_message}House scored Blackjack! You lose!\n"
    
    # bust
    game.player.bet = 1000
    game.dealer.score = 22
    game._process_blackjack(game.dealer)
    captured = capsys.readouterr()

    result_message = (
        "\nFinal Result\n"
        "---------------\n"
        f"{game.player}\n"
        f"{game.dealer}\n\n"
    )

    assert captured.out == f"{result_message}BUST! Congratulations! You win ${game.player.bet * PRIZE}!\n"


def test_player_action_prompt(monkeypatch):
    # invalid
    with pytest.raises(ValueError):
        monkeypatch.setattr("builtins.input", lambda _: "double down")
        player_action = input("Would you like another card? [hit/stay] ").upper()
        if player_action not in HIT + STAY:
            raise ValueError


def test_compare_hands(capsys, game):
    # scenario 1: player.score > dealer.score
    game.player.bet = 1000
    game.player.score = 18
    game.dealer.score = 17
    game._compare_hands()

    result_message = (
        "\nFinal Result\n"
        "---------------\n"
        f"{game.player}\n"
        f"{game.dealer}\n\n"
    )

    captured = capsys.readouterr()
    assert captured.out == f"{result_message}Congratulations! You win ${game.player.bet * PRIZE}!\n"

    # scenario 2: player.score == dealer.score
    game.dealer.score = 1
    game._compare_hands()

    result_message = (
        "\nFinal Result\n"
        "---------------\n"
        f"{game.player}\n"
        f"{game.dealer}\n\n"
    )

    captured = capsys.readouterr()
    assert captured.out == f"{result_message}Keep your money. We have a Tie!\n"

    # scenario 3: dealer.score > player.score
    game.dealer.score = 1
    game._compare_hands()

    result_message = (
        "\nFinal Result\n"
        "---------------\n"
        f"{game.player}\n"
        f"{game.dealer}\n\n"
    )

    captured = capsys.readouterr()
    assert captured.out == f"{result_message}Bummer! House wins!\n"


def test_new_game(monkeypatch, game):
    # invalid
    with pytest.raises(ValueError):
        monkeypatch.setattr("builtins.input", lambda _: "never")
        next_game = input("Thanks for playing! Would you like to play another game? [yes/no] ").upper()
        if next_game not in YES + NO:
            raise ValueError

    # valid - play again
    monkeypatch.setattr("builtins.input", lambda _: "yes")
    next_game = input("Thanks for playing! Would you like to play another game? [yes/no] ").upper()
    assert game.new_game() == True

    # valid - do not play again
    monkeypatch.setattr("builtins.input", lambda _: "no")
    next_game = input("Thanks for playing! Would you like to play another game? [yes/no] ").upper()
    assert game.new_game() == False
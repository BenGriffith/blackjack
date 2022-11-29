import pytest

from .context import blackjack


@pytest.fixture
def deck():
    return blackjack.Deck()

@pytest.fixture
def dealer():
    return blackjack.Dealer()

@pytest.fixture
def dealer_one_card(deck, dealer):
    dealer.deal_card(deck, blackjack.Action)
    return dealer

@pytest.fixture
def player():
    return blackjack.Player()

@pytest.fixture
def player_one_card(deck, player):
    player.deal_card(deck, blackjack.Action)
    return player

@pytest.fixture
def game(deck, dealer, player):
    return blackjack.Game(deck, dealer, player)

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
    dealer_card_one = blackjack.Card("hearts", "10")
    dealer_card_two = blackjack.Card("hearts", "5")
    game.dealer.hand.append(dealer_card_one)
    game.dealer.hand.append(dealer_card_two)
    game.dealer.score = 15
    game.player.score = 17
    assert len(game.dealer.hand) == 2
    assert game.dealer.score < blackjack.DEALER_SCORE_MIN
    game._player_action_stay()
    captured = capsys.readouterr()
    assert captured.out == f"Dealing Dealer Card...\n{game.dealer}\n"
    assert len(game.dealer.hand) == 3
    assert game.dealer.score > blackjack.DEALER_SCORE_MIN


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

    assert captured.out == f"{result_message}Congratulations! You scored Blackjack and win ${game.player.bet * blackjack.PRIZE}!\n"
    
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
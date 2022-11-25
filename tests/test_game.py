import pytest

from .context import blackjack


@pytest.fixture
def deck():
    return blackjack.Deck()

@pytest.fixture
def dealer():
    return blackjack.Dealer()

@pytest.fixture
def player():
    return blackjack.Player()

@pytest.fixture
def game(deck, dealer, player):
    return blackjack.Game(deck, dealer, player)


def test_deal_card_message(capsys, game, player, dealer):
    game._deal_card_message(player, 0)
    captured = capsys.readouterr()
    assert captured.out == "Dealing Player Card...\n"
    game._deal_card_message(dealer, 0)
    captured = capsys.readouterr()
    assert captured.out == "Dealing Dealer Card...\n"


def test_result_message(capsys, game, deck, player, dealer):
    player.deal_card(deck, blackjack.Action)
    dealer.deal_card(deck, blackjack.Action)

    message = (
        "\nResult after Round 1\n"
        "---------------\n"
        f"{player}\n"
        f"{dealer.__str__()}\n\n"
    )

    game._result_message(True, dealer.__str__())
    captured = capsys.readouterr()
    assert captured.out == message


# def test_game_start(monkeypatch, game):
#     monkeypatch.setattr("builtins.input", lambda _: "")

# def test_game_prompt(capsys, monkeypatch, game):

#     game.start()
#     captured = capsys.readouterr()
#     print(captured.out)
#     assert False


# def test_place_valid_bet(monkeypatch, game, player):
#     monkeypatch.setattr("builtins.input", lambda _: 10)
#     bet = input("How much would you like to bet? ")
#     player.bet = bet
#     assert player.bet == 10

#def test_place_invalid_bet(monkeypatch, game, player):
    #with pytest.raises(ValueError):
    #    monkeypatch.setattr("builtins.input", lambda _: "ten")

        
from blackjack.deck import Deck
from blackjack.player import Dealer, Player
from blackjack.game import Game


def main(play_again):
    deck = Deck()
    dealer = Dealer()
    player = Player()

    game = Game(deck, dealer, player)
    new_game = game.start(play_again)
    if new_game:
        return main(new_game)
    print("Hope to see you again soon!")


if __name__ == "__main__":
    main(False)
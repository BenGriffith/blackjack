from time import sleep

from blackjack.deck import Deck
from blackjack.player import Dealer, Player
from blackjack.game import Game, GAME_DELAY


def main(play_again):
    deck = Deck()
    dealer = Dealer()
    player = Player()

    game = Game(deck, dealer, player)
    if play_again:
        sleep(GAME_DELAY)
        print("\nWELCOME BACK! Let's play another game!")
        game.place_bet()
        if game.new_game():
            return main(True)
    else:
        if game.start():
            if game.new_game():
                return main(True)

    print("Hope to see you again soon!")


if __name__ == "__main__":
    main(False)
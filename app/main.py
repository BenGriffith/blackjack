from time import sleep

from app.deck import Deck
from app.player import Dealer, Player
from app.action import Action
from app.game import Game, GAME_DELAY


def main(play_again):
    deck = Deck()
    dealer = Dealer()
    player = Player()

    game = Game(deck, dealer, player, Action)
    if play_again:
        sleep(GAME_DELAY)
        print("\nWelcome back! Let's play another game!")
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
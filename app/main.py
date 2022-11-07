from deck import Deck
from player import Dealer, Player
from action import Action
from game import Game


def main(play_again):
    deck = Deck()
    dealer = Dealer()
    player = Player()

    game = Game(deck, dealer, player, Action)
    if play_again:
        print("\nWelcome back! Let's play another game!")
        game.place_bet()
        if game.new_game():
            return main(True)
    else:
        if game.start() not in ["no", "n"]:
            if game.new_game():
                return main(True)

    print("Hope to see you again soon!")


if __name__ == "__main__":
    main(False)
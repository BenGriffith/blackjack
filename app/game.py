from time import sleep

BLACKJACK = 21


class Game:

    def __init__(self, deck, dealer, player, Action):
        self.deck = deck
        self.dealer = dealer
        self.player = player
        self.action = Action

    def start(self):
        try:
            greeting = input("Welcome to Blackjack! Would you like to play a game? [yes/no] ").lower()
            if greeting not in ["yes", "y", "no", "n"]:
                raise ValueError("VALUE ERROR", "Please enter an acceptable value")
        except ValueError as val_err:
            err_type, message = val_err.args
            print(f"{err_type}: {message}\n")
            self.start()
        else:
            if greeting in ["yes", "y"]:
                self.place_bet()
            else:
                print("Thanks for stopping by! Hope to see you again soon!")

    def place_bet(self):
        try:
            self.player.bet = input("How much money would you like to bet? ")
        except ValueError as val_err:
            err_type, message = val_err.args
            print(f"{err_type}: {message}\n")
            return self.place_bet()
        else:
            self.first_round()

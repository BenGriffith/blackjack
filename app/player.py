from deck import Deck
from action import Action

class Player:

    def __init__(self):
        self._score = 0
        self._bet = 0
        self.hand = []

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        try:
            if value < 0:
                raise ValueError("VALUE ERROR", "Value should be greater than 0")
        except ValueError as value_err:
            err_type, message = value_err.args
            print(f"{err_type}: {message}")
            return
        self._score += value
        return self._score

    @property
    def bet(self):
        return self._bet

    @bet.setter
    def bet(self, value):
        try:
            if not isinstance(value, int):
                raise TypeError("TYPE ERROR", "Please provide an integer value")
        except TypeError as type_err:
            err_type, message = type_err.args
            print(f"{err_type}: {message}")
            return

        try:
            if value < 0:
                raise ValueError("VALUE ERROR", "Please provide a positive integer value")
        except ValueError as value_err:
            err_type, message = value_err.args
            print(f"{err_type}: {message}")
            return

        self._bet = value
        return self._bet

    def deal_card(self, deck, action):
        action(deck, self).hit()


class Dealer(Player):

    def __init__(self):
        Player.__init__(self)


if __name__ == "__main__":
    ben = Player()
    ben.bet = 10
    andrew = Dealer()
    print(andrew.bet, andrew.score, andrew.hand)
    deck = Deck()
    ben.deal_card(deck, Action)
    print(ben.hand)
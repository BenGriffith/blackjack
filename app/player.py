class Player:

    def __init__(self):
        self._score = 0
        self._hand = []
        self._bet = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        try:
            if value < 0:
                raise ValueError("Value should be greater than 0")
        except ValueError as value_err:
            print(value_err.args[0])
        self._score += value
        return self._score

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, card):
        self._hand.append(card)
        return self._hand

    @property
    def bet(self):
        return self._bet

    @bet.setter
    def bet(self, value):
        try:
            if not isinstance(value, int):
                raise TypeError("Please provide an integer value")
        except TypeError as type_err:
            print(type_err.args[0])

        try:
            if value < 0:
                raise ValueError("Please provide a positive integer value")
        except ValueError as value_err:
            print(value_err.args[0])

        self._bet = value
        return self._bet


class Dealer(Player):

    def __init__(self):
        Player.__init__(self)
class Dealer:

    def __init__(self):
        self._score = 0
        self._hand = []

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if value < 0:
            print("Value should be greater than 0")
            return
        self._score += value
        return self._score

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, card):
        self._hand.append(card)
        return self._hand


class Player(Dealer):

    def __init__(self):
        super().__init__()
        self._bet = 0

    @property
    def bet(self):
        return self._bet

    @bet.setter
    def bet(self, value):
        if not isinstance(value, int):
            print("Please provide an integer value")
            return
        if value < 0:
            print("Please provide a positive integer value")
            return
        self._bet = value
        return self._bet
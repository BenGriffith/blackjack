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
        if value < 0:
            raise ValueError()
        self._score += value
        return self._score

    @property
    def bet(self):
        return self._bet

    @bet.setter
    def bet(self, value):
        if not isinstance(value, int):
            raise TypeError()

        if value < 0:
            raise ValueError()
        self._bet = value
        return self._bet

    def deal_card(self, deck, action):
        action(deck, self).hit()

    def __str__(self):
        return f"{self.__class__.__name__}"


class Dealer(Player):

    def __init__(self):
        Player.__init__(self)

    @property
    def bet(self):
        raise AttributeError("Dealer cannot place a bet")
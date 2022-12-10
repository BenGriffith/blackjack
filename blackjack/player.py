class Player:

    def __init__(self):
        self._score = 0
        self._bet = 0
        self.hand = []
        self.kind = self.__class__.__name__

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if value < 0:
            raise ValueError("VALUE ERROR", "Value should be greater than 0")
        self._score += value
        return self._score

    @property
    def bet(self):
        return self._bet

    @bet.setter
    def bet(self, value):
        try:
            value = int(value)
        except ValueError:
            raise ValueError("VALUE ERROR", "Please provide an integer value")

        if value < 0:
            raise ValueError("VALUE ERROR", "Please provide a positive integer value")
        self._bet = value
        return self._bet

    def deal_card(self, deck, action):
        action(deck, self).hit()

    def __str__(self):
        stats = (
            f"{self.__class__.__name__} Bet: {self.bet}\n"
            f"{self.__class__.__name__} Score: {self.score}\n"
            f"{self.__class__.__name__} Hand: {', '.join(f'({card.suit.title()}, {card.rank})' for card in self.hand)}"
        )
        return stats


class Dealer(Player):

    def __init__(self):
        Player.__init__(self)

    def __str__(self):
        stats = (
            f"{self.__class__.__name__} Score: {self.score}\n"
            f"{self.__class__.__name__} Hand: {', '.join(f'({card.suit.title()}, {card.rank})' for card in self.hand)}"
        )
        return stats

    @property
    def bet(self):
        raise AttributeError("Dealer cannot place a bet")


class Player:

    def __init__(self):
        self._score = 0
        self._bet = 0
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
        self._bet += value
        return self._bet

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, card):
        self._hand.append(card)
        return self._hand


# used for prototyping - will be removed
if __name__ == "__main__":
    ben = Player()
    print(ben.score, ben.bet, ben.hand)
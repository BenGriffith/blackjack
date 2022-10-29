class Action:

    def __init__(self, deck, person):
        self.deck = deck
        self.person = person

    def hit(self):
        self.person.hand.append(self.deck.cards.pop())

    def stand(self):
        pass

    def double_down(self):
        self.player.bet = self.player.bet * self.player.bet
        self.hit()
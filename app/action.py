class Action:

    def __init__(self, deck, player, dealer):
        self.deck = deck
        self.player = player
        self.dealer = dealer

    def hit(self, individual):
        card = self.deck.cards.pop()
        if individual == "player":
            self.player.hand = card
        else:
            self.dealer.hand = card
        return

    def stand(self):
        pass

    def double_down(self):
        self.player.bet = self.player.bet * self.player.bet
        self.hit()
        return


class Action:

    def __init__(self, action, deck, player):
        self.deck = deck
        self.player = player

        if not self.validate_action(action):
            return

    def validate_action(self, action):
        if action not in ["hit", "stand", "double down"]:
            print("Please choose either hit, stand or double down")
        return True

    def hit(self):
        card = self.deck.cards.pop()
        self.player.hand = card
        return

    def stand(self):
        pass

    def double_down(self):
        self.player.bet = self.player.bet * self.player.bet
        self.hit()
        return
from blackjack.game_setup import BLACKJACK


class Action:

    def __init__(self, deck, person):
        self.deck = deck
        self.person = person

    def _set_ace(self, card_value):
        one, eleven = card_value
        if self.person.score + eleven > BLACKJACK:
            _card_value = one
        else:
            _card_value = eleven
        return _card_value

    def hit(self):
        card = self.deck.cards.pop()
        _card_value = card.card_value()
        if isinstance(_card_value, tuple):
            _card_value = self._set_ace(_card_value)
        self.person.score = _card_value
        self.person.hand.append(card)
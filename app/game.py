"""
Greeting
Player places bet
Dealer deals one card up to each player
Dealer deals one card up to themself
Dealer deals one more card up to each player
Dealer deals one cards face down to themself
Check player totals to see if anyone has scored 21

video: https://www.youtube.com/watch?v=eyoh-Ku9TCI
"""


class Game:

    def __init__(self, Deck, Dealer, Player, Action):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.action = Action(self.deck, self.player, self.dealer)

    def greeting(self):
        start_game = input("Welcome to Blackjack! Would you like to play a game? ")
        if start_game == "yes":
            self.bet()
        else:
            return

    def bet(self):
        initial_bet = input("How much money would you like to bet? ")
        self.player.bet = initial_bet
        self.first_round()

    def first_round(self):
        self.action.hit("player")
        self.action.hit("dealer")
        self.action.hit("player")
        self.action.hit("dealer")
        self.check_total()

    def check_total(self):
        pass
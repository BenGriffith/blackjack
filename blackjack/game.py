from time import sleep

from blackjack.action import Action
from blackjack.game_setup import (
    YES,
    HIT,
    STAY,
    BLACKJACK,
    PRIZE,
    GAME_DELAY,
    DEALER_SCORE_MIN,
    NO,
    PLAYER,
    DEALER,
)
from blackjack.exceptions import InvalidResponseException


class Game:

    def __init__(self, deck, dealer, player):
        self.deck = deck
        self.dealer = dealer
        self.player = player
        self.action = Action

    def start(self, play_again=False):
        while True:
            if play_again:
                sleep(GAME_DELAY)
                print("\nWELCOME BACK! Let's play another game!")               
                start_game = YES[0]
            else:
                start_game = input("Welcome to Blackjack! Would you like to play a game? [yes/no] ").upper()

            if start_game in YES:
                self.place_bet()
                return self.new_game()
            else:
                break

    def place_bet(self):
        try:
            self.player.bet = input("How much money would you like to bet? ")
        except Exception as err:
            print(f"ERROR - {err}\n")
            self.place_bet()
        else:
            self._first_round()

    def _deal_card_message(self, person, time):
        print(f"Dealing {person.kind} Card...")
        sleep(time)

    def _result_message(self, first_round=False, dealer_hand=None):
        print(f"\n{'Result after Round 1' if first_round else 'Final Result'}")
        print("---------------")
        print(self.player)
        print(f"{dealer_hand if first_round else self.dealer}\n")

    def _first_round(self):
        self._deal_card_message(self.player, GAME_DELAY)
        self.player.deal_card(self.deck, self.action)

        self._deal_card_message(self.dealer, GAME_DELAY)
        self.dealer.deal_card(self.deck, self.action)
        dealer_first_card = self.dealer.__str__()

        self._deal_card_message(self.player, GAME_DELAY)
        self.player.deal_card(self.deck, self.action)

        self._deal_card_message(self.dealer, GAME_DELAY)
        self.dealer.deal_card(self.deck, self.action)

        self._result_message(True, dealer_first_card)
        self._process_blackjack(self.player)

    def _process_blackjack(self, person):
        if person.kind == PLAYER:
            if person.score == BLACKJACK:
                self._result_message()
                print(f"Congratulations! You scored Blackjack and win ${self.player.bet * PRIZE}!")            
            elif person.score > BLACKJACK:
                self._result_message()
                print("BUST! House wins!")
            else:
                self._second_round()

        if person.kind == DEALER:
            if person.score == BLACKJACK:
                self._result_message()
                print("House scored Blackjack! You lose!")
            elif person.score > BLACKJACK:
                self._result_message()
                print(f"BUST! Congratulations! You win ${self.player.bet * PRIZE}!")
            else:
                self._compare_hands()

    def _player_action_hit(self):
        self._deal_card_message(self.player, GAME_DELAY)
        self.player.deal_card(self.deck, self.action)
        print(self.player)

    def _player_action_stay(self):
        if self.dealer.score > self.player.score:
            return
        if self.dealer.score < DEALER_SCORE_MIN:
            self._increase_dealer_score()

    def _increase_dealer_score(self):
        self._deal_card_message(self.dealer, GAME_DELAY)
        self.dealer.deal_card(self.deck, self.action)
        print(self.dealer)
        self._player_action_stay()

    def _second_round(self):
        try:
            player_action = input("Would you like another card? [hit/stay] ").upper()
            if player_action not in HIT + STAY:
                raise InvalidResponseException
        except InvalidResponseException as err:
            print(f"{err}\n")
            self._second_round()
        else:
            if player_action in HIT:
                self._player_action_hit()
                self._process_blackjack(self.player)
            else:
                self._player_action_stay()
                self._process_blackjack(self.dealer)
    
    def _compare_hands(self):
        self._result_message()
        if self.player.score > self.dealer.score:
            print(f"Congratulations! You win ${self.player.bet * PRIZE}!")
        elif self.player.score == self.dealer.score:
            print("Keep your money. We have a Tie!")
        else:
            print("Bummer! House wins!")
        
    def new_game(self):
        sleep(GAME_DELAY)
        try:
            next_game = input("\nThanks for playing! Would you like to play another game? [yes/no] ").upper()
            if next_game not in YES + NO:
                raise InvalidResponseException
        except InvalidResponseException as err:
            print(f"{err}\n")
            self.new_game()
        else:
            return next_game in YES
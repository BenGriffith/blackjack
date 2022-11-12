from time import sleep

YES = ["YES", "Y"]
NO = ["NO", "N"]
HIT = ["HIT", "H"]
STAY = ["STAY", "S"]
BLACKJACK = 21
PRIZE = 2
GAME_DELAY = 2
DEALER_SCORE_MIN = 16


class Game:

    def __init__(self, deck, dealer, player, Action):
        self.deck = deck
        self.dealer = dealer
        self.player = player
        self.action = Action

    def start(self):
        try:
            start_game = input("Welcome to Blackjack! Would you like to play a game? [yes/no] ").upper()
            if start_game not in YES + NO:
                raise ValueError("VALUE ERROR", "Please enter an acceptable value")
        except ValueError as val_err:
            err_type, message = val_err.args
            print(f"{err_type}: {message}\n")
            return self.start()
        else:
            if start_game in YES:
                self.place_bet()
                return True
            else:
                return False

    def place_bet(self):
        try:
            self.player.bet = input("How much money would you like to bet? ")
        except ValueError as val_err:
            err_type, message = val_err.args
            print(f"{err_type}: {message}\n")
            return self.place_bet()
        else:
            return self._first_round()

    def _deal_card_message(self, person, time):
        print(f"Dealing {person.__class__.__name__} Card...")
        sleep(time)

    def _final_result_message(self):
        print("\nFinal Result")
        print("---------------")
        print(self.player)
        print(self.dealer, "\n")

    def _first_round(self):
        self._deal_card_message(self.player, GAME_DELAY)
        self.player.deal_card(self.deck, self.action)

        self._deal_card_message(self.dealer, GAME_DELAY)
        self.dealer.deal_card(self.deck, self.action)
        dealer_status_first_card = self.dealer.__str__()

        self._deal_card_message(self.player, GAME_DELAY)
        self.player.deal_card(self.deck, self.action)

        self._deal_card_message(self.dealer, GAME_DELAY)
        self.dealer.deal_card(self.deck, self.action)

        print("\nResults after Round 1")
        print("---------------")
        print(self.player)
        print(dealer_status_first_card, "\n")

        blackjack_check_result = self._blackjack_check(self.player)
        return self._process_blackjack_check(self.player, blackjack_check_result)

    def _blackjack_check(self, person):
        if person.score == BLACKJACK:
            return "blackjack"
        elif person.score > BLACKJACK:
            return "bust"
        else:
            return "less"

    def _process_blackjack_check(self, person, result):
        if person.__class__.__name__ == "Player":
            if result == "blackjack":
                self._final_result_message()
                self.player.bet = self.player.bet * PRIZE
                print(f"Congratulations! You scored Blackjack and win ${self.player.bet}!")
            elif result == "bust":
                self._final_result_message()
                print("BUST! House wins!")
            else:
                return self._second_round()

        if person.__class__.__name__ == "Dealer":
            if result == "blackjack":
                self._final_result_message()
                print("House scored Blackjack! You lose!")
            elif result == "bust":
                self._final_result_message()
                self.player.bet = self.player.bet * PRIZE
                print(f"BUST! Congratulations! You win ${self.player.bet}!")
            else:
                return self._compare_hands()

    def _second_round(self):
        try:
            player_action = input("Would you like another card? [hit/stay] ").upper()
            if player_action not in HIT + STAY:
                raise ValueError("VALUE ERROR", "Please enter an acceptable value")
        except ValueError as val_err:
            err_type, message = val_err.args
            print(f"{err_type}: {message}\n")
            return self._second_round()
        else:
            if player_action in HIT:
                self._deal_card_message(self.player, GAME_DELAY)
                self.player.deal_card(self.deck, self.action)

                print(self.player, "\n")
                
                blackjack_check_result = self._blackjack_check(self.player)
                return self._process_blackjack_check(self.player, blackjack_check_result)
            else:
                return self._process_dealer_hand()

    def _process_dealer_hand(self):
        if self.dealer.score < DEALER_SCORE_MIN:
            if self.dealer.score > self.player.score:
                self._final_result_message()
                return
            self._deal_card_message(self.dealer, GAME_DELAY)
            self.dealer.deal_card(self.deck, self.action)
            print(self.dealer)
            return self._process_dealer_hand()
        blackjack_check_result = self._blackjack_check(self.dealer)
        return self._process_blackjack_check(self.dealer, blackjack_check_result)

    def _compare_hands(self):

        if self.player.score > self.dealer.score:
            self._final_result_message()
            self.player.bet = self.player.bet * PRIZE
            print(f"Congratulations! You win ${self.player.bet}!")
        elif self.player.score == self.dealer.score:
            self._final_result_message()
            print("Keep your money. We have a Tie!")
        else:
            self._final_result_message()
            print("Bummer! House wins!")
        
    def new_game(self):
        sleep(GAME_DELAY)
        try:
            next_game = input("\nThanks for playing! Would you like to play another game? [yes/no] ").upper()
            if next_game not in YES + NO:
                raise ValueError("VALUE ERROR", "Please enter an acceptable value")
        except ValueError as val_err:
            err_type, message = val_err.args
            print(f"{err_type}: {message}\n")
            return self.new_game()
        else:
            if next_game in YES:
                return True
            return False
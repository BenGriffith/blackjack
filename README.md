## General Info
Command Line Single-player game of Blackjack loosely following the structure/rules outlined in this YouTube video (https://www.youtube.com/watch?v=eyoh-Ku9TCI). 

The game consists of two rounds. In the first round, `Player` makes an initial bet and then two cards are dealt to the `Player` along with two cards being dealt to the `Dealer` with the second card face down/not yet revealed. In the last round, `Player` is presented with two options: hit or stay. When `Player` chooses hit, they are dealt another card by the `Dealer`. When `Player` chooses stay, they are deciding to not draw another card so the second card of the `Dealer` is revealed/accounted for. If the `Dealer` score is less than 16, they are required to draw another card until their score is greater than 16. `Player` score and `Dealer` score are then compared with the higher score winning.

At anytime during game play:
- If `Player` or `Dealer` score is greater than 21 (Blackjack), they bust, other entity wins and the game is over.
- If `Player` or `Dealer` score is equal to 21 (Blackjack), they win, other entity loses and the game is over.

If `Player` wins at Blackjack, they earn 2x their initial bet.

At the end of each game, the `Player` is asked if they would like to play again.

## Setup
To run this project, follow the steps below:
```
$ pip install play-blackjack
$ python -m blackjack
```
Alternatively:
```
$ git clone https://github.com/BenGriffith/blackjack.git
$ cd blackjack
$ python3 -m virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python -m blackjack
```
from deck import Deck
from entities import Player, Dealer
from hand import Hand
from typing import List
from entities import Player


class Game:
    
    def __init__(self, players: int = 1):
        self.players: List[Player] = []
        self.dealer_hand = None
        self.deck = Deck()
        
    def init_players(self, num_players) -> None:
        for _ in range(num_players):
            self.players.append(Player(10))
        
    def play(self) -> None:
        playing = True
        
        while playing:
            self.deck.shuffle()
            
            bet = int(input("Please enter your bet: "))
            self.players[0].change_balance(-bet)

            for i in range(0, len(self.players)):
                self.players[i].hand = Hand()
                
            self.dealer_hand = Hand(dealer=True)

            # for i in range(len(self.players)):
            #     for j in range(2):
            #         self.players[0].hand.add_card(self.deck.deal())
                    # self.dealer_hand.add_card(self.deck.deal())
            for i in range(2):
                self.players[0].hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())

            print("Your hand is:")
            self.players[0].hand.display()
            print()
            print("Dealer's hand is:")
            self.dealer_hand.display()

            game_over = False

            while not game_over:
                player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack()
                if player_has_blackjack or dealer_has_blackjack:
                    game_over = True
                    self.show_blackjack_results(player_has_blackjack, dealer_has_blackjack)
                    continue

                choice = input("Please choose [Hit / Stand / Double / Split] ").lower()
                while choice not in ["h", "s", "d", "sp", "hit", "stand", "double", "split"]:
                    choice = input("Please enter 'hit' or 'stand' or 'double' (or H/S/D/Sp) ").lower()
                if choice in ['hit', 'h']:
                    self.players[0].hand.add_card(self.deck.deal())
                    self.players[0].hand.display()
                    if self.player_is_over():
                        print("You have lost!")
                        game_over = True
                else:
                    player_hand_value = self.players[0].hand.get_value()
                    dealer_hand_value = self.dealer_hand.get_value()

                    print("Final Results")
                    print("Your hand:", player_hand_value)
                    print("Dealer's hand:", dealer_hand_value)

                    if player_hand_value > dealer_hand_value:
                        print("You Win!")
                        self.players[0].change_balance(bet * 2)
                    elif player_hand_value == dealer_hand_value:
                        print("Tie!")
                        self.players[0].change_balance(bet)
                    else:
                        print("Dealer Wins!")
                    game_over = True
                    
            print("Your balance is:", self.players[0].balance)
            
            again = input("Play Again? [Y/N] ")
            while again.lower() not in ["y", "n"]:
                again = input("Please enter Y or N ")
            if again.lower() == "n":
                print("Thanks for playing!")
                playing = False
            else:
                game_over = False

    def player_is_over(self):
        return self.players[0].hand.get_value() > 21

    def check_for_blackjack(self):
        player = False
        dealer = False
        if self.players[0].hand.get_value() == 21:
            player = True
        if self.dealer_hand.get_value() == 21:
            dealer = True

        return player, dealer

    def show_blackjack_results(self, player_has_blackjack, dealer_has_blackjack):
        if player_has_blackjack and dealer_has_blackjack:
            print("Both players have blackjack! Draw!")

        elif player_has_blackjack:
            print("You have blackjack! You win!")

        elif dealer_has_blackjack:
            print("Dealer has blackjack! Dealer wins!")

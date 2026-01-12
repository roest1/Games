from Deck import Deck
from Player import Player
from Dealer import Dealer
from Card import *
import time

class Game:
    def __init__(self, num_decks=1, ante=10):
        self.deck = Deck(num_decks)
        self.player = Player("You")
        self.dealer = Dealer()
        self.ante = ante
        self.pot = 0

    
    def welcome_message(self):
        print("="*80)
        print("Welcome to BlackJack!")
        print(f"Ante: ${self.ante}")
        print(f"Your Cash: ${self.player.balance}")

    def place_bet(self):
        bet_amount = input("Please enter your bet amount: ")
        bet_amount = int(bet_amount) if bet_amount.isdigit() else self.ante
        if self.player.balance < bet_amount + self.ante:
            print("Not enough balance to place the bet and pay the ante.")
            return False
        self.player.balance -= (bet_amount + self.ante)
        # Player's bet and ante, and dealer matches it
        self.pot += (bet_amount + self.ante) * 2
        print(
            f"Bet of ${bet_amount} and ante of ${self.ante} has been placed. Current balance: {self.player.balance}")
        print(f"Total pot is now: ${self.pot}")
        return True

    def start_round(self):
        self.pot = self.ante * 2  # Reset the pot to twice the ante at the start of each round
        self.player.hand.clear()
        self.dealer.hand.clear()

        dealer_time = 2
        # Deal the first card to the player and display it.
        self.player.add_card(self.deck.deal_card())
        self.display_state(show_dealer_first_card=True)
        time.sleep(dealer_time)

        # Deal the first card to the dealer (face down) and display the player's card.
        self.dealer.add_card(self.deck.deal_card())
        self.display_state(show_dealer_first_card=True)
        time.sleep(dealer_time)

        # Deal the second card to the player and display both player's cards and dealer's first card.
        self.player.add_card(self.deck.deal_card())
        self.display_state(show_dealer_first_card=True)
        time.sleep(dealer_time)

        # Deal the second card to the dealer (face up) and display all cards.
        self.dealer.add_card(self.deck.deal_card())
        self.display_state(show_dealer_first_card=False)

    def offer_insurance(self):
        insurance_bet = self.ante / 2  # half of the original bet
        player_choice = input("Do you want to buy insurance? (Y/N): ")
        if player_choice.lower() == 'y' and self.player.balance >= insurance_bet:
            self.player.balance -= insurance_bet
            self.pot += insurance_bet
            if self.dealer.get_hand_value() == 21:
                print("Dealer has Blackjack. Insurance pays out.")
                self.player.balance += insurance_bet * 2
            else:
                print("Dealer does not have Blackjack. Insurance bet lost.")

    def display_state(self, show_dealer_first_card=True):
        '''
        
        '''
        print("\033[H\033[J")  # Clear the screen
        # Display dealer's hand
        print("Dealer's Hand:")
        if show_dealer_first_card:
            # Show the dealer's hand with the first card hidden
            # Call the function with the whole dealer's hand; it will hide the first card automatically
            print(ascii_version_of_hidden_card(*self.dealer.hand))
        else:
            # When all cards should be visible (e.g., at the end of the hand)
            print(ascii_version_of_card(*self.dealer.hand))

        # Display dealer's hand value
        # Only show the dealer's hand value if the first card is not hidden
        if not show_dealer_first_card:
            print(f"Dealer's Hand Value: {self.dealer.get_hand_value()}")
        else:
            print("Dealer's Hand Value: ?")
            # print(f"Dealer's Hand Value: {self.dealer.get_hand_value()}")

        # Display dealer's cash and pot
        print("Dealer's Cash: ∞")
        print(f"Your Cash: ${self.player.balance}")
        print(f"Pot: ${self.pot}")


        # Display player's hand and its value
        print("\nYour Hand:")
        print(ascii_version_of_card(*self.player.hand))  # Ensure this function prints the cards side by side
        print(f"Hand Value: {self.player.get_hand_value()}")


    def is_busted(self, hand):
        return self.get_hand_value(hand) > 21

    def player_turn(self):
        # Before the player makes a choice, display the current state
        self.display_state()

        while True:
            choice = self.player.get_hit_or_stay()
            if choice == 'hit':
                self.player.add_card(self.deck.deal_card())
                # After hitting, display the updated state
                self.display_state()
                if self.player.get_hand_value() > 21:
                    print("Bust! You exceeded 21.")
                    return False
            else:
                print("\033[H\033[J")  # Clear the screen
                self.display_state(show_dealer_first_card=True)
                return True
            
    def dealer_turn(self):
        print("\nDealer's Hand:")
        print(self.dealer.show_hand(show_all_cards=True))
        while self.dealer.get_hand_value() < 17:
            self.dealer.add_card(self.deck.deal_card())
            print(self.dealer.show_hand(show_all_cards=True))

    def determine_winner(self):
        player_value = self.player.get_hand_value()
        dealer_value = self.dealer.get_hand_value()

        if player_value > 21:
            return 'lose'
        elif dealer_value > 21 or player_value > dealer_value:
            return 'win'
        elif player_value == dealer_value:
            return 'draw'
        else:
            return 'lose'
    
    def update_balance_after_round(self, outcome):
        # outcome could be 'win', 'lose', or 'draw'
        if outcome == 'win':
            self.player.balance += self.pot # Win: gets back double the bet
        elif outcome == 'draw':
            self.player.balance += self.ante  # Draw: gets back the bet
        # In case of 'lose', the bet is already deducted
            
    def play_round(self):
        self.start_round()
        if not self.player_turn():
            outcome = 'lose'
        else:
            self.dealer_turn()
            outcome = self.determine_winner()

        self.update_balance_after_round(outcome)
        print(f"Round outcome: {outcome.capitalize()}.")

    def play_game(self):
        self.welcome_message()
        while True:
            if not self.place_bet():
                print("Game over. You don't have enough balance.")
                break

            self.play_round()
            play_again = input("Do you want to play again? (Y/N): ")
            if play_again.lower() == 'n':
                break
            print("\033[H\033[J")

    def play_hand(self, hand):
        while not self.is_busted(hand):
            self.display_hand(hand)
            if self.get_hit_or_stay() == 'hit':
                hand.append(self.deck.deal_card())
    
    def handle_split(self):
        # Create a second hand for the player and move the second card to the new hand
        second_hand_card = self.player.hand.pop()
        second_hand = [second_hand_card, self.deck.deal_card()]
        self.player.hand.append(self.deck.deal_card())

        # Play out both hands
        print("Playing first hand:")
        self.play_hand(self.player.hand)
        print("Playing second hand:")
        self.play_hand(second_hand)

    


    

    

    

    

    

from Card import *

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.balance = 100  # Starting balance, can be changed

    def add_card(self, card):
        self.hand.append(card)

    def show_hand(self):
        return ascii_version_of_card(*self.hand)

    def get_hand_value(self):
        value = 0
        ace_count = 0
        for card in self.hand:
            if card.rank == 'Ace':
                ace_count += 1
                value += 11
            else:
                value += card.points
        while value > 21 and ace_count:
            value -= 10
            ace_count -= 1
        return value

    def get_hit_or_stay(self):
        while True:
            choice = input(
                f"{self.name}, do you want to hit or stay? (hit/stay): ").lower()
            if choice in ['hit', 'stay']:
                return choice
            else:
                print("Invalid choice. Please choose 'hit' or 'stay'.")

    
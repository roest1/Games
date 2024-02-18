from Player import Player
from Card import *

class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")

    def show_hand(self, show_all_cards=False):
        if show_all_cards:
            return super().show_hand()
        else:
            # Use ascii_version_of_hidden_card for hidden card
            return ascii_version_of_hidden_card(*self.hand)
    
    def play_hand(self, deck):
        while self.get_hand_value() < 17:
            self.add_card(deck.deal_card())


    
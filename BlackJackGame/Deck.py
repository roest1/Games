import random
from Card import Card
import secrets


class Deck:
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    ranks = ['2', '3', '4', '5', '6', '7', '8',
             '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, num_decks=1):
        self.cards = [Card(
            suit, rank) for suit in Deck.suits for rank in Deck.ranks for _ in range(num_decks)]
        self._shuffle()

    def _shuffle(self):
        # cryptographic pseudorandom number generator
        shuffled_deck = []
        while self.cards:
            card = secrets.choice(self.cards)
            self.cards.remove(card)
            shuffled_deck.append(card)
        self.cards = shuffled_deck

    def deal_card(self):
        return self.cards.pop()

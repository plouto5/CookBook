# Deck of cards class
import random


class Deck:

    def __init__(self):
        self.deck = []

    def make_deck(self):
        for x in ['H', 'D', 'S', 'C']:
            for y in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                self.deck.append(y+x)

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop()


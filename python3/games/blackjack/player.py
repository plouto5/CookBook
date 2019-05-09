# Player class

class Player:

    def __init__(self, name):
        self.name = name
        self.wallet = 0
        self.hand = []

    def hand(self,cards):
        self.hand.append(cards)

    def remove_hand(self):
        self.hand = []
        return self.hand

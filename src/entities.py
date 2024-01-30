from hand import Hand

class Player:
    def __init__(self):
        self.hand = Hand()
        self.balance = 0

class Dealer(Player):
    def __init__(self):
        super().__init__()
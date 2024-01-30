from hand import Hand

class Player:
    def __init__(self, balance: int = 1000):
        self.hand = Hand()
        self.balance = balance
    def change_balance(self, amount: int) -> None:
        self.balance += amount

class Dealer(Player):
    def __init__(self):
        super().__init__()
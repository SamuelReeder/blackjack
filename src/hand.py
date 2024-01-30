from card import Card

class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_card(self, card: Card) -> None:
        self.cards.append(card)
    
    def calculate_value(self) -> None:
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.rank.isnumeric():
                self.value += int(card.rank)
            else:
                if card.rank == "A":
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self) -> int:
        self.calculate_value()
        return self.value
    
    def reset(self) -> None:
        self.cards = []
        self.value = 0
        
    def display(self) -> None:
        if self.dealer:
            print("hidden")
            print(self.cards[1].rank, self.cards[1].suit)
        else:
            for card in self.cards:
                print(card.rank, card.suit, end=" ")
            print("Value:", self.get_value())
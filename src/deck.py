from card import Card
import random


class Deck:
    
    def __init__(self) -> None:
        self.cards = [Card(s, v) for s in ["Spades", "Clubs", "Hearts",
                      "Diamonds"] for v in ["A", "2", "3", "4", "5", "6", 
                      "7", "8", "9", "10", "J", "Q", "K"]]
        self.cards = self.cards * 4
        self.cards.append(Card(None, "Yellow"))
                
    def shuffle(self) -> None:
        random.shuffle(self.cards)
        
    def deal(self) -> Card:
        return self.cards.pop()
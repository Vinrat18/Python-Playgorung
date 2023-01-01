
from enum import Enum
import random

class CardValue(Enum):
    Ace = "Ace"
    Two = 2
    # Three = 3
    # Four = 4
    # Five = 5

class CardSuit(Enum):
    Heart = "Heart"
    Spade = "Spade"
    Club = "Club"
    Diamond = "Diamond"


class Card:
    suit: CardSuit
    value: CardValue

    def print(self) -> None:
        print(f"{self.value} of {self.suit}")

class Deck:
    __cards: list[Card] = []

    def __init__(self) -> None:
        print("Initiating Deck of cards")
        self.__create_cards()

    # @classmethod
    def __create_cards(self) -> None:
        self.__cards = []

        for suit in CardSuit:
            for value in CardValue:
                card = Card()
                card.suit = suit
                card.value = value
                self.__cards.append(card)
    
    def reset(self) -> None:
        self.__create_cards()
    
    def print(self) -> None:
        for card in self.__cards:
            card.print()
    
    def shuffle(self) -> None: 
        cards_count = len(self.__cards)
        for i in range(cards_count):
            randIndex = random.randint(0, cards_count - 1)
            self.__cards[i], self.__cards[randIndex] =  self.__cards[randIndex], self.__cards[i]
    
    def deal(self, count) -> list[Card]:
        if count > len(self.__cards):
            print("Error")
        
        return self.__cards[0:count]


if __name__ == "__main__":
    deck = Deck()

    deck.print()

    deck.shuffle()
    print("-------------------------------------------------------------")
    deck.print()

    print("-------------------------------------------------------------")
    for card in deck.deal(4):
        card.print()



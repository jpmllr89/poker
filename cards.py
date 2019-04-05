from random import shuffle
from globals import card

card = card



class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


    def __repr__(self):
        print(f"{self.card['value']} of {self.card['suit']}")


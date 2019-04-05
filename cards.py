from random import shuffle
from globals import card

card = card



class Card():

    def __init__(self):
        shuffle(card)
        self.card = card.pop()


    def __repr__(self):
        print(f"{self.card['value']} of {self.card['suit']}")


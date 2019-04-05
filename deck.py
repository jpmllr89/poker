import cards
from random import choice

class Deck:

	_deck = []


	def __init__(self):
		for i in range(0, 53):
			_deck.append(Card())


	def count_deck():
		return len(_deck)


decker = Deck()
print(decker._deck)
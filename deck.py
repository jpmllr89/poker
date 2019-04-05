from cards import Card
from random import choice

_deck = []

class Deck():

	def __init__(self):
		for i in range(0, 52):
			_deck.append(Card())


	def count_deck(self):
		return len(_deck)


	def __repr__(self):
		return f"Deck of {self.count_deck()} cards"


	def _deal(self, num):
		try:
			return _deck.pop()

		except ValueError:
			return "All cards have been dealt"


	def deal_card(self):
		return _deal(1)


	def deal_hand(self, num):
		hand = []
		for i in range(0, num):
			hand.append(deal_card(self))

		return hand

decker = Deck()
print(decker.count_deck())
decker.deal_hand(5)

print(decker.hand)

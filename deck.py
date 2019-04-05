from cards import Card
from random import shuffle

_deck = []


hand = []

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
		return self._deal(1)


	def deal_hand(self, num):
		hand = []
		for i in range(0, num):
			hand.append(self.deal_card())
		return hand


	def shuffle(self):
		if len(deck)<52:
			print("Only full decks can be shuffled")
			raise ValueError

		return shuffle(deck)

decker = Deck()
print(decker.count_deck())
print(decker.deal_hand(5))



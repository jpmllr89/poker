from random import shuffle
from cards import Card

_deck = []


hand = []

class Deck():


	def __init__(self):
		suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
		values = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
		self.cards = [Card(suit, value) for value in values for suit in suits]


	def __repr__(self):
		return f"Deck of {self.count()} cards"


	def shuffle(self):
		if self.count()<52:
			raise ValueError("Only full decks can be shuffled")
		return shuffle(self.cards)


	def count(self):
		return len(self.cards)


	def _deal(self, num):
		dealt = []
		try:
			cards = self.cards[-num:]
			self.cards = self.cards[:-num]
			return cards
		except ValueError:
			return "All cards have been dealt"

	def deal_card(self):
		return self._deal(1)[0]




	def deal_hand(self, num):
		hand = [deal_card() for i in range(0, num)]

	#def deal_card(self):

decker = Deck()

print(decker.cards)
print(decker.count())
decker.shuffle()

print(decker._deal(4))
print(decker.count())


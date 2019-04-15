#!/usr/bin/python
from card import Card
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Deck:
	"""
	Model a deck of standard playing cards, excluding the Joker
	"""
	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit, rank))

	def __str__(self): # debugging purposes for later?
		pass

	def shuffle(self):
		random.shuffle(self.deck)

	"""
	Deal cards to the dealer and player as necessary during game play.
	"""
	def deal(self): 
		try:
			top_card = self.deck.pop(0)
			return top_card
		except:
			print("Deck empty!")
			return None




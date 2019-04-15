#!/usr/bin/python
from card import Card
from deck import Deck
from hand import Hand
from chips import Chips
import os

playing = True


"""
Check that a Player's bet can be covered by their available chips and he/she entered a valid number.
"""
def take_bet():
	arr = []
	while True:
		try:
			total = int(raw_input("How many chips do you have?\n"))
			bet = int(raw_input("How many chips are you willing to bet?\n"))
			assert bet <= total and bet >= 0 and total >= 0
			arr.append(total)
			arr.append(bet)
		except ValueError:
			print("Not a valid non-negative integer amount of chips or bet. Try again!")
		except AssertionError:
			print("You don't have enough to bet that much. Try again!")
		else:
			return arr


"""
Either player can take hits until they bust. This function will be called during gameplay anytime a 
Player requests a hit, or a Dealer's hand is less than 17. It should take in Deck and Hand objects
as arguments, and deal one card off the deck and add it to the Hand. You may want it to check for aces in the event that a player's hand exceeds 21.
"""
def hit(deck, hand):
	hand.add_card(deck.deal())
	hand.adjust_for_ace()


"""
This function should accept the deck and the player's hand as arguments, and assign playing as a global
variable. If the Player Hits, employ the hit() function above. If the Player Stands, set the playing
variable to False - this will control the behavior of a while loop later on in our code.
"""
def hit_or_stand(deck, hand):
	global playing  # to control an upcoming while loop
	what_to_do = raw_input("Hit or stand?\n").lower()
	if what_to_do == "hit":
		hit(deck, hand)
	else:
		playing = False


"""
When the game starts, and after each time Player takes a card, the dealer's first card is hidden and all
of Player's cards are visible. At the end of the hand all cards are shown, and you may want to show each
hand's total value. Write a function for each of these scenarios.
"""
def show_some(player, dealer):
	print("Dealer's cards:")
	print(dealer.cards[1])
	
	print("Player's cards:")
	for card in player.cards:
		print(card)
	
def show_all(player, dealer):
	print("Dealer's cards:")
	for card in dealer.cards:
		print(card)
	print("Dealer's value: {}".format(dealer.value))
	print("Player's cards:")
	for card in player.cards:
		print(card)
	print("Player's value: {}".format(player.value))

"""
End of game scenarios
"""
def player_loses(chips):
	chips.lose_bet()
	print("You lose!")

def player_wins(chips):
	chips.win_bet()
	print("You win!")


def main():
	while True:
		print("Welcome to Black Jack!")  

		"""
		Create & shuffle the deck, deal two cards to each player
		"""
		deck = Deck() 
		deck.shuffle()
		player = Hand()  # player's hand
		dealer = Hand()  # dealer's hand
		for i in range(0, 2):
			player.add_card(deck.deal())
			dealer.add_card(deck.deal())
	
		"""
		Prompt the Player for their bet and set up the Player's chips
		"""
		chips_info = take_bet()
		chips = Chips(chips_info[0], chips_info[1])
		show_some(player, dealer)  

	
		while playing:  
			hit_or_stand(deck, player)  
			show_some(player, dealer)  
			if player.value > 21:  
				player_loses(chips)
				break

		if player.value <= 21:  # If Player hasn't busted, play Dealer's hand until Dealer reaches or exceeds 17
			while dealer.value < 17:
				hit(deck, dealer)
			show_all(player, dealer) 

			"""
			Run different winning scenarios
			"""
			if dealer.value > 21 or player.value > dealer.value:
				player_wins(chips)
			elif player.value < dealer.value:
				player_loses(chips)
		
		print("You now have {} chips.\n").format(chips.total)   
		play_again = raw_input("Would you like to play again? yes/no \n").lower()
		if play_again != "yes":
			print("Thanks for playing!\n")
			break

if __name__ == "__main__":
	main()

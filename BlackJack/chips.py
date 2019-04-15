#!/usr/bin/python

class Chips:
    def __init__(self, total, bet):
    	self.total = total
    	self.bet = bet     
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
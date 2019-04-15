#!/usr/bin/python

import sys

"""
For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""

class BankAccount:
	def __init__(self, owner, balance=0):
		self.owner = owner
		self.balance = balance

	def __str__(self):
		return "Account owner:  {}\nAccount balance:  {}".format(self.owner, self.balance)

	def deposit(self, amount):
		if amount < 0:
			return "Deposit denied! Please input a positive amount"
		self.balance += amount
		return "Deposit accepted"

	def withdraw(self, amount):
		if amount > self.balance:
			return "Funds unavailable!"
		self.balance -= amount
		return "Withdrawal accepted"


# Driver code to test all functions
def main():
    acct = BankAccount("Jack", 100)
    print(acct)

    assert acct.owner == "Jack"
    assert acct.balance == 100

    assert acct.deposit(-15) == "Deposit denied! Please input a positive amount"
    assert acct.balance == 100

    assert acct.deposit(50) == "Deposit accepted"
    assert acct.balance == 150

    assert acct.withdraw(75) == "Withdrawal accepted"
    assert acct.balance == 75

    assert acct.withdraw(500) == "Funds unavailable!"
    assert acct.balance == 75
    
    print "All tests passed"

if __name__ == "__main__":
    main()


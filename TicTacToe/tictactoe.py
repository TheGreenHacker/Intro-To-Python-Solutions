#!/usr/bin/python
import os
import random

coords = [(9, 1), (9, 5), (9, 9), (5, 1), (5, 5), (5, 9), (1, 1), (1, 5), (1, 9)]

def display_board(board):
    for row in board:
        row_str = "".join(row)
        print(row_str)

"""
Attempt to place a marker ('X' or 'O') at a desired position  (number 1-9) and
assigns it to the board. Return a bool to report success or failure and notify
the player accordingly.
"""
def place_marker(board, marker, position):
    if position >= 1 and position <= 9:
        x = coords[position - 1][0]
        y = coords[position - 1][1]
        if board[x][y] == " ":
            board[x][y] = marker
            return True
    return False

"""
Takes in a board and a mark (X or O) and then checks to see if that mark has won
"""
def win_check(board, mark):
    # check rows
    for row in xrange(1, 10, 4):
        count = 0
        for col in xrange(1, 10, 4):
            if board[row][col] == mark:
                count += 1
        if count == 3:
            return True

    # check columns
    for col in xrange(1, 10, 4):
        count = 0
        for row in xrange(1, 10, 4):
            if board[row][col] == mark:
                count += 1
        if count == 3:
            return True

    # check diagonals
    count = 0
    for square in xrange(1, 10, 4):
        if board[square][square] == mark:
            count += 1
    if count == 3:
        return True

    count = 0
    col = 9
    for row in xrange(1, 10, 4):
        if board[row][col] == mark:
            count += 1
        col -= 4
    return count == 3

"""
Checks if board is full
"""
def full_board_check(board):
    for row in xrange(1, 10, 4):
        for col in xrange(1, 10, 4):
            if board[row][col] == " ":
                return False
    return True

"""
Exception handling: player entered non-numeric string, position out of
bounds, or position already taken on board
"""
def invalid_input_handler(user_input, board):
    os.system('cls' if os.name == 'nt' else 'clear')
    if not user_input.isdigit():
        print("Please enter a valid number.")
    else:
        print("Please pick a valid and available position.")
    display_board(board)

def main():
    print("Welcome to Tic Tac Toe!")
    game_on = "yes"
    while game_on == "yes":
        # Set up the board
        board = [[" ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ",] for _ in range(11)]
        board[3] = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",]
        board[7] = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",]

        # Determine players
        mark_1 = ""
        while mark_1 != "X" and mark_1 != "O":
            mark_1 = raw_input("Player 1: Do you want to be X or O?\n").upper()
        mark_2 = "X" if mark_1 == "O" else "O"

        # Determine who goes first
        p1 = 1
        p2 = 2 
        if random.randint(1, 100) % 2:
            print("Player 1 will go first.")
        else:
            print("Player 2 will go first.")
            # Swap the players
            p1, p2 = p2, p1
            mark_1, mark_2 = mark_2, mark_1

        # Wait for players to be ready
        ready = "no"
        while ready != "yes":
            ready = raw_input("Are you ready to play?\n").lower()

        # While the game is not over yet...
        while True:
            display_board(board)
            # Player 1 turn
            while True:
                user_input = raw_input("Player {} choose your next position: (1-9)\n".format(p1))
                try:
                    position = int(user_input)
                except ValueError:
                    invalid_input_handler(user_input, board)
                    continue
                if place_marker(board, mark_1, position):
                    break
                invalid_input_handler(user_input, board)

            os.system('cls' if os.name == 'nt' else 'clear')
            display_board(board)

            if win_check(board, mark_1):
                print("Player 1 won!")
                break
            elif full_board_check(board):
                print("Tied game!")
                break

            # Player 2 turn
            while True:
                user_input = raw_input("Player {} choose your next position: (1-9)\n".format(p2))
                try:
                    position = int(user_input)
                except ValueError:
                    invalid_input_handler(user_input, board)
                    continue
                if place_marker(board, mark_2, position):
                    break
                invalid_input_handler(user_input, board)

            if win_check(board, mark_2):
                print("Player 2 won!")
                break

            os.system('cls' if os.name == 'nt' else 'clear')

        # Play again?
        replay = ""
        while replay != "no" and replay != "yes":
            replay = raw_input("Do you want to play again? Yes or No.\n").lower()
        game_on = replay


if __name__ == "__main__":
    main()



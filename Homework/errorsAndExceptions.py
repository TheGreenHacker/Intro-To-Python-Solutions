#!/usr/bin/python


"""
Problem 3
Write a function that asks for an integer and prints the square of it. Use a while
loop with a try, except, else block to account for incorrect inputs.
"""
def ask():
    while True:
        try:
            n = int(raw_input("Input an integer:"))
        except Exception as e:
            print("Not a valid number. Try again!")
        else:
            print("Your number squared is {}".format(n**2))
            break


# Driver code to test all functions
def main():
    """
    Problem 1
    Handle the exception thrown by the code below by using try and except blocks.
    """

    for i in ['a', 'b', 'c']:
        try:
            print(i**2)
        except TypeError:
            print("Cannot square non-numerical value")

    """
    Problem 2
    Handle the exception thrown by the code below by using try and except blocks. Then
    use a finally block to print 'All Done.'
    """

    x = 5
    y = 0

    try:
        z = x/y
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("All done")

    ask()

if __name__ == "__main__":
    main()
    

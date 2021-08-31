"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""

import random

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
name = input("What is your name? ")
# Here the user is asked to enter the name first
print("Hello, " + name + " I am your friend Michael")
print("Welcome to my number guessing...")
print("This is a game where you are to guess a secret number.")
print("This number is between 1 and 99.")
# Here the user is being introduced to the game.
# The user is being given an instructions to follow.
while True:
    user_input= int(input("Guess the number:"))
    ran_num = random.randint(1,99)
    # Here the user is being asked to guess the number and asked over a number of times based on the condition.
    ## Condition testing
    if user_input<ran_num:
        print("You guessed too low")
    # Here an information is displayed if the input is lower than the secret number.
    elif user_input>ran_num:
        print("You guessed too high")
    # Here an information is displayed if the input is higher than the secret number.
    else:
        print("Congratulations, You've mastered this game")
        break
    # Once the secret number is guessed the loop will break

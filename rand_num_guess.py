#!/usr/bin/env python3
# Created By: Yoma Ozoh
# Date: October, 2025
# This program plays a random number guessing game with the user

import random


def main():
    # ask user to guess number
    guess = float(input("Guess a number between 0 - 9: "))

    # set random number generator
    random_variable = random.randint(0, 9)
    # check if guess is correct or incorrect
    if guess == random_variable:
        print("You guessed correctly!")
    else:
        print("Incorrect, the correct number was: {}".format(random_variable))


if __name__ == "__main__":
    main()

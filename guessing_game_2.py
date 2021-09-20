#!/usr/bin/env python3

# Created by: Mr. Matthew Meech
# Created on: Sep 2021
# This program is a number guessing game


import random


def main():

    # input
    number = int(input("Enter number 0-9: "))
    print("")

    answer = random.randint(0, 9)

    # process & output

    if number == answer:
        print("you guessed right!")
    else:
        print("you guessed wrong!")

    print("\nDone.")


if __name__ == "__main__":
    main()

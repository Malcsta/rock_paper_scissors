"""
Description: Rock paper scissors console program
Author: Malcolm White
Date: 2023-09-29
Usage: This program is used to simluate rock, paper, scissors in the console.
The user can use the input function to make their choice, and the computer
will randomly make a choice.
"""

## Setup

import random
import os
from time import sleep

user_selections = ['R', 'P', 'S']
computer_selections = ['R', 'P', 'S']
interface_active = True


## Terminal window

while interface_active:
    computer_selection = random.randint(1,3)

    if computer_selection == computer_selections[0]:
        computer_selection = 'Rock'
    elif computer_selection == computer_selections[1]:
        computer_selection = 'Paper'       
    elif computer_selection == computer_selections[2]:
        computer_selection = 'Scissors'


    print("*"*40)
    print('{:^40s}'.format("ROCK PAPER SCISSORS")) 
    print('{:^40s}'.format("BY M@LC0LM"))
    print()
    print('{:^40s}'.format("Rock: R"))
    print('{:^40s}'.format("Paper: P"))
    print('{:^40s}'.format("Scissors: S"))
    print("*"*40)


## User input validation

    user_choice = input("Enter your selection: ")
    user_choice = user_choice.upper()
    if user_choice not in user_selections:
        print("*"*40)
        print('{:^40s}'.format("INVALID SELECTION")) 
        print("*"*40)
        break
## Users choice

    elif user_choice == user_selections[0]:
        user_choice = 'Rock'
    elif user_choice == user_selections[1]:
        user_choice = 'Paper'
    elif user_choice == user_selections[2]:
        user_choice = 'Scissors'




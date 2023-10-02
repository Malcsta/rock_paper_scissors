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
import time
import sys

user_selections = ('R', 'P', 'S')
computer_selections = ('R', 'P', 'S')
interface_active = True
user_score = 0
computer_score = 0
user_streak = 0

def slowtype(message):
    string_to_type = message
    for char in string_to_type:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.15)


## Terminal window

while interface_active:
    computer_selection = random.choice(computer_selections)
    print()
    print("*"*40)
    print('{:^40s}'.format("ROCK PAPER SCISSORS")) 
    print('{:^40s}'.format("BY M@LC0LM"))
    print('{:^40s}'.format(f"Your score: {user_score}"))
    print('{:^40s}'.format(f"Current streak: {user_streak}"))
    print('{:^40s}'.format(f"Computer score: {computer_score}"))
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
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        continue


## Determining who wins

    slowtype('3..2..1..')
    print(f"You picked: {user_choice}")
    sleep(1)
    print(f"Computer picked: {computer_selection}")
    sleep(1)

    if user_choice == computer_selection:
        print("*"*40)
        print('{:^40s}'.format("Tie!")) 
        print("*"*40)

    elif user_choice == 'S' and computer_selection == 'R':
        
        print('{:^40s}'.format("Rock beats scissors!"))
        sleep(1)
        print('{:^40s}'.format("Computer wins!"))
        computer_score += 1 
        user_streak = 0

    elif user_choice == 'R' and computer_selection == 'P':
        
        print('{:^40s}'.format("Paper beats rock!"))
        sleep(1)
        print('{:^40s}'.format("Computer wins!"))
        computer_score += 1  
        user_streak = 0
        
    elif user_choice == 'P' and computer_selection == 'S':
        
        print('{:^40s}'.format("Scissors beats paper!")) 
        sleep(1)
        print('{:^40s}'.format("Computer wins!"))
        computer_score += 1  
        user_streak = 0
        
    elif user_choice == 'S' and computer_selection == 'P':
        
        print('{:^40s}'.format("Scissors beats paper!")) 
        sleep(1)
        print('{:^40s}'.format("User wins!")) 
        user_score += 1
        user_streak +=1
        
    elif user_choice == 'P' and computer_selection == 'R':
        
        print('{:^40s}'.format("Paper beats rock!")) 
        sleep(1)
        print('{:^40s}'.format("User wins!"))
        user_score += 1 
        user_streak +=1
        
    elif user_choice == 'R' and computer_selection == 'S':
        
        print('{:^40s}'.format("Rock beats Scissorss!")) 
        sleep(1)
        print('{:^40s}'.format("User wins!"))
        user_score += 1 
        user_streak +=1
        
## Asking if user wants to try again

    try_again = input('Try again? (Y/N)')
    try_again = try_again.upper()
    if try_again == 'Y':
        os.system('cls' if os.name == 'nt' else 'clear')
    elif try_again == 'N':
        os.system('cls')
        interface_active = False

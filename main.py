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
from slowtype import slowtype

user_selections = ('R', 'P', 'S')
computer_selections = ('R', 'P', 'S')
interface_active = True
user_score = 0
computer_score = 0
user_streak = 0
<<<<<<< HEAD:main.py
=======

def slowtype(message):
    string_to_type = message
    for char in string_to_type:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.15)

>>>>>>> 97f5d59d8686fad4a643c5720ad74d192a366c03:rps.py

## Terminal window

while interface_active:
    computer_selection = random.choice(computer_selections)
    print()
<<<<<<< HEAD:main.py
    slowtype('Rock, Paper, Scissors!\n', 0.05)
    slowtype('By Malcolm White, 10/2023.\n', 0.05)
    sleep(0.7)
    print(f"Current streak: {user_streak}")
    sleep(0.7)
    slowtype('ROCK = R\n', 0.02) 
    sleep(0.7)
    slowtype('PAPER = P\n', 0.02) 
    sleep(0.7)
    slowtype('SCISSORS = S\n', 0.02) 
    sleep(0.7)
    
=======
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


>>>>>>> 97f5d59d8686fad4a643c5720ad74d192a366c03:rps.py
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

    slowtype('3..2..1..', 0.10)
    sleep(0.7)
    print(f"You picked: {user_choice}")
    sleep(1.2)
    print(f"Computer picked: {computer_selection}")
    sleep(1)

    if user_choice == computer_selection:
        print('Tie!')
        sleep(1)

    elif user_choice == 'S' and computer_selection == 'R':
        
        print("Rock beats scissors!")
        sleep(1)
<<<<<<< HEAD:main.py
        print("Computer wins!")
        computer_score += 1
        user_streak = 0 
=======
        print('{:^40s}'.format("Computer wins!"))
        computer_score += 1 
        user_streak = 0
>>>>>>> 97f5d59d8686fad4a643c5720ad74d192a366c03:rps.py

    elif user_choice == 'R' and computer_selection == 'P':
        
        print("Paper beats rock!")
        sleep(1)
        print("Computer wins!")
        computer_score += 1  
<<<<<<< HEAD:main.py
        user_streak = 0 
=======
        user_streak = 0
>>>>>>> 97f5d59d8686fad4a643c5720ad74d192a366c03:rps.py
        
    elif user_choice == 'P' and computer_selection == 'S':
        
        print("Scissors beats paper!") 
        sleep(1)
        print("Computer wins!")
        computer_score += 1  
<<<<<<< HEAD:main.py
        user_streak = 0 
=======
        user_streak = 0
>>>>>>> 97f5d59d8686fad4a643c5720ad74d192a366c03:rps.py
        
    elif user_choice == 'S' and computer_selection == 'P':
        
        print("Scissors beats paper!") 
        sleep(1)
        print("User wins!") 
        user_score += 1
<<<<<<< HEAD:main.py
        user_streak += 1
=======
        user_streak +=1
>>>>>>> 97f5d59d8686fad4a643c5720ad74d192a366c03:rps.py
        
    elif user_choice == 'P' and computer_selection == 'R':
        
        print("Paper beats rock!") 
        sleep(1)
        print("User wins!")
        user_score += 1 
<<<<<<< HEAD:main.py
        user_streak += 1
=======
        user_streak +=1
>>>>>>> 97f5d59d8686fad4a643c5720ad74d192a366c03:rps.py
        
    elif user_choice == 'R' and computer_selection == 'S':
        
        print("Rock beats Scissorss!") 
        sleep(1)
        print("User wins!")
        user_score += 1 
<<<<<<< HEAD:main.py
        user_streak += 1
=======
        user_streak +=1
>>>>>>> 97f5d59d8686fad4a643c5720ad74d192a366c03:rps.py
        
## Asking if user wants to try again

    try_again = input('Try again? (Y/N)')
    try_again = try_again.upper()
    if try_again == 'Y':
        os.system('cls' if os.name == 'nt' else 'clear')
    elif try_again == 'N':
        slowtype('Ладно, как вам угодно!', 0.05)
        sleep(2)
        os.system('cls')
        interface_active = False

sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
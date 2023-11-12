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

## Terminal window

while interface_active:
    computer_selection = random.choice(computer_selections)
    print()
    slowtype('Rock, Paper, Scissors!\n', 0.02)
    slowtype('By Malcolm White, 10/2023.\n', 0.02)
    sleep(0.7)
    slowtype(f"Current streak: {user_streak}\n", 0.02)
    sleep(0.7)
    slowtype('ROCK = R\n', 0.02) 
    sleep(0.7)
    slowtype('PAPER = P\n', 0.02) 
    sleep(0.7)
    slowtype('SCISSORS = S\n', 0.02) 
    sleep(0.7)
    
## User input validation

    while True:
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
            print("Computer wins!")
            computer_score += 1
            user_streak = 0 

        elif user_choice == 'R' and computer_selection == 'P':
            
            print("Paper beats rock!")
            sleep(1)
            print("Computer wins!")
            computer_score += 1  
            user_streak = 0 
            
        elif user_choice == 'P' and computer_selection == 'S':
            
            print("Scissors beats paper!") 
            sleep(1)
            print("Computer wins!")
            computer_score += 1  
            user_streak = 0 
            
        elif user_choice == 'S' and computer_selection == 'P':
            
            print("Scissors beats paper!") 
            sleep(1)
            print("User wins!") 
            user_score += 1
            user_streak += 1
            user_streak +=1
            
            sleep(1)
            print("User wins!")
            user_score += 1 
            user_streak += 1
            
        elif user_choice == 'R' and computer_selection == 'S':
            
            print("Rock beats Scissors!") 
            sleep(1)
            print("User wins!")
            user_score += 1 
            user_streak += 1
            
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
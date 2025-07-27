#Python number guesing game

import random

lowest_num = 1
highest_num = 100

Guesses = 0
Answer = random.randint(lowest_num , highest_num)

Is_running = True

print("Welcome to Python Guessing Game.")
print(f"Guess a number between {lowest_num} and {highest_num}.")

while Is_running:
    
    guess = input("Please enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        Guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("Number is out of range !")
            print(f"Please enter a number between {lowest_num} and {highest_num}.")
        elif guess < Answer:
            print("Too Low, Try Again!")
        elif guess > Answer:
            print("Too High, Try Again!")
        else:
            print()
            print("--------CORRECT ANSWER!---------")
            print()
            print(f"It took you {Guesses} Guesses to get to the answer.")
            Is_running = False
    else:
        print("Invalid Guess")
        print(f"Please enter a number between {lowest_num} and {highest_num}.")
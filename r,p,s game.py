#ROCK, PAPER,Scissors Game in Python

import random

Options = ("Rock","Paper","Scissors")
is_running = True

while is_running:
    
    Player = None
    Computer = random.choice(Options)

    while Player not in Options:
        Player = input("Rock,Paper or Scissors?: ")
        

    print(f"Player : {Player}")
    print(f"Computer : {Computer}")


    if Player == Computer:
        print("ITS A TIE!")
    elif Player == "Rock" and Computer == "Scissors":
        print("YOU WIN!")
    elif Player == "Paper" and Computer == "Rock":
        print("YOU WIN!")
    elif Player == "Scissors" and Computer == "Paper":
        print("YOU WIN!")
    else:
        print("AWW YOU LOSE!")

    if not input("Want to play again?(y/n): ").lower() == "y":
       is_running = False

print("Thanks For Playing!")

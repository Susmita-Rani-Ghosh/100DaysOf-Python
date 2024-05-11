rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

game_images = [rock, paper, scissors]
print("Welcome to the Rock, Paper, Scissors game!\nLet's start the game")

userChoice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. Type 'exit' to Exit \n"
    ))
if userChoice < 3 and userChoice >= 0:
    print(game_images[userChoice])
    print("Computer chose:")
    computerChoice = random.randint(0, 2)
    print(game_images[computerChoice])

    if userChoice == computerChoice:
        print("It's a draw")
    elif userChoice == 0 and computerChoice == 2:
        print("You win")
    elif userChoice == 2 and computerChoice == 0:
        print("You lose")
    elif userChoice > computerChoice:
        print("You win")
    elif userChoice < computerChoice:
        print("You Lose")
else:
    print("You made an invalid choice. Gmae Over")

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

user_points = 0
computer_points = 0

game_images = [rock, paper, scissors]
print("Welcome to the Rock, Paper, Scissors game! Let's start playing!")

while True:
    print(
        f"Score:\nYour points: {user_points}\tComputer points: {computer_points}\n"
    )
    userChoice = int(
        input(
            "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. Type 3 to EXIT \n"
        ))
    if userChoice == 3:
        if user_points == computer_points == 0:
            (print("Bye! See you later!"))
        print("Thanks for playing!")
        break
    if userChoice < 3 and userChoice >= 0:
        print(game_images[userChoice])
        print("Computer chose:")
        computerChoice = random.randint(0, 2)
        print(game_images[computerChoice])

        if userChoice == computerChoice:
            print("It's a draw")
        elif userChoice == 0 and computerChoice == 2:
            print("You win")
            user_points += 1
        elif userChoice == 2 and computerChoice == 0:
            print("You lose")
            computer_points += 1
        elif userChoice > computerChoice:
            print("You win")
            user_points += 1
        elif userChoice < computerChoice:
            print("You Lose")
            computer_points += 1
        print("\n")
    else:
        print("***You made an invalid choice. Try again.***")

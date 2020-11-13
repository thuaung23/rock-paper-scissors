import random
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
print("Welcome to the game of Rock, Paper, Scissor.")
user_choice = input("Choose 0 for Rock, 1 for Paper or 2 for Scissor.")
comp_choice = random.randint(0,2)

if user_choice == '0' and comp_choice == 0:
  print("Your choice: Rock\n", rock)
  print("Computer choice: Rock\n", rock)
  print("This round is a draw.")
elif user_choice == '0' and comp_choice == 1:
  print("Your choice: Rock\n", rock)
  print("Computer choice: Paper\n", paper)
  print("You lose.")
elif user_choice == '0' and comp_choice == 2:
  print("Your choice: Rock\n", rock)
  print("Computer choice: Scissors\n", scissors)
  print("You win.")
elif user_choice == '1' and comp_choice == 0:
  print("Your choice: Paper\n", paper)
  print("Computer choice: Rock\n", rock)
  print("You win.")
elif user_choice == '1' and comp_choice == 1:
  print("Your choice: Paper\n", paper)
  print("Computer choice: Paper\n", paper)
  print("This round is a draw.")
elif user_choice == '1' and comp_choice == 2:
  print("Your choice: Paper\n", paper)
  print("Computer choice: Scissors\n", scissors)
  print("You lose.")
elif user_choice == '2' and comp_choice == 0:
  print("Your choice: Scissors\n", scissors)
  print("Computer choice: Rock\n", rock)
  print("You lose.")
elif user_choice == '2' and comp_choice == 1:
  print("Your choice: Scissors\n", scissors)
  print("Computer choice: Paper\n", paper)
  print("You win.")
elif user_choice == '2' and comp_choice == 2:
  print("Your choice: Scissors\n", scissors)
  print("Computer choice: Scissors\n", scissors)
  print("This round is a draw.")
else:
  print("Invalid entry.")

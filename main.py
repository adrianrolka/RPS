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

#Write your code below this line 👇
choices = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if player > 2 or player < 0:
    print("Incorrect number. Try again")
else:
  print(choices[player] + "\nComputer chose:")
  computer = random.randint(0,2)
  print(choices[computer])
  if player == computer:
    print("Draw")
  elif player == 0 and computer == 1:
    print("You lose")
  elif player == 0 and computer == 2:
    print("You win!")
  elif player == 1 and computer == 2:
    print("You lose")
  elif player == 1 and computer == 0:
    print("You win!")
  elif player == 2 and computer == 0:
    print("You lose")
  elif player == 2 and computer == 1:
    print("You win!")
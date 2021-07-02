import random

#game images
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scisors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

# making a list of game images to use after
game_gafics = [rock, paper, scisors]

print("what do you Choose ? Type 0 for Rock, 1 for Paper, 2 for Scisors.")
player= int(input())

#checking if player enter a no. greater than 2 and if he will lose
if player>=3:
  print("You type a invalid character, You loose")

  # then the whole program goes to the else stream
else:
  print("\n Your Choice is \n" )
  print(game_gafics[player])

  # taking a random integer using randint function
  computer_choice = random.randint(0,2)
  print("\n Computer Choice is\n")
  print(game_gafics[computer_choice])

# algorithems to check the results of the game 
  if computer_choice == 0 and player == 2:
    print("\nYou loose")
  elif player == 0 and computer_choice == 2:
    print("\nYou Win")
  elif computer_choice > player:
    print("\nYou Loose")
  elif player > computer_choice:
    print("\nYou Win")
  elif computer_choice == player:
    print("\nThis is a Draw")
  
input()


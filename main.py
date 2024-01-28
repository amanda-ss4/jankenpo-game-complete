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

user_choice = int(input("Qual sua escolha? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura. \n"))

if user_choice >= 3 or user_choice < 0:
  print("Você perdeu!")
else:
  game = [rock, paper, scissors]
  print(game[user_choice])

  pc_choice = random.randint(0, 2)
  print("Escolha do PC: \n")
  print(game[pc_choice])

  if user_choice == pc_choice:
    print("É um empate!")
  elif (user_choice == 0) and (pc_choice == 2):
    print("Você ganhou!")
  elif (user_choice == 2) and (pc_choice == 1):
    print("Você ganhou!")
  elif (user_choice == 1) and (pc_choice == 0):
    print("Você ganhou!")
  else:
    print("Você perdeu!")


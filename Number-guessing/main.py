from art import logo
import random
print(logo)
print("Welcome to the number guessing game!! \nI'm thinking of a number between 1 and 100!")
actual_guess=random.randint(1,100)
print(actual_guess)
def level():
  difficulty=input("Choose a difficulty type 'easy' or 'hard'?")
  difficulty=difficulty.lower()
  if difficulty=="easy":
    attempts=10
  elif difficulty=="hard":
    attempts=5
  else:
    print("Since you entered a invalid difficulty type, I shall give you hard one!")
    attempts=5
  return(attempts)

attempts=level()
def guess_game(attempts):
  choice=False
  while not choice :
    print(f"You have {attempts} attempts remaining to guess the number!")
    user_input=int(input("Make a guess: "))
    if user_input==actual_guess:
      print("You win!!!! OMG!!")
      choice=True
    elif attempts==1:
      print("You Lose!!")
      choice=True
    elif user_input>actual_guess:
      print("Too high!\nGuess again!")
      attempts-=1
    elif user_input<actual_guess:
      print("Too low!\nGuess again!")
      attempts-=1
    else:
      print("umm i was not prepared for this ")
guess_game(attempts)
  
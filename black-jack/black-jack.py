
import art
import os
import random

choice = "y"
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_score=0
user_score=0
def calculations(computer_score=computer_score, user_score=user_score):
    next_computer_card = random.choice(cards)
    computer_score += next_computer_card
    computer_card.append(next_computer_card)
    if computer_score > 21:
        print("You win!")
        print(f"Your final hand: {user_card}, final score:{user_score}")
        print(f"Computer's final hand: {computer_card}, final score:{computer_score}")
    else:
        if computer_score == user_score:
            print("Draw!")
            print(f"Your final hand: {user_card}, final score:{user_score}")
            print(f"Computer's final hand: {computer_card}, final score:{computer_score}")
        elif computer_score > user_score:
            print("You lose!")
            print(f"Your final hand: {user_card}, final score:{user_score}")
            print(f"Computer's final hand: {computer_card}, final score:{computer_score}")
        else:
            print("You win!")
            print(f"Your final hand: {user_card}, final score:{user_score}")
            print(f"Computer's final hand: {computer_card}, final score:{computer_score}")


def first_cal(choice, computer_score, user_score):
    while choice == 'y' or choice == 'Y':

        print(
            f"Your cards: {user_card} , current score:{user_score}"
        )
        print(f"Computer's First card:{computer_card[0]}")
        if computer_score == 21:
            print("You lose!Computer got a blackjack!")
            print(f"Your final hand: {user_card}, final score:{user_score}")
            print(f"Computer's final hand: {computer_card}, final score:{computer_score}")
            break
        elif user_score == 21:
            print("You win!You've got a blackjack!")
            print(f"Your final hand: {user_card}, final score:{user_score}")
            print(f"Computer's final hand: {computer_card}, final score:{computer_score}")
            break
        else:
            if user_score > 21:
                if user_card[0] == 11 or user_card[1]== 11:
                    user_score -= 10
                    if user_score > 21:
                        print("You lose !Score exceeded 21")
                        print(f"Your final hand: {user_card}, final score:{user_score}")
                        print(f"Computer's final hand: {computer_card}, final score:{computer_score}")
                        break
                else:
                    print("You lose!Score exceeded 21")
                    print(f"Your final hand: {user_card}, final score:{user_score}")
                    print(f"Computer's final hand: {computer_card}, final score:{computer_score}")
                    break
            else:
                choice = input("Do you wanna get more card? y or n: ")
                if choice=='y':
                  user_next_card = random.choice(cards)
                  user_card.append(user_next_card)
                  user_score += user_next_card
                elif choice == 'n' or choice == 'N':
                  if computer_score < 17:
                    calculations(computer_score, user_score)


choice1='yes'
while choice1 == 'yes':
  choice1 = input("Do you wanna play a game of blackjack?Type yes or no: ")
  if choice1 == 'no':
    break
  os.system('clear')
  print(art.logo)
  user_card=[random.choice(cards),random.choice(cards)]
  computer_card = [random.choice(cards),random.choice(cards)]
  user_score = 0
  computer_score = 0
  next_user_card = 0
  next_computer_card = 0
  user_score = user_card[0] + user_card[1]
  computer_score = computer_card[0] + computer_card[1]
  first_cal(choice, computer_score, user_score)
  
     
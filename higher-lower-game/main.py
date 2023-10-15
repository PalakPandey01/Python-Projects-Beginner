import game_data
import art
import random 
import os
print(art.logo)
score=0
def which_is_larger(a,b):
  if (a>b):
    return ('A')
  else:
    return ('B')
first_person=random.choice(game_data.data)
def continuous(first_person,score):
  second_person=random.choice(game_data.data)
  name1=first_person["name"]
  description1=first_person["description"]
  country1=first_person["country"]
  follower1=first_person["follower_count"]
  print(f"Compare A: {name1} , a {description1}, from {country1} .")
  print(art.vs)
  name2=second_person["name"]
  description2=second_person["description"]
  country2=second_person["country"]
  follower2=second_person["follower_count"]
  print(f"Against B: {name2} , a {description2}, from {country2} .")
  choice=input("Who has more followers? Type \'A\' or \'B\': ")
  answer=which_is_larger(follower1,follower2)
  if (choice==answer):
    os.system('clear')
    score+=1
    print(art.logo)
    print("You're Right!")
    print(f"Current Score: {score}.")
    continuous(second_person,score)
  else:
    os.system('clear')
    print(art.logo)
    print("Sorry! You lose!")
continuous(first_person,score)


    
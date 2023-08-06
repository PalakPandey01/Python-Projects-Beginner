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


choice_user=int(input("Enter 1 for rock , 2 for paper and 3 for scissors."))
computer_choice=random.randint(1,3)
print("Computer chose:")
if computer_choice==1:
     print(rock)
elif computer_choice==2:
     print(paper)
else:
    print(scissors)


if choice_user!=1 and choice_user!=2 and choice_user!=3:
  print("wrong choice dumbo!")
else:
  print("You chose:")
  if choice_user==1:
     print(rock)
  elif choice_user==2:
     print(paper)
  else:
    print(scissors)

if computer_choice==1 and choice_user==1:
  print ("Draw!")
elif computer_choice==1 and choice_user==2:
  print("You win!")
elif computer_choice==1 and choice_user==3:
  print("You lose!")
if computer_choice==2 and choice_user==2:
  print ("Draw!")
elif computer_choice==2 and choice_user==3:
  print("You win!")
elif computer_choice==2 and choice_user==1:
  print("You lose!")
if computer_choice==3 and choice_user==3:
  print ("Draw!")
elif computer_choice==3 and choice_user==1:
  print("You win!")
elif computer_choice==3 and choice_user==2:
  print("You lose!")
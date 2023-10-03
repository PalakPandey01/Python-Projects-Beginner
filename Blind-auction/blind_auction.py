import os
import art
import time

print(art.logo)
dict_info={}
choice="yes"
while choice=="yes":
  print("WELCOME TO THE BLIND AUCTION PROGRAM!! TA DAAAAA!!")
  name=input("What is your name?:")
  bid_amount=input("What is your bidding amount?:")
  dict_info[name]=bid_amount
  choice=input("Are there any more bidders? yes or no?: ")
  choice=choice.lower()
  os.system('clear')
  if choice == "no":
    break

highest=0
for i in dict_info:
  value=dict_info[i]
  value1=float(value)
  if highest<=value1:
    highest=value1
    name_highest_bidder=i

print(f"The bid is won by {name_highest_bidder} who bid {highest}")

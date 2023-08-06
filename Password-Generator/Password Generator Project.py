#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
print("Easy level password generator:")
strings=""
for i in range (0,nr_letters):
  ranletter=random.randint(0,51)
  strings=strings+letters[ranletter]
for i in range (0,nr_symbols):
  ransymbols=random.randint(0,8)
  strings=strings+symbols[ransymbols]
for i in range (0,nr_numbers):
  rannumbers=random.randint(0,9)
  strings=strings+numbers[rannumbers]
print(strings)

  

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
print("Tough level password generator:")
strings=""
for i in range (0,nr_letters):
  ranletter=random.randint(0,51)
  strings=strings+letters[ranletter]
for i in range (0,nr_symbols):
  ransymbols=random.randint(0,8)
  strings=strings+symbols[ransymbols]
for i in range (0,nr_numbers):
  rannumbers=random.randint(0,9)
  strings=strings+numbers[rannumbers]
strings=list(strings)
strings=random.sample(strings,len(strings))
strings1=""
for j in strings:
  strings1+=j
print(strings1)
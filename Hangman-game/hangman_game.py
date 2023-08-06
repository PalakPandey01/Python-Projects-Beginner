#hangman project
import hangman_art
import random
import hangman_words

chosen_word = random.choice(hangman_words.word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

print(hangman_art.logo)
display=[]
for i in chosen_word:
    display.append("_")


lives=6
while "_" in display:
  print(f"Current lives left : {lives}")
  if lives==0:
    print("You lose!")
    break
  
  guess = input("Guess a letter: ").lower()
  if guess not in chosen_word:
    lives-=1
  print(hangman_art.stages[lives]) 

  if guess in display:
    print(f"You have already entered this letter :{guess}")
    
  c=-1
  for letter in chosen_word:
        c+=1
        if letter == guess :
          display[c]=letter
          
            
    
  
  print(display)


c=0
for i in display:
  if  "_"==i:
    c+=1
if c==0:
  print("You won!")
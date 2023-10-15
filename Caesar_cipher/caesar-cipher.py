import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)

def caesar(word,move,choice):
  if choice =="encode":
    encrypted_word=""
    for ch in word:
      if ch.isalpha()==True:
        c=alphabet.index(ch)
        shift1=move+c
        if shift1>=25:
          shift1=shift1%26
        encrypted_word=encrypted_word + alphabet[shift1]
      else:
        encrypted_word=encrypted_word+ch
    print(f"The encrypted word is {encrypted_word}")
  elif choice=="decode":
    decrypted_word=""
    move*=-1
    for ch in word:
      if ch.isalpha()==True:
        c=alphabet.index(ch)
        shift1=c+move
        if shift1<=0:
          shift1=shift1%26
        decrypted_word=decrypted_word + alphabet[shift1]
      else:
        decrypted_word+=ch
    print(f"The decrypted word is {decrypted_word}")
  else:
    print("wrong choice")

decision=input("Type yes if you wanna encode or decode something or type no:")
decision=decision.lower()

while decision=="yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text,shift,direction)
  decision=input("Type yes if you wanna encode or decode something or type no:")
  decision=decision.lower()
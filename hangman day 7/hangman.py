import random
from hangman_art import stages , logo
from hangman_words import wordlist
print(logo)
chosenword= random.choice(wordlist)

blank=[]
for i in range (len(chosenword)):
  blank.append("_")
print(blank)

lives=6
endofgame=False
while endofgame==False:
  letterchosen=input("Choose a letter.").lower()
  for i in range (len(chosenword)):
    if letterchosen==chosenword[i]:
      blank[i]=letterchosen #i. item yerine seçilen harfi yaz.
  print(blank)    
  if letterchosen not in chosenword:
    lives=lives-1 
    print(stages[lives])
  if lives==0:
    endofgame=True
    print(f"You lose.The word was {chosenword}. ")
  if "_" not in blank:
    endofgame=True
    print("You win.")

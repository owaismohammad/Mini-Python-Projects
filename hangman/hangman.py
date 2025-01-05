import random

from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

print(logo)
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')
print()

display=[]
for char in chosen_word:
  display.append('_')
f=[]
i=0
j=-1
while j!=6:
  if "_" not in display:
    from hangman_art import win
    print(win)
    break
  
  else:
    guess = input("Guess a letter: ").lower()
    
    if guess in chosen_word:
      
      if guess in f:
        print()
        from hangman_art import already
        print(already)
        print()
      f.append(guess)
      while i<len(chosen_word):
        if guess==chosen_word[i]:
          display[i]=guess
        i=i+1
    else:
        j=j+1
        print()
        print(f"You guessed {guess} which is not in the word. You lose a life.  ")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        print()
        print(stages[6-j])
        print()
    if j==6:
      print()
      from hangman_art import lose
      print(lose)
      break
    i=0
    print()
    print(display)
    print()

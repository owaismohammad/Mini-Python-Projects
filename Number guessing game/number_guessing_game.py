import random
from art import START_LOGO
from art import end
print(START_LOGO)
print("Welcome to the number guessing game")
print("I am thinking of a number between 1 to 100")
diff=input("Choose a difficulty. Type 'easy' or 'hard': ")
diff=diff.lower()
nos=random.randint(1,100)
if diff=='easy':
    flag=0
    i=10
    while i>=1:
        print(f"You have {i} attempts remaining to guess the number")
        guess=int(input("Make a guess:  "))
        if nos> guess:
            print("Too Low")
        elif nos<guess:
            print("Too High")
        elif nos==guess:
            print(f"You got it! The answer is {guess}")
            flag=1
            break
        i=i-1
        if i==0 and flag!=1:
            print("You've run out of guesses, you lose")
elif diff=='hard':
    flag=0
    i=5
    while i>=1:
        print(f"You have {i} attempts remaining to guess the number")
        guess=int(input("Make a guess:  "))
        if guess<nos:
            print("Too Low")
        elif guess > nos:
            print("Too High")
        elif nos==guess:
            print(f"You got it! The answer is {guess}")
            flag=1
            break
        i=i-1
        if i==0 and flag!=1:
            print("You've run out of guesses, you lose")

print(end)
from game_data import data
from art import logo
from art import vs
from art import end
print(logo)
import random
flag=1
g=random.randint(0,49)
c=0   
print()
while flag==1:
    h=random.randint(0,49)
    print()
    print()
    print(f"Your score is {c}")
    if g!=h:
        print(f"Compare A: {data[g]['name']}, {data[g]['description']}, from {data[g]['country']}")
        print(vs)
        print(f"Compare B: {data[h]['name']}, {data[h]['description']}, from {data[h]['country']}")
        print("Who  has more followers? Type 'A' or 'B': ")
        choice=input()
        if choice=='A' and (data[g]["follower_count"]>data[h]["follower_count"]):
            print("1")
            c=c+1
            continue
        elif choice=='B' and (data[h]["follower_count"]>data[g]["follower_count"]):
            print("2")
            g=h
            c=c+1
            continue
        elif choice=='A' and (data[g]["follower_count"]<data[g]["follower_count"]):
            print("3")
            flag=2
        elif choice=='B' and (data[h]["follower_count"]<data[g]["follower_count"]):
            print("4")
            flag=2
    else:
        print("5")
        continue
print(f"Sorry that's Wrong, Your score was {c}")
print(end)
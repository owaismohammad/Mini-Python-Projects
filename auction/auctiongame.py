list=[]
dict={}
from auctiongame_logo import logo
from auctiongame_logo import auction
print(auction)
print(logo)
def auction(name,bid):
    dict[bid]=name

hb=0

choice="yes"
while choice=="yes":
    name=input("What is your name? ")
    bid=int(input("How much is your bid? "))
    auction(name,bid)
    choice=input("Are there any more bidders (Yes/No): ")
    choice=choice.lower()
for key in dict:
    if key>hb:
        hb=key
print(f"The highest bid is by {dict[hb]}")


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


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
import random

letter_add=""
number_add=""
symbol_add=""
for no in range(0, nr_letters):
  letter_add+=letters[random.randint(0,len(letters)-1)]
for i in range(0, nr_symbols):
  symbol_add+=symbols[random.randint(0,len(symbols)-1)]
for j in range(0, nr_numbers):
  number_add+=numbers[random.randint(0,len(numbers)-1)]

password=letter_add+symbol_add+number_add
print(password)

# Method 1

# new=""
# random_List=[]
# for k in range(30):
#   r=random.randint(0,len(password)-1)
#   if r not in random_List:
#     random_List.append(r)
#   if len(random_List)==len(password):
#     break

# for y in random_List:
#   new+=password[y]
# print(new)

#Method 2

password_list=[]
for char in password:
  password_list.append(char)
random.shuffle(password_list)
new=""
for char in password_list:
  new+=char
print(new)

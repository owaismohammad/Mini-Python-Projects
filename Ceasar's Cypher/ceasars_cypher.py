
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
from art import logo
print(logo)
choice=input("Type Encode to encrypt, type 'decode' to decrypt: ")
choice=choice.lower()
s=""
cont="yes"
c=0
con="yes"
cot="yes"

while choice=="encode" or choice=="decode":

    if choice=="encode":

        while con=="yes":
            word=input("Type your message: ")
            word=word.lower()
            shift=int(input("Type the shift number: "))
            for char in word:
                if char==' ':
                    s+=char
                    continue
                c=letters.index(char)
                c+=shift
                if c>25:
                    c=c-26
                    s=s+letters[c]
                else:
                    s=s+letters[c]
            print(f"Here's the encoded result {s}")
            s=""
            c=0
            word=""
            con=input("Type yes if you want to further continue to encryption, othervise type no: ")
            con=con.lower()
        
    elif choice=="decode":
        while cot=="yes":
            word=input("Type your message: ")
            word=word.lower()
            shift=int(input("Type the shift number: "))
            for char in word:
                if char==' ':
                    s+=char
                    continue
                c=letters.index(char)
                c-=shift
                if c>25:
                    c=c-26
                    s=s+letters[c]
                else:
                    s=s+letters[c]
            print(f"Here's the decoded result {s}")
            s=""
            c=0
            word=""
            cot=input("Type yes if you want to further continue to decryption, othervise type no: ")
            cot=cot.lower()
    last=input("Do you wish to further use Ceasar's Cyphers 'yes' or 'no': ")
    last=last.lower()
    if last=="yes":

        choice=input("Type Encode to encrypt, type 'decode' to decrypt: ")
        choice=choice.lower()
    else:
        break
from art import end
print(end)

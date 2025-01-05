from turtle import Turtle, Screen
import random
screen=Screen()

def game():
    screen.setup(width=1000,height=700)
    screen.bgcolor("cornflower blue")

    heading1=Turtle()
    heading1.penup()
    heading1.goto(-470,200)
    heading1.pendown()
    heading1.color("black")
    style = ('Bauhaus 93', 30, 'bold')
    heading1.write('Turtle\nRace',font=style,align='left')
    heading1.hideturtle()

    heading2=Turtle()
    heading2.penup()
    heading2.goto(-470,250)
    heading2.pendown()
    heading2.color("black")
    style = ('Bauhaus 93', 20, 'bold')
    heading2.write('PICK THE COLOUR AND WIN THE RACE',font=style,align='left')
    heading2.hideturtle()


    
    color=['red','orange','green','blue','black','yellow','pink']
    y_positions=[-320,-240,-160,-80,0,80,160]
    x=0
    name=["red","orange","green","blue","violet","yellow","pink"]
    text=["red","orange","green","blue","violet","yellow","pink"]
    jumps=[1,2,3,4,5,6,7,8,9,10]
    style = ('Bauhaus 93', 12, 'bold')
    for r in range(0,7):
        
        name[r]=Turtle()
        name[r].shapesize(2)
        name[r].shape("turtle")
        name[r].color(color[r])
        name[r].penup()
        text[r]=Turtle()
        text[r].penup()
        text[r].color(color[r])
        text[r].goto(-470,y_positions[r]+20)
        text[r].pendown()
        style = ('Bauhaus 93', 15, 'bold')
        text[r].write(color[r],font=style,align='left')
        text[r].hideturtle()
        name[r].goto(x=-470,y=y_positions[r])
        
    user_bet=screen.textinput(title="Make Your Bet", prompt="Choose A Turtle you would want to win the Race!")

    while x!=500:
        for r in range(0,7):
            
            if name[r].xcor()>= 450:
                winner=name[r]
                x=500
                break
            else:
                name[r].forward(jumps[random.randint(0,9)])
    print(name[r])
    if user_bet==winner:
        gameover=screen.textinput(title="Turtle Race", prompt="Yay!! You Win\nDo you wish to Play Again(Y/N)?")
        
    else:
        gameover=screen.textinput(title="Turtle Race", prompt=f"'You Lose'\nThe Race is Won by{winner}.\nDo you wish to Play Again(Y/N)?")
    if gameover.lower()=='y':
        return True
    elif gameover.lower()=='n':
        return False

f=game()
if f==True:
    screen.clear()
    game()
else:
    message=screen.textinput(title="Turtle Race", prompt="Press 'Y' to exit")


    
screen.exitonclick()    
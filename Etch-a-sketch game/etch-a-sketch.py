from turtle import Turtle, Screen
import random

screen=Screen()

screen.title("Etch-A-Sketch Game")
timmy=Turtle()
timmy.shapesize(2)

timmy.shape('turtle')
timmy.color("midnight blue")
i=5
screen.bgcolor("white")
screen.screensize(100,100)
timmy.pensize(i)

heading1=Turtle()
heading1.penup()
heading1.goto(80,220)
heading1.pendown()
heading1.color("black")
style = ('Bauhaus 93', 12, 'bold')
heading1.write('W->UP     S->DOWN     A->LEFT\nD->RIGHT     SPACE->COLOR-CHANGE     F->CIRCLE\nY->TRY DIFFERENT SHAPES\nX->TURTLE\nK->LINE-THICK     O->LINE-THIN',font=style,align='left')
heading1.hideturtle()

heading=Turtle()
heading.penup()
heading.goto(-360,250)
heading.pendown()
heading.color("midnight blue")
style = ('Bauhaus 93', 25, 'bold')
heading.write('ETCH-A-SKETCH',font=style,align='left')
heading.hideturtle()




def forward():
    timmy.forward(50)
def back():
    timmy.backward(50)
def left1():
    timmy.left(30)

    

def right1():
    newheading=timmy.heading()-10
    timmy.setheading(newheading)

def clear():
    timmy.clear()   
    timmy.penup()
    timmy.home()
    timmy.pendown()
def changecolor():
    colors = [
    "black",
    "white",
    "red",
    "lime",
    "blue",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "aquamarine",
    "magenta",
    "green",
    "lightgray",
    "gray",
    "maroon",
    "olive",
    "teal",
    "silver",
    "skyblue",
    "springgreen",
    "limegreen",
    "greenyellow",
    "chartreuse",
    "mediumspringgreen",
    "lightgreen",
    "springgreen2",
    "mediumseagreen",
    "seagreen",
    "darkcyan",
    "lightseagreen",
    "cyan",
    "lightcyan",
    "aquamarine",
    "turquoise",
    "cadetblue",
    "steelblue",
    "lightsteelblue",
    "lightblue",
    "powderblue",
    "lightskyblue",
    "skyblue",
    "deepskyblue",
    "dodgerblue",
    "cornflowerblue",
    "mediumslateblue",
    "royalblue",
    "blue",
    "mediumblue",
    "darkblue"
]
    timmy.pencolor(colors[random.randint(0,len(colors))])
def drawcirclde():
    timmy.circle(50)
def penWidthinc():
    timmy.pensize(i+10)

def penWidthdec():
    timmy.pensize(i)

def shape():
    s=['arrow','circle','square','triangle','classic']
    timmy.shape(s[random.randint(0,4)])
def original():
    timmy.shape("turtle")
screen.listen()
screen.onkey(forward,'w')
screen.onkey(back,'s')
screen.onkey(left1,'a')
screen.onkey(right1, 'd')
screen.onkey(clear,'c')
screen.onkey(drawcirclde,'f')
screen.onkey(changecolor,'space')
screen.onkey(penWidthinc,'k')
screen.onkey(penWidthdec,'o')
screen.onkey(shape, 'y')
screen.onkey(original,'x')
screen.exitonclick()
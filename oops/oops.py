from turtle import Screen, Turtle
import prettytable
import turtle
timmy=Turtle()

turtle.colormode(255.0)

# tom=Turtle()
timmy.shape("turtle")
# tom.shape("circle")
# tom.color("orange")
myScreen=Screen()
print(myScreen.canvheight)
timmy.color("red")


#Making Dotted lines using pencolor()
# i=1
# while i<=10:
#     timmy.pencolor("black")
#     timmy.forward(5)
#     timmy.pencolor("white")
#     timmy.forward(5)
#     i+=1

#Making Dotted lines using penup() and pendown()

# i=0
# while i<=10:    
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)

#Makes the turtle move in a square
# timmy.forward(100)
# while True:
#         if abs(timmy.pos()) < 1:
#                 break
#         timmy.left(90)
#         timmy.forward(100)
# r=["red", "blue","yellow", "orange","purple", "black", "green","indigo"]
# timmy.forward(100)
# while True:
#     timmy.color(r[0])

#     if abs(timmy.pos()) < 1:
#             break
#     else:
#         timmy.left(120)
#         timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
# while True:
#         timmy.color(r[1])
        
#         if abs(timmy.pos()) < 1:
#                 break
#         timmy.left(90)
#         timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# while True:
#         timmy.color(r[2])
        
#         if abs(timmy.pos()) < 1:
#                 break
#         timmy.left(72)
#         timmy.forward(100)
# timmy.left(72)
# timmy.forward(100)
# while True:
#         timmy.color(r[3])
        
#         if abs(timmy.pos()) < 1:
#                 break
#         timmy.left(60)
#         timmy.forward(100)
# timmy.left(60)
# timmy.forward(100)
# while True:
#         timmy.color(r[4])
        
#         if abs(timmy.pos()) < 1:
#                 break
#         timmy.left(360/7)
#         timmy.forward(100)
# timmy.left(360/7)
# timmy.forward(100)
# while True:
#         timmy.color(r[4])
        
#         if abs(timmy.pos()) < 1:
#                 break
#         timmy.left(360/8)
#         timmy.forward(100)

# def drawshapes(num_sides,color):
#         timmy.color(color)
#         angle=360/num_sides
#         for i in range(num_sides):
#                 timmy.forward(100)
#                 timmy.left(angle)

# sides=int(input("Enter nos. of shapes you want to draw  "))
import random
color = [
    "Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink",
]
timmy.pensize(15)
# angle=[0,90,180,270]

# for i in range(3, sides+1):
#         drawshapes(i, color[i])


# j=True
# y=len(color)
# while True:
        # r=int(random.randint(1,254))
        # g=int(random.randint(1,254))
        # b=int(random.randint(1,254))
        # k=random.randint(1,100)
        # timmy.color(r,g,b)
#         j=random.randint(1,100)
#         timmy.forward(k)
#         timmy.left(angle[random.randint(0,len(angle)-1)])

#Drawing a Circle
timmy.pensize(0)
# while True:
    # r=int(random.randint(1,254))
    # g=int(random.randint(1,254))
    # b=int(random.randint(1,254))
#     k=random.randint(1,100)
    # timmy.speed(100)
    # timmy.color(r,g,b)
#     timmy.circle(50)
#     timmy.right(14)
#     timmy.circle(50)

# New Method
# i=0
# ang=4
# while 360-i!=2*ang:
#     r=int(random.randint(1,254))
#     g=int(random.randint(1,254))
#     b=int(random.randint(1,254))
#     timmy.speed(100)
#     timmy.color(r,g,b)
#     timmy.circle(50)
#     timmy.setheading(timmy.heading()+ang)
#     i+=ang
# myScreen.exitonclick()

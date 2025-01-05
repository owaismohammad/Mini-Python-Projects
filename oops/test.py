import turtle

# Create a screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Set the fastest drawing speed

# Function to draw a realistic tree
def draw_tree(x, y, trunk_length, trunk_width):
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Draw trunk
    t.color("saddlebrown")
    t.begin_fill()
    t.pensize(trunk_width)
    t.forward(trunk_length)
    t.left(90)
    t.forward(trunk_width * 2)
    t.left(90)
    t.forward(trunk_length)
    t.left(90)
    t.forward(trunk_width * 2)
    t.left(90)
    t.end_fill()

    # Draw leaves
    t.penup()
    t.goto(x, y + trunk_length)  # Move to the top of the trunk
    t.pendown()
    t.color("forestgreen")
    draw_branch(x, y + trunk_length, 70, 100)  # Draw a branch on the right
    draw_branch(x, y + trunk_length, 120, 100)  # Draw a branch on the left
    draw_branch(x, y + trunk_length, 180, 100)  # Draw a branch upward

# Function to draw a branch
def draw_branch(x, y, angle, length):
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()
    t.forward(length)
    t.setheading(angle + 20)
    t.forward(length * 0.8)
    t.setheading(angle - 20)
    t.forward(length * 0.8)
    t.setheading(angle)

# Draw a realistic tree
draw_tree(-100, -250, 150, 20)

# Hide turtle
t.hideturtle()

# Keep the window open
turtle.mainloop()

from turtle import Screen, Turtle
timmy=Turtle()

timmy.forward(50)


timmy.shape("turtle")
myScreen=Screen()
print(myScreen.canvheight)
timmy.color("CadetBlue")
myScreen.exitonclick()
from prettytable import PrettyTable
table=PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Bulbasaur"])
table.add_column("Pokemon Type",["Electric Type ", "Water Type ", "Grass Type"])
table.align='l'
print(table)
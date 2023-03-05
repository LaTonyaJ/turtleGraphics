import random
from turtle import Turtle, Screen

racing = False
colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow']
y_position = [-60, -30, 0, 30, 60, 90]
all_turtles = []

screen = Screen()
screen.setup(width=500, height=400)
choice = screen.textinput(title='Turtle Race', prompt='Make your bet. Choose a color: ')


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if choice:
    racing = True

while racing:
    for turtle in all_turtles:
        random_speed = random.randint(0, 10)
        turtle.fd(random_speed)
        if turtle.xcor() > 230:
            racing = False
            winning_turtle = turtle.pencolor()
            if choice == winning_turtle:
                print(f"You win! {winning_turtle} turtle is the winner")
            else:
                print(f"You lose. {winning_turtle} turtle is the winner")


screen.exitonclick()


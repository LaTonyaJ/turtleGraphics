import random
import turtle
from turtle import Turtle, Screen
from random import randint, choice

timmy = Turtle()
timmy.shape('turtle')

# Draw a square
# num = 0
# while num < 4:
#     timmy.fd(100)
#     timmy.left(90)
#     num += 1

# Draw a dotted line
# for num in range(50):
#     if num % 5 == 0:
#         timmy.color('blue')
#         timmy.pd()
#         timmy.fd(5)
#     timmy.pu()
#     timmy.fd(5)


# Draw diff shapes, start @ 3sides - 10sides
# 360 / num of sides = angle

# colors = ['red', 'orange', 'blue', 'green']
#
# for num in range(3, 11):
#     timmy.color(choice(colors))
#     for _ in range(num):
#         timmy.fd(100)
#         timmy.right(360/num)

# Random Walk

#
# def coin_flip():
#     turn = random.choice(['Left', 'Right'])
#     return turn
#
#
# def back_forth():
#     facing = random.choice(['fd', 'bk'])
#     return facing
#
#
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
#
#
# walking = True


turtle.colormode(255)
#
# for _ in range(250):
#     pick = coin_flip()
#     position = back_forth()
#     timmy.color(random_color())
#     timmy.pensize(15)
#     timmy.speed('fast')
#     if pick == 'Right':
#         timmy.right(90)
#     timmy.left(90)
#
#     if position == 'fd':
#         timmy.fd(30)
#     timmy.bk(30)

# Repeating Circle with random colors

timmy.speed(0)
current_position = timmy.heading()

while timmy.heading() != 355.0:
    timmy.circle(100)
    timmy.seth(current_position + 5)
    print(timmy.heading())
    timmy.color(random_color())
    timmy.circle(100)
    current_position = current_position + 5

screen = Screen()
screen.exitonclick()


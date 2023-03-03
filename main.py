from turtle import Turtle, Screen

tim = Turtle()


def move_forward():
    tim.fd(10)


def move_backward():
    tim.bk(10)


def move_counter():
    head = tim.heading()
    tim.seth(head - 10)


def move_clockwise():
    head = tim.heading()
    tim.seth(head + 10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen = Screen()
screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=move_counter)
screen.onkey(key='d', fun=move_clockwise)
screen.onkey(key='c', fun=clear_screen)
screen.exitonclick()


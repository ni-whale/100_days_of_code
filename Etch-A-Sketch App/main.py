from turtle import Turtle, Screen

leo = Turtle()
screen = Screen()

def move_forwards():
    leo.forward(10)


def move_backwards():
    leo.backward(10)


def counter_clockwise():
    leo.left(10)


def clockwise():
    leo.right(10)


def clear_drawing():
    leo.home()
    leo.clear()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=clear_drawing)


screen.exitonclick()

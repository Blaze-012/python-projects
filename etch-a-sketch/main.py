import turtle as t

tim = t.Turtle()
screen = t.Screen()

screen.listen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear():
    tim.reset()


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=turn_left)
screen.onkey(key="c", fun=clear)
screen.exitonclick()

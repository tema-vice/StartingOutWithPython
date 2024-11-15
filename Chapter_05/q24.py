# Exercise 24
import turtle as t

def main():
    width = int(input("Enter the width: "))
    length = int(input("Enter the length: "))
    t.hideturtle()
    drawPattern(width, length)
    t.exitonclick()


def drawPattern(width, length):
    t.pensize(2)
    for n in range(2):
        t.forward(width)
        t.left(90)
        t.forward(length)
        t.left(90)

    t.forward(width / 2)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(width / 2)
    t.left(90)
    t.forward(length / 2)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(length / 2)
    t.goto(0, 0)

    t.goto(0, length)
    t.goto(width, 0)
    t.penup()
    t.goto(width / 8, length / 8)
    t.pendown()

    for n in range(2):
        t.forward(length * (6 / 8))
        t.right(90)
        t.forward(width * (6 / 8))
        t.right(90)

    t.goto(width / 2, length / 8)
    t.goto(width / 2, length / 4)
    t.right(90)
    t.fillcolor('black')
    t.begin_fill()
    t.forward(width / 4)
    for n in range(2):
        t.left(90)
        t.forward(length / 2)
        t.left(90)
        t.forward(width / 2)
    t.end_fill()


main()

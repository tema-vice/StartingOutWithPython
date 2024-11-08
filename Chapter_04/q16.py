# Exercise 16
import turtle as t
ANGLE = 0
WIDTH = 5

t.hideturtle()
t.penup()
t.goto(200, -200)
t.pendown()
t.speed(0)
for square in range(100):
    for width in range(4):
        ANGLE += 90
        t.setheading(ANGLE)
        t.forward(WIDTH)
    WIDTH += 5
t.exitonclick()
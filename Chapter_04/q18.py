# Exercise 18
import turtle as t
ANGLE = 90
LENGTH = 4

t.hideturtle()
t.speed(0)
t.setheading(ANGLE)
for line in range(49):
    t.forward(LENGTH)
    t.left(ANGLE)
    LENGTH += 4
t.exitonclick()

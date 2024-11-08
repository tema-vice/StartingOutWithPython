# Exercise 17
import turtle as t
ANGLE = 135
LENGTH = 200

t.hideturtle()
t.setheading(90)
for line in range(8):
    t.forward(LENGTH)
    t.left(ANGLE)
t.exitonclick()

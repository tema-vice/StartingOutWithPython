# Exercise 19
import turtle as t
LENGTH = 40
ANGLE = 45

t.penup()
t.forward(-12)
t.pendown()
t.write("STOP")
t.penup()
t.goto(47,-15)
t.pendown()
t.setheading(90)
for line in range(8):
    t.forward(LENGTH)
    t.left(ANGLE)
t.exitonclick()

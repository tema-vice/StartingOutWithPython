# Exercise 15
import turtle as t
t.pensize(2)
t.fillcolor('black')
t.begin_fill()
t.goto(100,100)
t.goto(200,0)
t.goto(100,-100)
t.goto(0,0)
t.goto(-100,100)
t.goto(-200,0)
t.goto(-100,-100)
t.goto(0,0)
t.end_fill()
t.clear()

t.goto(100,0)
t.goto(0,250)
t.goto(-100,0)
t.goto(0,0)
t.begin_fill()
t.goto(100,0)
t.goto(0,125)
t.goto(-100,0)
t.goto(0,0)
t.end_fill()
t.clear()

t.goto(-100,100)
t.goto(-100,0)
t.goto(0,-100)
t.goto(100,-100)
t.goto(100,0)
t.goto(0,100)
t.goto(-100,100)
t.goto(100,-100)
t.goto(0,-100)
t.goto(0,0)
t.goto(100,0)
t.goto(0,0)
t.goto(0,100)
t.goto(0,0)
t.goto(-100,0)
t.goto(0,0)
t.clear()

t.penup()
t.goto(-200,0)
t.pendown()
t.circle(50)
t.penup()
t.goto(-143.75,-50)
t.pendown()
t.circle(50)
t.penup()
t.goto(-87.5,0)
t.pendown()
t.circle(50)
t.penup()
t.goto(-31.25,-50)
t.pendown()
t.circle(50)
t.penup()
t.goto(25,0)
t.pendown()
t.circle(50)
t.penup()
t.goto(0,0)
t.pendown()
t.clear()

t.goto(0,100)
t.write("North")
t.goto(0,-100)
t.write("South")
t.goto(0,-25)
t.circle(25)
t.goto(0,0)
t.goto(-100,0)
t.write("West")
t.goto(100,0)
t.write("East")
t.goto(0,0)
t.clear()

t.dot()
t.goto(200,200)
t.dot()
t.goto(-200,-200)
t.dot()
t.goto(-200,200)
t.dot()
t.goto(200,-200)
t.dot()
t.goto(200,200)
t.goto(200,-200)
t.goto(175,-200)
t.penup()
t.goto(125,-200)
t.pendown()
t.goto(25,-200)
t.penup()
t.goto(-25,-200)
t.pendown()
t.goto(-125,-200)
t.penup()
t.goto(-175,-200)
t.pendown()
t.goto(-200,-200)
t.goto(200,200)
t.goto(175,200)
t.penup()
t.goto(125,200)
t.pendown()
t.goto(25,200)
t.penup()
t.goto(-25,200)
t.pendown()
t.goto(-125,200)
t.penup()
t.goto(-175,200)
t.pendown()
t.goto(-200,200)
t.goto(0,0)
t.exitonclick()
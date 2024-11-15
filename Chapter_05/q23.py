# Exercise 23
import turtle as t

def main():
    drawBase()
    drawMidSection()
    drawArms()
    drawHead()
    drawHat()
    t.exitonclick()


def drawBase():
    t.pensize(2)
    t.hideturtle()
    t.circle(50)


def drawMidSection():
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.circle(40)


def drawArms():
    t.penup()
    t.goto(40, 140)
    t.pendown()
    t.goto(80, 170)
    t.goto(90, 190)
    t.goto(80, 170)
    t.goto(84,160)
    t.penup()
    t.goto(-40, 140)
    t.pendown()
    t.goto(-80, 160)
    t.goto(-90,175)
    t.goto(-100,185)
    t.goto(-90, 175)
    t.goto(-70,182)


def drawHead():
    t.penup()
    t.goto(0, 180)
    t.pendown()
    t.circle(30)
    t.penup()
    t.goto(-10, 210)
    t.pendown()
    t.circle(5)
    t.penup()
    t.goto(10, 210)
    t.pendown()
    t.circle(5)
    t.penup()
    t.goto(-15,195)
    t.pendown()
    t.goto(15, 195)


def drawHat():
    t.penup()
    t.goto(0,225)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.forward(40)
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(30)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(40)
    t.end_fill()
main()

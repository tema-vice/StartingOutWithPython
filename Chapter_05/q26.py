# Exercise 26
import turtle as t
import random as r

START_X = -250
START_Y = -250
WIDTH = 500

def main():
    t.hideturtle()
    t.speed(0)
    square(START_X,START_Y, 500, 'black')
    home()
    square(START_X + 220, START_Y + 300, 15, 'yellow')
    square(START_X + 220, START_Y + 280, 15, 'yellow')
    square(START_X + 170, START_Y + 310, 15, 'yellow')
    square(START_X + 195, START_Y + 330, 15, 'yellow')
    square(START_X + 50, START_Y + 110, 15, 'yellow')
    square(START_X + 100, START_Y + 180, 15, 'yellow')
    square(START_X + 330, START_Y + 220, 15, 'yellow')
    square(START_X + 350, START_Y + 260, 15, 'yellow')
    star()
    t.exitonclick()

def home():
    t.fillcolor("gray")
    t.begin_fill()
    t.goto(START_X, START_Y + 150)
    t.goto(START_X + 80, START_Y + 150)
    t.goto(START_X + 80, START_Y + 250)
    t.goto(START_X + 150, START_Y + 250)
    t.goto(START_X + 150, START_Y + 370)
    t.goto(START_X + 260, START_Y + 370)
    t.goto(START_X + 260, START_Y + 200)
    t.goto(START_X + 320, START_Y + 200)
    t.goto(START_X + 320, START_Y + 295)
    t.goto(START_X + 400, START_Y + 295)
    t.goto(START_X + 400, START_Y + 210)
    t.goto(START_X + 420, START_Y + 210)
    t.goto(START_X + 420, START_Y + 180)
    t.goto(START_X + WIDTH, START_Y + 180)
    t.goto(START_X + WIDTH, START_Y)
    t.goto(START_X, START_Y)
    t.end_fill()

def square(x, y, width, color):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for count in range(4):
        t.forward(width)
        t.left(90)
    t.end_fill()

def star():
    for i in range(6):
        cor_x = r.randint(-240,240)
        cor_y = r.randint(125, 240)
        square(cor_x, cor_y,4, 'white')
    for i in range(2):
        cor_x = r.randint(-240,-100)
        cor_y = r.randint(0,120)
        square(cor_x, cor_y, 4, 'white')
    for i in range(3):
        cor_x = r.randint(10,240)
        cor_y = r.randint(50,130)
        square(cor_x, cor_y, 4, 'white')
main()

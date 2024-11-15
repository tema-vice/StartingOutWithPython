# Exercise 25
import turtle as t

BLACK = 'black'
WHITE = 'white'

def main():
    width = int(input("Enter the width: "))
    while width < 1:
        print("Invalid value.")
        width = int(input("Please enter a valid value: "))
    t.hideturtle()
    t.speed(0)
    cor_y = 0
    for n in range(3):
        cor_x = 0
        square(cor_x, cor_y, width, BLACK)
        for n in range(2):
            cor_x += width
            square(cor_x,cor_y, width, WHITE)
            cor_x += width
            square(cor_x, cor_y,width,BLACK)
        cor_x = 0
        cor_y += width
        if (cor_y >= (width * 5)):
            break
        square(cor_x, cor_y, width, WHITE)
        for n in range(2):
            cor_x += width
            square(cor_x, cor_y, width, BLACK)
            cor_x += width
            square(cor_x, cor_y, width, WHITE)
        cor_y += width
    t.exitonclick()

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

main()
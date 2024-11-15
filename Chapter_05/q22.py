# Exercise 22
import turtle

def main():
    color = input("Enter the triangle's color: ")
    x_1, y_1 = get_angle_1()
    print()
    x_2, y_2 = get_angle_2()
    print()
    x_3, y_3 = get_angle_3()

    triangle(x_1, x_2, x_3, y_1, y_2, y_3, color)

def get_angle_1():
    x_1 = int(input("Enter the x-coordinate for vertex 1 of the triangle: "))
    y_1 = int(input("Enter the y-coordinate for vertex 1 of the triangle: "))
    return x_1, y_1

def get_angle_2():
    x_2 = int(input("Enter the x-coordinate for vertex 2 of the triangle: "))
    y_2 = int(input("Enter the y-coordinate for vertex 2 of the triangle: "))
    return x_2, y_2

def get_angle_3():
    x_3 = int(input("Enter the x-coordinate for vertex 3 of the triangle: "))
    y_3 = int(input("Enter the y-coordinate for vertex 3 of the triangle: "))
    return x_3, y_3

def triangle(x_1, x_2, x_3, y_1, y_2, y_3, color):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x_1, y_1)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(x_2, y_2)
    turtle.goto(x_3, y_3)
    turtle.goto(x_1, y_1)
    turtle.end_fill()
    turtle.exitonclick()

main()

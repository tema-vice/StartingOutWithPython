# Exercise 19
import turtle as t
# TARGET_LLEFT_X = 100
# TARGET_LLEFT_Y = 250
TARGET_WIDTH = 10
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

# Random target position generation
import random

TARGET_LLEFT_X = random.randint(0, 200)
TARGET_LLEFT_Y = random.randint(0, 200)


level = int(input("Enter game difficulty (difficulty multiplies target size by x):\n"))

TARGET_WIDTH = TARGET_WIDTH * level

# Create target
t.hideturtle()
t.speed(0)
t.penup()
t.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
t.pendown()
t.forward(TARGET_WIDTH)  # Draw the top side of the square target
t.setheading(NORTH)
t.forward(TARGET_WIDTH)  # Draw the right side of the square target
t.setheading(WEST)
t.forward(TARGET_WIDTH)  # Draw the bottom side of the square target
t.setheading(SOUTH)
t.forward(TARGET_WIDTH)  # Draw the left side of the square target
t.setheading(EAST)
t.penup()

# Move turtle to the center and prepare for shooting
t.goto(0, 0)
t.showturtle()
t.pendown()
t.speed(PROJECTILE_SPEED)

# Get user input for angle and force
angle = float(input("Enter the angle of projection:\n"))
force = float(input("Enter the launch force (Arrow step is 30 pixels):\n"))
distance = force * FORCE_FACTOR  # Calculate the distance to move based on force

# Launch the projectile
t.dot()
t.setheading(angle)
t.forward(distance)

# Hints for the user
TARGET_LLEFT_UP_Y = TARGET_LLEFT_Y + TARGET_WIDTH  # Upper-left Y coordinate of the target
TARGET_RRIGHT_X = TARGET_LLEFT_X + TARGET_WIDTH  # Lower-right X coordinate of the target

# Calculate the ideal angle range
import math

ANGLE_LEFT_A = math.degrees(math.atan(TARGET_LLEFT_UP_Y / TARGET_LLEFT_X))  # Left boundary of the ideal angle
ANGLE_RIGHT_A = math.degrees(math.atan(TARGET_LLEFT_Y / TARGET_RRIGHT_X))  # Right boundary of the ideal angle

# Check if the projectile hits the target
if (t.xcor() >= TARGET_LLEFT_X and t.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH)) and \
        (t.ycor() >= TARGET_LLEFT_Y and t.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print("You hit the target!")
else:
    print("Missed!\nHINTS:")

    # Check the angle
    if angle > ANGLE_LEFT_A:  # If the user's angle is too large
        print("Try a smaller angle.")
    elif angle < ANGLE_RIGHT_A:  # If the user's angle is too small
        print("Try a larger angle.")
    elif (angle <= ANGLE_LEFT_A) and (angle >= ANGLE_RIGHT_A):  # If the angle is correct
        print("The angle is correct.")

    # Check the force
    if (angle <= ANGLE_LEFT_A) and (angle >= ANGLE_RIGHT_A) and (t.ycor() < TARGET_LLEFT_Y):  # If the turtle is too low
        print("Try adding more force.")
    elif (angle <= ANGLE_LEFT_A) and (angle >= ANGLE_RIGHT_A) and (
            t.ycor() > TARGET_LLEFT_UP_Y):  # If the turtle is too high
        print("Try reducing the force.")

# Wait for a click to exit
t.exitonclick()

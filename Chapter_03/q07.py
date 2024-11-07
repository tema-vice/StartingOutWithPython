# Exercise 7
# Constants for primary colors
RED = "Red"
BLUE = "Blue"
YELLOW = "Yellow"

print(f"Primary colors: {RED}, {BLUE}, {YELLOW}")

color_1 = input("Enter a primary color to mix: ")
color_2 = input("Enter another primary color to mix: ")

if ((color_1 != RED and color_1 != BLUE and color_1 != YELLOW) or
        (color_2 != RED and color_2 != BLUE and color_2 != YELLOW)):
    print("The color entered is invalid.")
else:
    if color_1 == color_2:
        print(f"{color_1} + {color_2} = {color_1}.")
    elif (color_1 == RED and color_2 == BLUE) or (color_2 == RED and color_1 == BLUE):
        print(f"{color_1} + {color_2} = Purple.")
    elif (color_1 == RED and color_2 == YELLOW) or (color_2 == RED and color_1 == YELLOW):
        print(f"{color_1} + {color_2} = Orange.")
    elif (color_1 == BLUE and color_2 == YELLOW) or (color_2 == BLUE and color_1 == YELLOW):
        print(f"{color_1} + {color_2} = Green.")
# Exercise 2
length_1 = float(input("Enter the length of rectangle 1:\n"))
width_1 = float(input("Enter the width of rectangle 1:\n"))
length_2 = float(input("Enter the length of rectangle 2:\n"))
width_2 = float(input("Enter the width of rectangle 2:\n"))

if (length_1 * width_1) > (length_2 * width_2):
    print("Rectangle 1 is larger!")
elif (length_1 * width_1) < (length_2 * width_2):
    print("Rectangle 2 is larger!")
else:
    print("The rectangles are equal in size!")

# Exercise 14
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))


# Calculate the Body Mass Index (BMI).
bmi = weight / (height ** 2)

# Check if the input data is valid.
if bmi < 1:
    print("The entered data is incorrect.")
elif bmi < 18.5:
    print(f"Your BMI = {bmi:.1f} - Underweight.")
elif bmi < 25:
    print(f"Your BMI = {bmi:.1f} - Normal weight.")
else:
    print(f"Your BMI = {bmi:.1f} - Overweight.")

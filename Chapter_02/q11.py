# Exercise 11
men = int(input("Enter the number of men: "))
women = int(input("Enter the number of women: "))

print(f"Percentage of men: {men / (men + women):.1%}")
print(f"Percentage of women: {women / (men + women):.1%}")

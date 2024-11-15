# Exercise 12
def main():
    num_1 = int(input("Number 1: "))
    num_2 = int(input("Number 2: "))
    max(num_1, num_2)

def max(num_1, num_2):
    if num_1 > num_2:
        print(num_1)
    elif num_1 < num_2:
        print(num_2)
    else:
        print("The numbers are equal.")

main()
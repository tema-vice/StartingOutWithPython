# Exercise 15
A = 100
B = 90
C = 80
D = 70
F = 60
MIN_POINT = 0

def main():
    print("This program calculates the average score and determines grade levels.")
    calc_average()

def calc_average():
    total = 0
    for count in range(5):
        print(f"Enter the grade for subject {count + 1}: ", end="")
        point = int(input())
        while point < MIN_POINT or point > A:
            print("Grade must be between 0 and 100.")
            point = int(input("Please enter again: "))
        # Add valid grade to total
        total += point
        determine_grade(point)

    print()
    print(f"Total score: {total}")
    print(f"Average score: {total / 5:.1f}")


def determine_grade(point):
    if point <= A and point >= B:
        print(f"Score {point} corresponds to grade A")
    elif point < B and point >= C:
        print(f"Score {point} corresponds to grade B")
    elif point < C and point >= D:
        print(f"Score {point} corresponds to grade C")
    elif point < D and point >= F:
        print(f"Score {point} corresponds to grade D")
    else:
        print(f"Score {point} corresponds to grade F")

main()

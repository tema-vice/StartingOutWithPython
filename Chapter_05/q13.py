# Exercise 13
G = 9.8

def main():
    print("d = 1/2*g*t^2")
    for t in range(10):
        print(falling_distance(t+1))

def falling_distance(t):
    d = (1/2) * G * t**2
    return f"Second {t}\nThe distance is: {d:.2f} m."
main()

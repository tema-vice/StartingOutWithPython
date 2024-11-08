# Exercise 4
speed = float(input("Enter speed in km/h: "))
while speed < 0:
    print("Speed must be greater than zero")
    speed = float(input("Enter speed in km/h: "))

time = int(input("Enter the number of hours: "))
while time < 0:
    print("Time must be greater than zero")
    time = int(input("Enter the number of hours: "))

print("Hour\t\tDistance traveled")
print("--------------------------------")
for num in range(time):
    print(f"{num + 1}\t\t\t{speed * (num + 1)}")

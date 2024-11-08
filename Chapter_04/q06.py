# Exercise 6
print("Celsius\tFahrenheit")

for celsius in range(0, 21):
    fahrenheit = ((9 / 5) * celsius) + 32
    print(f"{celsius}\t{fahrenheit:.1f}")
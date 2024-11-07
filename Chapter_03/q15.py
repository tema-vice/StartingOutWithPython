# Exercise 15
sek = int(input("Enter the number of seconds: "))

if sek < 0:
    print("Incorrect input")

elif sek >= 86400:
    print(f"In {sek} seconds:")
    print(f"Days: {sek // 86400:.0f}")
    print(f"Hours: {(sek % 86400) // 3600:.0f}")
    print(f"Minutes: {(sek % 3600) // 60:.0f}")
    print(f"Seconds: {sek % 60:.0f}")

elif sek >= 3600:
    print(f"In {sek} seconds:")
    print(f"Hours: {sek // 3600:.0f}")
    print(f"Minutes: {(sek % 3600) // 60:.0f}")
    print(f"Seconds: {sek % 60:.0f}")

elif sek >= 60:
    print(f"In {sek} seconds:")
    print(f"Minutes: {sek // 60:.0f}")
    print(f"Seconds: {sek % 60:.0f}")

else:
    print(f"In {sek} seconds:")
    print(f"Seconds: {sek:.0f}")

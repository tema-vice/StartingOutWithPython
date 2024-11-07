# Exercise 10
COIN_5 = 0.05
COIN_10 = 0.1
COIN_50 = 0.5

coin_5 = int(input("Enter the number of 5 kopeck coins: "))
coin_10 = int(input("Enter the number of 10 kopeck coins: "))
coin_50 = int(input("Enter the number of 50 kopeck coins: "))

if coin_5 >= 0 and coin_10 >= 0 and coin_50 >= 0:
    # Calculate the total amount in rubles
    rubles = (coin_5 * COIN_5) + (coin_10 * COIN_10) + (coin_50 * COIN_50)

    # Check if the total amount equals 1 ruble
    if rubles == 1:
        print("Congratulations, you won!")
    else:
        print("You lost...")
else:
    print("Please enter a positive number!")
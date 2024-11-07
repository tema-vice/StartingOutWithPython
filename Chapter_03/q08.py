# Exercise 8
MEET = 10  # Sausages per pack
BREAD = 8  # Buns per pack

people = int(input("Enter the number of people attending the picnic: "))
hot_dog = int(input("Enter the number of hot dogs each person will receive: "))

if people > 0 and hot_dog > 0 :
    # Calculate total hot dogs needed
    people_hot_dog = people * hot_dog

    # Calculate the minimum number of packs required for sausages and buns
    min_meet = people_hot_dog // MEET  # Minimum packs of sausages
    min_bread = people_hot_dog // BREAD  # Minimum packs of buns

    if min_meet < (people_hot_dog / MEET):
        min_meet += 1
    if min_bread < (people_hot_dog / BREAD):
        min_bread += 1

    print(f"Minimum number of sausage packs needed: {min_meet}")
    print(f"Minimum number of bun packs needed: {min_bread}")
    print(f"Remaining sausages: {(min_meet * MEET) - people_hot_dog}")
    print(f"Remaining buns: {(min_bread * BREAD) - people_hot_dog}")

else:
    print("Please enter a positive integer")
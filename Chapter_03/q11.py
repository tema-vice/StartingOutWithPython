# Exercise 11
book = int(input("Enter the number of books you bought this month: "))

if book >= 8:
    print(f"You bought {book} book(s). You are awarded 60 points!")
elif book >= 6:
    print(f"You bought {book} book(s). You are awarded 30 points!")
elif book >= 4:
    print(f"You bought {book} book(s). You are awarded 15 points!")
elif book >= 2:
    print(f"You bought {book} book(s). You are awarded 5 points!")
elif book >= 0:
    print(f"You bought {book} book(s). You are awarded 0 points...")
else:
    print("Looks like you didn't buy any books.\nThat's bad...")
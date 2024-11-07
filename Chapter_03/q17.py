# Exercise 17
print("Please answer either \"Yes\" or \"No\".")

answer = input("Are you having issues with Wi-Fi?\n")

# Check if the input is valid ("Yes" or "No").
if answer != "Yes" and answer != "No":
    print("Invalid input. Error.")
else:
    if answer == "Yes":
        print("Restart your computer and try reconnecting.")
        answer = input("Did this fix the issue?\n")
        if answer == "No":
            print("Restart your router and try reconnecting.")
            answer = input("Did this fix the issue?\n")
            if answer == "No":
                print("Ensure all cables between the router and modem are securely connected.")
                answer = input("Did this fix the issue?\n")
                if answer == "No":
                    print("Move the router to a new location.")
                    answer = input("Did this fix the issue?\n")
                    if answer == "No":
                        print("Consider getting a new router.")
    print("Have a nice day!")


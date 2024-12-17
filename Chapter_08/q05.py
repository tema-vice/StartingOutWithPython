# Exercise 5
def main():
    print("Program for converting phone numbers.")
    new_number = get_user_number()
    print(f"Formatted number: {new_number}")

def get_user_number():
    while True:
        user_number = input("Enter the phone number in the format XXX-XXX-XXXX\n^: ")
        if len(user_number) != len('XXX-XXX-XXXX'):
            print("The length of the number is incorrect.")
        elif (not user_number[:3].isalnum()) or (not user_number[4:7].isalnum()) or (not user_number[8:].isalnum()):
            print("The number contains invalid characters.")
        elif (user_number[3] != '-') or (user_number[7] != "-"):
            print("The separator is incorrect.")
        else:
            number_result = translate_char_for_num(user_number)
            return number_result

def translate_char_for_num(user_number):
    user_number = user_number.upper()
    for ch in user_number:
        if ch in ('A', 'B', 'C'):
            user_number = user_number.replace(ch, "2")
        elif ch in ('D', 'E', 'F'):
            user_number = user_number.replace(ch, "3")
        elif ch in ('G', 'H', 'I'):
            user_number = user_number.replace(ch, "4")
        elif ch in ('J', 'K', 'L'):
            user_number = user_number.replace(ch, "5")
        elif ch in ('M', 'N', 'O'):
            user_number = user_number.replace(ch, "6")
        elif ch in ('P', 'Q', 'R', 'S'):
            user_number = user_number.replace(ch, "7")
        elif ch in ('T', 'U', 'V'):
            user_number = user_number.replace(ch, "8")
        elif ch in ('W', 'X', 'Y', 'Z'):
            user_number = user_number.replace(ch, "9")
    return user_number

main()

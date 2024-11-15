# Exercise 7
# Ticket prices
CLASS_A = 20
CLASS_B = 15
CLASS_C = 10


def main():

    ticket_a = int(input("How many Class A tickets were sold? "))
    while ticket_a < 0:
        ticket_a = int(input("The number of tickets cannot be negative: "))

    ticket_b = int(input("How many Class B tickets were sold? "))
    while ticket_b < 0:
        ticket_b = int(input("The number of tickets cannot be negative: "))

    ticket_c = int(input("How many Class C tickets were sold? "))
    while ticket_c < 0:
        ticket_c = int(input("The number of tickets cannot be negative: "))

    print(ticket_price(ticket_a, ticket_b, ticket_c))


def ticket_price(a, b, c):
    price_a = a * CLASS_A
    price_b = b * CLASS_B
    price_c = c * CLASS_C
    return f"The total revenue from ticket sales: {price_a + price_b + price_c:,.2f}"

main()
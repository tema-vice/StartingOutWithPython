# Exercise 9
import random

def main():
    deck = create_deck()
    deal_cards(deck)

def create_deck():
    deck = {'Ace of Spades': 1, '2 of Spades': 2, '3 of Spades': 3,
            '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6,
            '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9,
            '10 of Spades': 10, 'Jack of Spades': 10,
            'Queen of Spades': 10, 'King of Spades': 10,
            'Ace of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3,
            '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6,
            '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9,
            '10 of Hearts': 10, 'Jack of Hearts': 10,
            'Queen of Hearts': 10, 'King of Hearts': 10,
            'Ace of Clubs': 1, '2 of Clubs': 2, '3 of Clubs': 3,
            '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6,
            '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9,
            '10 of Clubs': 10, 'Jack of Clubs': 10,
            'Queen of Clubs': 10, 'King of Clubs': 10,
            'Ace of Diamonds': 1, '2 of Diamonds': 2, '3 of Diamonds': 3,
            '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6,
            '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9,
            '10 of Diamonds': 10, 'Jack of Diamonds': 10,
            'Queen of Diamonds': 10, 'King of Diamonds': 10}
    return deck


def deal_cards(deck):
    while len(deck) != 0:
        players = [[], []]
        while (sum(players[0]) < 22) and (sum(players[1]) < 22) and len(deck) != 0:
            for player_hand in players:
                if len(deck) == 0:
                    break
                drawn_card = random.choice(list(deck))
                if (deck[drawn_card] == 1) and (sum(player_hand) < 11):
                    player_hand.append(deck[drawn_card] + 10)
                else:
                    player_hand.append(deck[drawn_card])
                del deck[drawn_card]

        print()
        if (sum(players[0]) > 21) and (sum(players[1]) > 21):
            print("No winner!")
        elif (sum(players[0]) == 21) and (sum(players[1]) == 21):
            print("It's a tie!")
        elif sum(players[0]) > 21:
            print("Player 2 wins!")
        elif sum(players[1]) > 21:
            print("Player 1 wins!")
        elif sum(players[0]) < sum(players[1]):
            print("Player 1 wins!")
        elif sum(players[1]) < sum(players[0]):
            print("Player 2 wins!")
        elif sum(players[0]) == sum(players[1]):
            print("It's a tie!")
        print("Players' statistics:")
        print(f"Player 1: {sum(players[0])} - {players[0]}")
        print(f"Player 2: {sum(players[1])} - {players[1]}")
        # Debugging deck state
        # print(deck)
        # print(len(deck))

main()

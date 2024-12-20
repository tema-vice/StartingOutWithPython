# Exercise 7
def main():
    world_series_winners = {}
    year = 1903
    file = open('WorldSeriesWinners.txt', 'r')
    for line in file:
        world_series_winners[year] = line.rstrip('\n')
        year += 1
    file.close()
    while True:
        try:
            user_string = int(input("Enter a year (1903-2009) to find the winner: "))
            count_win = 0
            if user_string == 1904 or user_string == 1994:
                print(f"The World Series was not held in {user_string}.")
            elif user_string < 1903 or user_string > 2009:
                print("Information is available only for the period 1903-2009.")
            else:
                team = world_series_winners[user_string]
                # Count the total wins for this team
                for key, value in world_series_winners.items():
                    if value == team:
                        count_win += 1
                print(f"The team that won in {user_string}: {world_series_winners[user_string]}")
                print(f"Total World Series wins for this team: {count_win}")

            again = input("Continue searching? (y/n)\n^: ")
            if again.lower() != 'y':
                break

        except Exception:
            print("Input error. Please enter the year again.")


main()


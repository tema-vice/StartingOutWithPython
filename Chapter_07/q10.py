# Exercise 10
def main():
    team_name_list = get_list()
    count = 0
    user_team_name = input("Enter the name of the team you are looking for (e.g., 'New York Yankees'): ")
    for team_name in team_name_list:
        if team_name == user_team_name:
            count += 1

    if count != 0:
        print(f"{user_team_name} won {count} times between 1903 and 2009.")
    else:
        print(f"This team never won.")


def get_list():
    winners_teem_file = None
    list = []
    try:
        winners_teem_file = open('WorldSeriesWinners.txt', 'r')
        for teem in winners_teem_file:
            list.append(teem.rstrip("\n"))
    except Exception as error:
        print(error)
    finally:
        if winners_teem_file != None:
            winners_teem_file.close()
        return list
main()

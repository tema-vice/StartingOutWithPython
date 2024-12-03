# Exercise 15
import matplotlib.pyplot as plt
def main():
    data_list = []
    get_list(data_list)
    year = []
    for i in range(1, 53):
        year.append(i)
    plt.bar(year, data_list)
    plt.title('Gasoline Price Growth in 1998')
    plt.ylabel("Price")
    plt.xlabel("Week")
    plt.show()

def get_list(list):
    fuel_file = open('1994_Weekly_Gas_Averages.txt', 'r')
    for line in fuel_file:
        list.append(float(line.rstrip('\n')))
    fuel_file.close()

main()

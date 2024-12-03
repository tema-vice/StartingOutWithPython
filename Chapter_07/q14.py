# Exercise 14
import matplotlib.pyplot as plt
def main():
    data_list = []
    create_list(data_list)
    labels_name = ['Rent', 'Gasoline', 'Food', 'Clothing', 'Car Payments', 'Other']
    plt.pie(data_list, labels = labels_name)
    plt.show()


def create_list(list):
    data_file = open('data_about_spend.txt', 'r')
    for line in data_file:
        list.append(int(line.rstrip('\n')))
    data_file.close()

main()

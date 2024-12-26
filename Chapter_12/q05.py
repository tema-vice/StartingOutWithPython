# Exercise 5
def main():
    list = [0, 1, 3, 5, 2, 4, 0]
    print(f"Result: {recursive_func(list)}")

def recursive_func(list):
    if len(list) == 1:
        return list[0]
    else:
        list[0] += list[len(list) - 1]
        list.remove(list[len(list) - 1])
        return recursive_func(list)

main()

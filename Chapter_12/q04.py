# Exercise 4
def main():
    list = [0, 1, 3, 5, 2, 4, 0]
    print(f"Result: {recursive_func(list)}")

def recursive_func(list):
    if len(list) == 1:
        return list[0]
    else:
        list.remove(min(list))
        return recursive_func(list)

main()

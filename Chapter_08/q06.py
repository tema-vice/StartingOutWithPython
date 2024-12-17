# Exercise 6
def main():
    text_tuple = get_tuple()
    index = 0
    total_counter = 0
    while index < len(text_tuple):
        total_list = text_tuple[index].split()
        total_counter += len(total_list)
        index += 1
    print(f"On average, there are {total_counter / len(text_tuple):.1f} words per {len(text_tuple)} sentences.")

def get_tuple():
    text_file = open('text.txt', 'r')
    lines = text_file.readlines()
    text_file.close()
    index = 0
    while index < len(lines):
        lines[index] = lines[index].rstrip('\n')
        index += 1
    lines = tuple(lines)
    return lines

main()


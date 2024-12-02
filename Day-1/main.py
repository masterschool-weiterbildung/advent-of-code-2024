from pathlib import Path

import my_util


def main():
    FILE_PATH = "text.txt"

    str_output = my_util.load_data(FILE_PATH)

    # part_one(str_output)

    list_one = []
    list_two = []
    for val in str_output:
        lst = val.split();
        list_one.append(lst[0])
        list_two.append(lst[1])

    print(list_one, list_two)

    total = 0
    for count in range(len(list_one)):
        total = total + (list_two.count(list_one[count]) *  int(list_one[count]))
    print(total)


def part_one(str_output):
    list_one_sorted, list_two_sorted = get_sorted_list(str_output)

    total = 0
    for count in range(len(list_one_sorted)):
        total += abs(
            int(list_one_sorted[count]) - int(list_two_sorted[count]))
    print(total)


def get_sorted_list(str_output):
    list_one = []
    list_two = []
    for val in str_output:
        lst = val.split();
        list_one.append(lst[0])
        list_two.append(lst[1])
    list_one_sorted = sorted(list_one)
    list_two_sorted = sorted(list_two)
    return list_one_sorted, list_two_sorted


if __name__ == '__main__':
    main()

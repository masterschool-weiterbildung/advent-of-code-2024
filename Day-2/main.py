import my_util


def main():
    FILE_PATH = "text.txt"

    str_output = my_util.load_data(FILE_PATH)

    val_split = []

    for val in str_output:
        val_split.append(str(val).split());

    count = 0

    for val in val_split:
        comparisons = [my_util.is_true(val[i], val[i + 1])
                       for i in range(len(val) - 1)]

        if all(comparisons) and my_util.is_increasing_or_decreasing(val):
            count += 1

        print(count)


if __name__ == '__main__':
    main()

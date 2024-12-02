import my_util


def main():
    FILE_PATH = "text.txt"

    str_output = my_util.load_data(FILE_PATH)

    val_split = []

    for val in str_output:
        val_split.append(str(val).split());

    count = 0

    for val in val_split:
        comparisons = my_util.is_safe(val)

        if all(comparisons) and my_util.is_increasing_or_decreasing(val):
            count += 1
        else:
            for i in range(len(val)):

                modified_report = val[:i] + val[i + 1:]

                comparisons = my_util.is_safe(modified_report)

                if all(comparisons) and my_util.is_increasing_or_decreasing(
                        modified_report):
                    count += 1
                    break
    print(count)


if __name__ == '__main__':
    main()

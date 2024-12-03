import re

import my_util


def main():
    FILE_PATH = "text.txt"

    str_output = my_util.read_all(FILE_PATH)

    matches = re.findall(r'(?:mul)\([0-9]{1,3}\,[0-9]{1,3}\)', str_output)

    multiply_all = 0

    for match in matches:
        numbers = re.findall(r'\d+', match)

        print(match)

        num1, num2 = map(int, numbers)

        result_mul = num1 * num2

        multiply_all += result_mul

    print(multiply_all)


if __name__ == '__main__':
    main()

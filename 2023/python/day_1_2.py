"""
Your calculation isn't quite right. It looks like some of the digits are actually
spelled out with letters: one, two, three, four, five, six, seven, eight,
and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line.

For example:
```txt
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
```

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76.
Adding these together produces 281.

What is the sum of all of the calibration values?
"""

from typing import List


def get_list_from_txt(file_path: str) -> List:
    """
    Read the data from the file and return a list.

    Args:
        file_path: Path to the file

    Returns:
        List of data from the file
    """
    data_list: List = []
    with open(file_path, "r") as r_file:
        for line in r_file:
            data_list.append(line.strip())
    return data_list


def word_to_number(data: str) -> List[str]:
    """
    Convert number words to digits.

    This is a bit ugly but it works.

    Args:
        data: String containing the data

    Returns:
        List of digits
    """
    number_mapping = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    data = data.lower().strip()
    found_values = []
    i = 0

    while i < len(data):
        # Check for digits first (more efficient)
        if data[i].isdigit():
            found_values.append(data[i])
            i += 1
            continue

        # Check for number words
        found_word = False
        for word, number in number_mapping.items():
            if data[i:].startswith(word):
                found_values.append(number)
                found_word = True
                break

        i += 1 if not found_word else 1

    return found_values


def get_first_and_last(data: List[str]) -> int:
    """
    Get the first and last digits of a list and return the two-digit number.

    Args:
        data: List containing the data

    Returns:
        Two-digit number
    """
    first = data[0]
    last = data[-1] if len(data) > 1 else first
    return int(f"{first}{last}")


def main():
    """
    Main function to calculate the sum of all calibration values.
    """
    data: List = get_list_from_txt("data/day_1.txt")
    w2n: List = [word_to_number(row) for row in data]
    numbers: List = [get_first_and_last(row) for row in w2n]
    return sum(numbers)


if __name__ == "__main__":
    result = main()
    print(result)

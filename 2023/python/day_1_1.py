"""
The newly-improved calibration document consists of lines of text;
each line originally contained a specific calibration value that the Elves now need to recover.
On each line, the calibration value can be found by combining the first digit and the
last digit (in that order) to form a single two-digit number.

For example:
```txt
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
```

In this example, the calibration values of these four lines are 12, 38, 15, and 77.
Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
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


def get_first_and_last_of_string(data: str) -> int:
    """
    Get the first and last digits of a string and return the two-digit number.

    Args:
        data: String containing the data

    Returns:
        Two-digit number
    """
    number_list: List = [i for i in data if i.isdigit()]
    if len(number_list) > 1:
        return int(f"{number_list[0]}{number_list[-1]}")
    return int(number_list[0] * 2)


def main():
    """
    Main function to calculate the sum of all calibration values.
    """
    data: List = get_list_from_txt("data/day_1.txt")
    numbers: List = [get_first_and_last_of_string(data=row) for row in data]
    return sum(numbers)


if __name__ == "__main__":
    result = main()
    print(result)

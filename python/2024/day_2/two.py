"""2024 - Day 2 Part 2"""

import argparse


def get_inputs(file: str) -> list[list[int]]:
    """
    Read input file and convert each line into a list of integers.

    Args:
        file (str): Path to input file.

    Returns:
        list[list[int]]: List of integer lists, each representing a record.
    """
    data = []
    with open(file, "r") as f:
        for line in f:
            data.append([int(i) for i in line.split()])
    return data


def is_const(arr: list[int]) -> bool:
    """
    Check if the array is strictly increasing or decreasing.

    Args:
        arr (list[int]): List of integers to check.

    Returns:
        bool: True if array is strictly increasing or decreasing, False otherwise.
    """
    is_asc = all(arr[i] < arr[i + 1] for i in range(len(arr) - 1))
    is_dec = all(arr[i] > arr[i + 1] for i in range(len(arr) - 1))
    return is_asc or is_dec


def is_jump(arr: list[int]) -> bool:
    """
    Check if there are any jumps larger than 3 between adjacent elements.

    Args:
        arr (list[int]): List of integers to check.

    Returns:
        bool: True if there is a jump larger than 3, False otherwise.
    """
    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) > 3:
            return True
    return False


def check_problem_dampener(record: list[int]) -> bool:
    """
    Check if removing any single element from the record makes it valid.
    A valid record is strictly increasing/decreasing with no jumps larger than 3.

    Args:
        record (list[int]): List of integers to check.

    Returns:
        bool: True if removing any element makes the record valid, False otherwise.
    """
    for i in range(len(record)):
        cpy_check_is_const = is_const(record[:i] + record[i + 1 :])
        cpy_check_is_jump = is_jump(record[:i] + record[i + 1 :])
        if cpy_check_is_const and not cpy_check_is_jump:
            return True
    return False


def main():
    """
    The solution does the following:
        - Read records from input file.
        - For each record:
            - First check if it's valid as is (constant and no jumps)
            - If not valid, check if removing any single element makes it valid
        - Count records that are either valid or can be made valid
        - Return the total count.
    """
    data = get_inputs(args.file)

    record_status = []
    for record in data:
        check_is_const = is_const(record)
        check_is_jump = is_jump(record)

        if check_is_const and not check_is_jump:
            record_status.append(True)
        else:
            record_status.append(check_problem_dampener(record))

    return record_status.count(True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, default="input.txt")
    args = parser.parse_args()
    result = main()
    print(f"Result: {result}")

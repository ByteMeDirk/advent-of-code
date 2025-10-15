"""2024 - Day 3 Part 1"""

import argparse
import re

MUL_REG: str = "mul\([0-9]*,[0-9]*\)"


def get_inputs(file: str) -> str:
    """
    Read input file and convert each line into a list of integers.

    Args:
        file (str): Path to input file.

    Returns:
        list[list[int]]: List of integer lists, each representing a record.
    """
    with open(file, "r") as f:
        return f.read()


def parse_mul(val: str) -> tuple[int, int]:
    """
    Uses regex to parse the mul string values found in the input string.

    Args:
        val (str): String containing mul values.

    Returns:
        tuple[int, int]: Tuple containing the two mul values.
    """
    val1, val2 = val.replace("mul(", "").replace(")", "").split(",")
    return int(val1), int(val2)


def add_muls(muls: list) -> int:
    """
    First multiplies each tuple in the list and then adds all of them.

    Args:
        muls (list): List of tuples containing mul values.

    Returns:
        int: Sum of all multiplied values.
    """
    multiplied = [val1 * val2 for val1, val2 in muls]
    return sum(multiplied)


def main():
    """
    The solution does the following:
        - Get inputs from file.
        - Parse mul values from input string.
        - Multiply each mul value and add them all.
        - Return the sum of all multiplied values.
    """
    data = get_inputs(args.file)

    all_muls = []
    for mul in re.findall(MUL_REG, data):
        all_muls.append(parse_mul(mul))

    return add_muls(all_muls)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, default="input.txt")
    args = parser.parse_args()
    result = main()
    print(f"Result: {result}")

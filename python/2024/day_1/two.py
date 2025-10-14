"""2024 - Day 1 Part 2"""

import argparse


def get_inputs(file: str) -> tuple[list, list]:
    """
    Get inputs from file and return two lists of integers.

    Args:
        file (str): Path to file containing inputs.

    Returns:
        tuple[list, list]: Two lists of integers.
    """
    l_arr, r_arr = [], []
    with open(file, "r") as f:
        for line in f:
            l, r = line.split("   ")
            l_arr.append(int(l))
            r_arr.append(int(r))

    return l_arr, r_arr


def get_sim_score(l_arr: list, r_arr: list) -> list:
    """
    Calculate similarity scores between two lists.
    For each element in l_arr, multiply it by the number of times it appears in r_arr.

    Args:
        l_arr (list): First list of integers.
        r_arr (list): Second list of integers.

    Returns:
        list: List of similarity scores.
    """
    sim_score = []
    for li in l_arr:
        sim_count = 0
        for ri in r_arr:
            if li == ri:
                sim_count += 1
        sim_score.append(li * sim_count)
    return sim_score


def get_sup_sim_score(sim_score: list) -> int:
    """
    Calculate the sum of all similarity scores.

    Args:
        sim_score (list): List of similarity scores.

    Returns:
        int: Sum of all similarity scores.
    """
    return sum(sim_score)


def main():
    """
    The solution does the following:
        - Get inputs from file.
        - Calculate similarity scores between the two lists.
        - Return the sum of all similarity scores.
    """
    l_arr, r_arr = get_inputs(args.file)
    sim_arr = get_sim_score(l_arr, r_arr)
    sim_score = get_sup_sim_score(sim_arr)
    return sim_score


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, default="input.txt")
    args = parser.parse_args()
    result = main()
    print(f"Result: {result}")

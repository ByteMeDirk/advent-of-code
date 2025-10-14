"""2024 - Day 1 Part 1"""

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


def swap(arr: list, i: int, j: int) -> list:
    """
    Swap two elements in a list.

    Args:
        arr (list): List of elements.
        i (int): Index of first element.
        j (int): Index of second element.

    Returns:
        list: List with elements swapped.
    """
    arr[i], arr[j] = arr[j], arr[i]
    return arr


def partition(arr: list, lo: int, hi: int) -> int:
    """
    Partition the list into two sublists based on the pivot.

    Args:
        arr (list): List of elements.
        lo (int): Index of the first element in the sublist.
        hi (int): Index of the last element in the sublist.

    Returns:
        int: Index of the pivot.
    """
    pivot = arr[hi]
    i = lo - 1

    for j in range(lo, hi):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, hi)
    return i + 1


def quick_sort(arr: list, lo: int, hi: int) -> list:
    """
    Perform quick sort on the list.

    Args:
        arr (list): List of elements.
        lo (int): Index of the first element in the sublist.
        hi (int): Index of the last element in the sublist.

    Returns:
        list: Sorted list.
    """
    if lo < hi:
        partition_index = partition(arr, lo, hi)
        quick_sort(arr, lo, partition_index - 1)
        quick_sort(arr, partition_index + 1, hi)

    return arr


def get_distance(val1: int, val2: int) -> int:
    """
    Get the absolute distance between two values.

    Args:
        val1 (int): First value.
        val2 (int): Second value.

    Returns:
        int: Absolute distance between the two values.
    """
    return abs(val1 - val2)


def get_sum_distances(arr: list) -> int:
    """
    Get the sum of distances between adjacent elements in a list.

    Args:
        arr (list): List of distances.

    Returns:
        int: Sum of distances.
    """
    return sum(arr)


def main():
    """
    The solution does the following:
        - Get inputs from file.
        - Sort the lists.
        - Calculate the distance between adjacent elements in the sorted lists.
        - Return the sum of distances.
    """
    l_arr, r_arr = get_inputs(args.file)

    sorted_l_arr = quick_sort(l_arr, 0, len(l_arr) - 1)
    sorted_r_arr = quick_sort(r_arr, 0, len(r_arr) - 1)

    distances = []
    for li, ri in zip(sorted_l_arr, sorted_r_arr):
        distances.append(get_distance(li, ri))

    return get_sum_distances(distances)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str)
    args = parser.parse_args()
    result = main()
    print(f"Result: {result}")

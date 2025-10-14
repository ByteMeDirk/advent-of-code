import argparse


def get_inputs(file: str) -> tuple[list, list]:
    l_arr, r_arr = [], []
    with open(file, "r") as f:
        for line in f:
            l, r = line.split("   ")
            l_arr.append(int(l))
            r_arr.append(int(r))

    return l_arr, r_arr


def swap(arr: list, i: int, j: int) -> list:
    arr[i], arr[j] = arr[j], arr[i]
    return arr


def partition(arr: list, lo: int, hi: int) -> int:
    pivot = arr[hi]
    i = lo - 1

    for j in range(lo, hi):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, hi)
    return i + 1


def quick_sort(arr: list, lo: int, hi: int) -> list:
    if lo < hi:
        partition_index = partition(arr, lo, hi)
        quick_sort(arr, lo, partition_index - 1)
        quick_sort(arr, partition_index + 1, hi)

    return arr


def get_distance(val1: int, val2: int) -> int:
    return abs(val1 - val2)


def get_sum_distances(arr: list) -> int:
    return sum(arr)


def main():
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

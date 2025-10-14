import argparse


def get_inputs(file: str) -> tuple[list, list]:
    l_arr, r_arr = [], []
    with open(file, "r") as f:
        for line in f:
            l, r = line.split("   ")
            l_arr.append(int(l))
            r_arr.append(int(r))

    return l_arr, r_arr


def get_sim_score(l_arr: list, r_arr: list) -> list:
    sim_score = []
    for li in l_arr:
        sim_count = 0
        for ri in r_arr:
            if li == ri:
                sim_count += 1
        sim_score.append(li * sim_count)
    return sim_score


def get_sup_sim_score(sim_score: list) -> int:
    return sum(sim_score)


def main():
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

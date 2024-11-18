"""
As you continue your walk, the Elf poses a second question: in each game you played,
what is the fewest number of cubes of each color that could have been in the bag to
make the game possible?

Again consider the example games from earlier:
```txt
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
```

In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes.
If any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
The power of a set of cubes is equal to the numbers of red, green, and blue cubes
multiplied together. The power of the minimum set of cubes in game 1 is 48.
In games 2-5 it was 12, 1560, 630, and 36, respectively.
Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present.
What is the sum of the power of these sets?
"""

from typing import List, Dict, Tuple

MAX_CUBES: Dict = {"red": 12, "green": 13, "blue": 14}


def get_data_from_txt(file_path: str) -> List:
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


def parse_data(data: str) -> Tuple:
    """
    Parse the data into a dictionary.

    Args:
        data: String containing the data

    Returns:
        Tuple of game number and dictionary of game plays
    """
    # Get the game number and the game plays
    game_number, game_plays = data.split(":")[0].strip().split(" ")[1], data.split(":")[
        -1
    ].split(";")

    # Parse the game plays
    parsed_games = []
    for play in game_plays:
        counts = play.strip().split(", ")
        counts_dict = {}
        for count in counts:
            number, color = count.split()
            counts_dict[color] = int(number)
        parsed_games.append(counts_dict)

    return int(game_number), parsed_games


def calculate_minimum_cubes(data: List) -> Dict:
    """
    Calculate the minimum number of cubes needed for each color.

    Args:
        data: List of game plays

    Returns:
        Dictionary of minimum number of cubes needed for each color
    """
    min_cubes = {"red": 0, "green": 0, "blue": 0}
    for play in data:
        for color in min_cubes:
            min_cubes[color] = max(min_cubes[color], play.get(color, 0))
    return min_cubes


def calculate_power(data: Dict) -> int:
    """
    Calculate the power of the cubes.

    Args:
        data: Dictionary of minimum number of cubes needed for each color

    Returns:
        Power of the cubes
    """
    return data["red"] * data["green"] * data["blue"]


def main():
    """
    Main function to calculate the sum of all calibration values.
    """
    data: List = get_data_from_txt("data/day_2.txt")

    # Parse the data
    parsed_games: Dict = {}
    for row in data:
        game_number, game_plays = parse_data(data=row)
        parsed_games[game_number] = game_plays

    sum_power_calcs: int = 0
    for game_id, game_plays in parsed_games.items():
        min_cubes = calculate_minimum_cubes(game_plays)
        power_calcs = calculate_power(min_cubes)
        sum_power_calcs += power_calcs

    return sum_power_calcs


if __name__ == "__main__":
    result = main()
    print(result)

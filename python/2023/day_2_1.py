"""
You play several games and record the information from each game (your puzzle input).
Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a
semicolon-separated list of subsets of cubes that were revealed from the
bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:
```txt
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
```

In game 1, three sets of cubes are revealed from the bag (and then put back again).
The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube,
2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if
the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had
been loaded with that configuration. However, game 3 would have been impossible
because at one point the Elf showed you 20 red cubes at once; similarly, game 4
would also have been impossible because the Elf showed you 15 blue cubes at once.
If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with
only 12 red cubes, 13 green cubes, and 14 blue cubes.
What is the sum of the IDs of those games?
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


def check_valid_game(data: Dict) -> List:
    """
    Check if the game is valid.

    Args:
        data: Dictionary containing the data to validate

    Returns:
        List of valid games
    """
    valid_games = []
    for game_id, game_plays in data.items():
        is_valid = True
        for play in game_plays:
            for color, count in play.items():
                if count > MAX_CUBES[color]:
                    is_valid = False
                    break
            if not is_valid:
                break
        if is_valid:
            valid_games.append(game_id)

    return valid_games


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

    # Check for valid games
    valid_games = check_valid_game(data=parsed_games)

    return sum(valid_games)


if __name__ == "__main__":
    result = main()
    print(result)

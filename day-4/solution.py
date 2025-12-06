import sys

from typing import List


MAX_ADJACENT_ROLLS = 4


def get_file_path_argument() -> str:
    if len(sys.argv) > 1:
        return sys.argv[1]
    raise Exception("Error: File path argument not provided.")


def get_paper_grid(file_path) -> List[List[str]]:
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
            return list(map(lambda l: list(l.strip()), lines))
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        exit()


def is_roll(row, column, paper_grid):
    return paper_grid[row][column] == "@"


def is_within_bounds(row, column, paper_grid):
    return 0 <= row < len(paper_grid) and 0 <= column < len(paper_grid[0])


def is_roll_accessible(row, column, paper_grid: List[List[str]]):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    adjacent_rolls = 0

    for dr, dc in directions:
        check_features = (row + dr, column + dc, paper_grid)

        adjacent_rolls += is_within_bounds(*check_features) and is_roll(*check_features)

        if adjacent_rolls >= MAX_ADJACENT_ROLLS:
            return False

    return True


def remove_accessible_rolls(paper_grid) -> int:
    rolls_to_remove = [
        (r, c)
        for r in range(len(paper_grid))
        for c in range(len(paper_grid[0]))
        if is_roll(r, c, paper_grid) and is_roll_accessible(r, c, paper_grid)
    ]

    for row, column in rolls_to_remove:
        paper_grid[row][column] = "."

    return len(rolls_to_remove)


if __name__ == "__main__":
    file_path = get_file_path_argument()

    # 2D array of '.' empty space and '@' paper roll characters
    paper_grid = get_paper_grid(file_path)

    # total amount of rolls removed on the first pass
    rolls_removed_at_start = remove_accessible_rolls(paper_grid)

    # total amount of rolls that can be removed
    total_removed_rolls = rolls_removed_at_start

    while (removed := remove_accessible_rolls(paper_grid)) > 0:
        total_removed_rolls += removed

    print(f"Part 1: {rolls_removed_at_start}")
    print(f"Part 2: {total_removed_rolls}")

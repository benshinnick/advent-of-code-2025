import sys
import math

from typing import List


def get_file_path_argument() -> str:
    if len(sys.argv) > 1:
        return sys.argv[1]
    raise Exception("Error: File path argument not provided.")


def get_file_lines(file_path) -> List[str]:
    try:
        with open(file_path, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        exit()


def part_1(file_lines):
    math_grid = [l.split() for l in file_lines]

    results = []

    for column in range(len(math_grid[0])):
        operator = math_grid[-1][column]
        numbers = [int(row[column]) for row in math_grid[:-1]]
        results.append(math.prod(numbers) if operator == "*" else sum(numbers))

    return sum(results)


def part_2(file_lines):
    grid = [list(line.rstrip("\n")) for line in file_lines]
    results, numbers = [], []

    for col in range(len(grid[0]) - 1, -1, -1):
        line = [row[col] for row in grid[::-1]]
        number_string = "".join(line[::-1][:-1]).strip()
        operator = line[0].strip()

        if not number_string:
            continue

        numbers.append(int(number_string))

        if not operator:
            continue

        results.append(math.prod(numbers) if operator == "*" else sum(numbers))
        numbers.clear()

    return sum(results)


if __name__ == "__main__":
    file_path = get_file_path_argument()

    file_lines = get_file_lines(file_path)

    print(f"Part 1: {part_1(file_lines)}")
    print(f"Part 2: {part_2(file_lines)}")

import math
import sys

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


def calc_hits_for_left_rotation(num_clicks, dial_pointer) -> int:
    if dial_pointer == 0:
        return num_clicks // 100
    if num_clicks < dial_pointer:
        return 0
    return 1 + (num_clicks - dial_pointer) // 100


if __name__ == "__main__":
    file_path = get_file_path_argument()

    # 0 to 99
    dial_pointer = 50
    # number of times dial points at 0 after each rotation
    original_password = 0
    # number of times any click causes the dial to point to 0
    actual_password = 0

    for line in get_file_lines(file_path):
        # raw line example: 'L16\n'
        direction = line[0]  # L or R
        num_clicks = int(line.strip()[1:])
        hits = 0

        if direction == "R":
            hits = (dial_pointer + num_clicks) // 100
            dial_pointer = (dial_pointer + num_clicks) % 100

        if direction == "L":
            hits = calc_hits_for_left_rotation(num_clicks, dial_pointer)
            dial_pointer = (dial_pointer - num_clicks) % 100

        original_password += dial_pointer == 0
        actual_password += hits

    print(f"Part 1: {original_password}")
    print(f"Part 2: {actual_password}")

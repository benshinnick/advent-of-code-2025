import sys
import re

from typing import List


def get_file_path_argument() -> str:
    if len(sys.argv) > 1:
        return sys.argv[1]
    raise Exception("Error: File path argument not provided.")


def get_file_ranges(file_path) -> List[str]:
    try:
        with open(file_path, "r") as f:
            single_line_string = f.readline().strip()
            return single_line_string.split(",")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        exit()


def get_invalid_ids_within_range(range_start, range_end, invalid_pattern) -> List[int]:
    invalid_ids: List[int] = []

    for id in range(range_start, range_end + 1):
        if invalid_pattern.match(str(id)):
            invalid_ids.append(id)

    return invalid_ids


if __name__ == "__main__":
    file_path = get_file_path_argument()

    # IDs with some sequence of digits repeated twice
    original_invalid_ids: List[int] = []

    # IDs with some sequence of digits repeated at least twice
    actual_invalid_ids: List[int] = []

    # ([1-9]\d*) -> non-zero-prefixed number
    # \1 -> exact same sequence appears immediately after
    original_invalid_pattern = re.compile(r"^([1-9]\d*)\1$")

    # ([1-9]\d*) -> non-zero-prefixed number
    # \1+ -> exact same sequence appears one or more times after
    actual_invalid_pattern = re.compile(r"^([1-9]\d*)\1+$")

    for range_data in get_file_ranges(file_path):
        # inclusive range '95-115' -> [95, 115]
        start = int(range_data.split("-")[0])
        end = int(range_data.split("-")[1])

        original_invalid_ids += get_invalid_ids_within_range(
            start, end, original_invalid_pattern
        )
        actual_invalid_ids += get_invalid_ids_within_range(
            start, end, actual_invalid_pattern
        )

    print(f"Part 1: {sum(original_invalid_ids)}")
    print(f"Part 2: {sum(actual_invalid_ids)}")

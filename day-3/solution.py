import sys

from typing import List


def get_file_path_argument() -> str:
    if len(sys.argv) > 1:
        return sys.argv[1]
    raise Exception("Error: File path argument not provided.")


def get_battery_banks(file_path) -> List[str]:
    try:
        with open(file_path, "r") as f:
            return list(map(lambda l: l.strip(), f.readlines()))
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        exit()


def get_max_digit(bank, search_start_position, digits_remaining) -> tuple[int, int]:
    max_digit, max_position = 0, search_start_position

    for i in range(search_start_position, len(bank) - digits_remaining):
        if int(bank[i]) > max_digit:
            max_digit, max_position = int(bank[i]), i

    return max_digit, max_position


def get_max_joltage_for_bank(bank, num_batteries) -> int:
    max_digits = []

    for i in range(num_batteries):
        last_max_position = max_digits[i - 1][1] if i > 0 else -1
        search_start = last_max_position + 1
        digits_remaining = num_batteries - i - 1

        max_digits.append(get_max_digit(bank, search_start, digits_remaining))

    # stringify each max digit (first tuple value in max_digits) then combine and parse back into int
    return int("".join(map(lambda m: str(m[0]), max_digits)))


if __name__ == "__main__":
    file_path = get_file_path_argument()

    # max numbers formed by the digits of two selected batteries in each bank
    original_max_totals = []

    # max numbers formed by the digits of 12 selected batteries in each bank
    overrided_max_totals = []

    for bank in get_battery_banks(file_path):
        original_max_totals.append(get_max_joltage_for_bank(bank, 2))
        overrided_max_totals.append(get_max_joltage_for_bank(bank, 12))

    print(f"Part 1: {sum(original_max_totals)}")
    print(f"Part 2: {sum(overrided_max_totals)}")

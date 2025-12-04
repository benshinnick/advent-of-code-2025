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


def get_max_at_position(bank, start_position, num_remaining) -> tuple[int, int]:
    max_jolts = 0
    max_position = start_position

    for i in range(start_position, len(bank) - num_remaining):
        if int(bank[i]) > max_jolts:
            max_jolts = int(bank[i])
            max_position = i

    return max_jolts, max_position


def get_max_joltage_for_bank(bank, num_batteries) -> int:
    max_jolts = []
    last_max_position = -1

    for i in range(num_batteries):
        batteries_remaining = num_batteries - i - 1
        search_start_position = last_max_position + 1

        max_at_position, last_max_position = get_max_at_position(
            bank, search_start_position, batteries_remaining
        )

        max_jolts.append(max_at_position)

    return int("".join(map(str, max_jolts)))


if __name__ == "__main__":
    file_path = get_file_path_argument()

    # max numbers formed by the digits of two selected batteries in each bank
    original_max_totals = []

    # max numbers formed by the digits of 12 selected batteries in each bank
    overrided_max_totals = []

    for line in get_file_lines(file_path):
        # bank example: '234234234234278'
        bank = line.strip()

        original_max_totals.append(get_max_joltage_for_bank(bank, 2))
        overrided_max_totals.append(get_max_joltage_for_bank(bank, 12))

    print(f"Part 1: {sum(original_max_totals)}")
    print(f"Part 2: {sum(overrided_max_totals)}")

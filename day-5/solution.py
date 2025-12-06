import sys

from typing import List


MAX_ADJACENT_ROLLS = 4


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


def merge_overlapping_ranges(ranges):
    merged = []

    for start, end in sorted(ranges):
        # extend the last range if needed
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
            continue

        merged.append([start, end])

    return merged


def get_fresh_ranges(file_lines) -> List[tuple[int, int]]:
    fresh_ranges = []

    for line in file_lines[: file_lines.index("\n")]:
        fresh_ranges.append(list(map(lambda s: int(s), line.split("-"))))

    return merge_overlapping_ranges(fresh_ranges)


def get_produce_ids(file_lines) -> List[int]:
    produce_ids = []

    for line in file_lines[file_lines.index("\n") + 1 :]:
        produce_ids.append(int(line))

    return produce_ids


if __name__ == "__main__":
    file_path = get_file_path_argument()
    file_lines = get_file_lines(file_path)

    fresh_ranges = get_fresh_ranges(file_lines)
    produce_ids = get_produce_ids(file_lines)

    # all produce IDs that fall within the fresh ranges
    fresh_produce_ids = [
        produce_id
        for produce_id in produce_ids
        if any(start <= produce_id <= end for start, end in fresh_ranges)
    ]

    # count of all produce IDs that fall within the fresh ranges
    possible_fresh_ids = sum((end - start + 1) for start, end in fresh_ranges)

    print(f"Part 1: {len(fresh_produce_ids)}")
    print(f"Part 2: {possible_fresh_ids}")

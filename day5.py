import re
from typing import List, Tuple


def parse_input(file_path) -> Tuple[List[Tuple[int, int]], List[List[int]]]:
    mode = "rules"
    rules = []
    updates = []

    with open(file_path, "r") as file:
        contents = file.read()
        for l in contents.splitlines():
            if l == "":
                mode = "updates"
                continue

            if mode == "rules":
                a, b = l.split("|")
                rules.append((int(a), int(b)))
            else:
                updates.append([int(x) for x in l.split(",")])

    return rules, updates


def check_update(rules: List[Tuple[int, int]], update: List[int]) -> bool:
    for before, after in rules:
        if before not in update or after not in update:
            continue

        before_idx = update.index(before)
        after_idx = update.index(after)

        if before_idx > after_idx:
            return False

    return True


def sum_valid_updates_middles(
    rules: List[Tuple[int, int]], updates: List[List[int]]
) -> int:
    result = 0
    for update in updates:
        if check_update(rules, update):
            result += update[len(update) // 2]
    return result


if __name__ == "__main__":
    [rules, updates] = parse_input("./inputs/day5.txt")
    part1 = sum_valid_updates_middles(rules, updates)
    print("Sum of valid middle updates:", part1)

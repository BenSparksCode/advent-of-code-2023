# Advent of Code 2023 - Day 15

from functools import reduce

def hash(word: str) -> int:
    res = 0
    for c in word:
        res = ((res + ord(c)) * 17) % 256
    return res


def part_one(input):
    steps = input.split(",")
    return reduce(lambda acc, step: acc + hash(step), steps, 0)


def part_two(input):
    return None


if __name__ == "__main__":
    with open(f"data/2023/inputs/15.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

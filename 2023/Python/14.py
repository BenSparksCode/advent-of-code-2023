# Advent of Code 2023 - Day 14

from typing import List

def calc_load(grid: List[List[str]]) -> int:
    total = 0
    for y, row in enumerate(grid):
        for c in row:
            if c == "O": total += (len(grid) - y)
    return total


def part_one(input):
    grid = [list(i) for i in input.split("\n")]

    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == ".":
                for p in range(y + 1, len(grid)):
                    if grid[p][x] == "#": break
                    if grid[p][x] == "O":
                        grid[y][x] = "O"
                        grid[p][x] = "."
                        break

    return calc_load(grid)


def part_two(input):
    return None


if __name__ == "__main__":
    with open(f"data/2023/inputs/14.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

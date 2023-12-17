# Advent of Code 2023 - Day 14

from typing import List

def calc_load(grid: List[List[str]]) -> int:
    total = 0
    for y, row in enumerate(grid):
        for c in row:
            if c == "O": total += (len(grid) - y)
    return total

def tilt_north(grid: List[List[str]]):
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == ".":
                for p in range(y + 1, len(grid)):
                    if grid[p][x] == "#": break
                    if grid[p][x] == "O":
                        grid[y][x] = "O"
                        grid[p][x] = "."
                        break

def tilt_west(grid: List[List[str]]):
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == ".":
                for p in range(x + 1, len(grid[0])):
                    if grid[y][p] == "#": break
                    if grid[y][p] == "O":
                        grid[y][x] = "O"
                        grid[y][p] = "."
                        break

def cycle(grid: List[List[str]]) -> List[List[str]]:
    tilt_north(grid)
    tilt_west(grid)
    tilt_north(grid[::-1])
    grid = [row[::-1] for row in grid]
    tilt_west(grid)
    grid = [row[::-1] for row in grid]
    return grid


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
    grid = [list(i) for i in input.split("\n")]
    load_x = 1_000_000_000
    target_cycle = 103 + ((load_x - 103) % 14)

    for _ in range(1, target_cycle + 1):
        grid = cycle(grid)

    # Pattern stabilizes at 103 cycles.
    # From then, takes 14 cycles to repeat.
    # Therefore, load at X cycles = load at [103 + ((X - 103) % 14)] cycles.
    # Therefore, load at 1 000 000 000 cycles = load at 104 cycles
    # = 94255
        
    return calc_load(grid)


if __name__ == "__main__":
    with open(f"data/2023/inputs/14.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

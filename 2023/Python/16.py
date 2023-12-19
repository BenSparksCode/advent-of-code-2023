# Advent of Code 2023 - Day 16

import sys
from functools import reduce
from typing import List, Tuple

# My brother in Christ, you are running on an M2 Max
sys.setrecursionlimit(50000)

UP, RIGHT, DOWN, LEFT = 1, 2, 3, 4

# Recursively explore grid as a beam, recording each time a tile is energized
def beam_explore(pos: Tuple[int, int], dir: int, grid: List[List[str]], energized: dict):
    # Stop when beam hits a wall
    if dir == UP and pos[1] < 0: return
    if dir == RIGHT and pos[0] > len(grid[0]) - 1: return
    if dir == DOWN and pos[1] > len(grid) - 1: return
    if dir == LEFT and pos[0] < 0: return

    # Record dir that tile is energized in
    if pos in energized:
        if dir in energized[pos]: return # stop if traveling same tile in same dir
        energized[pos].append(dir)
    else:
        energized[pos] = [dir]
    c = char_at_pos(pos, grid)

    if dir == UP:
        if c == "." or c == "|": beam_explore(tuple([pos[0], pos[1] - 1]), UP, grid, energized)
        if c == "\\": beam_explore(tuple([pos[0] - 1, pos[1]]), LEFT, grid, energized)
        if c == "/": beam_explore(tuple([pos[0] + 1, pos[1]]), RIGHT, grid, energized)
        if c == "-":
            beam_explore(tuple([pos[0] + 1, pos[1]]), RIGHT, grid, energized)
            beam_explore(tuple([pos[0] - 1, pos[1]]), LEFT, grid, energized)

    if dir == RIGHT:
        if c == "." or c == "-": beam_explore(tuple([pos[0] + 1, pos[1]]), RIGHT, grid, energized)
        if c == "\\": beam_explore(tuple([pos[0], pos[1] + 1]), DOWN, grid, energized)
        if c == "/": beam_explore(tuple([pos[0], pos[1] - 1]), UP, grid, energized)
        if c == "|":
            beam_explore(tuple([pos[0], pos[1] - 1]), UP, grid, energized)
            beam_explore(tuple([pos[0], pos[1] + 1]), DOWN, grid, energized)

    if dir == DOWN:
        if c == "." or c == "|": beam_explore(tuple([pos[0], pos[1] + 1]), DOWN, grid, energized)
        if c == "\\": beam_explore(tuple([pos[0] + 1, pos[1]]), RIGHT, grid, energized)
        if c == "/": beam_explore(tuple([pos[0] - 1, pos[1]]), LEFT, grid, energized)
        if c == "-":
            beam_explore(tuple([pos[0] + 1, pos[1]]), RIGHT, grid, energized)
            beam_explore(tuple([pos[0] - 1, pos[1]]), LEFT, grid, energized)

    if dir == LEFT:
        if c == "." or c == "-": beam_explore(tuple([pos[0] - 1, pos[1]]), LEFT, grid, energized)
        if c == "\\": beam_explore(tuple([pos[0], pos[1] - 1]), UP, grid, energized)
        if c == "/": beam_explore(tuple([pos[0], pos[1] + 1]), DOWN, grid, energized)
        if c == "|":
            beam_explore(tuple([pos[0], pos[1] - 1]), UP, grid, energized)
            beam_explore(tuple([pos[0], pos[1] + 1]), DOWN, grid, energized)
    return

def char_at_pos(pos: Tuple[int, int], grid: List[List[str]]) -> str:
    return grid[pos[1]][pos[0]]


def part_one(input):
    grid = [list(i) for i in input.split("\n")]
    energized = {}

    beam_explore(tuple([0,0]), RIGHT, grid, energized)
    return reduce(lambda acc, k: acc + 1, energized.keys(), 0)


def part_two(input):
    init_grid = [list(i) for i in input.split("\n")]
    energized, grid = {}, init_grid
    max_energized = 0

    # Iterate length, alternating top and bottom starts
    for x in range(len(grid[0])):
        energized, grid = {}, init_grid # clear and traverse again
        beam_explore(tuple([x, 0]), DOWN, grid, energized)
        cnt = reduce(lambda acc, k: acc + 1, energized.keys(), 0)
        if cnt > max_energized: max_energized = cnt

        energized, grid = {}, init_grid # clear and traverse again
        beam_explore(tuple([x, len(grid) - 1]), UP, grid, energized)
        cnt = reduce(lambda acc, k: acc + 1, energized.keys(), 0)
        if cnt > max_energized: max_energized = cnt

    # Iterate height, alternating left and right starts
    for y in range(len(grid)):
        energized, grid = {}, init_grid # clear and traverse again
        beam_explore(tuple([0, y]), RIGHT, grid, energized)
        cnt = reduce(lambda acc, k: acc + 1, energized.keys(), 0)
        if cnt > max_energized: max_energized = cnt

        energized, grid = {}, init_grid # clear and traverse again
        beam_explore(tuple([len(grid[0]) - 1, y]), LEFT, grid, energized)
        cnt = reduce(lambda acc, k: acc + 1, energized.keys(), 0)
        if cnt > max_energized: max_energized = cnt

    return max_energized


if __name__ == "__main__":
    with open(f"data/2023/inputs/16.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

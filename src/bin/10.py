# Advent of Code 2023 - Day 10

import sys
import itertools
from typing import List, Tuple

# My brother in Christ, you are running on an M2 Max
sys.setrecursionlimit(50000)

Point = Tuple[int, int] # x, y

def explore(start: Point, curr_dist: int, grid, dists):
    valid_moves = find_valid_moves(start, grid)

    # End if no valid moves or can't improve dist
    if len(valid_moves) == 0: return None

    for move in valid_moves:
        # Stop searching if next move already discovered more efficiently 
        if point_to_dist(move, dists) <= curr_dist: continue
        # Store dist and keep searching
        dists[move[1]][move[0]] = curr_dist + 1
        explore(move, curr_dist + 1, grid, dists)
    
    return None

# Check 4 directions around point, return those points if valid char for entry
def find_valid_moves(pnt: Point, grid) -> List[Point]:
    valid_moves = []
    # Check Left
    if 0 < pnt[0] and grid[pnt[1]][pnt[0] - 1] in ["-", "L", "F"]: valid_moves.append(tuple([pnt[0] - 1, pnt[1]]))
    # Check Right
    if pnt[0] < len(grid[0]) - 1 and grid[pnt[1]][pnt[0] + 1] in ["-", "J", "7"]: valid_moves.append(tuple([pnt[0] + 1, pnt[1]]))
    # Check Up
    if 0 < pnt[1] and grid[pnt[1] - 1][pnt[0]] in ["|", "7", "F"]: valid_moves.append(tuple([pnt[0], pnt[1] - 1]))
    # Check Down
    if pnt[1] < len(grid) - 1 and grid[pnt[1] + 1][pnt[0]] in ["|", "J", "L"]: valid_moves.append(tuple([pnt[0], pnt[1] + 1]))
    return valid_moves

# Looks up the distance of an (x, y) point
def point_to_dist(point: Point, dists) -> int:
    return dists[point[1]][point[0]]

def part_one(input):
    # Grid is 140 x 140
    grid = input.split("\n")
    dists = [[999_999_999 for _ in grid[0]] for _ in grid]
    start = tuple([0, 0])

    # Find S
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "S":
                start = tuple([x, y])
                dists[y][x] = 0

    explore(start, 0, grid, dists)

    return max([i for i in itertools.chain(*dists) if i != 999_999_999])

def part_two(input):
    return None

if __name__ == "__main__":
    with open(f"data/inputs/10.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

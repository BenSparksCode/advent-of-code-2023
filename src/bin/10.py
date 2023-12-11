# Advent of Code 2023 - Day 10

import sys
import itertools
from typing import List, Tuple

# My brother in Christ, you are running on an M2 Max
sys.setrecursionlimit(50000)

Point = Tuple[int, int] # x, y

# Iteratively explore - allows to mark sides because direction is deterministic
def explore_iteratively(curr_point: Point, grid, dists):
    prev_point = curr_point
    curr_point = find_valid_moves(curr_point, grid)[0]
    while point_to_dist(curr_point, dists) != 0:
        valid_moves = find_valid_moves(curr_point, grid)
        move = valid_moves[0]
        if are_points_eql(move, prev_point): move = valid_moves[1]

        # Moving -->
        if curr_point[0] - move[0] == -1:
            adj_point = tuple([curr_point[0], curr_point[1] - 1]) # up
            if is_point_in_grid(adj_point, grid) and point_to_dist(adj_point, dists) == 999_999: set_point_dist(adj_point, -1, dists)
            adj_point = tuple([curr_point[0], curr_point[1] + 1]) # down
            if is_point_in_grid(adj_point, grid) and point_to_dist(adj_point, dists) == 999_999: set_point_dist(adj_point, -2, dists)
            adj_point = tuple([move[0], move[1] - 1]) # up
            if is_point_in_grid(adj_point, grid) and point_to_dist(adj_point, dists) == 999_999: set_point_dist(adj_point, -1, dists)
            adj_point = tuple([move[0], move[1] + 1]) # down
            if is_point_in_grid(adj_point, grid) and point_to_dist(adj_point, dists) == 999_999: set_point_dist(adj_point, -2, dists)

        # Moving <--
        elif curr_point[0] - move[0] == 1:
            adj_point = tuple([curr_point[0], curr_point[1] + 1]) # down
            if is_point_in_grid(adj_point, grid) and point_to_dist(adj_point, dists) == 999_999: set_point_dist(adj_point, -1, dists)
            adj_point = tuple([curr_point[0], curr_point[1] - 1]) # up
            if is_point_in_grid(adj_point, grid) and point_to_dist(adj_point, dists) == 999_999: set_point_dist(adj_point, -2, dists)
            adj_point = tuple([move[0], move[1] + 1]) # down
            if is_point_in_grid(adj_point, grid) and point_to_dist(adj_point, dists) == 999_999: set_point_dist(adj_point, -1, dists)
            adj_point = tuple([move[0], move[1] - 1]) # up
            if is_point_in_grid(adj_point, grid) and point_to_dist(adj_point, dists) == 999_999: set_point_dist(adj_point, -2, dists)
        
        else:
            # Moving ^
            if curr_point[1] - move[1] == 1:
                adj_point = tuple([curr_point[0] - 1, curr_point[1]]) # left
                if is_point_in_grid(adj_point, grid) and point_to_dist(adj_point, dists) == 999_999: set_point_dist(adj_point, -1, dists)
                adj_point = tuple([curr_point[0] + 1, curr_point[1]]) # right
                if is_point_in_grid(adj_point, grid) and point_to_dist(adj_point, dists) == 999_999: set_point_dist(adj_point, -2, dists)
                adj_point = tuple([move[0] - 1, move[1]]) # left
                if is_point_in_grid(adj_point, grid) and point_to_dist(adj_point, dists) == 999_999: set_point_dist(adj_point, -1, dists)
                adj_point = tuple([move[0] + 1, move[1]]) # right
                if is_point_in_grid(adj_point, grid) and point_to_dist(adj_point, dists) == 999_999: set_point_dist(adj_point, -2, dists)

            # Moving V
            else:
                adj_point = tuple([curr_point[0] + 1, curr_point[1]]) # right
                if is_point_in_grid(adj_point, grid) and point_to_dist(adj_point, dists) == 999_999: set_point_dist(adj_point, -1, dists)
                adj_point = tuple([curr_point[0] - 1, curr_point[1]]) # left
                if is_point_in_grid(adj_point, grid) and point_to_dist(adj_point, dists) == 999_999: set_point_dist(adj_point, -2, dists)
                adj_point = tuple([move[0] + 1, move[1]]) # right
                if is_point_in_grid(adj_point, grid) and point_to_dist(adj_point, dists) == 999_999: set_point_dist(adj_point, -1, dists)
                adj_point = tuple([move[0] - 1, move[1]]) # left
                if is_point_in_grid(adj_point, grid) and point_to_dist(adj_point, dists) == 999_999: set_point_dist(adj_point, -2, dists)

        prev_point = curr_point
        curr_point = move

# Recursively explore path options
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
    # Check Left (if allowed left)
    if 0 < pnt[0] and grid[pnt[1]][pnt[0] - 1] in "S-LF" and grid[pnt[1]][pnt[0]] in "S-J7":
        valid_moves.append(tuple([pnt[0] - 1, pnt[1]]))
    # Check Right (if allowed right)
    if pnt[0] < len(grid[0]) - 1 and grid[pnt[1]][pnt[0] + 1] in "S-J7" and grid[pnt[1]][pnt[0]] in "S-LF":
        valid_moves.append(tuple([pnt[0] + 1, pnt[1]]))
    # Check Up (if allowed up)
    if 0 < pnt[1] and grid[pnt[1] - 1][pnt[0]] in "S|7F" and grid[pnt[1]][pnt[0]] in "S|LJ":
        valid_moves.append(tuple([pnt[0], pnt[1] - 1]))
    # Check Down (if allowed down)
    if pnt[1] < len(grid) - 1 and grid[pnt[1] + 1][pnt[0]] in "S|JL" and grid[pnt[1]][pnt[0]] in "S|F7":
        valid_moves.append(tuple([pnt[0], pnt[1] + 1]))
    return valid_moves

# Looks up the distance of an (x, y) point
def point_to_dist(point: Point, dists) -> int:
    return dists[point[1]][point[0]]

def are_points_eql(point1: Point, point2: Point) -> bool:
    return point1[0] == point2[0] and point1[1] == point2[1]

def is_point_in_grid(point: Point, grid) -> bool:
    return 0 <= point[0] < len(grid[0]) and 0 <= point[1] < len(grid) 

def set_point_dist(point: Point, new_dist, dists):
    dists[point[1]][point[0]] = new_dist


def part_one(input):
    # Grid is 140 x 140
    grid = input.split("\n")
    dists = [[999_999 for _ in grid[0]] for _ in grid]
    start = tuple([0, 0])

    # Find S
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "S":
                start = tuple([x, y])
                dists[y][x] = 0

    explore(start, 0, grid, dists)

    return max([i for i in itertools.chain(*dists) if i != 999_999])


def part_two(input):
    # Grid is 140 x 140
    grid = input.split("\n")
    dists = [[999_999 for _ in grid[0]] for _ in grid]
    start = tuple([0, 0])
    inside = 0

    # Find S
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "S":
                start = tuple([x, y])
                dists[y][x] = 0

    # Explore to map the loop
    explore(start, 0, grid, dists)

    # Travel loop again, marking inside and outside pieces
    explore_iteratively(start, grid, dists)

    # Find inside marker
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            dist = point_to_dist(tuple([x,y]), dists)
            if dist == -1: inside = -2
            elif dist == -2: inside = -1
            else: continue
            break
        break
    
    # Mark the remaining inside parts
    for y, line in enumerate(grid):
        mark = False
        for x, char in enumerate(line):
            if point_to_dist(tuple([x,y]), dists) == inside: mark = True
            elif point_to_dist(tuple([x,y]), dists) != 999_999: mark = False
            if mark and point_to_dist(tuple([x,y]), dists) == 999_999:
                set_point_dist(tuple([x,y]), inside, dists)

    # Print input with color:
    for y, line in enumerate(grid):
        print("")
        for x, char in enumerate(line):
            if dists[y][x] == -1:
                print('\033[94m' + "#" + '\033[0m', end="")
            elif dists[y][x] == -2:
                print('\033[92m' + "+" + '\033[0m', end="")
            elif dists[y][x] != 999_999:
                print('\033[91m' + char + '\033[0m', end="")
            else:
                print(char, end="")
    print("")

    return {
        "#": len([i for i in itertools.chain(*dists) if i == -1]),
        "+": len([i for i in itertools.chain(*dists) if i == -2])
    }


if __name__ == "__main__":
    with open(f"data/inputs/10.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

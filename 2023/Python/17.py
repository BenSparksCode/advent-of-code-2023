# Advent of Code 2023 - Day 17

import sys
from typing import List, Tuple


# My brother in Christ, you are running on an M2 Max
sys.setrecursionlimit(50000)

UP, RIGHT, DOWN, LEFT = 1, 2, 3, 4
min_loss_map = {}
lowest_loss = 120
w = 0
h = 0

curr_rec = 0
rec_lim = 10_000_000


def explore(pos: Tuple[int, int], dir: int, curr_loss: int, same_move_cnt: int, grid: List[List[int]]):
    global lowest_loss, min_loss_map, curr_rec, rec_lim
    if curr_rec > rec_lim: return
    curr_rec += 1
    
    print("Pos:", pos, "Loss:", curr_loss)

    # TODO improve: abandon if manhattan_dist + loss so far > min_loss
    # abandon path if more loss than lowest so far
    if curr_loss >= lowest_loss: return

    # Store path as best if end reached
    if pos[0] == w - 1 and pos[1] == h - 1:
        lowest_loss = curr_loss
        return
    
    if pos in min_loss_map:
        if curr_loss >= min_loss_map[pos]: return
    else: min_loss_map[pos] = curr_loss

    # Move in all possible directions
    moves = get_moves(pos, dir, same_move_cnt)
    for m in moves:
        new_move_cnt = same_move_cnt + 1 if dir == m[1] else 1
        explore(m[0], m[1], curr_loss + pos_to_loss(m[0], grid), new_move_cnt, grid)

    return


def get_moves(pos: Tuple[int, int], dir: int, same_move_cnt: int) -> List[Tuple[Tuple[int, int], int]]:
    global w, h
    dirs = [UP, RIGHT, DOWN, LEFT]
    moves = [] # [(x,y), dir]
    if same_move_cnt >= 3: dirs.pop(dir - 1) # remove current dir if too many moves in that dir

    # TODO Sort for closest to 2.5 (bottom right direction)
    dirs.sort(key=dist_to_corner, reverse=False)
    # print(dirs)

    for d in dirs:
        if abs(d - dir) == 2: continue
        if d == UP and pos[1] > 0: moves.append(tuple([tuple([pos[0], pos[1] - 1]), d]))
        if d == RIGHT and pos[0] < w - 1: moves.append(tuple([tuple([pos[0] + 1, pos[1]]), d]))
        if d == DOWN and pos[1] < h - 1: moves.append(tuple([tuple([pos[0], pos[1] + 1]), d]))
        if d == LEFT and pos[0] > 0: moves.append(tuple([tuple([pos[0] - 1, pos[1]]), d]))

    return moves

def pos_to_loss(pos: Tuple[int, int], grid: List[List[int]]) -> int:
    return grid[pos[1]][pos[0]]

def dist_to_corner(d: int): return abs(d - 2.5)


# TODO use dict to store loss to reach each tile
# End if loss to reach tile is > best attempt
def part_one(input):
    grid = [[int(j) for j in list(i)] for i in input.split("\n")]
    global w, h
    w, h = len(grid[0]), len(grid)

    print(grid)

    explore(tuple([0,0]), RIGHT, 0, 1, grid)


    return lowest_loss


def part_two(input):
    return None


if __name__ == "__main__":
    with open(f"data/2023/inputs/17.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

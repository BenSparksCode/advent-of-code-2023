# Advent of Code 2023 - Day 17

import sys
from typing import List, Tuple
import heapq


# My brother in Christ, you are running on an M2 Max
sys.setrecursionlimit(50000)

UP, RIGHT, DOWN, LEFT = 1, 2, 3, 4
min_loss_map = {}
lowest_loss = 999_999
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
        explore(m[0], m[1], curr_loss + pos_to_tile_loss(m[0], grid), new_move_cnt, grid)

    return


def get_moves(pos: Tuple[int, int], dir: int, dir_cnt: int) -> List[Tuple[Tuple[int, int], int]]:
    global w, h
    dirs = [UP, RIGHT, DOWN, LEFT]
    moves = [] # [(x,y), dir]
    if dir_cnt >= 3: dirs.pop(dir - 1) # Exclude same dir move if too many in current dir

    for d in dirs:
        if abs(d - dir) == 2: continue # Exclude backwards move
        if d == UP and pos[1] > 0: moves.append(tuple([tuple([pos[0], pos[1] - 1]), d]))
        if d == RIGHT and pos[0] < w - 1: moves.append(tuple([tuple([pos[0] + 1, pos[1]]), d]))
        if d == DOWN and pos[1] < h - 1: moves.append(tuple([tuple([pos[0], pos[1] + 1]), d]))
        if d == LEFT and pos[0] > 0: moves.append(tuple([tuple([pos[0] - 1, pos[1]]), d]))

    return moves

def pos_to_tile_loss(pos: Tuple[int, int], grid: List[List[int]]) -> int:
    return grid[pos[1]][pos[0]]

def pos_and_dir_to_cumulative_cost(pos: Tuple[int, int], dir: int, cost_grid: List[List[List[int]]]) -> int:
    return cost_grid[pos[1]][pos[0]][dir - 1]

def pos_dir_cnt_to_cumulative_cost(pos: Tuple[int, int], dir: int, cnt: int, cost_grid: List[List[List[List[int]]]]) -> int:
    return cost_grid[pos[1]][pos[0]][cnt - 1][dir - 1]

def dist_to_corner(d: int): return abs(d - 2.5)


def djikstra(grid: List[List[int]], cost_grid: List[List[List[List[int]]]]):
    min_heap = [(0, (0,0), RIGHT, 1)] # (cost, (x,y), dir, dir_cnt)

    while min_heap:
        cost, pos, dir, dir_cnt = heapq.heappop(min_heap)
        moves = get_moves(pos, dir, dir_cnt)

        # TODO update to cost[y][x][cnt][d] form
        for m in moves:
            new_cost = cost + pos_to_tile_loss(m[0], grid)
            new_dir_cnt = dir_cnt + 1 if dir == m[1] else 1
            # TODO update to allow cnt of x to overwrite costs of cells == or with higher cnt than selves
            if new_cost < pos_dir_cnt_to_cumulative_cost(m[0], m[1], new_dir_cnt, cost_grid):
                cost_grid[m[0][1]][m[0][0]][new_dir_cnt - 1][m[1] - 1] = new_cost
                for cnt_i in range(new_dir_cnt + 1, 4): # cnt:2 overwrites 2 and 3 cnts
                    if new_cost < pos_dir_cnt_to_cumulative_cost(m[0], m[1], cnt_i, cost_grid):
                        cost_grid[m[0][1]][m[0][0]][cnt_i - 1][m[1] - 1] = new_cost
                heapq.heappush(min_heap, (new_cost, m[0], m[1], new_dir_cnt))
    return


# TODO use dict to store loss to reach each tile
# End if loss to reach tile is > best attempt
def part_one(input):
    grid = [[int(j) for j in list(i)] for i in input.split("\n")]
    global w, h
    w, h = len(grid[0]), len(grid)
    max_c = 999_999

    # NOTE OLD version
    # explore(tuple([0,0]), RIGHT, 0, 1, grid)

    # NEW: Djikstra vibes

    cost_grid = [[[[max_c]*4]*3 for _ in line] for line in grid]
    cost_grid[0][0] = [[max_c,0,max_c,max_c], [max_c,0,max_c,max_c], [max_c,0,max_c,max_c]]

    print(cost_grid[0][0])
    print(cost_grid[1][1][0][3])

    djikstra(grid, cost_grid)


    # Testing get_moves:
    # moves = get_moves((2,0), RIGHT, 3)
    # print(moves)
    # moves = get_moves(moves[0][0], moves[0][1], 1)
    # print(moves)

    # print(pos_and_dir_to_cumulative_cost((0,0), RIGHT, cost_grid))
    # print(pos_and_dir_to_cumulative_cost((0,0), UP, cost_grid))


    # print()
    # for i in cost_grid:
    #     print()
    #     for j in i:
    #         j = [x if x != max_c else (-1) for x in j]
    #         print(j, end="   \t")
    # print()

    print(cost_grid[h - 1][w - 1])

    return lowest_loss


def part_two(input):
    return None


if __name__ == "__main__":
    with open(f"data/2023/inputs/17.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

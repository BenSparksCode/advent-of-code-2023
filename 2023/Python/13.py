# Advent of Code 2023 - Day 13

from typing import List

def get_row_scores(grid: List[str]) -> List[int]:
    scores = []
    for r in grid:
        curr_score = 0
        for x, c in enumerate(r):
            if c == "#": curr_score += 2 * (10 ** x)
            else: curr_score += 1 * (10 ** x)
        scores.append(curr_score)
    return scores

def get_col_scores(grid: List[str]) -> List[int]:
    scores = []
    for x in range(len(grid[0])):
        curr_score = 0
        for y in range(len(grid)):
            if grid[y][x] == "#": curr_score += 2 * (10 ** y)
            else: curr_score += 1 * (10 ** y)
        scores.append(curr_score)
    return scores

def find_reflection_start(scores: List[int]) -> int:
    for i in range(1,len(scores)):
        side1 = scores[:i][::-1]
        side2 = scores[i:]
        mirror = True
        for j in range(min(len(side1), len(side2))):
            if side1[j] != side2[j]:
                mirror = False
                break
        if mirror: return i
    return -1 # if no mirror found

def find_reflection_start_with_smudge(scores: List[int]) -> int:
    for i in range(1,len(scores)):
        side1 = scores[:i][::-1]
        side2 = scores[i:]
        diffSum = 0
        for j in range(min(len(side1), len(side2))):
            # All zeroes must be removed from abs diffs. 100 -> 1
            if side1[j] == side2[j]: continue
            diffSum += int(str(abs(side1[j] - side2[j])).replace("0", ""))
            if diffSum > 1:
                break
        if diffSum == 1: return i
    return -1 # if no mirror found


def part_one(input):
    patterns = input.split("\n\n")
    patterns = [p.split("\n") for p in patterns]
    total = 0

    for p in patterns:
        rows = get_row_scores(p)
        row_mirror = find_reflection_start(rows)
        if row_mirror != -1:
            total += row_mirror * 100
            continue
        cols = get_col_scores(p)
        col_mirror = find_reflection_start(cols)
        if col_mirror != -1:
            total += col_mirror

    return total


def part_two(input):
    patterns = input.split("\n\n")
    patterns = [p.split("\n") for p in patterns]
    total = 0

    for p in patterns:
        rows = get_row_scores(p)
        row_mirror = find_reflection_start_with_smudge(rows)
        if row_mirror != -1:
            total += row_mirror * 100
            continue
        cols = get_col_scores(p)
        col_mirror = find_reflection_start_with_smudge(cols)
        if col_mirror != -1:
            total += col_mirror

    return total


if __name__ == "__main__":
    with open(f"data/2023/inputs/13.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

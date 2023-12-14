# Advent of Code 2023 - Day 3

import re

def check_adjacent_to_symbol(startX, endX, numY, grid) -> bool:
    for x in range(startX - 1, endX + 2):
        for y in range(numY - 1, numY + 2):
            # check if char inside grid
            if (x >= 0 and x <= len(grid[0]) - 1) and (y >= 0 and y <= len(grid) - 1):
                if not grid[y][x].isdigit() and grid[y][x] != ".":
                    return True
    return False

# Returns 1 index included in each adjacent num, or -1 if not found
def get_adjacent_num_indices(xGear, yGear, grid) -> (int, int):
    index1, index2 = -1, -1
    for x in range(xGear - 1, xGear + 2):
        for y in range(yGear - 1, yGear + 2):
            # indices must be inside grid
            if (x >= 0 and x <= len(grid[0]) - 1) and (y >= 0 and y <= len(grid) - 1):
                if grid[y][x].isdigit():
                    currentIndex = y * len(grid[0]) + x
                    # update index1 if part of the same number
                    if index1 == -1 or currentIndex - index1 == 1:
                        index1 = currentIndex
                    else:
                        index2 = currentIndex
    return index1, index2

# Finds the full number in the original text string that includes a given char index
def index_to_number(index, string) -> int:
    string = string.replace("\n","")
    for match in re.finditer(r'\d+', string):
        if match.start() <= index < match.end():
            return int(match.group())
    return None

def part_one(input):
    grid = input.split("\n")
    total = 0

    for y, line in enumerate(grid):
        num = 0
        numStartX = 0
        for x, char in enumerate(line):
            if char.isdigit():
                if num != 0:
                    num = (num * 10) + int(char)
                else:
                    numStartX = x
                    num = int(char)

                # look ahead to see if full number is found
                # if not a digit OR if end of line
                if x + 1 == len(line) or not line[x + 1].isdigit():
                    if check_adjacent_to_symbol(numStartX, x, y, grid):
                        total += num
                        num = 0
                        numStartX = 0

            # clear last num stuff if no digit found
            else:
                num = 0
                numStartX = 0

    return total

def part_two(input):
    grid = input.split("\n")
    total = 0

    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "*":
                index1, index2 = get_adjacent_num_indices(x, y, grid)
                if index1 == -1 or index2 == -1: continue
                total += index_to_number(index1, input) * index_to_number(index2, input)

    return total

if __name__ == "__main__":
    with open(f"data/inputs/03.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

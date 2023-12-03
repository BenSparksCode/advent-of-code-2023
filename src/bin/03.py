# Advent of Code 2023 - Day 3

def check_adjacent_to_symbol(startX, endX, numY, grid):
    for x in range(startX - 1, endX + 2):
        for y in range(numY - 1, numY + 2):
            # check if char inside grid
            if (x >= 0 and x <= len(grid[0]) - 1) and (y >= 0 and y <= len(grid) - 1):
                if not grid[y][x].isdigit() and grid[y][x] != ".":
                    return True
    return False

def part_one(input):
    grid = input.split("\n")
    total = 0

    # Traverse through, finding full number
    for y, line in enumerate(grid):
        num = 0
        numStartX = 0
        for x, char in enumerate(line):
            
            # build number as we go
            if char.isdigit():
                # expand existing num found
                if num != 0:
                    num = (num * 10) + int(char)
                # new num found
                else:
                    numStartX = x
                    num = int(char)

                # look ahead to see if full number is found
                # if not a digit OR if end of line
                if x + 1 == len(line) or not line[x + 1].isdigit():
                    # found full num, check if adjacent to a symbol
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
    return None

if __name__ == "__main__":
    with open(f"data/inputs/03.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

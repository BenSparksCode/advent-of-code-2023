# Advent of Code 2023 - Day 11

from functools import reduce

def part_one(input):
    grid = input.split("\n")
    tempGrid = []
    galaxies = []
    dists = []

    # Expand rows (horizontal)
    for line in grid:
        if "#" not in line:
            tempGrid.append(line)
        tempGrid.append(line)
    grid, tempGrid = tempGrid, [[] for _ in tempGrid]

    # Expand columns (vertical)
    for x in range(len(grid[0])):
        emptyLine = True
        for line in grid:
            if "#" in line[x]:
                emptyLine = False
                break
        for y, line in enumerate(tempGrid):
            if emptyLine:
                tempGrid[y].append(".")
            tempGrid[y].append(grid[y][x])
    grid = tempGrid

    # Find coords of all galaxies
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "#": galaxies.append(tuple([x,y]))

    # Find Manhattan distance between all galaxies
    for i, g in enumerate(galaxies):
        for j in range(i + 1, len(galaxies)):
            dists.append(abs(g[0] - galaxies[j][0]) + abs(g[1] - galaxies[j][1]))

    return sum(dists)


def part_two(input):
    grid = input.split("\n")
    scale = 1_000_000
    emptyRows = []
    emptyCols = []
    galaxies = []
    dists = []

    # Find indices of empty rows
    for y, line in enumerate(grid):
        if "#" not in line:
            emptyRows.append(y)

    # Find indices of empty columns
    for x in range(len(grid[0])):
        emptyLine = True
        for line in grid:
            if line[x] == "#":
                emptyLine = False
                break
        if emptyLine: emptyCols.append(x)

    # Find coords of all galaxies
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "#":
                # For each empty row/col before the galaxy, actual dim = dim + emptyCount * (scale - 1)
                expandX = x + (reduce(lambda acc, col: acc + (col < x), emptyCols, 0) * (scale - 1))
                expandY = y + (reduce(lambda acc, row: acc + (row < y), emptyRows, 0) * (scale - 1))
                galaxies.append(tuple([expandX,expandY]))

    # Find Manhattan distance between all galaxies
    for i, g in enumerate(galaxies):
        for j in range(i + 1, len(galaxies)):
            dists.append(abs(g[0] - galaxies[j][0]) + abs(g[1] - galaxies[j][1]))

    return sum(dists)


if __name__ == "__main__":
    with open(f"data/inputs/11.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

# Advent of Code 2023 - Day 11

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
    return None

if __name__ == "__main__":
    with open(f"data/inputs/11.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

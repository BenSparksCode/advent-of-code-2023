
# Advent of Code 2023 - Day 1

def part_one(input):
    total = 0

    # Iterate through each line in text file
    for line in input.split("\n"):
        lineNum = 0

        # Search from left
        for c in line:
            if c.isdigit():
                # insert leftmost digit as tens digit
                lineNum += int(c)*10
                break

        # Search from right
        for c in line[::-1]:
            if c.isdigit():
                # insert rightmost digit as units digit
                lineNum += int(c)
                break

        total += lineNum
        
    return total

def part_two(input):
    return None

if __name__ == "__main__":
    with open(f"data/inputs/01.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

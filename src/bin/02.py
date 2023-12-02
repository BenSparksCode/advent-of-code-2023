# Advent of Code 2023 - Day 2
import re

def check_num_color_valid(numColor: str) -> bool: 
    redLimit = 12
    greenLimit = 13
    blueLimit = 14

    if (re.search("blue", numColor)):
        if blueLimit < int(numColor.replace("blue", "").strip()): return False
    if (re.search("green", numColor)):
        if greenLimit < int(numColor.replace("green", "").strip()): return False
    if (re.search("red", numColor)):
        if redLimit < int(numColor.replace("red", "").strip()): return False

    return True

def part_one(input):
    total = 0

    for line in input.split("\n"):
        lineParts = line.split(":")
        game = int(lineParts[0][5:])
        rounds = lineParts[1].split(";")
        gameValid = True

        for round in rounds:
            if not gameValid: break

            for numColor in round.split(", "):
                if not check_num_color_valid(numColor):
                    gameValid = False
                    break
            
        if gameValid: total += game
        
    return total

def part_two(input):
    return None

if __name__ == "__main__":
    with open(f"data/inputs/02.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

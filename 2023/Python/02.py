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

def get_max_num_by_color(gameRounds: str, color: str) -> int:
    if color not in gameRounds: return 0
    maxNum = 0 
    colorSightings = gameRounds.split(color)
    colorSightingsCount = gameRounds.count(color)
    for i, colorSplitStr in enumerate(colorSightings):
        # Only take left of color word, so might have extra right item after last color sighting
        if i == colorSightingsCount: break
        # Take last 3 chars of the sighting - should be number and maybe spaces
        if maxNum < int(colorSplitStr[-3:].strip()): maxNum = int(colorSplitStr[-3:].strip())
    
    return maxNum

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
    total = 0

    for line in input.split("\n"):
        lineParts = line.split(":")
        allRounds = lineParts[1]

        maxGreen = get_max_num_by_color(allRounds, "green")
        maxBlue = get_max_num_by_color(allRounds, "blue")
        maxRed = get_max_num_by_color(allRounds, "red")
            
        total += maxGreen * maxBlue * maxRed
        
    return total

if __name__ == "__main__":
    with open(f"data/inputs/02.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

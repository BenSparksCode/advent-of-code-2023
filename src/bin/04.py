# Advent of Code 2023 - Day 4

def part_one(input):
    lines = input.split("\n")
    total = 0

    for line in lines:
        [winNumbers, guesses] = line.split(":")[1].split("|")
        winNumbers = [int(i.strip()) for i in winNumbers.split(" ") if len(i) > 0]
        guesses = [int(i.strip()) for i in guesses.split(" ") if len(i) > 0]
        correctGuesses = 0
        for guess in guesses:
            if guess in winNumbers: correctGuesses += 1

        if correctGuesses > 0: total += 2 ** (correctGuesses - 1)

    return total

def part_two(input):
    return None

if __name__ == "__main__":
    with open(f"data/inputs/04.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

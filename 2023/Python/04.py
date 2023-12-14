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
    lines = input.split("\n")
    cardCounts = {} # stores counts as cardNum : cardCount

    for i, line in enumerate(lines, start=1):
        # Add 1 per card for original card
        cardCounts[i] = 1 if i not in cardCounts else cardCounts[i] + 1

        # Find number of matches within a card
        [winNumbers, guesses] = line.split(":")[1].split("|")
        winNumbers = [int(i.strip()) for i in winNumbers.split(" ") if len(i) > 0]
        guesses = [int(i.strip()) for i in guesses.split(" ") if len(i) > 0]
        correctGuesses = 0
        for guess in guesses:
            if guess in winNumbers: correctGuesses += 1

        # Adding new cards per existing card in the dictionary
        for guess_i in range(i + 1, i + 1 + correctGuesses):
            if guess_i > len(lines): break
            cardCounts[guess_i] = cardCounts[i] if guess_i not in cardCounts else cardCounts[guess_i] + cardCounts[i]

    return sum(cardCounts.values())

if __name__ == "__main__":
    with open(f"data/2023/inputs/04.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

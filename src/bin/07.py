# Advent of Code 2023 - Day 7

import itertools

# Remap letter cards for ascii value order
trans = str.maketrans({
    'T': 'A',
    'J': 'B',
    'Q': 'C',
    'K': 'D',
    'A': 'E'
})

def hand_value(hand) -> int:
    score = 0
    for i in range(0, 10, 2):
        score += ord(hand[0][4 - int(i/2)]) * 10 ** i
    return score

def part_one(input):
    lines = input.translate(trans).split("\n")
    hands = [tuple(i.split(" ")) for i in lines] 
    hand_groups = [[] for _ in range(7)]
    hand_count = len(hands)
    total = 0

    for hand in hands:
        char_counts = {}
        for c in hand[0]:
            char_counts[c] = 1 if c not in char_counts else char_counts[c] + 1
        vals = sorted(char_counts.values(), reverse=True)

        # Five of a kind
        if vals[0] == 5: hand_groups[0].append(hand)
        # Four of a kind
        elif vals[0] == 4: hand_groups[1].append(hand)
        # Full house
        elif vals[0] == 3 and vals[1] == 2: hand_groups[2].append(hand)
        # Three of a kind
        elif vals[0] == 3: hand_groups[3].append(hand)
        # Two pair
        elif vals[0] == 2 and vals[1] == 2: hand_groups[4].append(hand)
        # One pair
        elif vals[0] == 2: hand_groups[5].append(hand)
        # High card
        else: hand_groups[6].append(hand)

    for group in hand_groups:
        group.sort(key=hand_value, reverse=True)

    for i, hand in enumerate(list(itertools.chain(*hand_groups))):
        total += int(hand[1]) * (hand_count - i)

    return total

def part_two(input):
    return None

if __name__ == "__main__":
    with open(f"data/inputs/07.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

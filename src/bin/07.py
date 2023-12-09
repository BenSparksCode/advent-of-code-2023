# Advent of Code 2023 - Day 7

import itertools
from collections import Counter

# Remap letter cards for ascii value order
trans1 = str.maketrans({
    'T': 'A',
    'J': 'B',
    'Q': 'C',
    'K': 'D',
    'A': 'E',
})

trans2 = str.maketrans({
    'T': 'A',
    'J': '1', # J is now weaker than 2
    'Q': 'C',
    'K': 'D',
    'A': 'E',
})

def hand_value(hand) -> int:
    score = 0
    for i in range(0, 10, 2):
        score += ord(hand[0][4 - int(i/2)]) * 10 ** i
    return score

def part_one(input):
    lines = input.translate(trans1).split("\n")
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
    lines = input.translate(trans2).split("\n")
    hands = [tuple(i.split(" ")) for i in lines] 
    hand_groups = [[] for _ in range(7)]
    hand_count = len(hands)
    total = 0

    for hand in hands:
        char_counts = Counter(hand[0])
        chars_and_counts = sorted([(k,v) for k, v in char_counts.items()], key = lambda x: x[1], reverse=True)
        js = 0 if "1" not in char_counts else char_counts["1"]
        others = [i for i in chars_and_counts if i[0] != "1"]

        # If 5 Js, or only Js and 1 other char, end early here
        if len(others) <= 1:
            hand_groups[0].append(hand)
            continue

        # Only care about 1st and 2nd most counts of chars
        first, second = others[0][1] + js, others[1][1]

        # Five of a kind
        if first == 5: hand_groups[0].append(hand)
        # Four of a kind
        elif first == 4: hand_groups[1].append(hand)
        # Full house
        elif first == 3 and second == 2: hand_groups[2].append(hand)
        # Three of a kind
        elif first == 3: hand_groups[3].append(hand)
        # Two pair
        elif first == 2 and second == 2: hand_groups[4].append(hand)
        # One pair
        elif first == 2: hand_groups[5].append(hand)
        # High card
        else: hand_groups[6].append(hand)

    for group in hand_groups:
        group.sort(key=hand_value, reverse=True)

    for i, hand in enumerate(list(itertools.chain(*hand_groups))):
        total += int(hand[1]) * (hand_count - i)

    return total

if __name__ == "__main__":
    with open(f"data/inputs/07.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

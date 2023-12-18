# Advent of Code 2023 - Day 15

from functools import reduce
from typing import List, Tuple

def hash(word: str) -> int:
    res = 0
    for c in word:
        res = ((res + ord(c)) * 17) % 256
    return res

def box_operation(box: List[Tuple[str, int]], label: str, focal: int, op: str) -> List[Tuple[str, int]]:
    lens_found = False
    for i, l in enumerate(box):
        if label == l[0]:
            if op == "=": box[i] = tuple([label, focal])
            else: box.pop(i)
            lens_found = True
            break
    if not lens_found:
        if op == "=": box.append(tuple([label, focal]))
    return box


def part_one(input):
    steps = input.split(",")
    return reduce(lambda acc, step: acc + hash(step), steps, 0)


def part_two(input):
    steps = input.split(",")
    boxes = [[] for _ in range(256)]
    total = 0
    for step in steps:
        if "=" in step:
            [label, focal] = step.split("=")
            box_index = hash(label)
            box = boxes[box_index]
            boxes[box_index] = box_operation(box, label, focal, "=")
        else:
            label = step.split("-")[0]
            box_index = hash(label)
            box = boxes[box_index]
            boxes[box_index] = box_operation(box, label, 0, "-")
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            total += (i+1) * (j+1) * int(lens[1])
    return total


if __name__ == "__main__":
    with open(f"data/2023/inputs/15.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

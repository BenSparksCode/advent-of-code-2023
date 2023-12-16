# Advent of Code 2023 - Day 12

from typing import List
from functools import reduce

def is_valid(proposed: str, groups: List[int]) -> bool:
    prop_groups = [i for i in proposed.split(".") if len(i) > 0]
    if len(prop_groups) != len(groups): return False
    for i, g_len in enumerate(groups):
        if len(prop_groups[i]) != g_len: return False
    return True

def is_valid_so_far_dot_end(proposed: str, groups: List[int]) -> bool:
    prop_groups = [i for i in proposed.split(".") if len(i) > 0]
    if len(prop_groups) == 0: return True
    if len(prop_groups) > len(groups): return False
    if len(prop_groups[-1]) != groups[len(prop_groups) - 1]: return False
    return True

def is_valid_so_far_hash_end(proposed: str, groups: List[int]) -> bool:
    prop_groups = [i for i in proposed.split(".") if len(i) > 0]
    if len(prop_groups) == 0: return True
    if len(prop_groups) > len(groups): return False
    if len(prop_groups[-1]) > groups[len(prop_groups) - 1]: return False
    return True

def count_valid_orders(template: str, groups: List[int]) -> int:
    len_full = len(template)
    hash_total = sum(groups)
    max_dots = len_full - hash_total
    # start the combos off
    combos = [".", "#"] if template[0] == "?" else [template[0]]
    for c in template[1:]:
        if c != "?": combos = [combo + c for combo in combos]
        else:
            combos = (
            [combo + "." for combo in combos if combo.count(".") < max_dots]
            + [combo + "#" for combo in combos if combo.count("#") < hash_total])
    return reduce(lambda acc, g: acc + is_valid(g, groups), combos, 0)

def count_valid_orders2(template: str, groups: List[int]) -> int:
    len_full = len(template)
    hash_total = sum(groups)
    max_dots = len_full - hash_total

    # start the combos off
    combos = [".", "#"] if template[0] == "?" else [template[0]]

    # start with . and # count restrictions, then relax for speed
    for c in template[1:]:
        tempCombos = []
        for combo in combos:
            if c == ".":
                if combo.count(".") < max_dots:
                    proposed = combo + "."
                    if is_valid_so_far_dot_end(proposed, groups): tempCombos.append(proposed)
            elif c == "#":
                if combo.count("#") < hash_total:
                    proposed = combo + "#"
                    if is_valid_so_far_hash_end(proposed, groups): tempCombos.append(proposed)
            else:
                if combo.count(".") < max_dots: 
                    proposed = combo + "."
                    if is_valid_so_far_dot_end(proposed, groups): tempCombos.append(proposed)
                if combo.count("#") < hash_total:
                    proposed = combo + "#"
                    if is_valid_so_far_hash_end(proposed, groups): tempCombos.append(proposed)

        if len(tempCombos) > 0: combos = tempCombos

    res = len(combos)
    print(res, "for template:", template)
    return res


def part_one(input):
    # Line format: ("XX", [a,b,c])
    lines = [tuple(line.split(" ")) for line in input.split("\n")]
    lines = [tuple([line[0], [int(i) for i in line[1].split(",")]]) for line in lines]
    return reduce(lambda acc, line: acc + count_valid_orders2(*line), lines, 0)


def part_two(input):
    # Expand line to: ("XX?XX?XX?XX?XX", [a,b,c,a,b,c,a,b,c,a,b,c,a,b,c])
    lines = [tuple(line.split(" ")) for line in input.split("\n")]
    lines = [tuple([line[0], [int(i) for i in line[1].split(",")]]) for line in lines]
    
    for i, line in enumerate(lines):
        newLine = (line[0] + "?") * 5
        newNums = line[1] * 5
        lines[i] = tuple([newLine[:len(newLine) - 1], newNums])

    return reduce(lambda acc, line: acc + count_valid_orders2(*line), lines, 0)


if __name__ == "__main__":
    with open(f"data/2023/inputs/12.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

# Advent of Code 2023 - Day 5

import multiprocessing
from typing import List, Tuple

# Interpolation Table
# +--------------------+-------------------+--------------------+--------------------+--------------------+--------------------+--------------------+
# |     seed<>soil     |    soil<>fert     |    fert<>water     |    water<>light    |    light<>temp     |    temp<>humid     |     humid<>loc     |
# +--------------------+-------------------+--------------------+--------------------+--------------------+--------------------+--------------------+
# | ((98,99), (50,51)) | ((15,51), (0,36)) | ((f1,f2), (w1,w2)) | ((w1,w2), (l1,l2)) | ((l1,l2), (t1,t2)) | ((t1,t2), (h1,h2)) | ((h1,h2), (l1,l2)) |
# +--------------------+-------------------+--------------------+--------------------+--------------------+--------------------+--------------------+
# Where each cell in the table is a tuple of 2 tuples, of 2 numbers
# E.g. ((seed_start, seed_end), (soil_start, soil_end))

# Types
CellType = Tuple[Tuple[int, int], Tuple[int, int]]
TableType = List[List[CellType]]

# Converts the input text file to a table of range rule lines
def get_ranges_tbl_from_input(input: str) -> List[List[str]]:
    lines = input.split("\n")[2:] # skip first 2 lines
    table = []
    curr_col = 0
    for line in lines:
        if ":" in line: table.append([])
        elif len(line) > 0: table[curr_col].append(line)
        else: curr_col += 1 
    return table

# Takes a table of same dimensions of output table
# Input table cells are each a line from the input txt
def build_table(rules_tbl: List[List[str]]) -> TableType:
    table = []
    for col_i, col in enumerate(rules_tbl):
        table.append([])
        for line in col:
            [to, frm, dist] = [int(num) for num in line.split(" ")]
            table[col_i].append(((frm, frm + dist - 1), (to, to + dist - 1)))
    return table

# NOTE: col_end must be 1 more than target column index for recursion to work
# E.g. Just converting with 1st col would take (val_start, 0, 1)
# E.g. Converting across full table would take (val_start, 0, len(table))
def convert_via_table(val_start: int, col_start: int, col_end: int, table: TableType) -> int:
    if col_start == col_end: return val_start

    # First check if value falls into rule
    for rule in table[col_start]:
        if rule[0][0] <= val_start <= rule[0][1]:
            val_start = rule[1][0] + (val_start - rule[0][0])
            return convert_via_table(val_start, col_start+1, col_end, table)

    # If no rule for value, map 1:1
    return convert_via_table(val_start, col_start+1, col_end, table)

# Function for multiprocessing
def find_lowest_loc_in_seed_range(args) -> int:
    lowest_loc = 99_999_999_999
    if len(args) != 3: return lowest_loc
    range_start, range_end, table = args
    for seed in range(range_start, range_end + 1):
        loc = convert_via_table(seed, 0, len(table), table)
        if loc < lowest_loc:
            lowest_loc = loc
            print("new lowest loc found:", lowest_loc)
    return lowest_loc


def part_one(input):
    seeds = [int(i) for i in input.split("\n")[0].split(" ")[1:]]
    table = build_table(get_ranges_tbl_from_input(input))
    lowest_loc = 99_999_999_999

    for seed in seeds:
        loc = convert_via_table(seed, 0, len(table), table)
        if loc < lowest_loc: lowest_loc = loc

    return lowest_loc


def part_two(input):
    seed_sets = [int(i) for i in input.split("\n")[0].split(" ")[1:]]
    table = build_table(get_ranges_tbl_from_input(input))
    args_list = [[] for i in range(int(len(seed_sets) / 2))]

    for i in range(0, int(len(seed_sets) / 2)):
        args_list[i] = [seed_sets[i * 2], seed_sets[i * 2] + seed_sets[(i * 2) + 1], table]

    with multiprocessing.Pool(processes=10) as pool:
        results = pool.map(find_lowest_loc_in_seed_range, args_list)
    
    return min(results)


if __name__ == "__main__":
    with open(f"data/2023/inputs/05.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))
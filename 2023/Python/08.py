# Advent of Code 2023 - Day 8

import math

def part_one(input):
    directions = input.split("\n")[0]
    lines = input.split("\n")[2:]

    nodes = {}
    curr_node = "AAA"
    steps = 0

    # Build hashmap of nodes
    for line in lines:
        k, v = line.split(" = ")
        nodes[k] = tuple(v.replace("(","").replace(")", "").split(", "))

    # Traverse the nodes until you get to ZZZ
    while(curr_node != "ZZZ"):
        for d in directions:
            if curr_node == "ZZZ": break
            steps += 1
            curr_node = nodes[curr_node][0] if d == "L" else nodes[curr_node][1]

    return steps

def part_two(input):
    # 6 XXAs and XXZs in my input
    directions = input.split("\n")[0]
    lines = input.split("\n")[2:]

    nodes = {}
    curr_nodes = []
    nodes_steps = []

    # Build hashmap of nodes
    for line in lines:
        k, v = line.split(" = ")
        if k[2] == "A": curr_nodes.append(k)
        nodes[k] = tuple(v.replace("(","").replace(")", "").split(", "))

    # For each of the XXA nodes, find their XXZ path
    for node in curr_nodes:
        steps = 0
        found = False
        while(not found):
            for d in directions:
                if node[2] == "Z":
                    nodes_steps.append(steps)
                    found = True
                    break

                steps += 1
                node = nodes[node][0] if d == "L" else nodes[node][1]

    # Unpacks the list of steps with *, and calculates LCM of those numbers
    return math.lcm(*nodes_steps)    

if __name__ == "__main__":
    with open(f"data/2023/inputs/08.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

# Advent of Code 2023 - Day 8

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
    return None

if __name__ == "__main__":
    with open(f"data/inputs/08.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

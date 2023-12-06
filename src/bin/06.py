# Advent of Code 2023 - Day 6

def part_one(input):
    lines = input.split("\n")
    times = [int(i) for i in lines[0].split(":")[1].split(" ") if len(i) > 0]
    dists = [int(i) for i in lines[1].split(":")[1].split(" ") if len(i) > 0]
    prod = 1

    for time_i, time in enumerate(times):
        win_strats = 0
        for hold_time in range(time):
            if hold_time * (time - hold_time) > dists[time_i]: win_strats += 1
        prod *= win_strats

    return prod

def part_two(input):
    return None

if __name__ == "__main__":
    with open(f"data/inputs/06.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

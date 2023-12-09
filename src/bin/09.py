# Advent of Code 2023 - Day 9

# Recursive function to find next num in the sequence
def next_in_seq(nums) -> int:
    if len(set(nums)) == 1 and nums[0] == 0: return 0
    diffs = []
    for i, num in enumerate(nums):
        if i + 1 == len(nums): break
        diffs.append(nums[i + 1] - num)
    return nums[-1] + next_in_seq(diffs)

def part_one(input):
    lines = input.split("\n")
    total = 0

    for line in lines:
        nums = [int(i) for i in line.split(" ")]
        total += next_in_seq(nums)

    return total

def part_two(input):
    return None

if __name__ == "__main__":
    with open(f"data/inputs/09.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

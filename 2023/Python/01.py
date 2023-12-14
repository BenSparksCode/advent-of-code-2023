# Advent of Code 2023 - Day 1

def part_one(input):
    total = 0

    # Iterate through each line in text file
    for line in input.split("\n"):
        lineNum = 0

        # Search from left
        for c in line:
            if c.isdigit():
                # insert leftmost digit as tens digit
                lineNum += int(c)*10
                break

        # Search from right
        for c in line[::-1]:
            if c.isdigit():
                # insert rightmost digit as units digit
                lineNum += int(c)
                break

        total += lineNum

    return total

def part_two(input):
    numWords = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    total = 0

    # Iterate through each line in text file
    for line in input.split("\n"):
        lineNum = 0

        # SEARCH FROM LEFT
        wordFound = False
        # Search from left for first digit char
        for cIndex,c in enumerate(line):
            if wordFound: break

            # First search for num words
            # Search space of up to [1, 2, 3, 4, cIndex]
            for numWordStartPointer in range(max(cIndex - 5, 0), cIndex + 1):
                # Substring not long enough - search deeper into line
                if cIndex - numWordStartPointer + 1 <= 2: break
                if wordFound: break

                # Check each length option
                for wordLen in range(3,6):
                    if line[numWordStartPointer:numWordStartPointer + wordLen] in numWords:
                        # Remember to scale digit by 10 for left side search
                        lineNum += numWords[line[numWordStartPointer:numWordStartPointer + wordLen]] * 10
                        wordFound = True
                        break
            
            # If we find a digit after not finding any words, use digit and break
            if c.isdigit() and not wordFound:
                # insert leftmost digit as tens digit
                lineNum += int(c)*10
                break

        # SEARCH FROM RIGHT
        wordFound = False
        # Search from right
        reverseLine = line[::-1]
        for cIndex,c in enumerate(reverseLine):
            if wordFound: break

            # First search for num words
            # Start the end pointer deepest inside reversed line and move outwards
            for numWordEndPointer in range(cIndex + 1, max(cIndex - 2, 2), -1):
                if wordFound: break

                # Check each length possibility from the end pointer
                for wordLen in range(3,6):
                    # Earliest word can start is at start of reversed line
                    if numWordEndPointer + 1 - wordLen <= 0: break
                    if wordFound: break

                    # Calculating final possible num word string
                    re_reversedSubstring = reverseLine[max(numWordEndPointer - wordLen, 0):numWordEndPointer][::-1]
                    if re_reversedSubstring in numWords:
                        lineNum += numWords[re_reversedSubstring]
                        wordFound = True
                        break

            # If we find a digit after not finding any words, use digit and break
            if c.isdigit() and not wordFound:
                # insert rightmost digit as units digit
                lineNum += int(c)
                break

        # Add 2 digit result of each line to the final total
        total += lineNum

    return total

if __name__ == "__main__":
    with open(f"data/2023/inputs/01.txt", "r") as file:
        input_data = file.read().strip()
    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))

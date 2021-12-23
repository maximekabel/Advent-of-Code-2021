file = open("input.txt")
input = file.read().splitlines()


def part_one(input):
    input = [line[line.index("|") + 2 :].split() for line in input]
    count = 0
    for line in input:
        for digit in line:
            if len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7:
                count += 1
    return count


print("Part 1: " + str(part_one(input)))

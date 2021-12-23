file = open("input.txt")
input = file.read().strip().split(",")
input = [int(i) for i in input]


def part_one(input):
    # get median of the list
    # input.sort()
    # best_position = (input[len(input) // 2] + input[~(len(input) // 2)]) / 2

    # total_fuel = 0
    # for crab in input:
    #     # get distance of crab to median and add to total fuel
    #     total_fuel += abs(crab - best_position)
    #     return total_fuel
    fuel_burned = lambda a, b: abs(a - b)
    total_fuel = min([sum(fuel_burned(j, i) for j in input) for i in range(max(input))])
    return total_fuel


def part_two(input):
    fuel_burned = lambda a, b: abs(a - b) * (abs(a - b) + 1) // 2
    total_fuel = min([sum(fuel_burned(j, i) for j in input) for i in range(max(input))])
    return total_fuel


print("Part 1: " + str(part_one(input)))
print("Part 2: " + str(part_two(input)))

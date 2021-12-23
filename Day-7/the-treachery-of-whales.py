file = open("input.txt")
input = file.read().strip().split(",")
input = [int(i) for i in input]
print(input)


#get median of the list
input.sort()
best_position = (input[len(input)//2]+input[~(len(input)//2)])/2

total_fuel = 0
for crab in input:
    #get distance of crab to median and add to total fuel
    total_fuel += abs(crab-best_position)

print("Part 1:" + str(total_fuel))
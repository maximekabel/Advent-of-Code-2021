file = open("input.txt")
input = file.read().splitlines()
input = [k.split(' ') for k in input]
print(input)

horizontal_pos = 0
depth = 0

for i in input:
    if i[0] == "forward":
        horizontal_pos += int(i[1])
    elif i[0] == "up":
        depth -= int(i[1])
    elif i[0] == "down":
        depth += int(i[1])
print("Horizontal Position: " + str(horizontal_pos))
print("Depth: " + str(depth))
print("Final answer Part One: " + str(horizontal_pos*depth) + "!")

hpos2 = 0
depth2 = 0
aim = 0
for i in input:
    if i[0] == "forward":
        hpos2 += int(i[1])
        depth2 += aim * int(i[1])
    elif i[0] == "up":
        aim -= int(i[1])
    elif i[0] == "down":
        aim += int(i[1])

print("Horizontal Position: " + str(hpos2))
print("Depth: " + str(depth2))
print("Final answer Part Two: " + str(hpos2*depth2) + "!")

file = open("input.txt")
input = file.read().splitlines()
input = [int(k) for k in input]
increased = 0

for i in range(len(input)-1):
    if input[i] < input[i+1]:
        increased+=1

print("Part 1: "+str(increased))
######################################

increased2 = 0
for i in range(len(input)-3):
    if (input[i]+input[i+1]+input[i+2]) < (input[i+1]+input[i+2]+input[i+3]):
            increased2+=1
print("Part 2: "+str(increased2))

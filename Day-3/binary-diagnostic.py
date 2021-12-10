file = open("input.txt")
input = file.read().splitlines()
# input = [k.split(' ') for k in input]
# print(len(input))

gamma = ""
epsilon = ""
for i in range(12):
    ones = 0
    for entry in input:
        if entry[i] == "1":
            # print(entry[i])
            ones += 1
    if ones >= (len(input) / 2):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
print("gamma: " + gamma)
print("epsilon: " + epsilon)
print("Solution P1: " + str((int(gamma, 2) * int(epsilon, 2))))

################################################################
o2_input = input
for i in range(12):
    ones = 0
    zeros = 0
    for entry in o2_input:
        if entry[i] == "1":
            ones += 1
        else:
            zeros += 1
    # print(ones)
    # print(zeros)
    if ones >= zeros:
        o2_input = list(filter(lambda entry: int(entry[i]) == 1, o2_input))
        # print(o2_input)
    else:
        o2_input = list(filter(lambda entry: int(entry[i]) == 0, o2_input))
        # print(o2_input)


co2_input = input
for i in range(12):
    ones = 0
    zeros = 0
    for entry in co2_input:
        if entry[i] == "1":
            ones += 1
        else:
            zeros += 1

    # print("ones: " + str(ones))
    # print("zeros: " + str(zeros))
    if len(co2_input) == 1:
        break
    if ones >= zeros:
        co2_input = list(filter(lambda entry: int(entry[i]) == 0, co2_input))
        # print(co2_input)
    else:
        co2_input = list(filter(lambda entry: int(entry[i]) == 1, co2_input))
        # print(co2_input)

print(o2_input)
print(co2_input)

print("Solution P2: " + str(int(co2_input[0], 2) * int(o2_input[0], 2)))

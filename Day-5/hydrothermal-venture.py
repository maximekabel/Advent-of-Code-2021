file = open("input.ex")
input = file.read().splitlines()

lines = []
for line in input:
    line = line.split(' -> ')
    left = line[0].split(',')
    left = [int(i) for i in left]
    right = line[1].split(',')
    right = [int(i) for i in right]
    if left[0] == right[0] or left[1] == right[1]:
        lines.append([left,right])


# print(max([max([max(part) for part in row]) for row in lines]))
grid = [[0]*10 for i in range(10)]

for line in lines:
    if line[0][0] == line[1][0]:
        x = line[0][0]
        y = list(range(line[0][1], line[1][1]+1))
        for wye in y:
            grid[wye][x] +=1
            print(grid[wye][x])
    

    if line[0][1] == line[1][1]:
        x = list(range(line[0][0], line[1][0]+1))
        y = line[0][1]

        for ecks in x:
            grid[y][ecks] += 1
# print(grid)
count = 0
for i in grid:
    count += sum(j > 1 for j in i)
# print(count)

for line in grid:
    print(line)
file = open("/home/max/Documents/Projects/Advent-of-Code-2021/Day-4/input.txt")
input = file.read().splitlines()

bingo_cage = input.pop(0).split(",")
input.pop(0)

board_dict = {}
boards = []
row, col = 0, 0
bingo = False

for line in input:
    if line == "":
        board_dict["rows"] = [0, 0, 0, 0, 0]
        board_dict["cols"] = [0, 0, 0, 0, 0]
        board_dict["bingo"] = False
        boards.append(board_dict)
        board_dict = {}
        row, col = 0, 0
    else:
        this_line = line.split()
        for number in this_line:
            board_dict[number] = [row, col, False]
            col += 1
        row += 1
        col = 0


for number in bingo_cage:
    # print(number)
    for board in boards:
        if number in board:
            row = board[number][0]
            col = board[number][1]
            board[number] = [row, col, True]
            board["rows"][row] += 1
            board["cols"][col] += 1

            if board["rows"][row] == 5 or board["cols"][col] == 5:
                bingo = True
                board["bingo"] = True
                first_bingo = board
                print("worked")
                break

    sum_unmarked_numbers = 0
    # print(board)
    if bingo:
        for key in board:
            if not key == "bingo" or key == "rows" or key == "cols":
                if board[key][2] is False:
                    sum_unmarked_numbers += int(key)
        print(sum_unmarked_numbers)
        print(number)
        print("Part 1: " + str(sum_unmarked_numbers * int(number)))
        break

import copy
import numpy as np
# temp lists
boards = []
temp_list = []
# open file and get rows
with open("input.txt", "r") as file:
    sequence = file.readline()
    sequence = list(map(int, sequence.replace(",", " ").split()))

    for line in file:
        if line == "\n":
            for i in range(0, 5):
                row = file.readline().split()
                row = list(map(int, row))
                temp_list.append(row)
        boards.append(temp_list.copy())

        temp_list.clear()
# copy board list
board_copy = copy.deepcopy(boards)


def calc_sum(array, num):
    # print final score of board
    # smaller number wins
    b_sum = 0
    for row_ in array:
        for val in row_:
            if val != "x":
                b_sum += val
    print(f"Total score is {b_sum * num}")


board_1 = None
last_num = None
# should make this a function but w.e
# check rows to see if numbers match sequence
for num in sequence:
    for board in boards:
        # rows
        for value, row in enumerate(board):
            if num in row:
                row[row.index(num)] = "x"
                last_num = num
            if not board_1:
                if row == ["x"] * len(row):
                    board_1 = board
                    # print(board)
                    calc_sum(board_1, last_num)

# make numpy array to turn columns into rows
boards_deepcopy = np.array(board_copy)
board_cols = []
board_2 = None
# turn columns into rows
for board in boards_deepcopy:
    for i in range(5):
        temp_list.append([row[i] for row in board])
    board_cols.append(temp_list[:])
    temp_list.clear()

for num in sequence:
    for board in board_cols:
        # rows
        for value, row in enumerate(board):
            if num in row:
                row[row.index(num)] = "x"
                last_num = num
            if not board_2:
                if row == ["x"] * len(row):
                    board_2 = board
                    # print(board)
                    calc_sum(board_2, last_num)
# Total score is 35056
# Total score is 4662
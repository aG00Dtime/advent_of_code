
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

board_np_array = np.array(boards)
columns = []

# turn columns into rows
for board in board_np_array:
    for i in range(5):
        temp_list.append([row[i] for row in board])
    columns.append(temp_list[:])
    temp_list.clear()


# def calc score
def score(array, number):
    board_sum = 0
    for rows in array:
        for val in rows:
            if val != "x":
                board_sum += int(val)
    print(f"Score: {board_sum * number} ,The sum of the board was {board_sum} and the last number was {number}.")


# win bool
won = False
# winning board
winning_board = list()
# the last number that was pulled
last_number = None
# check sequence
for num in sequence:
    # check rows
    for index, board in enumerate(boards):
        for row in board:
            if num in row:
                # mark number if found
                row[row.index(num)] = "x"
            if row == ["x"] * 5:
                won = True
                winning_board = board
                last_number = num
                break
    # check columns
    for index, board_col in enumerate(columns):
        for row in board_col:
            if num in row:
                # mark number if found
                row[row.index(num)] = "x"
            if row == ["x"] * 5:
                won = True
                winning_board = board_col
                last_number = num
                break
    # break out if won
    if won:
        score(winning_board, last_number)
        break

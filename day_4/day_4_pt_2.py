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

# copy
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


# winning board
last_to_win = list()
winning_boards = [False for board in boards]
# print(winning_boards)
# the last number that was pulled
last_number = None
# check sequence
for num in sequence:
    # check rows
    for index, board in enumerate(boards):
        if not winning_boards[index]:
            for row in board:
                if num in row:
                    # mark number if found
                    row[row.index(num)] = "x"
                if row == ["x"] * 5:
                    winning_boards[index] = True
                    last_to_win = board
                    last_number = num

    # check columns
    for index, board_col in enumerate(columns):
        if not winning_boards[index]:
            for row in board_col:
                if num in row:
                    # mark number if found
                    row[row.index(num)] = "x"
                if row == ["x"] * 5:
                    winning_boards[index] = True
                    last_to_win = board_col
                    last_number = num

    # break out if won
    if all(winning_boards):
        score(last_to_win, last_number)
        # print(winning_boards)
        break

boards = []
temp_list = []

with open("input.txt", "r") as file:
    sequence = file.readline()
    sequence = list(map(int, sequence.replace(",", " ").split()))

    for line in file:
        if line == "\n":
            for i in range(0, 5):
                row = file.readline().split()
                row = list(map(int, row))
                temp_list.append(row)
        boards.append(temp_list[:])
        temp_list.clear()

winning_board = None
last_num = None
board_sum = 0

for num in sequence:
    for board in boards[:]:
        # rows
        for value, row in enumerate(board):
            if num in row:
                row[row.index(num)] = "x"
                last_num = num
                if row == ["x"] * len(row):
                    winning_board = board
                    for i in range(5):
                        print(board[i])

                    for rows in winning_board:
                        for nums in rows:
                            if nums != "x":
                                board_sum += nums

                    print(f"Last number is {last_num} and the sum of the board is {board_sum}")
                    print(f"Final score is {board_sum * last_num}")
                    exit()

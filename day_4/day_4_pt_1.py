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

for num in sequence:
    for nums, rows in enumerate(boards):
        if num in row:
            row[row.index(num)] = "found"
            if row == ["found"] * len(row):
                board = rows[num // len(row) * len(row): num // len(row) * len(row) + len(row)]
                print(board)
                del rows[num // len(row) * len(row): num // len(row) * len(row) + len(row)]


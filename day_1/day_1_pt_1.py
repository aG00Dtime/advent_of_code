# vars
prev_line = 0
next_line = 0
count = 0
# read file
with open("input.txt", "r") as file:
    # read line
    line = file.readlines()
    # iterate
    for i in range(0, len(line) - 1):
        prev_line = int(line[i].strip())
        next_line = int(line[i + 1].strip())
        # check
        if prev_line < next_line:
            count += 1
# print count
print(f'Total increased count is {count}')

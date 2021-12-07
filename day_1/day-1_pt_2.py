# vars
count = 0
set_of_3 = []
next_sum = 0
prev_sum = 0

# read file
with open("../day_1_pt2/input.txt", "r") as file:
    # read line
    line = file.readlines()
    # iterate
    for i in range(0, len(line) - 1):
        for j in range(0, 3):
            try:
                # get val from line
                val = int(line[(i + j)].strip())
                # add val to sum
                next_sum = next_sum + val
                # add to list to print
                set_of_3.append(val)
            # if values run out
            except IndexError:
                print("Not enough values remain")
        # check if values are a group of 3
        if len(set_of_3) == 3:
            # check if next sum of 3 is more than the previous
            if next_sum > prev_sum:
                print(f"Set: {set_of_3}: {next_sum} (Increased)")
                # increase count by 1 if it is
                count += 1
            else:
                print(f"Set: {set_of_3}: {next_sum} (Decreased)")
            # reset values
            set_of_3.clear()
            prev_sum = next_sum
            next_sum = 0
# print final count -1 since we don't check the first
print(count - 1)

# print count

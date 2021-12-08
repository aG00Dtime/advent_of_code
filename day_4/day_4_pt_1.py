final_list = []
temp_list = []

with open("input.txt", "r") as file:
    sequence = file.readline()
    sequence = list(map(int, sequence.replace(",", " ").split()))

    for line in file:

        if line == "\n":

            for i in range(0, 5):
                temp_list.append(file.readline().strip())

        # print(temp_list)
        final_list.append(temp_list[:])
        temp_list.clear()


for board in final_list:
    print(board)

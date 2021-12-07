from collections import Counter
# vars
temp = []
gamma_rate = []
epsilon_rate = []

with open("input.txt", "r") as file:
    numbers = file.readlines()

    i, j = 0, 0
    while j != len(numbers[0]) - 1:

        temp.append(numbers[i][j])
        i += 1

        if i >= len(numbers) - 1:
            i = 0
            j += 1

            most_common = Counter(temp).most_common(1)
            most_common, count = str(most_common).split(",", -1)
            most_common = most_common.replace("[('", '').replace("'", '')

            # ep rate is the opposite of gamma rate
            if int(most_common) > 0:
                epsilon_rate.append(0)

            else:
                epsilon_rate.append(1)

            gamma_rate.append(most_common)
            temp.clear()

# join ga rate
gamma_rate = (str(i) for i in gamma_rate)
gamma_rate = ("".join(gamma_rate))

# join ep rate
epsilon_rate = (str(i) for i in epsilon_rate)
epsilon_rate = ("".join(epsilon_rate))

# convert to dec
int_gamma_rate = int(gamma_rate, 2)
int_epsilon_rate = int(epsilon_rate, 2)

# print
print(f"Gamma rate = {int_gamma_rate}")
print(f"Epsilon rate = {int_epsilon_rate}")
print(f"Power consumption = {int_gamma_rate * int_epsilon_rate}")

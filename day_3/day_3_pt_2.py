# oxygen rating
# consider the first bit  and determine the most common value
# if 0 and 1 are equal , keep only 1s
# consider the remain numbers , and repeat step 2 until 1 digit remains
# the last digit is the value we need


# global vars
oxygen = None
co2 = None


# def recursive function to determine rating
def oxygen_rating(data, init_ind):
    global oxygen
    # vars
    common_temp = []
    common_bit = None
    common_count = {}
    # hold temp list of values
    new_data_temp = []

    # extract index into a list to check most common
    for line in data:
        common_temp.append(line[init_ind].strip())
    # count the frequency
    for val in common_temp:
        if val in common_count:
            common_count[val] += 1
        else:
            common_count[val] = 1
    # check for the common bit

    if common_count['0'] <= common_count['1']:
        common_bit = 1
    else:
        common_bit = 0

    # print(common_temp)
    # print(f"common_bit = {common_bit} - {common_count}")

    # create a new list with the values that begin with the most common
    for val in data:
        if val[init_ind] == str(common_bit):
            new_data_temp.append(val.strip())

    # inc index
    init_ind += 1
    # if index is at the end of the str value print and exit
    if init_ind == len(data[0]):
        # conv value
        dec_val = (str(i) for i in new_data_temp)
        dec_val = "".join(dec_val)
        dec_val = int(dec_val, 2)
        # print
        print(f"Oxygen generator rating is {new_data_temp} | {dec_val} ")
        oxygen = dec_val
        return

    else:
        # continue recursion
        oxygen_rating(new_data_temp, init_ind)


# def recursive function to determine rating
def co2_rating(data, init_ind):
    global co2
    # vars
    common_temp = []
    common_bit = None
    common_count = {}
    # hold temp list of values
    new_data_temp = []

    # extract index into a list to check most common
    for line in data:
        common_temp.append(line[init_ind].strip())
    # count the frequency
    for val in common_temp:
        if val in common_count:
            common_count[val] += 1
        else:
            common_count[val] = 1
    # check for the common bit

    if common_count['0'] <= common_count['1']:
        common_bit = 0
    else:
        common_bit = 1

    # print(common_temp)
    # print(f"common_bit = {common_bit} - {common_count}")

    # create a new list with the values that begin with the most common
    for val in data:
        if val[init_ind] == str(common_bit):
            new_data_temp.append(val.strip())

    # inc index
    init_ind += 1

    if common_bit == 0 and len(new_data_temp) == 1:
        # conv value
        dec_val = (str(i) for i in new_data_temp)
        dec_val = "".join(dec_val)
        dec_val = int(dec_val, 2)
        # print
        print(f"CO2 rating is {new_data_temp} | {dec_val} ")
        co2 = dec_val
        return

    co2_rating(new_data_temp, init_ind)


# open file and pass data to the function
with open("input.txt", "r") as file:
    file = file.readlines()
    # get oxygen rating
    # oxygen_rating(file, 0, 1)
    # get co2 rating
    oxygen_rating(file, 0)
    co2_rating(file, 0)

    print(f"Life support rating is {oxygen * co2}")

# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
# It increases your horizontal position by X units.
# It increases your depth by your aim multiplied by X.
# vars
horizontal_pos = 0
depth = 0
aim = 0
# open file
with open("input.txt", "r") as file:
    for line in file:
        # split string to get direction and values
        # eg. forward 5 == direction ='forward', val = 5
        direction, val = line.split(' ', -1)

        # calculate depth and horizontal pos and aim
        if direction == "forward":
            horizontal_pos += int(val)
            depth += (aim * int(val))

        elif direction == "up":
            aim -= int(val)

        elif direction == "down":
            aim += int(val)
# print
print(f"Horizontal Position of {horizontal_pos} and Depth of {depth}")
print(f"Horizontal Position * Depth is {horizontal_pos * depth}")
print(f"Aim = {aim}")

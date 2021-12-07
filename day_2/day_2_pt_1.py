# horizontal position and depth start @ 0
# up and down are depth
# forward increases horizontal position

# vars
horizontal_pos = 0
depth = 0
# open file
with open("input.txt", "r") as file:
    for line in file:
        # split string to get direction and values
        # eg. forward 5 == direction ='forward', val = 5
        direction, val = line.split(' ', -1)

        # calculate depth and horizontal pos
        if direction == "forward":
            horizontal_pos += int(val)

        elif direction == "up":
            depth -= int(val)

        elif direction == "down":
            depth += int(val)
# print
print(f"Horizontal Position of {horizontal_pos} and Depth of {depth}")
print(f"Horizontal Position * Depth is {horizontal_pos * depth}")
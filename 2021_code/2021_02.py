import aocd

input_list = aocd.get_data(day=2, year=2021).splitlines()

depth = 0
horizontal = 0

for i in input_list:
    i = i.split()
    if i[0] == 'up':
        depth -= int(i[1])
    elif i[0] == 'down':
        depth += int(i[1])
    elif i[0] == 'forward':
        horizontal += int(i[1])

print(horizontal * depth)

depth = 0
horizontal = 0
aim = 0

for i in input_list:
    i = i.split()
    if i[0] == 'up':
        aim -= int(i[1])
    elif i[0] == 'down':
        aim += int(i[1])
    elif i[0] == 'forward':
        horizontal += int(i[1])
        depth += aim * int(i[1])

print(horizontal * depth)